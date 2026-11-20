from pathlib import Path
import json,re,hashlib,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
SUP=ROOT/'BAB3_PENDUKUNG_2026-10-25'
OUT=SUP/'RESTRUKTURISASI_PROPOSAL_2026-10-25'
result_path=OUT/'HASIL VALIDASI STRUKTUR PROPOSAL.json'
result_path.write_text(json.dumps({'status':'running','scope':'Document-only checks in progress'}),encoding='utf-8')
checks={};issues={}
def check(k,v,detail=None):
 checks[k]=bool(v)
 if not v:issues[k]=detail

for script,label in [('periksa_bab3_20261025.py','chapter_checker'),('validasi_revisi_terpadu_20261025.py','integrated_checker')]:
 run=subprocess.run([sys.executable,str(ROOT/'scripts'/script)],capture_output=True,text=True,encoding='utf-8')
 check(label+'_passed',run.returncode==0,run.stdout+run.stderr)
 print(run.stdout.strip())

ch=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'
t=ch.read_text(encoding='utf-8')
mapping=json.loads((OUT/'PETA RESTRUKTURISASI.json').read_text(encoding='utf-8'))
old=(OUT/'SEBELUM_RESTRUKTURISASI'/ch.name).read_text(encoding='utf-8')
ref=Path(mapping['reference']).read_text(encoding='utf-8')
main=re.findall(r'^## (3\.\d+) ([^\n]+)',t,re.M)
ref_main=re.findall(r'^## (3\.\d+) ([^\n]+)',ref,re.M)
check('five_main_titles_match_supplied_proposal',main==ref_main,main)
check('chapter_title_desain_dan_implementasi',t.startswith('# BAB 3\n# DESAIN DAN IMPLEMENTASI\n'))
sub=re.findall(r'^### (3\.3\.\d+) ([^\n]+)',t,re.M)
check('three_research_subsections',sub==[('3.3.1','Garis Besar Penelitian'),('3.3.2','Diagram Alir Penelitian'),('3.3.3','Prosedur Penelitian')],sub)
letters=re.findall(r'^\*\*([A-K])\. ',t,re.M)
check('eleven_procedure_parts_a_to_k',letters==list('ABCDEFGHIJK'),letters)
check('pxp_initialization_and_retrospective_retained','**E. Inisialisasi Iterasi' in t and '**I. Evaluasi Iterasi' in t)
check('blackbox_and_uat_retained','Black Box Testing' in t and 'User Acceptance Testing' in t)
check('no_adoption_of_sus_or_mobile_stack','System Usability Scale' not in t and 'React Native' not in t and 'Expo Push' not in t)
check('no_fourth_level_numbered_heading',not re.search(r'^#+ \d+\.\d+\.\d+\.',t,re.M))
heads={m[0] for m in re.findall(r'^#{2,3} (3(?:\.\d+){1,2}) ([^\n]+)',t,re.M)}
refs=set(re.findall(r'Subbab (3(?:\.\d+){1,2})',t))
check('all_explicit_section_references_resolve',refs<=heads,sorted(refs-heads))
check('section_ledger_matches_current_headings',set(mapping['section_map'])==heads)
check('structural_reference_unchanged',hashlib.sha256(Path(mapping['reference']).read_bytes()).hexdigest()==json.loads((SUP/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))['structure_reference']['sha256'])
for name,sha in mapping['unchanged_design_files'].items():
 check('unchanged_'+('usecase' if 'USE CASE' in name else 'schema'),hashlib.sha256(Path(name).read_bytes()).hexdigest()==sha)
check('previous_chapter_copy_matches_original_hash',hashlib.sha256((OUT/'SEBELUM_RESTRUKTURISASI'/ch.name).read_bytes()).hexdigest()==mapping['before_sha256'])
check('chapter_matches_transformation_manifest',hashlib.sha256(ch.read_bytes()).hexdigest()==mapping['after_sha256'])

def body(doc,title):return re.search(r'^\*\*Tabel 3\.\d+ '+re.escape(title)+r'\*\*\n\n(\|.*?)\n\n',doc,re.M|re.S).group(1)
for label,title in [('kf','Rancangan Kebutuhan Fungsional'),('us','Cerita Pengguna dan Kriteria Penerimaan'),('trace','Keterlacakan Kebutuhan sampai Evaluasi'),('uat','Rancangan Tugas Penerimaan Berdasarkan Kebutuhan')]:
 check(label+'_table_rows_preserved',body(old,title)==body(t,title))
old_citations={s for s in re.findall(r'\([^()\n]+\)',old) if re.search(r'\b(?:19|20)\d{2}\b|t\.t\.',s)}
check('existing_parenthetical_citations_preserved',all(s in t for s in old_citations),[s for s in old_citations if s not in t])
flow=(SUP/'gambar_proposal/Gambar_3_2_Alur_Pembuatan_Prototipe.svg').read_text(encoding='utf-8')
check('flow_has_current_procedure_labels',all('Prosedur '+x in flow for x in 'DEFGHIJ') and 'A sampai C' in flow)
check('flow_has_no_stale_subsection_labels',not re.search(r'3\.3\.[4-9]',flow))
images=re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)\n\n\*\*Gambar 3\.(\d+) ',t)
check('image_filename_numbers_match_captions',len(images)==10 and all(int(re.search(r'Gambar_3_(\d+)_',path)[1])==int(n) for path,n in images))
check('current_figures_use_separate_folder',all('/gambar_proposal/' in path for path,n in images))

old_table_numbers=sorted(int(x) for x in mapping['number_maps']['Tabel'])
check('all_twenty_previous_tables_retained',set(range(1,21))<=set(old_table_numbers))
check('implementation_responsibility_table_added','Pembagian Tanggung Jawab Implementasi ARTHA' in t)
check('all_ten_previous_figures_retained',len(mapping['figure_file_map'])==10)
check('five_section_source_index_present',len(json.loads((SUP/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))['sections'])==15)

report={
 'status':'passed' if all(checks.values()) else 'needs_correction',
 'scope':'Restructuring, source and diagram integrity, references, and cross-document consistency. No application tests, executed DDL, partner acceptance or final Word/PDF layout claimed.',
 'chapter':str(ch),'sha256':hashlib.sha256(ch.read_bytes()).hexdigest(),
 'main_sections':main,'numbered_sections':len(heads),'tables':21,'figures':10,
 'checks':checks,'passed':sum(checks.values()),'total':len(checks),'issues':issues,
 'upstream_results':{
   'chapter':str(SUP/'HASIL PEMERIKSAAN DRAF.json'),
   'integrated':str(ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25/HASIL VALIDASI TERPADU.json')},
 'open_items':['Kewenangan mitra dan rekening','Tarif, potongan serta kapasitas aktual','Peserta UAT dan kalender','Versi layanan dan inventaris perangkat','Tata letak akhir Word/PDF']}
result_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':report['passed'],'total':report['total'],'failed':[k for k,v in checks.items() if not v],'issues':issues},ensure_ascii=False))
assert all(checks.values()),issues
