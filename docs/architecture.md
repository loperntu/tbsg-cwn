# Architecture

## Design principle

TBSG + CWN.dia separates the **infrastructure for storing/tracing claims** from the **research method for interpreting temporal semantic change**.

- **TrustGraph**: context/provenance substrate, RDF/OWL ontology layer, named graphs, GraphRAG, future agent shared memory.
- **TBSG**: temporal semantic representation, graph rewiring, translator/period comparison, uncertainty-aware scholarly claims.
- **CWN.dia**: diachronic lexical-sense ontology connecting Buddhist historical senses to modern CWN anchors.

> TrustGraph stores and traces claims; TBSG defines temporal semantic change; CWN.dia models lexical sense genealogy.

## System architecture

```text
CBETA / Sanskrit / Pāli / CWN
            │
            ▼
     Retrieval & ingestion
            │
            ▼
 Textual evidence / attestations
            │
            ▼
  Epistemically qualified claims
            │
            ▼
┌──────────────────────────────────────┐
│ TrustGraph context hypergraph        │
│                                      │
│ default graph: accepted assertions   │
│ source graph: provenance/evidence    │
│ retrieval graph: query/agent traces  │
│ ontology: TBSG + CWN.dia             │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ TBSG temporal-semantic analysis      │
│                                      │
│ period / translator / genre slices   │
│ graph rewiring                       │
│ lexical differentiation              │
│ counterevidence and uncertainty      │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│ CWN.dia lexical sense genealogy      │
│ historical sense ↔ modern CWN sense  │
└──────────────────────────────────────┘
```

## Why a hypergraph / reified-claim model?

A scholarly translation assertion is n-ary. A binary edge such as:

```text
citta ──translated_as──> 心
```

suppresses critical historical and epistemic information. The real object is closer to:

```text
TranslationClaim C001
  subject                citta
  relation               translated_as
  object                 心
  attested_in            Txxx
  passage                p123
  translator             Kumārajīva
  normalized_date        405
  historical_sense       BUD_XIN_...
  alignment_confidence   0.91
  sense_confidence       0.82
  human_status           verified
  supported_by           Evidence E001, E002...
  contradicted_by        Evidence E019...
```

This motivates statement-level objects that can themselves receive provenance, confidence, temporal metadata, and counterevidence.

## Epistemic claim model

The preferred scholarly object is:

```text
Claim = Statement
      + Evidence
      + Provenance
      + Uncertainty
      + Counterevidence
      + Human adjudication
```

Recommended fields:

```text
claim_id
claim_type
subject
predicate
object
text_id
passage_id / line_id
Chinese context
parallel_text_id
Indic context
translator
translation_tradition
date / period
genre / school
historical_sense_id
CWN_sense_id(s)
source_verification_status
alignment_confidence
sense_confidence
diachronic_relation_confidence
human_status
supporting_evidence_ids
counterevidence_ids
model / extraction_method
created_at
```

A graph edge is never accepted merely because an LLM proposes it. RDF/OWL structure provides explicit semantics and traceability, not truth by itself.

## Named graph strategy

A TrustGraph-compatible deployment should distinguish at least:

```text
default graph
    accepted or currently active scholarly assertions

urn:graph:source
    document → page/passage → chunk/segment → extracted/reviewed claim provenance

urn:graph:retrieval
    GraphRAG / agent query traces and evidence paths

urn:graph:adjudication   (TBSG extension)
    human decisions, disagreement, counterevidence, superseded claims
```

The fourth graph is a proposed TBSG extension rather than an assumption about TrustGraph itself.

## Ontology sketch

```text
LexicalEntity
  ├── ChineseLexeme
  └── IndicLexeme

LexicalSense
  ├── ModernCWNSense
  └── HistoricalSense
        └── BuddhistHistoricalSense

ScholarlyClaim
  ├── TranslationClaim
  ├── SenseAssignmentClaim
  └── DiachronicRelationClaim

Evidence
  ├── TextualAttestation
  ├── ParallelAttestation
  └── CounterEvidence

AgentOrHuman
  ├── ExtractionAgent
  ├── VerificationAgent
  └── HumanAnnotator
```

Core relations include:

```text
translated_as
instantiates
attested_in
supported_by
contradicted_by
verified_by
equivalent_to
specialization_of
extension_of
related_to
no_modern_equivalent
predecessor_sense
successor_sense
```

## Open-world sense induction

CWN is a modern semantic anchor, not a closed historical inventory. A historical occurrence may be:

- `equivalent_to` a CWN sense
- `specialization_of` a CWN sense
- `extension_of` a CWN sense
- `related_to` one or more CWN senses
- `no_modern_equivalent`
- `NEW_BUDDHIST_SENSE` pending adjudication

Systematic CWN coverage failure may itself become evidence of historical specialization or innovation, subject to human validation.

## Temporal analysis

For temporal/translator slices, estimate quantities such as:

```text
P(Chinese term | Indic term, period, translator)
P(historical sense | lemma, period, translator)
```

Diagnostics may include:

- conditional entropy `H(Chinese | Indic)`
- Jensen–Shannon divergence between translation distributions
- edge appearance/disappearance
- node/sense birth, stabilization, specialization, or decline
- graph-edit or neighborhood-change measures

These are diagnostics, not self-interpreting evidence of semantic change. Analyses must control for translator, genre, corpus composition, textual dependence, sample size, and alignment uncertainty.

## DharmaSwarm extension

A later multi-agent layer can use the TrustGraph context graph as shared memory:

```text
retrieve
   ↓
hypothesize
   ↓
seek supporting evidence
   ↓
seek counterevidence
   ↓
verify
   ↓
write qualified claim to graph
   ↓
human adjudication
```

Agents therefore remain discovery/verification mechanisms. The graph is the auditable scholarly memory, while TBSG supplies the historical-semantic interpretation.
