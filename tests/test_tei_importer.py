import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from cbeta_tei_importer import extract_rows
class TEIImporterTests(unittest.TestCase):
 def parse(self, body):
  xml='<TEI xmlns="http://www.tei-c.org/ns/1.0" xmlns:cb="http://www.cbeta.org/ns/1.0" xml:id="T00n0000"><teiHeader><p>HEADER</p></teiHeader><text><body>'+body+'</body><back><p>APPARATUS</p></back></text></TEI>'
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'sample.xml';p.write_text(xml);return extract_rows(p)
 def test_nested_tail_order(self):
  r=self.parse('<lb n="0001a01"/><p>A<hi>B<hi>C</hi>D</hi>E</p>')
  self.assertEqual(r[0]['text'],'ABCDE')
 def test_note_subtree_not_only_note_text(self):
  r=self.parse('<lb n="0001a01"/><p>A<note>N<hi>BAD</hi>Z</note>B</p>')
  self.assertEqual(r[0]['text'],'AB')
 def test_edition_lines_and_readings(self):
  r=self.parse('<lb n="0001a01" ed="T"/><p>A<lb n="x" ed="X"/><app><lem>B</lem><rdg>BAD</rdg></app>C</p>')
  self.assertEqual([(x['line_id'],x['text']) for x in r],[('0001a01','ABC')])
 def test_preface_not_inherited_into_main_text(self):
  r=self.parse('<cb:div type="xu"><lb n="0001a01"/><p>PREFACE</p></cb:div><cb:div type="jing"><lb n="0001a02"/><p>MAIN</p></cb:div>')
  self.assertEqual([x['section_path'] for x in r],[['xu'],['jing']])
 def test_cross_line_and_fascicle(self):
  r=self.parse('<milestone unit="juan" n="2"/><lb n="0001a01"/><p>A<lb n="0001a02"/>B</p>')
  self.assertEqual([x['text'] for x in r],['A','B']);self.assertEqual(r[1]['fascicle'],'2')
 def test_heading_separated(self):
  r=self.parse('<lb n="0001a01"/><head>TITLE</head><p>BODY</p>')
  self.assertEqual([(x['text_role'],x['text']) for x in r],[('head','TITLE'),('body','BODY')])
if __name__=='__main__':unittest.main()
