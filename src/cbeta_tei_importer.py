"""Minimal CBETA TEI/P5 importer scaffold for TBSG.

This does not perform Indic–Chinese alignment. It extracts Chinese text and
provenance-friendly line-break IDs so later alignment results can be attached
to stable evidence locations.
"""
import re
import sys
import xml.etree.ElementTree as ET
import pandas as pd


def localname(tag):
    return tag.split("}")[-1]


def extract_segments(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    rows = []
    current_lb = None
    buf = []

    def flush():
        nonlocal buf
        text = "".join(buf).strip()
        if text:
            rows.append({"line_id": current_lb or "unknown", "text": re.sub(r"\s+", "", text)})
        buf = []

    for el in root.iter():
        name = localname(el.tag)
        if name == "lb":
            flush()
            current_lb = el.attrib.get("n") or el.attrib.get("{http://www.w3.org/XML/1998/namespace}id")
        if el.text and name not in {"note"}:
            buf.append(el.text)
        if el.tail:
            buf.append(el.tail)
    flush()
    return pd.DataFrame(rows)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python src/cbeta_tei_importer.py INPUT.xml OUTPUT.csv")
        raise SystemExit(2)
    df = extract_segments(sys.argv[1])
    df.to_csv(sys.argv[2], index=False)
    print(f"Wrote {len(df)} segments to {sys.argv[2]}")
