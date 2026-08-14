# Undeciphered Languages & Scripts: Research Plan v2

**Prepared for:** Laurent Heller · August 11, 2026
**Revision basis:** v1 (Aug 4) + adversarial review by GPT 5.6-Sol + citation verification (all 10 load-bearing citations confirmed; see §10).

---

## 0. The question (reframed)

Not *"Can frontier AI decipher undeciphered languages?"* but:

> **Under what information conditions can frontier AI produce independently verifiable new knowledge about undeciphered writing systems?**

This reframing is load-bearing. It prevents the project from being seduced by fluent output — an LLM's strongest capability, plausible language production, is this experiment's principal confound. Every design choice below exists to keep that confound caged. A rigorous null result ("AI cannot distinguish linguistic from structured nonlinguistic encoding at Indus-scale corpora") is a success under this framing.

## 1. Four problem shapes (unchanged from v1)

| Shape | Definition | Examples |
|---|---|---|
| **A** | Unknown script + unknown language, no bilingual | Indus, rongorongo, Proto-Elamite, Byblos, Phaistos |
| **B** | Partially readable script + unknown language | Linear A, Cypro-Minoan, Cretan Hieroglyphic |
| **C** | Readable script + opaque language | Etruscan, Meroitic, Paleohispanic, Eteocretan, Eteocypriot |
| **D** | Contested — may not encode language | Voynich, khipu (narrative), Vinča, Rohonc |
| **E** *(new)* | Partially solved system with unsolved units | Oracle Bone (~3,000 of ~4,500 characters undeciphered), Khitan | 

Shape E is new and methodologically central: unsolved units embedded in a solved system permit genuine held-out evaluation — withhold known characters, test recovery. The 2024–26 Oracle Bone literature (OBSD, CipherOBS, AlphaOracle, HieroSA) already demonstrates this design.

## 2. The evaluability gate (replaces the weighted rubric)

Evaluation class is a **gate, not a weight**. It determines what kind of claim a project is licensed to make; tractability is scored only *within* class.

| Class | What's possible | Permitted claim |
|---|---|---|
| **E0** | No independent falsification exists | Descriptive/structural analysis only — no decipherment claims |
| **E1** | Synthetic or previously-deciphered benchmark | Method-development claims |
| **E2** | Held-out real evidence; independently checkable predictions | Candidate decipherment hypotheses |
| **E3** | Prospective external confirmation | Strong decipherment claims |

Within-class tractability score: corpus size; text length/genre diversity; priors (related scripts, candidate families, anchors); digitization quality for machine consumption; confidence the system encodes language.

**Verification standards (tightened from v1):**
- A prediction counts only if it concerns something *externally observable independently of the decipherment*: object type, provenance, independently recognizable ideograms, numerical quantities, names independently attested elsewhere, sign values later established from independent parallels. "Predicting the reading of a new text" does not count — no one knows the reading.
- Onomastic arguments require preregistration: candidate name set, allowed phonological transformations, sign values learned independently of the target name, matching score, null distribution, acceptable coincidence probability. Without these, "this looks like Knossos" is horoscope logic.

## 3. Shadow decipherments (new — the methodological centerpiece)

Construct synthetic "unknown" corpora from *known* languages: replace signs with novel glyphs, destroy boundaries, introduce palaeographic variants, remove bilinguals, damage and truncate to match the target system's token count, text-length distribution, and available priors. Then measure what the AI pipeline actually recovers — against an answer key we secretly hold.

Two families:
- **Linear-A-shaped worlds:** a real language corpus degraded to Linear A's information conditions. Tests whether language-family ranking, segmentation, and phonetic hypothesis methods work *at that information level* before anyone runs them on the real thing.
- **Indus-shaped worlds, paired:** one encoding language, one encoding a meaningful *nonlinguistic* administrative/emblematic system, matched on corpus size, sequence length, sign inventory. Tests whether any statistic can tell them apart. Per the August 2026 non-specificity result (arXiv 2608.02999), the null for "is it language?" must be structured meaningful nonlinguistic systems — never random or shuffled tokens, which every published test trivially beats.

Shadow benchmarks also eliminate training contamination: I have read about Linear B's decipherment; re-deriving it proves nothing. Randomized shadow scripts remove that leak. They likewise guard against restart-exploitation (Tamburini's critique): methods tuned by repeated restarts against a known answer can't transfer to genuinely unknown scripts.

**Scope honesty:** full benchmark construction and model trials are a research program, not a session. Run 3 delivers the *designs* plus one small pilot shadow world; the shadow-generator itself gets red-teamed (a "nonlinguistic" generator that is secretly language-shaped breaks the control).

## 4. The claim ladder (new)

No agent is ever asked to "translate." Claims advance through levels, each inheriting constraints from the one below, each gated by preregistered tests:

L1 glyph normalization → L2 segmentation → L3 structural classes → L4 grammatical/semantic roles → L5 phonetic hypotheses → L6 lexical correspondences → L7 translation.

L7 output is prohibited unless L1–L6 survive their registered tests. The agent that generates a candidate hypothesis never defines its own success test.

**Negative control:** Phaistos Disc runs through the full pipeline. If the pipeline announces a decipherment of a 241-sign singleton, the pipeline has failed. This is a feature.

## 5. Preregistered nulls (new — written before any agent sees results)

Every substantive claim in Runs 2–3 gets H0/H1, metric, threshold, controls, and disconfirmation condition, deposited before scoring. Examples:

- **Indus:** H0 — observed sequence structure is no more diagnostic of natural language than matched structured nonlinguistic systems. The negative systems must be sophisticated administrative/emblematic generators, not shuffled tokens.
- **Linear A family ranking:** H0 — apparent affinity with family X is no stronger than affinity generated against historically/geographically plausible unrelated controls given the same phonological degrees of freedom. Success requires the method to first identify known relationships in information-matched shadow corpora, with stability under sign-value uncertainty and segmentation variation.

## 6. Inventory changes

Additions/corrections to the v1 seed table (full table carried forward otherwise):

| Change | Rationale |
|---|---|
| **Add Oracle Bone undeciphered subset** (~3,000 chars; large corpus; active 2024–26 ML literature) | Best evaluation environment in the field; shape E |
| **Add Cretan Hieroglyphic** as its own row (~300+ docs) | Central undeciphered Aegean system; was a v1 table omission |
| **Split "Iberian/Tartessian"** into Northeastern Iberian, Southeastern Iberian, Southwestern/Tartessian | Different decipherment status per system; one experimental object was sloppy |
| **Add Eteocretan, Eteocypriot** to shape C | Completeness under the C definition |
| **Add proto-cuneiform** as calibration case (not headline inventory) | Semantics, numerics, and linguistic encoding come apart — useful control |
| **Khitan reclassified** to shape E alongside Oracle Bone | Same solved-system-unsolved-units structure |

## 7. Candidate priority for Run 3 (re-ranked for evaluability, not glamour)

1. **Oracle Bone undeciphered characters** — E1/E2 achievable now (held-out known characters = real answer key); frontier work active; expert community exists for validation.
2. **Meroitic** — readable script, ~2,000 texts, machine-readable corpus established (Otten & Anastasopoulos 2025); incremental linguistic discovery is realistic; E2 plausible via loanword/toponym anchors.
3. **Linear A** — enough structure and priors to be interesting; extraordinary confirmation-bias hazard (everyone has a favorite family); shadow-world validation mandatory before any real-corpus claim.
4. **Cypro-Minoan** — sign-inventory and palaeographic clustering questions are tractable and have technical precedent; corpus tiny for anything more.
5. **Khipu** — record linkage against Spanish colonial documents is genuinely falsifiable (E2); structured data already exists in the Open Khipu Repository.

**Indus** stays in the project as the *stress test of the methodology* — the paired shadow-world experiment — not as a decipherment candidate. **Phaistos** is the negative control.

## 8. Architecture v2 (evidence ledger + blind judging)

Same three-run checkpoint structure; internal discipline substantially rebuilt:

**Run 1 — Inventory & Dossiers (~15 agents).**
- Agents start from the two verified surveys (Sommerschield et al. 2023; Braović et al. 2024) rather than rediscovering the bibliography; sweep effort goes to what the surveys *don't* cover — post-2023 work, non-Aegean systems, the long tail.
- Discovery agents (5, by region/shape) → **evidence agents** that do nothing but extract claims, methods, datasets, evaluation designs, and exact citations from primary sources into an **immutable structured ledger** (JSON, one record per claim, with source URL). No synthesis agent may add facts not in the ledger.
- Dossier agents (~8, per major system) compose from the ledger. Completeness critic + citation spot-check pass.
- **Checkpoint 1:** inventory + dossiers + the ledger itself.

**Run 2 — Evaluability Classification & Adversarial Review (~14 agents).**
- Preregistration first: nulls written and frozen before any scoring agent runs.
- Data-reality auditors verify each digital corpus exists, is accessible, and in what machine format.
- Independent tractability agents score systems **blind** — no agent sees another's scores. Disagreement is preserved and reported, never resolved by a lead agent.
- Falsification agents receive claim + ledger evidence, *not* the advocate's prose.
- **Cross-model tribunal:** my instances are correlated evidence, and internal agreement will not be presented as independent corroboration. Surviving claims go to you → GPT 5.6-Sol (and optionally a human epigrapher) for blind independent review; disagreements come back as first-class findings. Blind reports first, comparison second, rebuttal last.
- **Checkpoint 2:** evaluability-gated matrix + preserved disagreements.

**Run 3 — Experiment Design & Synthesis (~11 agents).**
- Experiment designers for the five priority systems, each design specifying: data plan, method, claim-ladder levels attempted, preregistered success/disconfirmation criteria, compute estimate, and what a null result means.
- Shadow-world designs for Linear A and Indus + one pilot shadow corpus built and red-teamed.
- Red team attacks every design's evaluation validity; Phaistos control run.
- Synthesis: written report (Word), evaluability/tractability matrix (xlsx), interactive explorer (persistent artifact). The narrative is written *last*, from the ledger.

~40 agents total; estimate unchanged (~6–13M tokens across runs).

## 9. Risk register additions (v1 §6 carried forward)

- **Non-specificity of language statistics** (arXiv 2608.02999): entropy, Zipf, positional constraints identify *structured communication*, not speech encoding. All is-it-language claims tested against matched meaningful nonlinguistic nulls.
- **Restart exploitation** (Tamburini 2023/2025): optimization methods validated on known scripts via repeated restarts cannot transfer honestly to unknown ones.
- **Training contamination**: no benchmark on historically deciphered systems without shadow-randomization.
- **Homogeneous-judge correlation**: internal multi-agent agreement ≠ independence; cross-model loop is mandatory for headline claims.
- **HARKing guard**: hypothesis generators never author their own success tests.

## 10. Citation verification (all confirmed 2026-08-11)

| Report citation | Verified as |
|---|---|
| Sommerschield et al. 2023 survey | Computational Linguistics 49(3), ACL Anthology 2023.cl-3.5 ✓ |
| Braović et al. 2024 systematic review | Computational Linguistics 50(2), ACL Anthology 2024.cl-2.7 ✓ |
| Guan et al. OBSD | ACL 2024 **Best Paper**, arXiv 2406.00684 ✓ |
| Peng et al. LVLM OBS decipherment | arXiv 2508.10113 ✓ |
| "CipherOBS" | "Decoding Ancient OBS via Generative Dictionary Retrieval," arXiv 2604.09668 (Apr 2026) ✓ |
| AlphaOracle | arXiv 2607.17849 (Jul 2026), + journal version ✓ |
| HieroSA | arXiv 2601.05508 (Jan 2026), THUNLP-MT ✓ |
| Tamburini | ACL CAWL 2023 + 2025 journal version (PMC) ✓ |
| Otten & Anastasopoulos Meroitic | ACL ALP Workshop 2025.alp-1.11 ✓ |
| Non-specificity paper | arXiv 2608.02999 (Aug 2026) ✓ |

## 11. Open decisions

1. Report depth: default ~30–50 pages + dossier appendix.
2. Cross-model tribunal cadence: after Run 2 only, or after Run 3 as well (recommended: both).
3. Human epigrapher: worth deciding before Run 3 whether you want to recruit one for the finalists.
