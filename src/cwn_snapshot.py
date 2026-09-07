"""Dependency-free, restricted data-image export for the pinned PNC release.

Unlike generic pickle.load, this reader rejects arbitrary global classes.
The public CwnGraph image used here contains only dictionaries and primitives.
Native IDs/glosses are preserved verbatim; mappings are separate proposals.
"""
import argparse,builtins,collections,hashlib,json,pickle
from pathlib import Path
class DataOnlyUnpickler(pickle.Unpickler):
 def find_class(self,module,name):
  if module=='collections' and name in {'defaultdict','Counter','OrderedDict'}:return getattr(collections,name)
  if module=='builtins' and name in {'set','frozenset','dict','list','tuple','str','int','float'}:return getattr(builtins,name)
  raise pickle.UnpicklingError('Disallowed global: '+module+'.'+name)
def export(image,manifest,out):
 with image.open('rb') as f:V,E,meta=DataOnlyUnpickler(f).load()
 if not all(isinstance(o,dict) for o in (V,E,meta)):raise ValueError('Unexpected image schema')
 wanted={k:v for k,v in V.items() if v.get('node_type')=='lemma' and v.get('lemma') in ['心','意','識']}
 senses=[]
 for (source,target),edata in E.items():
  if source in wanted and edata.get('edge_type')=='has_sense':
   n=V[target];senses.append({'lemma_id':source,'lemma':wanted[source]['lemma'],'sense_id':target,'gloss':n.get('def',''),'pos':n.get('pos'),'source':'CWN','status':'native_export'})
 result={'source':'https://github.com/lopentu/CwnGraph','manifest_url':'https://raw.githubusercontent.com/lopentu/CwnGraph/develop/etc/manifest.json','manifest':json.loads(manifest.read_text()),'image_metadata':meta,'image_sha256':hashlib.sha256(image.read_bytes()).hexdigest(),'retrieved':'2026-09-07','query':'exact lemma match: 心, 意, 識; all homographs retained','senses':sorted(senses,key=lambda s:(s['lemma'],s['sense_id'])),'rights':'CWN / CwnGraph source terms retained; this is a limited research excerpt, not a new standalone dictionary license.'}
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2));print('Native CWN senses:',len(senses))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('image',type=Path);p.add_argument('manifest',type=Path);p.add_argument('out',type=Path);a=p.parse_args();export(a.image,a.manifest,a.out)
