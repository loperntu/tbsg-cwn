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
- Temporal comparison: early, middle, and later translation periods

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

## Repository structure

```text
src/
  app.py                  Gradio prototype
  cbeta_tei_importer.py   Minimal TEI/P5 extraction scaffold

data/demo/
  demo_edges.csv
  demo_instances.csv
  demo_senses.csv
  demo_sense_links.csv
  demo_temporal_metrics.csv

schema/
  DATA_SCHEMA.csv

docs/
  architecture.md
  annotation.md
```

## Important data warning

All data currently under `data/demo/` are **synthetic demonstration data**. CWN IDs, glosses, alignments, counts, and historical-sense mappings are placeholders and must not be interpreted as historical findings.

## Run

```bash
pip install -r requirements.txt
python src/app.py
```

## Next research steps

1. Import real CWN sense IDs, glosses, and semantic relations through CwnGraph.
2. Extract 100–300 verified CBETA occurrences for `心 / 意 / 識` with stable provenance.
3. Add Indic parallels where available and manually adjudicate alignment/sense labels.
4. Evaluate graph rewiring across periods/translators without presupposing monotonic differentiation.
5. Extend from lexical mapping to a richer **lexical sense genealogy** and eventually to a self-verifying multi-agent discovery layer.

## Status

Research prototype / work in progress.
