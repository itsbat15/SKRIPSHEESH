from pathlib import Path
import re,json,hashlib,collections

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'BAB3_PENDUKUNG_2026-10-25/PENYELARASAN_BAHASA_2026-10-25'
TARGET=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU).md'
old_bytes=(OUT/'SEBELUM_PENYELARASAN'/TARGET.name).read_bytes()
before=old_bytes.decode('utf-8-sig').replace('\r\n','\n')
after=TARGET.read_text(encoding='utf-8-sig')
change=json.loads((OUT/'CATATAN PERUBAHAN NARASI.json').read_text(encoding='utf-8'))
checks={};issues={}
def check(k,v,detail=None):
 checks[k]=bool(v)
 if not v:issues[k]=detail
def tables(t):return re.findall(r'^\|.*$',t,re.M)
def images(t):return re.findall(r'^!\[[^\n]+$',t,re.M)
def captions(t):return re.findall(r'^(?:\*\*(?:Tabel|Gambar) 3\.[^\n]+|Sumber:[^\n]+)$',t,re.M)
check('all_table_rows_unchanged',tables(before)==tables(after))
check('all_ten_image_links_unchanged',images(before)==images(after) and len(images(after))==10)
check('all_captions_and_source_lines_unchanged',captions(before)==captions(after))
check('all_headings_unchanged',re.findall(r'^#.*$',before,re.M)==re.findall(r'^#.*$',after,re.M))
check('six_required_main_sections',re.findall(r'^## (3\.\d+) ',after,re.M)==['3.1','3.2','3.3','3.4','3.5','3.6'])
check('twenty_tables_sequential',re.findall(r'^\*\*Tabel 3\.(\d+) ',after,re.M)==[str(i) for i in range(1,21)])
check('ten_figures_sequential',re.findall(r'^\*\*Gambar 3\.(\d+) ',after,re.M)==[str(i) for i in range(1,11)])
check('all_129_narrative_paragraphs_revised',len(change['revisions'])==129 and all(x['before']!=x['after'] for x in change['revisions']))
missing=[]
for p in change['revisions']:
 citations=[x for x in re.findall(r'\([^()\n]+\)',p['before']) if re.search(r'\b(?:19|20)\d{2}\b|t\.t\.',x)]
 for c in citations:
  if c not in p['after']:missing.append({'paragraph':p['paragraph'],'citation':c})
check('citation_year_page_strings_preserved_in_same_paragraph',not missing,missing)
check('no_long_dash_in_prose',not any(x in after for x in ['\u2014','\u2013']))
check('no_double_dash_prose','--' not in re.sub(r'^\|.*$','',after,flags=re.M))
check('no_citation_footnotes','[^' not in after)
short=[];long=[];numeric=[]
for b in after.split('\n\n'):
 if not b.strip() or b.startswith(('#','|','!','**','Sumber:')):continue
 b=re.sub(r'\([^)]*\)','',b)
 sentences=[s for s in re.split(r'(?<=[.!?])\s+',b) if s.strip()]
 if len(sentences)<2:short.append(b)
 long.extend(s for s in sentences if len(s.split())>40)
 numeric.extend(s for s in sentences if re.match(r'^\s*\d',s))
check('prose_paragraphs_have_two_or_more_sentences',not short,short)
check('prose_sentences_at_most_40_words_excluding_citations',not long,long)
check('no_numeric_sentence_starts',not numeric,numeric)
headcodes=set(re.findall(r'^#{2,3} (3(?:\.\d+){1,2}) ',after,re.M))
check('section_references_resolve',set(re.findall(r'Subbab (3(?:\.\d+){1,2})',after))<=headcodes)
for label in ['Tabel','Gambar']:
 ids=re.findall(r'^\*\*'+label+r' 3\.(\d+) ',after,re.M)
 def mentioned_first(i):
  cap=after.index(f'**{label} 3.{i} ')
  return bool(re.search(re.escape(f'{label} 3.{i}')+r'(?!\d)',after[:cap]))
 check(label+'_introduced_before_caption',all(mentioned_first(n) for n in ids))
broken=[]
for p in re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)',after):
 if not Path(p).is_file():broken.append(p)
check('all_figure_files_exist',not broken,broken)
for p,sha in change['preserved_other_files'].items():
 name='draft1' if 'DRAFT 1' in p else 'five_section_draft' if 'DRAF 2026' in p else 'usecase' if 'USE CASE' in p else 'schema'
 check(name+'_not_modified',hashlib.sha256(Path(p).read_bytes()).hexdigest()==sha)
for prefix in ['KF','US','UC','PU','BB','UAT']:
 check(prefix+'_identifier_set_preserved',set(re.findall(r'\b'+prefix+r'-\d{2}\b',before))==set(re.findall(r'\b'+prefix+r'-\d{2}\b',after)))
check('backup_hash_matches_source',hashlib.sha256(old_bytes).hexdigest()==change['before_sha256'])
check('current_hash_matches_revision',hashlib.sha256(TARGET.read_bytes()).hexdigest()==change['after_sha256'])
report={'scope':'Editorial integrity checks only. Sentence-shape checks do not measure readability or certify methodological validity. No skill academic-paper used; no software, UAT, SQL or new source accreditation audit performed.',
 'file':str(TARGET),'sha256':hashlib.sha256(TARGET.read_bytes()).hexdigest(),
 'paragraphs_revised':129,'tables':20,'figures':10,'checks':checks,'passed':sum(checks.values()),'total':len(checks),'issues':issues}
(OUT/'HASIL PEMERIKSAAN NARASI.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':report['passed'],'total':report['total'],'failed':[k for k,v in checks.items() if not v],'issues':issues},ensure_ascii=False))
assert all(checks.values()),issues
