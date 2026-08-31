"""Collect candidate CBETA occurrences for TBSG annotation.

Uses the CBETA developer API. The collector deliberately stores *candidates*;
these records are not treated as verified historical-sense annotations until a
human reviewer checks textual provenance and context.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import pandas as pd
import requests

API_BASE = "https://cbdata.dila.edu.tw/dev"
DEFAULT_TERMS = ["心", "意", "識"]


def search_term(term: str, rows: int = 100, start: int = 0,
                order: str = "time_from+") -> dict:
    url = f"{API_BASE}/search"
    # CBETA requests that API clients set Referer for access analytics.
    headers = {"Referer": "https://github.com/loperntu/tbsg-cwn"}
    params = {
        "q": term,
        "rows": rows,
        "start": start,
        "order": order,
        "fields": "work,juan,term_hits,time_from,time_to,creator,category,vol",
    }
    response = requests.get(url, params=params, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


def flatten_results(term: str, payload: dict):
    rows = []
    for item in payload.get("results", []):
        row = {"query_term": term, "source_api": "CBETA dev API"}
        if isinstance(item, dict):
            row.update(item)
        rows.append(row)
    return rows


def collect(terms, out_dir: Path, page_size: int = 100, max_pages: int = 1,
            sleep_s: float = 0.4):
    out_dir.mkdir(parents=True, exist_ok=True)
    all_rows = []
    raw = {}

    for term in terms:
        raw[term] = []
        for page in range(max_pages):
            payload = search_term(term, rows=page_size, start=page * page_size)
            raw[term].append(payload)
            all_rows.extend(flatten_results(term, payload))
            if len(payload.get("results", [])) < page_size:
                break
            time.sleep(sleep_s)

    pd.DataFrame(all_rows).to_csv(out_dir / "cbeta_search_candidates.csv", index=False)
    (out_dir / "cbeta_search_raw.json").write_text(
        json.dumps(raw, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Wrote {len(all_rows)} candidate volume/work records to {out_dir}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--terms", nargs="+", default=DEFAULT_TERMS)
    parser.add_argument("--out", default="data/raw/cbeta_search")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=1)
    args = parser.parse_args()
    collect(args.terms, Path(args.out), args.page_size, args.max_pages)


if __name__ == "__main__":
    main()
