# wrapper/ — A24.2 invocation wrapper

The sole admissible path for AI invocations in registered roles
(data-steward, archival-triage, transcription-keying, scoring-executor,
red-team). Implements A24.2 of the amendment package frozen at
`freeze/amendments-v1`:

- **Monotonic run IDs** (`KHI-RUN-NNNNNN`), derived under a process lock
  from the committed records in `logs/invocations/`.
- **Push-before-invoke**: the pre-invocation commit (run ID, prompt hash,
  model ID, decoding settings, licensed-input hashes) is created, pushed,
  and remote-verified before any model call; push failure ⇒ no invocation,
  recorded as `ABORTED_PRE_PUSH_FAILED`.
- **Auto-archived results**: complete raw stdout/stderr byte streams are
  written, hashed, committed, and pushed immediately after return, error,
  abort, or timeout. A new invocation is refused while any run lacks a
  pushed result record (`finalize --abort` records crashed runs).
- **No silent retries**: every attempt, including every retry
  (`--retry-of` + `--retry-reason`, both mandatory together), is one line
  in `logs/invocations/attempts.jsonl` — the G5 attempt register for
  invocations.
- **Manual invocations inadmissible**: output lacking a wrapper record
  pair (pre + result, both pushed) may not enter any registered-role
  pathway.

## Hashing conventions

- Structured records: `SHA-256(JCS(record))` per A20.9 (RFC 8785 via
  `jcs.py`; UTF-8; no prefix/suffix/delimiter). Record files are pretty
  rendered for readability; the hash is over the canonical form of the
  parsed object (`invoke.py verify` recomputes everything).
- Raw byte artifacts (prompt file, stdout, stderr): SHA-256 over exact
  bytes. Byte streams admit no serialization ambiguity — the property
  A20.9 exists to guarantee — and their hashes are embedded in the
  JCS-hashed records.

## Commands

```
python3 wrapper/invoke.py run --role <role> --model-id <id> \
    --prompt-file <f> --decoding-file <f.json> [--input <f>]... \
    [--retry-of KHI-RUN-NNNNNN --retry-reason "..."] --adapter <argv>...
python3 wrapper/invoke.py status
python3 wrapper/invoke.py verify
python3 wrapper/invoke.py finalize --run-id <id> --abort --reason "..."
python3 wrapper/invoke.py selftest
```

Adapters (`wrapper/adapters/`) receive one JCS-encoded JSON object on
stdin and write raw model output to stdout. A real model adapter is
admissible only after its A24.3 model manifest is deposited;
`dummy_echo.py` (no AI, no network) serves the non-evidential `selftest`
role only.

Tests: `python3 -m unittest discover -s wrapper/tests`.
