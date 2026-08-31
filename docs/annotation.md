# Annotation protocol — MVP

The first production dataset should remain deliberately small: approximately 100–300 verified occurrences centered on `心 / 意 / 識` and, where parallel evidence permits, `citta / manas / vijñāna`.

## Per-token annotation

Record:

1. Chinese lemma and full local context.
2. Stable textual provenance (collection, text ID, fascicle/line/passage).
3. Translator/tradition and normalized date or period.
4. Indic parallel and lexical item, if securely available.
5. Candidate Buddhist historical sense.
6. Closest CWN sense ID(s), preserving native CWN identifiers.
7. Relation to CWN: `equivalent_to`, `specialization_of`, `extension_of`, `related_to`, or `no_modern_equivalent`.
8. Alignment confidence and sense confidence separately.
9. `NEW_BUDDHIST_SENSE` when existing historical/CWN-linked categories are inadequate.
10. Human adjudication status and notes, including counterexamples.

## Adjudication rule

Do not create a new historical sense merely because a context is unusual. A `NEW_BUDDHIST_SENSE` candidate should be reviewed for contextual modulation, constructional effects, textual corruption, alignment error, domain specialization, and recurrence across independent passages before promotion to a stable sense node.

## Minimal evaluation

Report at least:

- alignment agreement / accuracy on a manually checked sample
- sense-assignment agreement
- proportion routed to `NEW_BUDDHIST_SENSE`
- evidence/provenance completeness
- graph statistics by period and translator

Any claim of temporal differentiation must be tested against translator and corpus-composition confounds.
