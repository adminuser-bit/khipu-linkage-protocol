# Amendment Package — KHI Family Execution, v6 CONSOLIDATED (A20–A31)

**Status: DRAFT v6 — FREEZE CANDIDATE.** Supersedes
`AMD-2026-08-14-KHI-EXECUTION-v5-DRAFT.md` (retained, append-only; the
version chain v2→v3→v4→v5 is preserved in this directory).
**Version invariant (per review 05):** no substantive protocol text —
A20–A31, R-1, R-2, or the "Explicitly unchanged" list — differs from v4;
relative to v3, the only protocol-text changes are the [P3-V5] JCS hash
constructions + null_id definition and the [P3-V13] `UNSCOREABLE_N2_SUPPORT`
status/precedence, both adopted verbatim from
`REVIEW-2026-08-14-GPT-5.6-Sol-04-CONFIRMATION.md`, plus the A28.5
SHA-256(JCS(triple_id)) consistency edit certified sound in
`REVIEW-2026-08-14-GPT-5.6-Sol-05-FINAL.md`. Front-matter, version-history,
freeze-status, and closing-section text are administrative and change
across versions; **this document makes no exhaustive claim about literal
line-level deltas between versions** — literal diffs are recorded in git
history, which is the sole authority for them (two prior versions carried
false literal-delta claims, each blocked by external review — reviews 05
and 06). Review 06 records the compared v4/v5 protocol-body span as
byte-identical with SHA-256
`11cbd3fcc38a498d3b23b551d67504140b72c98d70121112aadf5529a124bebd`; the
v6 protocol body is byte-identical to v5's, verified by diff at
generation and independently checkable from git history. Prepared 2026-08-14 after verification pass
`REVIEW-2026-08-14-GPT-5.6-Sol-03-VERIFICATION.md` (verdict NOT CLEAR; 11
blocking MAJOR findings + 3 actionable MINOR — **all accepted**). Verification
findings are cited as [V#]; pass-1/pass-2 findings as [F#]/[A28-F#].
GOVERNANCE.md has been edited per [V11] and freezes with this package; its
SHA-256 at freeze enters `deposits/frozen-manifest.sha256` [F18].
Freezing requires: (1) operator ratification of R-1 and R-2 below
(instrument: `RATIFICATION-2026-08-14-R1-R2.md`); (2) signed tag
`freeze/amendments-v1` on an exact commit whose tree contains this document,
GOVERNANCE.md, and the updated frozen manifest, anchored **before** it gates
anything (GOVERNANCE R4 as amended). All substantive content is
externally certified (reviews 01–06); per review 06, no substantive
protocol finding remains, and administrative v4→v5→v6 changes are confined
to front-matter/version-history, freeze-status, and closing-section text.

## Operator ratification required

**R-1 — Explicit pre-data-contact substantive amendment of H-KHI-1 null (b)**
*(text per [V3], adopted verbatim).* Frozen H-KHI-1 null (b) required ≥100
same-genre decoy documents. This amendment replaces that requirement for this
run with exactly 25 same-stratum decoy documents selected by the A22.4
lottery, together with the A22.2 equal-document clustered-mixture null and
A22.3 strict rank-1 identity condition. This reduces the document-identity
panel from ≥100 to 25 and is therefore a **substantive weakening of that
component**, not a narrowing or mere clarification. It is adopted before any
H-KHI-1 scoring-data contact under the frozen amendment policy. Operator
signature constitutes explicit ratification of that change. (Context, recorded
not as justification but as disclosure: the literal frozen operationalization
was arithmetically unpassable — pure-rank minimum p = 1/(D+1) ≈ 0.0099 against
a 0.001 threshold — and both review layers required amendment over numerical
padding [F2, V3].)

**R-2 — Run-1 scope restriction** *(unchanged from v2; [V-review: "honestly
characterized"]).* The frozen two-human transcription requirement is
preserved. This run's adjudication universe is restricted to documents whose
numeric/group-structure transcription exists under scholarly human editorial
control (published critical editions); **Phase C / the H-KHI-2 E3 instrument
is blocked for this run** [F10, F23]. Run 1 is the E2 linkage experiment.

---

## A20 — Extent, two-stage architecture, and frozen Stage-2 inference

1. **Raw extent** [V4]. E_raw = U1 × G × D_cand is the full enumerated
   cross-product: every khipu in U1 (619), all four frozen groupings, every
   candidate document. No eligibility carve-outs at any level [F5].
2. **D_cand is mechanical** [F19]: all documents satisfying the frozen
   metadata-only eligibility rule (design §2.2: Peru, 1532–1700,
   visita/revisita/padrón/tasa, ≥20 grouped numeric entries per catalog or
   edition metadata, not content inspection) within the enumerated series,
   minus the decoy panel (A22.4 lottery) minus the positive-control document.
   No LLM or operator judgment touches membership; LLM triage may reorder
   processing only after membership is fixed, every suggestion logged (G5).
3. **Registered scoring extent** [V4]. If |E_raw| ≤ 1,000,000, set E = E_raw.
   If |E_raw| > 1,000,000, set E to exactly the first 1,000,000 triples under
   ascending SHA-256(JCS(["KHI-A20-LOTTERY-20260814", khipu_id,
   grouping_id, doc_id])) per A20.9 [P3-V5]. Thereafter **E means only the registered scoring extent
   and m = |E|**, deposited at `freeze/A0-universe-v1` before any scoring.
   Triples in E_raw \ E are reported as outside the deterministic sampled
   universe and receive no test status or p-value; all null-result language
   must then say "over the deterministic sampled universe."
4. **m never shrinks** [F6]: once frozen, no later scoreability failure
   reduces m. An unscoreable triple (A21, A22.5, A25.6) remains a registered
   test with no positive-claim eligibility, assigned p = 1 for multiplicity
   accounting.
5. **Stage 1 — screening.** Every triple in E scored with **exactly 9,999 N1
   draws and exactly 9,999 N2 draws** [A28-F3], the A20.6 add-one estimator,
   ties as exceedances, streams seeded SHA-256(JCS(["KHI-S1", khipu_id,
   grouping_id, doc_id, null_id])) [P3-V5], Monte Carlo uniformly (no exact-enumeration substitution at
   Stage 1), no adaptive extension, no rerun. Survivors: empirical p ≤ 0.01 on
   both nulls [F27]. All Stage-1 draws, exceedance counts, and statistics are
   discarded for inference [F3]; logged and reported descriptively only.
6. **Stage 2 — confirmatory, single frozen algorithm** [F4]: per survivor, per
   null: plain Monte Carlo, no importance sampling, no sequential stopping, no
   adaptive proposals, N = 10,000·m draws, fresh stream seeded
   SHA-256(JCS(["KHI-S2", khipu_id, grouping_id, doc_id, null_id])) [P3-V5], independent of every Stage-1
   stream; no Stage-1 draw, exceedance count, adaptive proposal, or fitted
   tail parameter may enter the Stage-2 p-value [F3]. Estimator: add-one
   empirical p = (1 + #{null ≥ observed}) / (1 + N); ties count as
   exceedances. Minimum attainable p = 1/(1 + 10,000·m) < 0.001/m — a 10×
   resolution margin [V2] — valid only where A21 support holds.
7. **Adjudication** (frozen text as amended by R-1): H1 requires Stage-2
   p < 0.001, Holm-corrected at denominator m, on N1 **and** the A22.2
   mixture null, **and** the A22.3 rank-1 identity condition.
8. **Attainability and capacity** [F1, V12]: the deposited power analysis
   must show, before Phase B, for the frozen m: (a) Stage-2 resolution
   < 0.001/m; (b) A21 support floors computable for every triple from
   pre-score quantities; (c) expected compute. **No Stage-1 survivor cap
   alters inference. Before Phase B the operator deposits a computational
   capacity S_max for planning only. If the realized number of Stage-1
   survivors exceeds S_max, no survivor subset may be selected or
   adjudicated; Stage 2 is suspended for all survivors until resources
   sufficient to score all survivors under identical frozen rules are
   provisioned. The excess itself is reported. S_max never changes E, m, or
   eligibility** [V12].
9. **Hash canonicalization** [V5] *(adopted verbatim; binds every lottery and
   RNG seed in this package)*: Every lottery and RNG seed uses RFC-8785
   canonical JSON serialized as UTF-8. `khipu_id` is the exact primary
   identifier in the pinned U1 table; `grouping_id` is exactly one of `"G-1"`,
   `"G-2"`, `"G-3"`, `"G-4"`; `doc_id` is the unique
   institution/fonds-series/item identifier produced by the frozen metadata
   codebook. A document lacking one unambiguous canonical item identifier is
   ineligible this run. `triple_id` is the canonical JSON array
   `[khipu_id, grouping_id, doc_id]`. No alias, normalization choice,
   alternative identifier, delimiter choice, or ID reassignment is permitted
   after enumeration begins. **For all domain-separated hashes, `JCS(x)`
   means RFC-8785 canonical JSON serialized as UTF-8, and the SHA-256 input
   is exactly `JCS(x)` with no prefix, suffix, delimiter, or additional
   normalization. `null_id` is exactly `"N1"` or `"N2"`** [P3-V5].

## A21 — Finite-support scoreability [F1, V1]

**N1:** let M₁ be the number of distinct admissible N1 permutation images of
the candidate document, computed or conservatively lower-bounded
combinatorially from group sizes, subtotal constraints, and tie profiles by
frozen code — never by sampling. Confirmatorily scoreable on N1 only if
**M₁ > 1000·m** (1/M₁ < 0.001/m).

**N2** *(replaces the v2 sum formula; [V1] adopted verbatim)*: let D be the
number of matched decoy documents and M_d the number of distinct admissible
A11 permutation images of decoy d. Because A22.2 samples documents uniformly
and then images uniformly conditional on document, N2 support is
probability-weighted, not S₂ = Σ_d M_d. The conservative finite-support
scoreability condition is **D · min_d M_d > 1000·m**, equivalently the maximum
null atom 1/(D · min_d M_d) < 0.001/m. The sum of permutation counts may be
reported descriptively but is not an effective-support denominator.

Monte Carlo draws never increase effective support beyond the exact
permutation universe. Triples failing either condition are unscoreable, remain
in m at p = 1, and are reported with both descriptive p-values.

## A22 — N2 construction, stratified decoys, lottery assignment

1. **Registered amendment to H-KHI-1 null (b)** — ratified as R-1: the decoy
   requirement is operationalized as the conjunction of A22.2 and A22.3, with
   a 25-document same-stratum panel (disclosed weakening from ≥100; R-1).
2. **N2 clustered-mixture null** [F2]: one draw = (select a decoy document d
   uniformly from the triple's matched 25-document stratum panel — equal
   weight per document, never per permutation — then draw one admissible A11
   structure-preserving permutation image of d). Carries the Stage-2 Holm
   requirement p < 0.001/m under the A20.6 estimator; support per A21.
3. **Rank-1 identity condition** [F2, F29]: the candidate document's
   unpermuted score must strictly exceed the unpermuted score of every decoy
   document in its matched panel; the exact identity-support p = 1/(D+1) is
   reported as-is and never conflated with the mixture p-value.
4. **Panel membership by hash lottery** [F20, V5]: within each frozen stratum,
   eligible documents are ordered by ascending
   SHA-256(JCS(["KHI-A22-LOTTERY-20260814", doc_id])) per A20.9 [P3-V5];
   the first 25 per stratum are decoys; the remainder are candidates. The
   positive-control document is the single predesignated exception (excluded
   from both). The complete assignment is deposited at A0 before any numeric
   transcription.
5. **Strata, frozen bins** [F8, V6]: **period ∈ {1532–1581, 1582–1631,
   1632–1681, 1682–1700}; documents may be compared only within the same
   period bin** (strictly within the ±50-year envelope, never wider) [V6];
   region = audiencia (Lima, Charcas, Quito; outside → unscoreable); type ∈
   {visita, revisita, padrón, tasa}; entry-count bins {20–49, 50–99, 100–199,
   ≥200}. A candidate is scored only against decoys matching all four axes.
   A stratum with <25 decoys renders its candidates unscoreable this run
   (they remain in m at p = 1); no same-run panel extension exists.
6. **Metadata codebook** [V7] *(adopted verbatim)*: The metadata codebook is
   frozen and externally anchored **before the first item-level enumeration
   result is inspected**. It contains the complete recognized-label →
   canonical-category mapping and normalization rules. Missing, conflicting,
   multi-valued, or previously unseen values on any load-bearing axis are
   coded `UNRESOLVED` and make the document ineligible/unscoreable this run;
   no label may be added, reclassified, or remapped after enumeration begins.

## A23 — Positive control under PC-G [F9, F28]

The Santa Valley control is scored under **PC-G**, a positive-control-only
grouping algorithm reproducing exactly the published Medrano & Urton (2018)
grouping procedure, implemented from the paper's description with a frozen
test fixture (the published 132/133 alignment), code hash deposited before
execution. PC-G is not G-1..G-4, appears nowhere in E, carries zero evidential
weight, and sits outside the Holm family. **Pass criterion:** the six Corongo
khipus (OKR IDs deposited at A0) vs the 1670 revisita achieve p < 0.001,
uncorrected, on N1 and on the A22.2 mixture null over the control's matched
stratum panel, plus the A22.3 rank-1 condition. Failure ⇒ pipeline defect,
family-wide quarantine (frozen text); G-1..G-4 results reported descriptively.

## A24 — Roles, invocation integrity, operator information boundary

1. Role disjointness by agent context isolation (v2 text retained): each role
   (data steward; archival triage; transcription keys; scoring executor; red
   team) is a separate agent invocation sharing no conversation state,
   receiving only its role's licensed inputs. Internal same-lineage agreement
   is never corroboration; G7 unchanged.
2. **Invocation wrapper** [F15, V9]: every AI invocation in any registered
   role runs through a frozen wrapper that (a) assigns a monotonic run ID;
   (b) **creates and pushes to the protected record a commit containing the
   monotonic run ID, prompt hash, model ID, and decoding settings before
   invoking the model, and verifies that the remote contains that commit; if
   the push fails, the invocation may not occur** [V9]; (c) **immediately
   after return, error, abort, or timeout, automatically hashes the complete
   raw output/error state and creates and pushes an append-only result commit
   before another registered invocation may begin** [V9]; (d) forbids silent
   retries — every retry capable of affecting search, transcription, or
   triage is a registered attempt in the G5 log. Manual direct invocations
   are inadmissible.
3. **Frozen model manifest** [F16]: before first use in each role, exact model
   IDs/versions, API mode, system prompts, temperature/top-p, seeds where
   supported, vision resolution and cropping rules, permitted tools, and
   network state are deposited. Unavailability triggers a dated amendment,
   never a quiet substitution.
4. **Operator information boundary** [F14]: the operator is procedurally and
   cryptographically denied all Phase-C sealed attribute content until Team-P
   prediction deposit; full-document handling of any potentially E3-eligible
   document is performed by the independent human custodian; the operator may
   receive only redacted numeric-field material; sealed ciphertexts and
   custodian logs are not operator-readable before deposit. (Phase C blocked
   this run per R-2; rule binds any future run under this record.)

## A25 — Transcription and source QC

1. **The frozen two-human requirement is preserved** [F10]. No AI substitution
   enters the preregistered adjudication path.
2. **Adjudication universe restriction** (R-2): candidate and decoy documents
   must have numeric fields and group structure attested in a published
   scholarly transcription produced under human editorial control. Unpublished
   manuscripts are excluded from adjudication this run; work on them is a
   labeled pilot whose outputs cannot enter registered scoring.
3. **Print-to-machine keying:** two independent keying passes from the
   edition. AI keyers permitted for this non-adjudicative mechanical step only
   under [F11] conditions: anonymized page/crop images (title, archive,
   document identity removed); network and retrieval disabled; A24.3 manifest;
   outputs auto-archived via A24.2. Inter-keyer agreement is reported only as
   inter-model agreement, never accuracy evidence.
4. **Deterministic disagreement resolution** [F13]: two-of-three identical
   keys determine a value; three-way or structural disagreement goes to an
   independent human reader blind to all linkage scores; unresolvable →
   coded missing/uncertain by frozen rule. The operator never chooses a value.
5. **Source-grounded verification** [F12]: n_check = min(F, max(ceil(0.05·F),
   598)) fields per document, seeded sample; pass iff the one-sided 95% exact
   binomial upper bound on the field error rate is ≤ 0.005; if F < 598, all
   fields are checked and the exact error rate reported. Group boundaries and
   hierarchy checked separately: 100% agreement or explicit uncertain coding.
   For every Stage-2 survivor, 100% of fields verified before adjudication is
   reported.
6. **Edition selection and field states** [F26, V8]: *(first sentence per
   [V8], adopted verbatim)* Where multiple admissible editions exist,
   primary-edition selection is mechanical and precedes linkage scoring:
   coverage = the count of printed numeric/group-structure fields, counting
   each of the five registered field states exactly once regardless of its
   value; choose the edition with the largest coverage count; ties are broken
   by latest publication date, then by lexicographic normalized
   DOI/ISBN/full citation. Neither numeric values nor any comparison with
   khipu data may enter edition selection. The counts and selected edition
   are deposited before any linkage score for that document is computed.
   Every field carries a state from {observed, editorially-restored,
   uncertain, illegible, supplied-subtotal}; primary scoring uses `observed`
   only; other states enter only the registered sensitivity treatment S2.
   Documents failing QC do not enter scoring (triples remain in m at p = 1).

## A26 — Historical declaration and prospective acquisition rule [F17]

1. No retroactive ratification.
2. **Historical declaration (deviation record):** design-time real-corpus acts
   in the program archive — the Linear A designer's decoding/counting of
   lineara.xyz records; the shadow-harness designer's derivation and
   publication of the Linear A length multiset — are recorded as A17 protocol
   deviations affecting those families. For family KHI: no content-level act
   beyond the registered Run 2 audit is known; Phase-0 repository acts are
   byte-level only, enumerated in `logs/operator-log.md`. Any additionally
   discovered pre-freeze act is reported as a deviation on discovery.
3. **Prospective rule:** after `freeze/amendments-v1` and before inferential
   scoring, a designated steward agent may perform only enumerated byte/schema
   acts (download, hash, file size, schema/table row counts, mechanically
   specified identifier resolution), logged before or at execution; these may
   populate manifests but may not inform thresholds, groupings, eligibility,
   nulls, candidate selection, power floors, or scoring code. Content-level
   statistics and feature distributions are excluded.

## A27 — Canonical record definition [F18, V11]

The canonical tribunal record is the **chain of signed annotated `freeze/*`
tags at exact commit hashes, each externally anchored before any action it
gates**; the default branch is a protected working surface and append-only
execution record, not itself a frozen canonical state. Each gated event cites
the hash of the preceding anchored commit. Execution logs form append-only
descendants of anchored commits; no history rewrite or force-push; tag
deletion/re-pointing is a protocol violation reported on discovery. A freeze
tag must point to a tree already containing its frozen-manifest update; **no
action gated by a freeze may occur while its anchoring is absent or pending**
(GOVERNANCE R4 as amended [V11]). GOVERNANCE.md as amended freezes with this
package; its SHA-256 enters `deposits/frozen-manifest.sha256` at freeze.

## A28 — Screen-Positive Non-Adjudicated Triples (SPNA)

1. **Membership** [A28-F2, F10, F13]. A triple in E (registered scoring
   extent only [V4]) is screen-positive iff Stage-1 yields p ≤ 0.01 on both
   nulls. It is **SPNA** iff it additionally (a) is confirmatorily scoreable
   under every frozen Stage-2 requirement, (b) actually completes Stage 2,
   and (c) does not satisfy adjudication. A screen-positive triple failing
   (a) or (b) is reported separately as `screen-positive / unscoreable`,
   holds no SPNA status, and may not enter the future-priority artifact.
   Membership in this band has no effect on Stage-2 eligibility, Holm
   ordering, m, any p-value, any E-class, or any success/disconfirmation
   decision.
2. **Exact Stage-1 freeze** [A28-F3, V14]. SPNA membership is computed using
   exactly 9,999 N1 draws and exactly 9,999 N2 draws **(matching A20.5
   exactly)**, the A20.6 add-one formula, ties as exceedances, the A20.5 seed
   derivation, no adaptive extension, no rerun, no exact-enumeration
   substitution at Stage 1. Any different draw count, seed, estimator, or
   retry is a different exploratory analysis and cannot alter the SPNA list.
3. **Terminal status** [A28-F10, V13, P3-V13]. Every triple in E receives
   exactly one terminal status from: `S1_ONLY_FAIL_RAW`,
   `S2_FAIL_BOTH_NULLS`, `S2_FAIL_N1`, `S2_FAIL_N2`, `S2_FAIL_HOLM`,
   `S2_FAIL_DECOY_RANK`, `UNSCOREABLE_N1_SUPPORT`, `UNSCOREABLE_N2_SUPPORT`,
   `UNSCOREABLE_DECOY_STRATUM`, `UNSCOREABLE_QC`, `PASS_ADJUDICATION`.
   **Precedence (frozen; first matching state wins): Stage-1 raw failure →
   N1-support → N2-support → decoy-stratum → QC → both Stage-2 raw nulls
   fail → N1 only → N2 only → Holm → decoy-rank → pass.** Only `S2_FAIL_*`
   statuses are SPNA-eligible.
4. **Joint-null reference bounds** [A28-F4, V10] *(adopted verbatim)*. No
   fitted or simulated joint-null expectation E₀[L] is claimed in this run
   because no joint N1/N2 calibration generator has been preregistered and
   validated before this freeze. Every screen-positive-count report therefore
   states the observed N, the independence reference m·10⁻⁴, and the
   dependence-robust Fréchet range 0 ≤ E₀[L] ≤ m·10⁻², all explicitly labeled
   non-adjudicative. No comparison of N with either reference licenses a
   directional claim. A calibrated E₀[L] may be introduced only by a future
   pre-data-contact amendment that fully specifies and validates the
   joint-null generator, subsample/allocation rule, simulation count, seeds,
   diagnostics, uncertainty interval, and extrapolation rule.
5. **Mandatory exhaustive, non-salient reporting** [A28-F5, F7, F12]. All
   screen-positive triples (SPNA and unscoreable) are reported in one
   standardized machine-readable table with all p-values, grouping, stratum,
   and terminal status; suppression or subset reporting is a protocol
   violation (G5); zero screen-positives is likewise reported. Prose/PDF
   renderings use deterministic SHA-256(JCS(triple_id)) order [P3-V5 rule], never score or
   p-value order. No individual triple receives a figure, case study,
   narrative paragraph, or headline treatment (sole exception: documenting a
   protocol anomaly). A p-sorted companion table may be generated
   mechanically only if labeled exploratory and accompanied by the complete
   table and clause-4 numbers. The program does not publish "top-N,"
   "strongest," "closest," or threshold-distance rankings.
6. **Future-use rule** [A28-F1, F8, F9]. (a) An SPNA triple may seed future
   archival research but may not obtain confirmatory evidential status by
   re-scoring the same underlying khipu–document data; a future same-data
   analysis is admissible only as a continuation of this run's original
   multiplicity family: the original frozen m remains the minimum denominator,
   the selection event is disclosed, and no screen-informed scoring or null
   change may reduce that burden; re-randomization is not independent
   evidence. (b) A same-data continuation may inherit m only if the scoring
   statistic, grouping definitions, null constructions, and eligibility rules
   are unchanged; any screen-informed change is an additional searched
   analysis requiring its own frozen multiplicity family or exploratory-only
   status; a method designed after viewing the screen cannot confirm screen
   members on the same data. (c) Confirmation requires genuinely independent
   evidence that played no role in this run's screening (preregistered sealed
   archive stratum, newly obtained independent document, newly recorded
   khipu evidence), constituting a new confirmatory family with its own
   correction. (d) Archive expansion motivated by screen-positives is
   **lead-conditioned discovery**: documents so discovered generate
   hypotheses only; an E2 claim from a lead-conditioned search requires
   either an independent confirmatory stratum frozen before inspection and
   not selected using A28 information, or multiplicity over the full
   lead-conditioned search tree, logged under G5.
7. **No claim, any channel** [A28-F6]. SPNA triples license no claim at any
   E-class, binding all program-controlled communications (papers, abstracts,
   titles, press releases, websites, grant applications, presentations,
   interviews, repository READMEs, social-media posts, correspondence). The
   terms "lead," "signal," "suggestive," "promising," "near match,"
   "candidate," "correspondence," "match," and equivalents are prohibited for
   these triples; no triple may be highlighted, ranked, named, or illustrated
   outside the clause-5 table; participants may not endorse third-party
   evidential characterizations; counts are never directional findings and
   do not aggregate.
8. **Required family-result phrasing** [A28-F5, F11, V10]: *"Zero of m
   registered triples satisfied H-KHI-1 adjudication. N triples met the
   preregistered computational screening rule (p_N1 ≤ 0.01 and p_N2 ≤ 0.01);
   the screening count is exploratory, has no E-class licensing, and must be
   interpreted against **the preregistered joint-null reference bounds in
   clause 4**. Screen-positive triples are not evidence of linkage."* The
   count does not modify, relax, interpolate, or qualify the H-KHI-1
   threshold and is not an estimator or bound on true-linkage prevalence;
   the family-null interpretation rests solely on adjudicated, scoreable
   tests and complies with A30.
9. **No intermediate bands** [A28-F15]. No reporting tier may exist between
   SPNA and adjudicated passes; descriptions of near-threshold Stage-2
   results beyond their numeric values in the clause-5 table are prohibited
   in all program-controlled communications.

## A29 — H-KHI-2 registrations (binding on any future Phase C) [F21–F24]

1. The H-KHI-2 family comprises every (new_pair, attribute_endpoint) test
   actually run, Holm-corrected at family α = 0.01; endpoints =
   {attachment→status/moiety, color→name-class}; all failures logged.
2. Phase C runs on all qualifying new pairs; no operator target selection.
3. E3 credit requires the target document's sealed attribute content was
   never publicly transcribed, digitized, or published before the latest
   training cutoff of any Team-P pretrained component; otherwise E2
   retrospective only, so labeled.
4. The complete attribute taxonomy, mapping rules, model
   architecture/weights or fitting algorithm, feature set, and
   released-fields-only baseline are frozen and deposited before Team P
   receives any numeric field of any prospective target pair; only
   deterministic inference follows.

## A30 — Reporting integrity for the null deliverable [F25]

Every report states |E_raw|, |E| (= m), the number of scoreable triples, and
the number unscoreable by reason (N1 support, N2 support, decoy stratum,
transcription QC). Unless every triple is scoreable or a formal bound accounts
for the unscoreable mass, the registered null conclusion is restricted to:
"No linkage passed among the scoreable registered triples; X of Y registered
triples were unscoreable (reasons enumerated)." The phrase "upper bound over
the enumerated search universe" is prohibited outside that condition; where
A20.3 sampling applied, all universe language says "deterministic sampled
universe."

## A31 — Feasibility note (informational, non-binding)

Stage-2 cost per survivor ≈ 2 nulls × 10,000·m draws (order 10–100 core-hours
at m ≈ 2.5×10⁵, embarrassingly parallel). Note per [V1]: the N2 support
condition D·min_d M_d > 1000·m requires every decoy in a scoreable triple's
panel to admit >10⁷ permutation images at D = 25, m = 2.5×10⁵ — small
tie-heavy decoy documents will fail this, and substantial unscoreable mass is
expected and reported per A30. The A20.8 deposit must confirm realized
figures before Phase B.

---

## Explicitly unchanged

All frozen H-KHI-1/H-KHI-2 thresholds except the R-1 null-(b)
operationalization; A11 N1 construction; A12 custodian (independent named
human — never AI, never the operator); G7 tribunal for headline claims; L5–L7
prohibitions; G9 equal-prominence nulls; Santa Valley zero evidential weight.

## Certification record

External G7 review (GPT-5.6 Sol, OpenAI lineage), five passes, all committed
verbatim in this directory: 01 (main package, 30 findings), 02 (A28, 16
findings, REVISE AND ADOPT), 03 (verification, NOT CLEAR, 11 blocking), 04
(confirmation: P3-V5 and P3-V13 blocking), 05
(final: P3-V5 CONFIRMED, P3-V13 CONFIRMED, A28.5 CONFIRMED SOUND;
substantive invariant PASSES; blocked v4's false literal self-description),
06 (byte-level v4→v5 comparison: protocol-body invariant CONFIRMED, body
span SHA-256 11cbd3fc…a124bebd; blocked v5's residual false "sole delta"
sentence, replaced in this version per the reviewer's authorized
formulation). Every finding across all passes was accepted and implemented
or operator-ratified (R-1, R-2). Review 06: "No substantive protocol
finding remains."
