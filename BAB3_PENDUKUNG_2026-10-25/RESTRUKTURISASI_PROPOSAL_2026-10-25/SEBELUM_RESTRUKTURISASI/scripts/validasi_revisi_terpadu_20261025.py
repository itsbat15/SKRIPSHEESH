from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
SUP=ROOT/'BAB3_PENDUKUNG_2026-10-25'
paths={
 'usecase':ROOT/'DOKUMEN MD/PERANCANGAN USE CASE & SKENARIO.md',
 'schema':ROOT/'DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md',
 'chapter':ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'}
texts={k:p.read_text(encoding='utf-8') for k,p in paths.items()}
meta=json.loads((OUT/'SKEMA_TERSTRUKTUR.json').read_text(encoding='utf-8'))
matrix=json.loads((OUT/'MATRIKS_KETERLACAKAN.json').read_text(encoding='utf-8'))
names={x['name'] for x in meta['tables']}
checks={}; issues={}
def check(k,result,detail=None):
 checks[k]=bool(result)
 if not result and detail is not None:issues[k]=detail

check('schema_has_23_unique_tables',len(names)==len(meta['tables'])==23)
uc_set={f'UC-{i:02}' for i in range(14)}
check('fourteen_distinct_usecase_scenarios',set(re.findall(r'^### (UC-\d{2})\.',texts['usecase'],re.M))==uc_set)
uc_diagram=texts['usecase'].split('```mermaid',1)[1].split('```',1)[0]
check('diagram_includes_all_usecases',set(re.findall(r'UC-\d{2}',uc_diagram))==uc_set)
active_matrix=texts['usecase'].split('## 5.',1)[1].split('## 6.',1)[0]
check('every_schema_table_referenced_in_usecase_matrix',all(re.search(r'\b'+n+r'\b',active_matrix) for n in names))
check('all_structured_matrix_tables_exist',all(set(f['tables'])<=names for f in matrix))
check('all_schema_tables_referenced_in_structured_matrix',set(n for f in matrix for n in f['tables'])==names)
check('all_14_requirements_mapped_once',[f['kf'] for f in matrix]==[f'KF-{i:02}' for i in range(1,15)])
check('all_14_user_stories_mapped_once',[f['us'] for f in matrix]==[f'US-{i:02}' for i in range(1,15)])
check('all_14_uat_groups_mapped_once',[f['uat'] for f in matrix]==[f'UAT-{i:02}' for i in range(1,15)])
check('all_usecases_have_requirement',set(f['uc'] for f in matrix)==uc_set)
check('every_requirement_has_bb_cases',all(f['bb'] for f in matrix))
check('all_33_bb_cases_mapped',set(b for f in matrix for b in f['bb'])=={f'BB-{i:02}' for i in range(1,34)})
ap=(OUT/'LAMPIRAN PENGUJIAN DAN PELAKSANAAN.md').read_text(encoding='utf-8')
bb_rows=re.findall(r'^\| (BB-\d{2}) \|',ap,re.M)
check('thirty_three_distinct_test_rows',len(bb_rows)==33 and len(set(bb_rows))==33)
check('all_test_rows_unexecuted',all('Belum diuji' in row for row in ap.splitlines() if row.startswith('| BB-')))
ch=texts['chapter']
check('six_template_main_sections',re.findall(r'^## (3\.\d+) ',ch,re.M)==['3.1','3.2','3.3','3.4','3.5','3.6'])
check('maximum_three_heading_levels',not re.search(r'^#+ \d+\.\d+\.\d+\.',ch,re.M))
check('twenty_sequential_tables',re.findall(r'^\*\*Tabel 3\.(\d+) ',ch,re.M)==[str(i) for i in range(1,21)])
check('ten_sequential_figures',re.findall(r'^\*\*Gambar 3\.(\d+) ',ch,re.M)==[str(i) for i in range(1,11)])
for name,start,end in [('requirements','**Tabel 3.9 ','Tabel 3.10'),('stories','**Tabel 3.12 ','Tabel 3.13')]:
 block=ch.split(start,1)[1].split(end,1)[0]
 prefix='KF' if name=='requirements' else 'US'
 check('chapter_'+name+'_complete',set(re.findall(r'^\| ('+prefix+r'-\d{2}) \|',block,re.M))=={f'{prefix}-{i:02}' for i in range(1,15)})
block=ch.split('**Tabel 3.13 ',1)[1].split('### 3.4.5',1)[0]
tuples=[]
for row in block.splitlines():
 if row.startswith('| KF-'):
  cols=[x.strip() for x in row.strip('|').split('|')]
  tuples.append((cols[0],cols[2],cols[3],cols[4],cols[5]))
expected=[(f['kf'],f['us'],f['uc'],f['iteration'],f"{f['test_group']}; {f['uat']}") for f in matrix]
check('chapter_trace_matches_canonical_contract',tuples==expected,tuples)
block=ch.split('**Tabel 3.7 ',1)[1].split('### 3.4',1)[0]
check('chapter_all_uat_tasks_present',set(re.findall(r'^\| (UAT-\d{2}) \|',block,re.M))=={f'UAT-{i:02}' for i in range(1,15)})
for f in matrix:
 row=next((s for s in active_matrix.splitlines() if s.startswith('| '+f['kf']+' ')),None)
 check('usecase_mapping_'+f['kf'],row is not None and all(v in row for v in [f['us'],f['uc'],f['iteration'],f['test_group'],f['uat']]),row)
for label,t in texts.items():
 clean=re.sub(r'```.*?```','',t,flags=re.S)
 check(label+'_no_long_dash',not any(c in clean for c in ['\u2014','\u2013']))
 check(label+'_no_double_dash_prose','--' not in re.sub(r'^\|.*$','',clean,flags=re.M))
 short=[];long=[];numeric=[];table_bad=[]
 for p in clean.split('\n\n'):
  if not p.strip() or p.startswith(('#','|','!','**','Sumber:','- ')) or re.match(r'^\d+\.',p):continue
  prose=re.sub(r'\([^)]*\)','',p)
  ss=[s for s in re.split(r'(?<=[.!?])\s+',prose) if s.strip()]
  if len(ss)<2:short.append(p[:180])
  long.extend(s for s in ss if len(s.split())>40)
  numeric.extend(s for s in ss if re.match(r'^\d',s))
 for block in t.split('\n\n'):
  if block.startswith('|'):
   counts=[len(re.split(r'(?<!\\)\|',line)) for line in block.splitlines() if line.startswith('|')]
   if len(set(counts))>1:table_bad.append(block[:150])
 check(label+'_prose_min_two_sentences',not short,short)
 check(label+'_prose_max_40_words',not long,long)
 check(label+'_no_numeric_sentence_start',not numeric,numeric)
 check(label+'_table_columns_consistent',not table_bad,table_bad)
 check(label+'_no_citation_footnotes','[^' not in t)

broken=[]
for p in [*paths.values(),*OUT.glob('*.md'),*SUP.glob('*.md')]:
 for s in re.findall(r'\]\(<([^>]+)>\)',p.read_text(encoding='utf-8')):
  if re.match(r'^[A-Za-z]:/',s) and not Path(re.sub(r':\d+$','',s)).exists():broken.append({'file':str(p),'target':s})
check('all_local_links_resolve',not broken,broken)
pngs=list((SUP/'gambar').glob('*.png'));svgs=list((SUP/'gambar').glob('*.svg'))
check('ten_png_ten_svg',len(pngs)==len(svgs)==10)
for p in pngs:
 with Image.open(p) as im:im.verify()
for p in svgs:ET.parse(p)
check('png_decode_and_svg_xml',True)
check('all_chapter_images_exist',all(Path(s).exists() for s in re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)',ch)))
check('usecase_figure_all_14_codes',all(f'UC-{i:02}' in (SUP/'gambar/Gambar_3_2_Use_Case_Inti.svg').read_text(encoding='utf-8') for i in range(14)))
check('all_six_wireframes_mark_simulation',all('SIMULASI' in p.read_text(encoding='utf-8').upper() for p in svgs if re.search(r'Gambar_3_[4-9]_',p.name)))
sources=json.loads((SUP/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))['sources']
check('original_13_source_pdf_hashes_unchanged',len(sources)==13 and all(hashlib.sha256(Path(s['file']).read_bytes()).hexdigest()==s['sha256'] for s in sources))
check('three_original_files_preserved',all((OUT/'SEBELUM_REVISI'/p.name).exists() and (OUT/'SEBELUM_REVISI'/p.name).read_bytes()!=p.read_bytes() for p in paths.values()))

def tb(n):return next(x for x in meta['tables'] if x['name']==n)
def field(n,f):return next(x for x in tb(n)['fields'] if x['name']==f)
check('payments_have_no_direct_bill_fk',not any(f['ref']=='bills.id' for f in tb('payments')['fields']))
check('allocations_bridge_payments_bills',field('payment_allocations','payment_id')['ref']=='payments.id' and field('payment_allocations','bill_id')['ref']=='bills.id')
check('single_final_review_per_submission',field('payment_reviews','payment_id')['unique'])
check('resubmission_preserves_parent',field('payments','resubmission_of_id')['ref']=='payments.id')
check('bankmatch_source_links_optional_unique',all(field('bank_matches',f)['nullable'] and field('bank_matches',f)['unique'] for f in ['payment_id','cash_batch_id']))
check('bill_payment_historical_branch',all(field(n,'branch_id')['ref']=='branches.id' for n in ['bills','payments']))
check('active_count_not_independent_field','current_students' not in {f['name'] for f in tb('classes')['fields']})
check('reminder_does_not_store_delivery_status',not any(f['name'] in ['sent_status','sent_at','delivery_status'] for f in tb('reminder_actions')['fields']))
check('class_lifecycle_not_fullness',field('classes','status')['type']=="ENUM('active','closed')")
check('schedule_subject_is_explicit',field('class_schedules','subject_id')['ref']=='subjects.id')
check('payment_states_match_documents',all('submitted' in texts[k] and 'verified' in texts[k] and 'returned' in texts[k] for k in ['usecase','schema']))

out={
 'date':'2026-10-25',
 'scope':'Checks of document structure, identifiers, declared schema relationships, source-file integrity, images, and cross-document mappings. Not executed SQL, application/concurrency testing, partner acceptance, or final Word/PDF layout.',
 'checks':checks,'issues':issues,'passed':sum(checks.values()),'total':len(checks),
 'files':{k:{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'words':len(texts[k].split())} for k,p in paths.items()},
 'counts':{'usecases':14,'schema_tables':len(names),'fields':sum(len(x['fields']) for x in meta['tables']),'foreign_keys':sum(bool(f['ref']) for x in meta['tables'] for f in x['fields']),'functional_requirements':14,'user_stories':14,'uat_tasks':14,'bb_cases':33,'chapter_tables':20,'chapter_figures':10},
 'application_tests_executed':False,'ddl_executed':False,'partner_acceptance_claimed':False,
 'open_decisions':['Kewenangan rekening dan pemeriksa transfer','Tarif, potongan, kapasitas dan ambang aktual','Pembayaran sebagian dan pengecualian pencocokan','Peserta dan tanggal UAT','Versi layanan, perangkat keras dan kalender','Penyelarasan Bab1/2 setelah keputusan terkait ditetapkan','Tata letak Word/PDF akhir']}
(OUT/'HASIL VALIDASI TERPADU.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':out['passed'],'total':out['total'],'failed':[k for k,v in checks.items() if not v],'issues':issues},ensure_ascii=False))
assert all(checks.values()),issues
