from pathlib import Path
import urllib.request, hashlib, json, concurrent.futures
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'JURNAL/VERIFIKASI_ULANG_SINTA_BAB2_1_2026-10-27'
OUT.mkdir(exist_ok=True)
URLS={
 'SK_72_2024_I.pdf':'https://stikesnas.ac.id/source/Pengumuman_Pemberitahuan_Hasil_Akreditasi_Jurnal_Periode_I_Tahun_2024_dan_Lampiran_SK_No72_E_KPT_2024.pdf',
 'SK_21_2018_I.pdf':'https://drive.google.com/uc?export=download&id=1YnHXnH7auWp3LI70V08qLQ40Y9XZGFtg',
 'SK_225_2022_III.pdf':'https://drive.google.com/uc?export=download&id=1QBv-KIg9_6iI0ZgESxD7bM4nzR3b-p0o',
 'SK_177_2024_II.pdf':'https://lp2m.unsuda.ac.id/wp-content/uploads/2025/04/Pemberitahuan_Hasil_Akreditasi_Jurnal_Ilmiah_Periode_II_Tahun_2024.pdf',
 'SK_204_2022_II.pdf':'https://ejournal.undip.ac.id/public/fileAccrDecree/2022-II-Elektronik.pdf',
 'JATI_SK_177_SALINAN_ITS.pdf':'https://www.its.ac.id/ppi/wp-content/uploads/sites/148/2024/11/Pemberitahuan-Masa-Perpanjangan-Akreditasi-Jurnal-Ilmiah-2024.pdf',
 'INFOTEK_ABOUT.html':'https://e-journal.hamzanwadi.ac.id/index.php/infotek/about',
 'DJTECHNO_ABOUT.html':'https://jurnal.dharmawangsa.ac.id/index.php/djtechno/en',
 'MULTITEK_SINTA.html':'https://sinta.kemdiktisaintek.go.id/journals/google/3417',
 'JARING_SAINTEK_SINTA.html':'https://sinta.kemdiktisaintek.go.id/journals/profile/9505',
 'REPOSITOR_SINTA_DIRECTORY.html':'https://sinta.kemdiktisaintek.go.id/journals/index?page=1068'
}
def fetch(item):
 name,url=item
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read()
  if name.endswith('.pdf') and not data.startswith(b'%PDF'): raise ValueError('Bukan PDF')
  (OUT/name).write_bytes(data)
  return dict(file=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='downloaded')
 except Exception as e:return dict(file=name,url=url,status='failed',error=str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: manifest=list(ex.map(fetch,URLS.items()))
 (OUT/'MANIFEST_BUKTI.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
 paths=list(OUT.glob('*.pdf'))+list((ROOT/'JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/BUKTI_AKREDITASI').glob('*.pdf'))
 matches=[]
 terms=['multitek','repositor','jaring sain','infotek','2598828','27453758']
 for p in paths:
  doc=pdfium.PdfDocument(str(p))
  for i in range(len(doc)):
   page=doc[i];tp=page.get_textpage();s=tp.get_text_range();tp.close();page.close()
   if any(t in s.lower() for t in terms):
    matches.append(dict(file=str(p.relative_to(ROOT)),pdf_page=i+1,text=s))
  doc.close()
 (OUT/'HALAMAN_BUKTI.json').write_text(json.dumps(matches,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'downloads':manifest,'matches':[{'file':m['file'],'page':m['pdf_page']} for m in matches]},ensure_ascii=False))
