# Scholarly claim schema

This document operationalizes the central TBSG principle:

> A graph edge is not automatically a scholarly fact.

The core unit is a **ScholarlyClaim** whose truth status remains revisable and whose evidential basis is explicit.

## Core form

```text
Claim = Statement
      + Evidence
      + Provenance
      + Uncertainty
      + Counterevidence
      + Human adjudication
```

## Claim types

### TranslationClaim

Use only when direct translation direction/source dependence is sufficiently established for the research purpose.

Conceptual form:

`Indic lexical item → translatedAs → Chinese lexical item`

### ParallelCorrespondenceClaim

Use when lexical items occur in aligned or parallel passages but direct translation direction or dependence on a specific extant witness is not established.

Example:

`Sanskrit vijñāna ↔ Chinese 識` in parallel Heart Sutra passages.

This distinction is mandatory. A parallel correspondence must not silently be promoted to a translation-source claim.

### SenseClaim

A claim about the historical sense instantiated by an attested token or passage.

## Minimal claim object

A production claim should record at least:

```text
claim_id
claim_type
subject_term
asserted_relation
object_term
text_id / parallel_text_id
passage_id / parallel_passage_id
translator or attributed_translator
period
supporting_evidence[]
counterevidence[]
alignment_confidence
sense_confidence
claim_confidence
verification_status
counterevidence_search_status
adjudication_status
```

## Named graph separation

The N-Quads model separates the graph into distinct epistemic zones:

- `urn:graph:claims` — active scholarly assertions
- `urn:graph:provenance` — textual attestations and source tracing
- `urn:graph:context` — translator attribution, period, genre, school, etc.
- `urn:graph:lexicon` — lexical items
- `urn:graph:senses` — Buddhist historical senses and CWN anchors
- `urn:graph:adjudication` — human review and revision history

The separation is deliberate. It allows the research layer to distinguish what the source attests from what the analyst infers.

## Synthetic and real-source examples

`examples/claim_example.nq` is intentionally **synthetic**. Its text IDs, passage IDs, confidence values, and CWN IDs must not be cited as historical findings.

`examples/claim_real_t0251_vijnana_shi.nq` is the first **real-source** vertical slice. It uses CBETA T0251 and a Sanskrit Heart Sutra parallel to model `vijñāna ↔ 識` as a `ParallelCorrespondenceClaim`.

The current real-source claim is not yet gold: CWN mapping, counterevidence search, and human review remain pending.

## Why multiple confidence fields?

Do not use one generic score for all uncertainty.

- **source verification**: does the passage actually exist at the cited location?
- **alignment confidence**: does the Indic lexical item correspond to the Chinese lexical item in the parallel?
- **sense confidence**: is the historical-sense assignment justified by context?
- **diachronic-relation confidence**: is `specializationOf`, `extensionOf`, etc. justified relative to CWN?
- **claim confidence**: optional aggregate, which must never replace the component scores.

## Translator attribution

Use `translator` only when the project is willing to assert translator identity at the relevant epistemic level.

Use `attributedTranslator` plus `attributionStatus` when preserving catalogue/traditional attribution while acknowledging unresolved textual-history questions. Translator attribution, source dependence, lexical correspondence, and historical-sense analysis must remain separable claims.

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

## Production promotion rule

A machine-prepared claim should not be treated as gold merely because both source passages are real. Promotion to an adjudicated claim requires, as applicable:

1. source verification;
2. alignment review;
3. sense review;
4. native CWN mapping or an explicit open-world decision (`noModernEquivalent` / `NEW_BUDDHIST_SENSE`);
5. counterevidence search;
6. human adjudication.

## TrustGraph compatibility

The ontology intentionally uses RDF/OWL and PROV-O-compatible terms. TrustGraph can therefore serve as the context/provenance substrate, but the ontology is designed to remain backend-independent.

TBSG remains responsible for defining and testing temporal semantic change; TrustGraph should not determine the historical interpretation by itself.
