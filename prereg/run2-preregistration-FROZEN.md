# PREREGISTRATION OF NULLS AND SUCCESS CRITERIA — FROZEN
## Undeciphered Writing Systems Research Program · Run 2, Stage 1

**Status:** FROZEN as of 2026-08-11. No scoring agent, tractability agent, falsification agent, or experiment agent has run at freeze time. No scoring output of any kind existed when this document was written.
**Governing plan:** `/home/claude/work/undeciphered-research-plan-v2.md` (v2, 2026-08-11), especially §2 (evaluability gate), §3 (shadow benchmarks), §4 (claim ladder), §5 (preregistered nulls).
**Evidence basis:** `/home/claude/work/run1-checkpoint1-inventory.md` (72 systems), `/home/claude/work/run1-checkpoint1-dossiers.md`, `/home/claude/work/run1-evidence-ledger.json` (572 records; citation spot-check 79 sampled / 4 minor failures, per inventory).
**Amendment policy:** Amendments are permitted only (a) before the first scoring agent contacts data for the affected hypothesis, and (b) as an appended, dated, signed changelog entry — never by editing frozen text. After data contact, the registered version is binding; deviations must be reported as protocol violations, not corrections.
**Citation convention:** Every empirical figure below carries its source. Where Run 1 sources disagree, the range is preserved and both sources named. Thresholds, α levels, panel compositions, and split fractions are *program design decisions made now, before scoring* — they are not empirical claims and cite nothing.

---

## 0. Global rules binding every hypothesis below

**G1 — Evaluability gate (plan §2).** Class determines licensed claim: E0 descriptive only; E1 method claims on synthetic/deciphered benchmarks; E2 candidate decipherment hypotheses on held-out real evidence; E3 strong claims with prospective external confirmation. No hypothesis below may issue a claim above its gate.

**G2 — Claim ladder (plan §4).** L1 glyph normalization → L2 segmentation → L3 structural classes → L4 grammatical/semantic roles → L5 phonetic hypotheses → L6 lexical correspondences → L7 translation. L7 output is prohibited program-wide in Runs 2–3. An agent that generates a hypothesis never authors or executes its own success test (HARKing guard, plan §9).

**G3 — Prediction admissibility (plan §2).** A confirmed prediction counts only if it concerns something externally observable independently of the decipherment: object type, provenance, independently recognizable ideograms, numerical quantities, names independently attested elsewhere, sign values later established from independent parallels. "Predicting the reading of a new text" never counts.

**G4 — Null construction.** Nulls are always *structured and meaningful*, never degenerate. For is-it-language questions the null generator class is matched meaningful nonlinguistic systems — never shuffled or random tokens, which every published test trivially beats (per the August 2026 non-specificity result, arXiv 2608.02999, <https://arxiv.org/abs/2608.02999>; verified in plan v2 §10 — the plan records it by arXiv ID; the Run 2 data-reality audit must log the exact title before H-IND-1 executes).

**G5 — Multiplicity.** Within each claim family, Holm–Bonferroni correction over all registered tests actually run. Every test run must be logged whether or not reported as headline; selective reporting is a protocol violation. Search logs (documents searched, decoys drawn, restarts executed) are mandatory and auditable — restart-exploitation guard per Tamburini (ACL CAWL 2023; 2025 journal version, *Frontiers in Artificial Intelligence*, DOI 10.3389/frai.2025.1581129, <https://cris.unibo.it/retrieve/7656690e-fe79-4b54-948b-fabce5723819/frai-8-1581129.pdf>; plan §9).

**G6 — Contamination.** No benchmark on historically deciphered systems without shadow-randomization (plan §3, §9). Any test material plausibly in model training data must be flagged; prospective sets (material published or deciphered after model cutoff) are the preferred contamination-resistant instrument.

**G7 — Independence of judges.** Internal multi-agent agreement is correlated evidence, never corroboration. Headline claims require the cross-model tribunal (plan §8).

**G8 — Data basis declaration.** Each experiment must declare whether it operates on (i) photographic scans/rubbings, (ii) hand-drawn facsimiles, (iii) transliterations/sign-code sequences, or (iv) a structured relational DB, and cite the specific resource version. Results do not transfer across bases without a registered bridging test.

**G9 — Null results are deliverables.** A rigorous failure to reject H0 is a success of the program (plan §0) and is reported at the same prominence as any positive finding.

---

## 1. Family IND — Indus script: is it language?

**Program role:** stress test of methodology, not a decipherment candidate (plan §7). **Gate:** structural claims E2; semantic readings E0–E1 (dossier §8, Indus).

**Corpus facts (ranges preserved).** Mahadevan 1977: ≥2,906 inscribed objects, 417(+2) distinct signs (scanned print concordance, Internet Archive, <https://archive.org/details/TheIndusScript.TextConcordanceAndTablesIravathanMahadevan>). Wells–Fuls ICIT: 4,537 objects, 5,509 texts, 19,616 sign occurrences, ~694 distinct signs — structured DB reported down since June 2021 ("Interactive Corpus of Indus Texts," Digital Classicist Wiki, <https://wiki.digitalclassicist.org/Interactive_Corpus_of_Indus_Texts>). Mean inscription length ~5 signs ("Indus script," Wikipedia, <https://en.wikipedia.org/wiki/Indus_script>). FIT_ISI_Corpora 2025: 963 curated seal images with grapheme transcription in SQL (JCAA, <https://journal.caa-international.org/articles/10.5334/jcaa.175>). Live dispute: Farmer–Sproat–Witzel 2004 nonlinguistic thesis (EJVS 11.2, <https://hasp.ub.uni-heidelberg.de/journals/ejvs/article/view/620>) vs Rao et al. 2009 conditional entropy, itself contested by Sproat (Wikipedia, <https://en.wikipedia.org/wiki/Indus_script>).

**Data basis:** transliterated sign-code sequences. Primary: ICIT-derived export if the Run 2 data-reality audit confirms access; fallback: digitized Mahadevan concordance. The chosen basis and allography scheme (417 vs ~694 signs) must be fixed in the pre-scoring appendix; results must be reported under both sign inventories if they disagree.

### H-IND-1 — Shadow-world discriminability (precondition; E1)
- **H0:** No statistic or classifier in the pipeline distinguishes corpora encoding natural language from matched *meaningful structured nonlinguistic* corpora (administrative/emblematic generators per plan §3) at Indus information conditions — token count matched to 19,616 ±10%, sign inventory within 417–694, mean text length ~5 signs, matched text-length distribution — better than chance.
- **H1:** At least one preregistered discriminant achieves reliable separation under those conditions.
- **Metric:** AUC of a frozen discriminator over ≥20 paired shadow worlds (≥10 language-encoding, ≥10 nonlinguistic; generator families red-teamed per plan §3 before use — a "nonlinguistic" generator that is secretly language-shaped voids the batch).
- **Threshold:** point AUC ≥ 0.80 AND 95% bootstrap CI lower bound > 0.65. Discriminator features and code frozen before any shadow world is scored.
- **Controls:** shuffled/random-token nulls are inadmissible (G4). Proto-cuneiform serves as a known semantics-without-full-glottography calibration item (inventory, proto-cuneiform entry, <https://en.wikipedia.org/wiki/Proto-cuneiform>): the discriminator's output on it must be reported. Generators and discriminator built by disjoint agent teams (G2).
- **Disconfirmation:** CI includes 0.5, or the red team produces one undetected language-shaped "nonlinguistic" generator → H0 stands; the headline finding is the null ("no statistic tested distinguishes language from structured nonlinguistic encoding at Indus scale"); H-IND-2 is cancelled and all Indus is-it-language claims are barred above E1.

### H-IND-2 — Real-corpus application (conditional on H-IND-1 rejecting H0; E2)
- **H0:** The real Indus corpus's discriminator score is within the distribution produced by the matched nonlinguistic generator class.
- **H1:** The score falls reliably in the language-encoding region.
- **Metric:** single, one-shot application of the frozen H-IND-1 discriminator to the real corpus; calibrated posterior P(linguistic | tested generator classes) with CI.
- **Threshold:** posterior ≥ 0.90 (or ≤ 0.10) to report a directional finding; anything in (0.10, 0.90) is reported as indeterminate.
- **Controls:** exactly one application; no post-hoc feature changes; report under both sign-inventory schemes; result explicitly conditioned on the generator class tested ("relative to these nonlinguistic models"), never as absolute proof of language.
- **Disconfirmation:** indeterminate posterior, or divergent verdicts across the two sign inventories → no claim; discrepancy reported.

---

## 2. Family LNA — Linear A language-family affinity ranking

**Gate:** E2, with mandatory shadow-world validation precondition (plan §7: "shadow-world validation mandatory before any real-corpus claim"). **Confirmation-bias hazard rated extraordinary** (plan §7).

**Corpus facts (ranges preserved).** 1,370 documents, 7,362–7,396 sign tokens, 97 unique signs (Braović et al. 2024, *Computational Linguistics* 50(2), <https://aclanthology.org/2024.cl-2.7.pdf>) vs ~1,427 artefacts, ~7,150 signs (Nepal & Perono Cacciafoco 2024, *Information* 15(2):73, GORILA-based, <https://www.mdpi.com/2078-2489/15/2/73>). No bilingual exists; anchors are Linear B retrojection, shared toponyms (pa-i-to etc.), and KU-RO arithmetic (dossier, Linear A §2, §4, citing <https://en.wikipedia.org/wiki/Linear_A>). Prior negatives: Semitic tests on libation tables negative; Carian/Cypriot matching "insufficient to yield conclusive evidence" (Nepal & Perono Cacciafoco 2024, above). Tamburini 2025 benchmark levels on *deciphered* pairs: 95.5% cognate accuracy Ugaritic/Old Hebrew, 89.4% Linear B/Greek (919 cognate pairs) (ledger records 100, 342; Tamburini 2025, *Frontiers in AI*, URL above) — these are E1 ceilings under full information, not expectations for Linear A conditions.

**Data basis:** transliteration + structured DB: SigLA (<https://sigla.phis.me/about.html>, CC BY-NC-SA) and/or the GORILA-derived corpus; both variants must be run (see stability clause).

### H-LNA-0 — Shadow validation precondition (E1)
- **H0:** At Linear A information conditions (~7,150–7,396 tokens, 97 signs, ~1,400 short administrative documents, partial sign-value priors, no bilingual), the affinity-ranking method cannot recover known relationships: its top-ranked family over a candidate panel is no more often the true relative than panel-uniform chance.
- **H1:** The method ranks the true relative first in ≥5 of 6 shadow worlds, with false-positive discipline (below).
- **Metric:** rank of true relative in ≥6 Linear-A-shaped shadow worlds (plan §3), each a real known language degraded to the target's information conditions, panel of 1 related + ≥7 unrelated languages.
- **Threshold:** ≥5/6 top-1 recovery; AND in ≥3 additional shadow worlds whose panels contain *no* related language, no control may cross the H-LNA-1 significance threshold in more than 1 of 3 worlds.
- **Controls:** shadow glyph randomization removes training contamination (G6); the answer key is held by a non-scoring agent; restart counts logged (G5).
- **Disconfirmation:** either criterion fails → H-LNA-1 is cancelled for Run 3; finding reported as "family ranking is not validated at Linear A information conditions."

### H-LNA-1 — Real-corpus affinity ranking (conditional on H-LNA-0; E2)
- **H0:** Apparent affinity of Linear A with any candidate family is no stronger than affinity generated against historically/geographically plausible *unrelated* controls given the same phonological degrees of freedom (plan §5).
- **H1:** Exactly one preregistered candidate family scores above the entire control distribution with the stability properties below.
- **Metric:** affinity score (as validated in H-LNA-0) of each candidate vs the empirical distribution of ≥7 unrelated controls; empirical p by permutation (≥1,000 permutations).
- **Threshold:** candidate max-score empirical p < 0.01 (Holm-corrected across candidates), AND stability: the same candidate ranks first under (a) both corpus variants (Braović vs GORILA-based), (b) ≥100 resamples over uncertain sign values, (c) ≥3 registered segmentation schemes.
- **Controls:** candidate panel registered here from Run 1 hypotheses — Anatolian/Luwian, Northwest Semitic (Ugaritic/Phoenician), Tyrsenian (Etruscan + Lemnian), Hurrian (dossier, Linear A §3) — plus unrelated controls chosen by a blind agent for equal phonological freedom (comparable syllabary-compatible phonotactics), with the identical transformation budget per language; exact control list and budget frozen in the pre-scoring appendix before any scoring. Known negatives (Semitic libation-table result, above) do not pre-bias the panel: Semitic stays in.
- **Disconfirmation:** no candidate clears controls, or any instability across (a)–(c), or a deliberately implausible control wins → H0 stands; the program reports that Linear A affinity claims at current information conditions are unsupported, and this becomes the registered prior against future single-family claims.

---

## 3. Family OBS — Oracle Bone undeciphered characters: held-out recovery

**Gate:** E3 available (dossier, OBS §8); shape E — unsolved units in a solved system permit genuine held-out evaluation (plan §1).

**Corpus facts (ranges preserved).** ~160,000 excavated pieces; ~4,500–4,600 distinct graphs; deciphered count ~1,000 (HUST-OBC, *Scientific Data* 2024, <https://www.nature.com/articles/s41597-024-03807-x>) to ~1,500–1,600 (AlphaOracle, arXiv 2607.17849, <https://arxiv.org/abs/2607.17849>; CipherOBS, arXiv 2604.09668) → ~3,000 undeciphered (inventory; ledger records 173, 181). Published baselines (2024–2026 literature): generative dictionary retrieval — 54.3% Top-10 and 86.6% Top-50 accuracy on unseen characters vs <3% for prior methods ("Decoding Ancient Oracle Bone Script via Generative Dictionary Retrieval," arXiv 2604.09668, <https://arxiv.org/abs/2604.09668>; ledger record 181); OBSD conditional-diffusion clue generation, ACL 2024 Best Paper ("Deciphering Oracle Bone Language with Diffusion Models," <https://aclanthology.org/2024.acl-long.831/>); PD-OBS radical-pictographic matching, 47,157-character annotated dataset, claims SOTA Top-10 (arXiv 2508.10113, <https://arxiv.org/abs/2508.10113>); AlphaOracle, 64% analyst-time reduction in an 86-specialist study (arXiv 2607.17849, above). **Source-attribution note (binding):** the Run 1 dossier attributes the 54.3/86.6 figures to arXiv 2607.17849 and AlphaOracle to arXiv 2508.10113; the evidence ledger (records 174, 181, 182) and plan §10 verification table attribute 54.3/86.6 to arXiv 2604.09668, AlphaOracle to 2607.17849, and PD-OBS to 2508.10113. The ledger/plan attribution is adopted here; the dossier's is recorded as an internal error to correct.

**Data basis:** labeled image datasets (rubbings/scans) — HUST-OBC (140,053 images, CC BY-NC), EVOBC (229,170 images), OBIMD and related sets via Open-Oracle hub (<https://github.com/Yuliang-Liu/Open-Oracle>) — plus transliterated inscription contexts; exact dataset versions pinned in the pre-scoring appendix.

### H-OBS-1 — Held-out deciphered-character recovery (E1 method claim)
- **Held-out split logic (registered now):** unit of holdout is the *character* (graph), never the image. Sample 10% of the deciphered inventory (≈100–160 characters given the 1,000–1,600 range; exact n recorded at execution against the pinned dataset), stratified by (i) occurrence-frequency tercile and (ii) structural class (pictograph vs compound, per dataset annotation). ALL images, variants, and evolution-chain entries (bronze/seal/clerical descendants) of a held-out character are masked — the paleographic chain is the anchor (dossier OBS §4, citing EVOBC), so leaving descendants visible is leakage. 5 independent random splits; report mean ± sd.
- **H0:** the pipeline's Top-10 retrieval accuracy on held-out deciphered characters does not exceed the strongest published baseline, 54.3% Top-10 (arXiv 2604.09668, above).
- **H1:** mean Top-10 > 54.3% with p < 0.05 across the 5 splits (one-sample test against the baseline constant); Top-50 secondary endpoint vs 86.6%.
- **What counts as success (registered):** *Top-10 retrieval* — the correct modern-character identity appears in the model's 10 highest-ranked candidates — is the success event, matching the dominant 2024–2026 evaluation convention (arXiv 2604.09668). Top-10 is the primary k; Top-50 secondary. Parity with baseline (Top-10 within ±2 points of 54.3%) licenses only "replication-grade method"; exceeding it as above licenses "method advance" (E1). Neither licenses any decipherment claim.
- **Controls / contamination:** characters whose accepted decipherment postdates the base model's training cutoff form a separate prospective subset (G6); if performance on the prospective subset is >20 points below the main held-out mean, contamination is declared and the main result is quarantined.
- **Disconfirmation:** H0 stands if the threshold is missed; report as a calibrated negative ("pipeline below published SOTA"), which caps H-OBS-2.

### H-OBS-2 — Proposals for genuinely undeciphered graphs (E2, E3 pathway)
- **H0:** A proposed identification for an undeciphered graph fits its attested inscription contexts no better than frequency-matched decoy identifications.
- **H1:** The proposal (a) ranks in the pipeline's Top-10, (b) beats ≥99 frequency-matched decoy characters on a frozen context-coherence score across ALL legible attested contexts of the graph, empirical p < 0.01, and (c) is coherent with the divination-formula grammar (preface–charge–prognostication–verification; dossier OBS §2) in every context, as judged blind.
- **Metric:** decoy-ranked context-fit score; blind expert or expert-proxy adjudication of formula coherence (judges never see which candidate is the pipeline's).
- **Threshold:** all of (a)–(c). One incoherent context falsifies the proposal (a graph reading must work everywhere it occurs — dossier OBS §8).
- **Controls:** graph must have ≥5 legible attested contexts (below that, E0-bar); hypothesis generator ≠ test executor (G2).
- **Disconfirmation / escalation:** failure of any prong kills the proposal. Surviving proposals are "candidate decipherment hypotheses" (E2) only; E3 requires external adjudication — submission to the expert-committee mechanism (National Museum of Chinese Writing, Anyang; 100,000-yuan verified-decipherment award, China Daily 2016, <https://www.chinadaily.com.cn/china/2016-10/28/content_27203697.htm>) or equivalent peer-reviewed acceptance. Until accepted externally, no "deciphered" language is permitted.

---

## 4. Family MAY — Maya undeciphered-residue reading proposals

**Gate:** E2 cap pending data audit. **Registered data caveat (binding):** the Run 1 evidence ledger contains NO corpus-fact records for Maya — its only Maya records concern glyph OCR/recognition coverage in the Sommerschield et al. 2023 survey (ledger record 21, citing "Machine Learning for Ancient Languages: A Survey," *Computational Linguistics* 49(3), <https://aclanthology.org/2023.cl-3.5/>). The inventory's completeness critique states Maya's undeciphered residue is "roughly 10-15% of signs unread" but flags this as an inventory gap needing an entry (inventory, "Completeness critique," item 2) — that figure is UNVERIFIED in the ledger. **Precondition:** the Run 2 data-reality audit must deposit sourced records for (i) total sign inventory, (ii) undeciphered-sign count, (iii) the corpus database used (e.g., candidate resources to be audited, not asserted here), before any H-MAY-1 scoring. Scoring against unaudited figures is a protocol violation.

### H-MAY-1 — Residue sign reading (E2)
- **H0:** A proposed value (syllabic or logographic) for an undeciphered Maya sign fits its attested contexts no better than the best of ≥99 decoy values drawn from the attested syllabary/lexicon under identical phonological and orthographic constraints.
- **H1:** The proposed value ranks first against the decoy set with empirical p < 0.01 (Holm-corrected across all residue proposals scored in the run), AND yields at least one G3-admissible independent prediction confirmed on evidence not used to generate the proposal — admissible prediction types, registered now: (i) a predicted syllabic substitution/spelling alternation with already-read signs attested elsewhere in the corpus; (ii) a predicted co-occurrence with an independently recognizable iconographic referent; (iii) a predicted name/toponym independently attested (routes through H-ONO-1).
- **Metric:** frozen context-coherence score over all occurrences + decoy ranking + binary confirmation of the registered prediction.
- **Threshold:** as in H1; signs with <10 attested occurrences are E0-barred from reading proposals (hapax and near-hapax readings are unfalsifiable).
- **Controls:** decoys matched for phonotactic plausibility and frequency; proposal generation and context-scoring by disjoint agents; the epigraphic-consensus reading inventory used for decoys pinned by version in the pre-scoring appendix.
- **Disconfirmation:** decoy ranking failure, any incoherent context, or the registered prediction failing → proposal rejected and logged. Family-level null: if ≥10 proposals are scored and none survives, the registered conclusion is "the pipeline cannot advance Maya residue readings at current information conditions."

---

## 5. Family MER — Meroitic lexical/grammatical expansion

**Gate:** E2 now; E3 pathway via unpublished/new texts (dossier, Meroitic §8: strongest evaluability case of its cluster).

**Corpus facts.** >2,000 known inscriptions; REM ~1,300 published + ~900 unpublished (Qasr Ibrim, Musawwarat); ~half funerary; 23-sign alphasyllabary in two graphic forms; fewer than ~100 words securely translatable (Rilly, "Meroitic," UCLA Encyclopedia of Egyptology, <https://escholarship.org/content/qt3128r3sw/qt3128r3sw_noSplash_a34fb083e49c75f88724b4054bd16aaf.pdf>). Machine-readable dataset: 871 texts/phrases, 1,868 unique word forms, 193 glossed words, 897 phrases; cross-lingual embedding lexicon induction reached ≤20% accuracy and "could not correctly translate terms that had not been seen before" (Otten & Anastasopoulos 2025, "Towards Ancient Meroitic Decipherment," NAACL ALP workshop, <https://aclanthology.org/2025.alp-1.11.pdf>; repo <https://github.com/Joshua-Otten/Meroitic-Corpus>, no explicit license — audit must confirm terms). No substantial bilinguals exist and Rilly doubts they ever did; anchors are onomastic and loanword-based (Rilly, UEE, above). Dominant family hypothesis: Northern East Sudanic (Rilly); minority Afroasiatic (Rowan) — the ledger verifier notes the "minority" framing is imported, so both are carried as live (inventory, citation-verification failure 4).

**Data basis:** transliteration dataset (Otten & Anastasopoulos) + print REM; no comprehensive image DB exists — claims about paleography are out of scope for this family.

### H-MER-1 — Individual lexical/grammatical claims via loanword/toponym/name anchors (E2)
- **H0:** A proposed Meroitic lexeme meaning or grammatical-morph function derived from a loanword, toponym, or personal-name anchor scores no better on its attested contexts than ≥99 decoy meanings drawn from the same semantic-field pool (for lexemes) or decoy function assignments (for morphs), under identical transformation budgets.
- **H1:** The proposal beats the decoy distribution at empirical p < 0.01 (Holm-corrected within the run), has ≥3 independent attestation contexts, and — if name/toponym-based — independently satisfies H-ONO-1 in full.
- **Metric:** decoy-ranked context-fit on the funerary-formula slot grammar (invocation–nomination–filiation–benedictions structure; Rilly, UEE, above) and non-funerary contexts where attested.
- **Threshold:** as in H1; additionally, NES-cognate-based claims must cite comparative Nubian/Nara/Taman/Nyima data gathered independently of the Meroitic claim (dossier, Meroitic §8a), with the comparative source deposited in the ledger before scoring.
- **Controls:** the ~900 unpublished REM texts are designated the *reserved test partition*: no generation agent may access any transcription of them; confirmed proposals must not degrade, and should improve, slot prediction when unpublished texts become available (E3 event, logged prospectively). Rowan-vs-Rilly family framing must not be assumed in scoring (both live).
- **Disconfirmation:** decoy failure, <3 contexts, or an anchor failing H-ONO-1 → rejected. A proposal contradicted later by a reserved-partition text is retracted with a first-class report.

### H-MER-2 — Aggregate method claim (E1)
- **H0:** The pipeline's lexicon-induction accuracy on the 193 glossed words (leave-k-out over the gold glosses) does not exceed the published ≤20% baseline (Otten & Anastasopoulos 2025, above).
- **H1:** Accuracy exceeds 20% with p < 0.05 across ≥5 leave-k-out folds.
- **Metric:** top-1 gloss accuracy (secondary: top-5), identical data splits published with code.
- **Threshold:** as in H1. This licenses only an E1 method claim; every individual new gloss still requires H-MER-1.
- **Controls:** folds frozen before model contact; no fold's gold glosses in any prompt/训练 context for that fold.
- **Disconfirmation:** ≤20% → registered negative; Meroitic expansion claims then rest solely on anchor-based H-MER-1 routes.

---

## 6. Family CM — Cypro-Minoan sign-inventory unification (CM1/CM2/CM3)

**Gate:** E2 for the classificatory claim; corpus too small for more (plan §7).

**Corpus facts (ranges preserved).** <250 inscriptions (Steele, CUP excerpt, <https://assets.cambridge.org/97811070/42865/excerpt/9781107042865_excerpt.pdf>) vs ~250 inscriptions, <4,000 syllabograms, ~100 unique signs (Braović et al. 2024, <https://aclanthology.org/2024.cl-2.7.pdf>) vs ca. 300 inscribed objects, <3,500 sign instances, 96 unique signs, analytic dataset 2,899 sign instances from 213 inscriptions — CM1: 1,153, CM2: 1,430, CM3: 316 (Corazza et al. 2022, *PLoS ONE* 17(7):e0269544, <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0269544>). Sign-inventory proposals 114 (Masson) / 96 (Olivier) / ~74 (Ferrara) (Unicode proposal L2/16-179, <https://unicode.org/L2/L2016/16179-n4733-cypro-minoan.pdf>). Prior evidence: Sign2Vecd unsupervised analysis supports "a unitary, single Cypro-Minoan script"; Masson's CM1/CM2/CM3 division increasingly questioned (Corazza et al. 2022, above; inventory).
**Data basis:** annotated sign-image dataset vectorized from published drawings (Corazza et al. 2022; code/vectors at <https://github.com/ashmikuz/sign2vec_d>; source images under publishers' copyright — hand-drawn basis, per Braović et al. 2024 caveat on such datasets).

### H-CM-1 — Unification vs division (E2, with built-in E1 preconditions)
- **Preconditions (both must pass before the real test):**
  1. *Separation control:* the pipeline, applied to two genuinely distinct but related scripts' sign images downsampled to CM sample sizes (e.g., Linear B vs Cypriot syllabary drawings; exact pair frozen in pre-scoring appendix), achieves balanced accuracy ≥ 0.80 in recovering the true two-script split.
  2. *Unity control:* the pipeline, applied to a single known script artificially partitioned by medium/site (mimicking the clay-tablet vs other-substrate split; 1,732 of the CM instances are on clay tablets — Corazza et al. 2022), reports separability within its chance band (registered as balanced accuracy ≤ 0.60).
- **H0:** CM1/CM2/CM3 are distinct systems — formally, the separability of the CM groups in the frozen embedding is at or above the separation-control band.
- **H1 (unification):** CM separability falls within the unity-control band, and residual variation is predicted better by substrate/site covariates than by Masson group labels.
- **Metric:** balanced accuracy of a frozen classifier distinguishing Masson groups on held-out sign instances; variance-partition comparison (group label vs substrate/site) as secondary endpoint.
- **Threshold:** H1 supported iff CM balanced accuracy ≤ midpoint between the two control bands AND the substrate/site model beats the group-label model on held-out likelihood (p < 0.05).
- **Controls:** power analysis registered for CM3 (n = 316 sign instances); if CM3 is underpowered at the registered effect size, the claim is restricted to CM1/CM2 and says so explicitly. Embeddings trained without group labels; held-out split at inscription level, never sign level.
- **Disconfirmation:** precondition failure → E1 only, no claim about CM ("method cannot resolve unification at this corpus size" is the registered finding). CM separability at/above the separation band → H0 stands (division supported), which contradicts and must be reported against the Corazza et al. 2022 unitary result rather than silently dropped.

---

## 7. Family KHI — Khipu-to-colonial-document record linkage

**Gate:** E2 now, E3 pathway demonstrated (dossier, Khipu §8; plan §7: "genuinely falsifiable (E2)").

**Corpus facts.** ~1,650–1,700 documented khipus (Thompson 2025 census; Khipu Field Guide, <https://khipufieldguide.ghost.io/counting-the-khipus-how-many-are-there-to-study/>); Open Khipu Repository: serverless SQLite DB + CSV registry, open license, v2.0.0 26 July 2022 (Zenodo, <https://zenodo.org/records/6908343>), v2.1.0 22 Dec 2025 adding KH0631–KH0702 (Zenodo, <https://zenodo.org/records/18025748>); 702 khipus with public data as of Jan 2026 ("Quipu," Wikipedia, <https://en.wikipedia.org/wiki/Quipu>). Decimal knot arithmetic accepted (Locke 1923; Wikipedia, above). Precedent: Medrano & Urton 2018 matched six mid-colonial Santa Valley khipus to a 1670 Spanish revisita census, 132 individuals; the only khipu–census match discovered so far; recto/verso attachment plausibly marks social status/moiety, color plausibly linked to names (*Ethnohistory* 65(1), <https://read.dukeupress.edu/ethnohistory/article-abstract/65/1/1/133085/Toward-the-Decipherment-of-a-Set-of-Mid-Colonial>; ledger records 225, 488–490). Hyland's Collata logosyllabic claim (95 cord signs, two lineage names) remains controversial (*Current Anthropology* 58(3), <https://www.journals.uchicago.edu/doi/abs/10.1086/691682>) and is NOT assumed by any test here.
**Data basis:** structured DB (OKR khipu.db, version pinned) — structural transcriptions (cord/knot/color tables), not photographs; archival documents as transcribed text with archive citations.

### H-KHI-1 — Numeric record linkage against permuted archives (E2)
- **H0:** The match score between a candidate khipu (or khipu set) and a colonial document is no higher than expected against permuted archives — i.e., the observed number of exact numeric correspondences arises at comparable rate when (a) the document's numeric entries are permuted preserving marginal value distributions, and (b) the khipu is scored against other archival documents of the same genre and region.
- **H1:** Observed match score exceeds both null distributions at empirical p < 0.001.
- **Metric:** frozen linkage score = count of exact numeric matches under matching rules (value tolerance = exact; ordering/grouping rules; hierarchy alignment) fixed in the pre-scoring appendix BEFORE any archive search; null distributions from ≥1,000 within-document permutations and ≥100 same-genre decoy documents.
- **Threshold:** p < 0.001 on both nulls, Holm-corrected for the total number of khipu–document pairs examined in the search (the search log of G5 supplies the correction denominator — the look-elsewhere effect across archives is the family's principal hazard).
- **Controls:** matching rules frozen pre-search; archives enumerated before scoring; any rule change after first contact voids the pair. Santa Valley khipus/census serve as the positive calibration pair (the pipeline must recover the published match).
- **Disconfirmation:** failure to beat permuted nulls → no linkage claim; failure to recover the Santa Valley positive control → pipeline defect, all family results quarantined.

### H-KHI-2 — Attribute-encoding generalization (E2→E3)
- **H0:** Proposed non-numeric encodings (cord color → name/name-class; recto/verso attachment → social status/moiety, per Medrano & Urton 2018) fitted on linkage-established pairs predict attributes on a NEW independently linked khipu–document pair no better than attribute-permuted nulls.
- **H1:** Held-out-pair prediction accuracy beats the permuted-attribute null at p < 0.01.
- **Metric:** accuracy on the new pair's independently documented attributes; null via ≥1,000 permutations of the attribute assignment.
- **Threshold:** p < 0.01; at least one genuinely new pair (not Santa Valley).
- **Controls:** the model is frozen before the new pair's document is read; E3 credit only if the prediction was deposited (hashed) before archival lookup — the prospective route (G3: names/quantities independently attested).
- **Disconfirmation:** no generalization → encoding claims remain pair-specific descriptions (E2 ceiling), and this limit is reported.

---

## 8. Family VOY — Voynich: language vs cipher vs hoax classification

**Gate:** E2 (held-out internal evidence only; no external corpus can exist — dossier, Voynich §8). L5+ output (phonetic values, readings, translations) is barred for Voynich regardless of classifier outcome.

**Corpus facts.** Single manuscript; ZL transliteration 157,304 characters; ~37,919 word tokens (Wikipedia, <https://en.wikipedia.org/wiki/Voynich_manuscript>) vs ~36,000–38,000 (inventory) — range preserved; ~5,385 loci; multiple machine-readable transliterations (Takahashi, ZL, v101/GC, Currier, FSG) in IVTFF 2.0 (voynich.nu, <https://www.voynich.nu/transcr.html>); vellum radiocarbon 1404–1438 (Wikipedia, above) vs Beinecke catalog late 15th–16th c. (<https://beinecke.library.yale.edu/beinecke/collections/beinecke-cipher-voynich-manuscript>) — both reported. Key statistical anomaly: Zipfian word frequencies but conditional character entropy h2 ≈ 2 vs 3–4 for natural languages (Wikipedia, above). Camps: natural language (Bowern & Lindemann, *Annual Review of Linguistics*, <https://www.annualreviews.org/content/journals/10.1146/annurev-linguistics-011619-030613>); hoax/meaningless (Rugg 2003 Cardan-grille demo; Schinner 2007; 2022 Yale human-gibberish experiments — all per Wikipedia, above); cipher. Graveyard of rejected solutions incl. Cheshire 2019, withdrawn by Univ. of Bristol (Shropshire Star, <https://www.shropshirestar.com/news/uk-news/2019/05/17/university-backtracks-over-voynich-manuscript-translation-claims/>).
**Data basis:** machine-readable transliterations (IVTFF 2.0); transliteration-scheme sensitivity is a registered robustness axis (results must hold under ≥2 independent transliterations, e.g., ZL and Takahashi).

### H-VOY-0 — Classifier validation battery (precondition; E1)
- **H0:** The 3-class classifier (natural language / ciphered language / meaningless structured pseudo-text) cannot reliably classify known-class controls at Voynich-like scale.
- **H1:** Macro-F1 ≥ 0.85 on the control battery.
- **Metric:** cross-validated macro-F1 on ≥30 texts per class, each length-matched (~37k tokens or equal truncation): (a) natural languages incl. low-resource, unspaced, and abjad/abugida orthographies; (b) period-plausible ciphers (simple/homophonic substitution, nomenclator, Cardan-grille variants) applied to natural text; (c) meaningless structured pseudo-text (human-generated gibberish following the 2022 Yale-style elicitation protocol + algorithmic Rugg-grille output).
- **Threshold:** macro-F1 ≥ 0.85; per-class recall ≥ 0.75.
- **Controls:** battery composition frozen before classifier development completes; class-(c) generators red-teamed (a generator secretly encoding language voids the batch, as in G4/H-IND-1).
- **Disconfirmation:** below threshold → H-VOY-1 cancelled; registered finding: "the three generating classes are not distinguishable at this scale by the tested features" — itself a publishable null bearing on the whole literature.

### H-VOY-1 — Voynich classification (conditional; E2)
- **H0:** No class receives calibrated posterior ≥ 0.90, or the favored class's generative models cannot reproduce Voynich's joint statistical profile.
- **H1:** One class has posterior ≥ 0.90 under both transliterations AND generators from that class reproduce, within preregistered tolerances (set in the pre-scoring appendix), the joint profile: Zipf exponent, h2 ≈ 2 anomaly, section/topic structure, and line-position effects.
- **Metric:** calibrated posterior from the frozen H-VOY-0 classifier + generative reproduction checks on held-out folios (classifier trained/tuned without a reserved 20% folio block; final statistics computed on the reserve).
- **Threshold:** as in H1; posterior reported with CI regardless of outcome.
- **Controls:** one-shot application per transliteration; disagreement between transliterations → indeterminate verdict. No reading, glyph-value, or plaintext claim may accompany any outcome (L5+ bar).
- **Disconfirmation:** H0 outcome is reported as "indeterminate — Voynich not assignable at ≥0.90," constraining future claims; a confident class assignment whose generators fail the reproduction check is a pipeline overconfidence finding and quarantines the result.

---

## 9. Family ONO — Onomastic anchor claims (transversal standard)

**Gate:** inherits the host system's gate; unregistered onomastic matches are inadmissible program-wide ("this looks like Knossos" is horoscope logic — plan §2). This template binds every name/toponym-based claim in families LNA, MER, MAY, KHI, and any other system (e.g., Eteocypriot, Sidetic).

### H-ONO-1 — Registered onomastic match (template)
- **Required registration BEFORE scoring (plan §2, all six elements):** (1) candidate name set, enumerated and closed; (2) allowed phonological transformations with an explicit cost budget; (3) sign values learned independently of the target names (provenance of each value documented); (4) matching score definition; (5) null distribution construction; (6) acceptable coincidence probability.
- **H0:** The match score of the proposed name identification lies within the null distribution generated by (a) ≥999 decoy names of matched length/structure drawn from the same onomasticon(s), and (b) ≥999 scrambled sign-value assignments consistent with the same independence constraints.
- **H1:** Observed score exceeds both nulls at empirical p < 0.005 (per claim), Holm-corrected across all onomastic claims in the run.
- **Metric:** the registered matching score (element 4) against both nulls.
- **Threshold:** p < 0.005 on both nulls; AND the identification must generate at least one G3-admissible corollary (e.g., the same sign values reading a second independent name, or a provenance/object-type covariation) that is checked and reported.
- **Controls:** transformation budget identical for target and decoys; candidate set closed before any sign values are inspected against it; generation and scoring by disjoint agents.
- **Disconfirmation:** failure on either null, or the corollary failing → the anchor is rejected and may not be reused in aggregate arguments ("many weak matches" do not sum; each must individually pass).

---

## 10. Family PHA — Phaistos Disc negative control (pipeline falsification)

**Gate:** E0 for all disc readings (dossier, Phaistos §8: 241-token unicum; no bilingual, no numerals, no accepted external values; every historical claim failed by non-falsifiability — Duhoux 2000 "How not to decipher the Phaistos Disc," per inventory and <https://en.wikipedia.org/wiki/Phaistos_Disc>).

**Corpus facts.** Unicum: 45 distinct stamped sign types, 241–242 tokens (123 side A, 119 side B, one illegible), 61 stroke-delimited "words" (Wikipedia, above; inventory). Unicode block U+101D0–U+101FF (Wikipedia, above).

### H-PHA-1 — Negative-control run (falsifies the PIPELINE, not a text claim)
- **Design:** the complete pipeline — every module used in families IND, LNA, VOY, ONO — is run on the Phaistos Disc with no special-casing, no hard-coded exclusion, and the operators blinded to its negative-control role where feasible.
- **H0 (the desired outcome):** the pipeline outputs only E0-licensed products: descriptive/structural analysis (sign inventory, token counts, direction, stroke-delimited segmentation — claim-ladder L1–L3) and explicit refusals above that.
- **H1 (pipeline failure — what falsifies the pipeline):** ANY of the following outputs on the disc:
  1. a language-family affinity ranked significant under the H-LNA-1 test procedure;
  2. an is-it-language posterior ≥ 0.75 (either direction) from the H-IND discriminator presented as a finding rather than flagged as out-of-domain (241 tokens is below any registered power floor);
  3. any L4 grammatical/semantic role assignment, L5 phonetic value, L6 lexical correspondence, or L7 translation emitted at or above the pipeline's reporting-confidence threshold;
  4. an onomastic match on the disc passing H-ONO-1 (with 45 sign types and 241 tokens, a passing match indicates the null machinery is miscalibrated);
  5. a Voynich-style class assignment with posterior ≥ 0.90.
- **Metric:** binary audit of pipeline outputs against conditions 1–5 by an agent that had no role in building the modules.
- **Threshold:** zero occurrences of conditions 1–5. One occurrence = pipeline failure.
- **Controls:** run scheduled alongside (not after) the real-system runs of Run 3, so failure quarantines concurrent results; the audit agent receives outputs stripped of system identity where module design allows.
- **Disconfirmation consequences (registered now):** on failure, (i) ALL concurrently produced positive results from the failing module family are quarantined and may not be reported until root-cause analysis and a re-run of both the control and the affected experiments; (ii) the failure is itself a first-class deliverable ("the pipeline announced X about a 241-sign singleton"), per plan §4: "If the pipeline announces a decipherment of a 241-sign singleton, the pipeline has failed. This is a feature." Passing H-PHA-1 is necessary but never sufficient evidence of pipeline validity.
- **Out-of-scope note:** disc authenticity (thermoluminescence never performed; Wikipedia, above) is E3-testable by physical means but is outside this program's instruments; no authenticity claim will be made.

---

## 11. Freeze block

| Field | Value |
|---|---|
| Registered hypotheses | H-IND-1, H-IND-2, H-LNA-0, H-LNA-1, H-OBS-1, H-OBS-2, H-MAY-1, H-MER-1, H-MER-2, H-CM-1, H-KHI-1, H-KHI-2, H-VOY-0, H-VOY-1, H-ONO-1, H-PHA-1 (16) |
| Freeze date | 2026-08-11 |
| Scoring status at freeze | No evaluability scoring, tractability scoring, or experiment execution has occurred |
| Pre-scoring appendices | Each family's operational appendix (dataset versions/hashes, control-panel lists, tolerance values, power analyses) must be frozen and hashed before that family's first data contact; appendices may narrow but never widen registered thresholds |
| Deviation rule | Any departure from this document after data contact is reported as a protocol violation in the affected checkpoint, with the original registered analysis reported alongside any deviation |
| Downstream citation | All Run 2 scoring agents, Run 3 experiment designers, and synthesis agents cite this document by hypothesis ID |
