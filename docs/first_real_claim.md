# First real-source vertical slice: T0251 `vijñāna` ↔ `識`

## Why this passage

The first real-source claim uses the Heart Sutra passage traditionally attributed to Xuanzang in CBETA T0251:

- Chinese passage ID: `T0251.001.0848c08-09`
- local text: `受、想、行、識，亦復如是。`
- parallel Sanskrit sequence: `evam eva vedanā-saṃjñā-saṃskāra-vijñānāni`

The lexical correspondence `vijñāna ↔ 識` is unusually transparent because both items occupy the same position in the parallel list of skandhas.

## Epistemic status

This is intentionally encoded as a `ParallelCorrespondenceClaim`, **not** as a direct `TranslationClaim`.

What the current evidence supports:

> In a Sanskrit Heart Sutra witness/transcription and CBETA T0251, `vijñāna` and `識` occur in corresponding positions in parallel passages.

What the current evidence does **not** establish by itself:

> That the specific extant Sanskrit witness was the direct source used by the translator traditionally associated with T0251.

This distinction is important because source dependence, translator attribution, lexical correspondence, and semantic interpretation are separate scholarly claims and should not be collapsed into one graph edge.

## Sources recorded in the N-Quads example

Chinese witness:
- CBETA / Taishō T08 no. 251
- stable line area: `0848c08-09`
- catalogued/traditional translator attribution: 玄奘
- normalized date used for the prototype: 649 (catalogue range 648–649)

Sanskrit parallel:
- *Prajñāpāramitā-hṛdaya-sūtra* Sanskrit transcription hosted by the NTU Buddhist Digital Library
- parallel phrase contains `vedanā-saṃjñā-saṃskāra-vijñānāni`

## Files

- `ontology/tbsg-cwn.ttl` — core ontology
- `ontology/philology-extension.ttl` — conservative parallel-correspondence vocabulary
- `examples/claim_real_t0251_vijnana_shi.nq` — first real-source N-Quads vertical slice

## Current unresolved steps

1. Run native CwnGraph export and replace the provisional historical-sense mapping with one or more real CWN sense IDs.
2. Human-review the historical-sense label `識 as the consciousness member of the five skandhas`.
3. Search for counterexamples / alternative lexicalizations in independent witnesses.
4. Validate the N-Quads file with an RDF parser and load it into a TrustGraph-compatible test deployment.
5. Only after those steps should the claim be promoted from `candidate` to a gold/adjudicated scholarly claim.

## Methodological lesson

This first case establishes the intended vertical slice:

`source passage → attestation → lexical correspondence claim → historical sense → CWN.dia mapping → human adjudication`

The graph is therefore a record of **what is asserted, why it is asserted, and what remains unresolved**, rather than a database that silently treats extracted triples as facts.
