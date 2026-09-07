# PNC 發表講稿與展示指南｜CiWN talk and demonstration guide

**版本：2026-09-07；主講約十分鐘，12 張主投影片，另附 2 張問答備用投影片。**

目前未取得會議的正式發表長度，故以十分鐘英文主講準備；十五分鐘場次可增加現場展示與討論，八分鐘場次可合併第 4、5 張及略過第 11 張細節。

**主旨句：** Every semantic claim should retain its evidence, context, and revision history.

**網站：** [SinDia Buddhist Semantics](https://lopentu.github.io/sindia-site/buddhist/)

## 會前兩天的優先順序

今天：核對姓名、題目與實際發表長度；請領域學者先檢視 C001 與《俱舍論》conset 判斷。未審核前保持 pending，無須為上台而改成已驗證。

明天：完整試講一次；在發表電腦開啟簡報及離線示範；確認中文字、梵文附加符號、投影比例。預備主網站、離線示範與投影片三種展示方式。

當天：先開好網站 C001，瀏覽器縮放 100%；若網路不穩，改用離線示範。外部書證連結需網路，內部資料檢視與檢查可離線執行。

## 英文主講與中文提示

### 01. CiWN: Contextual Buddhist Semantics

Today I would like to propose CiWN, a contextual semantic resource for Buddhist research. The starting point is a simple commitment: when a system proposes a semantic relation, a scholar should be able to recover the passage, inspect the interpretation, and revise the claim. We already have remarkable digital canons, dictionaries, and retrieval tools. Our question is how to build on them while preserving the differences that matter in philology. I will introduce the representation and show a small working prototype.

**中文提示。** 今天提出的是能保存脈絡、可回溯且可修訂的佛教語意資源。先肯定既有數位化、詞典與檢索成果，再指出新增的研究問題。這是初步方法與實作展示，不是完整語意史結論。

### 02. 心・意・識 need more than one label

Consider this passage from the Abhidharmakośabhāṣya. It states that mind, mentation, and consciousness are one in substance, yet it explains the three names differently: accumulation, mentation, and discrimination. This creates a useful representational problem. A resource should preserve the passage’s claim about common reference without erasing its explanatory distinctions. Nor should it turn this local claim into unrestricted synonymy across Buddhist traditions. The text gives us both a connection and its limits.

**中文提示。** 《俱舍論》同段有「體一」與「義異」。這不是宣布心、意、識普遍同義；而是展示同一書證如何支持局部連結，又約束其適用範圍。集起等英文只是工作性譯述，不作定譯。

### 03. A conset needs an explicit context

We provisionally call this a context-bounded conset. The crucial move is to treat membership as a claim with an explicit criterion and evidential scope. Embeddings can help discover candidate groups, but similarity does not establish synonymy. Glosses, context, and expert judgment remain necessary. In the full schema, membership links senses or attestations; the prototype uses readable form labels as an interface shortcut. The term conset itself is not our novelty claim. What matters is whether the representation improves scholarly annotation and review.

**中文提示。** conset 暫譯「脈絡限定的概念群」。向量是召回工具，不能取代釋義或文本論證；正式成員連結義項與用例。PNC 原型仍以詞形標籤呈現，需如實交代。

### 04. Five roles, one research programme

The programme brings five components together. CiWN organizes the lexical-conceptual resource. CWN.dia relates historical senses to native Chinese WordNet anchors, while keeping historical descent separate from semantic similarity. TBSG defines the temporal analysis. DharmaSwarm is the research workflow, including counterevidence and revision. TrustGraph is a replaceable infrastructure candidate. The research definitions should survive a change of backend. At present, we export claims and provenance, but have not completed a live TrustGraph integration.

**中文提示。** 強調研究方法與底層工具分離。CWN.dia 的語意對照不自動構成譜系；TrustGraph 目前是候選基礎設施，不應說已完成整合。

### 05. A claim carries its evidence

Our basic unit is a qualified scholarly claim. For a Chinese–Sanskrit correspondence, we preserve the two attestations separately from the alignment and the sense interpretation. Checking that the words occur in their sources is a mechanical task. Deciding what the correspondence means is a philological task. The current data therefore distinguish source checks, interpretation, inventory mapping, counterevidence search, and human review. A single confidence score would conceal these differences. We leave uncalibrated scores empty.

**中文提示。** 這張表就是核心資料模型的直觀版本。機械檢查通過，不等於語意判定成立；各層保留狀態，不以漂亮的 .98 代替校準與專家審核。

### 06. A real parallel, with a clear limit

The first correspondence uses the Heart Sūtra. The Chinese and Sanskrit passages place 識 and vijñāna in corresponding positions in the list of aggregates. This supports a passage-level correspondence proposal. It does not establish that this surviving Sanskrit transcription was the direct source of the Chinese text traditionally attributed to Xuanzang. That distinction is particularly important for the Heart Sūtra’s complex textual history. The interface makes the distinction visible rather than burying it in a footnote.

**中文提示。** 保留既有 vertical slice，但不把 ParallelCorrespondenceClaim 改成直接 translatedAs。現在引文與原始行號已重新核對；梵文見證為臺大網站轉寫，非已識別的玄奘翻譯底本。

### 07. CWN makes an inventory gap visible

We have now connected native CWN data. Exact queries for 心, 意, and 識 return twenty-seven senses, including homographs, from a pinned data image. These four are the retrieved senses of 識. None explicitly encodes the skandha sense. Our response is to preserve a candidate inventory gap rather than force the Buddhist usage into a convenient modern sense. This is a judgment about these queried entries, not a claim that all current CWN data lack Buddhist vocabulary. A coverage gap is also not proof of historical innovation.

**中文提示。** 原生詞網的價值之一，是讓「未能對應」成為可審查資料。限定此次 image 與 exact lemma 的四義，不擴張成整體 CWN 的涵蓋宣稱。識蘊等複合詞尚未在此次 exact query 中評估。

### 08. One file, several textual layers

A second concrete result comes from the importer. The T0251 XML contains prefaces as well as the sūtra body. One preface is explicitly headed as an imperial text of the Ming founder. When we count the character 心 in body-role text, excluding headings, bylines, and notes, we obtain nine occurrences in the prefaces and one in the sūtra. These are character counts, not sense counts. The lesson is methodological: if every passage inherits the work’s translator and period, an ingestion error can appear to be semantic change. We now retain section boundaries.

**中文提示。** 這是工程與方法稽核結果，不是首次發現《心經》有序文。9 與 1 都是 body-role 的字元計數，排除標題、署名、校注；不得當成詞義比例或獨立樣本。

### 09. Rejection belongs in the workflow

Let me show the working interface. I select the Heart Sūtra claim, inspect its sources, and run the checks. It becomes eligible for review, not accepted as gold. I then replace an evidence identifier with a missing one. The check rejects this version. Restoring the evidence allows another check, and the claim returns to the review queue. This is a controlled demonstration of the deterministic core. It is not a running multi-agent experiment. The next stage adds generation and counterevidence search, with bounded retries and independent evaluation.

**中文提示。** 現場操作約 60 秒：開 C001→執行來源檢查→測試缺失書證→還原書證並重新檢查。清楚說明「由使用者還原」而非代理自主找出答案；不把示範拒收當成大規模模型成效。

### 10. A small, inspectable prototype

The present release contains sixteen proposed claims grounded in six evidence windows from three Chinese works and one Sanskrit transcription. It also includes twenty-seven native CWN senses, source checks, a bilingual interface, and structured exports. None of the semantic claims has yet been accepted by an independent domain expert. The sixteen claims are not sixteen independent observations, since several share passages. We do not claim a temporal effect, a trained sense tagger, or a quality improvement from multiple agents. This transparent boundary is part of the design.

**中文提示。** 16 條主張來自 6 個片段，不是 n=16 的獨立實驗。來源檢查全部通過也不是模型語意正確率100%。這頁建議一定保留，避免問答時失去信任。

### 11. Evaluate verification, not agent count

The evaluation must ask whether verification helps, rather than whether more agents can produce more text. We will compare lexical baselines, one model, multiple roles without counterevidence, and the full verification workflow. A budget-matched single-model retry condition controls for additional inference. Experts will assess support, citation entailment, abstention, and cost per supported claim. Data splits will be by work or textual family, keeping closely related witnesses together. If translator and period cannot be separated, the result will be reported as a textual or translator difference, not as an effect of time.

**中文提示。** 研究貢獻應落在可比較預算下的品質提升。保留拒答率與成本，避免只接受少量簡單主張取得高 precision。切分以作品／文本家族為單位，不能把平行或重譯段落隨機分進 train 和 test。

### 12. Build a resource scholars can revise

Our aim is a resource that scholars can revise. A useful semantic graph should preserve not only what is asserted, but where it applies, why it is supported, and what remains unsettled. We welcome three kinds of collaboration: comparable textual materials, expert review of senses and relations, and historical questions that the evidence could genuinely challenge. The prototype is deliberately small. Its purpose is to make the research commitments inspectable and to provide a foundation that can grow through careful, shared work.

**中文提示。** 結尾把合作邀請落實為三件事：可比文本、專家審核、可否證問題。對既有佛教數位資源保持互補的定位。現在的小規模是為了把方法站穩，不宣稱已涵蓋大藏經。

### 13. Appendix / Do not flatten relations

The proposal’s seed systems require typed relations. An enumeration is not automatically a taxonomy, and a conditional relation should not be silently treated as an empirical causal estimate. The PNC data conservatively encode the eight consciousnesses as classified under 心法 within the Hundred Dharmas text. Further commitments require domain review.

**中文提示。** 答覆本體問題時使用。修正原附件把不同名相綱領一律當 DAG 分類樹的說法。保持 classified_under 的保守標記。

### 14. Appendix / A staged research plan

The immediate pilot targets one hundred to one hundred and fifty attestations, with dual annotation and adjudication. These are targets, not completed outputs. The twelve-month plan proceeds through data foundations, tagging and retrieval, controlled agent evaluation, and temporal analysis only where comparable evidence is available. Staffing and compute should follow these stages rather than the ambition to launch hundreds of agents at once.

**中文提示。** 規模皆是工作目標；正式研究需要人力承諾與經費，不在此虛列既有資源。優先三週落實少量可靠標註，不承諾兩天完成百筆專家 gold。

## 60–90 秒展示流程

1. 開啟「主張與書證」，選 C001「識與 vijñāna 的平行位置」。指出中文原文、梵文轉寫與來源行號；不要說此梵本就是玄奘底本。
2. 往下看 CWN.dia 缺口候選。四個「識」原生義項保留，但沒有強制選出一個等價義項。
3. 按「執行來源檢查」。說明通過後的狀態是「進入人工審核佇列」，不是 accepted。
4. 按「測試缺失書證」，看到拒收；按「還原書證並重新檢查」，看到回到待審核狀態。說明這是受控測試與使用者觸發的修復，不是自主 LLM swarm。
5. 如有時間，切到「同一檔案的不同時代」，展示 T0251 序文與正文的 9／1 字元計數；再切回主張列表選 C006，說明「義異而體一」。

## 問答準備｜Discussion notes

### Q1. 這與既有佛教知識圖譜有何不同？

**中文。** 我們沿用既有數位化與知識組織成果，新增的研究焦點是脈絡限定的義項與成員資格，以及可回溯、可拒收、可修訂的主張。不是宣稱既有知識圖譜只能靜態，亦不主張第一個佛教 AI 系統。

**English.** We build on existing resources and focus on a specific representational and evaluative problem: contextual sense membership and independently reviewable claims. We do not assume that existing knowledge graphs are necessarily static.

### Q2. conset 是不是只是把 synset 換個名字？

**中文。** 若只換名稱，沒有貢獻。此處把成員資格物件化，指定關係判準、書證與適用範圍，允許部分重疊、不同解釋及修訂。這些差異是否實際改善標註與檢索，是待實驗回答的問題。

**English.** Renaming a synset would not be a contribution. Our proposal reifies membership and records its criterion, evidence, and scope. Whether that helps annotation and retrieval must be tested.

### Q3. 為什麼還需要 CWN，而不是完全由 LLM 建構？

**中文。** 原生義項提供穩定可追蹤的對照，不必每次重新發明識別碼；未能對應也能保留下來。CWN 是比較錨點與涵蓋基準，不是古代佛典必須服從的完整義項清單。

**English.** CWN gives us stable identifiers and an explicit comparison inventory. Historical usages may match partially or remain unmatched. It is an anchor, not a compulsory destination.

### Q4. 你們已經找到語意變遷了嗎？

**中文。** 尚未。當前是來源校驗與表示原型；同一時期不同文本的差異不能直接叫歷時變遷。下一步須有可比時段、文本家族控制與獨立標註。

**English.** Not yet. The current release demonstrates representation and source checking. Temporal claims require comparable samples, textual-family controls, and independent annotation.

### Q5. 多代理真的比較可靠嗎？

**中文。** 目前未證明。來源檢查與受控重試已執行；多代理的可靠性需以相同材料、相近總預算與專家盲評比較。多個模型一起犯錯，不會因此成為多份獨立證據。

**English.** That remains an empirical question. We need matched budgets and independent adjudication. Multiple agents agreeing on an error do not create independent evidence.

### Q6. 16 條全部通過，是不是準確率 100%？

**中文。** 不是。那是存在性、字串與結構的檢查通過數，且多條主張共用同一片段。語意支持度尚未人工裁決，人工接受數目前為零。

**English.** No. It is a count of passed mechanical checks, not semantic accuracy. Several claims share evidence, and none has yet been independently accepted as gold.

### Q7. 為什麼使用《心經》，其文本史不是有爭議嗎？

**中文。** 正因如此，展示必須區分平行對應、傳統譯者歸屬與直接底本依存。本例只對第一項提出局部主張，並不解決整部《心經》的生成史。

**English.** That is why the model separates parallel correspondence, traditional attribution, and direct source dependence. This example makes only the first, local claim.

### Q8. MITRA-E 與 TrustGraph 已經接上了嗎？

**中文。** 都是已核對的外部候選資源，尚未完成本計畫的 live 整合與成效評估。當前資料與檢查不依賴它們，可先獨立重跑；正式整合將固定版本並驗證。

**English.** They are external candidates, not completed integrations. The present data and checks can be reproduced independently. Integration requires pinned versions and explicit validation.

### Q9. 序文的 9 次「心」與正文的 1 次有何意義？

**中文。** 它證明在這個固定檔案快照中，字元大多出現在序文的 body-role 段落；若整檔套用玄奘與唐代標籤，就可能錯置來源。這是資料流程的實例，不是新發現序文，也不是語意分布的統計推論。

**English.** It demonstrates a concrete provenance hazard in this snapshot. The result is an ingestion audit, not a novel textual-historical discovery or a distributional semantic finding.

### Q10. 需要何種合作？

**中文。** 優先需要可比較的文本與版本資訊、兩位領域標註者及裁決者，以及能由材料支持或反駁的研究問題。先讓百餘筆用例站得住腳，再談整部大藏經。

**English.** We need comparable texts, domain annotation and adjudication, and questions that the evidence can challenge. A defensible seed set comes before large-scale expansion.

## 建議避免的說法

避免「我們證明玄奘使某詞穩定化」「目前有 16 筆 gold」「300 agents 已在運作」「MITRA-E 已完成微調」「conset 自動等同於佛教概念」「現代 CWN 是古代義項的終點」。改說已完成可稽核原型，正在檢驗表示與驗證方法。

## 可直接使用的 150-word English abstract

CiWN proposes a contextual semantic resource for Buddhist research, linking lexical senses, textual evidence, and revisable scholarly claims. Building on Chinese WordNet and digitized Buddhist canons, the project investigates how conceptual groupings can preserve distinctions across texts, traditions, and historical periods. Its initial case examines 心, 意, and 識 through Chinese passages and Sanskrit parallels. A working prototype connects sixteen proposed claims to six evidence windows and exports twenty-seven native Chinese WordNet senses. It separates mechanical source checks from semantic interpretation and expert adjudication, and demonstrates rejection and repair when evidence references fail. A corpus-ingestion audit also shows why prefaces and sūtra bodies require distinct contextual metadata. These results establish an inspectable research workflow, while historical change and multi-agent reliability remain open questions. The next phase evaluates contextual sense annotation and evidence-guided verification under matched computational budgets, with independent scholarly review and explicit treatment of uncertainty, abstention, and textual dependence.

## 引用與資料

經文、CWN 與外部方法的來源均列於簡報備註及[完整雙語計畫](ciwn_proposal_bilingual.md)。資料版本、原始檔 hash、可重跑指令與限制見 [PNC release notes](pnc_release.md)。
