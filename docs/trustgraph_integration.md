# TrustGraph Integration Strategy

## Role in TBSG + CWN.dia

TrustGraph is treated as the **context/provenance substrate**, not as the theory of semantic change.

- TrustGraph: RDF/OWL storage, provenance, named graphs, GraphRAG, agent context.
- TBSG: temporal-semantic analysis and graph rewiring.
- CWN.dia: diachronic lexical-sense genealogy.

## Minimal integration target

The first integration should not deploy the full TrustGraph stack merely for the synthetic demo. Instead, establish compatibility through an RDF/N-Quads export of verified TBSG claim objects.

Target object:

```text
TranslationClaim
  subject
  predicate
  object
  source passage
  translator
  date/period
  historical sense
  confidence dimensions
  supporting evidence
  counterevidence
  human status
```

## Named graphs

Use TrustGraph-compatible graphs where possible:

- default graph: active assertions
- `urn:graph:source`: source/extraction provenance
- `urn:graph:retrieval`: query/agent reasoning provenance

Proposed TBSG extension:

- `urn:graph:adjudication`: human review, disagreement, counterevidence, superseded claims

## Ontology

The first OWL/Turtle ontology should cover:

- `LexicalEntity`
- `ChineseLexeme`
- `IndicLexeme`
- `LexicalSense`
- `ModernCWNSense`
- `BuddhistHistoricalSense`
- `ScholarlyClaim`
- `TranslationClaim`
- `SenseAssignmentClaim`
- `DiachronicRelationClaim`
- `TextualAttestation`
- `CounterEvidence`

Core relations:

- `translated_as`
- `instantiates`
- `attested_in`
- `supported_by`
- `contradicted_by`
- `verified_by`
- `equivalent_to`
- `specialization_of`
- `extension_of`
- `related_to`
- `no_modern_equivalent`
- `predecessor_sense`
- `successor_sense`

## Guardrail

RDF structure and provenance improve traceability but do not establish truth. Extraction confidence, source verification, alignment confidence, sense confidence, counterevidence, and human adjudication must remain distinct epistemic fields.
