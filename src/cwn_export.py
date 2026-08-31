"""Export native Chinese WordNet senses for TBSG/CWN.dia.

This script intentionally preserves CWN's native sense IDs and records a small
metadata sidecar so downstream diachronic analyses are reproducible.

The public CwnGraph manifest currently advertises v.2022.08.01 as its latest
image. Do not silently relabel that image as a newer CWN release.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

DEFAULT_LEMMAS = ["心", "意", "識"]


def node_id(node):
    for attr in ("id", "node_id", "sense_id"):
        value = getattr(node, attr, None)
        if value is not None:
            return str(value)
    text = repr(node)
    if "[" in text and "]" in text:
        return text.split("[", 1)[1].split("]", 1)[0]
    return text


def gloss_of(node):
    for attr in ("definition", "gloss", "defn"):
        value = getattr(node, attr, None)
        if value:
            return str(value)
    text = repr(node)
    return text.split(":", 1)[-1].rstrip("> ") if ":" in text else text


def relation_rows(sense):
    rows = []
    for rel in getattr(sense, "relations", []) or []:
        if len(rel) != 3:
            continue
        rel_type, other, direction = rel
        rows.append({
            "source_sense_id": node_id(sense),
            "relation": str(rel_type),
            "target_node_id": node_id(other),
            "target_repr": repr(other),
            "direction": str(direction),
        })
    return rows


def export_cwn(lemmas, out_dir: Path, image_tag: str | None = None):
    try:
        from CwnGraph import CwnImage
    except ImportError as exc:
        raise SystemExit(
            "CwnGraph is not installed. Install the optional dependency first: "
            "pip install git+https://github.com/lopentu/CwnGraph.git"
        ) from exc

    cwn = CwnImage(image_tag) if image_tag else CwnImage.latest()
    out_dir.mkdir(parents=True, exist_ok=True)

    senses_out = []
    relations_out = []

    for query in lemmas:
        # find_lemma accepts regex; anchors ensure exact lemma matching.
        candidates = cwn.find_lemma(f"^{query}$")
        for lemma in candidates:
            lemma_name = getattr(lemma, "lemma", query)
            for sense in getattr(lemma, "senses", []) or []:
                sid = node_id(sense)
                senses_out.append({
                    "sense_id": sid,
                    "lemma": str(lemma_name),
                    "query_lemma": query,
                    "gloss": gloss_of(sense),
                    "source": "Chinese WordNet / CwnGraph",
                    "layer": "modern_anchor",
                    "status": "NATIVE_CWN",
                })
                relations_out.extend(relation_rows(sense))

    senses = pd.DataFrame(senses_out).drop_duplicates()
    relations = pd.DataFrame(relations_out).drop_duplicates()
    senses.to_csv(out_dir / "cwn_senses.csv", index=False)
    relations.to_csv(out_dir / "cwn_relations.csv", index=False)

    meta = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "lemmas": list(lemmas),
        "requested_image_tag": image_tag,
        "loader": "CwnGraph.CwnImage",
        "note": (
            "CwnGraph's public manifest should be checked and recorded with each export. "
            "At repository setup time (2026-08-31), the manifest version was v2022.08 "
            "and the latest advertised image was v.2022.08.01."
        ),
    }
    (out_dir / "cwn_export_metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Exported {len(senses)} senses and {len(relations)} relations to {out_dir}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lemmas", nargs="+", default=DEFAULT_LEMMAS)
    parser.add_argument("--out", default="data/derived/cwn")
    parser.add_argument("--image-tag", default=None,
                        help="Pin a CwnGraph image tag instead of CwnImage.latest().")
    args = parser.parse_args()
    export_cwn(args.lemmas, Path(args.out), args.image_tag)


if __name__ == "__main__":
    main()
