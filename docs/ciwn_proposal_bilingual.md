# CiWN：具脈絡、可溯源的佛教語意資源
# CiWN: Contextual and Evidence-Grounded Buddhist Semantic Resources

**研究計畫討論稿｜Research proposal · 7 September 2026**  
**主持人｜Principal investigator:** 謝舒凱 Shu-Kai Hsieh，國立臺灣大學語言學研究所  
**架構｜Programme:** Sinographia Diachronica (SinDia) → CiWN / CWN.dia / TBSG / DharmaSwarm  
**網站｜Website:** [SinDia Buddhist Semantics](https://lopentu.github.io/sindia-site/buddhist/)  
**研究原始碼｜Research repository:** [TBSG + CWN.dia](https://github.com/loperntu/tbsg-cwn)

> **核心命題：佛教語意資源的基本單位，應是具有文獻脈絡與證據的可修訂主張。**  
> **Central proposition: Buddhist semantic resources should organize revisable claims whose meanings and evidential scope remain explicit.**

## 1. 計畫摘要｜Abstract

**中文。** 佛教文獻的數位化、詞典編纂與跨語檢索，已提供豐厚的研究基礎。在此基礎上，本計畫提出 CiWN（Citta WordNet），建立一套能保存歷史、宗派、文類與翻譯脈絡的佛教語意資源。CiWN 保留 WordNet 的義項區分與關係表示，同時將脈絡限定的概念群（context-bounded consets）及可溯源的學術主張納入架構。概念群的成員資格由文本書證與專家審核共同決定；向量表示提供候選，不直接決定同義性。

研究以「心、意、識」為起點，連結 CBETA、梵文平行材料與 Chinese WordNet（CWN）的原生義項。CWN.dia 負責歷史義項與現代詞網的對照及經證據支持的譜系；TBSG 分析不同時間與文獻脈絡中的關係配置；DharmaSwarm 則逐步建置提出候選、核對來源、尋找反例與修訂的研究流程。第一階段以小規模、可重跑的資料與驗證實驗為主，評估脈絡化表示是否改善義項涵蓋與詮釋透明度，以及明確驗證是否提高經獨立人工判定的主張品質。

**English.** Digitized canons, Buddhist dictionaries, and multilingual retrieval systems provide a substantial foundation for textual research. Building on these resources, CiWN (Citta WordNet) proposes a contextual semantic resource that preserves historical, doctrinal, generic, and translational distinctions. The framework retains sense-level lexical organization while introducing context-bounded concept groupings, provisionally termed *consets*, and evidence-bearing scholarly claims. Membership in a conset is a revisable assertion; embedding similarity proposes candidates rather than establishing synonymy.

The initial study examines 心, 意, and 識 through CBETA passages, Sanskrit parallels, and native Chinese WordNet (CWN) senses. CWN.dia records historical-sense mappings and evidence-supported genealogies; TBSG analyzes relational configurations across time and textual contexts; DharmaSwarm develops workflows for proposal, source checking, counterevidence search, and revision. The first phase prioritizes a small reproducible dataset and controlled evaluation. It asks whether contextual representation improves sense coverage and interpretability, and whether explicit verification improves independently adjudicated claim quality.

## 2. 研究定位與既有成果｜Positioning and related resources

**中文。** 本計畫將既有成果視為互補的基礎建設。CBETA 提供可定位的漢文佛典與校勘資訊；CWN 提供現代漢語義項、釋義及詞彙關係；MITRA 提供佛教語域的跨語平行材料與語意檢索模型。MITRA 論文報告 174 萬組句級平行資料，並提出 Gemma 2 MITRA-E；這是可評估的外部方法，並非本計畫已完成的模型訓練。[MITRA 論文](https://arxiv.org/abs/2601.06400)

Sanskrit Sembank 將詞典、WordNet 概念與 Sanskrit 語境標註相連，是本計畫建立義項標註語料的相關先例。CiWN 進一步關注的是：同一詞形在不同文獻脈絡中如何連結不同義項；概念群成員資格如何依脈絡變動；模型或研究者所提出的關係如何受到來源、反例與審核歷程約束。[Hellwig & Biagetti, 2025](https://doi.org/10.1007/s10579-025-09852-1)

**English.** Existing resources serve complementary roles. CBETA supplies addressable Chinese passages and editorial information; CWN provides contemporary Chinese senses and lexical relations; MITRA offers Buddhist-domain parallel data and semantic retrieval models. The MITRA paper reports 1.74 million parallel sentence pairs and introduces Gemma 2 MITRA-E. These are external resources to evaluate, not models trained by this project. The Sanskrit Sembank supplies an important precedent for linking lexicography, WordNet concepts, and contextual Sanskrit annotation. CiWN focuses on contextual membership, open-inventory historical annotation, and independently reviewable semantic claims. It does not claim to be the first Buddhist knowledge graph or multilingual alignment system.

**預期貢獻／Expected contribution.** 可檢驗的貢獻是「脈絡化義項表示 × 保留原生詞網錨點 × 可拒收的證據工作流程」的結合，而非 conset 一詞、向量聚類或代理人數量本身的首創性。A defensible contribution lies in the evaluated combination of contextual representation, native lexical anchors, and evidence-gated workflows—not in the term *conset*, clustering alone, or the number of agents.

## 3. 五個模組的分工｜Five complementary components

| 模組 Component | 責任 Responsibility | 現階段狀態 Current status |
|---|---|---|
| **CiWN** | 佛教詞形、用例、義項、概念群與主張／Buddhist forms, attestations, senses, consets, and claims | 概念與資料模型；小型候選集合／Model and small candidate collection |
| **CWN.dia** | 歷史義項與原生 CWN 義項的關係；有證據的譜系／Historical-sense mappings and evidence-supported genealogy | 已匯出原生義項；對應仍為候選／Native export completed; mappings remain proposals |
| **TBSG** | 依時間、譯者、文類與文本層次分析關係／Relational analysis by time, translator, genre, and textual layer | 分析設計；尚無經驗證的歷時效應／Design; no validated temporal effect |
| **DharmaSwarm** | 候選提出、來源檢查、反例搜尋、有限重試與審核／Proposal, source checks, counterevidence, bounded retry, review | 來源檢查與受控重試已實作；LLM swarm 待評估／Mechanical core implemented; LLM swarm planned |
| **TrustGraph** | 可替換的圖與代理協作基礎設施／Replaceable graph and agent infrastructure | 外部候選；未完成實際整合／External candidate; integration pending |

**中文。** SinDia 是整體研究入口，HCC 是可對接的語料與檢索設施。研究問題與資料交換格式應獨立於任何單一圖資料庫或代理框架。TrustGraph 官方資料提供相關圖檢索與代理工作流程能力；本計畫仍須實測命名圖、來源保存、匯出及版本相容性，不能將 RDF 語法正確等同於整合完成。[TrustGraph 2.6](https://trustgraph.ai/news/release-2-6)

**English.** SinDia is the programme’s public entry point, while HCC can supply corpus services. Research definitions and exchange formats remain independent of the backend. TrustGraph is a plausible infrastructure option, but named-graph preservation, provenance round-tripping, and version compatibility require explicit integration tests. Valid RDF alone does not establish backend compatibility.

## 4. 從 synset 到脈絡限定的 conset｜Context-bounded consets

**中文。** 不宜將「不用 gloss、改用 embeddings」視為兩條互斥道路。釋義、語境、向量與領域知識各有分工：向量協助召回與提出群組，釋義與書證支持可解釋的判斷，專家處理難例與本體承諾。傳統 synset 的同義性本來就涉及特定義項；限制主要出現在將單一固定義項清單跨越所有時期與傳統使用時。

本計畫暫將 conset 定義為：**在明示文獻與判準下，被提議具有某種共同概念關係的一組義項或用例。** 它不預設跨宗派普遍有效。實際的成員物件至少包含 conset ID、sense／attestation ID、關係判準、文獻範圍、支持證據、反例、審核狀態及版本。不能僅以詞形作成永久成員，也不自動推出 `owl:sameAs`、`skos:exactMatch` 或跨群組的傳遞閉包。

**English.** Glosses and embeddings are complementary. Embeddings support retrieval and candidate grouping; definitions and attestations make judgments interpretable; domain experts assess difficult cases and ontological commitments. A synset already concerns particular senses. The difficulty arises when a fixed inventory is imposed across historical periods and doctrinal traditions.

A conset is provisionally **a set of senses or attestations proposed to share a specified conceptual relation within an explicit evidential scope**. Membership must record its criterion, source context, supporting and opposing evidence, review status, and version. Neither universal synonymy nor automatic transitive closure follows. The PNC implementation uses form labels as a transparent interface shortcut; the research schema requires addressable sense/attestation memberships before large-scale annotation.

**書證例／Textual example.** 《俱舍論》卷四在說「心意識體一」後，又以「集起、思量、了別」分別說明命名理據，並明言「義雖有異而體是一」。本段支持提出局部共同指涉群，亦要求保留義理差異。它並不能證明三詞在任何佛典語境中皆可互換。[CBETA T1558, 0021c18–25](https://cbetaonline.dila.edu.tw/zh/T29n1558?line=0021c18)

**原提案修正／Revision to the initial examples.** 「涅槃、圓寂、滅度、寂滅、入滅」適合作為待檢驗的相關詞群，不宜先宣告同一 conset；必須區分解脫境界、滅除活動、佛陀或僧人的示寂事件，以及文類慣用法。The nirvāṇa-related terms are candidates for investigation, not a prevalidated cluster. State, process, death-event reference, and genre-specific usage may require different senses and relations.

## 5. 關係型別與本體承諾｜Typed relations

| 關係 Relation | 使用條件 Criterion | 初始處理 Initial treatment |
|---|---|---|
| `is_a` | 嚴格的種類—上位類／Taxonomic subtype | 需可辯護的包含判準；不由列舉直接產生／Require a taxonomic criterion |
| `member_of` | 集合成員，如三毒的成員／Set membership | 與種類關係分開／Separate from subtype |
| `part_of` | 結構性構成部分／Constitutive part | 八正道等體系須指定模型與脈絡／State the model and context |
| `classified_under` | 文獻明示的分類／Textual classification | PNC 對八識採此保守關係／Used conservatively in the demo |
| `condition_for` | 文獻所述的緣起條件／Textually asserted conditioning | 保留論述來源與方向，不當成經驗因果模型／Not automatically empirical causality |
| `antidote_for` | 指定修行系統中的對治／Practice-specific antidote | 以哪一傳統、何種條件成立為主張內容／Qualify by tradition and conditions |
| `parallel_corresponds_to` | 指定平行段落中的詞彙對應／Passage-specific lexical correspondence | 不推出直接翻譯依存／No direct source-dependence inference |
| `co_referential_in_context` | 同段明示共同指涉／Explicit contextual co-reference | 保留不同的解釋與使用條件／Preserve explanatory distinctions |
| `related_to` / `specialization_of` | 歷史與現代義項的候選對照／Historical-to-modern sense mapping | 分開審核；不等同於歷史衍生／Not automatically genealogy |

**中文。** 「色法、心法是五蘊／名色的下位詞」混合了不同分類系統；「貪、瞋、癡是三毒的下位詞」也可能混淆成員與種類。七十五法、百法、三十七道品與十二因緣並非同一種類的 DAG：有的是分類，有的是修行項目集合，有的是條件關係。整體研究圖可含循環及相互依賴，只有明確宣告為嚴格分類的子圖才要求無循環。

**English.** The proposed seed systems should not be flattened into one taxonomy. The seventy-five and hundred dharmas organize categories; other enumerations describe practice factors or conditional relations. The integrated graph may contain cycles. Acyclicity is a local requirement for a declared strict taxonomy, not an assumption about Buddhist knowledge as a whole.

## 6. 資料模型與標註單位｜Data model and annotation units

**中文。** 最少保留七類物件：`SourceWitness`、`Passage`、`Attestation`、`LexicalEntry`、`HistoricalSense`、`ConsetMembership`、`Claim`，以及附屬的 `ReviewEvent`。例如一條梵漢對應主張，除主詞、關係與受詞外，必須指出所用文本版本、段落、實際字串、正規化方式、語言與形態分析、作者／譯者歸屬、文本層次、來源日期、主張提出者、審核者及修訂關係。

年代至少區分原作、翻譯、序跋、抄寫／刊刻與現代數位化日期；日期可為區間或未知。宗派、譯者及版本依存本身亦可爭議，應保留歸屬來源與判定者。空值 `null`、未搜尋、未找到及經確認不存在是不同狀態。信心值須分來源、對齊、義項與歷時推論，經校準才報數值。

**English.** The model distinguishes sources, passages, attestations, lexical entries, historical senses, conset memberships, claims, and review events. Claims retain witness identity, locations, literal text, normalization, morphology, attribution, textual layer, source dates, provenance, and revision history. Composition, translation, paratext, witness production, and digitization dates remain separate; intervals and unknown dates are allowed. Attribution and doctrinal classification can themselves be qualified claims. Missing, unsearched, not found, and demonstrably absent must not be collapsed. Confidence dimensions remain separate and numerical scores require calibration.

**交換格式／Interchange.** 採用 RDF 命名圖與 PROV-O 表示來源，參考 OntoLex-Lemon 區分詞彙與概念，以及 SKOS 的概念組織關係。OntoLex-Lemon 的 2016 文件是 W3C Community Group Report，並非 W3C Recommendation；conset 的脈絡性亦不能靠 SKOS 直接補足，仍須將成員主張物件化。[OntoLex-Lemon](https://www.w3.org/2016/05/ontolex/)、[SKOS](https://www.w3.org/TR/skos-reference/)、[PROV-O](https://www.w3.org/TR/prov-o/)

## 7. CWN 的研究角色｜CWN as an empirical anchor

**中文。** CWN 提供三項價值：可重用的原生義項 ID 與釋義、現代漢語的對照基準，以及可辨識涵蓋缺口的義項清單。CWN.dia 將歷史義項另建於擴充層，以 `related_to`、`specialization_of`、`partial_match` 或 `no_inventory_match` 等待審查關係相接。只有在時序及文獻證據足夠時，才提出 predecessor／successor；現代錨點本身不證明歷史來源。

本次已讀取 CWN `v.2022.08.01` 資料影像，精確查詢「心、意、識」，共取得 27 個原生義項，保留同形詞，不更改上游釋義。「識」有四個查得義項（03039001–03039004），未明列五蘊義；故本原型保留缺口候選，不強配同義。「心」的 05231612「人的感情或思想」可作語意相關的待審查錨點。上述判斷僅針對此次查詢與固定快照，不代表最新詞網全部複合詞或全部佛教詞彙的涵蓋情形。[CwnGraph](https://github.com/lopentu/CwnGraph)

**English.** CWN supplies stable native identifiers, contemporary comparison senses, and an explicit inventory against which coverage can be assessed. Historical senses live in a separate extension layer. Mapping and genealogy are distinct tasks.

The current export contains 27 native senses from exact-lemma queries for 心, 意, and 識 in image `v.2022.08.01`, including homographs. The four retrieved senses of 識 do not explicitly encode the skandha sense. This supports a candidate coverage review, not an inference of historical innovation or absence from all CWN compounds. Sense 05231612 supplies a proposed related modern anchor for 心; it is not treated as equivalent or as a demonstrated historical descendant. The image metadata and SHA-256 are retained in the release.

## 8. 語料、跨語對齊與義項標註｜Corpus, alignment, and tagging

**中文。** 三週試作以三至五部文獻中的 100–150 個用例為目標，其中 30–50 個優先尋找可靠平行材料。這是目標，不是現有 gold 數量。樣本按文本、詞形與初步脈絡分層；雙人獨立標註後裁決，並記錄不能確定的用例。正式研究擴至至少兩個有可比材料的時段，但不以任意年代切片冒充歷時設計。

標註順序是定位用例、辨認複合詞邊界與形態、指認局部語境、選擇義項或提出新候選，再決定概念群成員資格。粒度設定可分「一般心理活動」「特定教義功能」「文獻專屬分析」，但必須明示父子或重疊關係，不以單一 slider 自動合併所有義項。context-aware tagger 採檢索候選、上下文排序、允許拒答的開放義項清單，最終產生 SemCor 類型的用例—義項標註資源。

**English.** The three-week pilot targets 100–150 attestations from three to five works, with 30–50 prioritized for reliable parallels. These are planned targets, not existing gold data. Sampling is stratified by text, form, and context; two annotators work independently before adjudication. Unresolved cases remain explicit. Later temporal analysis requires genuinely comparable evidence across periods.

Annotation proceeds from occurrence and morphological boundaries to context, sense assignment or novelty proposal, and contextual conset membership. Coarser and finer senses require explicit hierarchical or overlapping relationships. A context-aware tagger should retrieve and rank inventory candidates while retaining abstention and new-sense proposals. It is a planned component, not a model already evaluated by the PNC release.

**跨語限制／Cross-lingual constraint.** MITRA-E 可作段落檢索候選模型；句／段級檢索成效不等於詞級對齊或同義判定成效。梵文、巴利語、藏文與漢文的形態、複合詞、語序及版本差異須另行處理。多語對應允許部分、非對稱與無對應，不補造未核對的巴利語或藏語對譯。MITRA-E will be benchmarked for candidate retrieval; sentence-level success is not evidence of lexical alignment accuracy. Missing multilingual links remain missing.

## 9. DharmaSwarm：受證據約束的工作流程｜Evidence-gated research workflows

**中文。** 完整工作流程分為 retrieval、alignment、sense proposal、context checking、counterevidence search 及 adjudication preparation 等角色。代理人提交結構化主張，附上查詢、模型版本、prompt、種子、token／工具成本與來源；確定性檢查先擋下不存在的書證、錯誤行號、缺漏欄位、錯置文本層次及不支援的關係型別。語意與文獻學判斷另由獨立評審及專家決定，模型投票不能代替證據。

重試設上限，例如最多兩次修訂，並保留失敗紀錄。找不到支持時可退出或送人工；「反例未找到」須附已搜尋範圍與預算，不能宣告主張為真。不同角色使用同一模型時可能共享錯誤，因此研究必須包含同模型重試、不同模型、無反例搜尋及無驗證等消融條件。

**English.** The proposed roles cover retrieval, alignment, sense proposal, contextual checking, counterevidence search, and preparation for adjudication. Agents submit structured claims with sources and execution metadata. Deterministic gates reject missing evidence, invalid locations, schema violations, contextual mismatches, and unsupported relation types. Semantic judgment remains distinct. Agreement among models is not independent evidence.

Retries are bounded, for example at two revisions, and failed attempts remain available for analysis. The workflow must permit abstention and expert escalation. Unsuccessful counterevidence search records its scope and budget rather than asserting truth. Correlated model errors motivate ablations that distinguish explicit verification from additional inference calls.

**PNC 已完成範圍／Implemented PNC scope.** 已有無模型依賴的來源檢查、逐步紀錄、受控失敗與修復後重新檢查。介面中的重試由使用者還原書證觸發；並非代理自主發現修正。尚未執行 live LLM swarm、語意蘊涵判定或反例搜尋比較實驗。The interface demonstrates real deterministic checks and user-triggered repair. It does not impersonate a running LLM swarm.

## 10. 研究問題與評估｜Research questions and evaluation

**RQ1 — 表示與涵蓋／Representation and coverage.** 固定 synset、現代 CWN 強制配對、脈絡限定 conset 三種設計，在同一用例集的義項可表示性、專家判定正確率、未能對應比例與標註時間上有何差異？Does contextual representation improve usable coverage and expert agreement without merely multiplying senses?

**RQ2 — 可調粒度的標註／Granularity-aware annotation.** 檢索加排序的 tagger 是否在固定 coverage 下改善細粒度 accuracy，以及在固定 accuracy 下減少拒答？Evaluate risk–coverage curves, hierarchical F1, and inventory-gap precision. 不以「全部分到同一群」取得虛假的高一致性；對更細粒度的負擔另報人工時間。

**RQ3 — 條件化語意組織／Conditional semantic organization.** 關係分布在控制文類、譯者、文獻依存與語料量後是否不同？使用匹配文本，並按作品或文本家族重抽樣；如果譯者與年代無法識別，就報「文獻／譯者差異」，不報時代效應。

**RQ4 — 驗證效益／Verification benefit.** 在相同來源存取權與可比較運算預算下，明確驗證與反例搜尋是否改善盲評的主張支持度、引文正確率與修訂後可靠性？Can verification improve claim quality under matched budgets?

| 比較條件 Condition | 檢索 Retrieval | 候選提出 Proposal | 驗證 Verification |
|---|---|---|---|
| B0 | BM25／字元檢索 | 固定詞表／規則 | 相同來源檢查 |
| B1 | 相同候選材料 | 單一 LLM | 基本來源檢查 |
| B2 | 相同候選材料 | 多角色，無反例角色 | 基本來源檢查 |
| B3 | 相同候選材料 | 多角色＋反例搜尋 | 來源、脈絡及獨立判定 |
| B1-budget | 相同材料與 B3 總預算 | 單模型重試／多次抽樣 | 同等檢查，用以分離預算效應 |

**資料分割／Splits.** 以作品／文本家族切分 train、development、test，將重譯本與高度近似的段落放在同一群組，避免平行文本洩漏。人工 gold 對系統條件盲測；分歧以裁決紀錄公開。The partition is by work or textual family, not random passages. Related witnesses remain in the same partition.

**指標／Metrics.**

- **Philological Support Rate:** 經獨立評審確認有書證支持的主張／所有提出主張。另報已接受主張的 precision、召回與 abstention，避免只剩少量保守答案而得高分。The denominator is all proposed claims; accepted-set precision and abstention are reported separately.
- **Citation accuracy:** 位置與引文是否正確；另報引文是否真正支持詮釋，兩者不合併。Location/quotation correctness is separate from evidential entailment.
- **Counterevidence outcome:** 在固定範圍與預算內，維持、縮限、修訂、拒收、未決的比例；存活率只表示未被該次搜尋推翻。Survival under bounded search is not proof of truth.
- **成本與人工負擔:** 每項經裁決支持的主張所耗 token、工具呼叫、秒數及專家分鐘數。Report total rejected attempts and human time as well as accepted outputs.

**歷時分析／Temporal analysis.** 對充分且可比較的樣本，估計 `P(Chinese sense | Indic lemma, context)`，比較條件熵、Jensen–Shannon divergence 與關係更替，並報按文本群組計算的信賴區間與置換檢定。資料量不足的切片不做確定排序。Embedding 空間需固定模型或可驗證的對齊程序。預設的「壓縮→分化→穩定」僅可作待否證假說，不當成預寫結論。

## 11. PNC 原型的實際成果｜What the PNC prototype establishes

| 可報告項目 Reportable item | 已完成 Completed | 不應推論 Does not establish |
|---|---|---|
| 小型主張集合 | 16 條 machine-prepared 主張，來自 6 個書證片段、4 項來源（3 部漢文典籍＋1 份梵文轉寫） | 不是 16 個獨立樣本，也不是專家確認的 gold |
| CWN 匯出 | 27 個原生義項；固定 image tag、metadata、hash | 不代表最新全部 CWN；不代表歷史對應已驗證 |
| 來源檢查 | 16 條通過本機機械檢查；人工接受數為 0 | 不是 100% 語意準確率或 LLM benchmark |
| T0251 文本分層 | 序文 body-role 段落的「心」字 9 次；經文正文 1 次 | 不是詞義比例、獨立樣本或新發現的佛典文本史 |
| 概念群 | 《俱舍論》局部「心意識」群；保存不同命名理據 | 不支持跨宗派全域同義 |
| 互動與交換 | 來源連結、搜尋、文獻篩選、CWN 對照、拒收與重試、JSON／N-Quads | 未完成 live TrustGraph／LLM swarm |

**English.** The release establishes a functioning evidence interface and a reproducible source-validation core. Six evidence windows support sixteen proposals, so claim counts must not be interpreted as independent observations. Every semantic claim remains pending expert review. The T0251 result is a concrete ingestion audit: ignoring paratext can contaminate historical attribution. It is not a newly discovered fact about the sūtra’s history. The conset example and CWN inventory gap are grounded case studies for methodological discussion, not population-level findings.

**資料版本／Versioning.** 漢文 XML 以 cbeta-org/xml-p5 commit `dbdea41071e1e260ad84b72faefd4587333cf76d` 固定，已核對下載內容雜湊。這是 Git 快照，不逕稱 CBETA 2026.R2。梵文網站未提供可用的版本 ID，故記錄 URL、取得日期、原始內容 hash 與解碼方式。CWN 使用 `v.2022.08.01`；原生資料與本計畫的詮釋提案分開。

## 12. 兩天、三週與十二個月｜Immediate and longer-term work

**兩天內／Before PNC.** 當前交付物包括研究網站、候選資料、完整雙語計畫、約十分鐘的英文主講簡報及中英文講稿、離線展示。會前最重要的人工工作是請一位熟悉阿毗達磨或唯識的學者檢視 C001、C003–C008，以及「識」的 CWN 涵蓋缺口判斷；未完成仍維持 pending。另預留一次全程試講與會場裝置確認。

| 階段 Phase | 主要工作 Work | 可核驗交付物 Acceptance evidence |
|---|---|---|
| 第 1 週 Week 1 | 定稿標註指南、抽樣、雙人試標 30 例 | 分歧清單、修訂準則、來源邊界檢查 |
| 第 2 週 Week 2 | 擴至 100–150 例、固定資料分割、建立 B0／B1 | 版本化資料、來源清單、基準輸出與成本紀錄 |
| 第 3 週 Week 3 | B2／B3 小規模比較、盲評與失敗分析 | 可重跑報告；樣本不足時只報描述性結果 |
| 月 1–3 Months 1–3 | 語料與本體、領域合作、資料與授權清單 | 核驗種子集、標註手冊、CiWN schema v1 |
| 月 4–6 Months 4–6 | 可調粒度 tagger、MITRA-E 與 baseline 比較 | 凍結測試集、涵蓋／拒答曲線、版本化模型設定 |
| 月 7–9 Months 7–9 | 有界多代理、反例流程、受控消融 | 主張品質與成本比較、完整失敗紀錄 |
| 月 10–12 Months 10–12 | 有可比證據的歷時分析、整合發布 | 可審核資料版本、研究論文、公開展示及維護文件 |

**人力與經費假設／Resourcing assumptions.** 建議至少一名語言學／NLP 研究助理、一名工程或資料助理、兩位兼任領域標註者與一位裁決者；角色可由少數人兼任，但獨立盲評不可由產生答案者自行完成。運算先以檢索與小量推論為主，是否訓練或領域微調須由 baseline 結果決定。正式經費依人月、標註量、模型部署與主機需求編列，本稿不虛列已獲補助或硬體資源。

## 13. 網站與程式庫配置｜Website and repository plan

**中文。** 採 [SinDia 佛教語意專區](https://lopentu.github.io/sindia-site/buddhist/) 作研究入口，沿用現有網站的中英導覽；先以獨立靜態專區承載書證探索、架構與發表材料，便於現場展示與維護。`loperntu/tbsg-cwn` 保存研究模型、匯入與驗證程式、資料版本及文件；`lopentu/sindia-site` 保存網站及固定的展示資料副本，更新時必須由同一版本同步產生。HCC 保留為未來語料服務的對接端。

本次可存取並核對的是以上兩個 repo。使用者提供的 `lopentu/sindia` 與 `lopentu/historical-chinese-corpus` 在本次連線中回傳 404，不能據此判定不存在或已刪除；HCC 尚未取得可編輯的後端程式與部署設定。因此本階段選擇可核驗且可部署的 SinDia 路徑。

**English.** The Buddhist Semantics section under SinDia provides the research entry point. The research repository owns schemas, importers, validators, versioned data, and methodology; the website repository carries a release-matched demonstration snapshot. HCC remains a potential corpus-service integration. The two other supplied repositories were unavailable through the current connection, so their implementation and deployment state have not been inferred.

**持續更新／Maintenance.** 每一公開版本記錄來源快照、schema、候選提出方式與審核狀態；既有 claim ID 保持穩定，以新版本與 supersedes 關係記錄修訂。不得將示範 CSV 併入真實語料的統計，也不得將失敗後消失的主張從成本分母中移除。

## 14. 預期影響與合作邀請｜Expected impact and collaboration

**中文。** 本計畫希望建立一種能讓語言學者、佛學研究者與 AI 系統共同工作的語意資源：研究者可以從概念關係返回具體文獻，指出反例，修訂義項，並清楚看見哪些內容仍未確定。可共享的成果包括佛典歷史義項資源、語意標註語料、跨語對應主張、方法評估及研究介面。

在 PNC 最合適的合作邀請是尋求三種具體貢獻：協助挑選可比文本、共同審核義項與關係、提供可否證的佛教語意史問題。計畫的長期價值，在於把學術分歧與證據界線納入資源本身，使它能持續修訂而不失其所本。

**English.** CiWN aims to support shared work among linguists, Buddhist scholars, and AI systems. Researchers should be able to inspect a relation, recover its evidence, submit counterexamples, revise an interpretation, and identify unresolved questions. Reusable outcomes include historical senses, a sense-tagged corpus, qualified cross-lingual claims, evaluation protocols, and a scholarly interface. The immediate collaboration request is concrete: comparable texts, expert sense and relation review, and falsifiable questions about Buddhist semantic history.

## 15. 主要參考資源｜Selected references

1. Nehrdich, S., & Keutzer, K. (2026). *MITRA: A Large-Scale Parallel Corpus and Multilingual Pretrained Language Model for Machine Translation and Semantic Retrieval for Pāli, Sanskrit, Buddhist Chinese, and Tibetan.* [arXiv:2601.06400](https://arxiv.org/abs/2601.06400).
2. Hellwig, O., & Biagetti, E. (2025). *The Sanskrit Sembank.* Language Resources and Evaluation. [DOI](https://doi.org/10.1007/s10579-025-09852-1).
3. CBETA. [XML TEI P5 repository](https://github.com/cbeta-org/xml-p5), [line identifiers](https://cbeta.org/line-head-info), [source terms](https://cbeta.org/copyright).
4. Chinese WordNet / CwnGraph. [Repository and loader](https://github.com/lopentu/CwnGraph), [public manifest](https://raw.githubusercontent.com/lopentu/CwnGraph/develop/etc/manifest.json).
5. [CBETA T0251](https://cbetaonline.dila.edu.tw/zh/T08n0251), [CBETA T1558](https://cbetaonline.dila.edu.tw/zh/T29n1558), [CBETA T1614](https://cbetaonline.dila.edu.tw/zh/T31n1614).
6. NTU Buddhist Digital Library. [Sanskrit Prajñāpāramitāhṛdaya transcription](https://buddhism.lib.ntu.edu.tw/FULLTEXT/mukherjee/articles/html/sk-heart.htm).
7. Cimiano, P., McCrae, J. P., & Buitelaar, P. (Eds.). (2016). [Lexicon Model for Ontologies: Community Report](https://www.w3.org/2016/05/ontolex/).
8. W3C. [SKOS Reference](https://www.w3.org/TR/skos-reference/); [PROV-O](https://www.w3.org/TR/prov-o/).
9. TrustGraph. [Official project](https://github.com/trustgraph-ai/trustgraph), [2.6 release](https://trustgraph.ai/news/release-2-6).

**Source note.** 計畫依提供的 Project Proposal.md、其中的分享對話，以及既有 tbsg-cwn 提案與實作重新整合；先前對話中的數字、架構宣稱與示範結果均未自動視為已驗證的研究成果。Resources were checked on 7 September 2026; externally published capabilities remain separate from this project’s implementation status.
