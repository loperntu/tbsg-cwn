// Requires the Codex artifact-tool runtime and Noto Sans CJK TC for rendering.
import fs from 'node:fs/promises';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
const OUT=process.env.CIWN_SLIDES_OUT || 'output/pnc';
const TMP=process.env.CIWN_SLIDES_TMP || 'output/pnc/renders';
await fs.mkdir(OUT,{recursive:true});await fs.mkdir(TMP,{recursive:true});
const deck=Presentation.create({slideSize:{width:1280,height:720}});
const C={ink:'#142339',blue:'#244CA0',gray:'#56647A',line:'#CED8E8',pale:'#EEF3FB',white:'#FFFFFF',amber:'#795316'};
const notes=[];const layoutLog=[];
function box(s,x,y,w,h,fill=C.pale){return s.shapes.add({geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:'none',width:0}});}
function txt(s,t,x,y,w,h,size=28,color=C.ink,bold=false){const sh=s.shapes.add({geometry:'textbox',name:t.slice(0,45),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});sh.text=t;sh.text.style={fontSize:size,typeface:'Noto Sans CJK TC',color,bold,verticalAlignment:'top',wrap:'square',autoFit:'none',insets:{top:0,right:0,bottom:0,left:0}};layoutLog.push({slide:deck.slides.items.length,text:t,x,y,w,h,size});return sh;}
function slide(title,sub=''){const s=deck.slides.add();s.background.fill=C.white;txt(s,title,64,45,1152,78,48,C.ink,true);if(sub)txt(s,sub,64,127,1152,60,32,C.gray);txt(s,'CiWN / SinDia · PNC 2026',64,669,1080,25,16,C.gray);txt(s,String(deck.slides.items.length).padStart(2,'0'),1160,667,56,28,18,C.gray);return s;}
function note(s,title,en,zh,sources=[]){s.speakerNotes.textFrame.setText(`ENGLISH\n${en}\n\n中文備註\n${zh}\n\n[Sources]\n${sources.join('\n')}\n[/Sources]`);notes.push({slide:deck.slides.items.length,title,en,zh,sources});}
function table(s,heads,rows,x=64,y=215,widths=[330,500,322],rowH=64){const W=widths.reduce((a,b)=>a+b,0);box(s,x,y,W,rowH,C.pale);let xx=x;heads.forEach((h,i)=>{txt(s,h,xx+14,y+12,widths[i]-28,rowH-15,23,C.ink,true);xx+=widths[i];});rows.forEach((r,j)=>{const yy=y+rowH*(j+1);box(s,x,yy+rowH-1,W,1,C.line);let xxx=x;r.forEach((v,i)=>{txt(s,v,xxx+14,yy+11,widths[i]-28,rowH-14,23,C.ink);xxx+=widths[i];});});}
function two(s,leftTitle,left,rightTitle,right){txt(s,leftTitle,64,218,540,64,34,C.ink,true);txt(s,left,64,301,530,292,29);txt(s,rightTitle,676,218,540,64,34,C.ink,true);txt(s,right,676,301,530,292,29);}
const src={kosa:'https://cbetaonline.dila.edu.tw/zh/T29n1558?line=0021c18',heart:'https://cbetaonline.dila.edu.tw/zh/T08n0251',sa:'https://buddhism.lib.ntu.edu.tw/FULLTEXT/mukherjee/articles/html/sk-heart.htm',cwn:'https://github.com/lopentu/CwnGraph',hundred:'https://cbetaonline.dila.edu.tw/zh/T31n1614?line=0855b20',data:'https://github.com/loperntu/tbsg-cwn/tree/main/data/pnc2026',mitra:'https://arxiv.org/abs/2601.06400',ssb:'https://doi.org/10.1007/s10579-025-09852-1'};
{
 const s=deck.slides.add();s.background.fill=C.white;txt(s,'SINOGRAPHIA DIACHRONICA / PNC 2026',64,55,1130,45,25,C.blue,true);txt(s,'CiWN: Contextual\nBuddhist Semantics',64,218,1145,215,72,C.ink,true);txt(s,'A resource of revisable, evidence-grounded claims',64,470,1145,56,32,C.gray);txt(s,'謝舒凱 Shu-Kai Hsieh\nNational Taiwan University',64,578,1130,76,25);note(s,'CiWN: Contextual Buddhist Semantics','Today I would like to propose CiWN, a contextual semantic resource for Buddhist research. The starting point is a simple commitment: when a system proposes a semantic relation, a scholar should be able to recover the passage, inspect the interpretation, and revise the claim. We already have remarkable digital canons, dictionaries, and retrieval tools. Our question is how to build on them while preserving the differences that matter in philology. I will introduce the representation and show a small working prototype.','今天提出的是能保存脈絡、可回溯且可修訂的佛教語意資源。先肯定既有數位化、詞典與檢索成果，再指出新增的研究問題。這是初步方法與實作展示，不是完整語意史結論。',[src.mitra,src.ssb,src.data]);
}
{
 const s=slide('心・意・識 need more than one label','共同指涉與命名理據，可以同時存在。');
 txt(s,'心意識體一',64,231,1120,85,57,C.blue,true);txt(s,'集起故名心，思量故名意，了別故名識。',64,353,1120,80,37);txt(s,'One referent in this passage; different explanations of the names.',64,488,1120,94,31);txt(s,'《阿毘達磨俱舍論》卷四 · T1558, 0021c18–25',64,609,1130,34,21,C.gray);
 note(s,'心・意・識 need more than one label','Consider this passage from the Abhidharmakośabhāṣya. It states that mind, mentation, and consciousness are one in substance, yet it explains the three names differently: accumulation, mentation, and discrimination. This creates a useful representational problem. A resource should preserve the passage’s claim about common reference without erasing its explanatory distinctions. Nor should it turn this local claim into unrestricted synonymy across Buddhist traditions. The text gives us both a connection and its limits.','《俱舍論》同段有「體一」與「義異」。這不是宣布心、意、識普遍同義；而是展示同一書證如何支持局部連結，又約束其適用範圍。集起等英文只是工作性譯述，不作定譯。',[src.kosa]);
}
{
 const s=slide('A conset needs an explicit context','概念群的成員資格，本身也是待審核的主張。');
 two(s,'Candidate grouping','心 · 意 · 識\n\nCriterion: contextual co-reference\nScope: one Kośa passage\nMembership: revisable','Preserved distinctions','Different naming explanations\n\nNo universal synonymy\nNo automatic sameAs\nNo unqualified transitivity');
 note(s,'A conset needs an explicit context','We provisionally call this a context-bounded conset. The crucial move is to treat membership as a claim with an explicit criterion and evidential scope. Embeddings can help discover candidate groups, but similarity does not establish synonymy. Glosses, context, and expert judgment remain necessary. In the full schema, membership links senses or attestations; the prototype uses readable form labels as an interface shortcut. The term conset itself is not our novelty claim. What matters is whether the representation improves scholarly annotation and review.','conset 暫譯「脈絡限定的概念群」。向量是召回工具，不能取代釋義或文本論證；正式成員連結義項與用例。PNC 原型仍以詞形標籤呈現，需如實交代。',[src.kosa,src.data]);
}
{
 const s=slide('Five roles, one research programme','保留既有名稱，讓各模組各司其職。');
 table(s,['Component','Responsibility'],[['CiWN','Contextual lexical-conceptual resource'],['CWN.dia','Native anchors and qualified sense mappings'],['TBSG','Temporal and contextual relational analysis'],['DharmaSwarm','Proposal, checking, counterevidence, revision'],['TrustGraph','Replaceable infrastructure candidate']],64,204,[270,882],68);
 note(s,'Five roles, one research programme','The programme brings five components together. CiWN organizes the lexical-conceptual resource. CWN.dia relates historical senses to native Chinese WordNet anchors, while keeping historical descent separate from semantic similarity. TBSG defines the temporal analysis. DharmaSwarm is the research workflow, including counterevidence and revision. TrustGraph is a replaceable infrastructure candidate. The research definitions should survive a change of backend. At present, we export claims and provenance, but have not completed a live TrustGraph integration.','強調研究方法與底層工具分離。CWN.dia 的語意對照不自動構成譜系；TrustGraph 目前是候選基礎設施，不應說已完成整合。',[src.data,'https://trustgraph.ai/news/release-2-6']);
}
{
 const s=slide('A claim carries its evidence','原文、主張、詮釋與審核分開保存。');
 table(s,['Object','Example','Status'],[['Chinese attestation','T0251 · 識','Source checked'],['Sanskrit parallel','vijñānāni','Source checked'],['Correspondence claim','vijñāna ↔ 識','Proposed'],['Historical sense','Consciousness as a skandha','Review pending'],['Modern CWN mapping','Candidate inventory gap','Review pending']],64,204,[315,527,310],68);
 note(s,'A claim carries its evidence','Our basic unit is a qualified scholarly claim. For a Chinese–Sanskrit correspondence, we preserve the two attestations separately from the alignment and the sense interpretation. Checking that the words occur in their sources is a mechanical task. Deciding what the correspondence means is a philological task. The current data therefore distinguish source checks, interpretation, inventory mapping, counterevidence search, and human review. A single confidence score would conceal these differences. We leave uncalibrated scores empty.','這張表就是核心資料模型的直觀版本。機械檢查通過，不等於語意判定成立；各層保留狀態，不以漂亮的 .98 代替校準與專家審核。',[src.heart,src.sa,src.data]);
}
{
 const s=slide('A real parallel, with a clear limit','平行位置可以支持對應，不能單獨證明翻譯底本。');
 txt(s,'受、想、行、識，亦復如是。',64,224,1130,80,44,C.blue,true);txt(s,'evam eva vedanā-saṃjñā-saṃskāra-vijñānāni',64,344,1130,90,32);txt(s,'Passage-level correspondence\nDirect dependence on this extant witness remains unestablished.',64,490,1130,115,31);
 note(s,'A real parallel, with a clear limit','The first correspondence uses the Heart Sūtra. The Chinese and Sanskrit passages place 識 and vijñāna in corresponding positions in the list of aggregates. This supports a passage-level correspondence proposal. It does not establish that this surviving Sanskrit transcription was the direct source of the Chinese text traditionally attributed to Xuanzang. That distinction is particularly important for the Heart Sūtra’s complex textual history. The interface makes the distinction visible rather than burying it in a footnote.','保留既有 vertical slice，但不把 ParallelCorrespondenceClaim 改成直接 translatedAs。現在引文與原始行號已重新核對；梵文見證為臺大網站轉寫，非已識別的玄奘翻譯底本。',[src.heart+'?line=0848c08',src.sa]);
}
{
 const s=slide('CWN makes an inventory gap visible','固定快照：v.2022.08.01 · 精確查詢「識」');
 table(s,['Native sense ID','Original CWN gloss'],[['03039001','學習過而懂得，多指學術知識方面。'],['03039002','認識、熟悉。'],['03039003','能分辨並發掘人才。'],['03039004','見解、見聞。']],64,209,[310,842],69);
 txt(s,'No explicit skandha sense in these four entries.\nRetain a candidate gap; do not force equivalence.',64,583,1130,67,25,C.blue,true);
 note(s,'CWN makes an inventory gap visible','We have now connected native CWN data. Exact queries for 心, 意, and 識 return twenty-seven senses, including homographs, from a pinned data image. These four are the retrieved senses of 識. None explicitly encodes the skandha sense. Our response is to preserve a candidate inventory gap rather than force the Buddhist usage into a convenient modern sense. This is a judgment about these queried entries, not a claim that all current CWN data lack Buddhist vocabulary. A coverage gap is also not proof of historical innovation.','原生詞網的價值之一，是讓「未能對應」成為可審查資料。限定此次 image 與 exact lemma 的四義，不擴張成整體 CWN 的涵蓋宣稱。識蘊等複合詞尚未在此次 exact query 中評估。',[src.cwn,src.data]);
}
{
 const s=slide('One file, several textual layers','T0251 的序文與經文不能共用同一個譯者／年代標籤。');
 table(s,['Layer in the XML','Literal 心 count'],[['Body text of two prefaces','9'],['Sūtra body','1']],64,216,[850,302],85);
 txt(s,'One preface names the Ming founder in its heading.\nDocument-level metadata can contaminate temporal analysis.',64,504,1130,108,30);
 note(s,'One file, several textual layers','A second concrete result comes from the importer. The T0251 XML contains prefaces as well as the sūtra body. One preface is explicitly headed as an imperial text of the Ming founder. When we count the character 心 in body-role text, excluding headings, bylines, and notes, we obtain nine occurrences in the prefaces and one in the sūtra. These are character counts, not sense counts. The lesson is methodological: if every passage inherits the work’s translator and period, an ingestion error can appear to be semantic change. We now retain section boundaries.','這是工程與方法稽核結果，不是首次發現《心經》有序文。9 與 1 都是 body-role 的字元計數，排除標題、署名、校注；不得當成詞義比例或獨立樣本。',[src.heart,src.data]);
}
{
 const s=slide('Rejection belongs in the workflow','可操作的驗證核心：缺失書證 → 拒收 → 修復後重查');
 const cols=[64,464,864];const items=[['01 / Propose','16 source-backed\nclaim candidates'],['02 / Check','Missing evidence\ntriggers rejection'],['03 / Revise','Restore the citation;\nreturn to review']];
 items.forEach((a,i)=>{txt(s,a[0],cols[i],257,350,50,29,C.blue,true);txt(s,a[1],cols[i],355,350,126,31);});
 txt(s,'Implemented: deterministic source checks and controlled retry.\nPlanned: live LLM roles, counterevidence search, independent evaluation.',64,552,1150,94,26,C.gray);
 note(s,'Rejection belongs in the workflow','Let me show the working interface. I select the Heart Sūtra claim, inspect its sources, and run the checks. It becomes eligible for review, not accepted as gold. I then replace an evidence identifier with a missing one. The check rejects this version. Restoring the evidence allows another check, and the claim returns to the review queue. This is a controlled demonstration of the deterministic core. It is not a running multi-agent experiment. The next stage adds generation and counterevidence search, with bounded retries and independent evaluation.','現場操作約 60 秒：開 C001→執行來源檢查→測試缺失書證→還原書證並重新檢查。清楚說明「由使用者還原」而非代理自主找出答案；不把示範拒收當成大規模模型成效。',[src.data,'https://lopentu.github.io/sindia-site/buddhist/']);
}
{
 const s=slide('A small, inspectable prototype','成果邊界清楚，才有可累積的研究基礎。');
 table(s,['Completed','Still open'],[['16 proposed claims / 6 evidence windows','Expert adjudication: 0 accepted claims'],['27 native CWN senses','Historical mappings and sense tagging'],['Source checks, rejection, controlled retry','LLM swarm and counterevidence evaluation'],['JSON, N-Quads, bilingual website','Live graph-backend integration']],64,214,[606,546],83);
 txt(s,'No validated temporal effect or model-quality gain is claimed.',64,638,1150,30,22,C.blue,true);
 note(s,'A small, inspectable prototype','The present release contains sixteen proposed claims grounded in six evidence windows from three Chinese works and one Sanskrit transcription. It also includes twenty-seven native CWN senses, source checks, a bilingual interface, and structured exports. None of the semantic claims has yet been accepted by an independent domain expert. The sixteen claims are not sixteen independent observations, since several share passages. We do not claim a temporal effect, a trained sense tagger, or a quality improvement from multiple agents. This transparent boundary is part of the design.','16 條主張來自 6 個片段，不是 n=16 的獨立實驗。來源檢查全部通過也不是模型語意正確率100%。這頁建議一定保留，避免問答時失去信任。',[src.data]);
}
{
 const s=slide('Evaluate verification, not agent count','在相同材料與可比較預算下，交由獨立專家盲評。');
 table(s,['Condition','Purpose'],[['Lexical retrieval + rules','Establish a transparent baseline'],['Single LLM','Measure the initial proposal quality'],['Multiple roles, no counterevidence','Separate role decomposition from checking'],['Verification + counterevidence','Test evidential improvement'],['Budget-matched single-model retries','Control for additional inference']],64,201,[605,547],64);
 txt(s,'Support rate · citation entailment · abstention · cost per supported claim',64,621,1150,35,24,C.blue);
 note(s,'Evaluate verification, not agent count','The evaluation must ask whether verification helps, rather than whether more agents can produce more text. We will compare lexical baselines, one model, multiple roles without counterevidence, and the full verification workflow. A budget-matched single-model retry condition controls for additional inference. Experts will assess support, citation entailment, abstention, and cost per supported claim. Data splits will be by work or textual family, keeping closely related witnesses together. If translator and period cannot be separated, the result will be reported as a textual or translator difference, not as an effect of time.','研究貢獻應落在可比較預算下的品質提升。保留拒答率與成本，避免只接受少量簡單主張取得高 precision。切分以作品／文本家族為單位，不能把平行或重譯段落隨機分進 train 和 test。',[src.data]);
}
{
 const s=slide('Build a resource scholars can revise','讓學術判斷可以保留出處、異議與修訂。');
 txt(s,'Comparable texts.\nExpert review.\nQuestions that evidence can challenge.',64,227,1152,248,43,C.ink,true);
 txt(s,'lopentu.github.io/sindia-site/buddhist/',64,540,1152,57,31,C.blue,true);txt(s,'CiWN · CWN.dia · TBSG · DharmaSwarm',64,612,1152,41,24,C.gray);
 note(s,'Build a resource scholars can revise','Our aim is a resource that scholars can revise. A useful semantic graph should preserve not only what is asserted, but where it applies, why it is supported, and what remains unsettled. We welcome three kinds of collaboration: comparable textual materials, expert review of senses and relations, and historical questions that the evidence could genuinely challenge. The prototype is deliberately small. Its purpose is to make the research commitments inspectable and to provide a foundation that can grow through careful, shared work.','結尾把合作邀請落實為三件事：可比文本、專家審核、可否證問題。對既有佛教數位資源保持互補的定位。現在的小規模是為了把方法站穩，不宣稱已涵蓋大藏經。',[src.data]);
}
{
 const s=slide('Appendix / Do not flatten relations','分類、成員、條件與同義性應分開表示。');
 table(s,['Example','Conservative representation'],[['Eight consciousnesses under 心法','Text-scoped classified_under'],['Members of an enumerated set','member_of; not automatically is_a'],['Dependent-arising conditions','Textually qualified condition_for'],['Practice-specific antidotes','antidote_for with scope and source'],['Parallel lexical positions','parallel_corresponds_to; not direct descent']],64,202,[605,547],69);
 note(s,'Appendix / Do not flatten relations','The proposal’s seed systems require typed relations. An enumeration is not automatically a taxonomy, and a conditional relation should not be silently treated as an empirical causal estimate. The PNC data conservatively encode the eight consciousnesses as classified under 心法 within the Hundred Dharmas text. Further commitments require domain review.','答覆本體問題時使用。修正原附件把不同名相綱領一律當 DAG 分類樹的說法。保持 classified_under 的保守標記。',[src.hundred]);
}
{
 const s=slide('Appendix / A staged research plan','三週形成可裁決的種子集；十二個月完成受控評估。');
 table(s,['Stage','Deliverable'],[['Three-week pilot','100–150 attestations; dual annotation; baselines'],['Months 1–3','Corpus, guidelines, schema, expert seed set'],['Months 4–6','Granularity-aware tagging and retrieval evaluation'],['Months 7–9','Bounded agents and verification ablations'],['Months 10–12','Matched temporal analysis and versioned release']],64,202,[345,807],69);
 note(s,'Appendix / A staged research plan','The immediate pilot targets one hundred to one hundred and fifty attestations, with dual annotation and adjudication. These are targets, not completed outputs. The twelve-month plan proceeds through data foundations, tagging and retrieval, controlled agent evaluation, and temporal analysis only where comparable evidence is available. Staffing and compute should follow these stages rather than the ambition to launch hundreds of agents at once.','規模皆是工作目標；正式研究需要人力承諾與經費，不在此虛列既有資源。優先三週落實少量可靠標註，不承諾兩天完成百筆專家 gold。',[src.data]);
}
// A shared schema is reused by the separately delivered talk guide.
await fs.writeFile(`${TMP}/talk-notes.json`,JSON.stringify(notes,null,2));
await fs.writeFile(`${TMP}/layout-ledger.json`,JSON.stringify(layoutLog,null,2));
const pptx=await PresentationFile.exportPptx(deck);await pptx.save(`${OUT}/CiWN_PNC_2026.pptx`);
for(const [i,s] of deck.slides.items.entries()){
 const blob=await deck.export({slide:s,format:'png',scale:1});await fs.writeFile(`${TMP}/slide-${String(i+1).padStart(2,'0')}.png`,new Uint8Array(await blob.arrayBuffer()));
 const lay=await s.export({format:'layout'});await fs.writeFile(`${TMP}/slide-${String(i+1).padStart(2,'0')}.json`,await lay.text());
}
console.log(`Created ${deck.slides.items.length} slides and full-size renders.`);
