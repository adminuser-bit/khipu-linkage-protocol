# A28 — Screen-Positive Non-Adjudicated Triples (v2)

**Status: DRAFT v2 — NOT FROZEN.** Joins `AMD-2026-08-14-KHI-EXECUTION-v2-DRAFT.md`
for verification pass 2 and freezes with it under `freeze/amendments-v1`.
Supersedes the v1 A28 draft reviewed in
`REVIEW-2026-08-14-GPT-5.6-Sol-02-A28.md` (verdict: REVISE AND ADOPT; 16
findings, **all accepted**; implementations cited as [F#] against that review).
The band is renamed from "registered leads" to **screen-positive
non-adjudicated triples (SPNA)** [F5, F16]; the word "lead" appears below only
inside the technical term "lead-conditioned discovery."

**Origin:** operator inquiry 2026-08-14 (whether sub-threshold results have a
legitimate home). Adjudication thresholds are untouched; this creates a
claim-free exploratory reporting tier.

## Binding text

1. **Membership** [F2, F10, F13]. A triple is **screen-positive** iff its
   Stage-1 screening (A20.5) yields empirical p ≤ 0.01 on both N1 and N2. A
   screen-positive triple is **SPNA** iff it additionally (a) is confirmatorily
   scoreable under every frozen Stage-2 requirement (A21 support floors, A22.5
   decoy stratum, A25.6 QC), (b) actually completes Stage 2, and (c) does not
   satisfy adjudication. A screen-positive triple failing (a) or (b) is
   reported separately as `screen-positive / unscoreable`, holds no SPNA
   status, and may not enter the future-priority artifact (clause 6).
   Membership in this band has no effect on Stage-2 eligibility, Holm
   ordering, m, any p-value, any E-class, or any success/disconfirmation
   decision.

2. **Exact Stage-1 freeze** [F3]. SPNA membership is computed using **exactly
   9,999 N1 draws and exactly 9,999 N2 draws** (this fixes A20.5's "≥10,000"
   to 9,999 for both nulls), the A20.6 add-one empirical-p formula, ties
   counted as exceedances, streams seeded SHA-256("KHI-S1" ∥ triple_id ∥
   null_id), with no adaptive extension, no rerun, and no exact-enumeration
   substitution at Stage 1 (Monte Carlo uniformly, for band comparability).
   Any different draw count, seed, estimator, or retry is a different
   exploratory analysis and cannot alter the SPNA list.

3. **Terminal status** [F10]. Every triple in E receives exactly one terminal
   status from the closed set: `S1_ONLY_FAIL_RAW`, `S2_FAIL_N1`, `S2_FAIL_N2`,
   `S2_FAIL_HOLM`, `S2_FAIL_DECOY_RANK`, `UNSCOREABLE_N1_SUPPORT`,
   `UNSCOREABLE_DECOY_STRATUM`, `UNSCOREABLE_QC`, `PASS_ADJUDICATION`. The
   status is part of the recorded object; only completed, scoreable Stage-2
   failures (`S2_FAIL_*`) are SPNA-eligible.

4. **Joint-null calibration** [F4]. Before any Phase B scoring, a calibration
   procedure is frozen and deposited that estimates the expected
   screen-positive count under H0, E₀[L] = Σᵢ qᵢ with
   qᵢ = P_H0(p_N1 ≤ 0.01 ∧ p_N2 ≤ 0.01), **preserving the actual N1/N2
   dependence structure** (nested simulation on a deterministic stratified
   subsample of E, seeds and extrapolation rule frozen; code hash deposited).
   Every SPNA-count report states: observed N, calibrated E₀[L] with a
   simulation uncertainty interval, and the dependence-robust reference bounds
   (independence reference ≈ m·10⁻⁴; valid worst-case upper reference ≈
   m·10⁻²), each explicitly labeled non-adjudicative. If calibration fails
   its own diagnostics, the report carries the two reference bounds and says
   the calibrated expectation is unavailable.

5. **Mandatory exhaustive, non-salient reporting** [F5, F7, F12, F14].
   All screen-positive triples (SPNA and unscoreable) are reported in **one
   standardized machine-readable table** with both Stage-1 and (where run)
   Stage-2 p-values, grouping, stratum, and terminal status. Suppression or
   subset reporting is a protocol violation (G5); zero screen-positives is
   likewise reported. In any prose/PDF rendering the table appears in
   deterministic SHA-256(triple_id) order, never sorted by score or p-value.
   No individual triple receives a figure, case study, narrative paragraph, or
   headline treatment (sole exception: documenting a protocol anomaly). A
   p-sorted companion table may be generated mechanically only if labeled
   exploratory and accompanied by the complete table and clause-4 numbers.
   The program does not publish "top-N," "strongest," "closest," or
   threshold-distance rankings; ordering by p-value is an exploratory
   operation with zero claim licensing.

6. **Future-use rule** [F1, F8, F9 — replaces v1 clause 4 in full].
   a. An SPNA triple may seed future archival research but **may not obtain
      confirmatory evidential status by re-scoring the same underlying
      khipu–document data.** A future same-data analysis is admissible only as
      a **continuation of this run's original multiplicity family**: the
      original frozen m remains the minimum multiplicity denominator, the
      original selection event is disclosed, and no scoring or null change
      informed by the screen may reduce that burden. Mere re-randomization or
      re-permutation of the same observations is not independent evidence.
   b. A same-data continuation may inherit the original m **only if** the
      scoring statistic, grouping definitions, null constructions, and
      eligibility rules are unchanged. Any screen-informed change to those
      elements is an additional searched analysis: it must either join a
      frozen multiplicity family covering all alternative methods tried, or
      be treated as exploratory only. A method designed after viewing the
      screen cannot confirm screen members on the same data.
   c. Confirmation of an SPNA hypothesis requires **genuinely independent
      evidence that played no role in this run's screening** — e.g., a
      preregistered sealed portion of the archival record, a newly obtained
      independent document, or newly recorded khipu evidence — which may
      constitute a new confirmatory family with its own multiplicity
      correction.
   d. **Lead-conditioned discovery** [F8]: archive expansion motivated by
      screen-positive triples is so labeled. Documents discovered through
      that path generate hypotheses but are not automatically confirmatory
      evidence for the motivating khipu. An E2 linkage claim arising from a
      lead-conditioned search requires either (i) an independent confirmatory
      archive stratum, frozen before inspection and not selected using any
      A28 information, or (ii) multiplicity correction over the full
      lead-conditioned search tree — every screen member used to choose
      archives and every document inspected in consequence — with the search
      tree and branching decisions logged under G5.

7. **No claim, any channel** [F6]. SPNA triples license no claim at any
   E-class. The restriction binds **all program-controlled communications**:
   papers, abstracts, titles, press releases, websites, grant applications,
   presentations, interviews, repository READMEs, social-media posts, and
   correspondence describing results. The terms "lead," "signal,"
   "suggestive," "promising," "near match," "candidate," "correspondence,"
   "match," and equivalent evidential language are prohibited for these
   triples; no triple may be highlighted, ranked, named, or illustrated
   outside the clause-5 table. Program participants may not endorse
   third-party evidential characterizations. Aggregation is barred: counts
   are never directional findings, and "many weak matches" do not sum
   (H-ONO-1 discipline by analogy).

8. **Required family-result phrasing** [F5, F11]. The registered null
   deliverable is stated as: *"Zero of m registered triples satisfied H-KHI-1
   adjudication. N triples met the preregistered computational screening rule
   (p_N1 ≤ 0.01 and p_N2 ≤ 0.01); the screening count is exploratory, has no
   E-class licensing, and must be interpreted against its preregistered
   joint-null expectation E₀[L]. Screen-positive triples are not evidence of
   linkage."* The screen-positive count does not modify, relax, interpolate,
   or qualify the H-KHI-1 threshold and is not an estimator or bound on the
   prevalence of true linkages; the family-null interpretation rests solely
   on adjudicated, scoreable tests, and all upper-bound language additionally
   complies with A30 [F11].

9. **No intermediate bands** [F15]. No reporting tier may exist between SPNA
   and adjudicated passes. Descriptions of near-threshold Stage-2 results
   beyond their numeric values in the clause-5 table are prohibited in all
   program-controlled communications (A1 "promising trend" discipline).

## Interaction note

Clause 2 narrows A20.5 (N2 draws fixed at exactly 9,999); no other A20–A31
text is modified. This amendment widens nothing: the band is definitionally
claim-free and alters no registered test.
