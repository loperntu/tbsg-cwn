"""Extract CBETA main-text lines without mixing headers, notes, or witnesses.

Document order is preserved recursively (parent text, children, child tails).
Section paths retain prefaces and other contextual boundaries; date/translator
metadata are deliberately NOT propagated from the work to every line.
This is a conservative reading-text extractor, not a critical-edition merger.
"""
from __future__ import annotations
import argparse
import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path

TEI = '{http://www.tei-c.org/ns/1.0}'
CB = '{http://www.cbeta.org/ns/1.0}'
XML = '{http://www.w3.org/XML/1998/namespace}'
SKIP = {'note', 'rdg', 'mulu', 'anchor', 'teiHeader', 'back', 'fw'}


def localname(tag):
    return tag.split('}')[-1]


def extract_rows(xml_path):
    root = ET.parse(xml_path).getroot()
    body = root.find(f'{TEI}text/{TEI}body')
    if body is None:
        return []
    work = root.attrib.get(XML + 'id', Path(xml_path).stem)
    rows, buffer = [], []
    state = {'line_id': None, 'fascicle': None, 'section_path': [], 'text_role': 'body'}
    charmap = {}
    for char in root.findall(f'.//{TEI}char'):
        maps = {m.get('type'): m.text for m in char.findall(TEI + 'mapping')}
        charmap['#' + char.get(XML+'id', '')] = maps.get('normal_unicode') or maps.get('unicode')

    def flush():
        text = re.sub(r'\s+', '', ''.join(buffer))
        if text and state['line_id']:
            rows.append({'text_id': work, **state, 'section_path': list(state['section_path']), 'text': text})
        buffer.clear()

    def visit(el):
        name = localname(el.tag)
        if name in SKIP:
            return
        if name == 'lb':
            if el.get('ed', 'T') == 'T':
                flush(); state['line_id'] = el.get('n') or el.get(XML+'id')
            return
        if name == 'milestone' and el.get('unit') == 'juan':
            flush();state['fascicle'] = el.get('n');return
        if name == 'juan' and el.get('fun') == 'open':
            flush();state['fascicle'] = el.get('n')
        prior_path, prior_role = state['section_path'], state['text_role']
        if name == 'div':
            flush();state['section_path'] = prior_path + [el.get('type', 'unspecified')]
        if name in {'byline', 'head', 'jhead', 'docNumber'}:
            flush();state['text_role'] = name
        if name == 'g':
            value = charmap.get(el.get('ref'))
            if value:
                try: buffer.append(''.join(chr(int(c.removeprefix('U+'),16)) for c in value.split()))
                except ValueError: buffer.append('[' + el.get('ref','gaiji') + ']')
            else: buffer.append('[' + el.get('ref','gaiji') + ']')
        elif name == 'app':
            lemma = el.find(TEI+'lem')
            if lemma is not None: visit(lemma)
        elif name == 'choice':
            choices = list(el)
            chosen = next((c for c in choices if localname(c.tag) in {'corr','reg'}), choices[0] if choices else None)
            if chosen is not None: visit(chosen)
        else:
            if el.text: buffer.append(el.text)
            for child in el:
                visit(child)
                if child.tail: buffer.append(child.tail)
        if name == 'div' or name in {'byline','head','jhead','docNumber'}:
            flush();state['section_path'], state['text_role'] = prior_path, prior_role

    visit(body);flush()
    return rows


def extract_segments(xml_path):
    """Backward-compatible DataFrame API used by earlier notebooks."""
    import pandas as pd
    return pd.DataFrame(extract_rows(xml_path))


if __name__ == '__main__':
    ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');args=ap.parse_args()
    rows=extract_rows(args.input)
    with open(args.output,'w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['text_id','line_id','fascicle','section_path','text_role','text']);w.writeheader();w.writerows(rows)
    print(f'Wrote {len(rows)} segments to {args.output}')
