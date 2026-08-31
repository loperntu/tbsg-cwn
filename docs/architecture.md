# Architecture

## Core representation

TBSG + CWN.dia separates **attestation**, **historical sense**, and **modern lexical ontology**.

```text
Textual evidence (CBETA / parallel witness)
        │ attests
        ▼
Indic term ──translated_as──> Chinese form
                                  │ instantiates
                                  ▼
                         Buddhist historical sense
                                  │
                     ┌────────────┼────────────┐
                     │            │            │
                   time       translator      genre/school
                     │
                     ▼
                         diachronic_relation
                                  │
                                  ▼
                           Modern CWN sense
```

## Epistemic principle

A graph edge is not accepted merely because an LLM proposes it. Production data should retain sufficient provenance to reconstruct the claim from the source passage and, where relevant, the parallel Indic witness.

Recommended evidence object:

```text
claim_id
text_id
passage_id / line_id
Chinese context
parallel_text_id
Indic context
source_term
target_term
historical_sense_id
CWN_sense_id(s)
translator
date / period
alignment_confidence
sense_confidence
human_status
counterevidence
```

## Open-world sense induction

CWN is a modern semantic anchor, not a closed historical inventory. A historical occurrence may be:

- `equivalent_to` a CWN sense
- `specialization_of` a CWN sense
- `extension_of` a CWN sense
- `related_to` one or more CWN senses
- `no_modern_equivalent`
- `NEW_BUDDHIST_SENSE` pending adjudication

This design makes **CWN coverage failure potentially informative**: systematic failure may signal historical specialization or innovation rather than annotation error.

## Temporal analysis

For each temporal/translator slice, estimate weighted mappings such as:

`P(Chinese term | Indic term, period, translator)`

The prototype also computes conditional entropy `H(Chinese | Indic)` as a simple diagnostic of lexical differentiation. Entropy is not itself evidence of semantic change; results must be checked against corpus composition, translator effects, genre, textual dependence, and alignment quality.

## Long-term extension

A later DharmaSwarm layer can propose, challenge, and verify graph updates:

`retrieve → hypothesize → seek counterevidence → verify → graph → human adjudication`

The graph therefore serves as the epistemic substrate; agents are discovery and verification mechanisms rather than the knowledge representation itself.
