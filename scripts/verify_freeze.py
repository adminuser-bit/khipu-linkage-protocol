#!/usr/bin/env python3
"""Freeze guard: verify every hash in deposits/frozen-manifest.sha256.

Exit 0 iff every listed file exists and matches its recorded SHA-256.
Run locally or in CI. No dependencies beyond the standard library.
"""
import hashlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "deposits" / "frozen-manifest.sha256"


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not MANIFEST.exists():
        print(f"FAIL: manifest missing: {MANIFEST}")
        return 1
    failures = 0
    entries = 0
    for line in MANIFEST.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            expected, rel = line.split(None, 1)
        except ValueError:
            print(f"FAIL: malformed manifest line: {line!r}")
            failures += 1
            continue
        entries += 1
        target = ROOT / rel.strip()
        if not target.exists():
            print(f"FAIL: frozen file missing: {rel}")
            failures += 1
            continue
        actual = sha256(target)
        if actual != expected:
            print(f"FAIL: hash mismatch: {rel}\n  expected {expected}\n  actual   {actual}")
            failures += 1
        else:
            print(f"ok: {rel}")
    print(f"\n{entries} manifest entries, {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
