# Governance — Freeze Mechanics, Roles, and Record Integrity

This document is normative for every action taken in this repository. It
implements, for a one-operator + AI-agent team, the tribunal-record discipline of
`prereg/run2-preregistration-FROZEN.md` (global rules G1–G9, freeze block) and
`prereg/tribunal-record-and-prereg-amendments-v1_1.md` (A1–A19). Where this
document and a frozen prereg text disagree, **the frozen prereg text wins** and
the disagreement must be filed as a finding.

## 1. The record

The default branch of this repository is the canonical tribunal record for the
KHI family execution. Rules:

- **R1 — No history rewriting.** The default branch is protected: no force-push,
  no branch deletion, no tag deletion or re-pointing. A violation discovered later
  is a protocol violation and is reported, not repaired silently.
- **R2 — Frozen paths.** Every file listed in `deposits/frozen-manifest.sha256`
  is frozen. CI recomputes all manifest hashes on every push; any mismatch fails
  the build. Frozen text is never edited — corrections happen as new, dated,
  appended documents.
- **R3 — Append-only paths.** `amendments/`, `deposits/`, `sealed/`, and `logs/`
  are append-only: files may be added, and designated `.jsonl` logs may grow at
  the end, but no existing committed line may be modified or deleted. CI enforces
  this by diffing against the merge base.
- **R4 — External anchoring.** Every `freeze/*` tag is anchored outside GitHub
  within 72 hours: a Zenodo versioned deposit of the tagged tree (immutable DOI)
  and/or an OpenTimestamps proof of the tag's commit hash, committed back into
  `deposits/anchors/`. Until anchored, a freeze is provisional.
- **R5 — Deposits precede data contact.** A commitment (SHA-256, optionally with
  ciphertext) must be committed and pushed *before* the act it protects (archive
  search, document read, unmasking). The commit timestamp plus anchoring is the
  proof of ordering. Per A17 as amended: **unhashed input ⇒ no scoring.**

## 2. Freezes

A freeze is executed by the operator, and only by the operator:

1. Open a pull request containing exactly the material to be frozen.
2. CI green; external review recorded where required (G7 items).
3. Merge; append the new files' hashes to `deposits/frozen-manifest.sha256`.
4. Create a **signed annotated tag** `freeze/<name>-v<N>` (GPG/SSH signature by
   the operator's published key, fingerprint recorded in `deposits/operator-key.txt`).
5. Anchor per R4.

Registered freeze points for this run: `freeze/amendments-v1`,
`freeze/A0-universe-v1`, `freeze/scoring-code-v1`, and (Phase C only)
`freeze/teamP-model-v1` plus per-prediction deposits.

## 3. Roles (per amendment A24; summary)

- **Operator (Laurent Heller):** signs freezes; holds passphrases for sealed
  material in Phases A–B; performs registered human spot-checks; never edits
  adjudication code or thresholds after their freeze; every operator data act is
  logged in `logs/operator-log.md`.
- **Coordinating model (Claude, Fable 5):** protocol engineering, code authorship
  *before* freeze, agent orchestration, drafting. Never adjudicates: all
  pass/fail decisions are produced by frozen deterministic code.
- **Isolated agents:** role-separated single-purpose agent invocations (data
  steward, archival triage, transcription keying, scoring executor, red team).
  Disjointness is enforced by context isolation — an agent receives only its
  role's inputs — and every agent's full prompt/config is committed under
  `logs/agent-prompts/` no later than its invocation.
- **External reviewer model (different lineage, e.g. GPT-family):** adversarial
  review of the amendment package and of any headline claim (G7). Internal
  agreement among same-lineage agents is never corroboration.
- **Phase C custodian:** an independent **named human** per A12 and design §5 —
  this role is *not* substituted by AI or by the operator. Phase C cannot begin
  without the custodian's identity deposited.

## 4. Adjudication discipline

- All statistics (linkage scores, permutation nulls, empirical p, Holm
  accounting) are computed by code frozen at `freeze/scoring-code-v1`, run with
  pinned seeds, producing machine-readable outputs committed to `results/`.
- No LLM sits anywhere in an adjudication path (design §8, unchanged).
- Both p-values (N1, N2) are always reported for every scored pair, including
  unscoreable and failed pairs. Selective reporting is a protocol violation (G5).
- The search log `logs/search-log.jsonl` is the Holm denominator. One line per
  (khipu, document, grouping) triple scored, appended before its score is
  interpreted. LLM-triage candidate suggestions are logged as search actions.
- Null results are deliverables reported at equal prominence (G9).

## 5. Deviations

Any departure from frozen text after the relevant data contact is reported as a
**protocol violation** in `results/` alongside the registered analysis — never
retro-edited (freeze-block deviation rule, verbatim). Amendments are permitted
only before first data contact for the affected hypothesis, as dated appended
entries.
