from pathlib import Path
import math
import pandas as pd
import plotly.graph_objects as go
import gradio as gr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "demo"
EDGES = pd.read_csv(DATA / "demo_edges.csv")
SENSES = pd.read_csv(DATA / "demo_senses.csv")
LINKS = pd.read_csv(DATA / "demo_sense_links.csv")
INST = pd.read_csv(DATA / "demo_instances.csv")

SRC = ["citta", "manas", "vijñāna"]
TGT = ["心", "意", "識"]


def norm_edges(d):
    x = d.copy()
    x["p"] = x["count"] / x.groupby("source_term")["count"].transform("sum")
    return x


def entropy(d):
    x = norm_edges(d)
    total = x["count"].sum()
    h_total = 0.0
    for _, g in x.groupby("source_term"):
        ps = g["count"].sum() / total
        h_total += ps * (-sum(p * math.log2(p) for p in g["p"] if p > 0))
    return h_total


def translation_graph(period):
    d = norm_edges(EDGES[EDGES.period == period])
    pos = {t: (0, 2-i) for i, t in enumerate(SRC)}
    pos.update({t: (1, 2-i) for i, t in enumerate(TGT)})
    fig = go.Figure()
    for _, r in d.iterrows():
        a, b = pos[r.source_term], pos[r.target_term]
        fig.add_trace(go.Scatter(
            x=[a[0], b[0]], y=[a[1], b[1]], mode="lines",
            line=dict(width=1 + 9*r.p),
            hovertext=[f"{r.source_term} → {r.target_term}: {r.p:.3f}"]*2,
            hoverinfo="text", showlegend=False))
    for n, (x, y) in pos.items():
        fig.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text",
                                 marker=dict(size=34), text=[n], textposition="middle center",
                                 hoverinfo="text", hovertext=[n], showlegend=False))
    fig.update_layout(title=f"Layer A — Translation graph: {period}", height=420,
                      xaxis=dict(visible=False, range=[-.2, 1.2]),
                      yaxis=dict(visible=False, range=[-.6, 2.6]),
                      margin=dict(l=20, r=20, t=55, b=20))
    return fig


def sense_graph(lemma):
    hs = SENSES[(SENSES.lemma == lemma) & (SENSES.layer == "historical_buddhist")]
    cs = SENSES[(SENSES.lemma == lemma) & (SENSES.layer == "modern_anchor")]
    fig = go.Figure()
    nodes = []
    for i, (_, r) in enumerate(hs.iterrows()):
        nodes.append((r.sense_id, 0, i, r.gloss, "Historical Buddhist sense"))
    for i, (_, r) in enumerate(cs.iterrows()):
        nodes.append((r.sense_id, 1, i, r.gloss, "CWN modern anchor"))
    pos = {n[0]: (n[1], n[2]) for n in nodes}
    for _, r in LINKS.iterrows():
        if r.historical_sense_id in pos and r.cwn_sense_id in pos:
            a, b = pos[r.historical_sense_id], pos[r.cwn_sense_id]
            fig.add_trace(go.Scatter(x=[a[0], b[0]], y=[a[1], b[1]], mode="lines",
                                     line=dict(width=2 + 6*r.confidence),
                                     hovertext=[f"{r.relation}, conf={r.confidence:.2f}"]*2,
                                     hoverinfo="text", showlegend=False))
    for sid, x, y, gloss, layer in nodes:
        fig.add_trace(go.Scatter(x=[x], y=[y], mode="markers+text", marker=dict(size=38),
                                 text=[sid.replace("CWN_DEMO_", "CWN:").replace("BUD_", "BUD:")],
                                 textposition="bottom center", hovertext=[f"{layer}<br>{gloss}"],
                                 hoverinfo="text", showlegend=False))
    fig.update_layout(title=f"Layer B — Historical sense ↔ CWN anchor: {lemma}", height=390,
                      xaxis=dict(visible=False, range=[-.3, 1.3]),
                      yaxis=dict(visible=False, range=[-.6, max(1, len(cs))]),
                      margin=dict(l=20, r=20, t=55, b=45))
    return fig


def triage(lemma):
    return INST[INST.lemma == lemma][["instance_id", "period", "context", "indic_term",
                                      "assigned_sense_id", "llm_confidence",
                                      "cwn_compatibility", "decision"]]


def metrics():
    rec = []
    for p, g in EDGES.groupby("period", sort=False):
        rec.append([p, int(g["count"].sum()), round(entropy(g), 3)])
    return pd.DataFrame(rec, columns=["period", "aligned_tokens", "H(Chinese|Indic) bits"])


def explain(lemma):
    return f"""### Open-world sense policy for **{lemma}**

1. Treat CWN senses as **modern anchors**, not as a closed historical inventory.
2. Assign a Buddhist occurrence to an existing historical sense when contextual evidence is adequate.
3. If no historical/CWN-linked sense gives adequate coverage, route it to `NEW_BUDDHIST_SENSE`.
4. Human review distinguishes contextual modulation, domain specialization, genuine historical innovation, and annotation/alignment error.

**Important:** all CWN IDs and glosses in this demo are placeholders. Replace them with exported CwnGraph/CWN records before analysis.
"""


def update(period, lemma):
    return translation_graph(period), sense_graph(lemma), triage(lemma), metrics(), explain(lemma)


with gr.Blocks(title="TBSG + CWN.dia Prototype") as demo:
    gr.Markdown("""
# TBSG + CWN.dia — Prototype

**Indic lexical concept → Buddhist historical sense → modern CWN sense anchor**

The key design choice is **open-world sense induction**: CWN constrains and anchors analysis,
but does not force historical Buddhist usages into a modern sense inventory.

⚠️ The bundled data, CWN IDs, glosses, alignments, and counts are synthetic demonstration material.
""")
    with gr.Row():
        period = gr.Dropdown(list(EDGES.period.drop_duplicates()), value=EDGES.period.iloc[0], label="Period")
        lemma = gr.Dropdown(TGT, value="心", label="Chinese lemma")
    trans = gr.Plot()
    sg = gr.Plot()
    gr.Markdown("## Candidate sense assignment / NEW SENSE queue")
    inst = gr.Dataframe(interactive=False)
    note = gr.Markdown()
    gr.Markdown("## Diachronic diagnostic")
    met = gr.Dataframe(interactive=False)
    for c in [period, lemma]:
        c.change(update, [period, lemma], [trans, sg, inst, met, note])
    demo.load(update, [period, lemma], [trans, sg, inst, met, note])

if __name__ == "__main__":
    demo.launch()
