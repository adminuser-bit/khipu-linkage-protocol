#!/usr/bin/env python3
"""Dummy adapter for wrapper selftests. NOT a model; role 'selftest' only.

Reads the wrapper's JCS-encoded invocation object on stdin and writes a
deterministic acknowledgment to stdout. Exercises the complete A24.2 path
(pre-commit, push verification, capture, hashing, result commit) with no
AI involvement and no network access.
"""
import hashlib
import json
import sys


def main() -> int:
    raw = sys.stdin.buffer.read()
    obj = json.loads(raw.decode("utf-8"))
    sys.stdout.write(
        "SELFTEST-OK run_id=%s stdin_sha256=%s\n"
        % (obj["run_id"], hashlib.sha256(raw).hexdigest())
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
