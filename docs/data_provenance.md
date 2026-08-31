# Data provenance and version policy

TBSG/CWN.dia treats resource versioning as part of the evidence model.

## Chinese WordNet / CwnGraph

The project uses native CWN sense identifiers and does not mint replacements for existing CWN senses.

CwnGraph supports `CwnImage.latest()` and automatically downloads the data image advertised by its public manifest. At repository setup time (2026-08-31), that manifest reported:

- manifest version: `v2022.08`
- latest advertised image: `v.2022.08.01`

Therefore every CWN export must preserve its requested/resolved image tag or other version metadata. Do **not** describe a CwnGraph export simply as "latest CWN" without recording what image was actually loaded.

Run:

```bash
pip install -r requirements-cwn.txt
python src/cwn_export.py --lemmas 心 意 識
```

The exporter writes `cwn_senses.csv`, `cwn_relations.csv`, and `cwn_export_metadata.json` under `data/derived/cwn/` by default. Derived data are ignored by Git until redistribution/version policy is reviewed.

## CBETA

The candidate collector targets the CBETA developer API. At repository setup time the developer documentation reported API `4.6.1` and corpus data `2026R2`.

CBETA requests API users to provide a `Referer` header for access analytics; `src/cbeta_search.py` does so.

Run:

```bash
python src/cbeta_search.py --terms 心 意 識 --max-pages 1
```

Search output is **candidate evidence only**. It must not enter the validated graph until passage-level provenance and contextual interpretation are checked.

## Separation of evidence levels

Keep these distinct:

1. **retrieved candidate** — returned by corpus search;
2. **textually verified occurrence** — source passage and stable location checked;
3. **lexical alignment** — Indic/Chinese correspondence supported by a parallel witness;
4. **historical-sense annotation** — sense decision adjudicated;
5. **CWN diachronic relation** — relation to a modern CWN sense (`equivalent_to`, `specialization_of`, `extension_of`, `related_to`, `no_modern_equivalent`).

A TBSG edge should never collapse these confidence levels into one number.
