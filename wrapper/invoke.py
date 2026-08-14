#!/usr/bin/env python3
"""A24.2 invocation wrapper — the sole admissible path for AI invocations
in registered roles.

Implements amendment A24.2 (frozen at the wrapper freeze tag):

(a) Monotonic run IDs: KHI-RUN-NNNNNN, strictly increasing, derived under a
    process lock from the committed pre-invocation records in
    logs/invocations/.
(b) Pre-invocation commit: before any model call, a commit containing the
    run ID, prompt hash, model ID, and decoding settings is created AND
    pushed to the protected remote, and the wrapper verifies the remote
    branch head equals the local commit. Push failure => no invocation
    (the wrapper records an ABORTED_PRE_PUSH_FAILED result and exits).
(c) Post-invocation commit: immediately after return, error, abort, or
    timeout, the complete raw stdout/stderr byte streams are written,
    hashed, and committed with a result record, and the commit is pushed.
    A new registered invocation is refused while any prior run lacks a
    pushed result commit.
(d) No silent retries: the wrapper never retries a model call. A retry is
    a new run registered in logs/invocations/attempts.jsonl (the G5
    attempt register) with an explicit --retry-of and --retry-reason.

Manual direct invocations are inadmissible: only outputs carrying a
wrapper-produced record pair (pre + result, both pushed) may enter any
registered-role pathway.

Hashing conventions (documented for review):
- Structured records are hashed as SHA-256(JCS(record)) per A20.9
  (RFC 8785, UTF-8, no prefix/suffix/delimiter).
- Raw byte artifacts (prompt file, stdout, stderr) are hashed as SHA-256
  over their exact bytes; byte streams admit no serialization ambiguity,
  which is the property A20.9 exists to guarantee. The byte hashes are
  embedded in the JCS-hashed records.

Adapter contract: the adapter is an executable receiving one JCS-encoded
JSON object on stdin ({"run_id","role","model_id","decoding","prompt",
"inputs"}) and writing the complete raw model output to stdout, errors to
stderr. The wrapper treats adapter stdout/stderr as opaque bytes. Real
model adapters are admissible only after their A24.3 model manifest is
deposited; the dummy adapter is for wrapper selftests (role "selftest",
non-evidential) only.
"""

import argparse
import datetime
import fcntl
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import jcs  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INVOCATIONS_DIR = ROOT / "logs" / "invocations"
PROMPTS_DIR = ROOT / "logs" / "agent-prompts"
ATTEMPTS_LOG = INVOCATIONS_DIR / "attempts.jsonl"
LOCK_FILE = ROOT / ".invocation.lock"
BRANCH = "main"
REMOTE = "origin"

REGISTERED_ROLES = (
    "data-steward",
    "archival-triage",
    "transcription-keying",
    "scoring-executor",
    "red-team",
)
SELFTEST_ROLE = "selftest"  # non-evidential wrapper exercise; never registered
RUN_ID_RE = re.compile(r"^KHI-RUN-(\d{6})\.pre\.json$")
PUSH_ATTEMPTS = 3  # transport-level retries of `git push` only; never a model retry


class WrapperError(Exception):
    pass


def utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True,
        text=True,
        check=check,
    )


def write_record(path: pathlib.Path, record: dict) -> str:
    """Write a human-readable rendering; the record hash is over JCS(record),
    not the file bytes."""
    path.write_text(json.dumps(record, indent=2, sort_keys=True,
                               ensure_ascii=False) + "\n", encoding="utf-8")
    return jcs.sha256_jcs(record)


def load_record(path: pathlib.Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def acquire_lock():
    fd = os.open(LOCK_FILE, os.O_CREAT | os.O_RDWR, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        raise WrapperError(
            "another wrapper invocation holds the lock (%s)" % LOCK_FILE
        )
    return fd


def check_preconditions():
    if git("branch", "--show-current").stdout.strip() != BRANCH:
        raise WrapperError("invocations run only on branch %r" % BRANCH)
    if git("status", "--porcelain").stdout.strip():
        raise WrapperError(
            "working tree not clean; commit or stash everything before a "
            "registered invocation (record commits must contain exactly the "
            "invocation files)"
        )
    fetch = git("fetch", REMOTE, BRANCH, check=False)
    if fetch.returncode != 0:
        raise WrapperError("git fetch failed: %s" % fetch.stderr.strip())
    local = git("rev-parse", "HEAD").stdout.strip()
    remote = git("rev-parse", "%s/%s" % (REMOTE, BRANCH)).stdout.strip()
    if local != remote:
        raise WrapperError(
            "local %s (%s) != %s/%s (%s); an unpushed or unpulled state "
            "blocks invocation (A24.2 c). Push/pull, or finalize a stale "
            "run, then retry." % (BRANCH, local[:9], REMOTE, BRANCH, remote[:9])
        )


def pending_runs():
    if not INVOCATIONS_DIR.exists():
        return []
    pending = []
    for p in sorted(INVOCATIONS_DIR.iterdir()):
        m = RUN_ID_RE.match(p.name)
        if m and not (INVOCATIONS_DIR / ("KHI-RUN-%s.result.json" % m.group(1))).exists():
            pending.append("KHI-RUN-" + m.group(1))
    return pending


def next_run_id() -> str:
    n = 0
    if INVOCATIONS_DIR.exists():
        for p in INVOCATIONS_DIR.iterdir():
            m = RUN_ID_RE.match(p.name)
            if m:
                n = max(n, int(m.group(1)))
    return "KHI-RUN-%06d" % (n + 1)


def latest_freeze() -> dict:
    """Cite the preceding anchored freeze (A27): most recent freeze/* tag."""
    out = git("for-each-ref", "--sort=creatordate",
              "--format=%(refname:short) %(objectname)",
              "refs/tags/freeze/").stdout.strip().splitlines()
    if not out:
        raise WrapperError("no freeze/* tag found; wrapper may not run "
                           "outside an anchored record")
    tag, tag_obj = out[-1].split()
    commit = git("rev-list", "-1", tag).stdout.strip()
    return {"tag": tag, "tag_object": tag_obj, "commit": commit}


def commit_and_push(paths, message: str) -> str:
    git("add", "--", *[str(p) for p in paths])
    git("commit", "-m", message)
    commit = git("rev-parse", "HEAD").stdout.strip()
    push_error = ""
    for attempt in range(PUSH_ATTEMPTS):
        if attempt:
            time.sleep(2 * attempt)
        push = git("push", REMOTE, BRANCH, check=False)
        if push.returncode == 0:
            break
        push_error = push.stderr.strip()
    else:
        raise WrapperError("git push failed after %d attempts: %s"
                           % (PUSH_ATTEMPTS, push_error))
    ls = git("ls-remote", REMOTE, "refs/heads/%s" % BRANCH).stdout.split()
    if not ls or ls[0] != commit:
        raise WrapperError(
            "remote verification failed: %s/%s head is %r, expected %s"
            % (REMOTE, BRANCH, ls[0] if ls else None, commit)
        )
    return commit


def finalize_result(run_id: str, pre_commit: str, pre_record_sha256: str,
                    status: str, exit_code, duration_s,
                    stdout_bytes: bytes, stderr_bytes: bytes,
                    note: str) -> dict:
    stdout_path = INVOCATIONS_DIR / ("%s.stdout.raw" % run_id)
    stderr_path = INVOCATIONS_DIR / ("%s.stderr.raw" % run_id)
    stdout_path.write_bytes(stdout_bytes)
    stderr_path.write_bytes(stderr_bytes)
    result = {
        "record_type": "invocation-result",
        "schema_version": 1,
        "run_id": run_id,
        "status": status,
        "exit_code": exit_code,
        "duration_s": duration_s,
        "stdout_file": stdout_path.relative_to(ROOT).as_posix(),
        "stdout_sha256": hashlib.sha256(stdout_bytes).hexdigest(),
        "stdout_bytes": len(stdout_bytes),
        "stderr_file": stderr_path.relative_to(ROOT).as_posix(),
        "stderr_sha256": hashlib.sha256(stderr_bytes).hexdigest(),
        "stderr_bytes": len(stderr_bytes),
        "pre_commit": pre_commit,
        "pre_record_sha256": pre_record_sha256,
        "note": note,
        "timestamp_utc": utc_now(),
    }
    result_path = INVOCATIONS_DIR / ("%s.result.json" % run_id)
    result_sha = write_record(result_path, result)
    commit = commit_and_push(
        [result_path, stdout_path, stderr_path],
        "%s result record (status=%s)" % (run_id, status),
    )
    print("result record %s status=%s sha256_jcs=%s commit=%s"
          % (result_path.name, status, result_sha, commit))
    return result


def cmd_run(args) -> int:
    role = args.role
    if role not in REGISTERED_ROLES + (SELFTEST_ROLE,):
        raise WrapperError("unknown role %r; registered roles: %s (plus %r "
                           "for non-evidential wrapper selftests)"
                           % (role, ", ".join(REGISTERED_ROLES), SELFTEST_ROLE))
    prompt_src = pathlib.Path(args.prompt_file)
    prompt_bytes = prompt_src.read_bytes()
    decoding = json.loads(pathlib.Path(args.decoding_file).read_text(
        encoding="utf-8"))
    if not isinstance(decoding, dict) or not decoding:
        raise WrapperError("decoding settings must be a non-empty JSON object")
    inputs = []
    for p in args.input or []:
        ip = pathlib.Path(p)
        inputs.append({
            "path": ip.resolve().relative_to(ROOT).as_posix()
            if ip.resolve().is_relative_to(ROOT) else str(ip),
            "sha256": sha256_file(ip),
        })
    if args.retry_of and not args.retry_reason:
        raise WrapperError("--retry-of requires --retry-reason (G5: no "
                           "silent retries)")

    lock_fd = acquire_lock()
    try:
        check_preconditions()
        stale = pending_runs()
        if stale:
            raise WrapperError(
                "prior run(s) without a pushed result record: %s. Run "
                "`invoke.py finalize --run-id <id> --abort --reason ...` "
                "first (A24.2 c)." % ", ".join(stale)
            )
        INVOCATIONS_DIR.mkdir(exist_ok=True)
        PROMPTS_DIR.mkdir(exist_ok=True)
        run_id = next_run_id()
        freeze = latest_freeze()

        prompt_path = PROMPTS_DIR / ("%s.prompt.txt" % run_id)
        prompt_path.write_bytes(prompt_bytes)
        pre = {
            "record_type": "invocation-pre",
            "schema_version": 1,
            "run_id": run_id,
            "role": role,
            "selftest": role == SELFTEST_ROLE,
            "model_id": args.model_id,
            "decoding": decoding,
            "adapter_argv": args.adapter,
            "prompt_file": prompt_path.relative_to(ROOT).as_posix(),
            "prompt_sha256": hashlib.sha256(prompt_bytes).hexdigest(),
            "input_files": inputs,
            "retry_of": args.retry_of,
            "retry_reason": args.retry_reason,
            "preceding_freeze": freeze,
            "timeout_s": args.timeout,
            "timestamp_utc": utc_now(),
        }
        pre_path = INVOCATIONS_DIR / ("%s.pre.json" % run_id)
        pre_sha = write_record(pre_path, pre)
        attempt_line = jcs.canonicalize({
            "run_id": run_id,
            "role": role,
            "selftest": pre["selftest"],
            "retry_of": args.retry_of,
            "retry_reason": args.retry_reason,
            "timestamp_utc": pre["timestamp_utc"],
        }).decode("utf-8")
        with open(ATTEMPTS_LOG, "a", encoding="utf-8") as f:
            f.write(attempt_line + "\n")

        try:
            pre_commit = commit_and_push(
                [pre_path, prompt_path, ATTEMPTS_LOG],
                "%s pre-invocation record (role=%s)" % (run_id, role),
            )
        except WrapperError as e:
            # A24.2 (b): push failure => the invocation may not occur.
            local = git("rev-parse", "HEAD").stdout.strip()
            finalize_result(
                run_id, local, pre_sha, "ABORTED_PRE_PUSH_FAILED", None, 0.0,
                b"", str(e).encode("utf-8"),
                "pre-invocation push failed; model was NOT invoked (A24.2 b)",
            )
            raise
        print("pre record %s sha256_jcs=%s commit=%s (remote verified)"
              % (pre_path.name, pre_sha, pre_commit))

        adapter_stdin = jcs.canonicalize({
            "run_id": run_id,
            "role": role,
            "model_id": args.model_id,
            "decoding": decoding,
            "prompt": prompt_bytes.decode("utf-8"),
            "inputs": inputs,
        })
        start = time.monotonic()
        status, exit_code, out, err = "COMPLETED", None, b"", b""
        try:
            proc = subprocess.run(
                args.adapter, input=adapter_stdin, capture_output=True,
                timeout=args.timeout, cwd=str(ROOT),
            )
            out, err, exit_code = proc.stdout, proc.stderr, proc.returncode
            if exit_code != 0:
                status = "ERROR"
        except subprocess.TimeoutExpired as e:
            status = "TIMEOUT"
            out = e.stdout or b""
            err = e.stderr or b""
        except Exception as e:  # adapter failed to start, etc.
            status = "ERROR"
            err = ("wrapper-side invocation exception: %r" % e).encode("utf-8")
        duration = round(time.monotonic() - start, 3)

        result = finalize_result(
            run_id, pre_commit, pre_sha, status, exit_code, duration,
            out, err, args.note or "",
        )
        return 0 if result["status"] == "COMPLETED" else 1
    finally:
        os.close(lock_fd)


def cmd_finalize(args) -> int:
    lock_fd = acquire_lock()
    try:
        run_id = args.run_id
        pre_path = INVOCATIONS_DIR / ("%s.pre.json" % run_id)
        result_path = INVOCATIONS_DIR / ("%s.result.json" % run_id)
        if not pre_path.exists():
            raise WrapperError("no pre record for %s" % run_id)
        if result_path.exists():
            raise WrapperError("%s already has a result record" % run_id)
        if not args.abort:
            raise WrapperError("finalize supports only --abort (normal "
                               "results are written by `run` itself)")
        if not args.reason:
            raise WrapperError("--abort requires --reason")
        pre_sha = jcs.sha256_jcs(load_record(pre_path))
        pre_commit = git("log", "-1", "--format=%H", "--",
                         str(pre_path)).stdout.strip()
        finalize_result(
            run_id, pre_commit, pre_sha, "ABORTED_INCOMPLETE", None, 0.0,
            b"", args.reason.encode("utf-8"),
            "finalized post hoc; any model output from this attempt is "
            "inadmissible",
        )
        return 0
    finally:
        os.close(lock_fd)


def cmd_status(_args) -> int:
    stale = pending_runs()
    print("next run id: %s" % next_run_id())
    print("pending (no result record): %s" % (", ".join(stale) or "none"))
    return 1 if stale else 0


def cmd_verify(_args) -> int:
    """Recompute every record hash and raw-stream hash; exit 0 iff all match."""
    failures = 0
    checked = 0
    if not INVOCATIONS_DIR.exists():
        print("no invocations recorded")
        return 0
    for p in sorted(INVOCATIONS_DIR.glob("KHI-RUN-*.pre.json")):
        run_id = p.name[: -len(".pre.json")]
        checked += 1
        pre = load_record(p)
        prompt_path = ROOT / pre["prompt_file"]
        if sha256_file(prompt_path) != pre["prompt_sha256"]:
            print("FAIL %s: prompt hash mismatch" % run_id)
            failures += 1
        for entry in pre["input_files"]:
            if sha256_file(ROOT / entry["path"]) != entry["sha256"]:
                print("FAIL %s: input hash mismatch (%s)"
                      % (run_id, entry["path"]))
                failures += 1
        rp = INVOCATIONS_DIR / ("%s.result.json" % run_id)
        if not rp.exists():
            print("PENDING %s: no result record" % run_id)
            failures += 1
            continue
        result = load_record(rp)
        if result["pre_record_sha256"] != jcs.sha256_jcs(pre):
            print("FAIL %s: pre-record JCS hash mismatch" % run_id)
            failures += 1
        for stream in ("stdout", "stderr"):
            data = (ROOT / result["%s_file" % stream]).read_bytes()
            if hashlib.sha256(data).hexdigest() != result["%s_sha256" % stream]:
                print("FAIL %s: %s hash mismatch" % (run_id, stream))
                failures += 1
            if len(data) != result["%s_bytes" % stream]:
                print("FAIL %s: %s length mismatch" % (run_id, stream))
                failures += 1
        print("ok %s (%s)" % (run_id, result["status"]))
    print("%d run(s) checked, %d failure(s)" % (checked, failures))
    return 1 if failures else 0


def cmd_selftest(args) -> int:
    """Non-evidential end-to-end exercise of the full A24.2 path using the
    dummy adapter (role 'selftest'). Creates and pushes real record commits."""
    scratch = INVOCATIONS_DIR / "selftest-inputs"
    prompt = ROOT / "wrapper" / "selftest-prompt.txt"
    if not prompt.exists():
        raise WrapperError("missing %s" % prompt)
    decoding = ROOT / "wrapper" / "selftest-decoding.json"
    ns = argparse.Namespace(
        role=SELFTEST_ROLE,
        model_id="selftest/dummy-echo-v1",
        prompt_file=str(prompt),
        decoding_file=str(decoding),
        adapter=[sys.executable, str(ROOT / "wrapper" / "adapters" /
                                     "dummy_echo.py")],
        input=[],
        retry_of=None,
        retry_reason=None,
        timeout=args.timeout,
        note="wrapper selftest; non-evidential",
    )
    _ = scratch  # reserved for future selftest input fixtures
    return cmd_run(ns)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="A24.2 invocation wrapper (sole admissible AI-invocation "
                    "path for registered roles)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="perform one registered invocation")
    p_run.add_argument("--role", required=True)
    p_run.add_argument("--model-id", required=True)
    p_run.add_argument("--prompt-file", required=True)
    p_run.add_argument("--decoding-file", required=True,
                       help="JSON object of decoding settings (temperature, "
                            "top_p, max_tokens, seed, ...)")
    p_run.add_argument("--input", action="append",
                       help="licensed input file (repeatable); hashed into "
                            "the pre record")
    p_run.add_argument("--adapter", nargs=argparse.REMAINDER, required=True,
                       help="adapter argv, e.g. --adapter python3 "
                            "wrapper/adapters/dummy_echo.py")
    p_run.add_argument("--retry-of")
    p_run.add_argument("--retry-reason")
    p_run.add_argument("--timeout", type=float, default=1800.0)
    p_run.add_argument("--note", default="")
    p_run.set_defaults(fn=cmd_run)

    p_fin = sub.add_parser("finalize", help="record a result for a crashed/"
                                            "interrupted run")
    p_fin.add_argument("--run-id", required=True)
    p_fin.add_argument("--abort", action="store_true")
    p_fin.add_argument("--reason")
    p_fin.set_defaults(fn=cmd_finalize)

    p_st = sub.add_parser("status")
    p_st.set_defaults(fn=cmd_status)

    p_ver = sub.add_parser("verify", help="recompute all invocation-record "
                                          "hashes")
    p_ver.set_defaults(fn=cmd_verify)

    p_self = sub.add_parser("selftest", help="end-to-end dummy invocation "
                                             "(non-evidential)")
    p_self.add_argument("--timeout", type=float, default=120.0)
    p_self.set_defaults(fn=cmd_selftest)

    args = ap.parse_args(argv)
    try:
        return args.fn(args)
    except WrapperError as e:
        print("WRAPPER REFUSAL: %s" % e, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
