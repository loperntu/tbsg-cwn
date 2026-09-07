# PNC 2026 release: CiWN evidence prototype

The demonstration is published at [SinDia Buddhist Semantics](https://lopentu.github.io/sindia-site/buddhist/). See [deployment details](deployment/README.md).

## Scope and measured outputs

- 16 machine-prepared claim proposals; 6 evidence windows; 4 sources (3 Chinese works and 1 Sanskrit transcription).
- 27 native CWN senses from exact queries 心 / 意 / 識 in the pinned v.2022.08.01 image, including homographs.
- All 16 proposals pass deterministic local evidence checks. **0 expert-adjudicated claims.** This is not a model benchmark or a semantic accuracy score.
- T0251 literal 心 counts in body-role rows: 9 in the two prefaces, 1 in the sūtra body. Headings, bylines and notes are excluded. This is a provenance audit, not a new textual-historical discovery.
- 245 N-Quads statements export claim, evidence, source, mapping-proposal and conset objects. The existing w3id ontology namespace is reused as a vocabulary identifier; its external resolution and a live TrustGraph load are not asserted.

Several claims share a single evidence window. The number of claims is not the number of independent observations. All historical interpretations, conset memberships and native-sense mappings remain proposals.

## Reproduce with the Python standard library

From the repository root:

```bash
python -m unittest discover -s tests -v
python src/verify_claims.py data/pnc2026/claims.json --out /tmp/ciwn-verification.json
python src/export_pnc_rdf.py data/pnc2026/claims.json /tmp/ciwn-claims.nq
```

To rebuild from the pinned Chinese XML and the Sanskrit transcription:

```bash
python src/build_pnc_demo.py
```

Network access is needed once. For an existing cache, add `--offline --cache /absolute/path/to/cache`. The cached raw Chinese files must match the release hashes before the build uses them; Sanskrit also uses a fixed release hash. A changed source must be reviewed as a new release, not silently reused.

The committed `cwn-native.json` is the small native-sense excerpt. Re-extraction from the original official data image is possible with:

```bash
python src/cwn_snapshot.py /path/to/cwn-2022.08.01.pyobj /path/to/manifest.json data/pnc2026/cwn-native.json
```

The image location is recorded by the public manifest. This reader restricts pickle globals to primitive container classes. It does not execute CwnGraph package code or relabel the image as a newer release.

## What changed in the importer

The earlier root traversal could collect header/back matter, descendant note text, and child tails out of order. The importer now traverses the TEI body recursively, preserves text order, skips editorial notes and secondary readings, selects the Taishō line stream, and keeps textual role and section path. Work-level translator and date fields are not copied into every section.

The extractor is a conservative reading-text importer, not a full critical-edition engine. Gaiji resolution uses declared Unicode mappings where available and otherwise retains an explicit marker. Substantive source interpretation remains a separate layer.

## Verification and retry boundaries

The Python verifier checks schema fields, supported relation types, evidence references, quote hashes, line windows, section boundaries, contextual source consistency, and required literal forms. It cannot establish semantic entailment or the absence of counterevidence. Passed claims enter an expert review queue.

The browser runs a documented subset of those checks locally. Its missing-evidence test deliberately changes one reference; the user can restore it and rerun. This demonstrates the intended gate and repair behavior. No LLM call, autonomous repair, live counterevidence search, or multi-agent comparison runs in the browser.

## Relationship to the earlier prototype

The files under `data/demo/` and their temporal CSV metrics remain **synthetic** demonstration data. They are not used by the new public evidence interface. The earlier `examples/claim_real_t0251_vijnana_shi.nq` is preserved as a historical artifact and contains an uncalibrated 0.98 score; use the new PNC export for the current score-free representation. Native IDs are preserved and proposed mappings are not promoted to accepted relations.

## Release ownership

`tbsg-cwn` owns data and research code. `sindia-site/public/buddhist` contains a static release snapshot. To refresh the website, copy `data/pnc2026/` to its `data/`, regenerate `data.js` from the same `claims.json`, and update the proposal and talk HTML from the corresponding Markdown files. Do not hand-edit website data independently.

See [the bilingual research proposal](ciwn_proposal_bilingual.md), [the PNC talk](pnc_talk_bilingual.md), and [source rights](../data/pnc2026/SOURCE_RIGHTS.md).
