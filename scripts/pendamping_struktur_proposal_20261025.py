from pathlib import Path
import json,re,shutil

ROOT=Path(__file__).resolve().parents[1]
SUP=ROOT/'BAB3_PENDUKUNG_2026-10-25'
OUT=SUP/'RESTRUKTURISASI_PROPOSAL_2026-10-25'
BACK=OUT/'SEBELUM_RESTRUKTURISASI'
LEDGER=json.loads((SUP/'PETA_SUMBER_DAN_SUBBAB.json').read_text(encoding='utf-8'))
CH=ROOT/'BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md'
mapping=json.loads((OUT/'PETA RESTRUKTURISASI.json').read_text(encoding='utf-8'))
headings=dict(re.findall(r'^#{2,3} (3(?:\.\d+){1,2}) ([^\n]+)',CH.read_text(encoding='utf-8'),re.M))
def link(p,label):return f'[{label}](<{p.as_posix()}>)'
def backup(p):
    b=BACK/'PENDAMPING'/p.name;b.parent.mkdir(parents=True,exist_ok=True)
    if not b.exists():shutil.copy2(p,b)

checklist=(BACK/'CHECKLIST JURNAL UNTUK SETIAP SUBBAB BAB 3.md').read_text(encoding='utf-8')
prefix=checklist.split('## 2. Checklist setiap subbab',1)[0]
suffix=checklist.split('## 3. Bukti sumber dan halaman',1)[1]
for i in range(1,14):
    source_id=f'J{i:02}'
    start=suffix.index('### '+source_id+'.')
    end=suffix.find('\n### J',start+1)
    if end<0:end=suffix.find('\n## 4.',start)
    block=suffix[start:end]
    newrefs=', '.join(row['section'] for row in LEDGER['sections'] if source_id in row['sources'])
    block=re.sub(r'- Subbab terkait: [^\n]+','- Subbab terkait: '+newrefs+'.',block)
    suffix=suffix[:start]+block+suffix[end:]
rows=[]
for row in LEDGER['sections']:
    k=row['section'];sources=' '.join(row['sources']) or 'Data primer atau panduan'
    boundary={
     '3.1.4':'Luaran mengikuti panduan; bukti pencapaian dilaporkan setelah pelaksanaan.',
     '3.2.2':'Spesifikasi aktual memerlukan inventaris perangkat, bukan angka dari jurnal.',
     '3.2.1':'Versi antarmuka tersedia dari lockfile; versi layanan serta kompatibilitas perlu ditetapkan.',
     '3.3.3':'Bagian A sampai K memuat prosedur, kebutuhan, model, antarmuka, pengujian, serta penyerahan.',
     '3.3.2':'Diagram diadaptasi untuk PxP dan evaluasi ARTHA; bukan diagram metode teman yang disalin.',
     '3.4':'Integrasi dan aturan bisnis merupakan rancangan ARTHA; penggunaan teknis mengikuti dokumentasi resmi.',
     '3.5':'Empat iterasi dan dua belas minggu adalah usulan; tanggal kalender belum ditetapkan.'
    }.get(k,'Isi jurnal menjadi pembanding; fakta dan parameter ARTHA tetap memerlukan bukti mitra.')
    status='[ ] Pelengkapan primer diperlukan.' if k in ['3.1.4','3.2.2'] else '[x] Landasan tersedia.'
    rows.append(f'| {k} {headings[k]} | {sources} | {status} {boundary} |')
section='''## 2. Checklist setiap subbab setelah restrukturisasi

Pemetaan berikut mengikuti lima subbab utama yang dipilih pengguna berdasarkan proposal sebelum sempro. Penyesuaian susunan tidak mengubah metadata, lokator halaman, atau batas bukti akreditasi yang dicatat sebelumnya.

| Subbab | Sumber yang dapat digunakan | Status dan batas penggunaan |
| :--- | :--- | :--- |
'''+ '\n'.join(rows)+'''

Rincian prosedur pada Subbab 3.3.3 dibedakan menggunakan penanda huruf, bukan tingkat penomoran keempat. Landasan PxP tetap mencakup inisialisasi iterasi dan evaluasi iterasi, sedangkan evaluasi pengguna menggunakan UAT berbasis tugas.

## 3. Bukti sumber dan halaman'''+suffix
(SUP/'CHECKLIST JURNAL UNTUK SETIAP SUBBAB BAB 3.md').write_text(prefix+section,encoding='utf-8')

note='''# Catatan Bab 3 setelah penyesuaian struktur proposal sebelum sempro

Bab 3 telah disusun ulang sesuai arahan pengguna dengan lima subbab utama pada proposal pembanding sebelum sempro. Isi pengembangan tetap mengikuti PxP dan kebutuhan ARTHA, dengan dokumentasi rancangan yang telah diperiksa sebelumnya sebagai dasar.

## 1. Susunan yang digunakan

Bagian utama terdiri atas Konsep Desain, Spesifikasi Teknis, Tahapan Pembuatan Prototipe, Metode Implementasi, dan Jadwal Pembuatan Prototipe. Bab diberi judul Desain dan Implementasi, sedangkan nama berkas tetap dipertahankan agar tautan dokumen sebelumnya tetap dapat digunakan.

Subbab 3.3 mempunyai garis besar penelitian, diagram alir, dan prosedur penelitian. Rincian prosedur A sampai K memuat identifikasi, literatur, tujuh tahapan PxP, UAT, serta penyiapan dan penyerahan prototipe.

## 2. Perancangan yang dipertahankan

Kebutuhan dan cerita pengguna berada pada bagian penggalian kebutuhan, sedangkan use case, basis data, dan antarmuka berada pada bagian perancangan. Dua peran, WhatsApp manual, kelas penuh, pengajuan transfer, alokasi, serta pencocokan bank tetap memakai aturan rancangan yang sama.

Use case tetap berjumlah empat belas dan skema tetap mempunyai dua puluh tiga tabel. Bab 3 memuat dua puluh satu tabel dan sepuluh gambar, termasuk enam antarmuka dengan data simulasi.

## 3. Batas pemeriksaan

Pemeriksaan mencakup struktur, pemetaan kebutuhan, sitasi yang dipertahankan, nomor artefak, tautan, dan gambar. Pemeriksaan tersebut bukan eksekusi SQL, pengujian aplikasi, UAT, atau pemeriksaan tata letak Word/PDF akhir.

Kewenangan rekening, tarif, potongan, kapasitas aktual, peserta UAT, perangkat, serta kalender tetap perlu dilengkapi atau divalidasi. Bab 1 dan Bab 2 belum diubah dalam restrukturisasi ini, sedangkan pemetaan sumber jurnal telah mengikuti nomor bagian yang baru.

## 4. Berkas rujukan revisi

Rincian perpindahan bagian dan pemeriksaan tersedia pada laporan restrukturisasi. Salinan naskah sebelum perubahan tersimpan bersama peta pemindahan agar dapat dibandingkan kembali.

REPORT_LINK
'''
note=note.replace('REPORT_LINK',link(OUT/'LAPORAN PENYESUAIAN STRUKTUR BAB 3.md','Laporan penyesuaian struktur Bab 3')+'.')
(SUP/'CATATAN PENYUSUNAN DAN PEMERIKSAAN BAB 3.md').write_text(note,encoding='utf-8')

# Update companion table locators, while preserving the unchanged requirement identifiers.
p=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25/MATRIKS KETERLACAKAN KEBUTUHAN.md'
backup(p)
t=(BACK/'PENDAMPING'/p.name).read_text(encoding='utf-8')
t=re.sub(r'Tabel 3\.(\d+)\b',lambda m:'Tabel 3.'+mapping['number_maps']['Tabel'][m[1]],t)
p.write_text(t,encoding='utf-8')

report='''# Penyesuaian struktur Bab 3 berdasarkan proposal sebelum sempro

Restrukturisasi mengikuti arahan pengguna untuk memakai kerangka lima subbab pada Proposal-TA-10231008.md sebagai referensi saat menyiapkan proposal ARTHA. Isi penelitian tetap disesuaikan dengan pengembangan web, metode PxP, dua peran pengguna, dan evaluasi UAT yang telah dirancang.

## 1. Berkas hasil

Naskah diperbarui langsung pada lokasi semula dengan judul bab Desain dan Implementasi. Nama berkas tidak diganti agar rujukan dari dokumen pendamping tetap berlaku.

CHAPTER_LINK

## 2. Susunan baru dan asal isinya

| Bagian baru | Isi utama | Bagian asal pada draf sebelumnya |
| :--- | :--- | :--- |
| 3.1 Konsep Desain | Produk, pengguna, proses operasional, arsitektur, serta luaran | 3.1, 3.4.1, dan konsep arsitektur pada 3.5.1 |
| 3.2 Spesifikasi Teknis | Perangkat lunak, perangkat keras, lingkungan pengembangan dan pengujian | 3.5.2 sampai 3.5.4 |
| 3.3 Tahapan Pembuatan Prototipe | Garis besar, diagram alir, serta prosedur penelitian | 3.1.3, 3.2, 3.3, serta 3.4.2 sampai 3.4.7 |
| 3.4 Metode Implementasi | Integrasi antarmuka, layanan, data, berkas, serta penerapan aturan bisnis | Rincian teknis 3.5.1 dan penjelasan integrasi yang disesuaikan |
| 3.5 Jadwal Pembuatan Prototipe | Empat iterasi dan dua belas minggu relatif | 3.6 |

Subbab 3.3 mengikuti pola garis besar penelitian, diagram alir, dan prosedur seperti contoh sebelum sempro. Prosedur memakai penanda A sampai K agar rincian tidak menjadi penomoran empat tingkat.

## 3. Penyesuaian terhadap penelitian ARTHA

Tahapan inisialisasi dan evaluasi iterasi tetap dicantumkan karena pengembangan ARTHA menggunakan PxP. UAT berbasis tugas tetap digunakan, sedangkan metode XP, teknologi mobile, layanan push, serta SUS pada proposal pembanding tidak diadopsi ke rancangan ini.

Kebutuhan, kewenangan, cerita pengguna, serta keterlacakan diletakkan dalam penggalian kebutuhan. Use case, basis data, dan enam antarmuka ditempatkan pada perancangan; cara integrasi komponen dijelaskan pada metode implementasi agar tidak hanya mengulang urutan pengembangan.

Rancangan operasional tetap mempunyai empat belas kebutuhan, empat belas use case, dua puluh tiga tabel, tiga puluh tiga kasus uji, dan empat belas tugas UAT. Dokumen use case serta skema tidak diubah pada pekerjaan ini, dan hash keduanya dibandingkan untuk memeriksa keutuhan.

## 4. Penomoran dan dokumen pendamping

Tabel dinomori ulang menurut kemunculannya menjadi Tabel 3.1 sampai Tabel 3.21. Gambar menjadi arsitektur 3.1, alur 3.2, use case 3.3, model data 3.4, serta enam antarmuka 3.5 sampai 3.10.

Gambar disimpan pada folder gambar_proposal dengan sumber SVG dan PNG, sedangkan gambar versi sebelumnya dipertahankan. Label prosedur pada diagram alir mengikuti A sampai K, sehingga tidak lagi menunjuk subbab lama yang telah dipindahkan.

Pemetaan sumber dan checklist jurnal telah disesuaikan dengan lima belas bagian bernomor pada susunan baru. Metadata, PDF sumber, daftar pustaka, kode kebutuhan, dan batas keputusan mitra dipertahankan dari revisi sebelumnya.

## 5. Pemeriksaan dan keputusan terbuka

Hasil pemeriksaan struktur serta kesesuaian lintas dokumen disimpan dalam berkas validasi dengan hash naskah yang diperiksa. Pemeriksaan tidak menyatakan SQL, aplikasi, transaksi serentak, atau UAT telah dilaksanakan, dan tata letak Word/PDF belum termasuk cakupannya.

VALIDATION_LINK

Kewenangan pemeriksa rekening, tarif, potongan, kapasitas aktual, jadwal, serta peserta UAT tetap perlu ditetapkan bersama mitra. Hal tersebut tidak diisi dengan asumsi baru ketika struktur naskah diubah.

## 6. Bukti pemindahan dan salinan sebelumnya

Peta restrukturisasi memuat nomor lama dan baru, asal setiap bagian, hash blok sumber, serta hash dokumen rancangan yang tidak diubah. Naskah sebelum restrukturisasi dan dokumen pendamping yang terkait tersimpan pada folder SEBELUM_RESTRUKTURISASI.

MAP_LINK
'''
report=report.replace('CHAPTER_LINK',link(CH,'Bab 3 setelah restrukturisasi')+'.').replace('VALIDATION_LINK',link(OUT/'HASIL VALIDASI STRUKTUR PROPOSAL.json','Hasil validasi struktur proposal')+'.').replace('MAP_LINK',link(OUT/'PETA RESTRUKTURISASI.json','Peta restrukturisasi')+'.')
(OUT/'LAPORAN PENYESUAIAN STRUKTUR BAB 3.md').write_text(report,encoding='utf-8')

# Mark the earlier report as a record of the preceding revision, not the present structure.
p=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25/LAPORAN REVISI DAN VALIDASI TERPADU.md'
backup(p)
t=(BACK/'PENDAMPING'/p.name).read_text(encoding='utf-8')
first,rest=t.split('\n',1)
historical='\n\nCatatan versi: laporan ini merekam revisi terpadu sebelum perubahan struktur menjadi lima subbab utama. Susunan Bab 3 terkini dijelaskan pada '+link(OUT/'LAPORAN PENYESUAIAN STRUKTUR BAB 3.md','laporan restrukturisasi proposal')+'.\n'
p.write_text(first+historical+rest,encoding='utf-8')
print(json.dumps({'mapped_sections':len(LEDGER['sections']),'report':str(OUT/'LAPORAN PENYESUAIAN STRUKTUR BAB 3.md')},ensure_ascii=False))
