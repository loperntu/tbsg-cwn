"""Export the PNC snapshot as provenance-bearing N-Quads without a backend."""
import argparse,json
from pathlib import Path
NS='https://w3id.org/tbsg-cwn/ontology#'
RDF='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
PROV='http://www.w3.org/ns/prov#'
RDFS='http://www.w3.org/2000/01/rdf-schema#'
def export(p):
 lines=[]
 def u(s):return '<'+s+'>'
 def lit(s):return json.dumps(str(s),ensure_ascii=False)
 def q(s,pred,o,g,literal=False):lines.append(f'{u(s)} {u(pred)} {lit(o) if literal else u(o)} {u("urn:graph:"+g)} .')
 for c in p['claims']:
  uri='urn:ciwn:claim:'+c['id'];q(uri,RDF+'type',NS+'ScholarlyClaim','claims')
  for prop,val in [('subjectLabel',c['subject']),('objectLabel',c['object']),('relationType',c['predicate']),('claimScope',c['context']['scope'])]:q(uri,NS+prop,val,'claims',True)
  q(uri,RDFS+'label',c['label_en'],'claims',True)
  q(uri,NS+'reviewStatus','human-review-pending','adjudication',True)
  q(uri,NS+'mechanicalStatus',c['source_checks']['mechanical_status'],'adjudication',True)
  q(uri,NS+'counterevidenceSearchStatus','not-run','adjudication',True)
  for eid in c['evidence_ids']:q(uri,NS+'supportedBy','urn:ciwn:evidence:'+eid,'claims')
  q(uri,NS+'contextText','urn:ciwn:source:'+c['context']['source_id'],'context')
  if c['cwn_mapping'].get('native_sense_id'):
   # Candidate mappings remain reified. Do not assert an accepted sense link.
   m=uri+':mapping';q(uri,NS+'mappingProposal',m,'senses');q(m,NS+'targetNativeSenseId',c['cwn_mapping']['native_sense_id'],'senses',True);q(m,NS+'reviewStatus','pending','adjudication',True)
 for eid,e in p['evidence'].items():
  uri='urn:ciwn:evidence:'+eid;q(uri,RDF+'type',NS+'Attestation','provenance');q(uri,NS+'surfaceForm',e['quote'],'context',True);q(uri,PROV+'wasDerivedFrom',p['sources'][e['source_id']]['url'],'provenance');q(uri,NS+'contentSHA256',e['sha256'],'provenance',True)
  for prop,key in [('lineStart','start_line'),('lineEnd','end_line'),('sectionType','section')]:
   if key in e:q(uri,NS+prop,e[key],'context',True)
 for sid,s in p['sources'].items():
  uri='urn:ciwn:source:'+sid;q(uri,NS+'sourceURI',s['url'],'provenance');q(uri,NS+'contentSHA256',s['sha256'],'provenance',True)
  if s.get('source_revision'):q(uri,NS+'sourceRevision',s['source_revision'],'provenance',True)
 for c in p['consets']:
  uri='urn:ciwn:conset:'+c['id'];q(uri,RDF+'type',NS+'ContextualConset','senses');q(uri,NS+'scopeEvidence','urn:ciwn:evidence:'+c['scope_evidence'],'senses');q(uri,NS+'reviewStatus','candidate','adjudication',True)
  for i,term in enumerate(c['members']):
   m=uri+':membership:'+str(i);q(m,RDF+'type',NS+'ConsetMembershipProposal','senses');q(m,NS+'inConset',uri,'senses');q(m,NS+'memberForm',term,'lexicon',True)
 return '\n'.join(lines)+'\n'
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('input',type=Path);a.add_argument('output',type=Path);v=a.parse_args();text=export(json.loads(v.input.read_text()));v.output.write_text(text);print('Exported',len(text.splitlines()),'N-Quads statements')
