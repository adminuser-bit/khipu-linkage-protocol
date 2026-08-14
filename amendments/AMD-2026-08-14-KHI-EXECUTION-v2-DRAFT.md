# Amendment Package — KHI Family Execution, v2 (A20–A27, A29–A31)

**Status: DRAFT v2 — NOT FROZEN.** Supersedes `AMD-2026-08-14-KHI-EXECUTION-v1-DRAFT.md`
(retained, append-only). Prepared 2026-08-14 by the coordinating model after
external adversarial review `REVIEW-2026-08-14-GPT-5.6-Sol-01.md` (30 findings:
5 FATAL, 21 MAJOR, 4 MINOR — **all accepted**). Each amendment cites the
findings it implements as [F#]. Freezing requires: (1) a second external review
pass over this v2 **including GOVERNANCE.md** [F18]; (2) explicit operator
ratification of the two decisions below; (3) the operator's signed tag
`freeze/amendments-v1` on an exact commit, externally anchored.

**A28 is reserved** for the registered-leads band, pending its separate external
review; if adopted it will be restated against v2 mechanics (a lead = a Stage-1
survivor failing Stage-2 adjudication).

## Operator ratification required (two decisions)

**R-1 — Amendment of registered text (A22.1).** The frozen H-KHI-1 null (b)
("≥100 same-genre decoy documents", p < 0.001) is arithmetically unpassable as
literally operationalized: a pure-rank test over D decoys has minimum p =
1/(D+1) ≈ 0.0099 > 0.001. The v1 design's permutation padding was rejected by
both the internal red team and the external reviewer [F2: "must be amended
rather than numerically padded"]. A22.1 therefore **amends the registered
null-(b) operationalization** — a dated, pre-data-contact amendment to frozen
text, permitted by the amendment policy but requiring the operator's explicit
signature as such, not buried as a narrowing.

**R-2 — Run-1 scope restriction (A25).** The frozen two-human transcription
requirement is preserved, not widened [F10]. Consequence: this run's
adjudication universe is restricted to documents whose numeric/group-structure
transcription exists under scholarly human editorial control (published
critical editions), and **Phase C / the H-KHI-2 E3 instrument is blocked for
this run** [F10, F23] — it requires both two-human QC and an unpublished
document, neither available to the current team. Run 1 is the E2 linkage
experiment (H-KHI-1) plus, at most, E2-retrospective H-KHI-2 analysis.

---

## A20 — Frozen extent, two-stage architecture, and frozen Stage-2 inference

*Implements the red team's FATAL Holm-attainability fix as corrected by [F1, F3,
F4, F5, F6, F7, F19, F27].*

1. **Extent.** E = U1 × G × D_cand, the **full cross-product**, with no
   eligibility carve-outs at any level [F5]: every khipu in U1 (619), all four
   frozen groupings, every candidate document. m = |E| is computed and
   deposited at `freeze/A0-universe-v1` before any scoring.
2. **D_cand is mechanical** [F19]: all documents satisfying the frozen
   metadata-only eligibility rule (design §2.2: Peru, 1532–1700, visita/
   revisita/padrón/tasa, ≥20 grouped numeric entries *per catalog metadata or
   edition front matter, not content inspection*) within the enumerated series,
   **minus** the decoy panel (assigned by the A22.4 hash lottery) **minus** the
   positive-control document. No LLM or operator judgment touches membership;
   LLM triage may reorder processing only after membership is fixed, every
   suggestion logged (G5).
3. **m never shrinks** [F6]: once frozen, no later scoreability failure reduces
   m. An unscoreable triple (A21, A22.5, A25.6) remains a registered test with
   no positive-claim eligibility, assigned p = 1 for multiplicity accounting.
4. **Compute-bound fallback, frozen now** [F7]: if |E| > M_max = 1,000,000,
   the scored set is exactly M_max triples selected by ascending
   SHA-256(triple_id ∥ "KHI-A20-LOTTERY-20260814"), and m = M_max. All
   null-result language must then say "over the deterministic sampled
   universe," never "over the enumerated archive universe."
5. **Stage 1 — screening.** Every triple in E scored with 9,999 N1 draws and
   9,999 N2 mixture draws (A22.2), RNG stream seeded
   SHA-256("KHI-S1" ∥ triple_id ∥ null_id). Survivors: empirical p ≤ 0.01 on
   both nulls [F27]. **All Stage-1 draws, exceedance counts, and statistics are
   discarded for inference** [F3]; they are logged, reported descriptively, and
   never enter a confirmatory p-value.
6. **Stage 2 — confirmatory, single frozen algorithm** [F4]: for each survivor,
   per null: plain Monte Carlo, no importance sampling, no sequential stopping,
   no adaptive proposals, N = ceil(10 · m / 0.001) draws (= 10,000·m), fresh
   stream seeded SHA-256("KHI-S2" ∥ triple_id ∥ null_id), independent of every
   Stage-1 stream. Estimator: add-one empirical p = (1 + #{null ≥ observed}) /
   (1 + N); ties (null = observed) count as exceedances. Minimum attainable
   p = 1/(1+10,000·m) < 0.001/m — attainable by construction, conditional on
   the A21 support condition. Zero-exceedance results are reported as
   p ≤ 1/(1+N) and are valid only where A21 support is verified.
7. **Adjudication** (frozen text, as amended by A22.1): H1 requires Stage-2
   p < 0.001, Holm-corrected at denominator m, on N1 **and** the A22 N2
   construction, **and** the A22.3 rank-1 identity condition.
8. **Attainability demonstration** [F1, F4]: the deposited power analysis must
   show, before Phase B, for the frozen m: (a) Stage-2 Monte Carlo resolution
   < 0.001/m; (b) the A21 support floors are computable for every triple from
   pre-score quantities; (c) expected compute for Stage 2 at the registered
   survivor bound. If any part fails, scoring may not begin.

## A21 — Finite-support scoreability (replaces v1 A21 in full) [F1, F6]

For every triple, let M₁ be the number of distinct admissible N1 permutation
images, computed (or conservatively lower-bounded) combinatorially from group
sizes, subtotal constraints, and tie profiles by frozen code — never by
sampling. A triple is **confirmatorily scoreable on N1 only if M₁ > 1000·m**
(the conservative rank-1 Holm floor: 1/M₁ < 0.001/m). Likewise the N2 mixture
support S₂ = Σ_d M₁(d) over the triple's matched decoy panel must satisfy
S₂ > 1000·m. Monte Carlo draws never increase effective support beyond the
exact permutation universe. Triples failing either condition are unscoreable,
remain in m at p = 1, and are reported with both descriptive p-values.

## A22 — N2 reconstruction, stratified decoys, lottery assignment

*Implements [F2, F8, F20, F29]; A22.1 is ratification item R-1.*

1. **Registered amendment to H-KHI-1 null (b).** The decoy-document requirement
   is operationalized as the conjunction of A22.2 and A22.3, replacing the
   unpassable pure-rank reading and the rejected permutation-padded reading:
2. **N2 clustered-mixture null** [F2]: one draw = (select a decoy document d
   uniformly from the triple's matched stratum panel — **equal weight per
   document, never per permutation** — then draw one admissible A11
   structure-preserving permutation image of d). The mixture p-value estimates
   P(score ≥ observed | random same-stratum document with structure-preserved
   values), carries the Stage-2 Holm requirement p < 0.001/m under the A20.6
   estimator, and its finite support is governed by A21. Combination, tie, and
   estimator rules are exactly A20.6; no other combination is permitted.
3. **Rank-1 identity condition** [F2, F29]: the candidate document's unpermuted
   score must strictly exceed the unpermuted score of **every** decoy document
   in its matched panel. Its exact identity-support p = 1/(D+1) is reported
   as-is and is never conflated with the mixture p-value.
4. **Panel membership by hash lottery** [F20]: within each frozen stratum,
   eligible documents are ordered by ascending
   SHA-256(doc_id ∥ "KHI-A22-LOTTERY-20260814"); the first n_decoy = 25 per
   stratum are decoys; the remainder are candidates. The positive-control
   document is the single predesignated exception (excluded from both). The
   complete assignment is deposited at A0 before any numeric transcription.
5. **Strata, frozen bins** [F8]: period ∈ {1532–1583, 1584–1650, 1651–1700}
   (document's stated survey year; range documents by start year); region =
   audiencia (Lima, Charcas, Quito; outside → unscoreable); type ∈ {visita,
   revisita, padrón, tasa} per catalog/edition designation under a metadata
   codebook frozen at A0 *before* enumeration returns results; entry-count bins
   {20–49, 50–99, 100–199, ≥200} per catalog/edition metadata. A candidate is
   scored only against decoys matching all four axes. A stratum with <25 decoys
   renders its candidates unscoreable **this run** (they remain in m at p = 1);
   **no same-run panel extension exists** — deficient strata may be repaired
   only in a future preregistered run.

## A23 — Positive control under PC-G (replaces v1 A23) [F9, F28]

The Santa Valley control is scored under **PC-G**, a positive-control-only
grouping algorithm reproducing exactly the published Medrano & Urton (2018)
grouping procedure, implemented from the paper's description with a frozen test
fixture (the published 132/133 alignment), code hash deposited before
execution. PC-G is not G-1..G-4, appears nowhere in E, carries zero evidential
weight, and sits outside the Holm family [F28]. **Pass criterion:** the six
Corongo khipus vs the 1670 revisita achieve p < 0.001, uncorrected, on N1 and
on the A22.2 mixture null over the control's matched stratum panel, plus the
A22.3 rank-1 condition. Failure ⇒ pipeline defect, family-wide quarantine
(frozen text); results under G-1..G-4 are reported descriptively.

## A24 — Roles, invocation integrity, and operator information boundary

*Implements [F14, F15, F16]; retains v1 context-isolation core.*

1. Role disjointness by agent context isolation, as v1 A24.1, with the
   correlated-lineage limit retained verbatim (internal agreement is never
   corroboration; G7 unchanged).
2. **Invocation wrapper** [F15]: every AI invocation in any registered role runs
   through a frozen wrapper that (a) assigns a monotonic run ID; (b) commits
   prompt hash, model ID, and decoding settings **before** invocation;
   (c) automatically hashes and appends the complete raw output and error
   status immediately after, including aborted, failed, and superseded runs;
   (d) forbids silent retries — every retry capable of affecting search,
   transcription, or triage is a registered attempt in the G5 log. Manual
   direct invocations are inadmissible; their outputs may not enter any
   registered artifact.
3. **Frozen model manifest** [F16]: before first use in each role, the exact
   model IDs/versions, API mode, system prompts, temperature/top-p, seeds where
   supported, vision resolution and cropping rules, permitted tools, and
   network state are deposited. Unavailability of a frozen model triggers a
   dated amendment, never a quiet substitution.
4. **Operator information boundary** [F14]: v1's "operator inevitably has
   global visibility" is struck. The operator is procedurally and
   cryptographically denied all Phase-C sealed attribute content (names,
   statuses, moieties) until Team-P prediction deposit: full-document handling
   of any potentially E3-eligible document is performed by the independent
   human custodian; the operator may receive only redacted numeric-field
   material; sealed ciphertexts and custodian logs are not operator-readable
   before deposit. (Phase C is blocked this run per R-2; this rule binds any
   future run under this record.)

## A25 — Transcription and source QC (replaces v1 A25 in full)

*Implements [F10, F11, F12, F13, F26]; ratification item R-2.*

1. **The frozen two-human requirement is preserved.** No AI substitution enters
   the preregistered adjudication path.
2. **Adjudication universe restriction** [F10]: candidate and decoy documents
   must have their numeric fields and group structure attested in a published
   scholarly transcription (critical edition or peer-reviewed publication)
   produced under human editorial control. Unpublished manuscripts are
   excluded from adjudication this run; any work on them is a labeled pilot
   whose outputs cannot enter registered scoring.
3. **Print-to-machine keying:** two independent keying passes from the edition.
   AI keyers are permitted for this non-adjudicative mechanical step only under
   [F11] conditions: anonymized page/crop images with title, archive, and
   document identity removed; network and retrieval disabled; A24.3 frozen
   manifest; all outputs auto-archived via the A24.2 wrapper. Inter-keyer
   agreement is reported only as inter-model agreement, never as accuracy
   evidence.
4. **Deterministic disagreement resolution** [F13]: two-of-three identical keys
   determine a value (third key drawn under the same rules). Three-way or
   structural disagreement goes to an independent human reader blind to all
   linkage scores; if no unambiguous reading results, the field is coded
   missing/uncertain by frozen rule. **The operator never chooses a value.**
5. **Source-grounded verification** [F12]: the operator verifies keyed fields
   against the published edition with n_check = min(F, max(ceil(0.05·F), 598))
   fields per document, seeded sample; pass iff the one-sided 95% exact
   binomial upper bound on the field error rate is ≤ 0.005 (zero errors at
   n = 598 suffices; if F < 598, all fields are checked and the exact census
   error rate is reported). Group boundaries and hierarchy are checked
   separately and require 100% agreement or explicit uncertain coding. **For
   every Stage-2 survivor, 100% of fields are verified before adjudication is
   reported.**
6. **Edition hierarchy and field states** [F26]: where multiple editions exist,
   the frozen hierarchy is: most complete coverage of the document's numeric
   fields; ties broken by most recent critical edition; deposited per document
   at A0 before any scoring. Every field carries a state from {observed,
   editorially-restored, uncertain, illegible, supplied-subtotal}. **Primary
   scoring uses `observed` fields only**; all other states are excluded from
   the linkage score and enter only the registered sensitivity treatment S2.
   Documents failing this QC do not enter scoring (their triples remain in m
   at p = 1).

## A26 — Historical declaration and prospective acquisition rule (replaces v1 A26) [F17]

1. **No retroactive ratification.** Struck in full.
2. **Historical declaration (deviation record, not erasure):** design-time
   real-corpus acts recorded in the program archive — the Linear A designer's
   decoding and counting of lineara.xyz records, and the shadow-harness
   designer's derivation and publication of the Linear A per-document length
   multiset — are recorded as A17 protocol deviations affecting those
   families. For family KHI: no content-level data act beyond the registered
   Run 2 audit (OKR download, hash, table counts) is known; Phase-0 acts in
   this repository (byte-for-byte file copies and hashing) are byte-level only
   and enumerated in `logs/operator-log.md`. Any additionally discovered
   pre-freeze act is reported as a deviation on discovery.
3. **Prospective rule:** after `freeze/amendments-v1` and before inferential
   scoring, a designated steward agent may perform only enumerated byte/schema
   acts: download, cryptographic hash, file size, schema/table row counts, and
   mechanically specified identifier resolution. These acts populate manifests
   and may not inform thresholds, groupings, eligibility, nulls, candidate
   selection, power floors, or scoring code. Content-level statistics and
   feature distributions are excluded. Every act is logged before or at
   execution.

## A27 — Canonical record definition (replaces v1 A27) [F18, F30]

The canonical tribunal record is the **chain of signed annotated tags at exact
commit hashes**, each externally anchored (Zenodo versioned DOI and/or
OpenTimestamps) before any action it gates; the default branch is a working
surface only. Each gated event cites the hash of the preceding anchored
commit. Execution logs form append-only descendants of anchored commits; no
history rewrite or force-push; tag deletion/re-pointing is a protocol
violation reported on discovery. `GOVERNANCE.md` is included in the freeze:
its SHA-256 at freeze time is recorded in `deposits/frozen-manifest.sha256`,
and it is supplied to the external reviewer with this package [F18].

## A29 — H-KHI-2 registrations (binding on any future Phase C) [F21, F22, F23, F24]

1. **Multiplicity** [F21]: the H-KHI-2 family comprises every
   (new_pair, attribute_endpoint) test actually run, Holm-corrected at family
   α = 0.01, endpoints = {attachment→status/moiety, color→name-class}. All
   failures logged and reported.
2. **No selection** [F22]: Phase C runs on **all** qualifying new pairs under
   that correction; no operator choice of target exists.
3. **E3 eligibility** [F23]: E3 credit requires that the target document's
   sealed attribute content was never publicly transcribed, digitized, or
   published before the latest training cutoff of any Team-P pretrained
   component. Otherwise H-KHI-2 runs as an E2 retrospective test only, and is
   so labeled.
4. **Freeze ordering** [F24]: the complete attribute taxonomy, mapping rules,
   model architecture/weights or fitting algorithm, feature set, and
   released-fields-only baseline are frozen and deposited **before Team P
   receives any numeric field of any prospective target pair**. Only
   deterministic inference on the frozen model follows.

## A30 — Reporting integrity for the null deliverable [F25]

Every report states |E| (= m or M_max), the number of scoreable triples, and
the number unscoreable by reason (N1 support, decoy-stratum deficiency,
transcription QC, power floor). Unless every triple is scoreable or a formal
bound accounts for the unscoreable mass, the registered null conclusion is
restricted to: **"No linkage passed among the scoreable registered triples;
X of Y registered triples were unscoreable (reasons enumerated)."** The phrase
"upper bound over the enumerated search universe" is prohibited outside that
condition.

## A31 — Feasibility note (informational, non-binding)

Stage-2 cost per survivor ≈ 2 nulls × 10,000·m draws; at m ≈ 2.5×10⁵ this is
~5×10⁹ DP alignments per survivor (order 10–100 core-hours, embarrassingly
parallel). The A20.8 attainability deposit must confirm this against the
realized m and registered survivor bound before Phase B.

---

## Explicitly unchanged

All frozen H-KHI-1/H-KHI-2 thresholds except the A22.1 null-(b)
operationalization (ratification R-1); A11 N1 construction; A12 custodian
(independent named human — never AI, never the operator); G7 tribunal for
headline claims; L5–L7 prohibitions; G9 equal-prominence nulls; the Santa
Valley pair's zero evidential weight.

## Verification round instructions (external reviewer, pass 2)

Supplied files must include this document, GOVERNANCE.md [F18], the v1 draft,
your review 01, and the four frozen program documents from pass 1. Verify:
(1) each of your 30 findings is implemented or explicitly ratified by the
operator (R-1, R-2); (2) the A20.6/A21/A22.2 arithmetic — recompute minimum
attainable p on both nulls at m = |E| for a worked example; (3) no new
discretionary degree of freedom was introduced by v2; (4) the A22.5 frozen
bins and A22.4 lottery close findings 8/20 without creating a new lever in
the metadata codebook; (5) whether R-1 is correctly characterized as a
permitted pre-data-contact amendment rather than a widening-in-disguise.
