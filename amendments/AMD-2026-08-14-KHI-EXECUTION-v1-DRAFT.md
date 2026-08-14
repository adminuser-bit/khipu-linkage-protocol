# Amendment Package — KHI Family Execution (A20–A27)

**Status: DRAFT — NOT FROZEN.** Prepared 2026-08-14 by the coordinating model
(Claude, Fable 5) at the operator's direction. Becomes binding only upon
(1) adversarial review by an external model of a different lineage (G7),
recorded in this directory; (2) revision; (3) the operator's signed tag
`freeze/amendments-v1`. **No Phase A0 or later act may occur before that tag.**

**Amendment authority.** The frozen prereg permits amendments "(a) before the
first scoring agent contacts data for the affected hypothesis, and (b) as an
appended, dated, signed changelog entry" (freeze block; amendment policy). No
scoring agent has contacted data for H-KHI-1 or H-KHI-2: the program produced
designs only (report §8 "Honest Limits": "Its designs are specifications, not
executions"). Condition (a) is satisfied; this document is the condition (b)
instrument. Numbering continues the tribunal record v1.1 (A1–A19).

**Sources.** Each amendment cites its origin. A20–A23 implement the Run 3 red
team's **binding required fixes** for the KHI design
(`prereg/run3-redteam-and-claimband-matrix.md`: one FATAL, three MAJOR khipu
findings; "fixes for FATAL and MAJOR findings are binding on any execution").
A24–A26 register the team-structure substitutions required for a
one-operator + AI execution, as explicit deviations where they weaken frozen
requirements. A27 adopts this repository as the tribunal record.

---

## A20 — Fixed scoring extent, two-stage testing architecture, and Holm attainability (H-KHI-1)

**Origin:** Red-team FATAL finding [khipu]: the Holm denominator over the full
search (~2.5×10⁵ triples) drives the corrected threshold to ~4×10⁻⁹ while the
frozen draw counts resolve p only to ~10⁻⁴ — the registered test was
arithmetically unpassable; simultaneously, the unfrozen search extent permitted
optional stopping on the denominator. Required fix adopted verbatim and
operationalized.

**Binding text:**

1. **Frozen extent.** At `freeze/A0-universe-v1`, the scoring extent is frozen as
   the **full cross-product** E = U1_eligible × G × D_cand, where U1_eligible is
   the deterministic subset of the 619 U1 khipus passing the registered power
   floor (≥20 alignable entries after Locke extraction; rule and code frozen at
   A1), G = the four frozen groupings, and D_cand = the frozen candidate-document
   list. m = |E| is computed and deposited **before any scoring**. Every element
   of E is scored; early stopping is prohibited; if compute requires subsampling,
   the subsample is drawn by a seeded deterministic rule frozen at A0 and m is
   the subsample size. LLM-triage suggestions may reorder but never extend or
   shrink E; each suggestion is logged (G5).
2. **Stage 1 — screening.** Every triple in E is scored with the design's frozen
   draw counts (9,999 N1; ≥10,000 N2). Screening survivors are triples with both
   empirical p ≤ 0.01. Screening p-values are logged for all of E and are never
   used for adjudication.
3. **Stage 2 — confirmatory.** Each survivor is re-scored under the identical
   frozen rules with null resolution sufficient for Holm at m: draw counts
   N ≥ 10·m/0.001 for both nulls, or an exact/importance-sampled tail
   computation whose method, estimator, and conservative-bound construction are
   frozen in the A0 appendix before Phase B. Adjudication (frozen H-KHI-1 text:
   p < 0.001 on both nulls, Holm-corrected at denominator m) uses Stage 2
   values only.
4. **Attainability demonstration.** The deposited power analysis must demonstrate,
   before Phase B, that the minimum achievable Holm-corrected p under the Stage 2
   method is < 0.001/m. If it is not, scoring may not begin; the design returns
   to amendment.

## A21 — Degenerate-N1 pairs are unscoreable (H-KHI-1)

**Origin:** Red-team MAJOR finding [khipu]: the design's rule ("N1 underpowered →
N2 becomes the binding null") converted pairs unpassable under the frozen
dual-null requirement into passable-on-N2-alone — a widening authored inside a
design that disclaimed adjudication authority. Required fix adopted (first
branch).

**Binding text:** A pair whose N1 admissible permutation group cannot resolve
p < 0.001 — fewer than 1,000 distinct permutation images under the A11
structure-preserving rules — is **unscoreable under the frozen criteria and
cannot support a positive linkage claim in this run.** It is reported as
unscoreable with both computed p-values shown descriptively. The frozen
dual-null requirement of H-KHI-1 stands unmodified.

## A22 — Stratified decoy panel and rank-1 identity requirement (H-KHI-1, null N2)

**Origin:** Red-team MAJOR finding [khipu]: 99% of the N2 null mass was permuted
material rather than the registered decoy-document class, and period/region
mismatch between cheap 16th-century decoys and 17th-century candidates made the
null easier to beat. Required fix adopted verbatim.

**Binding text:**

1. A passing pair must, in addition to the frozen p < 0.001 requirements, rank
   **1st among the ≥100 pure decoy-document identity scores** for its stratum;
   the permutation-padded N2 p-value is reported alongside, never instead.
2. The decoy panel frozen at A0 is **stratified**, and each candidate document is
   scored against decoys matched on: period band (±50 years), region/audiencia,
   document type (visita / revisita / padrón / tasa), and entry-count stratum.
   The stratification scheme and each stratum's membership are frozen at A0. If
   any stratum required by a candidate has fewer than the frozen minimum of
   matched decoys, candidates in that stratum are unscoreable until the panel is
   extended by a dated pre-data-contact addendum for those candidates.

## A23 — Santa Valley positive-control criterion frozen (H-KHI-1)

**Origin:** Red-team MAJOR finding [khipu]: "recover the published match" — the
single event able to quarantine the whole family — had no registered threshold,
grouping, or null panel. Required fix adopted verbatim.

**Binding text:** The positive control **passes iff** the six Corongo khipus
(OKR identifiers resolved from Medrano & Urton 2018 + `okr-kh-numbers.csv` and
deposited at A0) versus the 1670 San Pedro de Corongo revisita achieve empirical
p < 0.001 on **both** N1 and N2, **uncorrected**, under the pre-frozen matching
rules and grouping **G-2** (color-band grouping), scored against the frozen A0
decoy panel (the control pair's own stratum), **outside the Holm family,
calibration-only, zero evidential weight for new claims.** Results under the
other three groupings are reported descriptively. Failure ⇒ pipeline defect and
family-wide quarantine per frozen text; the rule-sensitivity evidence about the
2018 match is reported to the tribunal record.

## A24 — Role disjointness by agent context isolation (G2 implementation)

**Origin:** Team-structure reality: this execution has one human operator plus AI
agents. G2 requires generator ≠ test-author ≠ executor; the design requires
disjoint Teams L/P and a non-scoring data steward.

**Binding text:**

1. Role disjointness among AI parties is implemented by **context isolation**:
   each role (data steward; archival triage; transcription keys 1 and 2; scoring
   executor; red team) is a separate agent invocation sharing no conversation
   state with other roles. An agent receives only the inputs its role licenses.
2. Every agent's complete prompt and configuration is committed under
   `logs/agent-prompts/` no later than its invocation (append-only, CI-enforced).
   An agent whose prompt was not committed produces no admissible output.
3. The coordinating model (Fable 5) may author code and prompts **before** the
   relevant freeze and may orchestrate invocations, but no LLM — coordinating or
   otherwise — sits in any adjudication path (design §8, reaffirmed). All
   pass/fail outputs come from code frozen at `freeze/scoring-code-v1`.
4. The operator inevitably has global visibility. The operator's protections
   against self-deception are: (i) no edits to frozen code/thresholds
   (CI-enforced); (ii) commitments before data contact (R5); (iii) an operator
   action log (`logs/operator-log.md`) recording every manual data act; (iv) the
   external cross-model review of any headline claim (G7, unchanged).
5. **Limit registered:** context isolation prevents information flow between
   agents but all internal agents share one model lineage; per the tribunal
   meta-finding, their agreement is correlated evidence and is never presented
   as corroboration. G7 external review remains mandatory for headline claims.

## A25 — Transcription QC substitution (registered deviation from design §3.A0.3)

**Origin:** The design requires "independent double keying of all numeric fields
and group structure by **two human transcribers**" at ≥99.5% agreement. A
one-operator team cannot satisfy this. This amendment registers a substitute and
**declares it a deviation weaker than the frozen requirement**; every report
using transcripts produced under it must say so.

**Binding text:**

1. **Preference order for the search universe:** (i) published scholarly
   transcriptions (keyed from print; transcription risk borne by the published
   edition, cited); (ii) digitized manuscripts transcribed under rule 2. Where a
   published edition exists, it is the primary key.
2. **AI double-keying:** two independent keying passes by AI systems of
   **different model lineages** (e.g., one Anthropic-lineage, one
   OpenAI-lineage), separately invoked, no shared context, tool + version + full
   prompt logged. Per-field agreement on numeric fields and group structure must
   be ≥99.5%; disagreements resolved by a third independent key plus operator
   adjudication, all recorded.
3. **Human spot-check:** the operator hand-verifies a seeded random sample of
   ≥5% of numeric fields (minimum 200 fields) per document against the source
   image or edition; the sample, seed, and error count are deposited. A
   spot-check error rate > 0.5% fails the document's QC gate.
4. A document failing any part of this gate does not enter scoring (unchanged).
5. **Disclosure:** all reports state that transcription QC used AI double-keying
   with human spot-checks rather than the registered two-human protocol.

## A26 — Ratification of audit-grade data acts (A17 clarification)

**Origin:** Red-team cross-cutting note: Run 3 designers performed audit-grade
real-corpus data acts (hashing, counting, snapshotting) at design time under a
carve-out A17's text does not contain; the red team asked the tribunal to either
ratify the carve-out explicitly or treat those acts as pre-appendix data contact.

**Binding text:** Audit-grade acts — downloading, hashing, verifying byte counts,
counting table rows, resolving identifiers — are ratified as **non-scoring data
contact** and do not trigger the freeze block's data-contact clause, **provided**
each act is logged (actor, date, artifact, hash) in `logs/operator-log.md` or the
relevant agent log before or at execution. Any act that computes a linkage score,
alignment, or null statistic is scoring contact and is governed by the freeze
requirements. The Run 3 design-time acts recorded in the archive are ratified
retroactively under this rule.

## A27 — This repository is the tribunal record for the KHI execution

**Binding text:** The repository `khipu-linkage-protocol` (default branch,
protected; signed `freeze/*` tags; externally anchored per GOVERNANCE.md R4) is
the canonical tribunal record for the KHI family execution. "Deposited,"
"logged," and "filed to the tribunal record" in all frozen documents are
satisfied by commits to this repository under GOVERNANCE.md rules R1–R5.
Deposits require a pushed commit **and**, for freeze tags, external anchoring;
the anchor timestamp is authoritative where ordering is contested.

---

## Explicitly unchanged

- All frozen H-KHI-1 / H-KHI-2 thresholds, null constructions (A11), and
  disconfirmation clauses. Nothing here widens any registered threshold; A20–A23
  narrow or operationalize, per the freeze block's "appendices may narrow."
- The A12 Phase C custodian remains an **independent named human** meeting the
  design §5 eligibility rules (excluding Medrano, Urton, FitzPatrick, Hyland;
  OKR affiliation requires conflict review). No AI or operator substitution.
- The G7 cross-model tribunal for headline claims.
- L5–L7 prohibitions; no glottographic or narrative-content claims; Hyland's
  Collata hypothesis neither assumed nor tested.
- G9: null results reported at equal prominence.

## Review instructions for the external model

You are reviewing an amendment package for a preregistered khipu–archive record
linkage experiment. Attack it: (1) Does any amendment widen a frozen threshold
or create an execution-time discretionary degree of freedom? (2) Is the A20
two-stage architecture sound — can a pair pass Stage 2 by construction, or is it
again unpassable? (3) Does A25's AI double-keying open a contamination channel
(both keyers may have memorized published visita editions — does that corrupt a
transcription, and does it matter given the source is the same edition)?
(4) Does A24's context-isolation claim hold given one operator sees everything?
(5) What is missing that would let a motivated team pass a false positive or
manufacture an uninterpretable null? Report findings with severity ratings;
required-fix format preferred.
