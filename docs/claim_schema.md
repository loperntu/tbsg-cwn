# Scholarly claim schema

This document operationalizes the central TBSG principle:

> A graph edge is not automatically a scholarly fact.

The core unit is a **ScholarlyClaim** whose truth status remains revisable and whose evidential basis is explicit.

## Minimal claim object

A translation claim should record at least:

```text
claim_id
subject_term
asserted_relation
object_term
text_id
passage_id
translator
period
supporting_evidence[]
counterevidence[]
alignment_confidence
sense_confidence
claim_confidence
verification_status
adjudication_status
```

## Named graph separation

The example N-Quads file separates the graph into distinct epistemic zones:

- `urn:graph:claims` — active scholarly assertions
- `urn:graph:provenance` — textual attestations and source tracing
- `urn:graph:context` — translator, period, genre, school, etc.
- `urn:graph:lexicon` — lexical items
- `urn:graph:senses` — Buddhist historical senses and CWN anchors
- `urn:graph:adjudication` — human review and revision history

The separation is deliberate. It allows the research layer to distinguish what the source attests from what the analyst infers.

## Example: vijñāna → 識

The bundled `examples/claim_example.nq` is intentionally **synthetic**. `TXXXX`, passage IDs, confidence values, and CWN IDs must not be cited as historical findings.

The important structure is:

```text
Claim C001
  subject: vijñāna
  relation: translatedAs
  object: 識
  supportedBy: E001
  contradictedBy: E019
  translator: 玄奘
  period: 7C
  alignmentConfidence: 0.91
  senseConfidence: 0.82
  verificationStatus: verified-demo
```

Evidence objects then point separately to text and passage resources. Historical sense nodes and modern CWN nodes live in the sense graph, rather than being collapsed into the lexical alignment claim.

## Why multiple confidence fields?

Do not use one generic score for all uncertainty.

- **source verification**: does the passage actually exist at the cited location?
- **alignment confidence**: does the Indic lexical item correspond to the Chinese lexical item in the parallel?
- **sense confidence**: is the historical-sense assignment justified by context?
- **diachronic-relation confidence**: is `specializationOf`, `extensionOf`, etc. justified relative to CWN?
- **claim confidence**: optional aggregate, which must never replace the component scores.

## Adjudication

Human adjudication is modeled as an activity, not simply a boolean flag. This makes it possible to retain:

- reviewer identity or anonymized reviewer role
- timestamp
- decision
- note
- disagreement
- superseded decisions
- revised claims

Production graphs should never delete rejected hypotheses merely to make the graph look clean. Rejected or superseded claims can be retained in a separate graph for auditability.

## TrustGraph compatibility

The ontology intentionally uses RDF/OWL and PROV-O-compatible terms. TrustGraph can therefore serve as the context/provenance substrate, but the ontology is designed to remain backend-independent.

TBSG remains responsible for defining and testing temporal semantic change; TrustGraph should not determine the historical interpretation by itself.
