from pathlib import Path
import json,re,hashlib
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'JURNAL/AUDIT_SITASI_BAB1_2026-10-25'
cached=json.loads((OUT/'SUMBER_DAN_TEKS_HALAMAN.json').read_text(encoding='utf-8'))
cache={str(Path(x['file'])):x['pages'] for x in cached}
def words(t): return re.findall(r'[^\W_]+',t.lower(),re.UNICODE)
drafts={n:(ROOT/n).read_text(encoding='utf-8') for n in ['BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md','BAB_2_TINJAUAN_PUSTAKA.md']}
grams={}
for name,txt in drafts.items():
    for ln,line in enumerate(txt.splitlines(),1):
        if not line or line.startswith(('#','|','```','+')): continue
        ww=words(line)
        for i in range(len(ww)-11): grams.setdefault(tuple(ww[i:i+12]),[]).append((name,ln))
inventory=[];hits=[];extra=[]
for file in sorted((ROOT/'JURNAL').rglob('*.pdf')):
    if 'BUKTI_AKREDITASI' in file.parts: continue
    key=str(file)
    if key in cache: pages=cache[key]
    else:
        try:
            doc=pdfium.PdfDocument(str(file));pages=[]
            for i in range(len(doc)):
                p=doc[i];tp=p.get_textpage(); t=tp.get_text_range();tp.close();p.close()
                pages.append(dict(pdf_page=i+1,text=t))
            doc.close()
            extra.append(dict(file=key,pages=pages))
        except Exception as e:
            inventory.append(dict(file=key,error=str(e)));continue
    inventory.append(dict(file=key,pages=len(pages),first_page=pages[0]['text'][:4500],sha256=hashlib.sha256(file.read_bytes()).hexdigest()))
    seen=set()
    for page in pages:
        ww=words(page['text'])
        for i in range(len(ww)-11):
            g=tuple(ww[i:i+12])
            for name,ln in grams.get(g,[]):
                sig=(name,ln,key,page['pdf_page'])
                if sig in seen: continue
                seen.add(sig)
                hits.append(dict(draft=name,line=ln,source=key,pdf_page=page['pdf_page'],matched_12_words=' '.join(g)))
(OUT/'INSPEKSI_KORPUS_DAN_KEMIRIPAN_LOKAL.json').write_text(json.dumps(dict(method='Exact 12 consecutive normalized words; not a plagiarism detector; native text only, no new OCR',inventory=inventory,hits=hits),ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'TEKS_SUMBER_TAMBAHAN_BAB2.json').write_text(json.dumps(extra,ensure_ascii=False),encoding='utf-8')
print(json.dumps(dict(pdf_count=len(inventory),additional_texts=len(extra),local_matches=len(hits),matches=hits),ensure_ascii=True))
