from pathlib import Path
import re,json,hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'BAB3_PENDUKUNG_2026-10-25'
chapter=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'
t=chapter.read_text(encoding='utf-8')
ledger=json.loads((OUT/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))
checks={}
main=re.findall(r'^## (3\.\d+) ',t,re.M)
checks['six_template_sections']=main==['3.1','3.2','3.3','3.4','3.5','3.6']
heads=re.findall(r'^#{2,3} (3(?:\.\d+){1,2}) ',t,re.M)
checks['all_sections_mapped']=set(heads)=={x['section'] for x in ledger['sections']}
checks['maximum_three_levels']=not bool(re.search(r'^#+ \d+\.\d+\.\d+\.',t,re.M))
checks['no_long_dash_prose']=not any(c in t for c in ['\u2014','\u2013'])
checks['no_sit_footnotes']='[^' not in t
checks['no_template_font_annotations']=not bool(re.search(r'\(\d+ pt',t))

short=[];long=[];pronouns=[];numeric=[]
for p in t.split('\n\n'):
    if not p.strip() or p.startswith(('#','|','!','**','Sumber:')): continue
    clean=re.sub(r'\([^)]*\)','',p)
    sentences=[s for s in re.split(r'(?<=[.!?])\s+',clean) if s.strip()]
    if len(sentences)<2: short.append(p)
    for s in sentences:
        if len(s.split())>40:long.append(s)
        if re.match(r'^\s*\d',s):numeric.append(s)
    if re.search(r'\b(?:saya|kami|kita|penulis)\b',clean,re.I):pronouns.append(p)
checks['paragraphs_at_least_two_sentences']=not short
checks['prose_sentences_max_40_words_excluding_citations']=not long
checks['no_numeric_sentence_start']=not numeric
checks['no_first_person_prose']=not pronouns

tables=re.findall(r'^\*\*Tabel 3\.(\d+) ',t,re.M)
figs=re.findall(r'^\*\*Gambar 3\.(\d+) ',t,re.M)
checks['sequential_20_tables']=[int(x) for x in tables]==list(range(1,21))
checks['sequential_ten_figures']=[int(x) for x in figs]==list(range(1,11))
for typ,ids in [('Tabel',tables),('Gambar',figs)]:
    checks[typ+'_all_mentioned_before_caption']=all(t.index(f'{typ} 3.{i}')<t.index(f'**{typ} 3.{i} ') for i in ids)

broken=[]
for p in [chapter,*OUT.glob('*.md')]:
    for s in re.findall(r'\]\(<([^>]+)>\)',p.read_text(encoding='utf-8')):
        if re.match(r'^[A-Za-z]:/',s):
            path=Path(re.sub(r':\d+$','',s))
            if not path.exists():broken.append(dict(file=str(p),target=s))
checks['all_local_links_resolve']=not broken
for source in ledger['sources']:
    assert hashlib.sha256(Path(source['file']).read_bytes()).hexdigest()==source['sha256'],source['id']
checks['source_files_hash_verified']=True

cited_keys=[('Dzhurov','2009'),('Fikri','2021'),('Sidiq','2025'),('Apriyanti','2024'),('Ahadi','2025'),('Thiovanda','2026'),('Hendri','2025'),('Sudirman','2021'),('Ramadhan','2026'),('Khafidhoh','2026'),('Kabisatullah','2026'),('Fajriansyah','2026'),('Gunawan','2025')]
bib=(OUT/'DAFTAR PUSTAKA BAB 3.md').read_text(encoding='utf-8')
checks['journal_and_proceedings_citations_have_entries']=all(name in t and name in bib and year in bib for name,year in cited_keys)
checks['nonjournal_citations_have_entries']=all(x in t and x in bib for x in ['2025a','2025b','t.t.-a','t.t.-b','t.t.-c','Vercel','WhatsApp'])
checks['no_false_test_results']='| Valid |' not in t and '| Sukses |' not in t and t.count('Belum diuji')>=6
checks['twenty_editable_and_raster_figure_files']=len(list((OUT/'gambar').glob('*.png')))==10 and len(list((OUT/'gambar').glob('*.svg')))==10

table_errors=[]
for block in t.split('\n\n'):
    if not block.startswith('|'):continue
    counts=[len(re.split(r'(?<!\\)\|',line)) for line in block.splitlines() if line.startswith('|')]
    if len(set(counts))>1:table_errors.append(block[:120])
checks['consistent_markdown_table_columns']=not table_errors

manifest={
 'date':'2026-10-25','scope':'Structural, citation-index, file-integrity, prose-shape and local-link checks; not a claim of final Word layout or implementation validation',
 'chapter':str(chapter),'chapter_sha256':hashlib.sha256(chapter.read_bytes()).hexdigest(),
 'word_count_including_tables':len(t.split()),'main_sections':len(main),'mapped_sections_and_subsections':len(heads),
 'tables':len(tables),'figures':len(figs),'journal_articles':12,'original_method_proceedings':1,'bibliography_entries':21,
 'checks':checks,'issues':dict(short_paragraphs=short,long_sentences=long,first_person=pronouns,numeric_start=numeric,broken_links=broken,table_column_errors=table_errors),
 'open_items':['actual hardware specifications','final software versions','UAT participants and instrument validation','calendar schedule','partner approval of payment authorities and capacity parameters','remaining reference metadata and accreditation coverage','final Word/PDF layout']
}
(OUT/'HASIL PEMERIKSAAN DRAF.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(words=manifest['word_count_including_tables'],checks_passed=sum(checks.values()),checks_total=len(checks),failures=[k for k,v in checks.items() if not v]),ensure_ascii=True))
assert all(checks.values()),manifest['issues']
