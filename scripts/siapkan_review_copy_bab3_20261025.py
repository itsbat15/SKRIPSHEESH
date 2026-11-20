from pathlib import Path
import json,re,hashlib
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25'
OUT.mkdir(parents=True,exist_ok=True)
paths={
 'panduan2025':ROOT/'PANDUAN TA/[2025] B PANDUAN KEPENULISAN TUGAS AKHIR ITK.pdf',
 'panduan2026':ROOT/'PANDUAN TA/Panduan TA dan SITASI - Sistem Informasi ITK 2026.pdf',
 'template':ROOT/'TEMPLATE TA/Copy of Template Laporan TA 2025 PROTOTIPE SI.docx.pdf'}
for key,p in paths.items():
 reader=PdfReader(p)
 pages=[{'pdf_page':i+1,'text':page.extract_text() or ''} for i,page in enumerate(reader.pages)]
 (OUT/(key+'_pages.json')).write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
 hits=[]
 pattern=r'TKT|70\s*%|sepuluh|10 tahun|5 tahun|lima tahun|3\.2|3\.5|3\.7|rubrik|Sangat Baik|prototipe|Prototipe|spasi|margin|Harvard|miring'
 for pg in pages:
  text=pg['text']
  if re.search(pattern,text):hits.append({'page':pg['pdf_page'],'start':text[:100].replace('\n',' ')})
 print(json.dumps({'document':key,'pages':len(pages),'hits':hits},ensure_ascii=False))
p=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (REVISI TEMPLATE TERBARU) copy.md'
t=p.read_text(encoding='utf-8-sig')
lines=t.splitlines();blocks=[];section='Pembuka';paragraph=0
for match in re.finditer(r'[^\n].*?(?=\n\s*\n|\Z)',t,re.S):
 block=match[0]
 if block.startswith('#'):
  section=block.replace('\n',' ');paragraph=0;continue
 if block.startswith(('|','!','**','Sumber:')):continue
 paragraph+=1
 blocks.append({'section':section,'paragraph':paragraph,'line':t.count('\n',0,match.start())+1,'text':block})
(OUT/'NASKAH_PER_PARAGRAF.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
meta={'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'lines':len(lines),'words':len(t.split()),'prose_paragraphs':len(blocks),'guides':{k:str(v) for k,v in paths.items()}}
(OUT/'LINGKUP PEMERIKSAAN.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(meta,ensure_ascii=False))
