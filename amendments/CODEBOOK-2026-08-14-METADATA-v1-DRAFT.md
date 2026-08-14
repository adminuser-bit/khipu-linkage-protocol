# Metadata Codebook v1 — A22.6 Instrument (DRAFT)

**Status: DRAFT v1 — prepared for external review.** This is the A22.6
metadata codebook for the run governed by the amendment package frozen at
`freeze/amendments-v1` (tag on commit 3bbcb8d). Per A22.6 it must be frozen
and externally anchored before the first item-level enumeration result is
inspected; per A20.9 it is the sole authority for `doc_id` construction. It
binds the four load-bearing stratification axes of A22.5 (type, period bin,
audiencia, entry-count bin) and the eligibility metadata rule of A20.2
(design §2.2: Peru, 1532–1700, visita/revisita/padrón/tasa, ≥20 grouped
numeric entries per catalog or edition metadata).

**Information-basis declaration.** This codebook was drafted from
schema-level knowledge only: the frozen protocol documents of this
repository and general knowledge of Spanish colonial archival practice and
catalog schemas. In preparing it, no archival catalog was queried, no
item-level catalog record, finding-aid entry, or edition table of contents
was inspected, and no enumeration output exists in this repository. Any
resemblance between this codebook's closed tables and the realized corpus
is therefore untested at drafting time; that is the property A22.6 exists
to guarantee.

**Master rule (A22.6, adopted verbatim from the frozen package):** missing,
conflicting, multi-valued, or previously unseen values on any load-bearing
axis are coded `UNRESOLVED` and make the document ineligible/unscoreable
this run; no label may be added, reclassified, or remapped after
enumeration begins. All tables below are **closed**: matching failures
resolve to `UNRESOLVED`, never to judgment calls.

---

## C1 — Load-bearing axes and canonical tokens

Every enumerated document receives exactly one value per axis:

| Axis | Canonical tokens (exact strings entering all JCS hashes) |
|---|---|
| type | `visita`, `revisita`, `padron`, `tasa` |
| audiencia | `lima`, `charcas`, `quito` |
| period | `1532-1581`, `1582-1631`, `1632-1681`, `1682-1700` |
| entries | `20-49`, `50-99`, `100-199`, `200plus` |

plus `doc_id` (C2). Axis-level failure codes: `UNRESOLVED_TYPE`,
`UNRESOLVED_AUDIENCIA`, `UNRESOLVED_PERIOD`, `UNRESOLVED_ENTRIES`,
`UNRESOLVED_DOC_ID`. Any one of them excludes the document this run
(recorded in the enumeration deposit with its failure code; never
silently dropped). Canonical tokens are ASCII by construction; A20.9
hashing operates on these exact strings.

## C2 — Canonical `doc_id` scheme: `institution/fonds-series/item`

### C2.1 String normalization (applied to each component)

1. Unicode NFC; then lowercase.
2. Diacritic folding by closed table: á→a, é→e, í→i, ó→o, ú→u, ü→u, ñ→n
   (uppercase forms via the prior lowercasing).
3. Each maximal run of characters outside `[a-z0-9]` becomes a single `-`.
4. Strip leading/trailing `-`.

The three normalized components are joined with `/`. A `doc_id` therefore
matches `[a-z0-9-]+/[a-z0-9-]+/[a-z0-9-]+` exactly.

### C2.2 Institution registry (closed)

| Token | Institution |
|---|---|
| `agi` | Archivo General de Indias, Sevilla (via PARES) |
| `ahn` | Archivo Histórico Nacional, Madrid (via PARES) |
| `agn-pe` | Archivo General de la Nación, Perú (Lima) |
| `bnp` | Biblioteca Nacional del Perú (Lima) |

A document held elsewhere (including one attested only in a published
edition whose original lies outside these four) is `UNRESOLVED_DOC_ID`
this run. Published editions attest transcriptions; the `doc_id` always
denotes the archival item, never the edition.

### C2.3 Fonds-series component

The holding institution's own top-level fonds designation, followed by its
series/section designation where the catalog individuates one, joined
internally by the normalization of C2.1 (e.g. an AGI *Lima* legajo yields
fonds-series `lima`; an AGN-PE fondo *Derecho Indígena* serie yields
`derecho-indigena-<serie>`). The catalog's own signatura vocabulary is
authoritative; nothing is inferred.

### C2.4 Item component

The catalog's minimal unambiguous item-level designation (legajo +
expediente/número; manuscript code; cuaderno). A folio range enters the
item component only where the catalog itself individuates the document at
folio level. A document for which the catalog provides no unambiguous
item-level designation is `UNRESOLVED_DOC_ID` (A20.9: "A document lacking
one unambiguous canonical item identifier is ineligible this run").

### C2.5 Uniqueness and duplicates

`doc_id` values must be unique across the enumeration. Two catalog entries
yielding the same `doc_id` are one document iff their pre-normalization
institution + full signatura strings are byte-identical (duplicate catalog
rows deduplicate mechanically); otherwise every colliding entry is
`UNRESOLVED_DOC_ID`. No manual disambiguation exists.

## C3 — Type axis: recognized-label → category mapping

### C3.1 Matching procedure

The catalog's title/type/description fields are normalized per C2.1 steps
1–2 plus diacritic folding, then matched for whole-word occurrences of the
base terms below. Matching is purely lexical; no reading of document
content, and no inference from fields other than title/type/description.

### C3.2 Base terms (closed)

| Category | Recognized base terms (diacritic-folded) |
|---|---|
| `visita` | visita, visitacion, visita general, visita personal, visita de la tierra |
| `revisita` | revisita, revisitacion |
| `padron` | padron, padroncillo, empadronamiento, numeracion, matricula |
| `tasa` | tasa, retasa, tasacion |

Reviewer-attention items, disclosed: (i) `numeracion` and `matricula` are
mapped to `padron` on the schema-level ground that both name census-roll
acts; (ii) `retasa` is mapped to `tasa` as a re-assessment of the same
fiscal kind. Striking any of these rows narrows the universe and is a
legitimate review outcome; adding rows after freeze is not.

### C3.3 Compound labels

If the matched base terms span more than one category, the category is
assigned by the frozen precedence **revisita > visita > padron > tasa**
(the census-act term outranks the fiscal-outcome term; the re-enumeration
term outranks the first-enumeration term). This precedence resolves, e.g.,
"visita y padrón" → `visita`, "padrón y revisita" → `revisita`, "revisita
y tasa" → `revisita`, "padrón y tasa" → `padron`. If any matched term is
not in C3.2, or no term matches, the type axis is `UNRESOLVED_TYPE`.

## C4 — Audiencia axis

### C4.1 Direct statement

If the catalog names the audiencia, map: "Audiencia de Lima" / "Los
Reyes" → `lima`; "Audiencia de Charcas" / "La Plata" → `charcas`;
"Audiencia de Quito" / "San Francisco de Quito" → `quito`.

### C4.2 Gazetteer (closed; timeless mature-boundary rule)

Otherwise the document's stated province/corregimiento is looked up in the
closed gazetteer below. Assignment uses the audiencias' **mature
post-1563 boundaries applied timelessly**: the region axis serves
stratification (documents comparable to documents of the same region), not
jurisdictional history, so a place maps to one region for the whole run
regardless of document date. This is a disclosed design choice for review;
its alternative (jurisdiction-at-date) imports date-dependence into a
second axis and makes region `UNRESOLVED` wherever period is.

| Region | Gazetteer entries (diacritic-folded matching) |
|---|---|
| `lima` | lima, cercado, huarochiri, canta, yauyos, jauja, tarma, chancay, canete, ica, huamanga, huancavelica, andahuaylas, abancay, cusco, cuzco, arequipa, camana, condesuyos, collaguas, trujillo, sana, piura, cajamarca, chachapoyas, huanuco, conchucos, huaylas, santa, huamalies, castrovirreyna, lucanas, parinacochas, vilcashuaman, chumbivilcas, canas, canchis, quispicanchis, paucartambo, calca, urubamba |
| `charcas` | la plata, chuquisaca, potosi, porco, chayanta, lipez, tarija, mizque, cochabamba, la paz, chucuito, pacajes, omasuyos, larecaja, sicasica, oruro, paria, carangas, atacama, arica, tarapaca, tucuman, santa cruz de la sierra |
| `quito` | quito, otavalo, ibarra, latacunga, ambato, riobamba, chimbo, guayaquil, cuenca, loja, jaen de bracamoros, zamora, macas, quijos |

Reviewer-attention items, disclosed: entries whose historical assignment
involved transfer or dispute (notably chucuito, arica, tarapaca, atacama,
puno-area provinces split across the Lima/Charcas boundary) are assigned
here by the mature-boundary rule; striking any entry into an explicit
`UNRESOLVED` list is a legitimate review outcome. `puno` itself is
deliberately absent (boundary-straddling); a document located only as
"puno" is `UNRESOLVED_AUDIENCIA`.

### C4.3 Failure modes

No recognized place, more than one recognized place mapping to different
regions, or a stated region outside the three audiencias (e.g. Panamá,
Santa Fe, Chile) → `UNRESOLVED_AUDIENCIA` (A22.5: outside → unscoreable).

## C5 — Period axis

Bins are frozen by A22.5: `1532-1581`, `1582-1631`, `1632-1681`,
`1682-1700`.

### C5.1 Year-set extraction from catalog date metadata

| Date form | Year set |
|---|---|
| single year *y* | {y} |
| explicit range *y1–y2* | {y1,…,y2} |
| "ca./c./hacia *y*" | {y−5,…,y+5} |
| decade ("años de 1650") | {1650,…,1659} |
| half-century ("primera/segunda mitad del siglo *N*") | the 50-year span |
| century ("siglo XVII") | {1601,…,1700} |
| open-ended ("post/antes de *y*"), undated | `UNRESOLVED_PERIOD` |

The date used is the date of the enumeration act itself; where the catalog
distinguishes a later copy (*traslado*) date from the act date, the act
date is used, and if only the copy date exists the axis is
`UNRESOLVED_PERIOD`.

### C5.2 Assignment

If the year set is wholly inside 1532–1700 **and** wholly inside one bin,
that bin is assigned. A year set extending outside 1532–1700, or spanning
two or more bins, is `UNRESOLVED_PERIOD`. No midpoint, no rounding toward
a bin, no operator choice.

## C6 — Entry-count axis

Eligibility floor (A20.2): ≥20 grouped numeric entries **per catalog or
edition metadata, not content inspection**. Bins: `20-49`, `50-99`,
`100-199`, `200plus`.

### C6.1 Admissible count statements

Explicit numeric statements, in catalog or edition metadata, of enumerated
units: tributarios, indios (tributarios), vecinos, casas, familias,
partidas, or an editor's stated count of entries/rows in the transcribed
document. Folio, page, image, and legajo counts are never admissible
proxies. Absent any admissible statement, the axis is
`UNRESOLVED_ENTRIES` and the document is ineligible (the ≥20 floor cannot
be certified mechanically).

### C6.2 Interval interpretation (closed)

| Statement form | Interval |
|---|---|
| exact *N* | [N, N] |
| "más de N" | [N+1, ∞) |
| "cerca de / unos / aproximadamente N" | [⌊0.9N⌋, ⌈1.1N⌉] |
| explicit range N1–N2 | [N1, N2] |

### C6.3 Assignment

Intersect all admissible statements' intervals. Empty intersection
(conflicting statements) → `UNRESOLVED_ENTRIES`. Intersection wholly below
20 → ineligible, recorded as below-floor (a determinate exclusion, not
`UNRESOLVED`). Intersection wholly inside one bin → that bin. Any other
intersection (spanning the floor or spanning bins) → `UNRESOLVED_ENTRIES`.
("más de N" with N+1 ≥ 200 lies wholly in `200plus`.)

## C7 — `UNRESOLVED` handling and change control

1. Any axis-level `UNRESOLVED_*` code excludes the document from D_cand
   and from every decoy panel this run; the document remains in the
   enumeration deposit with its failure code(s), so exclusions are
   auditable and countable per A30.
2. The tables of C2.2, C3.2, C4.1–C4.2, C5.1, and C6.1–C6.2 are complete
   at freeze. A value not matched by them is by construction "previously
   unseen" and resolves to the axis's `UNRESOLVED_*` code. After
   enumeration begins, no addition, reclassification, or remapping — a
   discovered defect in this codebook is reported as a finding and can be
   cured only for a future run's codebook, never for this one.
3. Nothing in this codebook licenses inspecting item-level catalog
   results before its freeze anchor exists; the enumeration fleet is
   gated on that anchor (A22.6, GOVERNANCE R4).

## C8 — Interfaces to frozen machinery

- `doc_id` values built under C2 are the exact strings entering the A20.9
  `triple_id`, the A20.3 extent lottery, and the A22.4 decoy lottery
  (`SHA-256(JCS(["KHI-A22-LOTTERY-20260814", doc_id]))`).
- A stratum is the 4-tuple of canonical tokens (type, audiencia, period,
  entries); decoy panels are drawn within exact 4-tuple equality (A22.5).
- The positive-control document is designated at A0 per A23 and is
  excluded from candidate and decoy sets by A20.2; this codebook contains
  no item-level statement about it.
