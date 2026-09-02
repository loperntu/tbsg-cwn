# TBSG + CWN.dia: A Provenance-Aware Temporal Semantic Hypergraph for Buddhist Computational Philology
# TBSG + CWN.dia：面向佛典計算文獻學的可溯源歷時語義超圖

## 1. Project Summary｜計畫摘要

### 中文

本計畫旨在建立一套可計算、可追溯、可否證的佛典歷時語義研究架構，暫名 **TBSG + CWN.dia**（Temporal Buddhist Semantic Graph with diachronic Chinese WordNet）。研究核心問題不是單純追蹤某一詞在歷史中的詞頻或向量漂移，而是分析佛教概念系統如何在跨語翻譯、譯者選擇、時代變遷與宗派／文類脈絡中發生**關係網絡的重組（graph rewiring）**。

第一階段以漢語「心、意、識」與 Indic `citta, manas, vijñāna` 為核心案例，結合 CBETA 佛典語料、可得之梵語／巴利語平行文本，以及 Chinese WordNet（CWN）的現代義項網絡。研究將建立三個互相區分但可連接的層次：

1. **TrustGraph infrastructure layer**：以 RDF/OWL、named graphs 與 provenance 支援可查詢的 evidence/claim hypergraph；
2. **TBSG analytical layer**：定義時間、譯者、文類與翻譯傳統下的語義網絡變化；
3. **CWN.dia lexical ontology layer**：建立佛典歷史義項與現代 CWN sense 之間的 sense genealogy。

本計畫特別強調：知識圖譜中的 edge 不等於學術事實。每一項語義或翻譯主張都必須是一個 **epistemically qualified claim**，包含 textual evidence、provenance、uncertainty、counterevidence 與 human adjudication。最終目標是從一般的 `retrieve → generate` AI humanities workflow，轉向：

`retrieve → hypothesize → seek evidence → seek counterevidence → verify → graph → revise`。

### English

This project proposes **TBSG + CWN.dia** (Temporal Buddhist Semantic Graph with diachronic Chinese WordNet), a provenance-aware and falsifiable framework for computational Buddhist philology. Rather than treating diachronic semantics as simple frequency change or vector drift, the project investigates how **conceptual relations are rewired** across translation periods, translators, genres, and doctrinal traditions.

The initial case study focuses on Chinese `心 / 意 / 識` and Indic `citta / manas / vijñāna`, integrating CBETA Buddhist corpora, available Sanskrit/Pāli parallel witnesses, and the modern sense inventory of Chinese WordNet (CWN). The architecture separates three complementary layers:

1. a **TrustGraph infrastructure layer** for RDF/OWL-based evidence, provenance, named graphs, and claim-level hypergraph representation;
2. a **TBSG analytical layer** that operationalizes temporal semantic change and graph rewiring;
3. a **CWN.dia lexical ontology layer** that models genealogical relations between Buddhist historical senses and modern CWN senses.

A central methodological commitment is that a graph edge is not automatically a scholarly fact. Every semantic or translation assertion is represented as an **epistemically qualified claim** carrying textual evidence, provenance, uncertainty, counterevidence, and human adjudication status. The long-term goal is to move AI-assisted humanities research from a `retrieve → generate` paradigm toward a more scholarly workflow:

`retrieve → hypothesize → seek evidence → seek counterevidence → verify → graph → revise`.

---

## 2. Background and Motivation｜研究背景與動機

### 中文

佛教典籍提供了一個罕見且理想的歷時語義研究場域。大量漢譯佛典橫跨二世紀至中古時期，存在不同譯者、譯場、宗派、文類以及梵語、巴利語、藏語等跨語證據。對歷史語義而言，這意味著我們不只觀察：

`心_3C → 心_5C → 心_7C`

還可能觀察：

`citta / manas / vijñāna → 心 / 意 / 識 → modern CWN senses`。

因此佛典語料有機會讓我們區分至少三種現象：漢語自身的 semantic change、translation-induced semantic change，以及佛教知識體系內部的 terminological specialization。

既有數位佛學或 Buddhist RAG 系統主要解決「找到哪些文本與問題相關」；歷時詞向量研究則常將一個詞壓縮為單一時間向量。兩者都較難處理以下問題：某一詞形在不同時期究竟包含哪些義項？義項是否出現、分化、穩定或消失？不同譯者是否重新配置同一組 Indic concepts 與漢語詞彙的對應？每個推論能否回到具體經文、平行文本與反例？

### English

Buddhist textual traditions provide an unusually rich environment for diachronic lexical-semantic research. Chinese Buddhist translations span centuries and involve multiple translators, translation bureaus, genres, doctrinal communities, and parallel witnesses in Sanskrit, Pāli, Tibetan, and other languages. This creates a rare form of cross-lingual semantic control.

Instead of observing only:

`心_3C → 心_5C → 心_7C`,

we may also observe:

`citta / manas / vijñāna → 心 / 意 / 識 → modern CWN senses`.

This makes it possible to distinguish, at least analytically, among semantic change internal to Chinese, translation-induced semantic change, and terminological specialization internal to Buddhist intellectual traditions.

Most existing Buddhist retrieval or RAG systems answer the question of which passages are relevant to a query. Diachronic embedding approaches, meanwhile, often compress a lexical item into one vector per period. Neither approach is well suited to tracking sense emergence, differentiation, stabilization, disappearance, translator-specific lexicalization, or the evidence path behind a historical claim. TBSG + CWN.dia is designed to address precisely these gaps.

---

## 3. Research Objectives and Questions｜研究目標與問題

### 中文

本計畫有四項主要目標：建立佛典歷史義項與翻譯關係的 evidence graph；將 CWN 擴展為可容納歷史義項但不污染現代詞網本體的 CWN.dia layer；定義可量化的 temporal graph rewiring 指標；最後加入可主動尋找支持與反證的 agentic verification workflow。

核心研究問題為：

**RQ1 — Historical sense structure**：佛典中的「心、意、識」能在多大程度上對應到現代 CWN 的既有義項？哪些用例需要 specialization、extension、no-modern-equivalent 或 NEW_BUDDHIST_SENSE？

**RQ2 — Translation-semantic organization**：`citta / manas / vijñāna` 與「心／意／識」的 many-to-many 對應是否隨時代、譯者或翻譯傳統而系統性改變？

**RQ3 — Graph rewiring**：這些改變是否可描述為 lexical compression、differentiation、stabilization，或其他非單調的 network reconfiguration？

**RQ4 — Epistemic reliability**：帶有 provenance、counterevidence 與 human adjudication 的 claim graph，是否能比一般 single-agent/RAG 產生更高的 philological support rate 與更低 unsupported-claim rate？

### English

The project has four objectives: (i) construct an evidence graph of Buddhist historical senses and translation relations; (ii) extend CWN with a separate diachronic layer without altering the synchronic ontology; (iii) operationalize temporal graph rewiring; and (iv) introduce agentic workflows that actively seek both support and counterevidence.

The main research questions are:

**RQ1 — Historical sense structure:** To what extent can Buddhist usages of `心 / 意 / 識` be mapped to existing modern CWN senses? Which usages require `specialization_of`, `extension_of`, `no_modern_equivalent`, or `NEW_BUDDHIST_SENSE`?

**RQ2 — Translation-semantic organization:** Do the many-to-many correspondences between `citta / manas / vijñāna` and `心 / 意 / 識` vary systematically by period, translator, or translation tradition?

**RQ3 — Graph rewiring:** Can these differences be characterized as lexical compression, differentiation, stabilization, or other non-monotonic forms of network reconfiguration?

**RQ4 — Epistemic reliability:** Does a provenance-bearing claim graph with counterevidence and human adjudication achieve higher philological support and lower unsupported-claim rates than ordinary single-agent or RAG workflows?

---

## 4. Conceptual Contribution｜概念與理論貢獻

### 中文

本研究將歷時語義的基本單位從「word at time t」改成「sense-and-relation configuration at time t」。換言之，研究對象不是單一詞向量的移動，而是整個 conceptual neighborhood 的重組：

`G_t = (V, E_t, S_t, Q_t)`，

其中 `V` 為 lexical/concept nodes，`E_t` 為某時段的語義或翻譯 relations，`S_t` 為 sense inventory，`Q_t` 則包含 evidence quality、confidence 與 adjudication status。

第二項理論貢獻是提出 **lexical sense genealogy**。佛典歷史義項不直接等同 CWN 現代 sense，而允許：

- equivalent_to
- specialization_of
- extension_of
- related_to
- no_modern_equivalent
- predecessor_sense / successor_sense

因此 WordNet coverage failure 不再只是 annotation failure，而可能成為歷時語義訊號。

第三項貢獻是 **epistemically qualified hypergraph**：

`Claim = Statement + Evidence + Provenance + Uncertainty + Counterevidence + Human Adjudication`。

### English

The project shifts the basic unit of diachronic semantics from a “word at time t” to a **sense-and-relation configuration at time t**. The object of study is therefore not merely vector displacement, but reconfiguration of a conceptual neighborhood:

`G_t = (V, E_t, S_t, Q_t)`,

where `V` denotes lexical/conceptual nodes, `E_t` temporal semantic or translation relations, `S_t` the sense inventory, and `Q_t` epistemic qualifications such as evidence quality, confidence, and adjudication status.

A second contribution is the notion of **lexical sense genealogy**. Buddhist historical senses are not forced into modern CWN senses but may stand in relations such as `equivalent_to`, `specialization_of`, `extension_of`, `related_to`, `no_modern_equivalent`, `predecessor_sense`, and `successor_sense`.

A third contribution is an **epistemically qualified hypergraph**, in which scholarly claims are represented as:

`Claim = Statement + Evidence + Provenance + Uncertainty + Counterevidence + Human Adjudication`.

---

## 5. System Architecture｜系統架構

### 中文

TrustGraph 在本計畫中不是研究理論，而是底層 semantic/provenance substrate。TrustGraph 2026 版本已提供 RDF/OWL context graph、named graphs、PROV-O provenance、GraphRAG 與 agent orchestration，因此特別適合承載佛典文獻學中天然的 n-ary claim。

系統架構如下：

```text
CBETA / Sanskrit / Pāli / CWN
            │
            ▼
  Retrieval and ingestion
            │
            ▼
 Evidence / Attestation objects
            │
            ▼
 Epistemically qualified claims
            │
            ▼
   TrustGraph hypergraph
            │
   ┌────────┼─────────┐
   │        │         │
source   default   retrieval
prov.     facts     traces
            │
            ▼
     TBSG analysis layer
            │
            ▼
         CWN.dia
            │
            ▼
       Modern CWN
```

TBSG 另建議增加 `urn:graph:adjudication`，用來保存人工判斷、爭議、反例、被 supersede 的 claim 與修訂歷史。這是本計畫對 TrustGraph provenance model 的 humanities-oriented extension。

### English

TrustGraph is not treated as the theory of semantic change; it serves as the semantic and provenance substrate. Its 2026 architecture provides RDF/OWL context graphs, named graphs, PROV-O provenance, GraphRAG, and agent orchestration, making it well suited to the inherently n-ary nature of philological claims.

The proposed stack is:

```text
CBETA / Sanskrit / Pāli / CWN
            │
            ▼
  Retrieval and ingestion
            │
            ▼
 Evidence / Attestation objects
            │
            ▼
 Epistemically qualified claims
            │
            ▼
   TrustGraph hypergraph
            │
   ┌────────┼─────────┐
   │        │         │
source   default   retrieval
prov.     facts     traces
            │
            ▼
     TBSG analysis layer
            │
            ▼
         CWN.dia
            │
            ▼
       Modern CWN
```

TBSG further proposes an `urn:graph:adjudication` layer for human decisions, disagreement, counterevidence, superseded claims, and revision history. This constitutes a humanities-oriented extension of the provenance model.

---

## 6. Data and Initial Scope｜資料與初始範圍

### 中文

第一階段刻意維持小而可驗證的資料規模。核心 lexical set 為「心、意、識」以及 `citta, manas, vijñāna`。資料來源包括：CBETA 漢譯佛典；可取得且有可靠對勘關係之 Sanskrit/Pāli parallels；Chinese WordNet；譯者、年代、經號、卷次與相關 bibliographic metadata。

第一個 gold dataset 目標為 100–300 個人工核驗 occurrence。每筆至少保存：text ID、passage/line ID、完整局部語境、lemma、translator/tradition、normalized date/period、Indic parallel（如有）、historical sense candidate、CWN sense candidate、alignment/sense confidence、human status 與 counterevidence note。

### English

The first phase deliberately keeps the dataset small and auditable. The core lexical set is `心 / 意 / 識` and `citta / manas / vijñāna`. Sources include CBETA Chinese Buddhist texts, securely aligned Sanskrit/Pāli parallels where available, Chinese WordNet, and bibliographic metadata such as translator, date, text ID, and fascicle/passage information.

The first gold dataset will contain approximately 100–300 manually verified occurrences. Each record will preserve at minimum: text ID, passage/line identifier, local context, lemma, translator/tradition, normalized date/period, Indic parallel when available, historical-sense candidate, CWN sense candidate, separate alignment/sense confidence scores, human adjudication status, and counterevidence notes.

---

## 7. Methodology and Work Packages｜方法與工作項目

### WP1 — CWN.dia Sense Anchoring｜CWN.dia 義項錨定

中文：從 CwnGraph 匯出「心、意、識」的 native sense IDs、glosses、relations 與版本資訊。對佛典 occurrence 進行 open-world sense annotation，不強迫所有歷史用例落入現代 sense inventory。低相容度案例進入 `NEW_BUDDHIST_SENSE` queue，再由人工判斷 contextual modulation、domain specialization、historical innovation 或 annotation error。

English: Export native CWN sense IDs, glosses, relations, and version metadata through CwnGraph. Annotate Buddhist occurrences under an open-world policy rather than forcing them into a closed modern sense inventory. Low-compatibility cases enter a `NEW_BUDDHIST_SENSE` queue for adjudication as contextual modulation, domain specialization, historical innovation, or annotation error.

### WP2 — Evidence and Provenance Graph｜證據與溯源圖

中文：將每個 occurrence 與 translation/sense claim 轉成 addressable evidence objects。來源驗證、alignment、sense assignment 與 diachronic relation 分別給予 status/confidence，不使用單一混合 confidence score。

English: Convert each occurrence and translation/sense assertion into addressable evidence objects. Source verification, lexical alignment, sense assignment, and diachronic relation are tracked separately rather than collapsed into a single confidence score.

### WP3 — Cross-Lingual Translation Graph｜跨語翻譯圖

中文：建立 `P(Chinese | Indic, period, translator)` 與相反方向分布，研究 many-to-many lexicalization。先從 securely aligned passages 開始，不以 LLM 自動對齊取代 philological validation。

English: Estimate distributions such as `P(Chinese | Indic, period, translator)` and their reverse mappings to model many-to-many lexicalization. Analysis begins with securely aligned passages; LLM alignment proposals do not substitute for philological validation.

### WP4 — Temporal Graph Rewiring｜歷時圖重組

中文：對不同 period/translator slices 建立 `G_t`，比較 edge weights、neighborhood、sense inventory 與 network topology。候選指標包括 conditional entropy、Jensen–Shannon divergence、edge turnover、sense birth/death、graph-edit distance 及 neighborhood change。

English: Construct temporal/translator-specific graphs `G_t` and compare edge weights, neighborhoods, sense inventories, and topology. Candidate diagnostics include conditional entropy, Jensen–Shannon divergence, edge turnover, sense birth/death, graph-edit distance, and neighborhood change.

### WP5 — DharmaSwarm Verification｜多代理驗證

中文：後續加入 retrieval agent、alignment agent、sense agent、counterexample agent 與 verifier。agents 共同讀寫 TrustGraph，但只有帶 provenance 與 qualification 的 claim 才能進入 active scholarly graph。

English: A later stage introduces retrieval, alignment, sense, counterexample, and verification agents. Agents share TrustGraph as structured memory, but only provenance-bearing, epistemically qualified claims may enter the active scholarly graph.

---

## 8. Evaluation｜評估設計

### 中文

評估分為三層。第一層是資料品質：source citation accuracy、alignment accuracy/agreement、sense annotation agreement、provenance completeness。第二層是歷時模型：比較 period/translator-conditioned distributions，並以 bootstrap 或 permutation testing 評估 observed rewiring 是否超出樣本變異。第三層是 AI scholarly reliability：比較 lexical baseline、single LLM、multi-agent、multi-agent + verification。

核心指標包括：

**Philological Support Rate (PSR)**

`PSR = supported claims / generated claims`

**Counterevidence Survival Rate (CSR)**

`CSR = claims surviving adversarial counterexample search / initially supported claims`

另報 unsupported claim rate、citation accuracy、calibration 與 human acceptance rate。

### English

Evaluation proceeds at three levels. First, data quality is measured through source citation accuracy, alignment agreement/accuracy, sense annotation agreement, and provenance completeness. Second, temporal models compare period- and translator-conditioned distributions, with bootstrap or permutation procedures used to determine whether observed rewiring exceeds sampling variation. Third, scholarly AI reliability is evaluated by comparing lexical baselines, single-LLM workflows, multi-agent systems, and multi-agent systems with explicit verification.

Two central metrics are:

**Philological Support Rate (PSR)**

`PSR = supported claims / generated claims`

**Counterevidence Survival Rate (CSR)**

`CSR = claims surviving adversarial counterexample search / initially supported claims`

Unsupported-claim rate, citation accuracy, calibration, and human acceptance rate will also be reported.

---

## 9. Confounds and Methodological Controls｜混淆因素與控制

### 中文

歷時語義結果不能直接歸因於「時代」。主要 confounds 包括 translator × period 共變、genre composition、文本之間的依賴關係、同一底本的重複、不同時期樣本量差異、OCR/encoding 問題以及 parallel alignment uncertainty。因此本研究至少同時報 period-conditioned 與 translator-conditioned analysis，並在可能情況下使用 matched text sets。

此外，`compression → differentiation → stabilization` 只是一個可檢驗假說，不是預設歷史敘事。若資料顯示 cyclic、translator-specific 或 non-monotonic rewiring，同樣構成有意義的研究結果。

### English

Temporal results cannot be attributed directly to “time.” Major confounds include translator–period collinearity, genre composition, textual dependence, repeated recensions, unequal sample sizes, encoding/OCR issues, and uncertainty in parallel alignment. The project therefore reports both period-conditioned and translator-conditioned analyses and uses matched text sets whenever possible.

The trajectory `compression → differentiation → stabilization` is explicitly treated as a falsifiable hypothesis rather than a presumed historical narrative. Cyclic, translator-specific, or otherwise non-monotonic rewiring is equally informative.

---

## 10. Three-Week MVP｜三週最小可行版本

### 中文

**Week 1：資料與 ontology。** 完成真實 CWN「心／意／識」sense export；建立 TBSG/CWN.dia RDF/OWL ontology draft；抽取第一批 CBETA candidates 並人工確認至少 50–100 筆。

**Week 2：claim graph。** 將 verified occurrences 轉為 claim/evidence objects；完成最小 TrustGraph-compatible RDF/N-Quads export；建立 historical sense ↔ CWN relation annotation；若平行文本足夠，加入第一批 Indic alignment。

**Week 3：分析與 demo。** 產生至少兩個 temporal/translator graph slices；計算 translation distribution 與基本 rewiring diagnostics；完成可點回 textual evidence 的視覺化；整理一個可被支持或反駁的 preliminary historical-semantic finding。

成功標準不是完成整套大藏經，而是：

> **Demonstrate one auditable case of semantic graph rewiring whose evidence path can be traced from a quantitative pattern back to individual Buddhist passages.**

### English

**Week 1 — Data and ontology.** Complete real CWN exports for `心 / 意 / 識`; draft the TBSG/CWN.dia RDF/OWL ontology; retrieve CBETA candidates and manually verify at least 50–100 occurrences.

**Week 2 — Claim graph.** Convert verified occurrences into claim/evidence objects; produce a minimal TrustGraph-compatible RDF/N-Quads export; annotate historical-sense ↔ CWN relations; add the first Indic alignments if secure parallels are available.

**Week 3 — Analysis and demo.** Construct at least two temporal or translator-specific graph slices; compute translation distributions and basic rewiring diagnostics; provide visualization with passage-level evidence drill-down; formulate one preliminary historical-semantic finding that can be independently challenged.

The success criterion is not coverage of the entire Buddhist canon, but:

> **Demonstrate one auditable case of semantic graph rewiring whose evidence path can be traced from a quantitative pattern back to individual Buddhist passages.**

---

## 11. Longer-Term Development｜中長期發展

### 中文

完成「心、意、識」後，可擴展到「空、色、法、緣、業、情、念、想」等概念，並納入不同譯者、時代、宗派與文類。CWN.dia 可逐步發展為 diachronic Chinese lexical knowledge resource；TBSG 則可擴展為 Buddhist Conceptual Change Graph。TrustGraph 最終可成為 DharmaSwarm 的 shared scholarly memory，使 agents 不共享不透明的 message history，而共享可查詢、可版本化、可追溯的 claims。

### English

After the initial `心 / 意 / 識` case, the framework can expand to concepts such as `空, 色, 法, 緣, 業, 情, 念, 想`, across translators, periods, schools, and genres. CWN.dia may develop into a reusable diachronic Chinese lexical knowledge resource, while TBSG can grow into a broader Buddhist Conceptual Change Graph. TrustGraph can ultimately serve as the shared scholarly memory for DharmaSwarm, allowing agents to exchange queryable, versioned, provenance-bearing claims rather than opaque message histories.

---

## 12. Expected Outputs｜預期成果

### 中文

預期成果包括：

- 一套 TBSG/CWN.dia ontology 與 claim schema；
- 100–300 筆人工核驗的「心／意／識」歷時佛典資料；
- CWN historical-sense mapping resource；
- TrustGraph-compatible evidence/provenance graph prototype；
- Temporal graph rewiring 分析工具與互動視覺化；
- 一篇以 computational historical semantics / computational philology 為核心的方法論論文；
- 後續可擴展之 DharmaSwarm verification framework。

### English

Expected outputs include:

- a TBSG/CWN.dia ontology and scholarly claim schema;
- a manually verified 100–300-instance diachronic Buddhist dataset for `心 / 意 / 識`;
- a CWN historical-sense mapping resource;
- a TrustGraph-compatible evidence/provenance graph prototype;
- temporal graph-rewiring analysis and interactive visualization tools;
- a methodological paper in computational historical semantics / computational philology;
- an extensible DharmaSwarm verification framework.

---

## 13. Significance｜研究意義

### 中文

本研究的學術意義不在於「讓 AI 讀佛經」，而在於重新界定 AI 如何參與文獻學與歷史語義研究。系統不把 LLM 當作答案機，而把它當成 hypothesis generator、evidence retriever 與 adversarial verifier；知識圖譜也不被視為真理庫，而是一個可修訂的 scholarly claim space。

因此，本研究試圖建立一種新的 computational philology infrastructure：其最小知識單位不是 chunk、embedding 或裸 triple，而是具有證據、時間、來源、不確定性、反例與人工判斷的 claim。這一框架不僅適用佛典，也可延伸至古典漢籍、翻譯史、宗教文本、法律史料與其他具有版本、引用與跨語關係的人文資料。

### English

The significance of this project lies not in simply “using AI to read Buddhist texts,” but in redefining how AI can participate in philology and historical semantics. LLMs are treated as hypothesis generators, evidence retrievers, and adversarial verifiers rather than answer machines; the graph is treated not as a store of truth but as a revisable scholarly claim space.

The project therefore proposes a new kind of computational philology infrastructure in which the minimal unit of knowledge is not a chunk, embedding, or bare triple, but a claim with evidence, time, provenance, uncertainty, counterevidence, and human adjudication. Although Buddhist texts provide the initial testbed, the framework is potentially applicable to classical Chinese corpora, translation history, religious texts, legal-historical archives, and other humanities domains characterized by versions, citations, and cross-lingual relations.

---

## 14. Technical References and Resources｜技術參考資源

- TrustGraph: https://github.com/trustgraph-ai/trustgraph
- TrustGraph documentation: https://docs.trustgraph.ai/
- TrustGraph context graph / ontology guides: https://trustgraph.ai/guides/key-concepts/
- Chinese WordNet / CwnGraph: https://github.com/lopentu/CwnGraph
- CBETA developer resources: https://cbdata.dila.edu.tw/dev/
- TBSG + CWN.dia repository: https://github.com/loperntu/tbsg-cwn

## Working Title｜暫定題目

**English:** *From Translation Evidence to Lexical Sense Genealogy: A Provenance-Aware Temporal Semantic Hypergraph for Buddhist Computational Philology*

**中文：**〈從翻譯證據到詞義譜系：面向佛典計算文獻學的可溯源歷時語義超圖〉
