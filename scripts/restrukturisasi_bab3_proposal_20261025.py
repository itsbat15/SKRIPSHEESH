"""Reorder authorised chapter blocks around the pre-seminar proposal structure."""
from pathlib import Path
import re,json,hashlib,shutil

ROOT=Path(__file__).resolve().parents[1]
SUP=ROOT/'BAB3_PENDUKUNG_2026-10-25'
OUT=SUP/'RESTRUKTURISASI_PROPOSAL_2026-10-25'
BACK=OUT/'SEBELUM_RESTRUKTURISASI'
CH=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'
REFERENCE=ROOT/'REFERENSI TA PXP/PROP. SEBELUM SEMPRO/Proposal-TA-10231008.md'
BACK.mkdir(parents=True,exist_ok=True)
for p in [CH,SUP/'PETA_SUMBER_DAN_SUBBAB.json',SUP/'CHECKLIST JURNAL UNTUK SETIAP SUBBAB BAB 3.md',SUP/'CATATAN PENYUSUNAN DAN PEMERIKSAAN BAB 3.md',SUP/'HASIL PEMERIKSAAN DRAF.json']:
    if not (BACK/p.name).exists():shutil.copy2(p,BACK/p.name)
old=(BACK/CH.name).read_text(encoding='utf-8')
ledger=json.loads((BACK/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))
headers=list(re.finditer(r'^#{2,3} (3(?:\.\d+){1,2}) ([^\n]+)\n',old,re.M))
blocks={m[1]:old[m.end():headers[i+1].start() if i+1<len(headers) else len(old)].strip() for i,m in enumerate(headers)}
assert len(blocks)==29
def h(level,code,title,body):return '#'*level+' '+code+' '+title+'\n\n'+body.strip()+'\n\n'
def b(title,body):return '**'+title+'**\n\n'+body.strip()+'\n\n'

arch=blocks['3.5.1']
sep='Autentikasi direncanakan menggunakan fasilitas Laravel Sanctum'
assert sep in arch
arch_concept,arch_technical=arch.split(sep,1)
arch_technical=sep+arch_technical
stage=blocks['3.2']
table_at=stage.index('Tabel 3.1 merangkum')
stage_table=stage[table_at:]
flow=stage[:table_at]
deployment_tail='Setelah tindak lanjut, pengembang menyiapkan versi serah uji'
uat=blocks['3.3.8']
assert deployment_tail in uat
uat,serah=uat.split(deployment_tail,1)
serah=deployment_tail+serah

intro='''# BAB 3
# DESAIN DAN IMPLEMENTASI

Bab ini menjelaskan konsep desain, spesifikasi teknis, tahapan pembuatan prototipe, metode implementasi, dan jadwal pengembangan sistem informasi manajemen operasional ARTHA. Perancangan serta evaluasi disiapkan sebagai bagian laporan tugas akhir jalur prototipe (Institut Teknologi Kalimantan, 2025b), dengan prosedur yang disesuaikan untuk pengembangan individual menggunakan PxP.

'''
text=intro
text+=h(2,'3.1','Konsep Desain',blocks['3.1'])
text+=h(3,'3.1.1','Pengguna dan Ruang Lingkup Sistem',blocks['3.1.1']+'\n\n'+blocks['3.1.2'])
text+=h(3,'3.1.2','Konsep Proses Operasional',blocks['3.4.1'])
text+=h(3,'3.1.3','Rancangan Arsitektur Sistem',arch_concept)
text+=h(3,'3.1.4','Luaran Prototipe',blocks['3.1.4'])
text+=h(2,'3.2','Spesifikasi Teknis',blocks['3.5'])
text+=h(3,'3.2.1','Spesifikasi Teknis Perangkat Lunak',blocks['3.5.3'])
text+=h(3,'3.2.2','Spesifikasi Teknis Perangkat Keras',blocks['3.5.2'])
text+=h(3,'3.2.3','Lingkungan Pengembangan dan Pengujian',blocks['3.5.4'])
text+=h(2,'3.3','Tahapan Pembuatan Prototipe','''Tahapan penelitian mencakup identifikasi masalah, studi literatur, pengembangan perangkat lunak, serta evaluasi dan penyiapan prototipe. Pengembangan perangkat lunak mengikuti siklus PxP, sedangkan pengumpulan bukti kebutuhan dan penerimaan pengguna mendukung penetapan serta pemeriksaan rancangan.''')
overview=blocks['3.1.3']+'''

Penelitian diawali dengan penelaahan permasalahan administrasi dari wawancara dan pemilihan literatur yang relevan. Kebutuhan kemudian dijabarkan menjadi cerita pengguna, rencana iterasi, rancangan proses dan data, serta kasus pengujian.

Pada setiap iterasi, tugas dipilih, dirancang, diimplementasikan, dan diuji sebelum hasil proses dievaluasi. Setelah fungsi terintegrasi memenuhi pemeriksaan awal, perwakilan pengguna menjalankan UAT dan memberikan masukan untuk perbaikan atau penyiapan versi serah uji.

'''+stage_table
text+=h(3,'3.3.1','Garis Besar Penelitian',overview)
text+=h(3,'3.3.2','Diagram Alir Penelitian',flow)
procedure='''Prosedur penelitian menjabarkan kegiatan pada diagram alir menjadi langkah yang dapat dilaksanakan dan ditelusuri. Tahapan berikut menggunakan penanda huruf agar rincian tetap berada dalam Subbab 3.3.3, sedangkan kebutuhan, rancangan, serta pengujian dihubungkan melalui kode yang sama.

'''
procedure+=b('A. Identifikasi Masalah','''Identifikasi masalah dilakukan dengan menelaah transkrip wawancara pengelola serta staf administrasi Bimbel Artha. Informasi dikelompokkan menurut pencatatan siswa, variasi tarif, pembayaran, penempatan kelas, jadwal tentor, dan kebutuhan pemantauan pusat.

Hasil penelaahan berupa hubungan antara proses berjalan, kendala yang dinyatakan narasumber, dan fungsi yang perlu dirancang. Peristiwa yang belum didukung bukti dicatat sebagai risiko yang perlu diperiksa, sedangkan perbedaan keterangan antarcabang diarahkan ke klarifikasi mitra.''')
procedure+=b('B. Studi Literatur','''Studi literatur digunakan untuk mempelajari PxP, sistem administrasi bimbel, pengelolaan multicabang, penjadwalan, serta pencatatan penerimaan. Sumber dipilih menurut kesesuaian isi, bagian yang dapat dirujuk, dan hubungan dengan kebutuhan pengembangan ARTHA.

Sumber asli Dzhurov dkk. (2009, hlm. 253 sampai 256) digunakan untuk tahapan PxP, sedangkan penelitian Fikri dan Arthawan Sugih Prabowo (2021, hlm. 103 sampai 105) menjadi pembanding penerapannya. Literatur evaluasi digunakan untuk menyusun pengujian fungsi dan keterlibatan pengguna, dengan instrumen yang disesuaikan terhadap tugas administrasi ARTHA.''')
procedure+=b('C. Penggalian Kebutuhan (*Requirements*)',blocks['3.3.1'])
procedure+=b('Kebutuhan fungsional dan nonfungsional',blocks['3.4.2'])
procedure+=b('Aktor dan kewenangan pengguna',blocks['3.4.3'])
procedure+=b('Cerita pengguna dan keterlacakan',blocks['3.4.4'])
procedure+=b('D. Perencanaan (*Planning*)',blocks['3.3.2'])
procedure+=b('E. Inisialisasi Iterasi (*Iteration Initialization*)',blocks['3.3.3'])
procedure+=b('F. Perancangan (*Design*)',blocks['3.3.4'])
procedure+=b('Pemodelan kasus penggunaan dan skenario',blocks['3.4.5'])
procedure+=b('Perancangan basis data',blocks['3.4.6'])
procedure+=b('Perancangan antarmuka',blocks['3.4.7'])
procedure+=b('G. Implementasi (*Implementation*)',blocks['3.3.5'])
procedure+=b('H. Pengujian Sistem (*System Testing*)',blocks['3.3.6'])
procedure+=b('I. Evaluasi Iterasi (*Retrospective*)',blocks['3.3.7'])
procedure+=b('J. Pengujian Penerimaan Pengguna dan Analisis Evaluasi',uat)
procedure+=b('K. Penyiapan dan Penyerahan Prototipe (*Deployment*)','''Penyiapan prototipe dilakukan pada lingkungan uji yang telah diperiksa sesuai spesifikasi pada Subbab 3.2.3. Konfigurasi, basis data, penyimpanan bukti, data simulasi, dan akun menurut peran disiapkan sebelum versi diserahkan untuk evaluasi mitra.

'''+serah+'''

Versi yang diserahkan dicatat bersama hasil pemeriksaan awal, panduan penggunaan, serta daftar keterbatasan. Pencadangan dan pemulihan diperiksa pada lingkungan terpisah, kemudian berita acara evaluasi digunakan untuk mencatat penerimaan serta pekerjaan yang masih perlu ditindaklanjuti.''')
text+=h(3,'3.3.3','Prosedur Penelitian',procedure)

implementation='''Metode implementasi menjelaskan cara mewujudkan konsep desain ARTHA melalui antarmuka web, layanan pengolahan data, dan penyimpanan terpusat. Urutan pekerjaan pengembang mengikuti PxP pada Subbab 3.3, sedangkan bagian ini menjelaskan hubungan komponen serta penerapan aturan pada aplikasi.

Antarmuka Next.js mengirim permintaan ke layanan Laravel setelah pengguna mengisi formulir atau memilih tindakan. Layanan memeriksa sesi, peran, dan objek cabang sebelum membaca atau mengubah data pada MySQL, kemudian mengembalikan hasil yang dapat ditampilkan antarmuka.

Tabel 3.21 merangkum tanggung jawab komponen agar validasi tampilan tidak menggantikan pemeriksaan peladen. Berkas bukti dipisahkan dari akses publik dan hanya disajikan setelah kewenangan pengguna diperiksa.

**Tabel 3.21 Pembagian Tanggung Jawab Implementasi ARTHA**

| Komponen | Tanggung jawab | Contoh penerapan |
| :--- | :--- | :--- |
| Antarmuka web | Menyajikan data, memeriksa kelengkapan awal, dan menjelaskan hasil tindakan | Formulir siswa, indikator kapasitas, pratinjau WhatsApp, dan daftar pengajuan |
| Layanan aplikasi | Memeriksa kewenangan objek dan menjalankan aturan bisnis | Akses cabang, alokasi tagihan, penempatan siswa, dan pemeriksaan transfer |
| Basis data | Menyimpan hubungan, riwayat, kunci unik, serta perubahan dalam transaksi | Keanggotaan aktif, keputusan pemeriksaan tunggal, dan referensi bank yang tidak dipakai ganda |
| Penyimpanan berkas privat | Menyimpan bukti dengan rujukan dan akses yang terkendali | Bukti transfer dan dokumen pemeriksaan yang diizinkan |
| Proses di luar aplikasi | Menjalankan tindakan yang tidak diintegrasikan otomatis | Admin mengirim pesan melalui WhatsApp; petugas memeriksa mutasi resmi |

'''+arch_technical+'''

Pada penempatan siswa, layanan menghitung ulang peserta aktif dan memeriksa kapasitas dalam transaksi penyimpanan yang sama. Pada persetujuan transfer, status pengajuan, alokasi tagihan, referensi dana masuk, keputusan, dan kuitansi diperiksa serta disimpan secara utuh agar permintaan berulang tidak menghasilkan penerimaan ganda.

Pencatatan tunai, penyerahan kas ke pusat, setoran bank, dan pencocokan menggunakan objek yang berbeda tetapi tetap merujuk transaksi sumber. Rekap penerimaan dihitung dari pembayaran sah, sedangkan setoran serta pencocokan tidak dijumlahkan sebagai pendapatan siswa yang baru.

Integrasi diuji bertahap menurut ketergantungan setiap iterasi dan kasus pengujian yang telah disiapkan. Versi kode, konfigurasi yang dapat didokumentasikan, perubahan skema, serta bukti uji disimpan agar hasil implementasi dapat ditelusuri kembali ke kebutuhan.'''
text+=h(2,'3.4','Metode Implementasi',implementation)
text+=h(2,'3.5','Jadwal Pembuatan Prototipe',blocks['3.6'])

# Replace only explicit section references, not citation page numbers or identifiers.
refs={
 'Rincian pelaksanaannya dijelaskan pada Subbab 3.3':'Rincian pelaksanaannya dijelaskan pada Subbab 3.3.3',
 'pada Subbab 3.6':'pada Subbab 3.5',
 'sebagaimana pada Subbab 3.6':'sebagaimana pada Subbab 3.5'}
for before,after in refs.items():text=text.replace(before,after)
text=text.replace('Tahapan pembuatan disusun sebagai alur kerja dari penggalian kebutuhan sampai penyiapan luaran.',
 'Diagram alir menggambarkan hubungan antara penyiapan kebutuhan, pengembangan iteratif, dan evaluasi prototipe.')
text=text.replace('Tabel 3.1 merangkum kegiatan dan luaran setiap tahap pada Gambar 3.1.',
 'Tabel 3.1 merangkum kegiatan dan luaran yang menjadi dasar diagram alir pada Subbab 3.3.2.')

# Caption order determines new numbers. Preserve a mapping for audits and companion tools.
maps={}
for kind in ['Tabel','Gambar']:
 ids=[int(x) for x in re.findall(r'^\*\*'+kind+r' 3\.(\d+) ',text,re.M)]
 assert len(ids)==len(set(ids)),(kind,ids)
 mapping={str(old):str(i) for i,old in enumerate(ids,1)}
 maps[kind]=mapping
 text=re.sub(kind+r' 3\.(\d+)\b',lambda m:kind+' 3.'+mapping[m[1]],text)

# Every image moves to a new asset folder; previous asset versions remain available.
old_to_new={
 'Gambar_3_10_Arsitektur_Prototipe':'Gambar_3_1_Arsitektur_Prototipe',
 'Gambar_3_1_Alur_Pembuatan_Prototipe':'Gambar_3_2_Alur_Pembuatan_Prototipe',
 'Gambar_3_2_Use_Case_Inti':'Gambar_3_3_Use_Case_Inti',
 'Gambar_3_3_Model_Data_Konseptual':'Gambar_3_4_Model_Data_Konseptual',
 'Gambar_3_4_Dasbor_Cabang':'Gambar_3_5_Dasbor_Cabang',
 'Gambar_3_5_Keanggotaan_Kelas':'Gambar_3_6_Keanggotaan_Kelas',
 'Gambar_3_6_Pengajuan_Transfer':'Gambar_3_7_Pengajuan_Transfer',
 'Gambar_3_7_Pemeriksaan_Transfer':'Gambar_3_8_Pemeriksaan_Transfer',
 'Gambar_3_8_Tunggakan_WhatsApp':'Gambar_3_9_Tunggakan_WhatsApp',
 'Gambar_3_9_Dasbor_Pusat_Pencocokan':'Gambar_3_10_Dasbor_Pusat_Pencocokan'}
text=re.sub(r'/gambar/(Gambar_[^/>]+)\.png',lambda m:'/gambar_proposal/'+old_to_new[m[1]]+'.png',text)
CH.write_text(text.rstrip()+'\n',encoding='utf-8')

# Bind source IDs to the actual new sections, preserving original PDF hashes and page locators.
by_old={x['section']:x for x in ledger['sections']}
section_map={
 '3.1':['3.1'], '3.1.1':['3.1.1','3.1.2'], '3.1.2':['3.4.1'],
 '3.1.3':['3.5.1'], '3.1.4':['3.1.4'], '3.2':['3.5'],
 '3.2.1':['3.5.3'], '3.2.2':['3.5.2'], '3.2.3':['3.5.4'],
 '3.3':['3.3'], '3.3.1':['3.1.3','3.2'], '3.3.2':['3.2'],
 '3.3.3':['3.3.1','3.3.2','3.3.3','3.3.4','3.3.5','3.3.6','3.3.7','3.3.8','3.4.2','3.4.3','3.4.4','3.4.5','3.4.6','3.4.7'],
 '3.4':['3.5.1'], '3.5':['3.6']}
ledger['sections']=[{'section':new,'sources':sorted(set(s for old_key in old_keys for s in by_old[old_key]['sources'])),
 'boundary':'Sumber dan batas penggunaannya dipertahankan dari bagian asal; fakta operasional serta keputusan mitra tidak ditetapkan oleh contoh proposal.',
 'previous_sections':old_keys} for new,old_keys in section_map.items()]
ledger['revision']='2026-10-25: five main sections following the supplied pre-seminar proposal; PxP and UAT retained'
ledger['structure_reference']={'file':str(REFERENCE),'sha256':hashlib.sha256(REFERENCE.read_bytes()).hexdigest(),'role':'Structural reference only; not evidence of ARTHA policies or a replacement for PxP sources'}
(SUP/'PETA_SUMBER_DAN_SUBBAB.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={
 'scope':'Authorised chapter reordering and transitions; unchanged operational design and bibliography',
 'source':str(CH),'before_sha256':hashlib.sha256((BACK/CH.name).read_bytes()).hexdigest(),
 'after_sha256':hashlib.sha256(CH.read_bytes()).hexdigest(),
 'reference':str(REFERENCE),'number_maps':maps,'figure_file_map':old_to_new,'section_map':section_map,
 'original_block_hashes':{k:hashlib.sha256(v.encode()).hexdigest() for k,v in blocks.items()},
 'unchanged_design_files':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'DOKUMEN MD/PERANCANGAN USE CASE & SKENARIO.md',ROOT/'DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md']}}
(OUT/'PETA RESTRUKTURISASI.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')

# Build the revised figures from the original, editable drawing source.
src=(ROOT/'scripts/gambar_revisi_terpadu_20261025.py').read_text(encoding='utf-8')
src=src.replace("OUT = ROOT / 'BAB3_PENDUKUNG_2026-10-25/gambar'","OUT = ROOT / 'BAB3_PENDUKUNG_2026-10-25/gambar_proposal'")
src=src.replace("BACK = ROOT / 'DOKUMEN MD/REVISI_TERPADU_2026-10-25/SEBELUM_REVISI/gambar'","BACK = ROOT / 'BAB3_PENDUKUNG_2026-10-25/RESTRUKTURISASI_PROPOSAL_2026-10-25/SEBELUM_RESTRUKTURISASI/gambar_proposal'")
src=re.sub(r"Gambar_3_\d+_[A-Za-z_]+",lambda m:old_to_new.get(m[0],m[0]),src)
for i,letter in enumerate('CDEFGHIJ',1):
    src=src.replace('(3.3.'+str(i)+')','(Prosedur '+letter+')')
src=src.replace('Tes, kode, refaktorisasi (3.3.5)','Tes, kode, refaktorisasi (G)')
src=src.replace('Penggalian kebutuhan dan studi literatur\\n(Prosedur C)',
 'Identifikasi masalah dan studi literatur\\nPenggalian kebutuhan (A sampai C)')
src=src.replace("proof=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'", "proof=ROOT/'BAB3_PENDUKUNG_2026-10-25/RESTRUKTURISASI_PROPOSAL_2026-10-25'")
# The historic generator removes old names; this new directory needs no deletion.
src=src.split("# Remove only this script's seven superseded figure names",1)[0]+"print(json.dumps({'figures':len(names),'directory':str(OUT)},ensure_ascii=False))\n"
(ROOT/'scripts/gambar_bab3_struktur_proposal_20261025.py').write_text(src,encoding='utf-8')
print(json.dumps({'words':len(text.split()),'main_sections':5,'tables':len(maps['Tabel']),'figures':len(maps['Gambar']),'table_map':maps['Tabel']},ensure_ascii=False))
