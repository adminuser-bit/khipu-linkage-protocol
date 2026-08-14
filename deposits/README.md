# deposits/ — Commitments and manifests (APPEND-ONLY)

- frozen-manifest.sha256 — the freeze guard's authority: every listed file is
  frozen; CI recomputes all hashes on every push.
- anchors/ — external anchoring proofs for each freeze tag (Zenodo DOIs,
  OpenTimestamps receipts). A freeze is provisional until anchored (R4).
- Commitment files (*.sha256) — SHA-256 of material committed BEFORE the data
  contact it protects (R5): A0 universe list, decoy panel, Santa Valley control
  IDs, scoring-code hashes, Team P prediction deposits (Phase C).
