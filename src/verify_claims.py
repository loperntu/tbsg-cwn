"""Mechanical provenance gates. Passing creates a review candidate, never gold.

This module checks the declared local source snapshot, not live remote pages.
Semantic entailment, source dependence and scholarly accuracy require review.
"""
import argparse,hashlib,json,re,unicodedata
from pathlib import Path

def norm(s):return re.sub(r'\s+','',unicodedata.normalize('NFC',s))
ALLOWED={'parallel_corresponds_to','explained_as','co_referential_in_context','classified_under'}
def verify_claim(c,p):
 errors=[];events=[]
 def gate(role,ok,code):
  events.append({'role':role,'passed':bool(ok),'check':code})
  if not ok:errors.append(code)
 gate('schema',all(c.get(k) for k in ['id','subject','predicate','object','evidence_ids','context','required_surfaces']),'required_fields')
 gate('relation',c.get('predicate') in ALLOWED,'predicate_supported')
 gate('context',c.get('context',{}).get('source_id') in p.get('sources',{}),'context_source_exists')
 evs=c.get('evidence_ids',[])
 gate('source',bool(evs) and all(e in p.get('evidence',{}) for e in evs),'evidence_exists')
 if all(e in p.get('evidence',{}) for e in evs):
  for eid in evs:
   e=p['evidence'][eid]
   gate('source',e.get('source_id') in p['sources'],eid+':source_exists')
   gate('integrity',e.get('sha256')==hashlib.sha256(e.get('quote','').encode()).hexdigest(),eid+':snapshot_hash')
   if 'lines' in e:
    gate('source',all(e['start_line']<=r['line_id']<=e['end_line'] for r in e['lines']) and e['quote']==''.join(r['text'] for r in e['lines']),eid+':line_window')
    gate('context',all(e['section'] in r['section_path'] and r['text_role']=='body' for r in e['lines']),eid+':section_boundary')
  gate('context',any(p['evidence'][e]['source_id']==c.get('context',{}).get('source_id') for e in evs),'context_supported_by_evidence')
  for eid,terms in c.get('required_surfaces',{}).items():
   gate('lexical',eid in evs and bool(terms) and all(norm(t) in norm(p['evidence'].get(eid,{}).get('quote','')) for t in terms),eid+':literal_surfaces')
  if c.get('predicate')=='parallel_corresponds_to':
   gate('alignment',len({p['evidence'][e]['source_id'] for e in evs})>=2,'parallel_has_two_sources')
 # Fail closed: these checks do not establish semantic entailment.
 status='eligible_for_review' if not errors else 'rejected'
 events.append({'role':'adjudication','passed':False,'check':'expert_review_pending'})
 return {'id':c.get('id'),'mechanical_status':status,'errors':errors,'events':events,'semantic_status':'not_evaluated','human_review':'pending'}
def verify_package(p):
 rows=[verify_claim(c,p) for c in p['claims']]
 return {'mode':'deterministic-source-checks','summary':{'total':len(rows),'eligible_for_review':sum(r['mechanical_status']=='eligible_for_review' for r in rows),'rejected':sum(r['mechanical_status']=='rejected' for r in rows),'expert_accepted':0},'claims':rows,'limitations':'Checks local evidence integrity and literal occurrence, not philological entailment. No self-verifying LLM experiment was run.'}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--out',type=Path);a=ap.parse_args();r=verify_package(json.loads(a.input.read_text()));t=json.dumps(r,ensure_ascii=False,indent=2)
 if a.out:a.out.write_text(t)
 else:print(t)
 raise SystemExit(bool(r['summary']['rejected']))
