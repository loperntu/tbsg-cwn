import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from verify_claims import verify_claim,verify_package
class VerifierTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.p=json.loads((ROOT/'data/pnc2026/claims.json').read_text())
 def test_candidates_never_become_gold(self):
  r=verify_package(self.p);self.assertEqual(r['summary']['expert_accepted'],0);self.assertEqual(r['summary']['eligible_for_review'],16)
 def test_missing_citation_is_rejected(self):
  c=copy.deepcopy(self.p['claims'][0]);c['evidence_ids'][0]='NOT-FOUND';self.assertEqual(verify_claim(c,self.p)['mechanical_status'],'rejected')
 def test_snapshot_tampering_is_detected(self):
  p=copy.deepcopy(self.p);p['evidence']['E-HEART-SKANDHA']['quote']+='偽造經文';r=verify_claim(p['claims'][0],p);self.assertIn('E-HEART-SKANDHA:snapshot_hash',r['errors'])
 def test_wrong_surface_is_rejected(self):
  c=copy.deepcopy(self.p['claims'][0]);c['required_surfaces']['E-SA-SKANDHA']=['NONEXISTENT'];self.assertEqual(verify_claim(c,self.p)['mechanical_status'],'rejected')
 def test_unlicensed_direct_translation_relation(self):
  c=copy.deepcopy(self.p['claims'][0]);c['predicate']='directly_translated_from';self.assertIn('predicate_supported',verify_claim(c,self.p)['errors'])
 def test_foreign_context_is_rejected(self):
  c=copy.deepcopy(self.p['claims'][0]);c['context']['source_id']='T1614';self.assertIn('context_supported_by_evidence',verify_claim(c,self.p)['errors'])
 def test_section_mismatch_is_rejected(self):
  p=copy.deepcopy(self.p);p['evidence']['E-HEART-SKANDHA']['lines'][0]['section_path']=['xu'];r=verify_claim(p['claims'][0],p);self.assertIn('E-HEART-SKANDHA:section_boundary',r['errors'])
 def test_repair_does_not_change_original(self):
  c=copy.deepcopy(self.p['claims'][0]);c['evidence_ids'][0]='MISSING';before=copy.deepcopy(c);verify_claim(c,self.p);self.assertEqual(c,before);c['evidence_ids'][0]='E-HEART-SKANDHA';self.assertEqual(verify_claim(c,self.p)['mechanical_status'],'eligible_for_review')
if __name__=='__main__':unittest.main()
