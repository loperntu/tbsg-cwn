"""Reproduce the small PNC evidence release from pinned, public source bytes.

No embeddings, live agents, or expert adjudication are simulated. The curated
claim templates are explicitly machine-prepared proposals. Only mechanical
source checks are automated. Run from any directory; uses Python stdlib only.
"""
from __future__ import annotations
import argparse,hashlib,json,re,urllib.request,unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from cbeta_tei_importer import extract_rows

REPO=Path(__file__).resolve().parents[1]
REV='dbdea41071e1e260ad84b72faefd4587333cf76d'
FILES={'T0251':('T/T08/T08n0251.xml','般若波羅蜜多心經','Prajñāpāramitāhṛdaya'), 'T1558':('T/T29/T29n1558.xml','阿毘達磨俱舍論','Abhidharmakośabhāṣya'), 'T1614':('T/T31/T31n1614.xml','大乘百法明門論','Treatise on the Hundred Dharmas')}
EXPECTED_HASHES={'T0251': 'f5507df86309f861ef2b92e9ba9db985c6db0ad357553599c6e921e15deca761', 'T1558': 'c38aec4b48a24702dbc6217b2604288d63007d65a48a08cea538397458894fca', 'T1614': '71792c2b98c7de70fdbf809d4ea7206c77d277154078cc3bf81764721b370f62', 'SA-HEART': '00ea2f1021daecbaba2852cbfbad0f95b1ead9abdde986508420659cd10d9796'}
SA_URL='https://buddhism.lib.ntu.edu.tw/FULLTEXT/mukherjee/articles/html/sk-heart.htm'
class TextParser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('style','script'):self.skip+=1
  if t in ('p','br','div'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('style','script'):self.skip-=1
  if t in ('p','div'):self.parts.append('\n')
 def handle_data(self,d):
  if not self.skip:self.parts.append(d)
def digest(b):return hashlib.sha256(b).hexdigest()
def normalized(s):return re.sub(r'\s+','',unicodedata.normalize('NFC',s))
def read_source(url,path,offline):
 if not path.exists():
  if offline:raise FileNotFoundError(path)
  req=urllib.request.Request(url,headers={'User-Agent':'CiWN-PNC-research/0.1','Referer':'https://lopentu.github.io/sindia-site/buddhist/'})
  path.write_bytes(urllib.request.urlopen(req,timeout=45).read())
 return path.read_bytes()
def build(cache,out,offline=False):
 cache.mkdir(parents=True,exist_ok=True);out.mkdir(parents=True,exist_ok=True)
 sources={};rows={}
 for work,(path,zh,en) in FILES.items():
  url=f'https://raw.githubusercontent.com/cbeta-org/xml-p5/{REV}/{path}'
  raw=read_source(url,cache/(work+'.xml'),offline)
  if digest(raw)!=EXPECTED_HASHES[work]:raise ValueError('Source snapshot differs from the reviewed release: '+work)
  # The publication date is the XML header date, not a claimed CBETA release.
  import xml.etree.ElementTree as ET
  root=ET.fromstring(raw);ns={'t':'http://www.tei-c.org/ns/1.0'}
  head=root.find('t:teiHeader',ns);header=ET.tostring(head,encoding='unicode')
  (out/(work+'-source-header.xml')).write_text(header)
  sources[work]={'id':work,'title_zh':zh,'title_en':en,'url':f'https://cbetaonline.dila.edu.tw/zh/{root.get("{http://www.w3.org/XML/1998/namespace}id")}', 'raw_url':url,'source_revision':REV,'sha256':digest(raw),'source_header_file':work+'-source-header.xml','edition':'CBETA XML TEI P5; Taishō main reading','retrieved':'2026-09-07','publication_date':root.findtext('t:teiHeader/t:fileDesc/t:publicationStmt/t:date',namespaces=ns),'rights':'CBETA: non-commercial use with source header intact; included header accompanies these excerpts.'}
  rows[work]=extract_rows(cache/(work+'.xml'))
 sa_bytes=read_source(SA_URL,cache/'heart-sa.html',offline)
 if digest(sa_bytes)!=EXPECTED_HASHES['SA-HEART']:raise ValueError('Sanskrit source changed; review before updating the release')
 parser=TextParser();parser.feed(sa_bytes.decode('cp950'));sa_text=''.join(parser.parts)
 sources['SA-HEART']={'id':'SA-HEART','title_zh':'臺大佛學數位圖書館：梵文《心經》轉寫','title_en':'NTU Buddhist Digital Library: Sanskrit Heart Sūtra transcription','url':SA_URL,'sha256':digest(sa_bytes),'retrieved':'2026-09-07','rights':'Brief scholarly excerpts; original transcription retains source terms.','source_revision':None,'decoding':'cp950: legacy bytes conflict with declared UTF-8; Sanskrit diacritics are HTML entities','witness_status':'hosted transcription; manuscript identity and direct source dependence not established'}
 evidence={}
 def ev(key,work,start,end,section='jing'):
  subset=[x for x in rows[work] if start<=x['line_id']<=end and x['text_role']=='body' and (not section or section in x['section_path'])]
  if not subset:raise ValueError((key,work,start,end))
  evidence[key]={'id':key,'source_id':work,'start_line':start,'end_line':end,'fascicle':subset[0]['fascicle'],'section':section,'quote':''.join(x['text'] for x in subset),'lines':subset,'url':sources[work]['url']+'?line='+start,'sha256':digest(''.join(x['text'] for x in subset).encode())}
 ev('E-HEART-SKANDHA','T0251','0848c08','0848c09')
 ev('E-HEART-MIND','T0251','0848c14','0848c15')
 ev('E-KOSA','T1558','0021c18','0021c25',section='pin')
 ev('E-HUNDRED','T1614','0855b20','0855b22')
 # Preserve a single literal paragraph from the HTML transcription, not an invented translation.
 for key,needle in [('E-SA-SKANDHA','evam eva'),('E-SA-MIND','tasmād aprāptitvād')]:
  lines=[re.sub(r'\s+',' ',s).strip() for s in sa_text.split('\n') if normalized(needle) in normalized(s)]
  if not lines:raise ValueError('Missing Sanskrit paragraph '+needle)
  q=lines[0];evidence[key]={'id':key,'source_id':'SA-HEART','quote':q,'locator':needle,'url':SA_URL,'sha256':digest(q.encode()),'section':'transcription'}
 claims=[]
 def add(id,subject,predicate,obj,evs,zh,en,notezh,noteen,required,context):
  claims.append({'id':id,'subject':subject,'predicate':predicate,'object':obj,'evidence_ids':evs,'label_zh':zh,'label_en':en,'note_zh':notezh,'note_en':noteen,'required_surfaces':required,'context':context,'status':'machine_prepared','human_review':'pending','counterevidence_search':'not_run','confidence':None,'cwn_mapping':{'status':'pending_native_export','native_sense_id':None},'proposed_by':'assistant-curated-template','source_checks':None})
 add('C001','vijñāna','parallel_corresponds_to','識',['E-HEART-SKANDHA','E-SA-SKANDHA'],'識與 vijñāna 的平行位置','識 and vijñāna in parallel passages','對應的是同一列舉位置；未聲稱此現存梵文轉寫就是漢譯底本。','This is a passage-level correspondence, not a claim that the extant Sanskrit transcription was the Chinese text’s direct source.',{'E-HEART-SKANDHA':['識'],'E-SA-SKANDHA':['vijñānāni']},{'source_id':'T0251','scope':'passage','tradition_zh':'般若文獻','tradition_en':'Prajñāpāramitā literature','date_label':'7th century; traditional attribution','attribution':'玄奘：經錄／傳統歸屬，非底本依存證明'})
 add('C002','citta','parallel_corresponds_to','心',['E-HEART-MIND','E-SA-MIND'],'心與 citta 複合詞的平行語境','心 and the citta compound in parallel context','梵文為 acittāvaraṇaḥ 複合形式；lemma 對應及否定作用域仍需梵文專家審核。','The Sanskrit witness has the compound acittāvaraṇaḥ. Lemma alignment and the scope of negation require specialist review.',{'E-HEART-MIND':['心'],'E-SA-MIND':['acittāvaraṇaḥ']},{'source_id':'T0251','scope':'passage','tradition_zh':'般若文獻','tradition_en':'Prajñāpāramitā literature','date_label':'7th century; traditional attribution'})
 for i,(term,feature,eng) in enumerate([('心','集起','accumulation'),('意','思量','mentation'),('識','了別','discrimination')],3):
  add(f'C{i:03}',term,'explained_as',feature,['E-KOSA'],f'{term}：{feature}故名',f'{term}: explained through {eng}','保留論述中的命名理據，不將之提升為跨宗派的唯一詞義。','Preserve the local explanation of the name; do not universalize it across traditions.',{'E-KOSA':[term,feature]},{'source_id':'T1558','scope':'passage','tradition_zh':'《俱舍論》本段論述','tradition_en':'Local Kośa exposition','date_label':'7th century; traditional attribution'})
 for i,(a,b) in enumerate([('心','意'),('意','識'),('心','識')],6):
  add(f'C{i:03}',a,'co_referential_in_context',b,['E-KOSA'],f'{a}／{b}：義異而體一',f'{a} / {b}: distinct explanations, one referent','「體一」是本段的義理主張；不能推出任何語境中皆可互換，亦不採 owl:sameAs。','The passage asserts a shared referent while distinguishing explanations. This licenses neither unrestricted substitutability nor owl:sameAs.',{'E-KOSA':['義雖有異而體是一',a,b]},{'source_id':'T1558','scope':'passage','tradition_zh':'《俱舍論》本段論述','tradition_en':'Local Kośa exposition','date_label':'7th century; traditional attribution','conset_id':'CONSET-KOSA-MIND-001'})
 for i,term in enumerate(['眼識','耳識','鼻識','舌識','身識','意識','末那識','阿賴耶識'],9):
  add(f'C{i:03}',term,'classified_under','心法',['E-HUNDRED'],f'{term}列於心法',f'{term} classified under 心法','限於《百法明門論》的八種心法分類。暫採保守的 classified_under，待審核是否可轉為嚴格上下位關係。','Scoped to this text’s eightfold classification. classified_under is conservative; a strict taxonomic interpretation awaits review.',{'E-HUNDRED':[term,'心法','八種']},{'source_id':'T1614','scope':'textual_classification','tradition_zh':'《百法明門論》分類','tradition_en':'Hundred Dharmas classification','date_label':'7th century; traditional attribution'})
 pre=[r for r in rows['T0251'] if r['text_role']=='body' and 'xu' in r['section_path']]
 body=[r for r in rows['T0251'] if r['text_role']=='body' and 'jing' in r['section_path']]
 audit={'work':'T0251','method':'Literal character count of 心 in body-role rows; paratext headings/bylines excluded. Not word segmentation, sense annotation, or independent samples.','preface_xin':sum(r['text'].count('心') for r in pre),'sutra_xin':sum(r['text'].count('心') for r in body),'preface_heading_row_count':len([r for r in rows['T0251'] if r['text_role']=='head' and 'xu' in r['section_path']]),'preface_headings':[r for r in rows['T0251'] if r['text_role']=='head' and 'xu' in r['section_path']],'source_id':'T0251','implication':'Document-level translator/year attribution cannot be safely propagated to every contained section.'}
 package={'release':'PNC-2026-09-07','schema_version':'0.2','description':'Small, source-checkable demonstration. All semantic claims await expert adjudication. No temporal effect or model benchmark has been measured.','sources':sources,'evidence':evidence,'claims':claims,'paratext_audit':audit,'consets':[{'id':'CONSET-KOSA-MIND-001','members':['心','意','識'],'scope_evidence':'E-KOSA','relation':'co_referential_in_context','status':'candidate','clustering':'curated from explicit passage, no embeddings run'}]}
 from verify_claims import verify_package
 cwn_path=out/'cwn-native.json'
 if cwn_path.exists():
  package['cwn']=json.loads(cwn_path.read_text())
  for c in claims:
   if c['id']=='C001':
    c['cwn_mapping']={'status':'candidate_inventory_gap','native_sense_id':None,'examined_sense_ids':['03039001','03039002','03039003','03039004'],'relation':'no_exact_match_in_queried_snapshot','review':'pending','note':'The four exact-lemma 識 glosses do not explicitly encode the skandha sense. This is a coverage-review candidate, not proof of historical innovation.'}
   elif c['id'] in ['C002','C003']:
    c['cwn_mapping']={'status':'candidate_related_to','native_sense_id':'05231612','relation':'related_to','review':'pending','note':'Native CWN gloss: 人的感情或思想。 A proposed modern anchor, not equivalence or a proven historical descendant.'}
   else:c['cwn_mapping']={'status':'not_assessed','native_sense_id':None}
 report=verify_package(package)
 for claim in package['claims']:claim['source_checks']=next(r for r in report['claims'] if r['id']==claim['id'])
 (out/'claims.json').write_text(json.dumps(package,ensure_ascii=False,indent=2))
 (out/'verification-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps({'claims':len(claims),'evidence_windows':len(evidence),'sources':len(sources),'report':report['summary'],'paratext':{'preface_xin':audit['preface_xin'],'sutra_xin':audit['sutra_xin']}},ensure_ascii=False))
 return package
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,default=REPO/'data/derived/source-cache');ap.add_argument('--out',type=Path,default=REPO/'data/pnc2026');ap.add_argument('--offline',action='store_true');a=ap.parse_args();build(a.cache,a.out,a.offline)
