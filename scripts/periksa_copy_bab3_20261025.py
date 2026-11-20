from pathlib import Path
import json,re,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25'
p=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md'
t=p.read_text(encoding='utf-8-sig')
paras=json.loads((OUT/'NASKAH_PER_PARAGRAF.json').read_text(encoding='utf-8'))
short=[];long=[];numeric=[];pronouns=[]
for row in paras:
 text=re.sub(r'\([^)]*\)','',row['text'])
 # Protect abbreviations so dkk. does not become an artificial sentence boundary.
 text=re.sub(r'\b(dkk|hlm|t\.t)\.',lambda m:m[0].replace('.','<DOT>'),text)
 sentences=[s.replace('<DOT>','.') for s in re.split(r'(?<=[.!?])\s+',text) if s.strip()]
 if len(sentences)<2:short.append(row)
 for s in sentences:
  if len(s.split())>40:long.append({**{k:row[k] for k in ['section','paragraph','line']},'words':len(s.split()),'sentence':s})
  if re.match(r'^\d',s):numeric.append(row)
 if re.search(r'\b(saya|kami|kita|penulis)\b',text,re.I):pronouns.append(row)
tables=re.findall(r'^\*\*Tabel 3\.(\d+) ([^\n]+)',t,re.M)
figures=re.findall(r'^\*\*Gambar 3\.(\d+) ([^\n]+)',t,re.M)
unmentioned=[]
for label,items in [('Tabel',tables),('Gambar',figures)]:
 for n,title in items:
  cap=t.index(f'**{label} 3.{n} ')
  if not re.search(re.escape(f'{label} 3.{n}')+r'(?!\d)',t[:cap]):unmentioned.append(f'{label} 3.{n}')
links=re.findall(r'!\[[^\]]*\]\(<([^>]+)>\)',t)
broken=[x for x in links if not Path(x).is_file()]
table_errors=[]
for block in re.split(r'\n\s*\n',t):
 if block.startswith('|'):
  if len({len(re.split(r'(?<!\\)\|',s)) for s in block.splitlines() if s.startswith('|')})>1:table_errors.append(block[:160])
ledger=json.loads((ROOT/'BAB3_PENDUKUNG_2026-10-25/PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))
meta=[{'id':s['id'],'author':s['author'],'file':s['file'],'year':int(re.findall(r'\d{4}',s['author'])[0])} for s in ledger['sources']]
dated_recent=sum(x['year']>=2016 for x in meta)
out={'scope':'Read-only document and local source checks, not full Word layout, implementation testing, or plagiarism-database matching',
 'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'prose_paragraphs':len(paras),'words':len(t.split()),
 'tables':len(tables),'figures':len(figures),'single_sentence_paragraphs':short,'sentences_over_40_words':long,
 'numeric_sentence_start':numeric,'first_person_prose':pronouns,'unmentioned_artifacts':unmentioned,
 'broken_image_links':broken,'table_column_errors':table_errors,'long_dash_prose':any(c in t for c in ['\u2014','\u2013']),
 'known_literature_sources':meta,'literature_since_2016':dated_recent,'known_literature_total':len(meta),
 'literature_recency_percent':round(dated_recent/len(meta)*100,2)}
(OUT/'HASIL PEMERIKSAAN STRUKTUR.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['sentences_over_40_words','known_literature_sources','single_sentence_paragraphs']},ensure_ascii=False))
print('LONG_SENTENCES',len(long))
for row in long:print(json.dumps(row,ensure_ascii=False))
