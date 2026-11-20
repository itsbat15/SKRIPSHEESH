from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27'
OUT = ROOT / 'DRAFT PROPOSAL MD/BAB 2'
OUT.mkdir(parents=True, exist_ok=True)


def link(path, label=None):
    p = Path(path)
    return f'[{label or p.name}](<{p.as_posix()}>)'


def local(pattern):
    return next(p for p in (ROOT / 'JURNAL').rglob(pattern) if 'ditandain' not in p.name)


docs = json.loads((BASE / 'DOKUMENTASI_RESMI/MANIFEST_DOKUMENTASI.json').read_text(encoding='utf-8'))
for doc in docs:
    if doc.get('looks_like_challenge'):
        generated = Path(doc['file']).resolve()
        assert BASE.resolve() in generated.parents
        generated.unlink()
        doc['status'] = 'link_only_browser_challenge'
        doc.pop('file', None)
(BASE / 'DOKUMENTASI_RESMI/MANIFEST_DOKUMENTASI.json').write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding='utf-8')

titles = [
    'Sistem Informasi Manajemen dan Pengembangannya', 'Personal Extreme Programming',
    'User Stories', 'Use Case Diagram', 'Business Process Model and Notation',
    'Class Diagram', 'Entity Relationship Diagram', 'Next.js', 'Tailwind CSS',
    'Laravel', 'REST API', 'MySQL', 'Black Box Testing', 'User Acceptance Testing',
]
rows = [
    ('Cukup untuk dasar', 'Laudon dan Laudon (2014); Sommerville (2011); Pressman (2010)',
     'Laudon cetak 45 sampai 48/PDF 47 sampai 50; Sommerville Bab 2, cetak 28 sampai 55/PDF 45 sampai 72, dan cetak 63/PDF 80 untuk pertimbangan pemilihan pendekatan.',
     'Gunakan PDF Laudon edisi ke-13 global tahun 2014. Klaim tahun 2020 atau 2022 harus memakai edisi lain yang memang tersedia, bukan PDF ini.'),
    ('Cukup untuk dasar', 'Dzhurov, Krasteva, dan Ilieva (2009); Beck dan Andres (2004)',
     'Dzhurov cetak 253 sampai 256/PDF 2 sampai 5; Beck salinan digital PDF 109 sampai 110 untuk stories dan siklus mingguan, serta PDF 120 untuk test-first.',
     'Dzhurov merupakan sumber asli PxP berbentuk prosiding, bukan jurnal SINTA. Sidiq dan Apriyanti menjadi contoh penerapan, bukan pengganti sumber dasar.'),
    ('Ada, perlu diperkuat', 'Beck dan Andres (2004); Cohn (2004), ditambah cuplikan resmi buku dan artikel penulis',
     'Cohn cetak 4 sampai 5/PDF 13 sampai 14 untuk definisi dan tiga aspek; cetak 17/PDF 26 untuk INVEST. Template kalimat tiga bagian dijelaskan dalam artikel resmi Cohn yang ditautkan.',
     'Berkas Cohn hanya bab contoh 61 halaman, bukan buku lengkap. Cohn tidak dinyatakan sebagai pencipta awal seluruh konsep user stories.'),
    ('Cukup, diperkuat standar', 'Sommerville (2011); OMG UML 2.5.1 (2017)',
     'Sommerville cetak 124 sampai 126/PDF 141 sampai 143; OMG Bab 18, cetak 639 dan seterusnya/PDF 681 dan seterusnya.',
     'Gunakan spesifikasi OMG untuk makna include dan extend. Contoh penerapan jurnal bukan standar notasi UML.'),
    ('Belum ada sumber khusus yang memadai', 'OMG BPMN 2.0.2 (2013), ditambahkan',
     'Bab 7, terutama §7.3.1 dan Tabel 7.1, cetak 26 sampai 28/PDF 56 sampai 58. Halaman sampul menyebut Desember 2013; katalog formal mencatat adopsi Januari 2014.',
     'BPMN bukan bagian UML. Pesan antarpool dan urutan aktivitas di dalam proses tidak boleh digambarkan dengan jenis garis yang sama tanpa mengikuti aturannya.'),
    ('Cukup, diperkuat standar', 'Sommerville (2011); OMG UML 2.5.1 (2017)',
     'Sommerville cetak 129 sampai 133/PDF 146 sampai 150; OMG §11.4 Classes, cetak 194 sampai 195/PDF 236 sampai 237 sebagai titik masuk.',
     'Jelaskan atribut, operasi, hubungan, dan multiplicity. Jangan menyamakan class diagram dengan tabel ERD atau membuat diagram yang tidak digunakan pada Bab 3.'),
    ('Ada, perlu sumber asal dan notasi', 'Pressman (2010); Chen (1976), ditambah cuplikan penulis; dokumentasi Mermaid untuk notasi implementasi',
     'Pressman cetak 165 sampai 166/PDF 194 sampai 195; Chen cetak 9 sampai 13/PDF 1 sampai 5 pada cuplikan yang tersedia.',
     'Cuplikan Chen hanya lima halaman pertama dari artikel 28 halaman. Notasi Crow’s Foot tidak boleh seluruhnya diatribusikan kepada cuplikan Chen; gunakan dokumentasi notasi yang benar-benar dipakai.'),
    ('Belum ada dokumentasi primer lokal', 'Vercel, dokumentasi Next.js; React, Managing State, ditambahkan',
     'Dokumentasi Next.js: halaman pengantar dan Layouts and Pages; React: Managing State. Gunakan judul bagian, URL, dan tanggal akses karena halaman HTML tidak memiliki halaman cetak tetap.',
     'Dokumentasi berubah. Bedakan fungsi yang tersedia dalam dokumentasi dari versi dan fitur yang benar-benar dipakai proyek.'),
    ('Belum ada dokumentasi primer lokal', 'Tailwind Labs, dokumentasi Tailwind CSS, ditambahkan',
     'Styling with Utility Classes dan Responsive Design; lokator menggunakan judul bagian serta URL.',
     'Framework tampilan tidak otomatis membuktikan kemudahan penggunaan, aksesibilitas, atau kepuasan pengguna.'),
    ('Ada contoh penerapan, belum cukup untuk teori teknis', 'Laravel, dokumentasi resmi Sanctum, Authorization, Validation, Database dan Eloquent, ditambahkan',
     'Sanctum: SPA Authentication; Authorization: Gates dan Policies; Validation: form/input validation; Database: Database Transactions; Eloquent: pengantar model.',
     'Dokumentasi seri 12.x dipakai sebagai referensi versi yang jelas, bukan bukti proyek sudah memakai Laravel 12. Mode SPA Sanctum menggunakan sesi berbasis kuki; token CSRF berbeda dari personal access token.'),
    ('Belum ada sumber asal REST lokal', 'Fielding (2000); Fielding, Nottingham, dan Reschke (2022), RFC 9110, ditambahkan',
     'Fielding Bab 5 dimulai cetak 76/PDF 94; §5.1.3 Stateless cetak 78/PDF 96 dan §5.1.5 Uniform Interface cetak 81/PDF 99. RFC 9110 §9 untuk metode dan §15 untuk status.',
     'Disertasi merupakan sumber asli REST, bukan buku atau jurnal SINTA. HTTP, JSON, dan CRUD saja belum cukup membuktikan seluruh batasan REST dipenuhi; uraikan arsitektur secara jujur.'),
    ('Ada contoh penggunaan, perlu manual resmi', 'Oracle, MySQL 8.4 Reference Manual, ditambahkan sebagai tautan resmi',
     'General Information; §15.1.20.5 FOREIGN KEY Constraints; §17.7.2 InnoDB Transaction Model. Ketiga halaman diverifikasi lewat layanan web, tetapi unduhan HTML langsung ditolak server.',
     'Pilih versi basis data implementasi yang konsisten. Dukungan transaksi tidak berarti sistem otomatis memenuhi seluruh aturan bisnis atau kepatuhan perbankan.'),
    ('Cukup untuk dasar, diperkuat silabus', 'Pressman (2010); ISTQB CTFL v4.0.1 (2024), ditambahkan',
     'Pressman cetak 497 sampai 498/PDF 526 sampai 527; ISTQB §4.2.1 EP halaman 39 dan §4.2.2 BVA halaman 40, sama dengan nomor PDF.',
     'EP dan BVA tidak menggantikan semua skenario alur, perubahan status, otorisasi, atau akses serentak. Tentukan varian BVA dan kaitkan nilai uji dengan aturan yang benar-benar dipilih.'),
    ('Cukup untuk dasar, diperkuat silabus', 'Sommerville (2011); ISTQB Acceptance Testing v1.0 (2019), ditambahkan',
     'Sommerville cetak 228 sampai 230/PDF 245 sampai 247; ISTQB §1.1.2 halaman 11, §2.1 halaman 15, Bab 3 halaman 19 sampai 21, dan §4.1.2 halaman 25.',
     'UAT tidak selalu memakai Likert. Sullivan dan Artino (2013) ditemukan untuk pendamping analisis Likert bila diperlukan, tetapi bukan sumber awal Likert atau standar ambang kelayakan.'),
]
matrix=[]
for i,(status,source,pages,caution) in enumerate(rows,1):
    matrix.append(dict(subbab=f'2.1.{i}',judul=titles[i-1],status_sebelum=status,sumber=source,lokator=pages,batas=caution))
(BASE/'MATRIKS_CAKUPAN_SUMBER.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2),encoding='utf-8')

# Preserve the pasted guide as evidence and create a separate revision.
attachment=Path(r'C:\Users\ARIEL\.codex\attachments\3c44f410-1494-4ca5-95af-241d1ef759a9\Pasted text.txt')
original=attachment.read_text(encoding='utf-8').lstrip('\ufeff')
(BASE/'PANDUAN_LAMPIRAN_SEBELUM_PENYESUAIAN.txt').write_text(original,encoding='utf-8')
parts=re.split(r'(?=\*\*2\.1\.\d+ )',original)
sections={}
for part in parts:
    m=re.match(r'\*\*2\.1\.(\d+) ',part)
    if m: sections[int(m.group(1))]=part
tail=''
if '**2.2 Penelitian Terdahulu**' in sections[14]:
    sections[14],tail=sections[14].split('**2.2 Penelitian Terdahulu**',1)
    tail='**2.2 Penelitian Terdahulu**'+tail
sections[5]='''**2.1.5 Business Process Model and Notation**

Jelaskan BPMN sebagai notasi pemodelan proses bisnis yang digunakan untuk memahami aktivitas dan koordinasi pihak terkait. Bedakan model proses berjalan dan usulan, serta bedakan BPMN dari diagram alir tahapan penelitian PxP.

Isi yang disarankan:

- Tujuan BPMN dan kegunaannya dalam memahami proses bisnis.
- Event, activity, gateway, pool, lane, sequence flow, message flow, dan data object yang dipakai.
- Aturan dasar pembacaan dan penghubungan notasi.
- Penggambaran pihak, aktivitas, dokumen, keputusan, serta kondisi alternatif.
- Hubungan pemetaan proses dengan penggalian dan validasi kebutuhan.

Sertakan tabel notasi berdasarkan spesifikasi resmi OMG dan gunakan hanya elemen yang relevan. Model proses bisnis ARTHA ditempatkan pada Bab 3 dan divalidasi bersama manajemen; penghapusan Activity Diagram tidak boleh diatribusikan sebagai instruksi eksplisit Bu Ayu karena transkrip hanya menyarankan pemetaan proses bisnis.

'''
order=[1,2,3,4,5,6,7,8,12,9,10,11,13,14]
guide='# Panduan isi Bab 2 sesuai susunan final\n\nPanduan ini disesuaikan pada 27 Oktober 2026 dengan susunan yang telah disepakati. Naskah Bab 2 yang sudah ada dan lampiran pengguna tidak ditimpa.\n\n'+parts[0]
for number,old in enumerate(order,1):
    section=sections[old]
    section=re.sub(r'^\*\*2\.1\.\d+ [^\n]+',f'**2.1.{number} {titles[number-1]}**',section,count=1)
    guide+=section.rstrip()+f'\n\nRujukan kerja yang disarankan: {matrix[number-1]["sumber"]}. Lokator dan batas penggunaannya tersedia pada matriks sumber pendamping.\n\n'
guide+=tail
guide+='\n\nCatatan penempatan rincian: Bab 3 memuat rencana pengujian, kriteria, serta kasus yang representatif; daftar kasus uji lengkap dapat ditempatkan di lampiran. Hubungan Bab 2, Bab 3, dan hasil Bab 4 perlu dipertahankan tanpa mengulang seluruh dokumen teknis di setiap bab.\n'
(OUT/'PANDUAN ISI BAB 2 - SUSUNAN FINAL DAN RUJUKAN.md').write_text(guide,encoding='utf-8')

report='''# Validasi panduan dan kelengkapan sumber Bab 2.1

Pemeriksaan dilakukan pada 27 Oktober 2026 terhadap panduan yang dilampirkan pengguna, koleksi JURNAL, serta susunan final Bab 2.1. Tujuannya adalah memastikan setiap topik memiliki sumber yang sesuai, bukan menyatakan seluruh klaim dalam draf Bab 2 sudah benar.

## 1. Hasil pemeriksaan panduan

Panduan lampiran benar secara umum dalam memisahkan teori dan penerapan, tetapi belum mengikuti keputusan terakhir. Bagian Activity Diagram harus diganti menjadi Business Process Model and Notation, sedangkan Tailwind CSS dipindahkan setelah Next.js sehingga penomoran teknologi juga berubah.

Ada empat penyempurnaan lain yang perlu dipakai ketika menulis. Pertama, Bab 3 cukup memuat rencana uji dan kasus representatif, sementara daftar kasus lengkap dapat ditempatkan pada lampiran; kedua, EP dan BVA tidak membuktikan seluruh perilaku transaksi; ketiga, kuesioner Likert tetap pilihan bersyarat; keempat, versi dokumentasi teknologi tidak dianggap otomatis sebagai versi yang telah dipasang pada proyek.

## 2. Batas standar ITK yang benar-benar ditemukan

Template prototipe, cetak 4 sampai 5/PDF 17 sampai 18, memperbolehkan kajian teknologi, metode, dan pendekatan desain yang mendukung prototipe. Template tidak menetapkan daftar empat belas judul tersebut sebagai daftar wajib dan menandai dasar teori pendukung sebagai bagian opsional.

Panduan kepenulisan ITK 2025 §3.7, cetak 16/PDF 24, mewajibkan konsistensi Harvard, kelengkapan sumber yang dikutip, penggunaan pengelola referensi, pengurutan alfabetis tanpa nomor, dan inden gantung 1,27 cm. Daftar pustaka kerja dalam dokumen ini perlu diimpor ke aplikasi referensi dan disesuaikan pada dokumen akhir.

Rubrik seminar proposal prototipe SI 2026, cetak 80/PDF 87, menempatkan dukungan minimal sepuluh pustaka lima tahun terakhir pada kategori Sangat Baik. Karena itu, sumber klasik primer dapat dipakai untuk konsep asal, tetapi tidak menggantikan kebutuhan dukungan mutakhir pada proposal; tidak ditemukan aturan bahwa setiap buku harus dibuang setelah batas tahun tertentu atau bahwa semua teori harus bersumber dari jurnal SINTA.

Pemilihan sumber lama sebagai fondasi adalah pertimbangan ilmiah berdasarkan fungsi sumber, bukan pengecualian tertulis yang menjamin nilai tertentu. Hasil penilaian tetap bergantung pada keseluruhan proposal dan penerapan rubrik oleh pembimbing atau penguji.

## 3. Matriks setiap subbab

Status berikut menggambarkan keadaan sebelum penambahan sumber pada pekerjaan ini. Sumber baru kemudian melengkapi teori yang belum tersedia secara khusus, sementara sumber jurnal penerapan tetap berfungsi sebagai pendamping.

| Subbab | Ketersediaan awal | Sumber utama yang dipilih |
| :--- | :--- | :--- |
'''
for m in matrix:report+=f'| {m["subbab"]} {m["judul"]} | {m["status_sebelum"]} | {m["sumber"]} |\n'
report+='\n## 4. Lokator dan batas penggunaan\n\nNomor cetak dan nomor urut PDF dibedakan agar rujukan mudah diperiksa. Untuk HTML, gunakan judul bagian dan URL; jangan membuat nomor halaman yang tidak tersedia.\n\n'
for m in matrix:
    report+=f'### {m["subbab"]} {m["judul"]}\n\n{m["lokator"]}\n\n{m["batas"]}\n\n'
report+='''## 5. Sumber primer yang ditambahkan

Tujuh PDF di bawah diperoleh dari situs standar, universitas asal, atau situs penulis. Label lengkap atau cuplikan menunjukkan isi yang benar-benar tersedia; berkas cuplikan tidak diperlakukan sebagai buku atau artikel lengkap.

'''
download=json.loads((BASE/'MANIFEST_UNDUHAN.json').read_text(encoding='utf-8'))
for d in download:
    report+=f'- {link(d["file"])}; [sumber unduhan]({d["url"]}).\n'
report+='''
Cuplikan Cohn berjumlah 61 halaman dan meliputi bagian terpilih, bukan seluruh buku; misalnya Bab 6 yang hanya disebut pada daftar isi tidak boleh dinyatakan telah dibaca lengkap. Cuplikan Chen berjumlah lima halaman, yaitu cetak 9 sampai 13 dari artikel asal pada halaman 9 sampai 36.

OMG UML dan BPMN merupakan spesifikasi primer yang otoritatif untuk notasi, tetapi versi yang dipakai bukan berarti versi pertama sepanjang sejarah notasi tersebut. Demikian pula, Cohn (2004) adalah rujukan utama user stories yang dipilih, bukan klaim bahwa Cohn menciptakan user stories.

## 6. Dokumentasi resmi dan hasil penyimpanan

Dokumentasi disimpan sebagai HTML jika server mengizinkan, sedangkan URL tetap menjadi alamat rujukan utama. Salinan lokal tidak menjamin seluruh tautan, skrip, atau tampilan halaman berfungsi tanpa internet.

| Sumber | Status | URL |
| :--- | :--- | :--- |
'''
for d in docs:
    status='HTML tersimpan dan judul diperiksa' if d['status']=='downloaded' else ('Tautan saja; server menolak unduhan HTML' if d['status']=='link_only' else 'Tautan saja; respons unduhan berupa pemeriksaan peramban, bukan artikel')
    report+=f'| {d["name"]} | {status} | [Buka sumber]({d["url"]}) |\n'
report+='''
Untuk dokumentasi tanpa tahun publikasi yang dapat dipastikan, gunakan penulis lembaga dan t.t. disertai tanggal akses 27 Oktober 2026. Jangan memakai 2026 sebagai tahun publikasi hanya karena halaman diakses pada tahun tersebut; beberapa dokumen lembaga yang sama perlu dibedakan secara konsisten oleh pengelola referensi.

## 7. Kedudukan jurnal SINTA dan sumber nonjurnal

Pekerjaan ini tidak menambahkan jurnal nasional baru karena kekurangan teori lebih tepat dipenuhi oleh sumber asli, standar, dan dokumentasi resmi. Akreditasi SINTA tidak berlaku untuk buku, disertasi, prosiding internasional, spesifikasi OMG, silabus ISTQB, atau dokumentasi perangkat lunak; artikel klasik Chen merupakan artikel internasional sumber awal model ER, bukan jurnal nasional yang diperingkat SINTA.

Jurnal penerapan dalam koleksi, seperti Apriyanti, Sidiq, Ahadi, dan INET, dapat dipakai sebagai contoh hasil implementasi. Namun, status edisi mengikuti bukti audit SINTA yang sudah ada dan bukan pemeriksaan akreditasi ulang pada pekerjaan ini; beberapa cakupan edisi yang sebelumnya belum pasti tetap tidak dinyatakan terverifikasi.

## 8. Peringatan khusus saat melanjutkan draf yang sudah tersedia

Berkas BAB_2_TINJAUAN_PUSTAKA.md yang sudah ada ternyata belum mengikuti seluruh keputusan susunan terakhir dan masih memuat beberapa klaim komparasi yang telah dikoreksi sebelumnya. Contohnya adalah larangan mutlak perangkapan peran Scrum dan ketidakmungkinan penerapan RAD; penambahan sumber pada pekerjaan ini tidak membuat klaim tersebut menjadi benar.

Gunakan Laudon dan Laudon (2014) untuk PDF edisi ke-13 global yang tersedia. Nama buku atau tahun baru, misalnya Connolly dan Begg (2020), tidak boleh diperlakukan telah tersedia hanya karena ditulis dalam draf; sumber yang benar-benar diperoleh perlu dicatat dan isinya diperiksa.

Rujukan asal REST menjelaskan batasan stateless, sedangkan rancangan autentikasi ARTHA menggunakan sesi. Jelaskan pilihan implementasi secara akurat dan hindari mengklaim semua batasan REST telah dipenuhi hanya karena aplikasi memakai JSON serta endpoint HTTP; keputusan teknis lebih rinci perlu diselaraskan pada Bab 3.

## 9. Hasil dan pekerjaan berikutnya

Setiap subbab kini mempunyai rujukan kerja yang dapat ditelusuri, baik dari koleksi awal maupun sumber primer yang ditambahkan. Hal ini merupakan kesiapan pustaka untuk mulai menulis, bukan pengesahan akhir setiap paragraf, gambar, formula, atau instrumen yang nanti digunakan.

Gunakan panduan revisi pendamping untuk mulai menyusun subbab secara berurutan, kemudian audit klaim dan halaman setelah paragrafnya terbentuk. Naskah Bab 2 yang sudah ada, Bab 1, dan Bab 3 tidak diubah oleh pekerjaan ini.
'''
report+='\n## 10. Tautan sumber lokal utama yang sudah tersedia\n\nSumber berikut tetap dipakai tanpa digandakan atau diubah. Nomor halaman relevan sudah dipetakan pada Bagian 4.\n\n'
for pat in ['*laudon*.pdf','Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf','ebook-pressman-sw-engineering.pdf','Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf','Personal Extreme Programming - Agile*.pdf']:
    report+='- '+link(local(pat))+'\n'
(BASE/'AUDIT SUMBER DAN PETA RUJUKAN BAB 2.1.md').write_text(report,encoding='utf-8')

bib=[]
def entry(kind,key,fields):
    bib.append('@'+kind+'{'+key+',\n'+',\n'.join('  '+k+' = {'+v+'}' for k,v in fields.items())+'\n}\n')
entry('book','Laudon2014',dict(author='Laudon, Kenneth C. and Laudon, Jane P.',title='Management Information Systems: Managing the Digital Firm',edition='13, Global',year='2014',publisher='Pearson'))
entry('book','Sommerville2011',dict(author='Sommerville, Ian',title='Software Engineering',edition='9',year='2011',publisher='Addison-Wesley'))
entry('book','Pressman2010',dict(author='Pressman, Roger S.',title="Software Engineering: A Practitioner's Approach",edition='7',year='2010',publisher='McGraw-Hill'))
entry('book','BeckAndres2004',dict(author='Beck, Kent and Andres, Cynthia',title='Extreme Programming Explained: Embrace Change',edition='2',year='2004',publisher='Addison-Wesley'))
entry('inproceedings','Dzhurov2009',dict(author='Dzhurov, Yani and Krasteva, Iva and Ilieva, Sylvia',title='Personal Extreme Programming: An Agile Process for Autonomous Developers',booktitle='Software, Services and Semantic Technologies',year='2009',pages='252--259'))
entry('book','Cohn2004',dict(author='Cohn, Mike',title='User Stories Applied: For Agile Software Development',year='2004',publisher='Addison-Wesley',note='Salinan tersedia berupa bab contoh resmi; bukan buku lengkap',url='https://www.mountaingoatsoftware.com/promotions/usa-chapters',urldate='2026-10-27'))
entry('article','Chen1976',dict(author='Chen, Peter Pin-Shan',title='The Entity-Relationship Model: Toward a Unified View of Data',journal='ACM Transactions on Database Systems',volume='1',number='1',pages='9--36',year='1976',doi='10.1145/320434.320440',note='Salinan penulis hanya halaman 9 sampai 13',url='https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf',urldate='2026-10-27'))
entry('phdthesis','Fielding2000',dict(author='Fielding, Roy Thomas',title='Architectural Styles and the Design of Network-based Software Architectures',school='University of California, Irvine',year='2000',url='https://ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf',urldate='2026-10-27'))
for key,title,year,url in [('OMG2017UML','OMG Unified Modeling Language, Version 2.5.1','2017','https://www.omg.org/spec/UML/2.5.1'),('OMG2013BPMN','Business Process Model and Notation, Version 2.0.2','2013','https://www.omg.org/spec/BPMN/2.0.2')]:
    entry('manual',key,dict(author='{Object Management Group}',title=title,year=year,url=url,urldate='2026-10-27'))
for key,title,year,url in [('ISTQB2024','Certified Tester Foundation Level Syllabus v4.0.1','2024','https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf'),('ISTQB2019','Certified Tester Foundation Level Syllabus: Acceptance Testing, Version 2019','2019','https://istqb.org/wp-content/uploads/2024/11/ISTQB-CT-AcT_Syllabus_v1.0_2019.pdf')]:
    entry('manual',key,dict(author='{International Software Testing Qualifications Board}',title=title,year=year,url=url,urldate='2026-10-27'))
entry('techreport','HTTP2022',dict(author='Fielding, Roy and Nottingham, Mark and Reschke, Julian',title='HTTP Semantics',institution='Internet Engineering Task Force',number='RFC 9110',year='2022',doi='10.17487/RFC9110',url='https://www.rfc-editor.org/rfc/rfc9110.html'))
for i,d in enumerate(docs,1):
    if d['name'].startswith(('HTTP_','Sullivan_')):continue
    org= 'Vercel' if d['name'].startswith('Nextjs') else ('React' if d['name'].startswith('React') else ('Tailwind Labs' if d['name'].startswith('Tailwind') else ('Laravel' if d['name'].startswith('Laravel') else ('Oracle' if d['name'].startswith('MySQL') else ('Mermaid' if d['name'].startswith('Mermaid') else 'Mike Cohn')))))
    entry('misc',f'Doc{i:02}',dict(author='{'+org+'}',title=d.get('title') or d['name'].replace('_',' '),url=d['url'],urldate='2026-10-27',note='Tanggal publikasi belum dipastikan; gunakan tanpa tahun, bukan tahun akses'))
(BASE/'REFERENSI_PRIMER_BAB2_1.bib').write_text('\n'.join(bib),encoding='utf-8')
print(json.dumps({'subbab':len(matrix),'pdf_primer':len(download),'html_valid':sum(d['status']=='downloaded' for d in docs),'tautan_saja':sum(d['status']!='downloaded' for d in docs),'entri_bib':len(bib),'panduan_final':str(OUT/'PANDUAN ISI BAB 2 - SUSUNAN FINAL DAN RUJUKAN.md')},ensure_ascii=False,indent=2))
