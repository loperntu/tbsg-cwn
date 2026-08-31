# TBSG + CWN.dia

**Temporal Buddhist Semantic Graph with a diachronic Chinese WordNet layer**

This repository explores how Buddhist translation terminology reorganizes across time, translators, and textual traditions, and how those historical senses can be linked to — but not forced into — modern Chinese WordNet (CWN) sense inventories.

## Research idea

The project models three linked semantic layers:

```text
Indic lexical concept
        ↓ translated_as
Chinese Buddhist lexical form
        ↓ instantiates
Buddhist historical sense
        ↓ diachronic_relation
Modern CWN sense anchor
```

The central object is not merely a word-to-word correspondence such as `citta → 心`, but a provenance-bearing historical claim: a lexical alignment attested in a dated text, associated with a translator/tradition, linked to a historical sense, and optionally related to a modern CWN sense.

A key design principle is **open-world sense induction**. CWN serves as a semantic backbone and modern anchor, not as a closed label set for historical data. Buddhist usages that do not fit existing senses are routed to `NEW_BUDDHIST_SENSE` for human adjudication.

## Initial case study

The MVP focuses on:

- Chinese: `心 / 意 / 識`
- Indic: `citta / manas / vijñāna`
- temporal comparison across translation periods and traditions

The main empirical question is:

> Does the lexical-semantic organization of Buddhist concepts exhibit measurable graph rewiring across translation periods and translation traditions?

Possible trajectories such as **compression → differentiation → stabilization** are hypotheses to be tested, not assumptions built into the model.

## Prototype features

- temporal translation graph with weighted `P(Chinese | Indic)` edges
- historical-sense ↔ CWN-anchor graph
- open-world `NEW_BUDDHIST_SENSE` queue
- token-level evidence/provenance fields
- conditional entropy `H(Chinese | Indic)` as a simple differentiation diagnostic
- CBETA TEI/P5 importer scaffold
- reproducible CWN sense/relationship exporter
- CBETA API candidate collector

## Repository structure

```text
src/
  app.py                  Gradio prototype
  cwn_export.py           Native CWN sense/relation export
  cbeta_search.py         CBETA API candidate collector
  cbeta_tei_importer.py   Minimal TEI/P5 extraction scaffold

data/demo/                Synthetic demo only
schema/
  DATA_SCHEMA.csv
docs/
  architecture.md
  annotation.md
  data_provenance.md
```

`data/raw/` and `data/derived/` are intentionally ignored until redistribution and version policies are checked.

## Important data warning

All data currently under `data/demo/` are **synthetic demonstration data**. CWN IDs, glosses, alignments, counts, and historical-sense mappings there are placeholders and must not be interpreted as historical findings.

## Run the demo

```bash
pip install -r requirements.txt
python src/app.py
```

## Export real CWN anchors

```bash
pip install -r requirements-cwn.txt
python src/cwn_export.py --lemmas 心 意 識
```

The exporter preserves native CWN sense IDs and writes version/provenance metadata. At repository setup time, CwnGraph's public manifest advertised version `v2022.08` / image `v.2022.08.01`; therefore exports must record the actual loaded image rather than loosely calling it "latest CWN".

## Collect CBETA candidates

```bash
python src/cbeta_search.py --terms 心 意 識 --max-pages 1
```

At repository setup time, the CBETA developer documentation reported API `4.6.1` with corpus data `2026R2`. Search results are **candidate evidence only** and require passage-level verification before entering the research graph.

## Next research steps

1. Run and inspect the real CWN export for `心 / 意 / 識`.
2. Extract and manually verify the first 100–300 CBETA occurrences with stable provenance.
3. Add Indic parallels where available and adjudicate alignment/sense labels.
4. Evaluate graph rewiring across periods/translators without presupposing monotonic differentiation.
5. Extend from lexical mapping to a richer **lexical sense genealogy** and eventually to a self-verifying multi-agent discovery layer.

## Status

Research prototype / work in progress.
