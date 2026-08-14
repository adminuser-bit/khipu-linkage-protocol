# Run 3 / Checkpoint 3: Experiment Designs

**Prepared:** August 11, 2026 · 11 agents; no agent-run failures · 8 designs · red team: 41 findings (3 fatal, 24 major, 14 minor — all with required fixes; fatal fixes are BINDING revisions, see companion file)

# Oracle Bone Undeciphered Subset (flagship)

# Run 3 Experiment Design — Oracle Bone Undeciphered Character Subset (Family OBS)

**Design ID:** R3-OBS-v1 · **Date:** 2026-08-11 · **Executes:** H-OBS-1, H-OBS-2 (`run2-preregistration-FROZEN.md` §3) as amended by A5, A6, A7, and bound by A16–A19 (`tribunal-record-and-prereg-amendments-v1_1.md`).
**Adjudicated band (tribunal Part I.2, binding):** *Oracle Bone subset — E2 now; E3 path via external adjudication (A7).* No claim in this design is licensed above that band. Per A18, E-classes attach to claims, not to the system; the claim-band statement is in §5.
**Governance rule:** this design specifies procedures only. Success/disconfirmation adjudication is fixed by the frozen preregistration + amendment appendix; the designer authors no adjudication criteria and no agent that generates a candidate identification executes its own test (G2).

---

## 1. Data acquisition plan (grounded in the Run 2 data-reality audit, not papers' claims)

All facts below cite the Run 2 audit (`run2-audits-methods-patch.md`) or tribunal record; where the audit and papers disagree, the audit governs.

### 1.1 Primary datasets (audited)

| Resource | Audit score | Audited reality | Role |
|---|---|---|---|
| **HUST-OBC** | **5/5** | Open download verified: GitHub + Figshare DOI 10.6084/m9.figshare.25040543.v3 (HTTP 202 verified 2026-08-11) + ModelScope mirror. 140,053 images in per-category folders + `chinese_to_ID.json` / `ID_to_chinese.json`. **Undeciphered subset explicitly labeled: 62,989 images / 9,411 undeciphered categories vs 77,064 images / 1,588 deciphered categories; undeciphered sources labeled L, X, Y+H in README.** CC BY-NC 4.0 (stated in the paper; no license file surfaced on GitHub README — custodian records this). It is a structured DB of glyph *images*, not transliterated running text. Sources: audit rows/notes; "HUST-OBC" dataset paper, *Scientific Data* 2024, <https://www.nature.com/articles/s41597-024-03807-x>; <https://github.com/Pengjie-W/HUST-OBC>. | Primary instrument for both hypotheses; defines unit treatment U-A (§3). |
| **EVOBC** | **4/5** | Open download verified: Hugging Face <https://huggingface.co/datasets/HaisuGuan/EVOBC> (HTTP 200) + Figshare share link. 229,170 JPGs, 13,714 categories across 6 stages (OBC, Bronze, Spring-Autumn, Warring States, Seal, Clerical); filename convention `ID#_Source_Era_*.jpg` + 2 JSON metadata maps. CC BY-NC-SA 4.0. README does **not** label an undeciphered subset — EVOBC maps evolution of decipherable characters; deciphered-count disagreement recorded by audit as range ~1,588–1,600 (HUST-OBC vs EVOBC paper). Source: audit row; <https://github.com/RomanticGodVAN/character-Evolution-Dataset>. | Evolution-chain masking (leakage control) and cross-stage linkage; OBS side of OBSD-style training pairs. |
| **PD-OBS** | 3/5 | Per tribunal Part I.3.4 (binding correction) and audit: the 47,157 images are **modern regular characters keyed to the KangXi Dictionary, NOT OBS types**; plus 10,968 ancient + 11,739 OBS category images *sourced from HUST-OBC and EVOBC*; dictionary/radical/pictographic-analysis files; Google-Drive-only hosting; **no license stated**. Sources: audit row; arXiv 2508.10113, <https://arxiv.org/abs/2508.10113>; <https://github.com/PKXX1943/PD-OBS>. | **Non-load-bearing auxiliary only** (structural-class annotations, fallback rung in §4.2). Excluded from any headline-supporting path unless license is clarified in writing; never a unit source (A19). |
| **OBSD repo** | 3/5 | Code + `modern_kanji.zip` in-repo; OBS training images must be assembled from EVOBC per README; no license stated. Source: audit row; "Deciphering Oracle Bone Language with Diffusion Models," ACL 2024, <https://aclanthology.org/2024.acl-long.831/>. | Protocol-sensitivity reference only (OBSD 1.9–41% Top-1 across setups is the documented reason for A5). |
| **Open-Oracle hub** | 2/5 | Curated index, not a data host; links OBIMD (10,077 images; GitHub + HF KLOBIP/OBIMD), OBI-Bench, PictOBI-20k, etc. Each linked dataset's license must be verified independently. Source: audit row; <https://github.com/Yuliang-Liu/Open-Oracle>. | Discovery layer for the context corpus (§1.2). |

### 1.2 Registered gap: inscription-context corpus (precondition OBS-P1)

H-OBS-2 requires, per its frozen text, "ALL legible attested contexts" of each target graph. **The audited 5/5 and 4/5 resources are per-character image datasets and contain no inscription contexts.** Candidate context resources are OBIMD (known only through the unaudited Open-Oracle index) and the Yinqiwenyuan national database (jgwlbq.org.cn; described in the Run 1 dossier as a free structured DB — <https://www.tencent.com/en-us/articles/2201854.html> — but **not** in the 42-resource audit table).

**Precondition OBS-P1 (blocking, per A17):** before any H-OBS-2 data contact, the data custodian audits OBIMD (and Yinqiwenyuan if OBIMD fails) against four binary checks: (i) per-inscription sign-level transcription exists in bulk-obtainable form; (ii) undeciphered-graph tokens are marked as such in transcriptions; (iii) a linkage key to standard catalog numbers (Jiaguwen Heji numbering — 41,956 rubbings + 13,766-piece 1999 supplement, "Jiaguwen Heji," Wikipedia, <https://en.wikipedia.org/wiki/Jiaguwen_Heji>) is present; (iv) license/terms permit the use. The audit report is deposited in the tribunal record. **If no resource passes all four checks, H-OBS-2 does not run**; the registered deliverable becomes the OBS-P1 audit itself plus H-OBS-1 (see §8). No degraded substitute is permitted.

**G8 declaration.** H-OBS-1 operates on basis (i) photographic scans/rubbings images (HUST-OBC/EVOBC). H-OBS-2 additionally operates on basis (iii) transliterated inscription contexts (OBS-P1 resource). The cross-basis **bridge is registered now**: image-category ↔ context-token linkage via catalog numbers; validation = custodian samples 100 linked occurrences (seed 20260811), palaeographer panel verifies correctness; **≥98/100 correct required, else H-OBS-2 is blocked** (G8: results do not transfer across bases without a registered bridging test).

### 1.3 Acquisition protocol and roles

A **data custodian agent/team** (disjoint from all modeling, baseline, and scoring teams) performs: download of pinned versions; SHA-256 manifest computation and deposit (appendix item PA-1); **re-keying of all category IDs to fresh random IDs** (contamination control, §7); split generation and masking (§4); custody of the answer key (holdout ID → modern identity) and of all control-panel identities. Modeling and scoring teams never receive `ID_to_chinese.json`, original HUST-OBC IDs, or any answer-key material for masked units.

---

## 2. The A19 unit mapping (frozen; both treatments run)

**The contested units (tribunal Part I.3.4, unit-mismatch registry):** historical "~3,000 undeciphered graphs" (range basis: ~4,500–4,600 distinct graphs, deciphered ~1,000 [HUST-OBC paper] to ~1,500–1,600 [AlphaOracle, arXiv 2607.17849]; Henan Provincial Government 2024: "only about one-third of the approximately 4,500 oracle bone characters… can be interpreted," <https://english.henan.gov.cn/2024/01-26/2893169.html>) **vs HUST-OBC's 9,411 undeciphered *categories*** vs allographs vs modern-character identities (with PD-OBS's 47,157 images being modern regular characters keyed to KangXi, a different universe entirely).

**Treatment U-A — "category-as-unit" (no discretion).** Unit = HUST-OBC category ID exactly as shipped in the pinned Figshare v3 release. Deciphered universe: 1,588 categories; undeciphered universe: 9,411 categories. No merging, no splitting. U-A is the **primary inferential frame** because it admits zero discretionary judgment.

**Treatment U-B — "graph-type / modern-identity" (frozen merge procedure).**
- *Deciphered side (deterministic):* categories are merged iff their `ID_to_chinese.json` values, NFC-normalized to Unicode codepoints (CJK Unified + Extensions), are identical. The label space for retrieval under both treatments is the modern-character identity (the frozen prereg's registered success event).
- *Undeciphered side (procedural + adjudicated):* merge candidates are proposed automatically — cosine similarity ≥ 0.85 (frozen; 0.80/0.90 reported as descriptive sensitivity only) among top-5 nearest neighbors under an image encoder trained by the custodian's contractor **on deciphered images only** (so H-OBS-1 holdouts are unaffected; the encoder never sees undeciphered labels because none exist). Every proposed merge involving a graph that enters H-OBS-2 must be **ratified or rejected by the A7 palaeographer panel under the frozen rubric before that graph is scored**; unratified merges do not apply.
- *Cross-dataset:* HUST-OBC↔EVOBC linkage on the deciphered side is by modern-identity JSON maps of both datasets (deterministic).

**Frozen disagreement rule (A19):** every H-OBS-1 and H-OBS-2 result is computed and reported under **both** U-A and U-B. If the treatments disagree on any registered success criterion, no positive claim is licensed; the disagreement is itself the reported finding. The mapping outcome (how many graph types the 9,411 categories collapse to; how the count relates to the historical ~3,000 figure) is a first-class L1 deliverable that directly addresses the unit-mismatch registry entry.

**PD-OBS exclusion (A19):** KangXi-keyed modern-character images are never treated as OBS types or used to define units.

---

## 3. Method (implementation-grade)

### 3.1 H-OBS-1 — held-out deciphered-character recovery (E1 method claim), as amended by A5/A6

**Split construction (custodian; frozen prereg §3 logic, operationalized).** Unit of holdout = character (per treatment), never the image. 5 independent splits; RNG NumPy PCG64, seeds 202608111–202608115. Each split holds out 10% of the deciphered inventory (U-A: 159 of 1,588 categories; U-B: 10% of the merged count, recorded at execution per the frozen prereg's "exact n recorded at execution"). Stratification: (i) occurrence-frequency tercile — frozen proxy = HUST-OBC image count per category (the audited datasets carry no attestation-frequency field; the proxy choice is frozen now to close the discretion); (ii) structural class (pictograph vs compound) **iff** a machine-readable annotation exists in the pinned HUST-OBC v3 (binary custodian check at acquisition, recorded; fallback rung 2 = PD-OBS radical/pictographic files if license clarified; rung 3 = tercile-only; the rung actually used is recorded in the appendix before scoring).

**Masking (leakage control).** For each held-out character: ALL HUST-OBC images of its category(-ies) AND all EVOBC images of the linked categories across all 6 stages are removed from every training/tuning artifact. Rationale is registered in the frozen prereg: the paleographic chain is the anchor (Run 1 dossier OBS §4, citing EVOBC, <https://arxiv.org/abs/2601.05508>), so visible descendants are leakage. The tribunal falsifier confirmed this masking "specifically blocks the paleographic-descendant leakage channel" (checkpoint-2 matrix, OBS verdict).

**Arm 1 — Program pipeline.** A retrieval pipeline mapping an unseen OBS character (its image set) to a ranked list of modern-character identities. Reference architecture (implementable by a competent ML team; internals are free, interfaces are frozen): image encoder pretrained on non-masked HUST-OBC+EVOBC images; cross-stage evolution model over EVOBC stages; retrieval head over the modern-identity label space; optional LVLM re-ranker **with the constraint that any LVLM's training cutoff enters the T_c computation (§7)**. Inputs: masked training set only. Output contract: for each held-out character, a ranked Top-50 list of Unicode codepoints.

**Arm 2 — Paired CipherOBS rerun (A5, binding).** The comparison target is a paired rerun of the CipherOBS generative dictionary-retrieval method ("Decoding Ancient Oracle Bone Script via Generative Dictionary Retrieval," arXiv 2604.09668, <https://arxiv.org/abs/2604.09668>) on **identical labels, masks, and the same five splits**, under both unit treatments — not the published 54.3% constant. Documented reason (A5): protocol sensitivity of OBS metrics (OBSD 1.9–41% Top-1 across setups). Executed by a **baseline team disjoint from the pipeline team** (anti-sandbagging). If the authors' code is unavailable, reimplementation follows the paper spec; a **reproduction gate** is run first on the paper's own published split: Top-10 within ±3.0 points of 54.3% (frozen tolerance). Gate failure does not cancel the paired run — the paired comparison remains primary per A5 — but the reproduction deficit is reported as a first-class protocol-sensitivity finding.

**Endpoints and tests (frozen).**
- Primary: split-level Top-10 accuracy difference (pipeline − CipherOBS rerun), one-sided paired t-test over the 5 splits, α = 0.05, Holm-corrected over the two unit treatments. "Method advance" (E1) is licensed only if U-A passes after Holm AND U-B agrees in direction (A19 rule §2).
- Secondary: pooled exact McNemar over character-split paired hit indicators; Top-50 endpoint, same structure.
- Parity band (frozen prereg): pipeline Top-10 within ±2.0 points of the paired baseline licenses only "replication-grade method."
- The published constants 54.3%/86.6% are reported descriptively only; they are not a comparison target (A5).
- Per A1's program-wide logic applied via the frozen prereg: missing any registered criterion = disconfirmation, not "promising."

### 3.2 A6 contamination instrument (primary; tightened)

**Prospective subset = primary contamination instrument.** Membership: deciphered characters whose *accepted* decipherment postdates **T_c**, the latest training-data cutoff among ALL pretrained components used anywhere in either arm (recorded in appendix PA-6 before scoring). Enumeration by the custodian from frozen sources: National Museum of Chinese Writing award batches (2016 mechanism: China Daily, <https://www.chinadaily.com.cn/china/2016-10/28/content_27203697.htm>; second batch with named first-prize winner Zhou Zhongbing, Henan Provincial Government 2024-01-26, <https://english.henan.gov.cn/2024/01-26/2893169.html>) plus peer-reviewed acceptances in the oracle-bone philology journal record. The enumerated list (with per-character source and acceptance date) is deposited before any scoring contact.

**Frozen criterion (A6, no grace band):** if (standard held-out mean Top-10 − prospective-subset Top-10) > 5.0 points in either arm/treatment, the deficit is **reported as evidence of leakage**; the standard-holdout result for that arm/treatment is quarantined from any method-advance claim, and the prospective-subset number becomes the only figure licensed for contamination-robust E1 claims. The frozen prereg's 20-point quarantine trigger is superseded by A6. Exact binomial CIs are reported alongside the point-estimate rule; the appendix power analysis (PA-8) quantifies the false-flag rate and records that the rule is deliberately conservative against leakage.

### 3.3 H-OBS-2 — proposals for genuinely undeciphered graphs (E2; E3 pathway), as amended by A6/A7

**Eligibility (frozen prereg + A19):** target graph must (a) be undeciphered under **both** unit treatments (U-B eligibility requires panel-ratified merge status), and (b) have ≥5 legible attested contexts in the OBS-P1 context corpus (below 5 → E0-bar). Conditional on H-OBS-1 not returning a calibrated negative (frozen prereg: a missed H-OBS-1 threshold "caps H-OBS-2" — operationalized: proposals may still be scored but the family headline is capped at "candidate list from a below-SOTA pipeline").

**Generation vs testing (G2 firewall).** The hypothesis-generation team produces, per target graph, the pipeline's Top-10 candidate identifications with rationale. A disjoint test-execution team runs the registered battery; a disjoint scoring custodian holds decoy identities and control-panel composition.

**Prong (a):** candidate ranks in the pipeline's Top-10 (mechanical check).

**Prong (b) — decoy-ranked context fit.** ≥99 decoy identifications per proposal, drawn with seed 20260811 from the deciphered inventory (modern identities of the 1,588/merged categories) ∪ a registered archaic-lexicon supplement list (deposited in appendix PA-5 before generation), matched to the candidate on context-corpus frequency (±1 tercile) and structural class where annotated. Frozen context-coherence score S = mean per-context log-probability of the candidate filling the target slot under a context model trained by the test team **only** on transcribed inscriptions with all H-OBS-2 target graphs masked. Success requires the proposal to rank 1st of 100 (empirical p < 0.01) across **ALL** legible attested contexts. Holm correction across all proposals scored in the run; every scored proposal logged (G5).

**Prong (c) — blind formula-coherence adjudication.** Judged against the divination-formula grammar (preface–charge–prognostication–verification; Run 1 dossier OBS §2, <https://www.nature.com/articles/s41597-024-03807-x>) in every context. Judges see the candidate set (proposal + decoy sample) without knowing which is the pipeline's. **A7 binding split:** expert-proxy (LLM) adjudication is permitted in development only; every headline E2 claim requires the named human palaeographer panel (§6) under the frozen rubric. One incoherent context falsifies the proposal (frozen prereg).

**Control panels (A16-conformant; identical reporting policy, adjudicators not told which items are controls).** Interleaved with real proposals: (P+) 20 positive controls — held-out *deciphered* characters presented as unknown with their true identity as candidate; (P−) 20 wrong-identity controls — held-out deciphered characters paired with a frequency-matched false identity; (Pø) 10 corrupted-glyph controls — synthetically corrupted images with no true identity. **Registered consequence:** any P− or Pø item that passes the full (a)–(c) battery is a miscalibration finding that quarantines all concurrently scored proposals pending root-cause analysis and re-run. P+ pass rate is reported as the battery's sensitivity estimate. Report rates and confidence distributions are compared across controls and real targets; divergence is itself a failed control (A16).

**Escalation:** survivors are E2 "candidate decipherment hypotheses" only. E3 requires external adjudication: submission to the National Museum of Chinese Writing expert committee (mechanism verified live and exercised: 2024 second award batch — tribunal falsification record; Henan gov URL above) or equivalent peer-reviewed acceptance. Until external acceptance, the word "deciphered" is prohibited (frozen prereg H-OBS-2).

---

## 4. Claim-ladder levels attempted and E-class licensing (A18 format)

| Ladder level | Attempted? | Content | Licensed E-class (per tribunal band: E2 now; E3 via A7 path) |
|---|---|---|---|
| L1 glyph normalization | Yes | A19 category↔graph-type↔allograph↔modern-identity mapping; merge deliverable | E1–E2 descriptive/structural (headline merge decisions require A7 panel) |
| L2 segmentation | Not contested (solved system) | Inherited from field consensus | n/a |
| L3 structural classes | Yes | Stratification classes; structural features; mapping-outcome statistics | E1–E2 structural |
| L4–L5 | Not independently claimed | Phonology/grammar enter only via established readings of context graphs | no new claims |
| L6 lexical correspondence | Yes | Graph → modern-character identifications (H-OBS-2) | **E2 candidate hypotheses maximum**; E3 only upon external acceptance (Anyang committee / peer review) |
| L7 translation | **Prohibited** (G2, program-wide Runs 2–3) | — | — |

Claim-band statement (A18): **OBS: E1 method claims (H-OBS-1 retrieval, both arms) · E2 candidate identifications (H-OBS-2 survivors, A7-reviewed) · E3 only upon external adjudication · E0 for any graph with <5 legible contexts.**

## 5. Preregistered success/disconfirmation criteria (references, not new authorship)

This design adds no adjudication criteria. The binding tests are:
- **H-OBS-1** (frozen prereg §3) with comparison target replaced per **A5** (paired CipherOBS rerun, identical labels/masks/five splits) and contamination control per **A6** (prospective subset primary; 5-point equivalence; larger deficit = leakage evidence, no grace band). Disconfirmation: any registered criterion missed → H0 stands; calibrated negative reported; caps H-OBS-2.
- **H-OBS-2** (frozen prereg §3): all of prongs (a)–(c); one incoherent context falsifies; ≥5-context eligibility floor; Holm across proposals; generator ≠ tester (G2); headline adjudication per **A7** (named human palaeographers; expert-proxy development-only); E3 only via external mechanism.
- **A19**: all results under both frozen unit treatments; treatment disagreement blocks positive claims and is itself the finding.
- **A17**: the pre-scoring appendix (§9) must be completed and deposited in the tribunal record before this experiment contacts data; an incomplete appendix at data contact is a protocol violation.
- **G5/G9**: every test logged; nulls reported at headline prominence.

## 6. Human-expert loop (A7, binding)

- **Panel:** ≥3 named human oracle-bone palaeographers, recruited and named in the tribunal record **before** any headline adjudication or U-B headline merge ratification. Qualification criteria (frozen): peer-reviewed publication record in jiaguwen palaeography; no authorship of the pipeline or of CipherOBS; dataset authorship disclosed and recorded. (No names are invented here; recruitment is a completion gate, deposited per A17/PA-9.)
- **Duties:** (i) ratify/reject U-B undeciphered-side merges for H-OBS-2 targets; (ii) blind prong-(c) formula-coherence adjudication under the frozen rubric (appendix PA-9: per-context 3-point coherence scale with written justification; "incoherent" = any context where the candidate violates the divination-formula slot grammar or attested collocational usage of the read context graphs; majority rule; all judgments archived); (iii) verify the G8 bridge sample (§1.2); (iv) countersign any headline E2 claim.
- **E3 path:** panel-surviving proposals are submitted to the National Museum of Chinese Writing expert committee (Anyang; mechanism live per Henan gov 2024 announcement) and/or peer review. Submission outcomes are logged prospectively whatever they are.
- Expert-proxy (model-based) adjudication is used only in development iterations and is never cited in support of any claim (A7).

## 7. Contamination controls (G6)

1. **Prospective subset primary (A6)** — §3.2; the program's designated contamination-resistant instrument (G6 explicitly prefers post-cutoff material).
2. **T_c registration** — training cutoffs of every pretrained component in both arms recorded before scoring (PA-6).
3. **Custodian re-keying** — all category IDs replaced with fresh random IDs; `ID_to_chinese.json` (public on GitHub since 2024, hence plausibly memorized) is never exposed to modeling/scoring teams.
4. **Memorization probe (frozen)** — before scoring, the custodian queries every LLM/LVLM component with 100 randomly sampled original HUST-OBC IDs for their character mappings; above-chance recall is recorded and reported with the results (re-keying already blocks the exploit; the probe documents exposure).
5. **Evolution-chain masking** — §3.1; blocks the paleographic-descendant channel.
6. **Paired-arm symmetry** — both arms share identical masks/splits, so the *comparative* E1 claim is protected even under shared contamination; the *absolute* accuracy level is only licensed through the prospective subset. This asymmetry is stated in every report.
7. **Flagging rule** — all test material predating T_c is flagged as plausibly in training data (G6); no unflagged-material claim is made.

## 8. Null results: scientific meaning and publishability (G9)

- **H-OBS-1 null (pipeline ≤ paired baseline):** a calibrated negative — "the program's pipeline does not exceed a protocol-matched CipherOBS under leakage-hardened, evolution-chain-masked, character-level splits." Publishable because the paired rerun is itself the first controlled replication of the 2026 SOTA under hardened splits: if the *rerun's* accuracy falls far below the published 54.3% (protocol sensitivity documented at 1.9–41% Top-1 for OBSD), the finding is that published OBS decipherment-aid numbers are protocol- and leakage-inflated — a direct correction to the field's evaluation practice.
- **A6 leakage flag:** a >5-point prospective deficit is positive evidence that held-out-character evaluation on pre-cutoff material overstates capability — bearing on every 2024–26 OBS ML paper that evaluates on long-published decipherments.
- **H-OBS-2 family null (no proposal survives):** registered conclusion — "the pipeline cannot advance OBS residue identifications at current information conditions." Because OBS is the program's *best-case* system (only system with an answer key and a live institutional adjudicator — checkpoint-2 matrix, upheld verdict), this null upper-bounds what current methods can deliver anywhere in the program: a failure at the field's most favorable information conditions is the strongest available negative about AI-assisted decipherment generally.
- **OBS-P1 failure null:** "no audited bulk context corpus exists for undeciphered-graph occurrences" — a data-reality finding that corrects the field's implicit assumption that context-fit evaluation is currently executable at scale.

## 9. Compute and team estimate

- **GPU compute: order 10^3 A100-hours.** Breakdown: 2 arms × 2 unit treatments × 5 splits = 20 training runs of a CipherOBS-class generative-retrieval model on ≤140k images (~50–100 A100-h each → 1,000–2,000 h), + development overhead ×~2, + encoder pretraining, context model, controls and prospective inference (~200–500 h). Envelope: **~2,000–6,000 A100-hours**. (Design decision/engineering estimate; not an empirical citation.)
- **Team: ~14–20 team-months** over 6–9 calendar months: 2 ML engineers (arms, firewalled) ~10–12 tm; 1 data custodian/engineer ~3–4 tm; test-execution/statistics agent-team ~2 tm; palaeographer panel ~0.5–1 tm consulting equivalent; coordination/tribunal interface ~1 tm.

## 10. Reporting

All results (both treatments, both arms, all five splits, prospective subset, all control panels, all H-OBS-2 proposals incl. failures) reported at equal prominence; error-reporting language per tribunal I.3.2 ("N agents; no agent-run failures; K citation-verification failures subsequently corrected"); deviations reported as protocol violations per the frozen prereg deviation rule; headline claims routed through the cross-model tribunal (G7).


**Compute estimate:** Order 10^3 A100 GPU-hours (envelope ~2,000-6,000): 20 training runs (2 arms x 2 unit treatments x 5 splits) of a CipherOBS-class generative-retrieval model at ~50-100 A100-h each, plus ~2x development overhead, encoder pretraining, context model, control panels and prospective-subset inference. Team ~14-20 team-months over 6-9 calendar months: 2 firewalled ML engineers (pipeline arm, baseline-rerun arm), 1 data custodian/engineer, test-execution/statistics team, >=3 named human palaeographers (consulting), tribunal coordination.

**Null result meaning:** Every null is a registered deliverable (G9). (1) H-OBS-1 null: the pipeline does not beat a protocol-matched CipherOBS rerun on leakage-hardened splits - and if the rerun itself lands far below the published 54.3% Top-10, the finding is that published OBS decipherment-aid numbers are protocol/leakage-inflated (protocol sensitivity already documented at 1.9-41% Top-1 for OBSD), a direct correction to field evaluation practice. (2) A6 flag: a >5-point prospective-subset deficit is positive evidence of training contamination in standard held-out evaluation, bearing on all 2024-26 OBS ML literature. (3) H-OBS-2 family null: the pipeline cannot advance OBS residue identifications at current information conditions - publishable as the program's strongest negative, because OBS is the adjudicated best-case system (only one with an answer key and a live institutional adjudicator); failure at the most favorable information conditions upper-bounds AI-assisted decipherment claims program-wide. (4) OBS-P1 failure: a data-reality finding that no audited bulk context corpus for undeciphered-graph occurrences exists, correcting the field's assumption that context-fit evaluation is currently executable.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (deposit to tribunal record before data contact; items marked [gate] are custodian completion gates that must be deposited before any scoring-agent contact). PA-1 Dataset pins: HUST-OBC Figshare DOI 10.6084/m9.figshare.25040543.v3 (140,053 images; 1,588 deciphered/77,064 images; 9,411 undeciphered/62,989 images; undeciphered sources L, X, Y+H; CC BY-NC 4.0) + GitHub Pengjie-W/HUST-OBC; EVOBC HF HaisuGuan/EVOBC + Figshare share ce2cf55b35a2f8ecc4c6 (229,170 JPGs; 13,714 categories; 6 stages; CC BY-NC-SA 4.0); SHA-256 manifests computed at acquisition [gate - not obtainable pre-acquisition]. PA-2 Unit treatments: U-A category-as-shipped (primary); U-B deterministic NFC-codepoint merge (deciphered) + cosine>=0.85 top-5-neighbor merge candidates (encoder trained on deciphered images only) with A7 panel ratification (undeciphered); sensitivity 0.80/0.90 descriptive only; both treatments reported everywhere; disagreement blocks claims. PA-3 Splits: 5 splits, 10% of deciphered inventory (U-A n=159/split), NumPy PCG64 seeds 202608111-202608115; stratification by image-count tercile (frozen frequency proxy) + structural class per fallback ladder (HUST-OBC annotation -> licensed PD-OBS files -> tercile-only; rung used recorded [gate]); evolution-chain masking of all HUST-OBC and linked EVOBC images across all 6 stages. PA-4 Tolerances: CipherOBS reproduction gate +/-3.0 Top-10 points on the paper's own split; replication band +/-2.0 points (frozen prereg); method-advance = one-sided paired t over 5 splits, alpha=0.05, Holm over {U-A,U-B}, plus direction agreement across treatments; A6 equivalence 5.0 points, point-estimate rule, no grace band; H-OBS-2 decoy rank 1/100 (p<0.01), Holm over all proposals scored. PA-5 Panels: 99 decoys/proposal, drawn seed 20260811 from deciphered inventory + registered archaic-lexicon supplement [gate: list deposited before generation], matched on context-corpus frequency (+/-1 tercile) and structural class; control panels P+ 20 disguised deciphered, P- 20 wrong-identity, P0 10 corrupted-glyph; any P-/P0 pass quarantines concurrent proposals (A16 reporting-rate comparison across controls vs targets). PA-6 Contamination: T_c = latest training cutoff over all pretrained components in both arms [gate: recorded before scoring]; prospective-subset enumeration from Anyang award batches (China Daily 2016-10-28; english.henan.gov.cn 2024-01-26 second batch, named winner Zhou Zhongbing) + peer-reviewed acceptances, list with per-character dates deposited [gate]; custodian re-keying of all IDs; 100-ID memorization probe protocol. PA-7 OBS-P1 context-corpus audit: four binary checks (bulk sign-level transcription; undeciphered tokens marked; Jiaguwen-Heji catalog linkage; license) on OBIMD (GitHub + HF KLOBIP/OBIMD, 10,077 images per Open-Oracle index) then Yinqiwenyuan; G8 bridge test 100 sampled linkages, >=98 correct required [gate; failure blocks H-OBS-2]. PA-8 Power analysis (assumptions stated as design decisions): H-OBS-1 primary - with split-level SD of paired Top-10 differences assumed 2.0 points, paired t (df=4, alpha=.05 one-sided) detects ~2.5-point advantage at ~80% power; per-split McNemar (n=159, ~20% discordance) detects ~9-10 points; pooled 5-split McNemar detects ~4-5 points. A6 instrument: at prospective n~25, SE of subset accuracy ~10 points; false-flag probability under true equality ~30% (one-sided) - recorded as deliberately conservative against leakage per A6's no-grace-band language; exact binomial CIs reported alongside. H-OBS-2: rank-1-of-100 test has size 0.01 exactly by construction; P+ panel (n=20) estimates battery sensitivity with binomial SE <=11 points. PA-9 A7 panel: >=3 named human oracle-bone palaeographers, names + disclosures deposited before headline adjudication or U-B headline merge ratification [gate]; qualification criteria frozen (jiaguwen palaeography publication record; no pipeline/CipherOBS authorship; dataset authorship disclosed); frozen rubric: per-context 3-point coherence scale against preface-charge-prognostication-verification slot grammar with written justification, majority rule, blind to pipeline choice, one incoherent context falsifies; E3 submission protocol to National Museum of Chinese Writing committee logged prospectively. PA-10 Statistical analysis code frozen and hashed before any scoring [gate]. PA-11 Search/run logs per G5 (all splits, restarts, proposals, panel judgments) with auditable deposit.

# Khipu Record Linkage & Prospective Prediction

# Run 3 Experiment Design — Family KHI: Khipu Record Linkage (H-KHI-1) and Prospective Attribute Prediction (H-KHI-2)

**Designer role statement (G2/HARKing guard):** This document specifies data, method, roles, and operational appendix values. It authors **no** adjudication criteria: every success/disconfirmation test below is a citation of `run2-preregistration-FROZEN.md` §7 (H-KHI-1, H-KHI-2) as amended by the binding appendix `tribunal-record-and-prereg-amendments-v1_1.md` (A11, A12, A15, A17, A18, A19). Where this design adds operational constraints, they only **narrow** registered thresholds (permitted by the freeze block: "appendices may narrow but never widen registered thresholds").

**Adjudicated gate (tribunal record §I.2):** Khipu = **"E2 now; E3 path via two-team masking design (A12)."** No claim in this design is licensed above that band.

---

## 1. Hypotheses executed and amendment compliance map

| Frozen ID | As amended by | What this design adds (narrowing only) |
|---|---|---|
| **H-KHI-1** (numeric record linkage vs permuted archives; E2) | **A11** (structure-preserving nulls; logged multiplicity over all groupings), A17, A19, G5, G6, G8 | Closed grouping-scheme set (4 schemes); degenerate-null diagnostic; archive enumeration freeze; power floor (≥20 alignable entries); transcription QC gate |
| **H-KHI-2** (attribute-encoding generalization; E2→E3) | **A12** (two-team masking with custodian), A17, A19, G3, G6, G7; name-level sub-claims route through **H-ONO-1** per **A15** | Released-fields-only baseline model (stricter than frozen requirement); attribute floor (≥25 attested individuals); frozen name-class taxonomy procedure |

Applicable global rules: G1–G9 of the frozen prereg. A16 (Phaistos control integrity) and A7 (OBS human experts) do not bind KHI directly; the human-loop analog is §10 below.

---

## 2. Data acquisition plan — grounded in the audited reality

### 2.1 Khipu side (verified 5/5 by the Run 2 data-reality audit)

- **Resource:** Open Khipu Repository (OKR) **v2.1.0**, Zenodo deposit DOI 10.5281/zenodo.18025748, published 2025-12-22; single file `open-khipu-repository-2.1.0.zip`, **79,808,932 bytes, md5:c741d4d3bbdeba531f547d10f85e2925** (Zenodo API record, retrieved 2026-08-11, <https://zenodo.org/api/records/18025748>). The Run 2 audit **downloaded and opened this zip** and counted directly: `khipu_main` = **619**, `primary_cord` = 633, `cord` = **54,403**, `cord_cluster` = 14,847, `knot` = 110,677, `ascher_cord_color` = 56,306; SQLite `khipu.db` with 25 tables + `okr-kh-numbers.csv` master registry + raw recording sheets (xlsx/docx/jpg) per khipu group (Run 2 audit, "Open Khipu Repository (OKR)" row and note; <https://github.com/khipulab/open-khipu-repository>).
- **License:** MIT per the LICENSE file read directly from the zip (audit); the Zenodo record's license field says `other-open` (Zenodo API, above). **Disagreement reported as-is; both carried.** Redistribution of derived tables is safe under either.
- **Not acquired / not claimed:** khipu photographs (OKR is structural transcription only — Run 1 dossier, Khipu §5, citing the OKR README, <https://github.com/khipulab/open-khipu-repository/blob/master/README.md>). No paleographic or photographic claims are in scope (G8).
- **G8 data-basis declaration:** khipu side = (iv) structured relational DB, version pinned above. Results do not transfer to photographs or to re-recordings without a registered bridging test.

### 2.2 Archival side (the audited gap this design must close)

The Run 2 falsifier's finding is binding input: **"the colonial archive side is neither digitized nor enumerated, so the Holm denominator (G5 search log) is defined only over documents the team happens to inspect"** (Checkpoint 2 matrix, Khipu — WEAKENED, <https://zenodo.org/records/18025748> et al. cited therein). Therefore the design's first deliverable is an **archive enumeration freeze (Phase A0)**: a closed, dated list of document series constituting the entire search universe for this run. Documents outside the frozen list may not be scored in this run (they may seed a future amended run).

**Candidate collections for Phase A0 enumeration** — registered here as *leads*, explicitly **not verified by the Run 2 audit** (which audited no archival collections); each must be confirmed, with series names and item counts, before the enumeration freezes:

1. **Archivo General de la Nación del Perú** (Lima), colonial holdings (visitas, revisitas, padrones, tribute assessments) — institutional portal <https://agn.gob.pe>.
2. **Archivo General de Indias** (Seville) via **PARES — Portal de Archivos Españoles**, <https://pares.cultura.gob.es> (Audiencia de Lima materials; partial digitization makes this the most machine-accessible lead).
3. **Regional archive for the Áncash/Santa drainage** (jurisdiction of the Santa Valley/Corongo positive-control pair; the Medrano & Urton 2018 revisita concerns San Pedro de Corongo — *Ethnohistory* 65(1), <https://read.dukeupress.edu/ethnohistory/article-abstract/65/1/1/133085/Toward-the-Decipherment-of-a-Set-of-Mid-Colonial>). Institutional existence and holdings to be verified in A0; the holding location of the 1670 revisita itself is taken from the paper at A0, not asserted here.
4. **Biblioteca Nacional del Perú**, manuscript collections — <https://www.bnp.gob.pe>.
5. **Published visita/revisita transcriptions** (print; keyable; primary backbone of the decoy panel because transcription cost is low): the mid-16th-century Andean visita editions of the ethnohistorical literature (e.g., the Huánuco 1562 and Chucuito 1567 visitas). These are cited as *leads to be bibliographically verified in A0* — the project record contains no audit of them, and per the evidence rules no count or edition detail is asserted here.
6. **Ecclesiastical archives** (Archivo Arzobispal de Lima; parish padrones) — lead, unverified.

**Genre/region/period eligibility rule (frozen):** documents eligible for the search universe and decoy panel are Spanish colonial administrative enumerations — visitas, revisitas, padrones, tribute tasas — pertaining to the Viceroyalty of Peru, dated 1532–1700, containing ≥20 numeric entries organized in named groups (ayllu/pachaca/parcialidad). Rationale: matches the only demonstrated linkage genre (Medrano & Urton 2018, above) without narrowing to its region.

### 2.3 Count-universe reconciliation (A19 — frozen unit treatment)

The A19 unit-mismatch registry records: "khipu counts 619 (OKR khipu_main v2.1.0) vs 702/703 (other universes)." Frozen mapping:

- **U1 = 619** — rows of `khipu_main` in `khipu.db` v2.1.0, verified by direct count (Run 2 audit). **U1 is the sole modeling/analysis universe.** Every model, search, and denominator in this design runs on U1.
- **U2 = 702** — the KH-number registry universe: KH numbers assigned through KH0702 (Zenodo v2.1.0 release notes: "72 new KH numbers (KH0631–KH0702) were assigned," <https://zenodo.org/records/18025748>), matching "702 quipus with public data as of Jan 2026" ("Quipu," Wikipedia, <https://en.wikipedia.org/wiki/Quipu>). U2 exceeds U1 because KH numbers cover khipus whose data exist in the release only as raw recording sheets not yet ingested into `khipu.db` tables (audit: release contains per-group xlsx/docx/jpg). **U2 is used only for census statements, always labeled.**
- **U3 = 703** — a count carried in the A19 registry whose universe is not identified in the tribunal record. **No provenance is invented here.** Frozen resolution procedure: at first data contact, count rows of `okr-kh-numbers.csv` and enumerate KH numbers absent from `khipu_main`; deposit the delta list and the identified source of "703" (e.g., registry rows including a superseded/duplicate entry) as a dated appendix addendum. This bookkeeping changes no threshold.
- **U4 (context only) = ~1,650–1,700** documented khipus worldwide (Thompson 2025 census; Khipu Field Guide, <https://khipufieldguide.ghost.io/counting-the-khipus-how-many-are-there-to-study/>). Used solely to state coverage honestly: U1 is ~37% of U4 (falsifier's figure), so *absence-of-linkage conclusions are conditional on the OKR sample*, never on "khipus" as a population.

---

## 3. Method — specified to implementation level

### Phase A0 — Archive enumeration freeze (before any scoring contact)

1. Verify each §2.2 lead: institution exists, series exists, item-level finding aid or catalog obtained; log every catalog consulted (G5 search log).
2. Freeze the **search universe list**: every document series admitted, with item counts. Freeze the **decoy panel**: ≥100 eligible documents (§2.2 rule) reserved as decoys, disjoint from any document later proposed as a match. Deposit both lists, dated and hashed, into the tribunal record. **No linkage scoring may occur before this deposit (A17).**
3. Transcription protocol for every document used (match candidates and decoys): HTR-assisted (tool name+version logged) followed by **independent double keying of all numeric fields and group structure by two human transcribers**; per-field agreement must be ≥99.5%, disagreements resolved by a third key; the agreement statistics are deposited with each transcript. A document failing QC does not enter scoring.

### Phase A1 — Khipu-side feature extraction (deterministic, code-frozen)

1. Verify the deposit: recompute md5 of the zip against `c741d4d3bbdeba531f547d10f85e2925`; compute and deposit sha256; recount the six audited tables; any deviation from the audit's counts (619/633/54,403/14,847/110,677/56,306) halts the run with a discrepancy report.
2. For each khipu in U1, compute per-pendant **Locke decimal values** from the `knot` table (single knots = powers of ten by tier, long knots = units, figure-eight = 1; algorithm implemented once, unit-tested against published OKR/Khipu Field Guide worked examples, code hash deposited at appendix freeze). Decimal knot arithmetic is the accepted, uncontested layer (Locke 1923; "Quipu," Wikipedia, <https://en.wikipedia.org/wiki/Quipu>).
3. Extract structure: cord clusters (`cord_cluster`), subsidiary hierarchy, top/summation cords, Ascher color codes (`ascher_cord_color`), recto/verso attachment where recorded. Cords flagged damaged/uncertain are excluded from primary scoring and included only in registered sensitivity analysis S1 (both reported — A19 dual-treatment discipline).
4. **Grouping schemes (closed set, frozen; A11 multiplicity):** G-1 recorded cord clusters; G-2 color-band grouping (maximal runs of consecutive pendants with identical Ascher color code); G-3 spacing segmentation (gaps in recorded attachment positions); G-4 fixed-width six-cord grouping (the Santa Valley convention — Medrano & Urton 2018). **No other grouping may be scored in this run.** Every (khipu, document, grouping) triple scored is logged; the Holm denominator (G5) is the count of all such triples.

### Phase B — H-KHI-1 linkage search and scoring

1. **Eligible khipu set:** all of U1. A prioritization heuristic (provenance metadata suggesting colonial-era context; presence of color banding; group-size regularity) may order the search but cannot exclude: it affects cost, not validity, and is logged.
2. **Frozen linkage score** (prereg: "count of exact numeric matches under matching rules… fixed in the pre-scoring appendix BEFORE any archive search"): for a (khipu grouping, document) pair, an **order-preserving alignment** (dynamic programming) between the sequence of khipu group-value vectors and the sequence of document entry-value vectors; score = number of exactly matched values (integer equality; tolerance = exact, per frozen text); **subtotal consistency constraint**: where both a khipu summation cord and a document subtotal exist for aligned blocks, they must match exactly or that alignment is voided. Secondary endpoint: matched-and-subtotal-consistent count. Scoring code frozen and hashed before Phase B.
3. **Null N1 — within-document, structure-preserving (A11):** admissible permutations are exactly those preserving (i) group sizes, (ii) all attested subtotal relationships, (iii) the within-group rank profile (ordering structure). Concretely: permute entry values only within a group and only among positions whose values are tied or whose rank pattern is preserved; permute whole groups only within same-size, same-parent classes carrying their subtotals with them. Because tribute values are small tie-heavy integers, this permutation group is typically large; **degenerate-null diagnostic (frozen):** if the admissible group yields <100 distinct document images, N1 is declared underpowered for that pair, reported as such, and N2 becomes the binding null — both p-values are always reported. Draws: 9,999 (narrowing the frozen "≥1,000").
4. **Null N2 — same-genre decoy documents:** the khipu grouping is scored against every decoy-panel document under identity plus 99 N1 draws each → ≥10,000 null draws; empirical p = (1 + #{null ≥ observed})/(1 + N). This operationalizes the frozen "≥100 same-genre decoy documents" so that p < 0.001 is resolvable — a pure-rank test over 100 decoys cannot reach 0.001, and leaving that unstated would be a discretionary hole.
5. **Adjudication (cited, not authored):** exactly the frozen H-KHI-1 text — H1 requires empirical p < 0.001 on **both** nulls, Holm-corrected over the full logged search (denominator from Phase B.1/A1.4); matching-rule changes after first contact void the pair; failure to beat nulls → no linkage claim.
6. **Positive control (frozen prereg):** the pipeline must recover the Santa Valley match — six khipus vs the 1670 San Pedro de Corongo revisita, 132 tributaries vs 133 color-banded six-cord groups (Medrano & Urton 2018, above; Run 2 method-evidence §5). The six khipus' OKR identifiers are resolved from the paper + `okr-kh-numbers.csv` and deposited in the appendix at A0. **Interpretation discipline (falsifier-compliant):** recovery under our *pre-frozen* rules is reported as pipeline functionality only; it contributes zero evidence to any new claim, because the 2018 correspondence is an unadjudicated retrospective match whose rules were chosen after seeing both sides (Checkpoint 2, Khipu — WEAKENED). Per frozen prereg, failure to recover it = pipeline defect, all family results quarantined; the rule-sensitivity information such a failure carries about the 2018 pair is reported to the tribunal, not adjudicated here.

### Phase C — H-KHI-2 prospective attribute prediction under A12 two-team masking (the E3 instrument)

**Trigger:** at least one *new* khipu–document pair (not Santa Valley) passes H-KHI-1 in full. If none does, Phase C does not run and the registered E2-ceiling finding issues (§7).

**Roles (all disjoint; G2):**
- **Team L (linkage):** runs Phases A/B. Upon a passing new pair, transmits to Team P **only** the numeric fields establishing the match (values, group sizes, order, subtotals) — per A12 verbatim: "linkage team reveals only the numeric fields establishing a new khipu–document match; attributes/names/status remain sealed with a custodian."
- **Custodian (named human; see §5):** receives the full QC'd transcript; splits it into released numeric fields vs sealed attribute fields (names, statuses, moiety/parcialidad labels, offices, kin notes); audits the release for leakage channels; holds the seal.
- **Team P (prediction):** never sees sealed fields. Fits encoding models on linkage-established training pairs (Santa Valley may be used for *training* only): cord color → name/name-class; recto/verso attachment → status/moiety (hypotheses from Medrano & Urton 2018 and FitzPatrick 2024, *Ethnohistory* 71(4):443, <https://read.dukeupress.edu/ethnohistory/article-abstract/71/4/443/391504/New-Insights-on-Cord-Attachment-and-Social>; assumed by no test — they are what is being tested). Model frozen before the new pair's document is read by anyone on Team P (frozen prereg).
- **Scoring agent:** executes the frozen metric on deposit + unmasking; had no role in model construction.

**Deposit protocol (E3 credit condition, frozen prereg: "E3 credit only if the prediction was deposited (hashed) before archival lookup"):** Team P produces a predictions file (per individual/cord: predicted attribute values with the frozen taxonomy); sha256 of the file is entered into the tribunal record and the ciphertext lodged with the custodian **before** the custodian unmasks. The custodian verifies hash-before-unmask ordering and files a custody log.

**Name-class taxonomy (frozen procedure, closing a discretionary hole):** Team P freezes its name-class taxonomy from training-pair data + published Andean onomastics before deposit; the custodian maps sealed names into that taxonomy under frozen mapping rules; unmappable names → class "other". Any claim at the level of a *specific name* (not class) is an onomastic claim and must satisfy **H-ONO-1 in full with its A15 frozen corollary universe** (p < 0.005 on both decoy-name and scrambled-value nulls) — otherwise it is inadmissible program-wide.

**Adjudication (cited):** frozen H-KHI-2 — held-out-pair accuracy vs ≥1,000 attribute-permutation nulls (this design runs 9,999), p < 0.01; at least one genuinely new pair. **Added stricter control (narrowing):** Team P's prediction must also beat a *released-fields-only baseline model* (predicting attributes from numeric fields, order, and group structure alone). Rationale: census list position often correlates with status/moiety; without this baseline, a "confirmed" attachment→moiety encoding could be position information laundered through the linkage. Success requires beating both the permuted null (frozen criterion) and the baseline (registered narrowing).

### What is *not* attempted

No L5 phonetic, L6 lexical, or L7 translation output; no glottographic claim about khipus; Hyland's Collata logosyllabic hypothesis is neither assumed nor tested (frozen prereg §7 preamble; *Current Anthropology* 58(3), <https://www.journals.uchicago.edu/doi/abs/10.1086/691682>). Khipu narrative content remains shape-D contested (plan v2 §1).

---

## 4. Claim ladder and E-class licensing (A18 claim-band format)

| Claim band | Ladder level | Licensed E-class (per tribunal I.2 + A18) | Instrument |
|---|---|---|---|
| Cord/knot value normalization, grouping, hierarchy parsing | L1–L3 | E2 (structural claims on held-out real khipus); descriptive outputs E0-safe | OKR U1, deterministic extraction |
| Khipu–document numeric linkage ("this khipu records this document's enumeration") | L3–L4 | **E2** | H-KHI-1 as amended (A11) |
| Attribute-encoding generalization, retrospective/pair-specific (color→name-class, attachment→moiety) | L4 | **E2 ceiling** | H-KHI-2 without prospective deposit |
| Attribute-encoding confirmed by **deposited-before-unmasking** prediction on a new independently linked pair | L4 | **E3 path** — the program's khipu E3 instrument per A12; headline claim additionally requires the cross-model tribunal (G7) | H-KHI-2 + A12 masking + custodian |
| Specific-name readings | L4/L6 boundary | Only via H-ONO-1 (A15), within host gate | H-ONO-1 template |
| Phonetic/lexical/narrative readings | L5–L7 | **Not licensed; not attempted** (E0/E1 band; L7 prohibited program-wide in Runs 2–3, G2) | — |

---

## 5. The custodian role, concretely (A12)

**Eligibility (frozen):** a named human, professionally competent in colonial Andean paleography/archival practice, with (i) no authorship or co-authorship of any khipu encoding hypothesis under test (this excludes the hypothesis authors Medrano, Urton, FitzPatrick, Hyland — note FitzPatrick administers OKR and Medrano/Hyland sit on its advisory board per the audit, so OKR affiliation alone requires case-by-case conflict review); (ii) no role in Teams L/P, scoring, or this design; (iii) contractual duty to the program's tribunal record, not to any team. Identity deposited in the tribunal record before Phase C.

**Duties:** (1) receive the full QC'd transcript of the new pair's document directly from the transcription unit — Teams L/P never receive it whole; (2) partition fields into released (numeric/structural) vs sealed (attributes/names/status) per the frozen schema; (3) leakage audit of the release (e.g., group labels that are themselves names are sealed and replaced by opaque tokens); (4) receive and timestamp Team P's hashed deposit; verify hash-before-unmask ordering; (5) unmask sealed fields to the scoring agent only; (6) file a custody log (dates, hashes, transmissions, anomalies) as a first-class tribunal deliverable; (7) authority to void the trial on any seal breach — a voided trial is reported, not rerun silently.

**Archival-side human loop (the KHI analog of A7's human-expert requirement):** document transcription and the leakage audit are human-expert tasks (paleographers, double-keyed per §3.A0.3). Any headline E3 claim goes to the cross-model tribunal (G7) and — adopted here as a narrowing commitment consistent with A7's principle that expert-proxy adjudication suffices only in development — to at least one named human Andeanist ethnohistorian for review of the archival identification before publication.

---

## 6. Preregistered success/disconfirmation criteria (citations to frozen text — none authored here)

- **H-KHI-1 success:** observed linkage score exceeds both N1 and N2 nulls at empirical p < 0.001, Holm-corrected over the logged search (frozen §7, H-KHI-1, with A11 null construction and G5 denominator). **Disconfirmation:** failure to beat permuted nulls → no linkage claim; failure to recover the Santa Valley positive control under pre-frozen rules → pipeline defect, all family results quarantined (frozen text verbatim).
- **H-KHI-2 success:** held-out-pair attribute accuracy beats attribute-permuted null at p < 0.01 on ≥1 genuinely new pair, with model frozen before document read and hash-deposited predictions for E3 credit (frozen §7, H-KHI-2; A12 procedure). **Disconfirmation:** no generalization → "encoding claims remain pair-specific descriptions (E2 ceiling), and this limit is reported" (frozen text verbatim).
- **Escalation:** E3 only via the A12 instrument; headline claims require the cross-model tribunal (G7). Internal agreement is never corroboration (tribunal meta-finding §I.1).

---

## 7. What a null result means (G9 — null results are deliverables)

1. **No new pair passes H-KHI-1:** the registered finding is a *multiplicity-honest upper bound on the khipu–archive linkage rate over an enumerated search universe* — the first such bound ever produced (the 2018 match was retrospective and un-enumerated; no second match has surfaced since — Checkpoint 2, Khipu). This bounds the "khipus as transcribed census sources" research program quantitatively, conditional on U1 (~37% of documented khipus) and on the frozen archive universe, and is publishable precisely because the search log makes the negative interpretable — the look-elsewhere effect the falsifier flagged is the family's principal hazard, and this run prices it.
2. **New pair passes H-KHI-1 but H-KHI-2 fails:** the numeric-linkage layer replicates while color/attachment encodings do not generalize — directly disciplining the Medrano–Urton color→name and FitzPatrick attachment→moiety proposals to pair-specific descriptions (frozen E2 ceiling), a first-class constraint on the field's most-cited khipu semantic claims.
3. **Santa Valley control not recovered under pre-frozen rules:** per frozen prereg, pipeline defect and quarantine; additionally reported to the tribunal as evidence bearing on the rule-sensitivity of the 2018 correspondence itself (its only formal stress test to date).

Each outcome is reported at equal prominence with any positive finding (G9).

---

## 8. Contamination controls (G6)

- **Deterministic scoring path:** the linkage score, nulls, and permutations are computed by frozen non-LLM code; no language model sits anywhere in the adjudication path, so training-data memorization of the widely published Santa Valley figures (paper, Wikipedia, press) cannot inflate any test statistic.
- **LLM usage boundary:** LLMs may assist only (a) archival triage/HTR post-processing, with every suggested candidate document logged as a search action (counted in the Holm denominator), and (b) code drafting. All LLM-touched transcriptions pass the human double-key QC gate.
- **Prospective instrument preference (G6 verbatim):** the E3 route runs on *unpublished archival documents newly transcribed for this run* — material that cannot be in any model's training data and that no researcher has previously paired with a khipu; this is the contamination-resistant instrument class the prereg prefers.
- **Embargo:** Team P's environment receives no text of the new pair's document before deposit (custodian-enforced); prompts/configs of any LLM tooling used by Team P are logged and auditable.
- **Public-data caveat registered:** khipu.db has been public since 2021; any future learned model touching khipu features must treat OKR as contaminated for held-out purposes across published analyses (logged for downstream designs).

---

## 9. Compute and team estimate

- **GPU:** order **10–100 GPU-hours** total, entirely for HTR of archival scans (order 10^3–10^4 page images through a handwriting model). No model training is required by the design.
- **CPU:** order **10^4 core-hours**: ~619 khipus × 4 groupings × (decoy panel of ~100 × 100 draws + 9,999 N1 draws) dynamic-programming alignments, embarrassingly parallel.
- **Team:** ~**10–16 team-months** over ~12 calendar months: archival historian/enumerator 4–6; paleographer-transcribers 2–3; ML/statistics engineer 3–4; custodian 0.5–1; coordination/QC 1–2. The budget is dominated by archives, not compute — this is the audited reality of the family (structured khipu data free and verified; archive side unenumerated).

---

## 10. Residual risks the tribunal should hold this design to

(i) Archive enumeration may verify fewer than 100 eligible decoy documents — then the decoy panel rule blocks scoring until the panel is filled or an amendment (dated, pre-data-contact for the affected pairs) registers a smaller panel with correspondingly limited claims; (ii) recording heterogeneity across OKR's source projects (Ascher/Pereyra/Harvard conventions) could correlate with provenance — the S1 sensitivity analysis and per-source reporting are mandatory; (iii) the six Santa Valley khipus' OKR identifiers must resolve cleanly at A0; any ambiguity is filed before Phase B; (iv) U1→U4 coverage means population-level negatives are conditional statements, always so phrased.

**Compute estimate:** GPU: 10–100 GPU-hours (HTR of archival scans only; no model training). CPU: ~10^4 core-hours for order-preserving alignment scoring and 9,999-draw structure-preserving permutation nulls across ≤619 khipus × 4 frozen groupings × ~100-document decoy panel (embarrassingly parallel). Team: 10–16 team-months over ~12 calendar months, dominated by archival enumeration and double-keyed transcription (archival historian 4–6, paleographer-transcribers 2–3, ML/stats engineer 3–4, custodian 0.5–1, coordination/QC 1–2).

**Null result meaning:** (1) No new khipu–document pair passes H-KHI-1: the deliverable is the first multiplicity-honest upper bound on the khipu–archive linkage rate over an enumerated, frozen search universe — quantifying whether the 2018 Santa Valley correspondence is a preservation accident, conditional on OKR's ~37% coverage of documented khipus; publishable per G9 because the frozen search log makes the negative interpretable against the family's principal hazard (look-elsewhere across archives). (2) Linkage replicates but H-KHI-2 attribute prediction fails: color→name and recto/verso→moiety proposals are formally capped as pair-specific descriptions (frozen E2 ceiling) — a first-class constraint on the field's most-cited khipu semantic claims. (3) Santa Valley control unrecovered under pre-frozen rules: per frozen prereg, pipeline defect and family-wide quarantine, plus tribunal-reported evidence on the rule-sensitivity of the 2018 match itself (its first formal stress test). All three outcomes are reported at the same prominence as any positive finding.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (frozen; deposit precedes any scoring data contact). DATASET: OKR v2.1.0, DOI 10.5281/zenodo.18025748 (published 2025-12-22); file open-khipu-repository-2.1.0.zip, 79,808,932 bytes, md5:c741d4d3bbdeba531f547d10f85e2925 (Zenodo API, retrieved 2026-08-11); sha256 computed and deposited as the registered first action at data contact; table-count verification gate: khipu_main=619, primary_cord=633, cord=54,403, cord_cluster=14,847, knot=110,677, ascher_cord_color=56,306 (Run 2 audit values) — any deviation halts the run. License: MIT (in-zip) / Zenodo 'other-open' — both recorded. UNIT TREATMENTS (A19): U1=619 analysis universe; U2=702 census universe; U3=703 frozen resolution procedure (okr-kh-numbers.csv row count + delta enumeration, no threshold impact); damaged/uncertain cords excluded primary, included in sensitivity S1 (both reported); color treatments dual: full Ascher code (primary), colorway clusters (secondary). GROUPING PANEL (A11 multiplicity, closed): G-1 recorded cord_cluster; G-2 color-band runs; G-3 attachment-spacing segmentation; G-4 fixed six-cord groups; Holm denominator = all (khipu, document, grouping) triples logged. MATCHING RULES (frozen pre-search): Locke decimal cord values (code hash deposited); exact integer equality (tolerance = exact); order-preserving DP alignment; attested subtotal mismatch voids the alignment. NULLS: N1 structure-preserving within-document permutation (preserves group sizes, subtotal relationships, within-group rank profile; 9,999 draws; degenerate-null diagnostic: <100 distinct images → N1 declared underpowered, N2 binding, both p reported); N2 decoy panel ≥100 same-genre documents (frozen at Phase A0) × (identity + 99 N1 draws) ≥10,000 draws; empirical p=(1+#{≥obs})/(1+N). CONTROL PANELS: decoy panel list = Phase A0 deposit (composition rule frozen: Peruvian visitas/revisitas/padrones/tasas 1532–1700, ≥20 grouped numeric entries, disjoint from match candidates); positive control = six Santa Valley khipus (OKR IDs resolved from Medrano & Urton 2018 + registry at A0 deposit) vs 1670 San Pedro de Corongo revisita; calibration-only, zero evidential weight for new claims. TOLERANCES: numeric = exact; transcription QC gate = double-keyed numeric fields, ≥99.5% agreement, third-key adjudication; HTR tool name+version pinned at A0. POWER ANALYSIS (frozen protocol, pinned seed 20260811, code hash deposited before scoring): simulation over OKR U1 value distributions × decoy-panel entry-value distributions; registered floors derived: H-KHI-1 pairs with <20 alignable entries not scoreable (tie-heavy small-integer values cannot reach p<0.001 below floor; Santa Valley anchor ≈130 entries sits far above); H-KHI-2 new pair must attest ≥25 individuals with the target attribute (binary-attribute permutation p<0.01 attainable at ≈23/30 correct); 9,999 permutations for both hypotheses (narrowing frozen ≥1,000). H-KHI-2 FREEZES: attribute endpoints (recto/verso→moiety/status; color→name-class); name-class taxonomy frozen by Team P pre-deposit from training pairs + published onomastics, custodian mapping rules frozen, unmappable→'other'; deposit = sha256 of predictions file in tribunal record before unmasking; added stricter control: must beat released-fields-only baseline model; specific-name claims require full H-ONO-1/A15 registration (closed candidate set, transformation budget, dual nulls p<0.005). ROLES: Team L, Team P, scoring agent, custodian all disjoint; custodian = named human paleographer/archivist, no authorship of tested hypotheses (excludes Medrano, Urton, FitzPatrick, Hyland), identity deposited pre-Phase C; custody log is a tribunal deliverable.

# Maya Undeciphered Residue

# EXP-MAY-1 — Maya Undeciphered-Sign Residue: Sealed-Holdout Reading-Proposal Experiment
**Run 3 experiment design · 2026-08-11 · Design agent: E2-Maya designer (this agent authors no adjudication; all success tests reference the frozen prereg + amendments)**

**Binding documents (canonical, in precedence order):** `/home/claude/work/tribunal-record-and-prereg-amendments-v1_1.md` (A1–A19) · `/home/claude/work/run2-preregistration-FROZEN.md` (H-MAY-1 §4, H-ONO-1 §9, global rules G1–G9) · `/home/claude/work/undeciphered-research-plan-v2.md` · `/home/claude/work/run2-audits-methods-patch.md` (data-reality audits + inventory patch) · `/home/claude/work/run2-checkpoint2-matrix.md` (adjudicated status + falsification verdict).

---

## 0. Adjudicated basis and claim cap

- Checkpoint 2 adjudicated status (matrix, Maya row): **E2-conditional**, "weakened in both directions": the audit's claim that MHD record counts are unpublished is FALSE (Glyph Dwellers Report 75 publishes them), while the "10–15% of signs unread" figure conflicts with the sourced ~1/3-uncategorized figure and must be **reported as a range** (run2-checkpoint2-matrix.md, "Maya undeciphered residue — WEAKENED"; source: MHD Reference Materials 5, Glyph Dwellers R75, <http://glyphdwellers.com/pdf/R75.pdf>).
- Frozen prereg precondition (run2-preregistration-FROZEN.md §4, binding caveat): sourced records for (i) total sign inventory, (ii) undeciphered-sign count, (iii) the corpus database used must be deposited **before any H-MAY-1 scoring**. Status: partially discharged by the falsification record (R75 counts: 69,670 non-codical glyph blocks, 50,772 coded graphemes, 2,235 datable texts, 15,332 codical glyph blocks, 1,210-grapheme inventory, ~1/3 of graphemes uncategorized as to logographic vs syllabic function). This design **completes** the discharge via appendix items PA-1/PA-2 (pinned MHD export + deterministically derived counts), deposited to the tribunal record before generator contact (A17).
- **Claim cap (A18 band format, licensed by the tribunal record — not by this design):**
  **Maya residue: E2 / L3–L4 function-class claims and L5/L6 single-sign value proposals that pass every H-MAY-1 prong including sealed corroboration · E1 / method, calibration, and any proposal lacking sealed-prediction confirmation · E0 / signs with <10 attested occurrences; L7 (translation of connected text) prohibited program-wide (G2).**
  No E3 is licensed: unlike Oracle Bone (institutional adjudicator, tribunal record I.2), Maya has no adjudicated external-confirmation instrument in this program. A prospective route (readings confirmed by texts published after this design's freeze) is *logged* for future adjudication but licenses nothing now.

## 1. Hypotheses executed (frozen IDs)

- **H-MAY-1** (run2-preregistration-FROZEN.md §4) as amended by **A8** (sealed holdout: corroborating occurrences/imagery pre-designated and hashed before the hypothesis generator runs; retrieval and prompts sealed; rediscovery of unsealed corroboration scores nothing), **A17** (appendix complete before data contact), **A18** (claim-band reporting), **A19** (unit mapping frozen; dual reporting).
- **H-ONO-1** (§9) as amended by **A15** (corollary type + full candidate search universe frozen before matching) — invoked **only** for proposals taking prediction route (iii) (name/toponym).
- Harness interlock: **H-PHA-1 / A16** — the Phaistos negative control runs concurrently with this experiment using the identical reporting/confidence policy; a control failure quarantines concurrent Maya results (prereg §10).
- This design registers one internal **calibration gate MAY-P1** (§4.6). It is an E1 method gate implementing G2/G6 inside H-MAY-1's registered controls ("proposal generation and context-scoring by disjoint agents"; decoy protocol). It narrows — it can only cancel or cap, never widen, any registered threshold (permitted per prereg Freeze block: "appendices may narrow but never widen").

## 2. Data acquisition plan (grounded in the audits, not papers' claims)

**G8 declaration.** Basis (iii) transliterations/sign-code sequences + (iv) structured relational DB (MHD Texts_Classic + Texts_Codical tables + grapheme Catalog). Imagery is used **only** as sealed corroborating evidence (route ii). Results do not transfer to a photographic/facsimile basis without a registered bridging test (G8). Paleographic claims are out of scope.

**2.1 Audited reality (what actually exists).**
- **MHD (Maya Hieroglyphic Database, Macri/Looper):** audit score **3/5**. Web application is a React SPA (JS-only; content not fetchable); tutorials at mlooper.yourweb.csuchico.edu/MHD/ document a search UI **with CSV export of query results**; datasets are deposited at **tDAR project 514652 (DOI 10.48512/XCV8514652) listing 3 downloadable datasets**; account requirement could not be confirmed; license not stated on public pages — tDAR deposit terms govern the deposited datasets ("Maya Hieroglyphic Database (MHD, Macri/Looper)", run2-audits-methods-patch.md audit table, <https://www.mayadatabase.org/>). Audit note: third-party front end mayacorpus.org (Gonzalez 2025) serves MHD data claiming 200,000+ glyph blocks and credits the MHD team — "indicates the underlying data is obtainable, but no documented bulk-download/API on either site"; "do not cite a total without querying the DB."
- **Published MHD counts (supersede the audit's pessimism, per falsification verdict):** 69,670 non-codical glyph blocks / 50,772 coded graphemes / 2,235 datable texts / 15,332 codical glyph blocks / 1,210-grapheme inventory; ~1/3 of graphemes uncategorized as to logographic vs syllabic function (Glyph Dwellers R75, <http://glyphdwellers.com/pdf/R75.pdf>; run2-checkpoint2-matrix.md Maya verdict).
- **Idiap/MAAYA Maya Codex glyph dataset:** audit score **2/5**; Zenodo record 4646648 is **restricted** (verified via Zenodo API), 174 reconstructed vectorial glyph images from 72 blocks of the Dresden/Madrid/Paris codices + Thompson-catalog co-occurrence model; no license field ("Maya Codex glyph image dataset (Idiap/MAAYA)", run2-audits-methods-patch.md, <https://www.idiap.ch/en/dataset/maya-codex>). Audit note: "a shape-analysis benchmark, not a corpus." **Design ruling: NOT load-bearing.** Access will be requested for an optional L1 glyph-normalization sanity check only; no success criterion depends on it.
- **Cross-check resources:** Text Database and Dictionary of Classic Mayan, Univ. Bonn (classicmayan.org) — ~8,000 text carriers catalogued, open-access sign catalog; Maya Codices Database (mayacodices.org) (inventory patch entry "Maya script — undeciphered sign residue", run2-audits-methods-patch.md).
- **Corpus-scale disagreements (reported as ranges, never resolved):** ~8,000 documented texts / ~400,000 glyph blocks / ~2.4M estimated sign tokens (Bonn ClassicMayan portal) vs ~5,000 surviving text carriers (SLUB Dresden); sign inventory ~650 distinct characters incl. ~200 syllabograms (SLUB) vs 1,210 MHD graphemes (R75) vs 391 signs = 150 syllabograms + 241 logograms in the Unicode preliminary list (Vail 2023, L2/23020) (all per inventory patch, run2-audits-methods-patch.md; EPFL/Idiap residue statement "10 to 15% of the symbols are not known", <https://actu.epfl.ch/news/revealing-the-mysteries-of-the-maya-script>).

**2.2 Concrete access path (ordered; executed by the Custodian agent, §4.2, before any generator contact).**
1. **Primary — tDAR deposit:** download the 3 datasets of tDAR project 514652 (DOI 10.48512/XCV8514652) under tDAR terms; create account if required (audit could not confirm). Success condition: per-occurrence records (glyph block → grapheme codes, text ID, position) for Texts_Classic and Texts_Codical plus the grapheme Catalog.
2. **Fallback A — documented CSV export:** scripted per-grapheme queries through the MHD search UI's CSV export (the audited, documented path), enumerated over the full 1,210-grapheme catalog, throttled, with **prior written permission from the MHD directorship (M. Looper, CSU Chico)**. All queries logged (G5).
3. **Fallback B — negotiated bulk transfer:** written data agreement with the MHD team (precedent: mayacorpus.org redistribution credits "the MHD team", audit note). Terms deposited in the tribunal record.
4. **Fallback C (degraded scope):** codical corpus only — MHD Texts_Codical (15,332 blocks) via A/B plus Maya Codices Database cross-check. Triggering C is a registered **descope event** reported in the checkpoint, and power recomputed (PA-8) before any scoring.
**Abort rule:** if by **T0+8 weeks** no path yields per-occurrence records covering ≥80% of candidate-panel occurrences (panel per §3.3), the experiment reports a **data-access null** — "MHD bulk access not obtainable under documented or negotiated paths" — as a first-class deliverable (G9) and stops. No substitute corpus may be swapped in post hoc.
**Licensing rule:** no MHD-derived record is redistributed; deliverables publish derived statistics, hashes, and code only, unless tDAR/MHD terms permit more (audit: license not stated — treat as all-rights-reserved by default, as the audit does for unlicensed resources).

## 3. Unit mapping (A19 — frozen treatments)

Per A19 and tribunal Part I.3–4, every contested unit gets an explicit frozen mapping; results are reported under **all** treatments where they disagree.

**3.1 Sign-inventory catalog (the pinned inventory).** Primary unit = **MHD grapheme code** (Macri–Looper catalog system as implemented in the pinned MHD export; catalog basis: Macri & Looper 2003 *New Catalog of Maya Hieroglyphs* vol. 1 and Macri & Vail vol. 2, as recorded in the inventory patch and Vail 2023 L2/23020). Two frozen concordances, built by the Custodian and hashed (PA-3): (a) MHD code ↔ **Thompson T-number** (Thompson 1962 catalog) using MHD's own T-number cross-reference fields; (b) MHD code ↔ Bonn TWKM sign catalog ID where the Bonn open-access catalog provides one. Signs lacking a concordance entry are reported under MHD codes only, flagged. The Thompson concordance exists because decoy pools, prior literature, and the Idiap co-occurrence model are T-number-keyed; **no scoring ever mixes unit systems inside one statistic.**

**3.2 Residue definition — dual treatment (the 10–15% vs ~1/3 conflict).**
- **U1 (broad, MHD-derived):** residue = MHD graphemes with **no accepted logographic or syllabic value** in the pinned Catalog export (the operationalization of R75's "~1/3 uncategorized of 1,210"; expected order ~400 graphemes — the exact count is computed deterministically from the pinned export and deposited as PA-2, never asserted in advance).
- **U2 (narrow, field-consensus):** residue = signs unread under the ~650-character inventory framing (SLUB/EPFL 10–15% ≈ 65–98 signs; inventory patch + EPFL URL above), operationalized as U1 ∩ {graphemes mapped to a Thompson/Bonn catalog entry} — i.e., established, catalogued signs without values, excluding rare uncatalogued graphs.
- All headline tallies (panel size, survivors, family-level null) are reported under **both** U1 and U2. Divergent verdicts are reported as divergent (prereg H-IND-2 precedent).

**3.3 Candidate panel rule (deterministic, frozen).** Panel = residue graphemes (per treatment) with **≥10 attested occurrences** in the pinned export (the prereg E0-bar: "signs with <10 attested occurrences are E0-barred from reading proposals — hapax and near-hapax readings are unfalsifiable"), excluding graphemes whose occurrences are >80% within a single repeated formula (a frozen anti-pseudo-replication rule; formulaic repetition is the Maya analog of the Meroitic "formulaic monoculture" weakness, run2-checkpoint2-matrix.md). The hapax-enrichment risk is registered: R75's 1,210 graphemes over 50,772 coded occurrences imply a long tail, so "the H-MAY-1-scoreable subset may indeed be small" (falsification verdict) — the panel may lawfully be small, and its size is itself a reported finding. Panel derivation script + output hashed (PA-4). Cap: at most **K = 25** proposals scored in this run (multiplicity, §7).

## 4. Method (implementable specification)

**4.1 Role separation (G2; prereg control "proposal generation and context-scoring by disjoint agents").** Five disjoint teams, no shared personnel/agents, no shared writable state: **Custodian C** (acquisition, panel, sealing; never generates or scores) · **Generator G** (proposals only) · **Decoy team D** (decoy sets; deterministic) · **Scorer S** (frozen scoring only; blind to which candidate is G's) · **Auditor X** (leakage/log audit; built no module). The adjudication rules themselves come from the frozen prereg + amendments; nobody in this design authors them.

**4.2 Sealing architecture (A8 — auditable, leakage-detectable).**
1. C ingests the pinned export into an occurrence DB: one row per glyph-block occurrence of a panel sign — text ID, site/provenance, object type, date, block position, co-occurring grapheme codes, accepted readings of co-occurring known signs, iconographic annotation fields where MHD provides them.
2. **Pre-designation:** for each panel sign, C partitions occurrences into VISIBLE (~70%) and **SEALED (~30%, min 3 occurrences)**, stratified by text genre and site, using a pinned RNG seed committed as SHA-256(seed‖salt) (PA-5). All imagery/iconographic annotation fields for that sign are sealed in their entirety. C also **designates, per sign, the admissible G3 prediction route** from H-MAY-1's registered list — (i) syllabic substitution/spelling alternation attested elsewhere, (ii) co-occurrence with an independently recognizable iconographic referent, (iii) independently attested name/toponym (→ H-ONO-1/A15) — choosing the route(s) for which sealed evidence of that type exists. The designation table, sealed-row ID list, and their SHA-256 hashes are deposited in the tribunal record **before G runs** (A8, A17).
3. **Sealed execution environment:** G runs in an offline container (no network) whose corpus mount physically excludes sealed rows and all imagery; container image hash recorded; every prompt and output appended to a hash-chained log (per-day Merkle root deposited). Sealing is thus auditable at three layers: mount manifest (what G *could* read), prompt/output logs (what G *did* read/say), and the pre-deposited hashes (what was sealed and when).
4. **Post-run leakage audit (X):** scan G's full logs for sealed occurrence IDs, sealed text IDs, or verbatim sealed content. Any hit voids the affected proposal(s); per A8, "rediscovery of unsealed corroborating evidence scores nothing" — corroboration credit attaches **only** to pre-designated sealed evidence.

**4.3 Generator (G).** For each panel sign, G may use, over VISIBLE data only: distributional embeddings of glyph-block contexts; substitution-slot analysis against known spelling frames; syllabary-grid gap analysis (which CV values lack a known sign); Ch'olan-Tzeltalan lexical resources (pinned dictionary, PA-6); LLM-assisted proposal drafting (logged; §6 blinded mode governs). Output per sign: **at most one** proposal = {value class: syllabic CV or logographic lexeme; proposed value; machine-checkable prediction statement on the designated route — a predicate over sealed records}. Proposals + predictions are deposited and hashed **before unsealing**.

**4.4 Decoys (D).** Frozen decoy pool (PA-6): union of (a) all attested syllabic values in the pinned syllabary grid, (b) all accepted logographic values in the pinned MHD Catalog, (c) lexemes from the pinned Ch'olan-Tzeltalan etymological dictionary (Kaufman with Justeson 2003, *A Preliminary Mayan Etymological Dictionary*, FAMSI report, famsi.org — exact file pinned + hashed at acquisition). **4,999 decoys per proposal**, sampled deterministically (pinned seed) matched on value class, phonotactic plausibility (CV structure for syllabic; word-class + semantic-domain stratum for logographic), and frequency tercile — satisfying the prereg's "≥99 decoy values … under identical phonological and orthographic constraints" with headroom so the Holm-corrected empirical-p floor is attainable (min empirical p = 1/5,000 = 2×10⁻⁴ < 0.01/K for K ≤ 25; §7).

**4.5 Scorer (S) — frozen context-coherence score.** A small masked glyph-block language model (transformer, ≤50M params) trained **only** on visible, non-panel MHD sequences (grapheme-code tokens + accepted-value side channel), frozen before any proposal exists (weights hashed, PA-7). Score of a candidate value v for sign σ = mean per-occurrence log-likelihood of σ's contexts (ALL occurrences, visible + sealed, per the prereg metric "frozen context-coherence score over all occurrences") under substitution of v, combined with a frozen slot-grammar compatibility term (Maya logosyllabic orthographic rules: CV-CV synharmony defaults, affixation positions) — combination weights fixed in PA-7 before data contact. **Incoherence rule (frozen):** an occurrence is "incoherent" if its score falls below the 1st percentile of the known-sign occurrence-score distribution (computed once on the calibration panel, PA-7); per the prereg, **any incoherent context rejects the proposal**. S evaluates the deposited proposal against its 4,999 decoys blind (candidate order shuffled; S never told which is G's).

**4.6 Calibration gate MAY-P1 (E1; runs before any residue scoring).** 20 **known-value** signs, stratified by frequency tercile and value class, are masked and run through the entire pipeline (sealing, generation, 4,999 decoys, scoring) in **glyph-blinded mode** (§6). Frozen gate: G+S recover the true value at **rank 1 in ≥12/20 (60%)** and within top-10 in **≥16/20 (80%)**. Failure → H-MAY-1 execution is cancelled for this run; registered E1 finding: "the pipeline cannot recover known Maya sign values at Maya information conditions"; no residue proposal is scored (prevents uninterpretable nulls). The gate can only cancel; it cannot relax any H-MAY-1 threshold.

**4.7 Order of operations (binding).** (1) Appendix deposited (A17) → (2) Custodian acquisition, pinning, hashing, panel, sealing, designation deposit → (3) MAY-P1 gate → (4) G runs sealed; proposals deposited+hashed → (5) D builds decoy sets → (6) S unseals, scores, checks predictions → (7) X audits logs + memorization probes → (8) Holm correction, family verdict → (9) expert + tribunal review of survivors (§8) → (10) A18-band reporting under U1 and U2.

## 5. Claim-ladder levels attempted and E-class licensing

| Ladder level | Attempted? | Product | Licensed class (per tribunal record) |
|---|---|---|---|
| L1 glyph normalization | Not as a claim — MHD's coding is adopted as given; optional Idiap sanity check | none | — |
| L2 segmentation | Not attempted (glyph-block segmentation is field-established in MHD) | none | — |
| L3 structural classes | Yes — function-class (syllabic vs logographic) assignment for residue signs | distributional class labels | **E2** if decoy-tested; E1 otherwise |
| L4 grammatical/semantic roles | Yes, narrowly — slot-grammar role of residue signs | slot-role labels | **E2** ceiling, same test |
| L5 phonetic hypotheses | Yes — syllabic CV value proposals | H-MAY-1 proposals | **E2** only with all prongs incl. sealed corroboration; else E1 |
| L6 lexical correspondences | Yes — logographic lexeme proposals | H-MAY-1 proposals | **E2** same conditions; route (iii) additionally requires full H-ONO-1 pass |
| L7 translation | **Prohibited** (G2, program-wide) | — | — |

## 6. Contamination controls (G6)

Maya epigraphy is saturated in model training data; the residue signs have no accepted values (no answer key can leak), but **published proposals** and **sealed evidence** can.
1. **Published-proposal registry (frozen before G runs):** a literature sweep (logged, G5) records every published reading proposal for each panel sign (Glyph Dwellers series, standard epigraphic literature). After scoring, S/X match G's outputs against the registry: matches are labeled **"recovered (prior: cited)"**, non-matches **"novel"**. Both are scored identically under H-MAY-1, but a recovered proposal's report must cite the prior claimant and may claim only *independent computational corroboration*, never discovery. The registry is compiled by X, not G; G never sees it.
2. **Glyph-blinded mode (load-bearing):** for MAY-P1 and the primary residue run, all grapheme codes are bijectively remapped to opaque identifiers and accepted values supplied only via an explicit value table — severing the model's memorized literature from the corpus representation (the Maya analog of shadow glyph randomization, plan v2 §3/G6). An unblinded replicate run is reported alongside; **only blinded-mode results license E2**; divergence between modes is itself reported as a contamination measurement.
3. **Weight-level leakage probe:** before generation, X probes the base model with cloze prompts over sealed-occurrence content; sealed items reproducible above a frozen chance band are flagged, and any prediction confirmed **only** on flagged items is downgraded to E1 and reported as possibly contaminated.
4. **Prospective subset:** panel-sign occurrences from texts first published after 2026-01 (base-model cutoff) form a logged prospective stratum; performance deficits on it are reported as leakage evidence, never passed under a grace band (A6 logic, adopted here as reporting duty, not as a threshold change).
5. **A16 interlock:** the Phaistos control runs concurrently under the identical reporting/confidence policy; module-family failure quarantines Maya results (prereg §10).

## 7. Multiplicity, logging, and thresholds (G5 + frozen prereg)

- Success/disconfirmation are **exactly** H-MAY-1's: proposal ranks **first** against the decoy set at empirical p < 0.01, **Holm–Bonferroni corrected across all residue proposals scored in the run** (K ≤ 25; with 4,999 decoys, rank-1 empirical p = 2×10⁻⁴, below every Holm threshold down to 0.01/25 = 4×10⁻⁴); **AND** zero incoherent contexts across all occurrences; **AND** the pre-designated sealed prediction confirms (binary; route (iii) requires the full H-ONO-1 protocol: both nulls at p < 0.005, corollary checked, candidate universe frozen per A15).
- **Disconfirmation (frozen):** decoy-ranking failure, any incoherent context, or prediction failure → proposal rejected and logged. **Family-level null:** if ≥10 proposals are scored and none survives, the registered conclusion is "the pipeline cannot advance Maya residue readings at current information conditions" (verbatim, prereg §4).
- Every proposal generated, scored, or abandoned is logged whether or not reported (G5); search logs (queries, decoy draws, restarts, seeds) are auditable; selective reporting is a protocol violation.

## 8. Human-expert loop and tribunal (G7; A7-analog)

A7 binds OBS specifically ("real experts for headline claims"). For Maya, no amendment mandates it — this design **adopts the analogous requirement as binding** (a narrowing, hence permitted): expert-proxy adjudication is allowed in development only; any proposal surviving all H-MAY-1 prongs must, before headline E2 reporting, pass review by **≥2 named human Maya epigraphers** under a rubric frozen in the appendix (PA-9: context-fit, orthographic legality, iconographic plausibility; reviewers blind to which candidate is the pipeline's, decoy-interleaved). Per G7, internal agreement is never corroboration: every headline claim additionally goes to the cross-model tribunal (blind reports first, comparison second). Expert or tribunal rejection caps the proposal at E1 and is reported, not suppressed.

## 9. Compute and team estimate

- **Compute (order of magnitude: ~10³ GPU-hours).** Scorer MLM training over ≤85k glyph blocks: 50–100 GPU-h. MAY-P1 + generation (LLM-assisted, 45 signs total incl. calibration): 200–800 GPU-h inference. Decoy scoring (≤25 proposals × 5,000 candidates × ~10–50 occurrences on a ≤50M-param scorer): 50–200 GPU-h. Replicates (blinded/unblinded, U1/U2): ×~1.5. **Total ≈ 500–1,700 GPU-hours** — deliberately small; the binding costs are data access and sealing discipline, not FLOPs.
- **Team: ~10–14 team-months** — data acquisition/negotiation + custodian engineering 3–4; pipeline (G/D/S) 4–5; audit + tribunal + reporting 2–3; epigrapher consultation 1–2. Calendar: 6–9 months, gated by the T0+8-week access milestone.

## 10. What a null result means (G9)

Maya is the program's best-conditioned shape-E residue case after Oracle Bone: known language family and script structure, a 50,772-occurrence structured corpus, and a published grapheme catalog — and unlike OBS, no institutional adjudicator or answer key. A rigorous family-level null therefore says: **even under the most favorable non-OBS information conditions in the field — solved system, known language, structured data — sealed-holdout computational methods cannot advance single-sign decipherment.** That bounds expectations for every worse-conditioned system in the inventory, converts the "AI will read the residue" claim into a measured negative at registered power (PA-8), and delivers three standalone artifacts regardless of outcome: the MAY-P1 known-sign recovery benchmark (the first decoy-calibrated evaluation of Maya value recovery), the A8 sealed-holdout protocol as a reusable instrument for Mesoamerican epigraphy, and the dual-unit (U1/U2) residue accounting that resolves the 10–15%-vs-~1/3 discrepancy operationally. Null results are deliverables at equal prominence (G9).

## 11. Closed degrees of freedom (reviewer checklist)

Access path + abort/descope rules (§2.2); unit system, concordances, dual residue treatments (§3, A19); panel rule incl. ≥10-occurrence bar and formula filter (§3.3); sealing fractions, seeds committed by hash, prediction-route designation before generation (§4.2, A8); one proposal per sign; decoy pool, count (4,999), matching strata, seeds (§4.4); scorer architecture, training data, weights hash, incoherence percentile, combination weights (§4.5); calibration gate numbers (12/20, 16/20) and its cancel-only authority (§4.6); K = 25 cap and Holm denominator = all proposals scored (§7); blinded mode as the E2-licensing mode (§6); registry-based novel/recovered labeling (§6); expert rubric and tribunal routing (§8); reporting bands fixed by A18. Every threshold that adjudicates success lives in the frozen prereg + amendments, not in this design; everything else is pinned above or in the A17 appendix. Remaining data-dependent quantities (exact panel n, exact decoy pools) are produced by pinned, hashed, deterministic scripts at custodian time, before any hypothesis generation.

**Compute estimate:** Order 10^3 GPU-hours total (~500–1,700): scorer masked-LM training 50–100 GPU-h; LLM-assisted generation + calibration ~200–800 GPU-h; decoy scoring (≤25 proposals × 5,000 candidates on a ≤50M-param scorer) 50–200 GPU-h; ×~1.5 for blinded/unblinded and U1/U2 replicates. Team: ~10–14 team-months over 6–9 calendar months, gated by the T0+8-week data-access milestone; dominant cost is data access and sealing discipline, not compute.

**Null result meaning:** A family-level null (≥10 proposals scored, none surviving) is the registered conclusion "the pipeline cannot advance Maya residue readings at current information conditions" (H-MAY-1, verbatim). Scientifically it bounds the field's best non-OBS case: Maya offers a solved script structure, known language family, and a 50,772-occurrence structured corpus — the most favorable residue conditions without an institutional adjudicator — so failure here at registered power caps expectations for every worse-conditioned shape-E/B/C system in the inventory. It is publishable per G9 (null results are first-class deliverables) and ships three standalone artifacts regardless: the first decoy-calibrated known-sign recovery benchmark for Maya (MAY-P1), a reusable A8 sealed-holdout protocol for Mesoamerican epigraphy, and an operational dual-unit resolution of the 10–15%-vs-~1/3 residue discrepancy. A MAY-P1 gate failure is a distinct, also-publishable E1 null: known Maya sign values are not recoverable by these methods at these information conditions, which quarantines residue claims across the literature.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (deposited to tribunal record before any experiment data contact; custodian pinning/hashing precedes and gates generator contact). PA-1 Dataset pinning: MHD export identity = tDAR project 514652 (DOI 10.48512/XCV8514652) dataset files as retrieved (or Fallback A/B export), SHA-256 per file computed at acquisition and deposited; Bonn TWKM sign-catalog snapshot (classicmayan.org) hashed; Kaufman–Justeson 2003 FAMSI etymological dictionary file hashed; base-model ID + training cutoff (2026-01) recorded. PA-2 Discharge of prereg precondition: deterministically derived counts from the pinned export — total graphemes, U1 residue count, U2 residue count, per-sign occurrence table — deposited with derivation-script hash (completes the H-MAY-1 binding caveat items i–iii; prior basis: Glyph Dwellers R75 figures 1,210 / 50,772 / 69,670 / 15,332 / ~1/3 uncategorized). PA-3 Unit concordances (A19): MHD↔Thompson T-number and MHD↔TWKM tables, hashed; unmapped signs flagged. PA-4 Candidate panel: rule = residue ∧ ≥10 occurrences ∧ ≤80% single-formula concentration; K_max = 25; panel list generated by pinned script, hashed. PA-5 Sealing commitments (A8): per-sign 30% sealed fraction (min 3 occurrences), stratified by genre and site; RNG seed committed as SHA-256(seed‖salt); sealed-row ID list hash; per-sign prediction-route designation table (routes i/ii/iii) hash; all deposited before generator execution. PA-6 Control panels: decoy pool = attested syllabic grid values ∪ accepted MHD logographic values ∪ pinned dictionary lexemes; 4,999 decoys per proposal; matching strata = value class, CV phonotactics / word-class + semantic domain, frequency tercile; decoy-draw seeds pinned. Calibration panel = 20 known-value signs stratified by frequency tercile × value class, list hashed. Expert rubric (PA-9) frozen: context-fit / orthographic legality / iconographic plausibility, blind decoy-interleaved presentation, ≥2 named Maya epigraphers. PA-7 Frozen scorer + tolerances: scorer = masked glyph-block LM ≤50M params trained only on visible non-panel sequences, weights hashed before proposals exist; score = mean per-occurrence log-likelihood + slot-grammar term with fixed combination weights (deposited numeric values); incoherence tolerance = below 1st percentile of known-sign occurrence-score distribution (computed once on calibration panel, then frozen); MAY-P1 gate = ≥12/20 rank-1 and ≥16/20 top-10, cancel-only authority; blinded-mode bijective code remapping seed pinned; memorization-probe chance band frozen. PA-8 Power analysis (concrete): with 4,999 decoys, rank-1 empirical p = 2×10⁻⁴ < Holm floor 0.01/25 = 4×10⁻⁴, so every registered threshold is attainable at K ≤ 25; per-proposal detection power estimated by the MAY-P1 recovery rate under the identical decoy protocol (gate minimum 0.60 top-1), giving P(family null | ≥10 correct proposals) ≤ 0.4¹⁰ ≈ 1×10⁻⁴ — a family null is therefore evidential, not vacuous; U2-treatment panel may be small (hapax-enrichment risk registered); if either treatment yields <10 scoreable signs, the family-level null clause is reported as not triggerable under that treatment (stated in advance, not decided post hoc). PA-10 Environment: generation container image hash, corpus-mount manifest hash, hash-chained prompt/output log with daily Merkle roots, published-proposal registry hash (compiled by auditor, hidden from generator).

# Meroitic Lexical/Grammatical Expansion

# Run 3 Experiment Design — Meroitic Lexical/Grammatical Expansion (Family MER)

**Design ID:** R3-MER-v1 · **Date:** 2026-08-11 · **Designer:** Run 3 experiment-design agent (this document designs; it does not adjudicate — all success tests are executed against `run2-preregistration-FROZEN.md` §5 (H-MER-1, H-MER-2), §9 (H-ONO-1), and the binding amendment appendix `tribunal-record-and-prereg-amendments-v1_1.md`, by agents disjoint from hypothesis generation, with headline claims routed to the cross-model tribunal per G7).

**Adjudicated gate (binding):** "Meroitic: E2; E3 contingent on custodian-sealed reserve (A9)" (tribunal record §I.2). Checkpoint-2 falsification verdict: "E2, narrow anchor route (H-ONO-1); reserved-partition claim struck" (`run2-checkpoint2-matrix.md`, Meroitic row and WEAKENED entry). This design licenses nothing above that band.

---

## 0. Claim-band declaration (A18 format)

**Meroitic: E2 / L3 structural + L4 morph-function + L6 lexical claims, anchor route only (H-MER-1 + H-ONO-1) · E1 aggregate lexicon-induction method claims (H-MER-2) · no claim on language-family identity (Rilly NES vs Rowan Afroasiatic both carried live per matrix correction of the "minority" framing, [Meroitic language, Wikipedia](https://en.wikipedia.org/wiki/Meroitic_language)) · L5 not attempted (Griffith sign values assumed, not re-litigated) · L7 prohibited program-wide (G2) · paleography out of scope (no image DB — frozen prereg §5 data-basis note) · E3: no claim this run; prospective pathway only via the custodian protocol of §6.**

Problem shape: C (readable script + opaque language, plan v2 §1). The script is fully read (Griffith 1907–1911; [Rilly, "Meroitic," UCLA Encyclopedia of Egyptology](https://escholarship.org/content/qt3128r3sw/qt3128r3sw_noSplash_a34fb083e49c75f88724b4054bd16aaf.pdf)); the bottleneck is the language: fewer than ~100 words securely translatable (Rilly, UEE, above).

---

## 1. Data acquisition plan (grounded in the Run 2 audit, not papers' claims)

### 1.1 What actually exists (audit findings, binding)

1. **Otten & Anastasopoulos 2025 corpus — audit score 3/5.** Verified by clone 2026-08-11: plain-text **ASCII custom transcription** (not Unicode Meroitic), **no REM identifiers on most units**, **no license file** (all-rights-reserved by default; underlying transcriptions from copyrighted works — Lobban 2021, Rilly 2007, Millet 1968, Hofmann 1998, Hägg 2000), last commit 2024-05-14, and `mero-corpus.txt` (18,090 lines) is the **synthetic name-swap augmented version** that "must not be confused with attested text" (`run2-audits-methods-patch.md`, Otten row and note; paper: [Otten & Anastasopoulos 2025, "Towards Ancient Meroitic Decipherment," ACL ALP](https://aclanthology.org/2025.alp-1.11.pdf); repo: [Joshua-Otten/Meroitic-Corpus](https://github.com/Joshua-Otten/Meroitic-Corpus)). Paper stats: 871 attested texts/phrases; augmented corpus 1,868 unique word forms, 17,257 sentences/phrases, 782,761 words; 193 glossed words; 897 phrases.
2. **REM — audit score 1/5.** All three tomes are **page scans on Persée** (Tome I REM 0001–0387, II 0401–0851, III 1001–1278); on-site viewing works, **scripted PDF download blocked (HTTP 403 observed by the audit client)**; NOT transliteration data, NOT a structured DB; "no Meroitic OCR exists" (`run2-audits-methods-patch.md`; [REM on Persée](https://www.persee.fr/issue/rem_0000-0000_2000_num_1_1)).
3. **The newest corpus publication is print-only.** Otten & Anastasopoulos note Hallof 2024 "is not currently available in any digital format" (audit note); Hallof's Qasr Ibrim editions exist as print volumes ([Hallof, *The Meroitic Inscriptions from Qasr Ibrim*, SRaT 9.3, Röll Verlag](https://roell-verlag.de/Hallof-Meroitic-Inscriptions-SRaT-9-3/en)).
4. **The ~900-text unpublished reserve is not an instrument the program controls** (Qasr Ibrim, Musawwarat; Rilly UEE): "no access, deposit, or blind-scoring mechanism exists … an unenforceable partition is a pathway, not held-out evidence" (checkpoint-2 falsification, Meroitic). A9 therefore governs: aspirational until a custodian seals texts (§6).

### 1.2 Acquisition actions (all frozen; no discretionary additions after data contact)

- **D1. Pin the corpus.** `github.com/Joshua-Otten/Meroitic-Corpus` at commit `1a6eb1097d89309944908400e8d8b7905fa2bea1` (2024-05-14). File-level SHA-256 hashes are frozen in the A17 appendix (§7). The designer's contact was hash/line-count only; no content was read (declared per A17 discipline).
- **D2. License clearance.** No license exists; before any redistribution or derived-data publication, written permission is sought from the corpus authors (George Mason University). Failure to obtain it restricts outputs to result tables without redistributed text. This is a publication constraint, not a scoring constraint; it is logged either way.
- **D3. REM-alignment concordance (the design's answer to the no-REM-identifier problem).** Build `mer-concordance-v1.csv`: one row per attested unit in the five attested Data files, with fields {file, line-span, source work + page (Millet 1968 / Rilly 2007 / Lobban 2021 / named narrative), REM number where the source work cites one, else NO-REM flag, genre tag (funerary-formula / royal / graffito / ostracon / vocab-item / other), duplication-group ID}. REM numbers are recovered from the source works' own citations and verified against the Persée REM scans by **manual page lookup** (the audited access mode — scripted download is blocked). Two agents double-key independently; disagreements go to the named human consultant (§9). The concordance is hashed and deposited before any Track-2 scoring. Purposes: (i) **deduplication** — the same REM text entering via two source works is one evidential unit (duplication-group ID; analogous to the Indus object-family dedup condition, tribunal §I.2); (ii) **genre stratification** for the formulaic-monoculture control (§4); (iii) **firewall enforcement** — every unit is positively identified as published-attested, so nothing from the unpublished reserve can silently enter (A9).
- **D4. Anchor-side resources (for H-ONO-1).** Candidate onomastica: Egyptian royal/divine names in Meroitic spelling and Meroitic names in Egyptian/Greek documents — the anchor classes named by the dossier ([Rilly, UEE](https://escholarship.org/content/qt3128r3sw/qt3128r3sw_noSplash_a34fb083e49c75f88724b4054bd16aaf.pdf)). Candidate digital sources (Trismegistos, trismegistos.org; Lexicon of Greek Personal Names) are **named here but NOT relied on**: per the tribunal's pseudo-precision rule (§I.3.5 precedent — unverified resources "must be audited before any design relies on it"), a data-reality audit of each onomasticon (existence, access mode, export, license, count) is a **precondition**; its result is deposited as appendix item P-6 before any H-ONO-1 registration closes. NES comparative data (Nubian/Nara/Taman/Nyima) must be "gathered independently of the Meroitic claim … deposited in the ledger before scoring" (frozen H-MER-1 threshold clause) — Old Nubian sources are audited and deposited the same way.
- **D5. Absolute firewall (A9).** `mero-corpus.txt` (18,090 lines, augmented) is quarantined in a separate directory with a tainted-path naming convention (`SYNTHETIC-AUGMENTED/`). It may be touched only under the narrow Track-1 representation-training condition of §3.1, always labeled synthetic. **Halt rule (registered):** any agent output describing the augmented corpus, or any statistic computed on it, as ancient/attested evidence halts the run (A9 verbatim), and the incident is a first-class protocol-violation report.

**G8 declaration:** basis (iii) transliterations/sign-code sequences (ASCII custom transcription normalized to Millet's paradigm, per the audit) + print REM scans as verification-only reference. No result transfers to bases (i)/(ii) without a registered bridging test; none is registered here.

---

## 2. Unit-mapping freeze (A19)

Registry entry (tribunal §I.3.4): "Meroitic 871 attested texts vs 782,761-word augmented corpus." Frozen treatments — results reported under all treatments where they disagree:

- **U1 Text universe.** Evidential universe = the 871 attested units (as enumerated by D3), deduplicated by REM concordance group. Coverage is reported against BOTH denominators: REM ~1,300 published and >2,000 known inscriptions (Rilly, UEE). The 782,761-word figure is never a corpus-size claim; it appears only as "synthetic augmentation volume."
- **U2 Gloss universe (new mismatch, registered here).** Otten's 193 glossed words vs Rilly's "fewer than ~100 words securely translatable" (Rilly, UEE) do not describe the same set. Frozen dual treatment: **Tier B** = all 193 Otten glosses (matches the published ≤20% baseline's own universe — required for a like-for-like H-MER-2 comparison); **Tier A** = the subset independently marked secure against Rilly's UEE list, constructed by the human consultant before scoring (membership list hashed; expected n < 100 per Rilly). H-MER-2 primary endpoint on Tier B; Tier A reported alongside. Divergent verdicts are reported as divergence, never averaged.
- **U3 Transcription scheme.** ASCII-custom → standard transliteration normalization table (Millet-paradigm base, per the audit; Rilly-convention variants for the four syllabics *ne, se, te, to* and the *e*-sign flagged) frozen as appendix item P-2. Where Millet vs Rilly conventions disagree, both normalizations are run (dual treatment).
- **U4 Sign inventory.** 23-sign alphasyllabary in two graphic forms (Rilly, UEE) — uncontested; single treatment, recorded for completeness.

---

## 3. Method (implementable specification)

Three tracks. Generation and scoring are always disjoint agents (G2/HARKing guard); every scored test is logged whether or not headline (G5), with Holm–Bonferroni within each claim family.

### 3.1 Track 1 — H-MER-2, aggregate lexicon-induction method claim (E1)

Baseline reproduction + registered improvement attempt against the published floor: VecMap-style alignment achieved ≤20% accuracy on training dictionaries and 0% on unseen terms ([Otten & Anastasopoulos 2025](https://aclanthology.org/2025.alp-1.11.pdf); method-evidence audit §3).

- **Data:** attested files only for evaluation. Representation training may additionally use `SYNTHETIC-AUGMENTED/mero-corpus.txt` under two frozen arms — Arm-S (with augmentation, replicating the published setup) and Arm-N (attested-only) — both reported (A19-style dual treatment; the augmented file never contributes an evaluation item, gloss, or decoy).
- **Models (frozen menu, no additions after contact):** (a) Word2Vec re-run at the paper's dims 20–120 (exact replication control, using the repo's own code files pinned in §7); (b) fastText-style character-n-gram embeddings (n=2–5) trained on the attested corpus — motivated by the alphasyllabary + suffixing typology; (c) unsupervised morphological segmentation (Morfessor 2.0 baseline + Bayesian HMM segmenter) feeding morph-aware embeddings; (d) alignment: VecMap (unsupervised, numeral-seeded, noun-seeded — the paper's three settings) + Procrustes over the anchor seed lexicon. Anchor language: the repo's Late Egyptian comparison corpus (302 texts per the dossier); an Old Nubian corpus may be added ONLY if its audit (D4) passes before appendix deposit — otherwise not at all.
- **Evaluation:** leave-k-out over the gold glosses, 5 folds, k≈39 (Tier B: 193 glosses; folds frozen with seed 20260811 before model contact). **Narrowing (registered):** all attested units containing a held-out gloss word are masked from that fold's training/prompt context — stricter than the frozen text's minimum, closing the formula-leakage channel flagged by the falsifier ("held-out folds share the … slot grammar with training"). Metric: top-1 gloss accuracy (secondary top-5), identical splits published with code (frozen H-MER-2 metric).
- **Success/disconfirmation:** exactly as frozen — H1 iff accuracy > 20% with p < 0.05 across ≥5 folds (one-sample test vs the baseline constant; exact binomial specification in §7 P-8). ≤20% → registered negative: "Meroitic expansion claims then rest solely on anchor-based H-MER-1 routes" (frozen disconfirmation clause). This track licenses E1 method claims only; **every individual new gloss still requires H-MER-1** (frozen text).

### 3.2 Track 2 — H-MER-1 individual lexical/grammatical claims via anchors (E2), with H-ONO-1 where name/toponym-based

- **Generation (Agent-G):** produces ≤9 proposals per run (cap registered in §7 P-4 for Holm attainability): lexeme-meaning proposals from loanword/toponym/name anchors, and morph-function proposals (e.g., case/postposition/plural/determiner function assignments). Agent-G may use any tool including LLMs (contamination is a scoring-side hazard, controlled in §8). Each proposal is deposited (hashed) with: proposed gloss/function, anchor type, anchor evidence, and enumerated attestation contexts, BEFORE Agent-S sees it.
- **Registration (Agent-F, blind):** assigns each lexeme proposal's semantic field mechanically — the WordNet 3.1 supersense (lexicographer file) of the proposed gloss's first-listed synset — and samples the decoy panel per §7 P-4. Agent-F never sees context-fit scores.
- **Scoring (Agent-S, frozen function):** context-fit on the funerary-formula slot grammar (invocation–nomination–filiation–benedictions; Rilly, UEE) and non-funerary contexts where attested (frozen H-MER-1 metric). Implementation (frozen): for each attestation context c of claim word w with candidate gloss m — (1) map every already-glossed word in c (Tier-B glosses, excluding w) to its English gloss; (2) score S(m,c) = Σ_j α(j) · cos(v_m, v_gj) in a pinned English fastText space (cc.en.300, §7 P-5), α(j) = 1 for slot-adjacent glosses, 0.5 otherwise; (3) claim score = mean over contexts. Decoys scored by the identical function. Morph proposals: candidate function f is scored by the held-out pseudo-log-likelihood improvement of a frozen slot-grammar model (first-order model over {slot label, morph, host class}, trained on attested phrases excluding the claim's contexts) when f's positional/co-occurrence constraints are imposed, vs decoy assignments (decoy universe: §7 P-4b).
- **Success/disconfirmation (frozen, not authored here):** H1 iff the proposal beats the decoy distribution at empirical p < 0.01 (Holm-corrected within the run), has ≥3 independent attestation contexts (independence = distinct REM concordance groups, per D3 — a registered tightening), and — if name/toponym-based — **independently satisfies H-ONO-1 in full** (all six registration elements instantiated in §7 P-6; both nulls at p < 0.005; G3-admissible corollary checked). NES-cognate-based claims must cite comparative data deposited before scoring (frozen threshold clause). Disconfirmation: decoy failure, <3 contexts, or anchor failing H-ONO-1 → rejected and logged; "many weak matches do not sum" (H-ONO-1 disconfirmation clause).
- **Formulaic-monoculture control (narrowing, registered):** a headline E2 lexeme claim requires ≥1 of its ≥3 contexts to lie outside the four funerary-formula slots (genre tags from D3). Claims whose every context is formula-internal are scored and reported, but labeled **"formula-internal — consistent with formula completion"** and are not headline-eligible. This directly answers the falsifier's "decoy-ranked context-fit on that grammar risks rewarding formula completion."
- **Family-framing control (frozen):** Rowan-vs-Rilly framing must not be assumed in scoring (frozen H-MER-1 controls); the scoring function above contains no family-dependent term.

### 3.3 Track 3 — E3 pathway instrument (no E3 claim this run)

For every Track-2 survivor, a **prospective prediction record** is deposited (hashed) per the frozen control clause ("confirmed proposals must not degrade, and should improve, slot prediction when unpublished texts become available — E3 event, logged prospectively"): predicted distributional consequences on custodian-sealed texts — e.g., occurrence rate of word-form w in nomination-slot position in funerary texts from site-class S within frozen frequency bands. Admissibility argument (registered): because the script is read, the sign-sequence content of a sealed text is externally observable by custodian epigraphers **independently of any semantic hypothesis under test** — this is the G3-compatible observable class (names independently attested, quantities, distributional facts), not "predicting the reading of a new text." The retraction rule is frozen: a proposal contradicted by a reserved-partition text is retracted with a first-class report.

---

## 4. Claim-ladder levels attempted and licensing

| Level | Attempted? | Licensed class (per tribunal record) |
|---|---|---|
| L1 glyph normalization | No (no image DB; paleography out of scope) | — |
| L2 segmentation | Given by the script (2–3-dot word dividers; Rilly, UEE) — descriptive verification only | E0 descriptive |
| L3 structural classes (slot-grammar induction, morph distribution) | Yes (infrastructure + reportable structure) | E2 structural |
| L4 grammatical roles (morph-function proposals) | Yes, via H-MER-1 morph route | E2, anchor route |
| L5 phonetic hypotheses | Not attempted (Griffith values assumed) | — |
| L6 lexical correspondences | Yes, via H-MER-1 + H-ONO-1 | E2, anchor route |
| L7 translation | Prohibited (G2, Runs 2–3) | — |
| Aggregate method (lexicon induction) | Yes (H-MER-2) | E1 |
| Language-family identity | Not attempted; no claim licensed either way | — |
| E3 strong claims | Not this run; custodian pathway only (A9) | E3-contingent |

---

## 5. Preregistered success/disconfirmation criteria (references, not new authorship)

This design executes, without modification of thresholds: **H-MER-1** (E2; frozen §5), **H-MER-2** (E1; frozen §5), **H-ONO-1** (transversal template; frozen §9) — under global rules G1–G9 and amendments **A9** (custodian + firewall), **A15** (corollary universe frozen before matching — applied to every H-ONO-1 corollary via §7 P-6), **A17** (appendix deposited before data contact; §7), **A18** (claim-band reporting; §0), **A19** (unit treatments; §2). Where this design adds constraints (fold masking, ≥1 non-formulaic context, REM-group context independence, decoy-count/claim-cap fixes), each is a **narrowing** — permitted ("appendices may narrow but never widen registered thresholds," frozen §11) — and each is itemized in §7 so no discretion remains at execution time. Adjudication of headline outcomes: cross-model tribunal (G7); the executing team and this designer have no vote.

---

## 6. Custodian protocol (A9 concrete proposal — the E3 instrument)

**Problem (audited):** the ~900 unpublished texts (Qasr Ibrim, Musawwarat es-Sufra; [Rilly, UEE](https://escholarship.org/content/qt3128r3sw/qt3128r3sw_noSplash_a34fb083e49c75f88724b4054bd16aaf.pdf)) are held by editors with no access/deposit/blind-scoring mechanism; even published REM is scan-only (audit §1.1). Single-scholar dependence on the REM editor (Rilly) is a registered defect (checkpoint-2 falsification).

**Proposal targets (named; institutional roles to be confirmed in writing before any commitment is claimed):**
1. **Académie des Inscriptions et Belles-Lettres (AIBL)** — REM's publisher ([REM, AIBL](https://aibl.fr/publications/repertoire-depigraphie-meroitique-vol-i/)) — as protocol guarantor.
2. **Section française de la direction des antiquités du Soudan (SFDAS) / CNRS-LLACAN (C. Rilly)** — REM editorship — as scientific editor of sealed transcriptions, explicitly **not** sole custodian (two-person rule below).
3. **Egypt Exploration Society, London** — Qasr Ibrim excavation-memoir publisher (e.g., [Mills, *The Cemeteries of Qasr Ibrim*, EES Excavation Memoirs](https://www.amazon.com/Cemeteries-Qasr-Ibrim-Excavation-Memoirs/dp/0856980781); Meroitic Qasr Ibrim editions in [Hallof, SRaT 9.3, Röll Verlag](https://roell-verlag.de/Hallof-Meroitic-Inscriptions-SRaT-9-3/en)) — for the Qasr Ibrim tranche.
4. **Humboldt-Universität zu Berlin, Institut für Archäologie (Musawwarat es-Sufra project)** ([HU Berlin project page](https://www.archaeologie.hu-berlin.de/de/aknoa/forschung-und-projekte/projekte/musawwarat-es-sufra)) with the **Musawwarat Graffiti Archive** (hosted at MPIWG Berlin, [musawwaratgraffiti.mpiwg-berlin.mpg.de](https://musawwaratgraffiti.mpiwg-berlin.mpg.de/)) — for the Musawwarat tranche.
5. A neutral technical escrow (university library or Zenodo restricted deposit) holding hashes and sealed predictions.

**Mechanism (mirrors the adjudicated A12 two-team masking design):** (i) custodian consortium selects ≥100 unpublished texts across ≥2 sites and ≥3 genres; epigraphers transcribe them (funded work-package — the audit's finding that "transcription work nobody has funded" is the real blocker is answered with budget, not hope); (ii) SHA-256 of each sealed transcription + coarse metadata (site, genre, length band) deposited publicly at time T0; (iii) program deposits hashed Track-3 prediction records against that metadata; (iv) staged revelation in ≥3 tranches ≥6 months apart; (v) unmasking and scoring adjudicated by custodian-appointed epigraphers under the frozen rubric — never by the program. Until (i)–(ii) exist, **every Meroitic claim runs at E2 on existing anchors** (A9 verbatim). Program-side deliverable this run: the signed protocol text + funding estimate, sent to institutions 1–4; their acceptance is itself logged as an external event.

---

## 7. A17 pre-scoring appendix (frozen values; deposited to the tribunal record before any Track contacts data)

- **P-1 Dataset pin.** `Joshua-Otten/Meroitic-Corpus`, commit `1a6eb1097d89309944908400e8d8b7905fa2bea1` (2024-05-14). SHA-256 (attested evidential files): `LobbanVocabList.txt` (200 lines) `1275c34d…f622`; `MilletExamples.txt` (1,447) `9e0dc67c…670f`; `RillyExamples.txt` (40) `beae69e1…15f7`; `TanyidamaniNarrative.txt` (6) `92144779…dba1`; `HamadabStelaOfAmanirenasNarrative.txt` (5) `8c3e2290…b115`; `KalabshaMeroiticInscriptionOfKharamadoyeNarrative.txt` (6) `e06dba12…6d04d`; `Kalabsha_Millet.txt` (46) `42408955…7ac0`. Quarantined synthetic file: `mero-corpus.txt` (18,090) `b7f3350c…53ce`. Full 64-hex digests and the complete file manifest (including `Code/` and `Embeddings/` pins for the Track-1 replication arm) are in the deposited manifest `R3-MER-manifest-v1`. Contact declaration: hash/line-count only; no content read at design time.
- **P-2 Normalization table.** ASCII→transliteration mapping (Millet-paradigm base; Rilly-variant column for *ne/se/te/to* and *e*), deposited as `mer-normalization-v1.csv` and hashed before scoring; dual-run where columns disagree (A19/U3).
- **P-3 Concordance.** `mer-concordance-v1.csv` per D3, double-keyed, hashed before Track-2 scoring; duplication groups define context-independence and fold masking.
- **P-4 Control panels (Track 2).** (a) **Lexeme decoys: 999 per claim** (a registered narrowing of "≥99" — with 99 decoys the minimum attainable empirical p is 1/100 = 0.01, which cannot satisfy the frozen "p < 0.01"; 999 decoys give min p = 0.001). Pool: all WordNet 3.1 lemmas sharing the blind-assigned supersense, intersected with the top-2,000 lemmas of that supersense by frequency in the pinned `wordfreq` v3.x English list, minus the candidate; sampled to 999 with seed 20260811; if the intersected pool < 999, the full pool is used and the attainable-p floor is reported; if < 100, the claim is not scoreable this run (reported as such, not relaxed). (b) **Morph decoy universe:** frozen closed inventory of grammatical-function labels (case: genitive/dative-directive/locative/ablative/vocative; postpositions; determiner; plural; copula; TAM markers; person/number indices; discourse particles — full enumerated list in the deposited inventory `mer-function-inventory-v1`, closed before scoring) × host classes (NP-final, V-final, clause-final) × 20 site-permutation variants per assignment (seeds 1–20), to ≥999 decoy assignments; if the label×host universe < 100 distinct labels, morph claims are not scoreable this run. (c) **Claim cap: m ≤ 9 proposals per run** — with 999 decoys, min p = 0.001, and Holm's smallest threshold 0.01/m requires m ≤ 9 for the threshold to be attainable at rank 1. This closes the multiplicity/granularity loophole arithmetically.
- **P-5 Frozen scoring artifacts.** English gloss space: fastText `cc.en.300.bin` (pinned file hash in manifest); cosine in float64; tie tolerance ε = 10⁻⁹ (ties count against the proposal); slot-adjacency weights α ∈ {1, 0.5} as in §3.2, frozen.
- **P-6 H-ONO-1 instantiation (per anchor claim; all six elements closed before sign-value inspection — noting values are Griffith's, established 1907–1911, hence independent of all candidates by construction, provenance documented per element 3).** (1) candidate name set: enumerated closed list from the audited onomasticon deposit (D4 audit precondition; counts cited only after audit); (2) transformation budget: frozen cost table (vowel-quality shift 1; nasal assimilation 1; final -e apocope 1; consonant substitution outside frozen equivalence classes 3; max total cost 4 — identical for target and decoys); (3) sign values: Griffith/Rilly standard values, source page-cited; (4) matching score: cost-weighted edit distance normalized by name length; (5) nulls: ≥999 decoy names matched on length/structure from the same onomasticon + ≥999 scrambled value assignments (permuting values within {consonant signs} and within {vowel signs} separately, preserving syllabic signs' CV structure); (6) acceptance: p < 0.005 on both nulls, Holm across all onomastic claims in the run, + one pre-designated G3 corollary from the frozen corollary universe (A15): {same values reading a second independent name; provenance covariation; object-type covariation} — corollary type designated per claim before matching begins, search log auditable.
- **P-7 Fold freeze (Track 1).** 5 folds, k≈39, seed 20260811, split at gloss-word level with REM-group text masking (§3.1); fold membership hashed before model contact.
- **P-8 Power analysis (registered computations, design decisions citing nothing).** H-MER-2, Tier B (n=193), one-sided exact binomial vs p₀ = 0.20 at α = 0.05: critical count 49/193 (size 0.040); power 0.48 at true accuracy 0.25, 0.81 at 0.28, **0.93 at 0.30**, 0.998 at 0.35. Tier A (illustrative n = 97–100): critical 27/97 (size 0.040); power 0.71 at 0.30, 0.95 at 0.35 — Tier A is therefore adequately powered only for large effects, and a Tier-A null at effect < 0.35 is reported as "underpowered," not "negative." H-MER-1: rank-based attainability as in P-4; sensitivity calibration = the decoy machinery run on 20 development glosses (drawn from Tier B, excluded from any claim), reporting the empirical distribution of true-gloss ranks; this calibration is part of the deposited appendix and its glosses are barred from Track-2 claims.
- **P-9 Tolerances.** Embedding training: 5 seeds (1–5), mean ± sd reported; accuracy comparisons at 4 decimal places; any post-hoc feature or weight change after first scoring contact voids the affected claim (protocol violation, frozen §11 deviation rule).
- **P-10 Onomasticon/comparanda audits** (D4) deposited before H-ONO-1 registration closes; absent audits, name-based claims are not scoreable this run.

---

## 8. Contamination controls (G6)

1. **Training-data exposure is assumed, not debated:** Rilly's UEE article, Millet 1968-derived examples, Lobban 2021, and the 2025 paper (published pre-cutoff) are plausibly in every frontier model's training data — flagged per G6. Consequences: (a) Track-2 **scoring functions are non-LLM** (fastText cosine, slot-grammar pseudo-likelihood) — deterministic, contamination-immune; (b) LLMs may serve only in Agent-G generation, where contamination cannot manufacture a pass (the decoy test punishes memorized glosses no less than novel ones — a memorized *correct* gloss still counts as knowledge only at E2-anchor standard, and its anchor must pass H-ONO-1); (c) H-MER-2 is contamination-vulnerable in any LLM-assisted arm — therefore the **primary H-MER-2 arms are non-LLM** (Word2Vec/fastText/Morfessor pipelines trained only on the pinned corpus); any LLM-assisted arm is secondary and carries a contamination flag with the model's cutoff date recorded.
2. **Prospective instrument:** custodian-sealed texts (§6) are the contamination-proof endpoint (unpublished, post-cutoff by construction) — the program's preferred instrument class per G6.
3. **Synthetic firewall:** §1.2 D5 halt rule (A9).
4. **Negative control coupling:** the Phaistos control (H-PHA-1) runs concurrently with Run 3 experiments; a pipeline failure there quarantines concurrent Meroitic results per the frozen consequence clause, and the identical reporting/confidence policy applies here (A16 discipline).

---

## 9. Human-expert loop

A7 binds OBS specifically; **no amendment mandates a human loop for MER**, and this design claims no exemption from tribunal review (G7) on that basis. The design nonetheless includes named-human elements where the tribunal's factual findings demand them: (i) a **named Meroiticist consultant** (recruited before execution; the plan v2 §11 open decision on recruiting an epigrapher is hereby exercised for MER) resolves concordance double-keying disagreements (D3) and constructs the Tier-A secure-gloss list (U2) — both BEFORE scoring, so no post-hoc discretion; (ii) the **single-scholar dependence** on Rilly (author of the NES classification, compiler of comparanda, REM editor — checkpoint-2 falsification) is mitigated structurally: the consultant for (i) must not be the REM editor, NES comparanda must come from independently deposited sources (frozen H-MER-1 clause), and the custodian consortium (§6) distributes custody across four institutions; (iii) E3 adjudication, if ever reached, is by custodian-appointed epigraphers, never program agents.

---

## 10. Compute and team estimate

- **Compute: order 10² GPU-hours** (upper bound of the order estimate). Word2Vec/fastText training on a ~10³-text corpus is minutes per configuration on CPU; the full frozen sweep (2 arms × 2 normalizations × ~6 model configs × 5 seeds × 5 folds ≈ 600 runs) remains CPU-tractable (<10³ CPU-hours); GPU spend is dominated by optional LLM-assisted generation and segmenter training. No large-model training is required or licensed by this design.
- **Team: ~8–10 team-months.** ML engineering 2 FTE × 3 months (pipeline, decoy machinery, frozen scoring functions, logs); philological consultant 0.5 FTE × 4 months (concordance verification, Tier-A list, normalization table); program management/custodian negotiation 0.25 FTE × 8 months (institutional letters, protocol, escrow). Custodian-side transcription funding (§6) is a separate work-package priced with the institutions, not counted here.

---

## 11. What a null result means, and why it is publishable

- **H-MER-2 null (≤20%):** the first *registered, adequately powered* (0.93 at effect 0.30) confirmation that the embed-and-align family fails at ~10³-text scale even with morphological awareness and a related anchor corpus — converting Otten & Anastasopoulos's exploratory negative into a calibrated corpus-size floor for lexicon induction on Shape-C languages. Per G9, reported at headline prominence.
- **H-MER-1 family null (all ≤9 proposals fail decoys/anchors):** the registered conclusion is that the anchor route — **the exact mechanism that produced Griffith's original decipherment** (checkpoint-2 falsification note) — is exhausted at the current published-anchor inventory. That is the strongest evidence obtainable that the binding constraint on Meroitic is *data release, not method*, and it converts the custodian proposal (§6) from nice-to-have into the field's critical path — a publishable, actionable negative.
- **Custodian refusal/non-response:** itself a documented finding about the field's evaluability infrastructure, logged as the A9 pathway remaining aspirational; Meroitic then remains capped at E2 indefinitely, and the program says so.

## 12. Residual-discretion audit (self-check against the "no degrees of freedom" standard)

Every execution-time choice is pinned: dataset (commit + per-file SHA-256), unit treatments (U1–U4 dual-run rules), fold seeds and membership hashes, decoy counts/pools/seeds, claim cap (m ≤ 9), scoring formulas and tie rules, transformation budgets, corollary universes (A15), normalization tables, calibration-gloss exclusions, halt rules, and reporting policy (A16-identical across control and targets). The only open values are those that *cannot* exist before their preconditions (onomasticon audit counts, Tier-A membership n, custodian tranche composition) — each is gated behind a deposit-before-scoring rule, so it is fixed before it can influence any score. Any deviation after data contact is reported as a protocol violation with the registered analysis alongside (frozen §11).

**Compute estimate:** Order 10^2 GPU-hours (upper bound; dominated by optional LLM-assisted candidate generation and segmenter training). Core pipeline is CPU-tractable: ~600 frozen configurations (2 arms x 2 normalizations x ~6 models x 5 seeds x 5 folds) of Word2Vec/fastText/Morfessor-scale training on a ~10^3-text corpus, <10^3 CPU-hours total. Team: ~8-10 team-months (2 ML FTE x 3 mo; 0.5 philology FTE x 4 mo; 0.25 PM FTE x 8 mo for custodian negotiation); custodian-side transcription is a separately priced work-package.

**Null result meaning:** An H-MER-2 null (<=20% induction accuracy) is the first registered, adequately powered (0.93 power at effect size 0.30, exact binomial, n=193) confirmation that the embed-and-align family fails at ~10^3-text scale even with morphological awareness and a related anchor language — a calibrated corpus-size floor for lexicon induction on Shape-C languages, upgrading Otten & Anastasopoulos's exploratory negative. An H-MER-1 family null (all <=9 anchor proposals failing decoy/H-ONO-1 tests) means the anchor route — the mechanism that produced Griffith's original decipherment — is exhausted at the current published-anchor inventory: the binding constraint on Meroitic is data release, not method. That result makes the custodian-sealed reserve the field's critical path and is publishable per G9 at the same prominence as any positive finding. Custodian non-response is itself a documented evaluability finding: Meroitic stays capped at E2 and the program reports why.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (R3-MER, frozen for deposit before data contact): P-1 Dataset pin — Joshua-Otten/Meroitic-Corpus commit 1a6eb1097d89309944908400e8d8b7905fa2bea1 (2024-05-14); SHA-256: LobbanVocabList.txt(200 ln)=1275c34d10bf4dc397cc0e457f3a686fdb76f3fbc192b3b42efb6afba753d622; MilletExamples.txt(1447)=9e0dc67ca945fa915479f015cdb6083b5788f86c3cc096f171994b0e4e670e6f; RillyExamples.txt(40)=beae69e1b417cdd6bcdf88b2d6987af22b6cc99044dbd40d3276b8b13815f1f7; TanyidamaniNarrative.txt(6)=92144779aec84f735a3f0851c8898ad26a40a733d4466aebe93ecfd307e4dba1; HamadabStelaOfAmanirenasNarrative.txt(5)=8c3e22902ac61361dc13bc7863b4b418ba88b06c4eaf71e4fbeba6a176dbe115; KalabshaMeroiticInscriptionOfKharamadoyeNarrative.txt(6)=e06dba12998118c420f4188a6607b9cab7fdfc6287922355923b27e5f136d04d; Kalabsha_Millet.txt(46)=42408955e513a98e35b539013ceaaff2ebc25616e2091c09f16a12d9b1ef7ac0; QUARANTINED synthetic mero-corpus.txt(18090)=b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce; replication pins: Code/getW2V_embeddings.py=3dc5ddc5..., all Code/ and Embeddings/ hashes in manifest R3-MER-manifest-v1; contact declaration: hash/line-count only at design time. P-2 Normalization table mer-normalization-v1.csv (Millet base + Rilly variant columns for ne/se/te/to and e); dual-run on disagreement (A19/U3). P-3 REM concordance mer-concordance-v1.csv, double-keyed, hashed before Track-2 scoring; duplication groups define context independence and fold masking. P-4 Control panels — lexeme decoys 999/claim (narrowed from >=99: min empirical p 1/1000=0.001 makes frozen p<0.01 attainable), pool = WordNet 3.1 supersense lemmas (blind-assigned by Agent-F from first-listed synset) intersected with top-2000 wordfreq-v3 English frequency list, seed 20260811; pool<999 -> full pool with attainable-p floor reported; pool<100 -> claim unscoreable this run. Morph decoy universe = frozen closed function inventory (mer-function-inventory-v1) x host classes (NP-final/V-final/clause-final) x 20 site-permutations (seeds 1-20) to >=999 assignments; <100 distinct label-host pairs -> morph claims unscoreable. Claim cap m<=9 per run (Holm 0.01/m attainable iff m<=9 at min p 0.001). P-5 Scoring artifacts — fastText cc.en.300.bin (hash in manifest), float64 cosine, tie tolerance 1e-9 (ties count against proposal), slot-adjacency weights alpha={1,0.5}. P-6 H-ONO-1 instantiation — closed candidate name set from audited onomastica (audit deposit P-10 precondition); transformation cost table (vowel shift 1, nasal assimilation 1, final -e apocope 1, out-of-class consonant substitution 3, budget cap 4, identical for target and decoys); sign values = Griffith/Rilly standard (1907-1911, independent by construction, page-cited); score = cost-weighted length-normalized edit distance; nulls = >=999 matched decoy names + >=999 scrambled value assignments (values permuted within consonant-sign and vowel-sign classes, CV structure of syllabics preserved); acceptance p<0.005 both nulls, Holm across run, + one pre-designated A15 corollary from frozen universe {second-name reading, provenance covariation, object-type covariation}, search log auditable. P-7 Fold freeze — 5 folds, k~39, seed 20260811, gloss-word split with REM-group text masking; membership hashed before model contact. P-8 Power — H-MER-2 Tier B n=193 exact one-sided binomial vs p0=0.20, alpha=0.05: critical 49/193 (size .040), power .48@.25, .81@.28, .93@.30, .998@.35; Tier A n~97: critical 27/97 (size .040), power .71@.30, .95@.35 (Tier-A null below effect .35 reported as underpowered); H-MER-1 sensitivity calibration on 20 development glosses (excluded from claims), true-gloss rank distribution deposited. P-9 Tolerances — 5 training seeds (1-5) mean+/-sd; post-contact feature/weight changes void the claim (protocol violation). P-10 Onomasticon and NES-comparanda data-reality audits deposited before H-ONO-1 registration closes; absent audit, name-based claims unscoreable. Unit treatments frozen (A19): U1 attested-871/REM-1300/known->2000 dual-denominator reporting; U2 gloss Tier A (Rilly-secure subset, consultant-built, hashed pre-scoring) vs Tier B (all 193, baseline-matching primary); U3 Millet/Rilly transcription dual-run; U4 23-sign inventory single treatment. Halt rule: augmented corpus described as ancient evidence halts the run (A9).

# Proto-Elamite Structural/Semantic Inference (+ Proto-cuneiform calibration arm)

# Run 3 Experiment Design — Proto-Elamite Structural/Semantic Inference (E2 band) with Proto-Cuneiform Calibration Arm

**Design ID:** R3-PE-01 · **Date:** 2026-08-11 · **Status:** Design frozen pending (a) tribunal deposit of the A17 appendix (§14) and (b) registration of the H-PE/H-PC hypothesis family as amendment **A20** under the frozen prereg's amendment policy ("Amendments are permitted only (a) before the first scoring agent contacts data for the affected hypothesis, and (b) as an appended, dated, signed changelog entry" — run2-preregistration-FROZEN.md, Amendment policy). No agent has contacted experiment data for any hypothesis in this design.

**Governing documents (binding, in precedence order):** tribunal-record-and-prereg-amendments-v1_1.md (A1–A19) → run2-preregistration-FROZEN.md (G1–G9; H-PHA-1; H-ONO-1) → undeciphered-research-plan-v2.md (§2 gate, §3 shadow benchmarks, §4 ladder, §9 risk register) → run2-audits-methods-patch.md (audited data reality) → run2-checkpoint2-matrix.md (falsification verdicts).

**Adjudication independence (G2/HARKing guard):** This document *designs* experiments; it does not adjudicate them. All success tests are scored by agents disjoint from the hypothesis-generating and design agents, against the frozen prereg + amendments; headline claims are adjudicated by the cross-model tribunal (G7; tribunal I.1: "internal agreement, however structured, is never sufficient"). The expert-review rubric (§11) is authored by the tribunal convener, not by this designer.

---

## 1. Licensed claim bands and prohibited claims

Adjudicated status (tribunal I.2): **Proto-Elamite: E2 — structural/semantic claims; no phonetic/language-identity route.** Checkpoint 2 (falsification, UPHELD): "E2 for accounting-structural/semantic claims via entries-must-sum-to-totals arithmetic and held-out splits… language/phonology capped at E1 per the glottography caveat… dual-scheme (allography) reporting mandatory" (run2-checkpoint2-matrix.md, Proto-Elamite verdict). Proto-cuneiform: **E2 upheld, administrative-semantic claims; calibration role coherent; a confident language/non-language verdict on it is a calibration failure by design** (run2-checkpoint2-matrix.md, Proto-cuneiform verdict).

**Claim-ladder levels attempted (G2, plan §4), with licensed E-class per band (A18 format):**

| Band | Attempted? | Licensed class | Instrument |
|---|---|---|---|
| L1 glyph normalization (allography schemes over M-codes) | Yes | E2 structural (dual-scheme reporting per A19) | CDLI M-code ATF + cdli-gh/proto-elamite_data sign drawings |
| L2 segmentation / document parsing | Yes | E2 structural | H-PE-1 (held-out, arithmetic-verified gold) |
| L3 structural classes (six numerical systems, header–entry–total grammar) | Yes | E2 structural | H-PE-1, H-PE-2 |
| L4 semantic roles (commodity categories; administrative/institution roles) | Yes | E2 candidate-hypothesis claims only, G3-admissible checks + human-expert review | H-PE-3, H-PE-4 |
| L5 phonetic hypotheses | **No — prohibited** | — (tribunal I.2: no phonetic route) | — |
| L6 lexical correspondences / L7 translation | **No — prohibited** (L7 barred program-wide, G2) | — | — |
| Language-identity / is-it-language | **No — not exercised** (would be E1-max; zero such claims registered) | — | — |

**Drift guard (explicit prohibition, enforced mechanically):** No output of any module or report in this design may contain: (i) a phonetic value for any M-sign; (ii) an identification of the underlying language (including any engagement with Desset's 2020 "Early Proto-Iranian" recast, recorded in the graveyard as "not accepted" — run1-checkpoint1-dossiers.md, Proto-Elamite §6, citing [Proto-Elamite script, Wikipedia](https://en.wikipedia.org/wiki/Proto-Elamite_script)); (iii) a glottography verdict; (iv) any reading, gloss, or translation of a sign sequence. A lexical filter over all agent outputs flags candidate violations; a non-design audit agent reviews flags; any confirmed L5+ emission is reported as a protocol violation per the frozen deviation rule. The same reporting-confidence policy applies to the Phaistos control (A16). Results are phrased in A18 claim-band format: *"Proto-Elamite: E2/L1–L4 accounting-structural/semantic · E1 language-status (not exercised) · E0 phonetic readings (prohibited)."* The proto-cuneiform arm additionally prohibits any language/non-language verdict (calibration-failure condition, run2-checkpoint2-matrix.md).

---

## 2. Data acquisition plan (audited reality only)

Per G8, data basis is declared as **(iii) transliterations/sign-code sequences + (iv) structured relational catalogue**; the L1 allography audit additionally consults (ii)-type vector drawings for scheme construction (no image-ML claims). Results do not transfer to photographic bases without a registered bridging test (none registered here).

**Primary corpus — Proto-Elamite.** CDLI live database, period facet "Proto-Elamite (ca. 3100-2900 BC)": **1,755 catalogue entries; ATF inscription export returned 1,597 texts (508 KB, verified download 2026-08-11)** — ~91% sign-level coverage using M### sign codes (Meriggi-derived) + N-numerals; lang tags predominantly `qpc` (34+1544 variants), 3 `nlc`, 1 `qpe` (run2-audits-methods-patch.md, "CDLI live database — Proto-Elamite holdings + ATF coverage," 5/5; <https://cdli.earth/search?f[period][]=Proto-Elamite (ca. 3100-2900 BC)>). Audit-mandated range reporting: tablet count **1,600–1,755** (older literature ~1,600 vs CDLI 1,755 entries; audit note, same row). Sign codes are **graphotactic, not phonetic readings** (audit note). ~9% of entries (158) lack ATF (run2-checkpoint2-matrix.md, PE verdict) — these are handled in §8 as a registered prospective-extension pool, not as available data.

**Calibration corpus — proto-cuneiform.** CDLI live database: **Uruk IV 1,892 entries (1,836 in ATF export); Uruk III 5,921 entries (5,440 in ATF export)**, verified 2026-08-11; ATF is sign-level transliteration with N-sign numerical notation (run2-audits-methods-patch.md, "CDLI live database — proto-cuneiform holdings," 5/5, "Best-in-class among audited systems… Live export verified end-to-end (downloaded 1.6MB Uruk III ATF, 5,440 texts)"; <https://cdli.earth/search?f[period][]=Uruk III (ca. 3200-3000 BC)>).

**Operational caveats adopted from the audit (not from papers' claims):** cdli.mpiwg-berlin.mpg.de 301-redirects to cdli.earth; intermittent 502s (observed 3×, retries succeed); default pagination 25/page — must pass `limit=` (verified up to 10,000); the GitHub bulk dump (github.com/cdli-gh/data) is **stale ("Last update was August 2022")** and is prohibited as a primary source — live export only (audit rows 5/5 and 4/5). **License risk logged:** CDLI states no blanket data license on the new UI; per-image facet offers CC-BY-4.0/PD/none (audit). The proto-cuneiform falsification verdict classifies this as "a redistribution risk worth logging," not an evaluability defect (run2-checkpoint2-matrix.md). Consequence: we redistribute derived statistics, split manifests as P-number lists, and hashes — not the ATF payload.

**Auxiliary resources.** (a) cdli-gh/proto-elamite_data: EPS vector drawings of PE signs named by M-number, **CC-BY-4.0**, "useful for glyph normalization (claim-ladder L1) but images only" (audit, 2/5; <https://github.com/cdli-gh/proto-elamite_data>) — used solely to construct the frozen allography mapping (§3). (b) The third-party ProtoElamite GitHub repo (1,467 Susa-tablet JSON derivative; run1-checkpoint1-dossiers.md §1, <https://github.com/MahmoodKhalil57/ProtoElamite>) is a **cross-check only**, never a primary source (unlicensed derivative). (c) Published structural knowledge for the frozen category inventory: [Englund 2004, "The State of Decipherment of Proto-Elamite"](https://cdli.earth/files-up/publications/englund2004c.pdf) (six numerical systems: sexagesimal — high-status objects; decimal — animals and low-status humans; bisexagesimal + derivatives — grain products; grain-capacity systems; one area-system attestation; tripartite heading–entries–totals document structure) and [Kelley, *Proto-Elamite*, Cambridge Element](https://www.cambridge.org/core/elements/protoelamite/3684B7262E21A8B6AF8657D948A5B1A6) (commodity/personnel/institution signs; ~1,700 tablets, ≥1,600 from Susa, ~100 from 8–9 other sites).

**Acquisition procedure (frozen):** one acquisition window 2026-08-15→2026-08-31; a non-scoring **data-steward agent** downloads PE, Uruk IV, Uruk III ATF + catalogue CSV via the live export with `limit=10000`, retries on 502; computes SHA-256 of every file; deposits hashes + row/text counts + acquisition timestamps into the tribunal record **before any model-training or scoring agent contacts the data** (A17). Counts must reconcile to the audited figures within ±3% (live DB drift tolerance, frozen); larger drift halts the run pending re-audit. The audit's byte count (508 KB PE ATF) is the provisional fingerprint until the hash is deposited.

---

## 3. Frozen unit treatments (A19) and dedup (G6-adjacent)

PE's contested units, frozen per A19 (the Part I.3–4 registry pattern applied to this system's disputes):

1. **Sign inventory / allography.** Disputed by counting method: "between 600 and 900 discrete signs" (Englund) vs Meriggi's "under 400 sign entries" vs de Mecquenem's inflated ~5,500 ([Englund 2004](https://cdli.earth/files-up/publications/englund2004c.pdf); run1-checkpoint1-dossiers.md §1). The falsifier made dual-scheme reporting mandatory (checkpoint 2). Frozen treatments: **Scheme S1 ("CDLI/Meriggi as-encoded")** — M-codes exactly as in the ATF, variant suffixes distinct (M143-A ≠ M143); **Scheme S2 ("variant-merged")** — a deterministic mapping collapsing registered variant suffixes to base M-numbers, built mechanically from the M-number naming convention of the ATF sign list and the cdli-gh/proto-elamite_data file inventory (M001.EPS, M143-A.EPS, …), deposited as a hashed lookup table in the appendix. **Every endpoint is computed under both S1 and S2; scheme disagreement on any pass/fail verdict → no single-scheme headline; the divergence is itself the reported finding** (mirrors the H-IND-2 dual-inventory rule and A19's "reported under all frozen unit treatments where they disagree"). N-signs (numerals) are scheme-invariant and are stated as such wherever an endpoint is numeral-only.
2. **Corpus-count universe.** 1,600–1,755 tablets (audit range, frozen); the analysis universe is the deduplicated ATF set (below), reported alongside the raw counts.
3. **Numerical-system assignment.** The six-system grammar (Englund 2004) with the N-prefix/M-prefix sign partition ([Proto-Elamite script, Wikipedia](https://en.wikipedia.org/wiki/Proto-Elamite_script)) is frozen as a **per-N-sign → system(s) lookup + conversion table** deposited in the appendix before data contact. This discharges the falsifier's forking-paths attack (3): "the prereg's pre-scoring appendix mechanism can freeze system assignment before scoring" (checkpoint 2). Entries whose system is ambiguous under the frozen table are labeled `ambiguous` mechanically; no per-case discretion exists at scoring time.

**Dedup (leakage guard, A2-analog "object-family level"):** (i) merge P-numbers referring to the same physical object via CDLI catalogue join/composite fields; (ii) exact-duplicate ATF payloads collapsed; (iii) near-duplicates (Jaccard ≥ 0.8 over sign 3-grams, computed under S2) forced into the same split. All rules deterministic; executed by the data steward; manifest hashed.

---

## 4. Roles, blinding, and split construction

- **Data steward** (non-scoring): acquisition, dedup, splits, gold-label derivation, answer-key custody.
- **Modeling team**: sees train+dev only.
- **Proposal generator** (H-PE-3b/H-PE-4): disjoint from the **scoring/audit agent** (G2).
- **Phaistos audit agent**: had no role in building modules (H-PHA-1).
- **Cross-model tribunal**: adjudicates all headline claims (G7).

**Splits:** tablet-level (never line-level), 70/10/20 train/dev/test, stratified by (i) provenience (Susa vs non-Susa) and (ii) ATF completeness tercile; **5 independent splits, seeds frozen: {3100, 2900, 1755, 1597, 20260811}**; report mean ± sd across splits (mirrors H-OBS-1 split logic). One-shot test application per split per endpoint; no post-hoc feature or hyperparameter changes (H-IND-2 discipline). Identical machinery for the proto-cuneiform arm.

---

## 5. Preregistered hypotheses (to be registered as amendment A20; adjudication references the frozen prereg + A1–A19)

All endpoints inherit: **A1 conjunctive success logic** (failure to satisfy *every* registered criterion = failure; no "promising" zone); **G5** Holm–Bonferroni within this family over all endpoints actually run, mandatory search/restart logs; **G9** null results reported at equal prominence; **G3** admissibility (predictions concern numerical quantities, object type, provenance — never "the reading of a new text"); damaged/broken lines excluded from gold by frozen mechanical rules (ATF damage flags), never by judgment.

### H-PE-1 — Document-structure parsing on held-out tablets (L2/L3; E2 structural; precondition for H-PE-3/4)
- **H0:** A model trained on the training split labels line roles {header, entry, subtotal, total, other} on held-out tablets no better than the registered positional baseline (frozen heuristic: obverse-initial line = header; reverse-final numerical line(s) = total — the tripartite structure per [Englund 2004](https://cdli.earth/files-up/publications/englund2004c.pdf)).
- **H1:** Macro-F1 ≥ 0.80 **AND** ≥ baseline + 0.10, mean across 5 splits, cluster-bootstrap 95% CI lower bound above baseline.
- **Gold labels (independent of any model):** derived mechanically — a line is gold-`total` iff its notation equals the sum of the tablet's preceding eligible entries under the frozen system grammar (§3.3); entries/headers by frozen positional+composition rules; tablets where arithmetic cannot verify are excluded from the primary endpoint mechanically. A 60-tablet gold subset is independently double-annotated by two trained annotators (κ reported); parser–annotator agreement < 0.90 halts the family pending parser-rule repair *before* any scoring (logged as appendix narrowing, never widening).
- **Model space (frozen):** CRF/HMM over symbolic line features, gradient-boosted trees, and a from-scratch transformer ≤ 20M params; hyperparameter grids enumerated in the appendix; dev-split selection only.
- **Disconfirmation:** any criterion missed → H0 stands; H-PE-3/4 are not scored (family reports the structural null); H-PE-2 may still run (numeral-only).

### H-PE-2 — Quantity prediction / arithmetic completion (L3; E2; G3-admissible: numerical quantities)
- **Eligibility (mechanical):** held-out tablets, ≥2 entries, all entries + total legible under frozen damage rules ("arithmetic-complete").
- **Task A (total masking):** mask the total notation; predict exact value **and** numerical system. **Task B (entry masking):** mask one entry's notation; predict the exact arithmetically-consistent value including unit conversions within the frozen system grammar.
- **H0:** exact-match rates are within the null distribution from frequency-matched sampling of attested same-length-band notations under corpus marginals (≥1,000 draws per split; sampler frozen).
- **H1 (conjunctive):** Task B accuracy ≥ 0.90 on arithmetically-determined cases AND Task A exact (value+system) ≥ 0.75, mean across splits, each with empirical p < 0.001 vs null.
- **Tolerance:** exact numeric equality after canonicalization to the frozen fraction representation per system — value tolerance is **exact**, per the H-KHI-1 precedent.
- **Rationale for band:** this is the "entries-must-sum-to-totals" instrument the falsifier upheld: the six systems were validated by this arithmetic decades ago (Englund 2004), so passing is not a new decipherment — it is the frozen check that the pipeline's *parses and system assignments* constrain new claims on withheld tablets with G3-admissible predictions (checkpoint 2, attack 2 disposition). Scheme note: numeral-only; S1/S2-invariant (stated per A19).
- **Disconfirmation:** any criterion missed → registered negative: "pipeline has not demonstrated command of the numerical-system grammar on held-out tablets"; H-PE-3/4 are not scored.

### H-PE-3 — Commodity-category semantics (L4; E2 candidate hypotheses)
- **Precondition:** H-PE-1 and H-PE-2 pass (both schemes for H-PE-1).
- **Frozen category inventory K:** the published commodity/personnel/institution sign identifications compiled *only* from [Englund 2004](https://cdli.earth/files-up/publications/englund2004c.pdf) and [Kelley, Cambridge Element](https://www.cambridge.org/core/elements/protoelamite/3684B7262E21A8B6AF8657D948A5B1A6), each entry carrying its source locus; list hashed in the appendix before data contact. No other secondary literature is admissible (sealed-sources rule, §8.5).
- **Endpoint 3a (association claim):** **H0:** the numerical system of a held-out entry is not predictable from its non-numerical signs beyond structure-preserving permutation nulls (system labels permuted within tablets, preserving per-tablet system marginals — A11-analog structure-preserving null; ≥1,000 permutations). **H1:** balanced accuracy exceeds the permutation null at empirical p < 0.01 (Holm) under **both** S1 and S2. This operationalizes the registered system–commodity associations (grain→bisexagesimal/capacity; animals/low-status humans→decimal; high-status objects→sexagesimal, per Englund 2004) as an out-of-sample prediction rather than a citation.
- **Endpoint 3b (novel-sign proposals):** the generator agent proposes category assignments for M-signs **not in K** with ≥10 legible occurrences (E0-bar below 10, mirroring H-MAY-1's hapax bar). Scoring: frozen context-fit score (likelihood under the 3a association model over **ALL** attested contexts of the sign) vs **≥999 decoy assignments** (categories drawn frequency-matched from K's category set); success requires empirical p ≤ 0.001, Holm-corrected across all scored proposals at family α = 0.01; **at most 10 proposals scored per run**, selected by the frozen rule "highest occurrence count first" (Holm feasibility: 0.01/10 = 0.001 = the decoy floor). **Every-context rule:** one attested context in a numerical system inconsistent with the proposed category, absent a mechanically-flagged damage exclusion, falsifies the proposal (mirrors H-OBS-2's one-incoherent-context rule).
- **Disconfirmation:** 3a failure → no commodity-band claim; 3b proposals failing are logged and may not be reused in aggregate arguments (H-ONO-1 discipline). Family null if 3a fails or 0/≤10 proposals survive: "the pipeline cannot advance Proto-Elamite commodity semantics beyond the published inventory at current information conditions."

### H-PE-4 — Administrative-role semantics (L4; E2 candidate hypotheses)
- **Precondition:** H-PE-1 and H-PE-2 pass.
- **Endpoint 4a (slot-role prediction):** **H0:** the identity of the header-slot (owner/institution) sign on a held-out document is not predictable from document content beyond a sign-role permutation null. **H1:** top-1 slot-sign prediction beats the null at empirical p < 0.01 (Holm), both schemes.
- **Endpoint 4b (external covariation, G3-admissible):** for each proposed role sign (≥10 occurrences; ≤10 proposals, same Holm arithmetic and every-context rule as 3b), one **pre-designated** covariation prediction registered before scoring, drawn from the closed covariate set {commodity/system profile of the document; CDLI-catalogued object type; CDLI-catalogued provenience}. Provenience covariates are **secondary/exploratory unless the non-Susa document count in the test split ≥ 30** (frozen floor; Susa dominance ≥1,600 of ~1,700 tablets caps power — [Kelley, Cambridge Element](https://www.cambridge.org/core/elements/protoelamite/3684B7262E21A8B6AF8657D948A5B1A6)).
- **Disconfirmation:** as H-PE-3. Note: **H-ONO-1 is not invoked** — PE has no proper-name anchors ("No proper-name anchors are established," run1-checkpoint1-dossiers.md §2) and no onomastic claim is registered or permitted in this design.

### H-PC-0 — Proto-cuneiform calibration arm (E2 administrative-semantic; precondition for interpreting all PE results)
- **Design:** the *identical* pipeline (same parser rules adapted only by the frozen Uruk sign/system tables, same model spaces, same split logic, same seeds) runs on Uruk IV + Uruk III ATF, where numerical/metrological systems are deciphered (Nissen–Damerow–Englund, per the checkpoint-2 proto-cuneiform verdict) and many sign identifications are anchored by descendant cuneiform. **ATF language codes (qpc/nlc/sux) are conventions, not ground truth, and are never used as labels** (checkpoint 2: "downstream agents must not treat them as ground truth").
- **Registered calibration floors:** H-PE-1-analog macro-F1 ≥ 0.85; H-PE-2-analog Task B ≥ 0.95. **Failing either floor → all PE results are quarantined as a pipeline defect** (the H-KHI-1 positive-control logic: failure to recover the known case quarantines the family). Passing floors makes a PE null interpretable as an information-conditions finding rather than a method defect; the PC–PE performance gap is itself a registered deliverable.
- **Calibration-integrity condition:** any confident language/non-language verdict emitted about proto-cuneiform is a **calibration failure by design** (checkpoint 2). This arm is administratively separate from H-IND-1's use of proto-cuneiform as a discriminator control; no outputs are shared.

---

## 6. Method specification (implementation level)

1. **ATF parser:** deterministic; consumes CDLI ATF; emits a document tree (object → surfaces → columns → lines → tokens{M-sign | N-notation | damage}); frozen grammar for N-notations per the §3.3 conversion table; unit tests shipped with the appendix; parser version hashed. Yield statistics (lines parsed / excluded, per rule) are mandatory reporting.
2. **Feature sets (frozen):** line position (surface, ordinal, column), token composition (counts of N- vs M-tokens), sign identities under S1/S2, tablet-level aggregates. No features may be added after first test contact.
3. **Models:** (a) CRF/HMM line labeler; (b) gradient-boosted classifier for system/category prediction; (c) from-scratch encoder-only transformer ≤ 20M params on the symbolic vocabulary (no pretrained weights — §8.1). Hyperparameter grids enumerated in the appendix; selection on dev only; final weights hashed before test contact.
4. **Nulls:** implemented as registered code deposited with the appendix; permutation and decoy samplers seeded from the frozen seed list; every null draw logged (G5).
5. **Reporting:** per-endpoint, per-split, per-scheme (S1/S2) tables; all registered tests reported whether or not headline (G5); claim-band phrasing per A18; error-reporting language per tribunal I.3.2 ("N agents; no agent-run failures; K citation-verification failures subsequently corrected").

---

## 7. Negative control (H-PHA-1, A16)

The PE/PC modules (parser, structure labeler, quantity predictor, category/role scorer) run on the Phaistos Disc encoding alongside — not after — the real runs, under an **identical, frozen reporting/confidence policy** (A16), with system identity stripped from module inputs where the design allows. Registered pipeline-failure conditions for this design's modules (extending H-PHA-1 conditions 3): (i) any total/subtotal detection on the disc at reporting confidence (the disc has "no numerals" — run2-preregistration-FROZEN.md §10); (ii) any commodity-category or administrative-role assignment on disc signs at/above the reporting threshold. Per A16, report rates and confidence distributions are compared across control and targets by the independent audit agent; suppression-style divergence is itself a failed control. On failure: concurrent PE/PC positives are quarantined per H-PHA-1's registered consequences.

---

## 8. Contamination controls (G6)

1. **Contamination-resistant primary models:** all primary endpoints use models trained from scratch on the training split's symbolic data only — no web-pretrained weights — so public CDLI ATF in LLM pretraining corpora cannot leak into primary metrics.
2. **LLM firewall (optional generator only):** if an LLM is used in H-PE-3b/4 proposal generation, it operates under bijective randomization of all M-/N-codes with P-numbers stripped (shadow-randomization, plan §3/G6 — the mechanism validated by the finding that LLM "script competence substantially rides on Unicode-mediated training exposure," ["Reasoning Over the Glyphs," arXiv 2501.17785](https://arxiv.org/abs/2501.17785), per run2-audits-methods-patch.md §6). A proposal is admissible only if it arises under ≥2 independent remappings; remapped runs are primary.
3. **Temporal firewall / prospective subset (A6-analog, frozen):** cutoff 2026-08-11. ATF transcriptions newly published by CDLI after cutoff — including any of the 158 currently ATF-less PE entries, *transcribed by CDLI editors independently of this program* — form the prospective subset. Equivalence criterion frozen: prospective performance within 10 points of the standard held-out mean; any larger deficit is **reported as evidence of leakage, not passed under a grace band** (A6 wording adopted). This is a prospective *check*, not an E3 claim: PE's E3 path (National Museum of Iran holdings; ongoing Sofalin excavation — [Kelley, Cambridge Element](https://www.cambridge.org/core/elements/protoelamite/3684B7262E21A8B6AF8657D948A5B1A6)) requires an independent custodian committing to staged revelation (A9 pattern) and is **explicitly not claimed** here.
4. **Dedup/leakage:** §3 (object-family dedup, near-duplicate same-split forcing, tablet-level splits only).
5. **Sealed sources:** during scoring, no agent may consult publications containing per-tablet interpretations (Englund/Dahl/Kelley editions and commentary) beyond the frozen inventory K; retrieval logs audited (A8 pattern: rediscovery of unsealed corroborating evidence scores nothing).

---

## 9. Multiplicity and search discipline (G5)

Holm–Bonferroni within this family over all endpoints actually run: {PE-1, PE-2A, PE-2B, PE-3a, PE-3b(≤10), PE-4a, PE-4b(≤10), PC-0 floors}. Every model configuration trained, every null draw, every proposal generated-but-unscored is logged; selective reporting is a protocol violation. Restart counts logged (Tamburini restart-exploitation guard, [DOI 10.3389/frai.2025.1581129](https://cris.unibo.it/retrieve/7656690e-fe79-4b54-948b-fabce5723819/frai-8-1581129.pdf), per G5).

---

## 10. Power analysis (summary; frozen numbers in appendix §A.7)

Basis figures: 1,597 ATF texts (audit); "just over 1,600 pieces, with around 10,000 lines of text" ([Englund 2004](https://cdli.earth/files-up/publications/englund2004c.pdf)); conservative dedup retention 88% (assumption, frozen). Test split ≈ 280 tablets ≈ 1,750 lines/split. H-PE-1: detecting +0.10 F1 at effective n ≈ 875 (design effect 2.0), α=0.0125 → power > 0.99; floor ≥ 400 gold lines. H-PE-2: floor 60 eligible mask events/task/split; at null ≤ 0.05, the p < 0.001 criterion is met at ≥ 11/60; power ≥ 0.95 at true accuracy ≥ 0.30. H-PE-3a: floor 300 held-out entries; detect +0.08 balanced accuracy over permuted mean (sd ≈ 0.03) → power > 0.9. H-PE-3b/4b: ≥999 decoys, ≤10 proposals, ≥10 occurrences each — Holm-feasible by construction. H-PC-0: Uruk III test split ≈ 1,088 texts; floors trivially powered. **Floor rule (frozen):** if an eligible count at execution falls below its floor, that endpoint is reported "underpowered — no claim"; thresholds may narrow, never widen (freeze block, prereg §11).

---

## 11. Human-expert loop

A7 binds OBS headline claims by its terms; its principle — expert-proxy adjudication in development only; real named experts for headline claims — is adopted here as a registered condition because H-PE-3b/4b headline claims are category/role assignments requiring philological judgment. **Development:** internal philology-persona proxies only. **Headline E2 claims:** blind review by ≥2 named human specialists in proto-writing/Proto-Elamite under a rubric authored and frozen by the tribunal convener (not this designer). Documented candidate pool (from the Run 1 dossier §6, as evidence of feasibility, not commitment): Jacob Dahl (Oxford; CDLI PE digitization lead since 2012) and Kathryn Kelley (Uppsala; 2026 Cambridge Element). Blinding: experts receive each surviving proposal embedded among 3 registered decoy proposals without model provenance (H-OBS-2 pattern: judges never see which candidate is the pipeline's). Recruitment is the plan-§11 open decision; **no headline L4 claim is reportable without this review** — absent recruitment, surviving proposals are reported as "machine-screened candidates pending expert adjudication," one band lower in prominence.

---

## 12. Compute and team estimate

- **Compute:** symbolic corpora are tiny (PE ATF 508 KB; Uruk III 1.6 MB verified). CPU-dominant. GPU: 5 splits × 2 arms × model grid for the ≤20M-param transformer + ablations ≈ **order 10²  GPU-hours (frozen ceiling 200 GPU-hours)**; optional LLM proposal generation ≤ 2M tokens. No training run exceeds single-GPU scale.
- **Team:** ≈ **9 team-months** (~4–5 elapsed months at 2–3 FTE): data engineering + steward 1.5; parser + double-annotated gold subset 2.0; modeling 2.0; calibration arm 1.5; analysis/reporting/tribunal packaging 1.5; expert-loop coordination 0.5–1.0.

---

## 13. What a null result means (G9)

If the pipeline clears the H-PC-0 calibration floors but fails H-PE-1/2, the registered finding is: *distributional/structural inference that demonstrably works on proto-cuneiform (where the answer key exists) cannot recover even the accounting skeleton of Proto-Elamite from best-in-class sign-level data at 1,600–1,755-tablet scale* — an information-conditions bound on the most digitization-favorable shape-A system in the program (the falsifier: "the only system where the held-out protocol is executable today on licensed-open structured data"). If H-PE-1/2 pass but H-PE-3/4 fail, the finding is that PE's accounting *syntax* generalizes out-of-sample while its *semantics* beyond the published inventory does not — directly quantifying how much of the field's semantic knowledge is recoverable versus saturated, and setting the registered prior against future semantic claims made without new anchors. Both nulls are first-class deliverables (G9; plan §0: a rigorous null "is a success of the program"), publishable because every threshold, null, unit treatment, and search path was frozen before data contact — the failure mode excluded is exactly the discretionary-fit regime that SIGIL showed can "read" a meaningless corpus three incompatible ways (["On the Non-Specificity of Statistical Measures Used in Script Decipherment," arXiv 2608.02999](https://arxiv.org/abs/2608.02999)). If H-PC-0 floors fail, nothing about PE is concluded (pipeline defect; quarantine).

---

## 14. Residual degrees-of-freedom audit

| Potential discretion | Closed by |
|---|---|
| Which tablets count / dedup | §3 mechanical rules, hashed manifest, steward-only |
| Sign inventory choice | A19 dual-scheme S1/S2, both always reported |
| Numerical-system assignment | Frozen per-N-sign lookup (§3.3), deposited pre-contact |
| Split membership / seeds | Frozen seeds, tablet-level, steward-only |
| Gold labels | Mechanical arithmetic derivation + double-annotated audit subset |
| Model/hyperparameter search | Enumerated grids, dev-only selection, weights hashed pre-test |
| Which proposals scored | ≤10, highest-occurrence-first rule |
| Null construction | Registered samplers + seeds, structure-preserving |
| Success thresholds | Frozen here; narrow-only rule |
| Post-hoc salvage of failures | A1 conjunctive logic; deviation = protocol violation |
| Claim inflation (phonetic/language/E3) | §1 prohibition list + lexical filter + audit agent + A18 phrasing |
| Self-adjudication | G2/G7: disjoint scoring agents; tribunal adjudication; convener-authored expert rubric |

**Compute estimate:** Order 10^2 GPU-hours (frozen ceiling 200 GPU-hours; single-GPU scale — corpora are 508KB/1.6MB symbolic text; CPU-dominant classical models plus a ≤20M-param from-scratch transformer across 5 splits × 2 arms × frozen grids; optional LLM proposal generation ≤2M tokens under sign-code randomization). Team: ~9 team-months over ~4–5 elapsed months at 2–3 FTE (data/steward 1.5, parser+gold annotation 2.0, modeling 2.0, calibration arm 1.5, analysis/reporting 1.5, expert-loop coordination 0.5–1.0).

**Null result meaning:** The calibration arm makes the null diagnostic rather than ambiguous. If H-PC-0 floors pass but H-PE-1/2 fail: distributional inference that demonstrably works on proto-cuneiform cannot recover even the accounting skeleton of Proto-Elamite from best-in-class licensed-open sign-level data at 1,600–1,755-tablet scale — an information-conditions bound on the single most executable held-out protocol in the program (falsifier: "the only system where the held-out protocol is executable today on licensed-open structured data"). If H-PE-1/2 pass but H-PE-3/4 fail: Proto-Elamite accounting syntax generalizes out-of-sample but semantics beyond the published Englund/Kelley inventory does not — quantifying saturation of the field's semantic knowledge and becoming the registered prior against future semantic claims lacking new anchors. If H-PC-0 fails: pipeline defect, PE results quarantined, no PE conclusion. All three outcomes are publishable first-class deliverables under G9 because every threshold, unit treatment, null, and search path is frozen pre-contact, excluding the discretionary-fit regime SIGIL (arXiv 2608.02999) showed can produce three incompatible "readings" of a meaningless corpus.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (deposit to tribunal record before first data contact; items may narrow, never widen). A.1 DATASET VERSIONS/FINGERPRINTS: CDLI live export, period facet "Proto-Elamite (ca. 3100-2900 BC)" — audited 2026-08-11: 1,755 entries / 1,597 ATF texts / 508KB (provisional fingerprint); Uruk IV facet: 1,892/1,836; Uruk III facet: 5,921/5,440 (1.6MB verified); SHA-256 of each acquired ATF+catalogue file computed by the data steward at acquisition (window 2026-08-15→31) and deposited before scoring; reconciliation tolerance ±3% vs audited counts, else halt; cdli-gh/proto-elamite_data pinned by commit hash at acquisition (CC-BY-4.0). A.2 UNIT TREATMENTS (A19): Scheme S1 = CDLI/Meriggi M-codes as encoded (variant suffixes distinct); Scheme S2 = deterministic variant-merge lookup table (hashed) built from ATF sign list + EPS file inventory; corpus-count universe reported as 1,600–1,755 raw alongside the deduplicated analysis universe; frozen per-N-sign → numerical-system lookup + conversion table (Englund 2004 six systems: sexagesimal/decimal/bisexagesimal+derivatives/grain-capacity+subdivisions/area) — mechanical `ambiguous` labeling, no scoring-time discretion. A.3 SPLITS: tablet-level 70/10/20, stratified by provenience (Susa/non-Susa) and completeness tercile; 5 splits, seeds {3100, 2900, 1755, 1597, 20260811}; dedup rules: catalogue join/composite merge, exact-ATF collapse, Jaccard≥0.8 sign-3-gram (S2) same-split forcing; manifests hashed. A.4 CONTROL PANELS: H-PE-2 null = frequency-matched attested-notation sampler, ≥1,000 draws/split, seeded; H-PE-3a null = within-tablet structure-preserving system-label permutation, ≥1,000; H-PE-3b/4b decoys = ≥999 frequency-matched category/role assignments from frozen inventory K (compiled solely from Englund 2004 englund2004c.pdf and Kelley Cambridge Element, per-entry source loci, hashed); ≤10 proposals per endpoint, highest-occurrence-first selection; ≥10-occurrence floor per proposal; expert-review panels = each surviving proposal + 3 registered decoy proposals, provenance-blind. A.5 TOLERANCES: quantity match = exact after canonical fraction representation per frozen system grammar (value tolerance exact); damage handling = mechanical exclusion on ATF damage flags; parser gold vs 60-tablet double-annotated subset agreement ≥0.90 (κ reported) else halt-and-repair before scoring; prospective-subset equivalence = within 10 points of held-out mean (deficit reported as leakage evidence, never grace-banded). A.6 THRESHOLDS (conjunctive per A1): H-PE-1 macro-F1 ≥0.80 AND ≥baseline+0.10 with cluster-bootstrap 95% CI lower bound above baseline; H-PE-2 Task B ≥0.90 AND Task A ≥0.75, each empirical p<0.001; H-PE-3a p<0.01 Holm under both S1 and S2; H-PE-3b/4b empirical p≤0.001, Holm at family α=0.01, every-context consistency; H-PC-0 floors macro-F1 ≥0.85 and Task-B ≥0.95 (failure quarantines all PE results); H-PHA-1 extension: any disc total/subtotal detection or category/role assignment at reporting confidence = pipeline failure. A.7 POWER ANALYSIS (frozen assumptions): 1,597 ATF texts, ~10,000 lines (Englund 2004), 88% dedup retention assumption; test split ≈280 tablets/≈1,750 lines; H-PE-1 power>0.99 for +0.10 F1 at effective n≈875 (design effect 2.0, α=0.0125), floor 400 gold lines; H-PE-2 floor 60 mask events/task/split, p<0.001 met at ≥11/60 under null ≤0.05, power ≥0.95 at true ≥0.30; H-PE-3a floor 300 entries, power>0.9 for +0.08 balanced accuracy (permuted sd≈0.03); H-PE-4b provenience covariates exploratory unless non-Susa test docs ≥30; floor breach → "underpowered — no claim." A.8 MODEL SPACES: CRF/HMM, gradient-boosted trees, from-scratch transformer ≤20M params; enumerated hyperparameter grids; dev-only selection; weights hashed pre-test; no pretrained weights in primary models; LLM generator (optional) only under bijective M-/N-code randomization, ≥2 independent remappings concordance required. A.9 CUTOFFS/BLINDING: temporal cutoff 2026-08-11; sealed-sources list (per-tablet interpretive literature) with audited retrieval logs; role assignments (steward/modeling/generator/scorer/Phaistos-auditor) recorded; one-shot test application per split per endpoint; all runs, restarts, and null draws logged per G5.

# Linear A (limit case, shadow-validation precondition)

# Run 3 Experiment Design — Linear A: Family-Affinity Ranking under Mandatory Shadow-Validation Precondition

**Design ID:** R3-DES-LNA-v1.0 · **Date:** 2026-08-11 · **Status:** deposited before any data contact by scoring agents (A17)
**Executes:** H-LNA-0, H-LNA-1 (frozen in `/home/claude/work/run2-preregistration-FROZEN.md` §2), with H-ONO-1 (§9) instantiated as the A4 external-consequence instrument and H-PHA-1 (§10) coupled per A16.
**Binding documents:** `run2-preregistration-FROZEN.md` (canonical thresholds — this design copies them and may narrow, never widen); `tribunal-record-and-prereg-amendments-v1_1.md` (A1–A19; adjudicated E-classes); `undeciphered-research-plan-v2.md` §§2–5, 9; `run2-audits-methods-patch.md` (audited data reality); `run2-checkpoint2-matrix.md` (Linear A falsification verdict: WEAKENED).
**Governance rule honored:** this designer does not author adjudication. Every success/disconfirmation criterion below is a verbatim reference to the frozen preregistration and its amendment appendix; the pre-scoring appendix (§14) only pins operational values within the frozen envelope.

---

## 1. Adjudicated E-class bands and what this design is licensed to claim

Per the Checkpoint 2 matrix as amended (tribunal record §I.2 note: systems not listed retain matrix status subject to A18 claim-band conversion), the Linear A adjudicated status is: **"E2, structural/numeral band only; effectively E1 for phonetic/family claims pending H-LNA-0"** (`run2-checkpoint2-matrix.md`, Linear A row and falsification verdict, citing <https://en.wikipedia.org/wiki/Linear_A>, <https://aclanthology.org/2024.cl-2.7.pdf>, <https://www.mdpi.com/2078-2489/15/2/73>, <https://cris.unibo.it/retrieve/7656690e-fe79-4b54-948b-fabce5723819/frai-8-1581129.pdf>).

Claim-band matrix for this design (A18 format — E-classes attach to claims, not the system):

| Claim band | Ladder level | Highest licensed E-class | Licensing route |
|---|---|---|---|
| Shadow-method validation ("the method can/cannot rank families at LNA conditions") | L1–L3, L5 instrumental | **E1** | H-LNA-0 as written |
| Incidental structural/numeral findings on the real corpus (segmentation stats, sign co-occurrence, numeral structure) | L1–L3 | **E2** (adjudicated structural/numeral band) | reported descriptively; no new headline structural claims are a target of this design |
| Real-corpus family **ranking** (closed tournament) | L5-adjacent | **E1** | A4: "A winning family in the closed tournament is an E1 ranking result" |
| Real-corpus family **claim** ("Linear A shows affinity with family X") | L5/L6 interface | **E2** (ceiling) | H-LNA-1 pass **and** A4: one pre-designated G3-admissible prediction confirmed, adjudicated under H-ONO-1 + cross-model tribunal (G7) |
| Phonetic value tables produced inside the method | L5 | **E1 artifacts only** — never published as readings | G1; tribunal band |
| Lexical correspondences, translations | L6–L7 | **barred** (L7 prohibited program-wide, G2; L6 above adjudicated band) | — |

**Precondition structure (explicit, binding):** No agent contacts the real Linear A corpus with the affinity method until (i) the shadow-world battery of §3 is built and red-teamed, (ii) H-LNA-0 is scored by the disjoint scoring team, and (iii) the H-LNA-0 pass is verified against the frozen thresholds by the falsification agent and logged in the tribunal record. If H-LNA-0 fails, **H-LNA-1 is cancelled for Run 3** (frozen disconfirmation clause) and the real corpus is never scored. Plan v2 §7: "shadow-world validation mandatory before any real-corpus claim" (<file: undeciphered-research-plan-v2.md>).

---

## 2. Data acquisition plan (audited reality, not papers' claims)

**G8 declaration.** Data basis: (iii) transliterations/sign-code sequences + (iv) structured relational data. No image-based paleography is attempted; results do not transfer to image bases without a registered bridging test (G8).

### 2.1 The two corpus variants (both mandatory per H-LNA-1 stability clause (a))

**Variant U1 — SigLA snapshot.** Audit finding (`run2-audits-methods-patch.md`, SigLA row, 2/5): live web app, CC BY-NC-SA 4.0 stated verbatim in the site footer ("Dataset and drawings are available under the CC BY-NC-SA 4.0 license," <https://sigla.phis.me/>); no documented export; the entire dataset ships client-side as `database.js` (2,516,528 bytes verified by download in the audit and re-verified byte-identical this session) containing `/* Signs */` and `/* Data */` sections as custom escaped-octal-encoded JS strings consumed by an OCaml/js_of_ocaml app; changelog live to June 2026; Aug 24 2021 entry states "all tablets from GORILA are now present in SigLA" (<https://sigla.phis.me/about.html>). Acquisition steps: (1) snapshot `database.js` on the freeze date; SHA-256 deposited (§14 — **obtained this session**); (2) write and publish a documented decoder for the escaped-octal serialization (permitted for non-commercial research under CC BY-NC-SA with attribution and share-alike; decoder released under the same license); (3) validate decoded document/sign counts against the census ranges (1,370 documents / 7,362–7,396 tokens / 97 signs, Braović et al. 2024, "Computational Linguistics 50(2)," <https://aclanthology.org/2024.cl-2.7.pdf>); deviations logged, not silently reconciled.

**Variant U2 — lineara.xyz snapshot.** Audit finding (4/5): best available bulk-downloadable structured Linear A corpus, but unofficial: `LinearAInscriptions.js` at <https://raw.githubusercontent.com/mwenge/lineara.xyz/master/LinearAInscriptions.js> (HTTP 200 verified in audit and this session), a JS array of JSON objects per document (fields: name, image, tracingImage, parsedInscription in Unicode Linear A, transcription, transliteratedWords, translatedWords), built from George Douros's GORILA tabulation spreadsheet with images cropped from EFA-copyrighted CEFAEL GORILA scans; **no LICENSE file (404 at repo root)** (<https://lineara.xyz/>, <https://cefael.efa.gr/>). New observation this session: the file header carries an SQLite-style "author disclaims copyright to this source code" blessing — this covers the JS code at most, **not** the Douros-derived transcription data or EFA images; the audit's legal caution stands. **License-caution handling (frozen):** U2 is used internally for analysis only; the corpus file, images, and any substantial excerpt are never redistributed; published outputs reference documents by GORILA sigla and report only derived statistics; an action item (non-blocking) is to request license clarification from the maintainer. Snapshot hashed this session (§14); this session counted **1,722 top-level inscription records** — more than either census figure, presumably faces/sides/non-GORILA additions; see A19 treatment below.

**Concordance.** A frozen mapping table SigLA-ID ↔ lineara.xyz record name ↔ GORILA siglum is built before method contact; documents present in one variant only are listed in a discrepancy log and reported. Primary analyses run on each variant as-is (the frozen clause says both variants must be run, not their intersection).

**Images and 3D:** not acquired (out of basis). **Younger's KU pages:** NXDOMAIN-dead per audit — not used, not cited as live. **Petrolito et al. 2015 corpus:** no data artifact exists per audit (0/5, <https://aclanthology.org/W15-3715/>) — not used.

### 2.2 Candidate/decoy comparison lexicons (acquisition list with audited-status flags)

Each panel language needs a machine-readable comparison lexicon (target size N_lex = 2,000 entries; hard floor 800; below floor → ineligible, reported). Registered candidates (prereg H-LNA-1): Anatolian/Luwian; Northwest Semitic (Ugaritic/Phoenician); Tyrsenian (Etruscan + Lemnian); Hurrian. Sources to pin (hash + version deposited before the appendix is declared complete, per A17):
- Ugaritic/Hebrew and Linear B/Greek lexicons: NeuroDecipher release (<https://github.com/j-luo93/NeuroDecipher>; Linear B side from the Tselentis lexicon, per `run2-audits-methods-patch.md` §4).
- Etruscan: Burman digital concordance, Zenodo DOI 10.5281/zenodo.13784774 v1.0.2, public domain (found by the Etruscan falsifier, `run2-checkpoint2-matrix.md`; <https://zenodo.org/records/13784774>) + published glossaries, provenance documented. **Lemnian falls below the 800-entry floor and is carried as flagged supplementary comparanda only** — the Tyrsenian candidate lexicon is operationally Etruscan; this limit is stated in every report of the Tyrsenian result.
- Luwian, Hittite: no bulk-download license was audited this program — acquisition risk. Route: hand-keyed lexica from published dictionaries with per-entry provenance, or negotiated export; the appendix is incomplete (A17 blocks data contact) until these artifacts are hashed.
- Hurrian: no machine-readable lexicon audited. Fallback (frozen): hand-keyed from Laroche, *Glossaire de la langue hourrite* + published Mitanni-letter glossaries, per-entry provenance logged. Same A17 blocking rule.
- Shadow-world source corpora: CDLI live exports for Sumerian Ur III and Old Assyrian (audit: CDLI 5/5, verified end-to-end ATF export, <https://cdli.earth/>); Linear B tablets (DĀMOS/LiBER; to be audited and pinned); Ugaritic economic texts; Hittite/Luwian corpora (Hethitologie-Portal; to be pinned); Demotic/Coptic (TLA/Trismegistos; to be pinned); Old Novgorod birchbark corpus (gramoty.ru; to be pinned). Every one of these is subject to the same rule: **no shadow world is built from a source whose artifact is not yet hashed in the appendix deposit.**

### 2.3 A19 unit-mapping freeze (Linear A contested units)

Registered unit treatments (results reported under all where they disagree; divergent verdicts → no claim, per H-LNA-1 disconfirmation):
- **UT-1 corpus universe:** U1 (Braović/SigLA: 1,370 docs, 7,362–7,396 sign tokens, 97 signs) vs U2 (GORILA-based: ~1,427 artefacts, ~7,150 signs; Nepal & Perono Cacciafoco 2024, <https://www.mdpi.com/2078-2489/15/2/73>). New A19 registry entry deposited with this design: **lineara.xyz ships 1,722 records vs 1,370 documents vs ~1,427 artefacts** — record ≠ document ≠ artefact; the concordance table is the frozen mapping.
- **UT-2 sign inventory:** GORILA/AB standard signary; composite/ligature signs under two frozen treatments — atomic (primary) and decomposed (secondary); claims must hold under both (a narrowing).
- **UT-3 token counting:** sign tokens (numerals and klasmatograms excluded from affinity-method input corpus-wide; see §7 P2 for why numerals are sealed content).

---

## 3. Shadow-world generator specification (program centerpiece, plan v2 §3)

### 3.1 Frozen information-condition parameter block

Every shadow world is a real, known language degraded to Linear A's audited information conditions (prereg H-LNA-0 conditions, operationalized):

| Parameter | Value (frozen) | Tolerance |
|---|---|---|
| Sign-token count | drawn per-world from [7,150, 7,396] (both census endpoints, A19) | exact (hard window) |
| Unique sign inventory | 97 target | 92–97 realized |
| Document count | drawn from [1,370, 1,427] | exact |
| Document-length distribution | matched to the empirical histogram of the frozen real snapshot (per variant) | KS distance ≤ 0.05 |
| Genre mix | ≈97% administrative list documents (heading + entries [sign-group + logogram-slot + numeral] + total line); ≈3% recurring votive formula (mirrors ~41 libation-formula documents of ~1,000 recovered, dossier §2, <https://en.wikipedia.org/wiki/Linear_A>) | ±2 pp |
| Numerals | decimal notation isomorphic to Linear A's; totals arithmetically consistent; numeral values redrawn (anti-memorization); numerals stripped from method input as in the real run | — |
| Word boundaries | divider marks retained at the real corpus's measured divider rate | ±2 pp |
| Damage | lacuna/illegible fraction and truncation matched to measured real-corpus damage fraction | ±2 pp |
| Partial sign-value priors | coverage fraction c = the real prior-table coverage (measured from the frozen per-sign provenance table, §14); injected error rate ε ∈ {5%, 15%} (two sensitivity levels, both run — true retrojection error unknown, so it is a design parameter, not an empirical claim) | c ± 2 pp |
| Bilingual | none | — |
| Glyph identity | every sign mapped to a novel random ID; no Linear A/B/real-script codepoints (G6; prereg control "shadow glyph randomization removes training contamination") | — |

### 3.2 Generator pipeline (Team G; disjoint from method Team M)

1. **Source ingestion:** admin-genre corpus of the hidden language H, phonologically transcribed (documented transcription standard per language).
2. **Syllabary induction:** frozen syllabification algorithm builds a CV(+restricted CVC) syllabary; frozen *underspecification operators* (merge voicing/aspiration series, merge liquids, delete coda consonants, merge vowel length) applied in a fixed order until inventory ≤ 97 — mirroring the known underspecification of Aegean syllabaries. The operator sequence per world is logged and is part of the answer key.
3. **Allography layer (L1 test):** each grapheme receives 1–4 allograph IDs with Zipf-distributed usage; allograph key held by custodian.
4. **Document assembly:** entries resampled and reordered, numeral values redrawn under arithmetic consistency, names/toponyms replaced by frequency-matched samples from the hidden language's onomasticon — this defeats memorization of famous source documents (e.g., recognizable Linear B tablet structure) while preserving language statistics.
5. **Damage model:** lacunae + truncation to the frozen fractions.
6. **Emission:** per world — shadow corpus (sign codes), prior table (coverage c, error ε; which priors are wrong is custodian-held), panel comparison lexicons under the identical transformation budget, and a manifest hash.

**Custodianship:** answer keys (language identity, glyph map, operator log, error-injected priors) are held by a non-scoring custodian agent (frozen prereg control). Team M and Team S never see keys until scoring is complete and deposited.

### 3.3 Concrete world roster (frozen; A3 panels in §3.4)

Six relative-present worlds spanning the genealogical distances the real candidate panel spans, plus three no-relative worlds (frozen prereg threshold clause):

| World | Hidden language H (source corpus) | True relative R (panel member) | Approx. divergence | Rationale |
|---|---|---|---|---|
| W1 | Mycenaean Greek (Linear B admin tablets, DĀMOS/LiBER) | archaic/epic Greek lexicon | ~0.5 ky | best genre match in existence; close-relative regime |
| W2 | Ugaritic (economic/administrative texts) | Biblical Hebrew | ~0.5–1 ky | NW Semitic sister — mirrors the NW Semitic candidate |
| W3 | Hittite (court inventories/land grants) | Cuneiform Luwian | ~1–1.5 ky | branch-internal Anatolian — the documented hard case (Tamburini 2025: 47.5±1.67% on Luwian/Hittite at full information, "Frontiers in AI," <https://cris.unibo.it/retrieve/7656690e-fe79-4b54-948b-fabce5723819/frai-8-1581129.pdf>) |
| W4 | Old Assyrian Akkadian (kārum trade accounts, CDLI) | Ugaritic | ~2 ky+ | deep-relative regime (East vs West Semitic) |
| W5 | Demotic Egyptian (account ostraca) | Coptic | ~1 ky | later-stage-of-lineage regime; admin genre |
| W6 | Old Novgorod dialect (birchbark admin/debt notes) | Old Church Slavonic | ~0.5 ky | ~1,100 short real admin documents — closest natural scale match |
| N1 | Sumerian (Ur III admin, CDLI) | **none** | — | isolate; panel includes heavy-contact unrelated Akkadian — the A3 stress decoy |
| N2 | Achaemenid Elamite (Persepolis Fortification-style admin) | **none** | — | isolate-grade; contact decoys Old Persian, Akkadian |
| N3 | Basque (early administrative/notarial records, syllabary-encoded) | **none** | — | canonical isolate; contact decoys Latin/Romance |

W2/W4 both Semitic and W1/W5 lineage-stage cases are deliberate: the method must not be able to pass by exploiting one family's peculiarities; the falsification agent checks per-world results for family-driven artifacts.

### 3.4 Decoy panels (A3 — frozen composition and matching rules)

A3 (binding): decoys matched to the hidden relative on **genealogical distance, contact history, phonotactic compatibility, corpus genre, and reconstruction depth** — "not merely 'unrelated.'" Panel composition frozen before any shadow world is built — this section is that freeze.

Matching operationalization (checked by red team, §3.5):
- **Genealogical:** no decoy has an accepted genetic relationship to H or to R at consensus phylogeny (decoys may be related to each other). Phylum-level relatives excluded (e.g., Egyptian excluded from Semitic-hidden panels — Afroasiatic).
- **Contact:** every panel contains ≥2 decoys with documented historical contact with H's speech community (the hard confound: contact mimics affinity).
- **Phonotactics:** each decoy's lexicon encodability in the world's 97-sign syllabary within ±10 pp of R's encodability under the same underspecification operators.
- **Genre:** decoy comparison lexicons drawn from admin/economic corpora where they exist; otherwise lexicon-wide with a genre flag reported.
- **Reconstruction depth:** decoy attestation within ±800 y of R's attestation date, or the deviation documented in the panel manifest.

Frozen panels (R in bold; ≥7 decoys each; all lexicons truncated to the identical budget):

- **W1** (H = Mycenaean Greek): **archaic Greek**; Ugaritic, Akkadian, Hurrian, Elamite, Sumerian, Old Tamil, Basque. (Contact decoys: Ugaritic, Akkadian.)
- **W2** (H = Ugaritic): **Biblical Hebrew**; Hittite, Cuneiform Luwian, Hurrian, Elamite, Sumerian, archaic Greek, Old Tamil. (Contact: Hittite, Hurrian, Greek.)
- **W3** (H = Hittite): **Cuneiform Luwian**; Ugaritic, Akkadian, Hurrian, Hattic, Elamite, Sumerian, Basque. (Contact: Hattic, Hurrian, Akkadian — Hattic is the signature A3 decoy: massive contact, no genetic relation.)
- **W4** (H = Old Assyrian): **Ugaritic**; Hittite, Luwian, Hurrian, Elamite, Sumerian, archaic Greek, Old Tamil, Basque. (Contact: Sumerian, Hurrian, Elamite, Hittite.)
- **W5** (H = Demotic): **Coptic**; archaic Greek, Hittite, Luwian, Hurrian, Elamite, Sumerian, Old Tamil. (Contact: Greek — the crucial confound for Demotic.)
- **W6** (H = Old Novgorod): **Old Church Slavonic**; Old Turkic, medieval Finnic, Hungarian, Old Georgian, Old Tamil, Basque, Akkadian. (Contact: Old Turkic, Finnic. Note: OCS is Slavic and hence related; that is the point — it is R. Finnic/Turkic are the contact decoys.)
- **N1** (H = Sumerian): Akkadian, Hittite, Hurrian, Elamite, archaic Greek, Ugaritic, Old Tamil, Basque — no relative exists.
- **N2** (H = Elamite): Akkadian, Old Persian, Sumerian, Hurrian, Ugaritic, archaic Greek, Old Tamil, Basque. (Dravidian note: the Elamo-Dravidian hypothesis is not consensus; Old Tamil's presence is deliberate and its result is reported, but N2's pass/fail is computed excluding Old Tamil to avoid adjudicating a live fringe hypothesis inside a control; both computations reported.)
- **N3** (H = Basque): Latin, Spanish-Romance, Celtiberian-Celtic lexicon, archaic Greek, Ugaritic, Old Georgian, Old Tamil, Hungarian. (Contact: Latin/Romance, Celtic.)

If any listed lexicon fails the 800-entry floor at acquisition, the frozen substitution rule applies: replace with the next language in the frozen reserve list {Old Georgian, Old Japanese, Middle Egyptian (only where phylum-legal), Hungarian, Quechua (deliberately implausible reserve)} that satisfies all five A3 axes; every substitution logged in the appendix deposit before H-LNA-0 scoring.

### 3.5 Red-team protocol (voids batches, per G4/H-IND-1 analog and plan v2 §3)

A disjoint red team receives the generator spec and emitted worlds **without keys** and attacks: (i) a decoy secretly related to H or R, or contact-loading exceeding the A3 envelope; (ii) information-condition mismatch outside §3.1 tolerances; (iii) leakage — glyph map recoverable from document-structure fingerprints of famous source corpora, prior table more informative than (c, ε) declares, or source text reconstructable; (iv) generator "language-shapedness" defects in the assembly step. Any confirmed attack **voids the world batch**; regenerated worlds are re-red-teamed. Red-team findings are deposited whether or not exploited.

### 3.6 Blinding and answer-key discipline

The scoring team receives worlds labeled by opaque IDs, mixed with the real-corpus run order at H-LNA-1 time and with the Phaistos control (§9), under the A16 rule: identical reporting/confidence policy across control and targets, pipeline not told which target is which where module design allows; report-rate and confidence-distribution divergence across targets is itself a failed control (A16).

---

## 4. Method specification (M-LNA — implementable by a competent ML team)

**Design principle:** two independent method arms whose published precursors are E1-verified in the method-evidence base, combined by a frozen rule; entirely deterministic/classical or trained-from-scratch — **no pretrained LLM touches shadow or real corpus data at any stage** (G6; Linear A transliterations and every published "decipherment" are in LLM training data).

- **Stage 1 — normalization (L1):** decode snapshot → sign-code sequences under UT-1/UT-2/UT-3 treatments; allograph normalization in shadow worlds is part of the task (the method must collapse allographs; algorithm frozen: distributional clustering with positional context, following the Sign2Vec_d positional-context precedent, "Unsupervised deep learning supports reclassification of Bronze age cypriot writing system," <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0269544>).
- **Stage 2 — sign-value priors:** the per-sign prior table (§14) assigns each sign a value class: A = secure Linear B homomorph (fixed), B = probable (resampled: 10% swap-out per resample), C = conjectural (resampled uniformly over admissible values). ≥100 resamples per the frozen H-LNA-1 stability clause (b).
- **Stage 3 — segmentation (L2), three registered schemes** (frozen clause (c)): S1 = divider-based (GORILA word dividers); S2 = unsegmented with joint segmentation in the Luo-2021 style ("Deciphering Undersegmented Ancient Scripts Using Phonetic Prior," <https://aclanthology.org/2021.tacl-1.5.pdf>), adapted from alphabets to syllabaries via a syllable-decomposition layer; S3 = entry-structural (tablet line/entry parsing; logogram+numeral slots stripped, residual sign-groups as units).
- **Stage 4 — affinity scoring, two arms:**
  - **Arm A (CSA):** coupled simulated annealing over constrained k-permutation sign→value mappings (nulls, one-to-many, many-to-one allowed), energy coupling mapping quality and lexicon match by wildcard edit distance + modified linear sum assignment, 16 parallel annealers — the Tamburini 2023/2025 architecture (<https://aclanthology.org/2023.cawl-1.10/>; <https://cris.unibo.it/retrieve/7656690e-fe79-4b54-948b-fabce5723819/frai-8-1581129.pdf>), with priors as palaeographic constraints. **Restart discipline (frozen):** exactly 4 independent runs per configuration, mean±sd reported, no best-of-N selection — per the method-evidence finding that best-of-restart selection is epistemically leaky (BK13 18%→90% spread; objective score and accuracy decouple; `run2-audits-methods-patch.md` cross-cutting finding 4).
  - **Arm B (phonetic-prior neural matching):** Luo-2021-style model with universal phonetic feature embeddings on the candidate side (pretrained only on modern phoneme-inventory data, never on ancient corpora); outputs cognate-retrieval confidence-coverage curves; 4 runs, mean±sd.
- **Stage 5 — combined affinity score:** per candidate language, the mean of the two arms' within-panel z-scored statistics (Arm A: negative energy; Arm B: confidence-coverage AUC); weights 50/50, frozen now. Ranking = descending combined score. **H-LNA-0 metric = rank of R** (frozen).
- **Stage 6 — significance machinery (H-LNA-1 and no-relative worlds):** empirical p by ≥1,000 permutations (frozen floor): scrambled sign-value assignments consistent with the same prior-independence constraints + lexicon permutations preserving entry length/frequency profiles. **Budget symmetry rule (frozen):** because full-budget re-annealing 1,000× is infeasible, the permutation comparison is computed in a reduced-budget regime (1/10 anneal budget) applied **identically** to the observed statistic and to every permutation replicate — statistic/null symmetry is preserved; full-budget scores are used only for point rankings. Holm correction across the 4 candidates (G5).
- **Code freeze:** the complete method (both arms, aggregation, permutation machinery), its dependencies, and seeds are hashed and deposited **before the first shadow world is scored**; any post-hoc change voids all subsequent scores back to the change point (protocol violation per the freeze block deviation rule).
- **Team separation (G2):** Team G (generator) ∥ Team M (method) ∥ Team S (scoring execution) ∥ custodian ∥ red team ∥ falsification agent. No agent occupies two roles.

---

## 5. Preregistered success/disconfirmation criteria (verbatim references — not restated as new text)

**H-LNA-0 (E1, precondition)** — thresholds as frozen: top-1 recovery of the true relative in **≥5 of 6** relative-present shadow worlds; AND in **≥3 no-relative worlds**, no control crosses the H-LNA-1 significance threshold in more than **1 of 3** worlds. Controls: shadow glyph randomization (G6); answer key with non-scoring agent; restart counts logged (G5). Disconfirmation: either criterion fails → **H-LNA-1 cancelled for Run 3**; registered finding: "family ranking is not validated at Linear A information conditions." (All verbatim from `run2-preregistration-FROZEN.md` §2, as amended by A3 — the §3.4 panels discharge the A3 matching duty.)

**H-LNA-1 (conditional; tournament = E1 per A4)** — thresholds as frozen: candidate max-score empirical p < 0.01 (Holm-corrected across candidates) vs ≥7 unrelated controls, ≥1,000 permutations; AND stability under (a) both corpus variants (U1/U2), (b) ≥100 sign-value resamples, (c) ≥3 segmentation schemes. Candidate panel as registered: Anatolian/Luwian, NW Semitic (Ugaritic/Phoenician), Tyrsenian (Etruscan + Lemnian), Hurrian; Semitic stays in despite prior negatives (frozen clause). Unrelated controls: chosen by a **blind agent** (frozen clause) — this design supplies only the eligibility pool and draw procedure (§14 item 6), not the panel itself. Disconfirmation: no candidate clears controls, or any instability across (a)–(c), or a deliberately implausible control wins → H0 stands; registered program prior: "Linear A affinity claims at current information conditions are unsupported."

**A4 (binding rewrite of the E2 route):** the tournament winner is an **E1 ranking result**; E2 requires a pre-designated G3-admissible independent prediction, checked. §7 designates the prediction types now, as A4 requires.

**A1 analog note:** no "promising near-miss" band exists anywhere in this design; every zone between full threshold satisfaction and disconfirmation is a failure (tribunal record A1 establishes the program-wide reading).

---

## 6. Multiplicity, logging, and anti-restart discipline (G5)

Every world scored, every configuration (variant × treatment × scheme × resample × run), every permutation batch, and every panel draw is logged with seeds to an append-only run ledger; the Holm denominator for H-LNA-1 is the count of registered candidate tests actually run; no unregistered panel, feature, or aggregation may be scored (protocol violation). Restart budget is structurally fixed at 4 runs/configuration (§4); the run ledger is the auditable restart log the frozen H-LNA-0 controls demand (Tamburini restart-exploitation guard, "On automatic decipherment of lost ancient scripts…," DOI 10.3389/frai.2025.1581129).

---

## 7. E2 escalation: pre-designated prediction types (A4) instantiated through H-ONO-1

Candidate prediction types designated **now**, before any tournament runs (A4 requirement). The designated E2 instrument is P1; P2/P3 are registered secondaries that license nothing above E1 alone but are run and reported.

**P1 — Onomastic prediction (PRIMARY; the E2 instrument).** If a family wins the tournament, its refined value hypotheses must identify ≥1 Linear A sign-group as a name/toponym **independently attested outside the Linear A→Linear B retrojection chain**. Admissible attestation sources (closed set, frozen): (a) Egyptian New Kingdom Aegean toponym lists (Kom el-Hetan statue base); (b) Near Eastern archival references to Aegean names (Mari/Amarna Kaptara/Keftiu class); (c) a custodian-sealed list of Linear B onomastic items excluded from all prior construction and training material. **Circularity guard (falsifier-driven):** the Checkpoint 2 falsifier showed the classic toponym check is circular — values retrojected from Linear B regenerate Linear B-like toponyms, "near-zero bits" (`run2-checkpoint2-matrix.md`, Linear A verdict). Therefore P1 scores **only** sign-groups whose value assignments came from tournament refinement (class B/C signs, §4 Stage 2) and only against targets sealed away from every anchor and prior (H-ONO-1 element 3: sign values learned independently of the target names). Full H-ONO-1 registration is mandatory before scoring: closed candidate name set; transformation cost budget; value provenance; matching score; both nulls (≥999 decoy names, ≥999 scrambled value assignments); p < 0.005 on both, Holm across all onomastic claims; plus one G3-admissible corollary checked. All thresholds are H-ONO-1's frozen text, not this design's.

**P2 — Numerical/metrological prediction (secondary).** The winning family's morphological analysis predicts which sign-group slots are quantity-bearing modifiers vs personnel/commodity heads; checked against KU-RO/klasmatogram arithmetic (numeral values are stripped from all method input corpus-wide, §2.3 UT-3, and their values in a custodian-held document list are sealed) — G3-admissible: numerical quantities. Scoring: predictions deposited (hashed) before unsealing; exact agreement rule and decoy-assignment null (≥999) frozen in the appendix deposit.

**P3 — Provenance prediction (secondary).** Family-conditional orthographic-variant clustering predicts document provenance (site) on custodian-held metadata never supplied to the method — G3-admissible: provenance. Same deposit-then-unseal protocol.

**Adjudication of P1–P3:** executed by Team S, verified by the falsification agent, and — for the headline E2 claim — reviewed by the cross-model tribunal (G7). This designer authors none of it.

---

## 8. Contamination controls (G6)

1. **Shadow phase:** glyph randomization (frozen control); numeral redraw + entry resampling + onomasticon replacement (§3.2 step 4) so that no famous source document survives as a recognizable template; source-corpus manifests hashed; red-team leakage attack (§3.5).
2. **Method composition:** no pretrained LLM in any data-touching path (shadow or real); universal phonetic embeddings pretrained on modern phoneme inventories only; all trainable components trained from scratch inside the pipeline.
3. **Real phase:** Linear A transliterations, SigLA, lineara.xyz, and the entire claim literature (Owens, La Marle, Semitic/Tyrsenian proposals — dossier §3/§6) are presumed present in any LLM training set; hence rule 2, and hence no agent may consult generative-model outputs about Linear A during scoring (logged attestation).
4. **Prospective mini-instrument:** SigLA is still ingesting tablets (changelog entries June 2026, audit; <https://sigla.phis.me/about.html>). Documents ingested after the snapshot date form a small prospective set; the winning configuration's descriptive statistics on it are reported (registered as descriptive only — no threshold attaches; a contamination-resistant sanity channel per G6's preference for post-cutoff material).
5. **Cross-variant integrity:** U1/U2 divergence beyond the concordance's known differences triggers a data-integrity halt, not silent reconciliation.

---

## 9. Phaistos negative-control coupling (H-PHA-1, A16)

The full M-LNA module runs on the Phaistos Disc alongside (not after) the real-corpus run, with no special-casing and under the A16 identical frozen reporting/confidence policy; where module design allows, the scoring team is not told which input is the control. A significant affinity ranking on the disc under the H-LNA-1 procedure is **pipeline failure** (H-PHA-1 condition 1): all concurrent LNA results are quarantined pending root-cause analysis and re-run (frozen consequence). The module's registered power floor (inputs below the frozen minimum token count; the disc's 241–242 tokens are far below Linear A scale, prereg §10, <https://en.wikipedia.org/wiki/Phaistos_Disc>) must be emitted as an out-of-domain flag under the same policy for every input class — a flag policy that fires only for the disc is an A16 divergence and itself fails the control.

---

## 10. Human-expert loop

A7 binds OBS (real palaeographers for headline claims); no amendment mandates a human expert for LNA. This design **adopts the A7 discipline voluntarily as a narrowing**: any headline E2 claim via P1 requires, in addition to the mandatory cross-model tribunal (G7), review by a named human Aegean epigrapher under a frozen rubric limited to (i) independence/validity of the external attestations matched, (ii) philological admissibility of the transformations used within the registered budget. The expert reviews evidence; the expert does not set or move thresholds. If no epigrapher has been recruited when P1 adjudication is due (plan v2 §11 open decision 3), the E2 claim is **not issued** — it waits; the E1 ranking result publishes regardless.

---

## 11. Compute and team estimate

See structured fields. Order of magnitude: **~10³ GPU-hours** (Arm B training/inference across 9 worlds + real run + resamples: ≈1,000–2,500 GPU-h) and **~1.5×10⁵ CPU core-hours** (CSA annealing dominates; reduced-budget permutation regime keeps the 1,000-permutation floor affordable). Team: ≈**24–30 team-months** over 9–12 calendar months (generator 2p×4mo; method 3p×7mo; scoring/infra 1p×6mo; red team 2p×2mo; custodian/falsifier/tribunal liaison ≈2 team-months; epigrapher consult ≈0.5).

## 12. What a null result means (G9: a first-class deliverable)

- **H-LNA-0 fails:** registered finding — "family ranking is not validated at Linear A information conditions." This is the program's registered prior against **every** future single-family Linear A claim and the first information-conditions-matched validation bound on a century of affinity proposals (Anatolian, Semitic, Tyrsenian, Hurrian — dossier §3). It is publishable because it converts "Linear A is undeciphered" into a quantitative statement: methods of the strongest published class (CSA 95.5% on Ugaritic/Hebrew at full information; 47.5% on Luwian/Hittite as conditions degrade — Tamburini 2025, URL above) measurably cannot recover *known* relationships at ~7.4k tokens/97 signs/no bilingual. The red-teamed shadow worlds (minus keys) release as a community benchmark either way.
- **H-LNA-0 passes, H-LNA-1 null:** stronger and equally publishable — a validated instrument that demonstrably finds true relatives at these conditions found none among the four registered families: affirmative evidence against all four (bounded, as always, by panel coverage: conditional on the registered candidates; isolate status and unsampled families remain open).
- **Tournament winner, P1 fails:** "ranking without external consequence" — E1 stands, E2 refused, and the refusal is reported at headline prominence (A1-style: the gap between ranking and consequence is a failure of the affinity claim, not a promising near-miss).

## 13. Protocol-violation rules

Any deviation from this design after data contact is reported as a protocol violation alongside the original registered analysis (freeze block, deviation rule). Incomplete appendix at data contact = protocol violation (A17). An agent describing shadow corpora as ancient evidence, or U2's translatedWords field as established meanings, halts the run (A9-firewall analog, adopted).

**Compute estimate:** Order 10^3 GPU-hours (~1,000–2,500: Arm B phonetic-prior neural matching across 9 shadow worlds x ~9-language panels x 3 segmentation schemes x 4 runs, plus real-corpus run with >=100 sign-value resamples) plus ~1.5x10^5 CPU core-hours (Arm A coupled simulated annealing, 16 annealers, 4 runs/config; >=1,000-permutation nulls made affordable by a frozen reduced-budget regime applied symmetrically to observed and null statistics). Shadow generation and red-teaming are CPU-trivial (<10^3 core-hours). Team: ~24–30 team-months over 9–12 calendar months (generator 2, method 3, scoring/infra 1, red team 2 part-time, custodian/falsifier liaison, ~0.5 for a named Aegean epigrapher consult).

**Null result meaning:** Three registered null layers, each a first-class deliverable per G9. (1) H-LNA-0 fails: "family ranking is not validated at Linear A information conditions" — the program's registered prior against all future single-family Linear A claims and the first information-conditions-matched quantitative bound on the century-old affinity literature (Anatolian/Semitic/Tyrsenian/Hurrian); publishable because it shows the strongest published method class (CSA: 95.5% Ugaritic/Hebrew at full information, collapsing to 47.5% Luwian/Hittite) measurably cannot recover KNOWN relationships at ~7.4k tokens / 97 signs / no bilingual — and the red-teamed shadow benchmark releases to the community regardless. (2) H-LNA-0 passes but H-LNA-1 nulls: a validated instrument that demonstrably finds true relatives at these conditions found none among the four registered families — affirmative, bounded evidence against all four candidate hypotheses (conditional on panel coverage; isolate status remains open). (3) Tournament winner but the pre-designated A4 prediction fails: "ranking without external consequence" — E1 ranking stands, E2 refused, refusal reported at headline prominence with no near-miss band (A1 discipline).

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX — R3-DES-LNA-v1.0 (deposited to tribunal record; items marked [PENDING-BLOCKS-CONTACT] must be completed before any scoring-agent data contact, per A17)

1. DATASET VERSIONS/HASHES (obtained 2026-08-11 this session):
- SigLA database.js: https://sigla.phis.me/database.js — 2,516,528 bytes (matches audit byte count exactly); SHA-256 cc624f148fd84c94fd2910b0adf92ecace25f52f9175664122bdf8384a8f1b9d; contains /* Signs */ and /* Data */ sections as audited; license CC BY-NC-SA 4.0 (site footer).
- lineara.xyz LinearAInscriptions.js: https://raw.githubusercontent.com/mwenge/lineara.xyz/master/LinearAInscriptions.js — 1,609,137 bytes; SHA-256 4da8e1f9693d30880ee505e56541fc189add70605bad88436c44a8e11a57764c; 1,722 top-level inscription records counted; header carries an SQLite-style "author disclaims copyright to this source code" blessing (covers code at most, not Douros/GORILA-derived data or EFA images); repo LICENSE 404 per audit. [PENDING: pin GitHub commit SHA — API unavailable this session.]
- [PENDING-BLOCKS-CONTACT] hashes for: candidate lexicons (NeuroDecipher Ugaritic/Hebrew + Linear B/Tselentis, github.com/j-luo93/NeuroDecipher; Burman Etruscan concordance Zenodo 10.5281/zenodo.13784774 v1.0.2; Luwian/Hittite hand-keyed or negotiated; Hurrian hand-keyed from Laroche GLH) and all nine shadow-source corpora (CDLI Ur III + Old Assyrian ATF exports; DAMOS/LiBER Linear B; Ugaritic economic; Hittite/Luwian; Demotic/Coptic; gramoty.ru birchbark; Basque records). Rule: unhashed artifact = ineligible.

2. A19 UNIT REGISTRY ENTRY (new, deposited): lineara.xyz 1,722 records vs Braovic 1,370 documents (7,362–7,396 sign tokens, 97 signs; aclanthology.org/2024.cl-2.7.pdf) vs GORILA-based ~1,427 artefacts (~7,150 signs; mdpi.com/2078-2489/15/2/73). Frozen treatments: UT-1 both corpus universes (U1=SigLA, U2=lineara.xyz) with frozen concordance; UT-2 atomic (primary) vs decomposed (secondary) ligatures — claims must hold under both; UT-3 sign tokens with numerals/klasmatograms stripped from method input (numeral values sealed for P2).

3. SHADOW-WORLD PANEL COMPOSITIONS (A3, frozen — full roster in design §3.3–3.4): W1 Mycenaean Greek→archaic Greek; W2 Ugaritic→Hebrew; W3 Hittite→Cun. Luwian; W4 Old Assyrian→Ugaritic; W5 Demotic→Coptic; W6 Old Novgorod→OCS; no-relative N1 Sumerian, N2 Elamite (pass/fail computed with and without Old Tamil), N3 Basque. Each panel: 1 true relative (or none) + >=7 decoys, >=2 documented-contact decoys, phonotactic encodability within ±10pp of R, attestation within ±800y of R or logged deviation, no decoy genetically related to H or R at consensus phylogeny. Frozen substitution reserve: Old Georgian, Old Japanese, Middle Egyptian (phylum-legal panels only), Hungarian, Quechua (deliberately implausible reserve). Lexicon budget: 2,000 entries, floor 800.

4. GENERATOR TOLERANCES (frozen): tokens per world drawn in [7,150, 7,396] (hard); documents in [1,370, 1,427]; realized inventory 92–97 signs; doc-length KS<=0.05 vs frozen real snapshot; genre mix ~97% admin lists / ~3% votive formula ±2pp; divider rate ±2pp; damage fraction ±2pp of measured; prior coverage c = measured real prior-table coverage ±2pp; prior error rate epsilon in {5%,15%}, both run; glyph IDs novel/random; numerals redrawn under arithmetic consistency.

5. SIGN-VALUE PRIOR TABLE [PENDING-BLOCKS-CONTACT]: per-sign table with provenance class A (secure Linear B homomorph, fixed) / B (probable, 10% swap-out per resample) / C (conjectural, uniform over admissible values); >=100 resamples per frozen H-LNA-1 clause (b); the measured coverage fraction c feeds item 4.

6. H-LNA-1 CONTROL-PANEL PROCEDURE (the panel itself is chosen by a blind agent per the frozen prereg — this appendix freezes only pool + procedure): eligibility pool = {Sumerian, Elamite, Hattic, Old Georgian, Old Tamil, Basque, Middle Egyptian, Akkadian, Old Nubian, Old Japanese, Hungarian, Finnish/medieval Finnic, Classical Nahuatl, Quechua, Old Turkic, Celtiberian}; constraints on the draw: >=7 controls; >=2 contact-plausible with Bronze Age Aegean sphere; >=2 typology/phonotactics-matched; >=1 deliberately implausible; no control related to any registered candidate family at consensus phylogeny (excludes all IE and all Semitic/Afroasiatic-at-phylum from control slots where conflict arises); identical transformation budget for all panel members. Draw executed by the designated blind agent with committed seed; result deposited before scoring.

7. METHOD FREEZE [PENDING-BLOCKS-CONTACT]: code hash of both arms (CSA: 16 annealers, 4 runs/config, no best-of-N; Luo-2021-style syllabic adaptation), 50/50 z-score aggregation, segmentation schemes S1–S3, permutation machinery (>=1,000 permutations; reduced-budget symmetric regime at 1/10 anneal budget for observed AND null), all seeds. Deposited before the first shadow world is scored.

8. POWER ANALYSIS (design decisions, cite nothing): H-LNA-0 top-1 rule at panel size 8 (1R+7D): P(pass|chance)=C(6,5)(1/8)^5(7/8)+(1/8)^6 ≈ 1.64e-4; at panel size 9: ≈ 9.2e-5. Power: per-world true recovery q=0.9 → 0.886; q=0.8 → 0.655; q=0.7 → 0.420 — deliberately conservative: moderate methods fail the precondition. False-positive battery: allowed exceedance 1 of 3 no-relative worlds; under calibrated nulls per-world FP ≈ 0.04 (Holm 0.01 x 4), P(spurious battery failure) ≈ 0.0047; sensitivity limit acknowledged: mild miscalibration (per-world FP 0.2–0.3) detected with probability only 0.10–0.22 — mitigated by a registered descriptive QQ-calibration diagnostic pooled across all 9 worlds (no threshold change). H-LNA-1: thresholds are frozen prereg text (p<0.01 Holm across 4 candidates, >=1,000 permutations, stability (a)(b)(c)); minimum achievable empirical p at 1,000 permutations = 1/1001 < 0.01 (feasible).

9. P1–P3 SEALING [PENDING-BLOCKS-CONTACT]: custodian seals (hashes deposited): (a) closed onomastic candidate list for P1 (Kom el-Hetan Aegean toponym list entries; Mari/Amarna Kaptara/Keftiu class references; Linear B onomastic exclusion list) with H-ONO-1 six-element registration; (b) P2 numeral-value seal over the custodian-held accounting-document list; (c) P3 provenance-metadata seal. Deposit-then-unseal protocol; predictions hashed before unsealing.

10. PHAISTOS/A16 COUPLING: identical frozen reporting/confidence policy document (shared with the H-PHA-1 runner) deposited; out-of-domain power-floor flag defined uniformly for all inputs; disc run scheduled alongside the real run.

11. SNAPSHOT/FREEZE DATES: corpus snapshots and concordance frozen at appendix completion date; SigLA post-snapshot ingestions (changelog live to June 2026) form the descriptive prospective set (no threshold).

12. DECLARATION: per A17, this appendix is incomplete until every [PENDING-BLOCKS-CONTACT] item is deposited; any data contact before then is a protocol violation reportable in the Run 3 checkpoint.

# Shadow-Benchmark Harness: Indus stress test + Voynich E1 + pilot corpus

# Run 3 Experiment Design — Shadow-Benchmark Harness
## Indus methodology stress test + Voynich E1 model comparison + pilot shadow corpus

**Designer role statement (G2/HARKing guard, plan v2 §9).** This document *designs*; it does not adjudicate. Every success/disconfirmation criterion below is either (a) quoted from the frozen preregistration `/home/claude/work/run2-preregistration-FROZEN.md` as amended by `/home/claude/work/tribunal-record-and-prereg-amendments-v1_1.md` (amendments A1–A19, all entered 2026-08-11 before Run 3 data contact), or (b) a new registered sub-test whose *execution and scoring* is assigned to agents disjoint from this designer and whose outcome binds via the frozen text, not via any later judgment of this designer. Scoring agents cite hypothesis IDs, never this document's prose, as authority. Headline claims require the cross-model tribunal (G7; tribunal record §I.1: internal agreement is never sufficient).

**Binding documents:** research plan v2 (`undeciphered-research-plan-v2.md`); frozen prereg (`run2-preregistration-FROZEN.md`); tribunal record & amendments v1.1 (`tribunal-record-and-prereg-amendments-v1_1.md`); Run 2 data-reality audits (`run2-audits-methods-patch.md`); Checkpoint 2 matrix (`run2-checkpoint2-matrix.md`).

**Claim bands executed (A18 format):**
- **Indus: E2 / L1–L3 predictive-structural · E1 language-status · E0 readings** (tribunal record §I.2, split verdict). No component of this design emits any reading, phonetic value, or semantic claim (E0 band untouched; L4–L7 not attempted).
- **Voynich: E1 — model-comparison only** (tribunal record §I.2; A14). No class label (language/cipher/meaningless) is asserted at any posterior; L5+ output barred regardless of outcome (prereg §8).

**Data-contact declaration.** This designer's only data acts were audit-grade: pinning file hashes (EVA files, CDLI dump, lineara.xyz JS) and building the pilot shadow world from *source-language* data. No Voynich statistic and no Indus corpus statistic was computed by this designer. The pre-scoring appendix (Part F) is complete at design time per A17; items that structurally require the not-yet-built Indus corpus (occurrence counts, final power run) are sequenced so they are deposited by the data team *before* any scoring agent contacts data — see F.6.

---

# PART A — INDUS: methodology stress test + narrow structural E2

Program role: stress test of methodology, not a decipherment candidate (plan v2 §7; tribunal Part III lists Indus as a mandatory harness element).

## A.1 Data acquisition plan (grounded in the audit, not papers' claims)

Audited reality (Run 2 data-reality audit, all verified 2026-08-11):
- **ICIT (Wells–Fuls)** is *alive but gated*: HTTP 401, access by email negotiation with fuls(at)epigraphica.de, **no license, no bulk export, no API** ("ICIT — Interactive Corpus of Indus Texts," audit row, <http://www.indus.epigraphica.de>). The Digital Classicist "down since June 2021" note is outdated. Content is also fixed in print: Fuls, *Corpus of Indus Inscriptions* and *A Catalog of Indus Signs* (Mathematica Epigraphica 3–4, 2023).
- **Mahadevan 1977 (M77)** exists openly only as a 1.6 GB scan with dirty OCR (Internet Archive, <https://archive.org/details/TheIndusScript.TextConcordanceAndTablesIravathanMahadevan>); the structured EBUDS encoding behind Rao et al. 2009 was **never publicly released** (audit row).
- **mayig/indus-valley-script-corpus**: MIT-licensed independent CISI digitization, but only 179 artifacts (~4% of ICIT scale), Mohenjo-daro M-001–M-199 (audit row, <https://github.com/mayig/indus-valley-script-corpus>; clone verified 2026-08-11, last commit 2025-04-16).
- **FIT_ISI_Corpora 2025**: 963 curated seal images with grapheme transcription in SQL (JCAA, <https://journal.caa-international.org/articles/10.5334/jcaa.175>) — image-centric, open.
- Falsifier verdict (Checkpoint 2, Indus — WEAKENED): structural E2 "stands only conditionally on the pre-scoring appendix fixing an accessible, deduplicated, dual-inventory basis."

**Registered acquisition plan.**
1. **Primary basis (buildable, redistributable): a new keyed M77 corpus.** Re-key the Mahadevan concordance from the Archive scan into a structured corpus (object ID, sign sequence in M77 sign numbers, object type, site/provenance, concordance duplicate-attestation links). Method: OCR-assisted double-entry by two independent keyers + adjudication of disagreements by a third; per-object error rate target ≤1% estimated on a 200-object double-blind sample. Deliverable `indus-m77-keyed` with a corpus contract (counts + SHA-256) deposited to the tribunal record **before any scoring agent contacts it** (A17 sequencing, F.6). Underlying work is © ASI Memoir 77; the derived sign-sequence dataset is keyed for research use and its redistribution status is assessed by counsel before public release — internal use for scoring is unaffected; this is declared, not hidden.
2. **Secondary basis (negotiated): ICIT export.** Request access per the audited channel. If granted: exact export frozen and hashed at receipt. Registered caveat carried on every ICIT-based result: unlicensed, non-redistributable, not independently re-runnable (falsifier's independence objection) — such results are labeled "conditionally reproducible" and can never carry a headline alone.
3. **Cross-validation bases:** mayig (179 objects) and FIT_ISI (963 seals) used only as transcription cross-checks on the overlap with the keyed M77 corpus (G8 bridging: agreement rate reported; no claim transfers across bases without it).
4. **A19 unit treatments (frozen now):** Treatment **M417** = Mahadevan 417(+2) sign inventory, as keyed from M77. Treatment **W694** = Wells–Fuls ~694-sign inventory via ICIT export or, failing that, via a keyed mapping from Fuls's print *Catalog of Indus Signs* (purchase + re-key). Every EXP-IND result is computed and reported under **both** treatments; divergent verdicts are reported as divergence with no tie-break (prereg H-IND-2 controls; A19). **Fallback (registered):** if by month 3 neither ICIT export nor the print catalog mapping exists, affected results are reported under M417 only, flagged "single-unit-treatment — capped," and the tribunal is notified; no claim under a single treatment may be presented as inventory-robust.
5. **Data basis declaration (G8):** transliterated sign-code sequences (basis iii), plus structured object metadata (basis iv). Paleography/images out of scope.

## A.2 EXP-IND-A — H-IND-1 shadow discriminability (E1; amended by A1)

**Hypothesis executed:** H-IND-1 as frozen, with A1's strict failure definition: *disconfirmation = failure to satisfy every registered success criterion (point AUC ≥ 0.80 AND 95% bootstrap CI lower bound > 0.65); the zone between "CI includes 0.5" and full success is a failure, not "promising."*

**World panel (frozen; composition in appendix F.2).** 24 worlds: 12 language-encoding, 12 meaningful-nonlinguistic, each matched to Indus information conditions registered in H-IND-1: token count 19,616 ±10%, sign inventory within 417–694, mean text length ~5 signs, matched text-length distribution (per-world length multiset drawn from the keyed M77 length distribution; until it is deposited, from the ICIT-published aggregate: 5,509 texts / 19,616 occurrences, "Interactive Corpus of Indus Texts," Digital Classicist Wiki, <https://wiki.digitalclassicist.org/Interactive_Corpus_of_Indus_Texts>).
- **Nonlinguistic families (6 × 2 seeds):** (N1) SIGIL replica built to the published spec — slot grammar, finite-pool Pitman–Yor urns, licensing, ligatures, administrative rare signs, regional outposts, direction conventions ("On the Non-Specificity of Statistical Measures Used in Script Decipherment," arXiv 2608.02999, <https://arxiv.org/abs/2608.02999>) — with new seeds and a new sign registry; (N2) SIGIL-variant with re-drawn grammar/urn/licensing parameters; (N3) emblem-rank system (deity/office emblem sequences with rank-ordering constraints); (N4) owner-mark heraldic sealing system (mark + office + commodity slots); (N5) numerical-accounting notation without phonology (proto-cuneiform-like commodity+quantity structure); (N6) nonlinguistic protocol code (fixed-protocol marker sequences with state-dependent licensing). G4 bar: no shuffled/random-token generator anywhere.
- **Language-encoding families (6 × 2 seeds):** Indus-genre degradations (short seal-type texts: names, titles, patronymics, commodity terms) of real languages re-coded to novel glyphs: (L1) Sumerian Ur III seal legends and short receipts (CDLI dump, pinned — see F.1); (L2) Old Akkadian seal/brick legends (CDLI dump); (L3) syllabically re-encoded Latin onomastic/titular strings (epigraphic-formula genre); (L4) syllabically re-encoded Ancient Greek onomastics; (L5) logosyllabic mixed encoding of Sumerian (logogram+phonetic-complement regime); (L6) abjad-style consonantal encoding of a Semitic corpus. Each family's concrete source dataset must pass a data-reality micro-audit (exists, license, hash) before the family is built; a family failing audit is replaced from a registered reserve list (F.2) — replacement logged, never silent.
- **Team separation (G2/prereg H-IND-1 controls):** generator team ≠ discriminator team ≠ red team ≠ scoring executor. Answer keys sealed with the custodian (same protocol as the pilot, Part C).
- **Red team (prereg: mandatory):** attacks every generator family before scoring; one undetected language-shaped "nonlinguistic" generator voids the batch and, per H-IND-1's frozen disconfirmation clause, leaves H0 standing.

**Discriminator (frozen before any panel world is scored).** A feature registry closed at freeze: the six SIGIL exact-scored criteria and its descriptive battery (repetition ratios, terminal Gini/entropy asymmetries, LNRE model fits, Zipf–Mandelbrot parameters, conditional entropy h2, positional-coverage asymmetry, transition-graph reciprocity/connectance, masked-sign restoration), plus small from-scratch sequence models (n-gram/char-LM cross-entropy profiles) trained per-world — **no pretrained models anywhere** (G6; rationale: the Unicode/training-exposure confound demonstrated in "Reasoning Over the Glyphs," arXiv 2501.17785, <https://arxiv.org/abs/2501.17785>). The discriminator (a classifier over the frozen features) is trained on a disjoint *development* world set (same families, different seeds, generated first and marked dev-only), then frozen: code + weights + feature list hashed and deposited. Evaluation = one pass over the 24-world panel; world-level scores → AUC.
- **Decision rule (frozen, per H-IND-1 + A1):** point AUC ≥ 0.80 AND 95% bootstrap CI (10,000 resamples, percentile) lower bound > 0.65 → H0 rejected. Anything else → **failure** (A1), H-IND-2 cancelled, all Indus is-it-language claims barred above E1 (frozen disconfirmation clause).
- **Secondary diagnostic (registered, non-gating):** leave-one-generator-family-out AUC, reported per family (A13's logic imported as a diagnostic; gating stays exactly as frozen — appendices may narrow reporting, never widen thresholds).
- **Calibration items (frozen):** the discriminator's output on proto-cuneiform (CDLI Uruk III/IV ATF export, audited 5/5) is reported per H-IND-1 controls; a confident language/non-language verdict on it is a calibration failure (Checkpoint 2, Proto-cuneiform UPHELD verdict). The Phaistos Disc is *not* scored by this discriminator except within the concurrent H-PHA-1 negative-control run, where an is-it-language posterior ≥ 0.75 presented as a finding is pipeline failure condition 2 (prereg §10).
- **Power (computed for this design, 2026-08-11; simulation spec in F.4):** at panel 12+12, P(meet both criteria) ≈ 0.37 at true AUC 0.80, 0.84 at 0.90, 0.985 at 0.95; false-pass rate 0.0015 at true AUC 0.50 and 0.019 at 0.60. The rule is deliberately severe: only strong discriminability passes; marginal true effects are expected to fail and be reported as the null (G9).

## A.3 EXP-IND-B — H-IND-2, relabeled E1 model comparison (A2)

Conditional on EXP-IND-A rejecting H0. Executed exactly as frozen (single one-shot application of the frozen discriminator to the real corpus; no post-hoc feature changes; both A19 unit treatments) with A2's relabel and conclusion rewrite:
- **Licensed output:** a likelihood ratio / classifier score *conditional on the registered generator families*, reported with CI, under both M417 and W694. Every report must state the prior, mixture weights, and generator-family coverage limits (A2).
- **Prohibited output (verbatim per A2):** any statement of the form "P(Indus is linguistic) = x" or any directional language/non-language finding. The frozen H-IND-2 threshold (posterior ≥ 0.90 / ≤ 0.10) is retained as the *reporting gate* for the conditional score, but the conclusion sentence is A2's, never the frozen E2 phrasing; divergence across the two sign inventories → no claim, discrepancy reported (frozen disconfirmation).
- **Contamination note (G6):** the real Indus sequences (Mahadevan/EBUDS-derived n-grams) plausibly occur in web text; because the discriminator uses only hand-computed statistics and per-world from-scratch models, the memorization channel is closed by construction; this is asserted in the run report with the discriminator's dependency manifest.

## A.4 EXP-IND-C — Narrow E2/L1–L3 structural experiments (tribunal-licensed)

**License:** tribunal record §I.2, Indus row: "Preregistered structural predictions against withheld real objects (sequences, object type, provenance) satisfy §2," conditions: dedup at object-family level; both allography treatments frozen; contamination controls; predictions defined before holdout exposure; no linguistic interpretation of predictive success. The following three sub-tests are registered now as a dated changelog entry under the prereg amendment policy (before data contact for this family); execution and scoring are assigned to disjoint agents; this designer adjudicates nothing.

**Dedup unit (frozen definition):** *object family* = the transitive closure of M77 concordance duplicate-attestation links, further merged for (a) identical full sign sequence under the active unit treatment AND same object type, and (b) seal↔sealing impression pairs. All members of a family fall on the same side of every split. (Falsifier basis: "the Mahadevan concordance is organized around duplicate attestations"; unregistered dedup was the leakage attack — Checkpoint 2, Indus verdict.)

**Split protocol:** 20% of object families held out, stratified by site and object type; split drawn by the custodian from the deposited corpus contract; holdout object records sealed until predictions are deposited (hash-committed). 5 independent splits; report mean ± sd; all tests Holm–Bonferroni-corrected within the IND structural family over all tests actually run (G5), under each unit treatment separately, verdicts reported under both (A19).

- **H-IND-S1 (L3, E2) — object-type prediction.** H0: a frozen classifier over sign-sequence features predicts the held-out family's object type (M77 object classes, collapsed to a frozen ≥5-way scheme deposited with the corpus contract) no better than the permutation null (labels permuted within site strata, ≥1,000 permutations). H1: balanced accuracy exceeds the null at empirical p < 0.01. Licensed claim on success: "sign sequences carry object-type-predictive structure" — nothing more.
- **H-IND-S2 (L3, E2) — provenance prediction.** Same design; target = site class (Mohenjo-daro / Harappa / other, frozen); null permutes within object-type strata. Registered confound control: duplicate families concentrate within sites; dedup handles leakage, stratified permutation handles base-rate structure.
- **H-IND-S3 (L2/L3, E2) — out-of-sample positional structure.** H0: a positional model (frozen: interpolated n-gram over sign classes + positional slot model, trained on training families only) predicts masked signs at frozen mask positions (first, last, and one uniform-random interior position per held-out text of length ≥3) no better than a frequency-only baseline. H1: top-10 recovery exceeds baseline at p < 0.01 (paired permutation). Licensed claim: "positional regularities generalize across object families" (a structural, G3-compatible sequence claim per the tribunal's explicit licensing of predictions on sign sequences; no reading is implied and none is emitted).
- **Models:** feature-based classifiers (regularized logistic/gradient boosting) and n-gram models trained from scratch on the corpus only. **No pretrained LLM/embedding touches any Indus experiment** (G6).
- **Disconfirmation:** any sub-test failing its threshold under either unit treatment is reported as failed under that treatment; divergence across treatments is itself a first-class finding (the falsifier's "allography fork caps any single structural finding").

## A.5 Indus contamination controls (G6) — summary
(1) No pretrained models anywhere in IND scoring paths (dependency manifests audited). (2) Shadow worlds use novel glyph IDs with sealed keys; source corpora for language worlds are hash-pinned; the arXiv 2501.17785 Unicode-exposure result is the registered rationale. (3) Real-corpus experiments operate on re-coded sign IDs (seeded bijection per run) so no tool inherits M77 numbering conventions. (4) Discriminator frozen before panel contact; one-shot rule for H-IND-2. (5) H-PHA-1 negative control runs concurrently; failure quarantines concurrent IND results (prereg §10; A16 identical-reporting-policy rule applies across control and targets).

---

# PART B — VOYNICH: H-VOY-0 / H-VOY-1 as E1 model comparison

## B.1 Data acquisition (audited reality)

Audit verdict: the only 5/5 leg. Files verified by download in Run 2 and re-pinned by this design on 2026-08-11 with SHA-256 (F.1): **ZL3b-n.txt** (411,671 B; IVTFF header "#=IVTFF Eva- 2.0", version 3b dated 13/05/2025) and **IT2a-n.txt** (342,104 B) from voynich.nu/data/ ("Voynich MS — transliteration files," <https://www.voynich.nu/transcr.html>). Frozen choices:
- **Primary transliterations (prereg requires ≥2 independent):** ZL (Zandbergen–Landini) and IT (Takahashi). **GC** (v101 alphabet) = registered third robustness axis, reported but non-gating. **RF is excluded from evidence**: the audit records it as an automated ZL+GC synthesis — not independent.
- **Stratification variables (tribunal condition; internal falsifier):** scribal hand (five hands, Lisa Fagin Davis's digital palaeography: "Alumna joins the long search to unlock enigmatic 15th-century manuscript," Yale Library, <https://library.yale.edu/news/alumna-joins-long-search-unlock-enigmatic-15th-century-manuscript>) and Currier language A/B. Operationally: the folio→(hand, Currier) table is compiled from ZL3b IVTFF page-level metadata plus Davis's published assignments, deposited and hashed as appendix item F.5 by the data team before classifier development begins; conflicts between sources are carried as a "contested-stratum" flag, never resolved silently.
- License: no explicit license on voynich.nu files (site © René Zandbergen 2025, per audit); files used for analysis, not redistributed.
- G8 basis: machine-readable transliterations (basis iii). No claim about the physical manuscript.

## B.2 EXP-VOY-A — H-VOY-0 validation battery (E1; amended by A13)

Executed as frozen: 3-class battery (natural language / ciphered language / meaningless structured pseudo-text), ≥30 texts per class, length-matched by equal truncation to the Voynich scale (~37k tokens; range 36k–38k preserved per prereg §8), cross-validated macro-F1; thresholds macro-F1 ≥ 0.85 AND per-class recall ≥ 0.75.

**Generator-family registry (frozen; full list F.2).** Class (a): ≥10 natural languages including unspaced orthographies, abjad/abugida, and low-resource cases, each re-coded to novel glyph IDs (G6). Class (b): period-plausible ciphers per the frozen prereg list — simple substitution, homophonic substitution, nomenclator, Cardan-grille variants — applied to class-(a) plaintexts. Class (c): (c1) Rugg Cardan-grille table generation; (c2) Timm–Schinner-style self-citation/auto-copying generation; (c3) SIGIL-style slot-grammar pseudo-text adapted to page/line structure; (c4) human-elicited gibberish following the 2022 Yale-style protocol (prereg §8). **Feasibility decision, frozen now (falsifier: published human gibberish is far shorter than 37k tokens):** each (c4) "text" is the concatenation of one writer's multiple sessions; where a class-(c4) text still falls short, statistics are computed on equal-length blocks with text length as a registered covariate; (c4) minimum 6 texts, with classes topped up to 30 by (c1)–(c3) — composition counts frozen in F.2. Class-(c) generators are red-teamed per G4; a generator secretly encoding language voids the batch (frozen control).

**A13 LOGO protocol (mandatory).** Two evaluations: (i) standard cross-validation on the registry; (ii) leave-one-generator-family-out: for every family, classifiers retrained without it and evaluated on it — **including two held-back families per class built by the red team after the classifier team's feature set is frozen and never seen during construction** (A13's "families never seen during classifier construction"). **Registered execution rule (a narrowing, permitted):** H-VOY-1 runs only if the frozen thresholds are met AND LOGO macro-F1 ≥ 0.75 across left-out families. High in-registry F1 with LOGO failure is reported as *fingerprinting, not classification* (A13 verbatim) and counts as H-VOY-0 disconfirmation for licensing purposes; the frozen finding is then "the three generating classes are not distinguishable at this scale by the tested features."

**Features/models:** hand-computed statistics (entropy suite incl. h2, Zipf/Zipf–Mandelbrot fits, word-structure/morphology proxies, line-position effects, repetition/self-citation metrics, network statistics) + small from-scratch sequence models per text. No pretrained models (G6); all inputs re-coded to novel glyphs so no memorized EVA strings can leak (the Voynich transliterations are certainly in LLM training data; this closes the channel structurally).

**Recall-threshold operating characteristics (computed 2026-08-11, F.4):** at n=30/class, P(observed recall ≥ 23/30) = 0.044 if true recall 0.60; 0.514 at 0.75; 0.930 at 0.85 — the battery is powered to pass only clearly-working classifiers.

## B.3 EXP-VOY-B — H-VOY-1 as E1 model comparison (A14; tribunal E1)

Conditional on EXP-VOY-A passing under B.2's rule. Executed as frozen with A14's relabel and the tribunal's stratification condition:
- **Reserve design:** a 20% folio block, stratified so train and reserve match on hand × Currier-language composition (all five hands and both Currier populations represented in the reserve in proportion); reserve frozen and hashed before classifier finalization (the falsifier's exchangeability attack is thereby answered by design, and the same analysis is additionally reported **per stratum**).
- **Mixture outcome (registered):** because five hands × two Currier populations may not share one generating process (falsifier: single-class framing ill-posed), the design registers a per-stratum verdict table. If different strata are best explained by different generator families, the registered finding is "stratum-dependent best-explaining families" — a mixture result, reported as such; it is not collapsed into a single-family headline.
- **One-shot rule:** exactly one application per transliteration (ZL, IT); disagreement between transliterations → indeterminate verdict (frozen).
- **A14 frozen reproduction tolerances** — moved into the hypothesis now, before any generator is built (concrete values, design decisions, cite nothing): a generator family "reproduces" the reserve profile iff ALL of: (1) Zipf–Mandelbrot exponent within ±0.10 of the reserve value; (2) conditional character entropy h2 within ±0.15 bits; (3) hapax-legomenon fraction within ±0.03 absolute; (4) mean word length within ±0.3 characters; (5) word-length distribution Jensen–Shannon divergence (base 2) ≤ 0.02; (6) line-position effects: line-initial and line-final character-distribution association (Cramér's V) each within ±0.05 absolute; (7) between-section word-frequency association (Cramér's V over the frozen section partition) within ±0.05. All computed on reserve folios only, per transliteration, identically for manuscript and generator output. The manuscript-side values are measured once at execution by the scoring agent; the tolerance *widths* above are frozen now and may not move.
- **Licensed conclusion (A14 verbatim discipline):** "among the preregistered generating models, family X best explains Voynich statistics out-of-sample" — E1 model-comparison. Prohibited: class labels (language / cipher / meaningless) at any posterior; any reading, glyph value, or plaintext (L5+ bar, frozen). A confident assignment whose generators fail reproduction is a pipeline-overconfidence finding and quarantines the result (frozen).
- **H-PHA-1 interplay:** a Voynich-style class assignment with posterior ≥ 0.90 on the Phaistos Disc is pipeline-failure condition 5; the concurrent control run covers this family (prereg §10; A16 reporting-policy identity enforced).

## B.4 Human-expert loop
A7 (named human oracle-bone palaeographers) binds the OBS family, which is outside this design's scope; it is noted here because the harness shares the frozen rubric mechanism: for Voynich, no headline requires expert adjudication since every claim is E1, but two human touchpoints are registered: (i) class-(c4) human-gibberish writers (elicitation protocol frozen in F.2; writers naive to the classifier's features); (ii) the hand/Currier stratification table is compiled from published palaeography (Davis) — if the program's optional human epigrapher (plan v2 §11, open decision 3) is recruited, they review the F.5 table before freeze; their role is documentation review, not outcome adjudication.

---

# PART C — PILOT SHADOW CORPUS (built, runnable, sealed)

Delivered at `/home/claude/work/shadow-pilot/` — working Python, deterministic, ~4 minutes CPU end-to-end, verified:
- **World SW-PILOT-01**: Sumerian Ur III administrative texts (CDLI bulk ATF dump, hash-pinned; live CDLI export returned empty responses on 2026-08-11 re-probe, so the frozen stale dump is used — better for reproducibility; both facts logged) degraded to **measured** Linear A information conditions derived from real GORILA-based data (lineara.xyz, aggregate statistics only): 1,697 documents matched **1:1 to the real Linear A document-length multiset** (verified exactly), 8,357 sign/ligature tokens + 437 lacunae ≈ the 8,912-token Linear A scale, core source inventory 115 signs (LA: 97 core), glyph inventory 145 with allographs+ligatures, word boundaries erased and re-marked at the *measured* LA divider rate 0.147, numerals converted to additive Aegean-style decimal and thinned to the measured LA numeral density (1,558 vs target 1,580), sign-level lacunae at 5%.
- Files: `README.md` (every design choice + limitations + red-team leads), `profile.py`/`profile.json` (frozen target profile), `build_shadow.py`, `verify_build.py` (public + custodian modes; all 8 checks PASS), `fetch_raw.sh` (hash-pinned inputs), `corpus/shadow_corpus.txt` + `corpus/corpus_contract.json` (public), `sealed/ANSWER_KEY.SEALED.json` + seal notice (glyph map, allograph map, ligature registry, per-doc CDLI P-numbers, scribe assignments, lacuna positions, build seed — custody: non-scoring agent per H-LNA-0 controls). Code public, **seed sealed**: auditable generator, non-regenerable key. Corpus SHA-256 `0df416fa…d9fd92d9`; sealed-key commitment `7a00365a…c509813ffb` recorded in the public contract.
- Status: harness validation and red-team target only; explicitly **not** one of the frozen H-LNA-0 or H-IND-1 worlds (those are built by the disjoint generator team). Documented residual leaks (public source corpus; isolate source language; single world) are closed in the production designs, not here.

---

# PART D — Claim-ladder levels and licensed E-classes

| Experiment | Ladder levels attempted | Licensed E-class (per tribunal record) | Claim on success |
|---|---|---|---|
| EXP-IND-A (H-IND-1) | L1–L3 on synthetic worlds | E1 | "a frozen discriminant separates language from matched nonlinguistic encoding at Indus conditions" |
| EXP-IND-B (H-IND-2, A2) | — (one-shot scoring) | E1 model-comparison | generator-conditional score only; no directional language finding |
| EXP-IND-C (S1–S3) | L1 (frozen unit treatments), L2–L3 | E2 (structural band only) | object-type/provenance/positional structure generalizes across object families |
| EXP-VOY-A (H-VOY-0, A13) | L1–L3 on controls | E1 | classifier validated (or fingerprinting null) |
| EXP-VOY-B (H-VOY-1, A14) | L1–L3 internal statistics | E1 model-comparison | "family X best explains Voynich statistics out-of-sample," possibly per-stratum |
| Pilot world | L0 infrastructure | n/a (no claim) | none |

L4–L7: not attempted anywhere in this design; L7 prohibited program-wide (G2); Voynich L5+ barred regardless of outcome; Indus readings E0-barred.

# PART E — Preregistered success/disconfirmation (authority = frozen text)

- **H-IND-1:** success/failure exactly per frozen §1 + A1 (strict conjunction; red-team void condition; failure cancels H-IND-2 and bars is-it-language claims above E1).
- **H-IND-2:** per frozen §1 + A2 (relabel E1; prohibited sentence forms; dual-inventory divergence → no claim).
- **H-IND-S1/S2/S3:** registered in A.4 (dated amendment-appendix entry, pre-data-contact); thresholds p < 0.01 Holm-corrected within family; dedup and dual-treatment conditions per tribunal record §I.2; any deviation after data contact is a protocol violation reported per the freeze block.
- **H-VOY-0:** per frozen §8 + A13; execution rule B.2 (a registered narrowing); fingerprinting outcome = disconfirmation for licensing.
- **H-VOY-1:** per frozen §8 + A14 + tribunal stratification condition; tolerances of B.3 are the frozen A14 values; indeterminate and mixture outcomes are first-class results.
- **H-PHA-1:** runs concurrently; conditions 2 and 5 specifically police this design's modules; failure quarantines concurrent results (frozen §10).

# PART F — A17 pre-scoring appendix → see `appendix_items` (deposited with this design)

# PART G — Compute and team estimate
See `compute_estimate` field. Order of magnitude: ~10² GPU-hours (point estimate ≈300, ceiling 10³ with reruns); CPU-dominated otherwise; ~10–14 team-months over 4–6 calendar months.

# PART H — Null results
See `null_result_meaning` field. Every null above is a registered deliverable at headline prominence (G9).

# PART I — Governance
Designer ≠ executor ≠ adjudicator throughout; custodian holds all sealed material; all search/restart logs auditable (G5); headline claims go to the cross-model tribunal (G7); the Checkpoint 2 matrix is reissued in A18 claim-band format at synthesis; any post-data-contact deviation is reported as a protocol violation with the registered analysis alongside (freeze block).

**Compute estimate:** Order of magnitude 10^2 GPU-hours; point estimate ≈300 GPU-h, ceiling ≈10^3 with full robustness reruns. Breakdown: H-IND-1 worlds are CPU-minutes each (pilot: ~4 min for a full world); per-world from-scratch char-LM features ≈ 24 panel + ~36 dev worlds × ~1 GPU-h ≈ 60 GPU-h; EXP-IND-C is CPU-only (n-grams, boosted classifiers, permutation nulls ≈ CPU-days). Voynich battery ≈ 100+ control texts × small sequence models ≈ 60 GPU-h; generative-reproduction fitting (cipher/self-citation/slot-grammar/char-LM families) ≈ 50–100 GPU-h; LOGO retraining multiplies battery cost ×~10 on the cheap feature models (mostly CPU). Red-team and quarantine reruns budgeted at 2×. No pretrained-LLM inference anywhere in scoring paths (G6), which is what keeps this in the 10^2 band. Team: ~10–14 person-months over 4–6 calendar months — Indus 5–7 (of which 2–3 = M77 double-entry re-keying + contract; 1 = ICIT negotiation/print-catalog keying), Voynich 3–4 (battery construction incl. human-gibberish elicitation, LOGO harness, one-shot runs), shared harness/red-team/custodian/tribunal packaging 2–3.

**Null result meaning:** Every null is a registered first-class deliverable (G9). (1) H-IND-1 null (the expected outcome after SIGIL, arXiv 2608.02999): "no preregistered statistic distinguishes language-encoding from matched meaningful nonlinguistic corpora at Indus information conditions" — under the frozen disconfirmation clause this cancels H-IND-2 and bars ALL Indus is-it-language claims above E1, converting the 2004–2014 Rao/Farmer–Sproat–Witzel entropy wars into a closed, preregistered, severe-test result; publishable because it is the first *adversarially red-teamed, prereg-frozen* version of the non-specificity finding, with A1 closing the "promising trend" escape. (2) EXP-IND-C null: positional/object-type/provenance structure fails to generalize across object families — direct evidence that published Indus structural regularities ride on duplicate-attestation leakage (the falsifier's registered attack), a methods result the whole field must answer. (3) A19 divergence outcome (M417 vs W694 verdicts disagree): quantifies how much Indus "structure" is an artifact of allography decisions — a novel, citable cap on the literature. (4) H-VOY-0 failure or A13 fingerprinting outcome: "the three generating classes are not distinguishable at Voynich scale by the tested features; in-registry accuracy was generator fingerprinting" — constrains every published Voynich classification claim and explains the literature's contradictory verdicts. (5) H-VOY-1 indeterminate/mixture outcome: the manuscript is not assignable at the frozen tolerances, or strata disagree — the first stratification-honest negative, directly usable against future single-class claims. (6) H-PHA-1 pass is never evidence of validity, but its failure quarantining concurrent results is itself a publishable pipeline-falsification demonstration (plan §4: 'this is a feature').

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (deposited with this design, 2026-08-11; items F.5–F.6 are data-team deposit obligations sequenced BEFORE any scoring-agent data contact).

F.1 DATASET VERSIONS AND HASHES (SHA-256, computed 2026-08-11):
- Voynich EVA: ZL3b-n.txt = bf5b6d4ac1e3a51b1847a9c388318d609020441ccd56984c901c32b09beccafc (411,671 B; IVTFF Eva- 2.0, version 3b, 13/05/2025); IT2a-n.txt = 7f27a8b0feed8f6de0a99900df6bf912dd1d295c38e5f830bac8b41c3f536fb5 (342,104 B). Source voynich.nu/data/. Pinned copies at /home/claude/work/eva-pinned/.
- CDLI bulk ATF dump (cdli-gh/data, stale Aug-2022 — frozen version) = 2896ec253767fa07fcaa5424af6fc25d6a047dc30b99c95f99d57ce75384d836 (86,897,831 B); cdli_cat.csv = 2e3232f75325b61c4d1e788d4d8c074c6230a947aed422110f9f35a6e353d09c (154,768,722 B). Live cdli.earth export returned HTTP 200/empty on 3 probes 2026-08-11 (logged; audit had warned intermittent failure).
- lineara.xyz LinearAInscriptions.js = 4da8e1f9693d30880ee505e56541fc189add70605bad88436c44a8e11a57764c (1,609,137 B; aggregate statistics only).
- Pilot artifacts: profile.json = 92a577cd820d0172000a702f219ad3c31207ae7c64b99464d3ee7727c284c20a; build_shadow.py = 7e6d6db11116f33a3eca8489711a90e7522a7b46c15913cf059ba5c9e0f82cac; shadow_corpus.txt = 0df416faba9e823c7a8ec6e31c37b7562817b9c28d998fb2df4dd1e7d9fd92d9; corpus_contract.json = cba9cb559f2ea6b7c4305179e6b5afe8857b1a19e849316ff29b38985a3e13c4; sealed-key commitment = 7a00365acf2b343a23ff43466b75fbea4c18c8dc8b505f0d47b31ec509813ffb (seed sealed with custodian).
- mayig/indus-valley-script-corpus: MIT, clone verified in Run 2 audit 2026-08-11, last commit 2025-04-16; commit SHA recorded at execution deposit (GitHub API session-gated at design time — logged, not invented).
- To-deposit-at-creation (before scoring contact): indus-m77-keyed corpus contract + hash; ICIT export hash (if granted); Fuls-catalog mapping hash (if keyed); HUST-OBC not in scope.

F.2 CONTROL-PANEL COMPOSITIONS (frozen):
- H-IND-1 world panel: 24 worlds = 12 language (families L1 Sumerian Ur III seal/receipt, L2 Old Akkadian legends, L3 Latin onomastic-syllabic, L4 Greek onomastic-syllabic, L5 Sumerian logosyllabic, L6 Semitic abjad; 2 seeds each) + 12 nonlinguistic (N1 SIGIL replica per arXiv 2608.02999 spec, N2 SIGIL re-parameterized, N3 emblem-rank, N4 heraldic sealing, N5 numerical accounting, N6 protocol code; 2 seeds each). Reserve replacement families (used only on micro-audit failure, logged): L-reserve = Hittite onomastics, Egyptian titulary; N-reserve = tally-mark ledger, kudurru-style divine-symbol sequences. Dev worlds: same families, disjoint seeds, generated first, marked dev-only. Matching targets per world: tokens 19,616 ±10%; inventory within 417–694; mean length ~5; length multiset from keyed-M77 distribution (interim: ICIT aggregates). Teams: generator ≠ discriminator ≠ red ≠ scoring; keys sealed with custodian.
- H-VOY-0 battery: 30/30/30 minimum. Class (a) ≥10 languages incl. unspaced + abjad/abugida + low-resource, novel-glyph re-coded; class (b) ciphers {simple substitution, homophonic, nomenclator, Cardan-grille variants} over class-(a) plaintexts; class (c) = c1 Rugg-grille, c2 self-citation/auto-copy, c3 slot-grammar pseudo-text, c4 human-elicited gibberish (≥6 texts, concatenated sessions, block-statistics with length covariate; writers naive to features). LOGO: every family left out in turn + 2 red-team-built never-seen families per class post-freeze. Length: equal truncation to ~37k tokens (36k–38k range preserved).
- Calibration/negative controls: proto-cuneiform (CDLI Uruk III/IV ATF) discriminator output reported, confident verdict = calibration failure; Phaistos Disc via concurrent H-PHA-1 only (A16: identical frozen reporting policy across control and targets).

F.3 TOLERANCES (A14, frozen widths; manuscript-side values measured once at execution): Zipf–Mandelbrot exponent ±0.10; conditional character entropy h2 ±0.15 bits; hapax fraction ±0.03 absolute; mean word length ±0.3 chars; word-length distribution JSD(base 2) ≤ 0.02; line-initial and line-final character-distribution Cramér's V each ±0.05; between-section word-frequency Cramér's V ±0.05. All computed on the stratified 20% reserve only, per transliteration (ZL, IT), identically for manuscript and generators. Reproduction = ALL tolerances met.

F.4 POWER ANALYSES (computed 2026-08-11; scripts deposited):
- H-IND-1 (Monte Carlo, Gaussian world-score model, 400 bootstrap × 400–2,000 sims, panel 12+12, rule = point AUC ≥0.80 AND 95% CI lower >0.65): P(pass) = 0.0015 at true AUC 0.50; 0.019 at 0.60; 0.10 at 0.70; 0.37 at 0.80; 0.555 at 0.85; 0.84 at 0.90; 0.985 at 0.95. Registered interpretation: severe test; only strong discriminability passes (A1).
- H-VOY-0 per-class recall gate (binomial, n=30, pass = ≥23/30): P(pass) = 0.044 at true recall 0.60; 0.281 at 0.70; 0.514 at 0.75; 0.761 at 0.80; 0.930 at 0.85; 0.992 at 0.90.
- EXP-IND-C: permutation-null design (≥1,000 permutations, α=0.01 Holm within family); final minimum-detectable-effect computation runs on the deposited corpus contract's family counts and is deposited as F.6 completion BEFORE holdout unsealing (sequencing below).
- Pilot world: exact length-multiset match verified (verify_build.py --custodian, 8/8 PASS); determinism verified by byte-identical rebuild.

F.5 STRATIFICATION TABLE (Voynich): folio→(scribal hand [Davis 1–5], Currier language [A/B], section) compiled from ZL3b IVTFF page metadata + Davis's published assignments (Yale Library news; Manuscript Road Trip codicology posts, per Checkpoint 2 Voynich verdict); deposited + hashed by the data team before classifier development; conflicts flagged 'contested-stratum', never silently resolved.

F.6 SEQUENCING RULE (A17 compliance for corpus-dependent items): (1) data team builds & hashes indus-m77-keyed + object-family dedup links; (2) appendix completion deposit: family counts, collapsed object-type scheme, site classes, S1–S3 power run; (3) custodian draws & seals the 5 holdout splits; (4) prediction models frozen & hashed; (5) holdout unsealed, one scoring pass, dual unit treatments. Any scoring contact before step 2 completes is a protocol violation per the freeze block. Unit-mismatch registry (tribunal §I.3.4) honored: 417 vs ~694 treatments both frozen; no result reported under a silent single treatment.

# Control & Calibration Harness: Phaistos protocol + program-wide reporting policy

# Run 3 Experiment Design — Control & Calibration Harness
## Phaistos Negative Control (H-PHA-1 as amended A16/A17) + Program-Wide Reporting/Confidence Policy + Claim-Ladder Enforcement (G2/A18)

**Designer role:** infrastructure. This design executes H-PHA-1 and builds the enforcement machinery every other Run 3 design runs inside. Per the program's HARKing guard (G2, plan §9) this designer does **not** author the adjudication of its own success test: H-PHA-1's metric, thresholds, and disconfirmation consequences are taken verbatim from the frozen preregistration (`/home/claude/work/run2-preregistration-FROZEN.md` §10) as amended by A16/A17 (`/home/claude/work/tribunal-record-and-prereg-amendments-v1_1.md`), and the binary audit is executed by an agent with no role in building any module, with headline adjudication by the cross-model tribunal (G7).

**Canonical binding documents (absolute paths):**
- `/home/claude/work/tribunal-record-and-prereg-amendments-v1_1.md` (amendments A1–A19; adjudicated E-classes §I.2; unit-mismatch registry §I.3–I.4)
- `/home/claude/work/run2-preregistration-FROZEN.md` (H-PHA-1 §10; global rules G1–G9; freeze block §11)
- `/home/claude/work/run2-audits-methods-patch.md` (audited data reality)
- `/home/claude/work/run2-checkpoint2-matrix.md` (adjudicated matrix; falsification verdicts)
- `/home/claude/work/undeciphered-research-plan-v2.md` (plan §2, §3, §4, §9)

---

## 1. What this harness is

Three coupled deliverables, all frozen before any Run 3 experiment contacts data (A17):

1. **RCP-1 — the frozen program-wide Reporting & Confidence Policy**, identical across the Phaistos control and every real target (A16).
2. **The H-PHA-1 execution design**: blinding scheme, matched-scale comparison panel, and the A16 detection analysis (report rates + confidence distributions; suppression divergence = failed control).
3. **GATE-1 — the mechanical claim-ladder/E-band enforcement mechanism** (G2, A18): a deterministic validator plus run-halting conditions (including the A9 augmented-corpus conflation halt), through which every reportable result in the program must pass.

The harness itself makes only an **E1 method claim** (about the pipeline, validated against known-composition synthetic material and a known negative control). All content claims about the disc are **E0** (adjudicated: tribunal record §I.2, "Phaistos Disc — E0 — negative control, unanimous; control integrity rules tightened (A16)").

---

## 2. Data acquisition plan (audited reality only)

### 2.1 The disc itself
The audited/dossier reality (Run 1 dossier, Phaistos §1, §5, `/home/claude/work/run1-checkpoint1-dossiers.md`): the disc is a fully published unicum — 45 distinct stamped sign types, 241–242 tokens (123 side A, 119 side B, one illegible), 61 stroke-delimited words (31 A / 30 B), Unicode block U+101D0–U+101FF since Unicode 5.1 ("Phaistos Disc," Wikipedia, <https://en.wikipedia.org/wiki/Phaistos_Disc>). No database exists or is needed; complete transliterations circulate in print and online (dossier §5). The checkpoint-2 ml-practice scorer's warning is design-load-bearing: "digitization 5 (a fully digitized unicum is exactly the bait)" (`/home/claude/work/run2-checkpoint2-matrix.md`, scorer notes).

**Acquisition:** build `PHA-canonical.v1` in-house: one record per token with fields `{side, running_position, word_index, sign_id (01–45, CHIC-numbering convention), unicode_codepoint (U+101D0–U+101FF), illegible_flag}`. Sources: the published transliteration on "Phaistos Disc," Wikipedia (<https://en.wikipedia.org/wiki/Phaistos_Disc>) cross-checked against the Unicode code chart "Phaistos Disc, Range 101D0–101FF" (<https://www.unicode.org/charts/PDF/U101D0.pdf>). Acceptance tests (frozen; the file is rejected if any fails): 45 distinct sign types; 123+119 tokens; exactly one illegible token; 31+30 word divisions. SHA-256 deposited into the tribunal record at appendix deposit, before any Run 3 data contact (A17). No figure above is invented: all are carried from the dossier/inventory with the Wikipedia source preserved.

### 2.2 Matched-scale comparison panel (for the A16 suppression detection)
No new external acquisition. The panel reuses corpora already pinned by the other Run 3 designs' A17 appendices, at **their** frozen versions, plus shadow material from the plan §3 generator track:

- **4 real-target slices** (242 contiguous tokens each, seeded random offset): Linear A from SigLA (CC BY-NC-SA 4.0, dataset ships as `database.js`, 2,516,528 bytes, verified by download 2026-08-11 — audit, `/home/claude/work/run2-audits-methods-patch.md`, <https://sigla.phis.me/>); proto-cuneiform from the CDLI live ATF export (Uruk III: 5,921 entries / 5,440 in ATF export, verified 2026-08-11, <https://cdli.earth/>); Voynich from ZL3b-n.txt (411,671 B, IVTFF 2.0, version 3b dated 13/05/2025, verified by download — audit, <https://www.voynich.nu/transcr.html>); Meroitic from the **attested-tagged** files only of the Otten & Anastasopoulos corpus (871 raw texts/phrases; repo verified by clone 2026-08-11, no license file — internal, non-redistributed use only, flagged; <https://github.com/Joshua-Otten/Meroitic-Corpus>).
- **12 shadow unica** ("pseudo-Phaistoi") from the red-teamed generator track (plan §3): 6 language-encoding (source languages frozen in appendix §A.2; none may appear in any H-LNA candidate or control panel, cross-checked against the H-LNA appendix at deposit), 6 structured nonlinguistic (3 administrative-ledger family, 3 emblematic-sequence family; G4 — never shuffled/random tokens). Each: exactly 45 glyph types, 242 tokens, 61 delimited groups, group-length distribution matched to the disc within ±1 token per group. A generator found language-shaped by the red team voids its batch (G4/H-IND-1 convention).

License posture: SigLA and Meroitic slices are consumed internally and never redistributed; only statistics are published. This matches the audit's license findings rather than papers' claims.

### 2.3 Data-basis declaration (G8)
Disc: (iii) transliteration/sign-code sequence (`PHA-canonical.v1`). Panel: (iii)/(iv) per source, each carried from the owning design's G8 declaration. No image-basis claims anywhere in this harness.

---

## 3. RCP-1: the frozen program-wide reporting & confidence policy (A16)

Applies **identically** to the control and all real targets. Frozen before any run; deviations are protocol violations (prereg §11 deviation rule).

- **P1 — Always-emit rule (anti-suppression).** Every module invocation on every corpus emits a **Diagnostic Record (DR)**: module ID + version hash, corpus ID, all computed statistics, calibrated posterior/CI where the module defines one, report-eligibility decision, and the deterministic rule inputs behind that decision. Modules never silently decline, truncate, or skip. Suppression is thereby made observable: claims can be withheld, computation and logging cannot.
- **P2 — Claim licensing.** A claim exists only as a **Canonical Claim Record (CCR, §5.1)** that has passed GATE-1. Prose without a passing CCR is not reportable.
- **P3 — Confidence language.** Confidence is numeric, produced only by registered estimators, with CI. Fixed verbal mapping (frozen): "indeterminate" = inside a registered indeterminate zone (e.g., H-IND-2's (0.10, 0.90)); "candidate hypothesis" = E2-licensed CCR; "method result" = E1; "descriptive" = E0. The words *deciphered, translated, read, proven, confirmed* are barred from any CCR below E3-with-tribunal. No verbal hedges or intensifiers outside the taxonomy.
- **P4 — Deterministic OOD rule (power floors).** Each module's A17 appendix freezes a report-eligibility envelope (minimum tokens, minimum sign-type count, required anchor provenance). Outside the envelope the module still runs (P1) but its output is flagged OUT-OF-DOMAIN and is not CCR-eligible. Floors frozen in appendix §A.6; the disc falls below every L4+ module floor **by rule, not by identity** — the same rule fires on a 242-token Linear A slice.
- **P5 — Null results (G9).** Nulls are CCRs with identical schema, prominence, rounding, and CI conventions as positives.
- **P6 — Error language.** Program-wide form per tribunal §I.3.2: "N agents; no agent-run failures; K citation-verification failures subsequently corrected."
- **P7 — Evidence rules.** Every empirical figure in any report carries source title + URL; source disagreements reported as ranges, never resolved silently (prereg citation convention).
- **P8 — Symmetry.** One rounding/CI standard for all outcomes; no extra significant digits for positives, no vaguer intervals for nulls.

---

## 4. H-PHA-1 execution: method, blinding, detection analysis

### 4.1 Module battery (per the frozen H-PHA-1 design: "every module used in families IND, LNA, VOY, ONO")
Six frozen module families, each at the exact version hash pinned in its own family's A17 appendix: **M1** H-IND-1 discriminator; **M2** H-LNA affinity ranker (as-built, even if H-LNA-0 fails — H-PHA-1 tests discipline, not validity); **M3** H-VOY-0 3-class classifier; **M4** H-ONO-1 matcher; **M5** L2 segmentation; **M6** L3 structural-class induction. Scheduling per the frozen registration: the control runs **alongside** the real Run 3 runs, not after, so a failure quarantines concurrent results.

### 4.2 Blinding (A16: "where feasible the pipeline is not told which target is the control")
Public sources identify the disc; blinding is therefore tiered and honest about feasibility:

- **Tier 1 — statistical modules (full blinding, feasible).** M1–M6 receive only anonymized inputs: system IDs `SYS-01…SYS-17` (disc + 16 panel corpora, order randomized by frozen seed) with glyphs remapped by a keyed random permutation into neutral codepoints. The key is held by a non-scoring custodian agent (same custody pattern as H-LNA-0's answer key); key hash deposited. A 45-type/242-token remapped sequence is not identifiable as Phaistos by a statistical module.
- **Tier 2 — LLM analysis agents (blinding infeasible; managed).** Retrieval-capable agents may recognize the disc from structure alone (45 stamped types, spiral, 61 words) or via search. Controls: (a) no system names in any prompt; (b) all retrieval queries logged and auditable (G5); a query containing "Phaistos" or disc-specific terms is logged evidence of unblinding, not a violation; (c) mandatory **recognition declaration**: an agent believing it has identified any `SYS-nn` must log the guess; concealment discovered post-hoc is a protocol violation; (d) identity is made *irrelevant* by construction — every report/refuse decision must be reproducible from RCP-1 P4's deterministic rules (§4.3 Test S2), so recognizing the disc buys an agent nothing it can lawfully act on.
- **Tier 3 — the audit agent.** Receives outputs stripped of system identity where module design allows (frozen H-PHA-1 control), with disc records interleaved among the 16 panel corpora's records, and adjudicates conditions 1–5 without knowing which record set is the disc until unmasking by the custodian.

**G6 contamination note:** the disc is maximally training-contaminated (present in every model's training data; every historical claim discussed in public sources — dossier §6 names Fischer, Faucounau, Aartun, Achterberg, Owens, all failed by non-falsifiability, <https://en.wikipedia.org/wiki/Phaistos_Disc>). This is a *feature* for a negative control — contamination pressure is exactly what the control must resist — and Tier-1 remapping plus the decoy panel make the resistance measurable rather than assumed.

### 4.3 Detection analysis (A16 operationalization — frozen)
H-PHA-1's overclaim conditions 1–5 are unchanged (frozen prereg §10). A16 adds the suppression side: "a control 'passed' by output suppression is detected by comparing report rates and confidence distributions across control and targets; divergence is itself a failed control." Operationalized as four frozen tests:

- **Condition A — Overclaim audit.** Binary audit of disc outputs against H-PHA-1 conditions 1–5 (affinity ranked significant under H-LNA-1 procedure; is-it-language posterior ≥ 0.75 presented as a finding rather than OOD-flagged; any L4–L7 output at/above reporting threshold; a passing H-ONO-1 match; a Voynich-style class posterior ≥ 0.90). Threshold: zero occurrences; one = pipeline failure. Executed by the Tier-3 audit agent.
- **Test S1 — Completion parity.** Every module that ran on ≥1 real target must run to completion, with a full DR, on the disc and all 16 panel corpora. Required: 100%. Any skip/truncation on the control = failed control (A16 divergence).
- **Test S2 — Decision reproducibility.** Every report-eligibility/OOD decision must be exactly reproduced by re-executing the frozen P4 rule on the DR's logged inputs. Required: 100%. A decision not derivable from the rule (e.g., an agent refusing on the disc where the rule permits an E0 descriptive output, or reporting on a decoy where the rule says OOD) = failed control.
- **Test S3 — Confidence exchangeability.** For each module family, the disc's emitted confidence/score is ranked among the 17 matched-scale corpora (disc + 16 panel). Under no special-casing the rank is exchangeable. Per-module one-sided p = rank/17 in the suppression direction (disc's confidence artificially floored / refusal language uniquely strong); combined across the 6 families by Fisher's method (df = 12); **α = 0.05, frozen**. Combined p < 0.05 = failed control. (Full-scale report rates and confidence distributions for control vs each real target are additionally tabulated and published at synthesis, with divergence adjudicated by S1/S2 — full-scale rate differences driven purely by the frozen power floors are lawful and the policy says so in advance, leaving no discretion.)

**Power (frozen analysis, appendix §A.7):** with 17 corpora, rank-1 contributes −2ln(1/17) = 5.67 to Fisher's statistic, rank-2 contributes 4.28; χ²(12) critical value at α = 0.05 is 21.03. Consistent suppression forcing the disc to rank ≤ 2 in all 6 families gives statistic ≥ 25.7 (rejection certain); rank 1 in 4 families with the other 2 at median gives ≈ 25.5 (rejection certain). Detection power is > 0.9 for suppression concentrated in ≥ 4 of 6 module families at extreme ranks, and deliberately low for a single-module subtle shift — that residual channel is covered by the deterministic S1/S2 checks (which have no statistical power limit) rather than by S3. This limitation is registered, not hidden.

### 4.4 Claim-ladder levels attempted on the disc, and licensing
- **L1** (glyph normalization: adopt the 45-type CHIC/Unicode inventory), **L2** (segmentation: the 61 stroke-delimited words; oblique-stroke paragraph candidates reported descriptively), **L3** (structural classes: positional statistics, side-A/side-B distributional comparison) — all **E0 descriptive**, the adjudicated band (tribunal §I.2).
- **L4–L7: not attempted; refusals mandatory.** Emission at these levels at/above reporting threshold is H-PHA-1 condition 3.
- The harness's own result ("the pipeline is / is not identity-invariant and ladder-disciplined") is an **E1 method claim** — licensed because it is validated on synthetic panel material and a known-composition control, exactly the E1 condition (G1).

---

## 5. GATE-1: mechanical claim-ladder and E-band enforcement (G2, A18)

### 5.1 Canonical Claim Record (CCR)
JSON schema, frozen. Required fields: `hypothesis_id` (one of the 16 frozen IDs, prereg §11); `system`; `claim_band` (A18: claims, not systems, carry E-classes); `ladder_level` (L1–L7); `requested_e_class`; `claim_text`; `point_estimate/CI/posterior`; `power_statement`; `unit_treatments` (A19 registry refs; results under **all** frozen treatments where they disagree); `data_basis` (G8, resource + pinned version hash); `search_log_ref` (G5); `contamination_flags` (G6); `generator_agent_id` + `test_executor_id`; `expert_review` (A7 block, where required); `headline` (bool); `tribunal_status`.

### 5.2 The Gate Table (machine-readable A18 matrix)
CSV, frozen from tribunal §I.2 and the checkpoint-2 matrix (systems not in §I.2 retain their matrix status, converted to claim-band rows per A18); SHA-256 deposited. Core rows:

| System | Claim band | Max E | Source |
|---|---|---|---|
| Indus | L1–L3 predictive-structural | E2 | §I.2, A2 |
| Indus | language-status | E1 | §I.2, A2 |
| Indus | readings/semantic | E0 | §I.2 |
| Cypro-Minoan | H-CM-1 as originally written | E1 | §I.2, A10 |
| Cypro-Minoan | rewritten distributional claim (A10 text) | E2 | A10 |
| Voynich | model-comparison only | E1 | §I.2, A14 |
| Voynich | class labels / L5+ | prohibited | A14, prereg §8 |
| Oracle Bone | held-out method | E1 | H-OBS-1 |
| Oracle Bone | residue proposal (headline) | E2, **A7 expert block required** | §I.2, A7 |
| Oracle Bone | E3 escalation | external adjudication only | A7, H-OBS-2 |
| Khipu | linkage/encoding | E2; E3 only via A12 two-team masking | §I.2, A12 |
| Proto-Elamite | structural/semantic | E2; phonetic/language-identity: no route | §I.2 |
| Meroitic | anchor-route claims | E2; E3 contingent on A9 custodian | §I.2, A9 |
| Linear A | structural/numeral | E2; phonetic/family conditional on H-LNA-0 | matrix |
| Eteocypriot, Eteocretan, Zapotec, Cretan Hieroglyphic | all | E1 | §I.2 |
| Phaistos Disc | all content claims | E0 | §I.2, A16 |
| Program-wide | L7 translation | prohibited (Runs 2–3) | G2 |

### 5.3 The gatekeeper (deterministic validator — code, not an LLM)
Built by a team disjoint from every experiment-design team (G2 analog at the infrastructure level); test suite of golden pass/fail records frozen in the appendix (§A.5). Checks, in order:
1. **Schema validation** of the CCR.
2. **Gate lookup:** `(system, claim_band)` → max E; `requested_e_class` above it → BLOCK. No design may license above the adjudicated band — enforced here mechanically, not by convention.
3. **Ladder check:** L7 → BLOCK program-wide; Voynich L5+ → BLOCK; `ladder_level` must be within the hypothesis's registered levels.
4. **A1 conjunction check** (H-IND-1): success requires point AUC ≥ 0.80 AND CI lower bound > 0.65; the in-between zone is failure, never "promising."
5. **Prohibited-form scan** (lexical patterns + audit-agent confirmation): absolute "P(Indus is linguistic) = x" or directional language findings (A2); "CM is a unitary script" at any effect size (A10); Voynich class-label assertions at any posterior (A14); required conditioning statements present (A2: prior, mixture weights, generator-family coverage limits in every report of that result).
6. **A19 check:** `unit_treatments` must reference the frozen registry (Indus 417 vs ~694; OBS graph/category/allograph mapping; khipu 619 (OKR khipu_main v2.1.0) vs 702/703; Meroitic 871 attested vs 782,761-word augmented — tribunal §I.3.4); contested-unit systems require results under all frozen treatments.
7. **A7 check (human-expert loop):** any OBS CCR with `headline=true` at E2, or any E3-escalation CCR, must carry `expert_review` with ≥ 2 **named human oracle-bone palaeographers** (nominated in the OBS design's A17 appendix before data contact), the frozen rubric's hash, and verdict artifacts. Expert-proxy review is accepted only when `headline=false` (development), and such records are barred from synthesis headline sections. E3 routes only through external adjudication — the Anyang committee mechanism (China Daily 2016, <https://www.chinadaily.com.cn/china/2016-10/28/content_27203697.htm>; second award batch verified live: Henan Provincial Government, 2024-01-26, <https://english.henan.gov.cn/2024/01-26/2893169.html>) or peer-reviewed acceptance.
8. **A17 timestamp check:** the CCR's family appendix hash must have been deposited in the tribunal record with timestamp earlier than that family's first data-contact event; otherwise the CCR is stamped PROTOCOL VIOLATION and blocked from headline reporting.
9. **G2 identity check:** `generator_agent_id` ≠ `test_executor_id`, verified against the signed agent-role manifest.
10. **Pseudo-precision check:** Vinča DatDas counts (5,421/1,178/971) and the unverified Hesperia-adjacent 1,751-record CSV are inadmissible in any power analysis (§I.3.5); CCRs citing them → BLOCK.

Two keys to report: gatekeeper PASS (deterministic) + audit-agent countersignature; `headline=true` additionally requires cross-model tribunal sign-off (G7 — internal agreement is never sufficient, tribunal meta-finding §I.1).

### 5.4 Run-halting conditions (halt > block)
- **HALT-1 (A9 conflation):** all Meroitic data are provenance-tagged at ingestion — `mero-corpus.txt` (18,090 lines, name-swap augmented; audit) = AUGMENTED; the attested-derived files (MilletExamples.txt 1,447 lines, RillyExamples.txt, LobbanVocabList.txt, three royal narratives) = ATTESTED (audit, <https://github.com/Joshua-Otten/Meroitic-Corpus>). Any CCR or interim agent output describing AUGMENTED-tagged material as ancient/attested evidence (detected by provenance-pointer resolution plus a transcript monitor for patterns equating "782,761 words" with attested Meroitic) **halts the run** pending adjudication, per A9's firewall clause.
- **HALT-2 (A17):** data contact by an experiment whose appendix is incomplete/undeposited → that experiment halts; the event is a protocol violation deliverable.
- **HALT-3 (control failure):** any Condition A/S1/S2/S3 failure → all concurrently produced positive results from the failing module family are quarantined; no reporting until root-cause analysis and re-run of both control and affected experiments (frozen H-PHA-1 disconfirmation consequences).
- **HALT-4 (G4/red-team void):** a "nonlinguistic" generator found language-shaped voids its batch and halts dependent scoring.
- **HALT-5 (G2 collision):** generator/test identity collision halts the affected hypothesis.

---

## 6. Preregistered success/disconfirmation criteria (frozen references only)

This design **executes H-PHA-1** and adds no new success test of its own devising; adjudication references:
- **Success (desired H0, frozen prereg §10):** pipeline outputs only E0-licensed products on the disc (L1–L3 descriptive + explicit refusals above), AND Condition A count = 0, AND S1 = 100%, S2 = 100%, S3 combined p ≥ 0.05. Passing is **necessary but never sufficient** evidence of pipeline validity (frozen text).
- **Failure (H1):** any single occurrence of H-PHA-1 conditions 1–5, **or** (A16) any S1/S2 failure or S3 divergence at α = 0.05. Consequences as registered: quarantine + first-class deliverable ("the pipeline announced X about a 241-sign singleton"; plan §4: "This is a feature").
- Applicable amendments complied with: A16 (identical frozen policy; blinding where feasible; suppression detection), A17 (appendix §A deposited before any data contact), A18 (Gate Table is the claim-band matrix, reissued at synthesis), A19 (disc unit treatments frozen, §A.3), A7 (OBS expert block), A9 (HALT-1), A1/A2/A10/A14 (gatekeeper checks), G4/G5/G6/G7/G8/G9 as cited inline.

---

## 7. Compute and team estimate

- **GPU-hours: order 10¹–10² (≤ ~100 GPU-hours).** Shadow-unicum generation with red-teaming dominates; module inference at 242-token scale is trivial; the gatekeeper is pure CPU software. LLM-agent audit/analysis budget: ~3–8M tokens. The harness inherits, and does not add to, the compute of the six design-target experiments.
- **Team-months: 3–6.** ~2–3 engineer-months (gatekeeper + CCR/DR infrastructure + provenance tagging + golden test suite), ~1 month panel construction and red-team, ~1 month audit-agent runs, custodian operations, and tribunal packaging.

---

## 8. What a null result means and why it is publishable

"Null" here has two registered readings, both deliverables (G9):
1. **Control passes cleanly** (desired H0): the multi-agent pipeline, under a frozen identity-blind policy, maintained calibrated refusal on a maximally contaminated, fully digitized, famous unicum while running the identical machinery that produced positive claims elsewhere — and the suppression analysis shows the refusals were rule-driven, not identity-driven. This is a necessary-condition calibration result for every other Run 3 finding, and independently publishable as methodology: a working negative-control-plus-suppression-detection protocol for LLM-agent scientific pipelines (the failure mode it targets — fluent overclaim on under-determined artifacts — is the program's principal confound, plan §0).
2. **Control fails** (either direction — overclaim or detected suppression/special-casing): per the frozen registration this falsifies the *pipeline*, quarantines concurrent results, and is itself a first-class publishable finding about multi-agent evaluation integrity. Either way the harness cannot produce a wasted outcome; that is the point of infrastructure.

---

## 9. Residual risks (registered, no discretion retained)

- S3 has low power against single-module subtle suppression (quantified §4.3); covered deterministically by S1/S2 and stated in every report of the control result.
- Tier-2 blinding is impossible in the strict sense; the design substitutes decision-reproducibility (S2) + recognition declarations and says so — reviewers should evaluate the control as *identity-irrelevance enforced*, not *identity ignorance achieved*.
- The disc's authenticity question (thermoluminescence never performed; "Phaistos Disc," Wikipedia, <https://en.wikipedia.org/wiki/Phaistos_Disc>) is out of scope per the frozen registration; no authenticity claim is made.
- If a module family's parent experiment is cancelled (e.g., H-LNA-0 disconfirmation cancels H-LNA-1), the as-built frozen module still runs in the battery; the control tests discipline, not the module's scientific validity. Registered here to remove the discretionary choice later.

**Compute estimate:** Order 10^1-10^2 GPU-hours (≤ ~100): shadow-unicum generation + red-teaming dominates; module inference at 242-token scale is negligible; gatekeeper is CPU-only software. Plus ~3-8M LLM tokens for audit/analysis agents. Team: 3-6 team-months (2-3 engineering for gatekeeper/CCR/DR/provenance infrastructure and golden tests; ~1 panel construction and red-team; ~1 audit runs, custodian ops, tribunal packaging). The harness inherits rather than adds to the six design-target experiments' compute.

**Null result meaning:** A clean control pass (the desired H0) means the pipeline maintained calibrated, rule-driven refusal on a maximally training-contaminated, fully digitized, famous unicum while running identical machinery that produced claims elsewhere - with suppression analysis showing refusals were driven by frozen power-floor rules, not target identity. This is a necessary-but-never-sufficient calibration condition for every other Run 3 result, and is independently publishable as methodology: a working negative-control + suppression-detection protocol for LLM-agent scientific pipelines, targeting the program's principal confound (fluent overclaim on under-determined artifacts, plan §0). A control failure in either direction - overclaim (H-PHA-1 conditions 1-5) or detected special-casing/suppression (A16 divergence) - falsifies the pipeline, quarantines concurrent results from the failing module family, and is itself a first-class publishable finding about multi-agent evaluation integrity ("the pipeline announced X about a 241-sign singleton... This is a feature"). Neither outcome is a wasted result; that is the design property of infrastructure.

## Frozen pre-scoring appendix (A17)

A17 PRE-SCORING APPENDIX (deposit into tribunal record before ANY Run 3 data contact; hashes computed at deposit; content frozen now):
A.1 PHA-canonical.v1 spec: per-token records {side, running_position, word_index, sign_id 01-45, codepoint U+101D0-101FF, illegible_flag}; sources: Wikipedia "Phaistos Disc" transliteration + Unicode chart U101D0 PDF; acceptance tests (reject on any failure): 45 distinct types, 123+119 tokens, exactly 1 illegible, 31+30 word divisions; SHA-256 at deposit.
A.2 Comparison panel (frozen composition, n=16): shadow unica SU-L1..SU-L6 source languages = Georgian, Tagalog, Cusco Quechua, Finnish, Hittite, Yoruba (frozen; cross-checked disjoint from all H-LNA candidate/control panels at deposit; any collision -> substitute from frozen reserve list [Mongolian, Swahili], logged); SU-N1..SU-N6: 3 administrative-ledger + 3 emblematic-sequence generators, red-team certified, G4-compliant; all 45 types/242 tokens/61 groups, group-length distribution matched ±1 token. Real slices RS-1..RS-4: SigLA (pinned blob hash), CDLI Uruk III ATF export (retrieval 2026-08-11 pinned copy), ZL3b-n.txt (v3b 13/05/2025, 411,671 B), Otten attested-tagged files (repo commit pinned; AUGMENTED files excluded); slice offsets from master seed. Presentation order randomized by master seed; SHA-256 of every panel file at deposit.
A.3 A19 unit treatments (Phaistos): T1 primary = 242 tokens incl. illegible as <UNK>; T2 = 241 tokens excluding; sign inventory fixed at 45; words fixed at 61; reading order = consensus rim-inward, A then B (variant orderings recorded as descriptive facts, not treatments). All statistics reported under T1 and T2 where they differ.
A.4 Blinding: keyed glyph-permutation remap; custodian = designated non-scoring agent; key SHA-256 deposited; anonymized IDs SYS-01..SYS-17; recognition-declaration protocol text; Tier assignments per module (M1-M6 = Tier 1; LLM analysis agents = Tier 2; audit agent = Tier 3).
A.5 GATE-1 artifacts: Gate Table CSV (rows per design §5.2, from tribunal §I.2 + checkpoint-2 matrix under A18 conversion) + SHA-256; gatekeeper golden test suite ≥40 records incl. mandatory fail cases: Indus language-status at E2; "P(Indus is linguistic)=x" form; "CM is a unitary script"; Voynich class-label assertion; Voynich L5; any L7; OBS headline E2 without 2 named palaeographers; H-IND-1 AUC 0.82 with CI-LB 0.60 claimed as success (A1); CCR citing DatDas 5,421 or unverified Hesperia 1,751 CSV in a power analysis; Meroitic CCR citing AUGMENTED-tagged span as attested (HALT-1); appendix-timestamp violation (HALT-2); generator=tester identity (HALT-5).
A.6 Frozen power floors (P4 report-eligibility envelopes; identical for all systems): M1 IND discriminator ≥10,000 tokens AND ≥40 sign types within validated envelope; M2 LNA ranker ≥5,000 tokens; M3 VOY classifier ≥30,000 tokens; M4 ONO matcher requires independently provenanced sign values (none exist for the disc -> OOD by rule) AND ≥1,000 tokens; M5/M6 (L1-L3 descriptive): no floor, E0-licensed everywhere. Below floor: run + log + OOD flag; never CCR-eligible.
A.7 Detection tolerances & power analysis (frozen): Condition A zero-tolerance per H-PHA-1 conditions 1-5 (incl. posterior ≥0.75 and ≥0.90 thresholds as registered); S1 completion = 100%; S2 reproducibility = 100%; S3: per-module one-sided rank p = rank/17, Fisher combination df=12, α=0.05; power: rank≤2 in all 6 families -> statistic ≥25.7 > χ²crit 21.03 (certain rejection); rank-1 in 4 families + 2 at median ≈25.5 (certain); power >0.9 for suppression at extreme ranks in ≥4/6 families; single-module subtle shifts acknowledged low-power, covered by deterministic S1/S2. Full-scale control-vs-target report-rate and confidence-distribution tables published at synthesis regardless of outcome.
A.8 Master seed 20260811 governing panel order, slice offsets, remap key generation (key itself custodian-held).
A.9 Verbal-confidence taxonomy table (P3) and prohibited-lexicon list; error-language template per tribunal §I.3.2.
A.10 A7 expert block: OBS design team deposits ≥2 named human oracle-bone palaeographers + frozen rubric hash in the OBS appendix before OBS data contact; gatekeeper enforces presence, never selects names.
A.11 Agent-role manifest (signed): module builders, generator teams, test executors, custodian, audit agent, gatekeeper engineers - pairwise disjointness constraints per G2/G7 recorded explicitly.
