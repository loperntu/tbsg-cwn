# TBSG + CWN.dia

**Temporal Buddhist Semantic Graph with a diachronic Chinese WordNet layer**

This repository develops a provenance-aware, uncertainty-aware framework for studying how Buddhist lexical-semantic systems reorganize across time, translators, and textual traditions. The project combines three distinct layers:

1. **TrustGraph** as the semantic/provenance substrate and future agent-context layer;
2. **TBSG** as the temporal-semantic representation and analysis method;
3. **CWN.dia** as the diachronic sense ontology linking Buddhist historical senses to modern Chinese WordNet (CWN) anchors.

The design principle is simple:

> **TrustGraph stores and traces claims; TBSG defines temporal semantic change; CWN.dia models lexical sense genealogy.**

## Research idea

```text
CBETA / Indic witnesses / CWN
             │
             ▼
     Evidence + Claim Objects
             │
             ▼
   TrustGraph Context Hypergraph
  (RDF/OWL, provenance, named graphs)
             │
             ▼
      TBSG analytical layer
  (time, translator, graph rewiring)
             │
             ▼
          CWN.dia
 (historical sense genealogy)
             │
             ▼
       Modern CWN anchors
```

The central object is not merely a word-to-word edge such as `citta → 心`, but an **epistemically qualified claim**:

```text
Claim = Statement
      + Evidence
      + Provenance
      + Uncertainty
      + Counterevidence
      + Human status
```

A translation claim may therefore connect an Indic lexeme, Chinese lexical form, text, passage, translator, date, historical sense, confidence scores, supporting passages, and counterexamples as one addressable scholarly object.

## Initial case study

The MVP focuses on:

- Chinese: `心 / 意 / 識`
- Indic: `citta / manas / vijñāna`
- temporal comparison across translation periods and traditions
- mapping Buddhist historical senses to CWN without forcing historical data into a modern closed sense inventory

Primary empirical question:

> **Does the lexical-semantic organization of Buddhist concepts exhibit measurable graph rewiring across translation periods and translation traditions?**

Possible trajectories such as **compression → differentiation → stabilization** are hypotheses to be tested, not assumptions built into the model.

## Why TrustGraph?

TrustGraph is used as infrastructure rather than as the research theory. Its RDF/OWL context-graph model, statement-level provenance, named graphs, ontology support, GraphRAG, and agent orchestration are well matched to philological evidence that is naturally n-ary and provenance-sensitive.

However, a structured graph does not make an extracted claim true. TBSG therefore preserves separate epistemic fields for:

- source verification
- lexical alignment confidence
- historical-sense confidence
- CWN diachronic-relation confidence
- supporting evidence
- counterevidence
- human adjudication status

## Prototype features

- temporal translation graph with weighted `P(Chinese | Indic)` edges
- historical-sense ↔ CWN-anchor graph
- open-world `NEW_BUDDHIST_SENSE` queue
- token-level evidence/provenance fields
- conditional entropy `H(Chinese | Indic)` as a simple differentiation diagnostic
- CBETA TEI/P5 importer scaffold
- reproducible CWN sense/relationship exporter
- CBETA API candidate collector
- TrustGraph-compatible claim/evidence model (design stage)

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
  proposal_bilingual.md
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

The exporter preserves native CWN sense IDs and writes version/provenance metadata. Exports must record the actual loaded CWN image/version rather than loosely calling it "latest CWN".

## Collect CBETA candidates

```bash
python src/cbeta_search.py --terms 心 意 識 --max-pages 1
```

Search results are **candidate evidence only** and require passage-level verification before entering the research graph.

## Near-term roadmap

1. Run and inspect the real CWN export for `心 / 意 / 識`.
2. Extract and manually verify the first 100–300 CBETA occurrences with stable provenance.
3. Define the TBSG/CWN.dia ontology in RDF/OWL and map it to TrustGraph named/provenance graphs.
4. Add Indic parallels where available and adjudicate alignment/sense labels.
5. Evaluate graph rewiring across periods/translators without presupposing monotonic differentiation.
6. Add a future DharmaSwarm layer for `retrieve → hypothesize → seek counterevidence → verify → graph → human adjudication`.

## Status

Research prototype / work in progress.
