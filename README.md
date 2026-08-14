# Khipu Record Linkage — Execution Repository & Tribunal Record

**Program:** Undeciphered Writing Systems Research Program — Family KHI execution
(H-KHI-1 numeric record linkage; H-KHI-2 prospective attribute prediction).

**Status:** `PHASE-0-DRAFT` — governance and amendment package drafted; **nothing is
frozen; no scoring data contact has occurred.** The amendment package in
`amendments/` requires (1) external cross-model adversarial review (G7) and
(2) the operator's signed freeze tag before any Phase A0 work begins.

This repository is the continuation of the program's tribunal record for the khipu
family. Its founding documents are the frozen preregistration, the tribunal record
and amendments v1.1 (A1–A19), the Run 3 KHI experiment design, and the Run 3
red-team findings — imported **verbatim** into `prereg/` and hashed in
`deposits/frozen-manifest.sha256`.

## What this experiment is

Test whether Inca khipus in the Open Khipu Repository can be linked, by their
decimal knot arithmetic alone, to specific Spanish colonial administrative
enumerations (visitas, revisitas, padrones, tasas, Peru 1532–1700) — under
preregistered matching rules, structure-preserving permutation nulls,
a stratified decoy-document panel, full multiplicity accounting over a frozen
search universe, and a calibration run against the one published match
(Medrano & Urton 2018, Santa Valley / San Pedro de Corongo 1670).

A null result is a registered deliverable: the first multiplicity-honest upper
bound on the khipu–archive linkage rate over an enumerated search universe.

## Repository layout

| Path | Contents | Mutability |
|---|---|---|
| `prereg/` | Founding documents, verbatim imports | **Frozen at import** (hash-guarded) |
| `amendments/` | Dated amendment package(s) | Append-only; each frozen by signed tag |
| `code/` | Scoring/extraction code | Frozen by signed tag before Phase B |
| `deposits/` | SHA-256 commitment files, manifests | Append-only |
| `sealed/` | Ciphertexts of sealed material (never plaintext before unmask) | Append-only |
| `logs/` | Search log (Holm denominator), custody log, agent prompts | Append-only |
| `results/` | Reports, both p-values always, nulls at equal prominence | Post-scoring only |
| `scripts/` | Freeze-guard verification tooling | Maintained |

## Freeze mechanics (summary; normative text in GOVERNANCE.md)

- A **freeze** is a signed annotated git tag (`freeze/<name>-v<N>`) on the protected
  default branch. Frozen paths are listed in `deposits/frozen-manifest.sha256`.
- CI (`.github/workflows/freeze-guard.yml`) recomputes hashes of all manifest
  entries on every push and fails if any frozen byte changed; it also rejects any
  edit to append-only files that is not a pure append.
- Each freeze tag is externally anchored (Zenodo versioned DOI and/or
  OpenTimestamps) so that not even the repository owner can silently rewrite it.
- A **deposit** (commitment) is a committed SHA-256 of a file — optionally with its
  ciphertext in `sealed/` — made *before* the corresponding data contact; unmasking
  later commits the plaintext, which CI verifies against the prior commitment.

## How to verify this repository (any third party)

```bash
python3 scripts/verify_freeze.py            # checks every manifest hash
git tag -v freeze/<name>                    # verifies tag signature
shasum -a 256 -c deposits/frozen-manifest.sha256
```

## Order of operations (nothing may run out of order)

1. **Phase 0** — amendment package externally reviewed (different model lineage),
   revised, then frozen: `freeze/amendments-v1`. ← *we are here*
2. **Phase A0** — archive enumeration freeze: closed search universe + stratified
   decoy panel + Santa Valley control IDs deposited → `freeze/A0-universe-v1`.
3. **Phase A1** — OKR v2.1.0 verification gate; extraction + scoring code frozen →
   `freeze/scoring-code-v1`.
4. **Phase B** — Santa Valley calibration, then screening pass, then confirmatory
   pass. Every (khipu, document, grouping) triple appended to `logs/search-log.jsonl`.
5. **Phase C** — only if a new pair passes H-KHI-1 in full: A12 two-team masking
   with an independent named human custodian (unchanged from the frozen design).

## Provenance

Source archive: `undeciphered-program-archive.zip`,
sha256 `3c03958e0ae5096bf5c9269928e047e34d18767309911e9efd387ff266b645f4`
(program working archive, runs 1–3, 2026-08-04 → 2026-08-11). The seven documents
in `prereg/` were copied from it byte-for-byte on 2026-08-14.
