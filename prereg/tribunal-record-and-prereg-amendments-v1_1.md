# Cross-Model Tribunal Record & Preregistration Amendment Appendix v1.1

**Date:** August 11, 2026
**Tribunal composition:** 3 internal blind scorers + 2 internal falsifiers (Claude/Fable family) · GPT 5.6-Sol (independent, two-stage blind protocol) · convened by L. Heller
**Status of amendments:** All entered before Run 3 data contact for every affected hypothesis. Permitted under the frozen preregistration's amendment policy (dated changelog; frozen text untouched). The frozen document `run2-preregistration-FROZEN.md` remains canonical; this appendix binds all Run 3 work.

---

## Part I — Tribunal adjudication record

### I.1 Meta-finding (headline)

The three internal scorer personas (info-theory, philology, ML-practice) produced **unanimous** E2 ratings on all systems the external tribunal member demoted on gate grounds (Indus, Cypro-Minoan, Voynich, SE Iberian, SW/Tartessian, Isthmian, Eteocypriot, Zapotec). Persona diversity within one model family did not produce judgment independence on the gate question. The internal falsification pass caught three over-ratings (Cretan Hieroglyphic, Eteocypriot, Zapotec) but passed Indus, Cypro-Minoan, and Voynich as "weakened." The blind cross-model pass independently located the gate boundary the internal pipeline missed. **Consequence: the cross-model tribunal is confirmed as load-bearing for all headline claims (rule G7); internal agreement, however structured, is never sufficient.**

### I.2 Adjudicated statuses (disputed systems)

| System | Internal (post-falsification) | Sol Stage A | Final adjudicated | Basis |
|---|---|---|---|---|
| **Indus** | E2 "structural only" | E1 | **E2 / L1–L3 predictive-structural claims only; E1 language-status; E0 readings** | Split verdict. Preregistered structural predictions against withheld real objects (sequences, object type, provenance) satisfy §2. H-IND-2 relabeled (A2). Conditions: dedup at object-family level; both allography treatments frozen; contamination controls; predictions defined before holdout exposure; no linguistic interpretation of predictive success. |
| **Cypro-Minoan** | E2 "classificatory" | E1 | **E1 under H-CM-1 as originally written; E2 available only for the rewritten distributional claim (A10)** | Sol objection sustained: failure to separate ≠ evidence of unity (failure-to-reject-H0-as-proof error). Operational defects noted by internal falsifier (withheld source images; embeddings inherit the under-test team's preprocessing; CM2/Enkomi confound) stand. |
| **Voynich** | E2 "class question" | E1 | **E1 — model-comparison only** | Sol objection sustained in full. Held-out folios carry observations, not class labels; no stratification fix supplies the missing truth label. H-VOY-0/1 remain valuable and will run; conclusions restricted (A14). |
| **Eteocypriot** | E1 (refuted) | E2 | **E1** | Sol reversed. Bilinguals are consumed evidence, known for generations, not contamination-free holdouts; the assumed unpublished IG XV reserve was published in 2020 and is mostly Greek syllabic. *Canonical example: "bilingual exists" and "E2 exists" are not synonyms.* |
| **Eteocretan** | E1 | E2 | **E1** | Sol reversed. Five texts, all long published, all consumed by every claimant; one bilingual stone physically lost. High in-principle falsifiability without held-out instrument = E1 under this program's severe gate. |
| **Zapotec** | E1 (refuted) | E2-narrow | **E1** | Sol reversed. The externally checkable stratum is the already-solved pan-Mesoamerican calendrics; a solved subsystem is a benchmark, not a truth condition for the unsolved subsystem. E1 agenda (digitize Urcid corpus, calendrical recognition benchmarks, distributional classes) endorsed. |
| Cretan Hieroglyphic | E1 (refuted) | E1 | **E1** | Unanimous. |
| Phaistos Disc | E0, all scorers | E0 | **E0 — negative control** | Unanimous; control integrity rules tightened (A16). |
| Oracle Bone subset | E2 upheld | E3-available | **E2 now; E3 path via external adjudication (A7)** | Strongest system in program. |
| Khipu | E2 (weakened) | E3-available | **E2 now; E3 path via two-team masking design (A12)** | |
| Proto-Elamite | E2 upheld | E2 structural/semantic | **E2 — structural/semantic claims; no phonetic/language-identity route** | |
| Meroitic | E2 (weakened) | E2 (not E3 yet) | **E2; E3 contingent on custodian-sealed reserve (A9)** | |

Systems not listed retain their Checkpoint 2 matrix status, subject to the claim-band conversion (A18).

### I.3 Factual reconciliations (from Sol Stage A audit, verified internally)

1. **Canonical inventory count: 82.** Run 1 array verified by direct count at 72 unique entries; the merge agent's prose note ("68 entries") is erroneous and is struck. Run 2 added 10 non-colliding entries. Caveat: Tărtăria, Gradeshnitsa, and Karanovo were split out of the former single Vinča entry.
2. **Error reporting language:** "N agents, 0 errors" is replaced program-wide by the form "N agents; no agent-run failures; K citation-verification failures subsequently corrected."
3. **Corrections that supersede Run 1 text** (canonical as of this record): Byblos has one machine-readable sign-level corpus (Elamicon); the Corazza Cypro-Minoan source images are withheld (only code/vectors/models public); ICIT is alive behind HTTP authentication without public bulk access; Eteocypriot secure corpus ≈ 26 inscriptions (the "several hundred" figure was wrong, not uncertain); Zapotec figures are Urcid's 570 epigraphic examples (Grokipedia-derived figures struck); Linear Elamite transliterations use Private Use Area codepoints + custom font, not standard Unicode.
4. **Unit-mismatch registry (A19):** Indus sign inventory 417 (Mahadevan) vs ~694 (Wells–Fuls); OBS historical "~3,000 undeciphered graphs" vs HUST-OBC's 9,411 undeciphered *categories* (mapping graph-type ↔ category ↔ allograph ↔ modern-character identity required before any holdout); PD-OBS's 47,157 images are modern regular characters keyed to KangXi, not OBS types; khipu counts 619 (OKR khipu_main v2.1.0) vs 702/703 (other universes); Meroitic 871 attested texts vs 782,761-word *augmented* corpus.
5. **Pseudo-precision flag:** Vinča DatDas counts (5,421/1,178/971) are the author's uncorroborated claims for an inaccessible resource; inadmissible in any power analysis. The Hesperia-adjacent "2026 open CSV" (1,751 records) remains unverified and must be audited before any design relies on it.

---

## Part II — Preregistration Amendment Appendix v1.1 (dated changelog)

Each amendment cites its source: [SA-n] = Sol Stage A loophole n; [SB] = Sol Stage B; [INT] = internal falsifier. All amendments entered 2026-08-11, before Run 3 data contact.

**A1. H-IND-1 (failure definition).** [SA-1] Disconfirmation is redefined as failure to satisfy *every* registered success criterion (point AUC ≥ 0.80 AND CI lower bound > 0.65). The zone between "CI includes 0.5" and full success is a failure, not a "promising" result.

**A2. H-IND-2 (relabel and conclusion rewrite).** [SA-2, SB] Relabeled **E1 model-comparison**. Licensed conclusion: a likelihood ratio or classifier score *conditional on the registered generator families*. Prohibited: any statement of the form "P(Indus is linguistic) = x" or a directional language/non-language finding. The prior, mixture weights, and generator-family coverage limits must be stated in every report of this result.

**A3. H-LNA-0 (shadow-decoy matching).** [SA-3] Decoy languages must be matched to the hidden relative on genealogical distance, contact history, phonotactic compatibility, corpus genre, and reconstruction depth — not merely "unrelated." Panel composition frozen before any shadow world is built.

**A4. H-LNA-1 (E2 requires an external consequence).** [SA-4] A winning family in the closed tournament is an E1 ranking result. E2 requires the winning family to generate at least one pre-designated G3-admissible independent prediction (onomastic, numerical, morphological, or archaeological) that is then checked. The prediction type is designated before the tournament runs.

**A5. H-OBS-1 (paired baseline).** [SA-5] The comparison target is a paired rerun of the CipherOBS method on identical labels, masks, and the same five splits — not the published 54.3% constant. Protocol-sensitivity of OBS metrics (OBSD 1.9–41% Top-1 across setups) is the documented reason.

**A6. OBS contamination trigger (tightened).** [SA-6] The prospective (post-cutoff) subset becomes the primary instrument. Equivalence criterion: prospective performance within 5 points of the standard held-out mean, frozen; any larger deficit is reported as evidence of leakage, not passed under a grace band.

**A7. H-OBS-2 (real experts for headline claims).** [SA-7] Expert-proxy adjudication is permitted in development only. Any headline E2 claim, and the E3 escalation path, requires review by named human oracle-bone palaeographers under the frozen rubric.

**A8. H-MAY-1 (sealed holdout).** [SA-8] Corroborating occurrences and imagery for any candidate residue-sign test are pre-designated and hashed before the hypothesis generator runs; retrieval and prompts are sealed against them. Rediscovery of unsealed corroborating evidence scores nothing.

**A9. H-MER-1 (custodian requirement + data firewall).** [SA-9] The ~900-text REM reserve is aspirational until an independent custodian identifies the sealed texts and commits to staged revelation; until then Meroitic claims run at E2 on existing anchors. Firewall: the 871 attested texts and the 782,761-word augmented corpus are never conflated; an agent describing the augmented corpus as ancient evidence halts the run.

**A10. H-CM-1 (conclusion rewrite).** [SA-10, SB] Licensed E2 claim: "Under independently reconstructed sign data and the frozen representation, Masson's CM group labels have no out-of-sample predictive signal beyond substrate/site covariates above effect size X." The conclusion "CM is a unitary script" is prohibited at any effect size (E1 interpretive claim). The test may not run on embeddings inheriting the preprocessing of the team whose conclusion is under test.

**A11. H-KHI-1 (structure-preserving nulls).** [SA-11] Permutation nulls must preserve hierarchy, subtotal relationships, ordering, and group sizes. Multiplicity accounting covers every khipu grouping/partition tried, logged.

**A12. H-KHI-2 (two-team masking).** [SA-12] Procedural contradiction resolved: linkage team reveals only the numeric fields establishing a new khipu–document match; attributes/names/status remain sealed with a custodian; prediction team deposits predictions; custodian unmasks. This is the program's E3 instrument for khipu.

**A13. H-VOY-0 (generator fingerprinting).** [SA-13] Leave-one-generator-family-out evaluation is mandatory, including families never seen during classifier construction. High macro-F1 without LOGO transfer is reported as fingerprinting, not classification.

**A14. H-VOY-1 (tolerances frozen; gate corrected).** [SA-14, SB] Reproduction tolerances move from the pre-scoring appendix into the frozen hypothesis before any generator is built. The real-manuscript result is labeled E1 model-comparison: "among preregistered generating models, family X best explains Voynich statistics out-of-sample." Class labels (language / cipher / meaningless) may not be asserted at any posterior.

**A15. H-ONO-1 (corollary universe frozen).** [SA-15] The corollary type and the full candidate search universe (names, provenances, object types, covariations) are frozen before matching begins; the search log is auditable; corrections apply over the frozen universe.

**A16. Phaistos control integrity.** [SA-16] The reporting/confidence policy is identical and frozen across the Phaistos control and all real targets before any run. Where feasible the pipeline is not told which target is the control. A control "passed" by output suppression is detected by comparing report rates and confidence distributions across control and targets; divergence is itself a failed control.

**A17. Appendix escape hatch closed.** [SA-global] All "pre-scoring appendix" items (dataset versions, control panels, tolerances, power analyses) must be completed and deposited into the tribunal record before Run 3 experiment designs contact data. An experiment whose appendix is incomplete at data contact is a protocol violation.

**A18. Claim-band matrix architecture.** [SB] E-classes attach to claims, not systems. The canonical matrix format becomes: highest licensed E-class per claim band, e.g. "Indus: E2/L1–L3 structural · E1 language-status · E0 semantic readings." The Checkpoint 2 matrix is reissued in this format at Run 3 synthesis.

**A19. Unit-mapping requirement.** [SA-audit, SB] Every experiment must freeze an explicit mapping for its system's contested units (sign inventories, character categories vs graph types, corpus-count universes) per the registry in Part I.3–4. Results are reported under all frozen unit treatments where they disagree.

---

## Part III — Run 3 shortlist (recommendation for sign-off)

**Design targets (6):** Oracle Bone residue · Khipu · Maya residue · Meroitic · Proto-Elamite · Linear A (limit case; shadow-validation precondition).
**Mandatory harness elements (3):** Proto-cuneiform (calibration, runs alongside, not a finalist slot) · Indus (methodology stress test: shadow discriminator + narrow E2/L1–L3 structural experiments per A2) · Phaistos (negative control per A16).
**Dropped from v2's top five:** Cypro-Minoan (no truth oracle for the unification claim as registered; source images withheld) — retains an E1/E2-narrow experiment option under A10 if capacity allows.
**Voynich:** H-VOY-0/1 run as E1 methodological experiments within the shadow-benchmark track, not as a design-target slot.
