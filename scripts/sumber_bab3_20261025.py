from pathlib import Path
import json, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'BAB3_PENDUKUNG_2026-10-25'
OUT.mkdir(exist_ok=True)
OLD=ROOT/'JURNAL/AUDIT_SITASI_BAB1_2026-10-25'
corpus=json.loads((OLD/'SUMBER_DAN_TEKS_HALAMAN.json').read_text(encoding='utf-8'))+json.loads((OLD/'TEKS_SUMBER_TAMBAHAN_BAB2.json').read_text(encoding='utf-8'))
prior=json.loads((ROOT/'JURNAL/PEMERIKSAAN_SINTA_2026-10-24.json').read_text(encoding='utf-8'))
extra=json.loads((ROOT/'JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/METADATA_DAN_VERIFIKASI.json').read_text(encoding='utf-8'))['references']

specs=[
('J01','Dzhurov','Dzhurov dkk. (2009)',[(2,'253'),(3,'254'),(4,'255'),(5,'256')],
 'Prinsip, tahapan, estimasi tugas, pengujian unit, dan evaluasi iterasi PxP.',
 'Prosiding sumber asli, bukan jurnal SINTA. Tidak menetapkan Fibonacci sebagai kewajiban dan tidak memberikan jadwal kalender ARTHA.',
 "Dzhurov, Y., Krasteva, I. dan Ilieva, S. (2009) 'Personal Extreme Programming: An Agile Process for Autonomous Developers', dalam International Conference on Software, Services & Semantic Technologies (S3T), Sofia, hlm. 252 sampai 259.",
 'https://dse.fmi.uni-sofia.bg/personalPage-Ilieva.htm'),
('J02','Fikri','Fikri dan Arthawan Sugih Prabowo (2021)',[(3,'103'),(4,'104'),(5,'105')],
 'Contoh penerapan PxP, user story, rencana rilis, rancangan data, dan antarmuka.',
 'PDF berlabel edisi Desember 2020, tetapi metadata penerbit bertanggal 4 Januari 2021. Nama lengkap penulis kedua adalah I Putu Deny Arthawan Sugih Prabowo, sehingga S. P. pada PDF bukan bukti bahwa Prabowo orang berbeda. Cakupan SK untuk edisi perlu dipastikan terpisah.',
 "Fikri, A.M. dan Arthawan Sugih Prabowo, I.P.D. (2021) 'Rancang Bangun Sistem Informasi Buku Tamu pada Dinas Pemuda, Olahraga dan Pariwisata Kota Balikpapan dengan Metode Personal Extreme Programming', Multitek Indonesia: Jurnal Ilmiah, 14(2), hlm. 101 sampai 110. https://doi.org/10.24269/mtkind.v14i2.2568",
 'https://journal.umpo.ac.id/index.php/multitek/article/view/2568'),
('J03','Sidiq','Sidiq dkk. (2025)',[(3,'37'),(4,'38'),(11,'45')],
 'Penggalian kebutuhan dan pencatatan perubahan serta durasi pelaksanaan PxP.',
 'Bukan bukti seluruh proyek selalu lebih cepat. Total pengembangan 50 hari dan implementasi 37 hari berbeda; cakupan SK SINTA untuk edisi 2025 masih belum dipastikan dari arsip yang tersedia.',
 "Sidiq, A.L., Marthasari, G.I. dan Aminudin (2025) 'Implementasi Metode Personal Extreme Programming pada Pengembangan Sistem Informasi Surat Menyurat (Studi Kasus: Dinas Pendidikan Pemuda dan Olahraga Kabupaten Tambrauw)', Jurnal Jaring SainTek, 7(1), hlm. 35 sampai 46. https://doi.org/10.31599/zsbj5v55",
 'https://ejurnal.ubharajaya.ac.id/index.php/jaring-saintek/article/view/744'),
('J04','Apriyanti','Apriyanti dkk. (2024)',[(2,'3679'),(3,'3680'),(6,'3683'),(7,'3684'),(8,'3685')],
 'Contoh pengembangan PxP, pengujian kotak hitam, dan keterlibatan pengguna dalam UAT.',
 'Objek e-kavling dan UAT berupa kuesioner. Tidak menjadi sumber langsung seluruh tugas UAT ARTHA; jumlah peserta tidak konsisten pada beberapa bagian artikel sehingga tidak disalin.',
 "Apriyanti, N., Wati, S.F.A. dan Najaf, A.R.E. (2024) 'Pemanfaatan Metodologi PXP dan Pengujian User Acceptance Testing (UAT) dalam Pengembangan Website E-Kavling', JATI (Jurnal Mahasiswa Teknik Informatika), 8(3), hlm. 3678 sampai 3686. https://doi.org/10.36040/jati.v8i3.9766",
 'https://mail.ejournal.itn.ac.id/jati/article/view/9766'),
('J05','Ahadi','Ahadi dkk. (2025)',[(7,'764'),(8,'765')],
 'Pemisahan kewenangan cabang dan pemantauan pusat; contoh kebutuhan serta pemodelan sistem.',
 'Objek hotel dengan empat aktor, bukan bukti bahwa ARTHA harus mempunyai tepat dua peran atau sudah diuji pada delapan cabang.',
 "Ahadi, A.H., Pariyadi dan Djauhari, T. (2025) 'Pengembangan Sistem Informasi Manajemen Hotel Multi-Cabang Berbasis Web dengan Framework Laravel', Djtechno: Jurnal Teknologi Informasi, 6(2), hlm. 758 sampai 773. https://doi.org/10.46576/djtechno.v6i2.7139",
 'https://jurnal.dharmawangsa.ac.id/index.php/djtechno/article/view/7139'),
('J06','Thiovanda','Thiovanda (2026)',[(1,'1'),(4,'4'),(5,'5')],
 'Pembanding dekat sistem les: data cabang, head admin, admin cabang, guru, jadwal, dan pembayaran.',
 'Sudah mempunyai manajemen cabang. Tahun berasal dari verifikasi penerbit pada audit; volume dan nomor belum dicantumkan karena tidak jelas pada PDF dan laman tidak dapat diakses ulang saat penyusunan ini.',
 "Thiovanda, V. (2026) 'Perancangan Sistem Informasi Pencatatan Penjadwalan dan Pembayaran Les Berbasis Web', Jurnal Ilmu Komputer dan Sistem Informasi, hlm. 1 sampai 6. https://doi.org/10.24912/yctfww47",
 'https://journal.untar.ac.id/index.php/jiksi/article/view/36675'),
('J07','05_Penerimaan','Hendri dkk. (2025)',[(1,'124'),(2,'125')],
 'Kebutuhan pencatatan penerimaan SPP dan penelusuran perbedaan catatan pembayaran.',
 'Analisis dan rancangan Figma; bukan bukti implementasi aplikasi bank atau fakta ARTHA. PDF memiliki variasi ejaan Alghifary/Alghifari; identitas rinci mengikuti metadata sumber dan perlu konsistensi saat impor.',
 "Hendri, Alghifari, M., Putri, H.Y., Rahayu, M. dan Nurmalasari (2025) 'Analisis Sistem Informasi Akuntansi Penerimaan Kas (SPP) pada Yayasan Semesta Khatulistiwa', JUSTIAN: Jurnal Sistem Informasi Akuntansi, 6(2), hlm. 124 sampai 135. https://doi.org/10.31294/justian.v6i2.9114",
 'https://doi.org/10.31294/justian.v6i2.9114'),
('J08','Sudirman','Sudirman dan Tristianti (2021)',[(1,'126'),(2,'127')],
 'Konsep perbedaan pencatatan internal dan rekening koran serta dasar pencocokan bank.',
 'Objek perusahaan, bukan bimbel. Tidak otomatis membenarkan klaim sistem menyusun seluruh rekonsiliasi saldo dan laporan akuntansi.',
 "Sudirman, B. dan Tristianti, M. (2021) 'Sistem Informasi Pengendalian Kas Bank dengan Metode Rekonsiliasi pada CV. Lisa Pratama Berbasis Client-Server', MEANS (Media Informasi Analisa dan Sistem), 6(2), hlm. 126 sampai 129. https://doi.org/10.54367/means.v6i2.1450",
 'https://doi.org/10.54367/means.v6i2.1450'),
('J09','Ramadhan','Ramadhan dan Widodo (2026)',[(15,None),(17,None)],
 'Pencatatan cabang, rekap pusat, dan rekap penerimaan harian per kanal.',
 'Studi akuntansi dan rekomendasi format, bukan implementasi aplikasi. Gunakan urutan PDF karena footer 15/15 dan 17/15 tidak konsisten; bukan nomor halaman jurnal.',
 "Ramadhan, F. dan Widodo, H. (2026) 'Accounting Treatment of Head Office and Branches Based on SAK EP: A Study on UMKM Rams Dimsum', Indonesian Journal of Law and Economics Review, 21(2). https://doi.org/10.21070/ijler.v21i2.1706",
 'https://ijler.umsida.ac.id/index.php/ijler/article/view/1706'),
('J10','Khafidhoh','Khafidhoh dkk. (2026)',[(1,'15'),(2,'16'),(5,'19')],
 'Kebutuhan jadwal tentor bimbel dan pertimbangan konflik penugasan.',
 'Penelitian memakai algoritma genetika untuk menyusun jadwal otomatis. ARTHA hanya mengadaptasi kebutuhan pemeriksaan konflik, bukan algoritma atau hasilnya.',
 "Khafidhoh, N., Febrianti, A.R. dan Sujono (2026) 'Sistem Penjadwalan Menggunakan Algoritma Genetika Berbasis Web', Jurnal Teknologi Informasi: Jurnal Keilmuan dan Aplikasi Bidang Teknik Informatika, 20(2), hlm. 15 sampai 20. https://doi.org/10.47111/jti.v20i2.24540",
 'https://e-journal.upr.ac.id/index.php/JTI/article/view/24540'),
('J11','Kabisatullah','Kabisatullah dan Noprisson (2026)',[(5,'93'),(6,'94'),(7,'95')],
 'Validasi kapasitas dan irisan waktu pada peladen, termasuk pencegahan permintaan serentak yang tidak sah.',
 'Objek ruang rapat dengan CSP dan Android. Batas kapasitas ARTHA berasal dari mitra; tidak mengklaim mengimplementasikan seluruh CSP. PDF menulis Noprison, metadata penerbit menggunakan Noprisson.',
 "Kabisatullah, F. dan Noprisson, H. (2026) 'Pengembangan Aplikasi RapaTrack untuk Manajemen Ruang Rapat Menggunakan Constraint Satisfaction Problem Berbasis Android', JUSIBI (Jurnal Sistem Informasi dan E-Bisnis), 8(2), hlm. 89 sampai 96. https://doi.org/10.54650/jusibi.v8i2.678",
 'https://doi.org/10.54650/jusibi.v8i2.678'),
('J12','Fajriansyah','Fajriansyah dkk. (2026)',[(2,'116'),(10,'124'),(11,'125')],
 'Pembanding integrasi siswa, jadwal, dan pembayaran pada bimbel.',
 'Hasil efisiensi Bee Hive tidak dipindahkan sebagai hasil atau jaminan untuk ARTHA.',
 "Fajriansyah, S.N., Wijaya, M.S., Eryana, D.A., Safa, A., Pramadhan, H.R., Wicaksono, A., Baehaqi, M.I., Deivivi, F., Nurfajriansyah, D. dan Apandi, S. (2026) 'Pengembangan Sistem Informasi Bimbingan Belajar Berbasis Web untuk Efisiensi Operasional Bee Hive', Jurnal Rekayasa Informasi Swadharma, 6(2), hlm. 115 sampai 126. https://doi.org/10.56486/jris.vol6no2.1346",
 'https://doi.org/10.56486/jris.vol6no2.1346'),
('J13','Gunawan','Gunawan dkk. (2025)',[(1,'424'),(9,'432')],
 'Pembanding integrasi modul administrasi bimbel dan pemeriksaan berbasis peran.',
 'Memakai Waterfall dan susunan pengguna berbeda. Tidak menjadi pembuktian bahwa sistem ARTHA lebih efisien atau lebih unggul.',
 "Gunawan, S.C., Nurwegiono, M. dan Setiawan, R. (2025) 'Sistem Informasi Bimbingan Belajar RSDC Berbasis Website dengan Menggunakan Metode Waterfall untuk Meningkatkan Efisiensi Administrasi', Riau Jurnal Teknik Informatika, 4(3), hlm. 424 sampai 435. https://doi.org/10.52158/rjti.v4i3.3655",
 'https://doi.org/10.52158/rjti.v4i3.3655')]

sources=[]
for sid,key,author,loc,use,limit,bib,url in specs:
    x=next(x for x in corpus if key in x['file'])
    path=Path(x['file']); assert path.exists()
    for page,_ in loc: assert 1<=page<=len(x['pages'])
    old=next((q for q in prior if Path(q['file'].replace('\\','/')).name==path.name),None)
    ex=next((q for q in extra if q.get('doi','') and q['doi'].lower() in bib.lower()),None)
    rank=('SINTA '+str(ex['rank'])) if ex else (old['rank'] if old else 'Tidak berlaku')
    ranknote=ex.get('period') if ex else (old.get('note','') if old else 'Prosiding, bukan jurnal nasional')
    certainty='edisi tercakup berdasarkan pemeriksaan 24 Oktober 2026' if (ex or sid in ['J04','J12','J13']) else 'peringkat jurnal; cakupan edisi perlu pemeriksaan SK'
    if sid=='J01':certainty='tidak dinilai dengan SINTA'
    sources.append(dict(id=sid,author=author,file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),locations=[dict(pdf_page=n,printed=p) for n,p in loc],use=use,limit=limit,bibliography=bib,publisher=url,rank=rank,rank_note=ranknote,rank_scope=certainty))

mapping=[
('3.1','J05 J06 J12 J13','Gambaran produk menggunakan pembanding domain; seluruh fakta ARTHA berasal dari wawancara.'),
('3.1.1','J12 J13','Integrasi modul bimbel; identitas, cabang, serta masalah aktual memerlukan sumber primer mitra.'),
('3.1.2','J05 J06','Pemisahan cabang dan akses pusat; dua peran serta pilihan WhatsApp/kapasitas merupakan kebutuhan ARTHA.'),
('3.1.3','J01 J02','Tahapan asli PxP dan contoh penerapan individual.'),
('3.1.4','','Luaran, TKT 5, dan HKI berasal dari panduan ITK 2026, bukan kewajiban yang ditetapkan jurnal.'),
('3.2','J01 J04','Diagram adaptasi PxP dan penambahan evaluasi pengguna; bukan diagram asli yang disalin tanpa perubahan.'),
('3.3','J01 J02 J04','Prosedur pengembangan serta evaluasi; detail pelaksanaan dirancang untuk ARTHA.'),
('3.3.1','J02 J03','Contoh wawancara dan user story; jumlah informan dan cakupan cabang harus dilengkapi.'),
('3.3.2','J01 J02','Estimasi tugas dan rencana iterasi; empat iterasi dua minggu merupakan usulan, bukan angka dari jurnal.'),
('3.3.3','J01','Pemilihan tugas iterasi dan disiplin pencatatan; data uji disusun sendiri.'),
('3.3.4','J01 J02','Desain sederhana, data, dan antarmuka; rancangan aktual disesuaikan kebutuhan.'),
('3.3.5','J01','Urutan tes, kode, dan refaktorisasi; bukti TDD harus dikumpulkan saat implementasi.'),
('3.3.6','J04 J11','Pengujian fungsi dan pembanding validasi batas; semua kasus uji ARTHA merupakan rancangan baru.'),
('3.3.7','J01 J03','Catatan waktu, perubahan, galat, dan evaluasi; tidak menyalin klaim proyek lebih cepat.'),
('3.3.8','J04','Keterlibatan pengguna dan UAT; lembar tugas ARTHA merupakan adaptasi yang perlu validasi isi.'),
('3.4','J05 J06 J07','Pembanding konsep; seluruh artefak merupakan rancangan penelitian ini.'),
('3.4.1','J07 J08 J09','SPP, pencatatan cabang, dan pencocokan bank; tidak membuktikan alur mitra sudah disetujui.'),
('3.4.2','J05 J10 J11','Pembanding kebutuhan, konflik jadwal, kapasitas; mekanisme tautan memakai dokumentasi WhatsApp.'),
('3.4.3','J05 J06','Peran serta kewenangan cabang/pusat; keputusan dua peran berasal dari ruang lingkup ARTHA.'),
('3.4.4','J02','Bentuk user story dan acceptance criteria; isi tabel dirancang sendiri.'),
('3.4.5','J05 J02','Contoh penggunaan use case; diagram dan skenario ARTHA disusun sendiri.'),
('3.4.6','J02 J05 J11','Contoh rancangan data dan validasi; jurnal bukan bukti skema ARTHA sudah 3NF.'),
('3.4.7','J02 J07','Contoh rancangan antarmuka; kesesuaian antarmuka ARTHA perlu dibuktikan melalui UAT.'),
('3.5','J05 J11','Pembanding penerapan Laravel; spesifikasi aktual tidak boleh diisi hanya berdasarkan jurnal.'),
('3.5.1','J05 J11','Pemisahan antarmuka/layanan adalah pilihan rancangan; Next.js, Sanctum, dan notifikasi memakai dokumen resmi.'),
('3.5.2','','Tidak membutuhkan jurnal untuk mengarang perangkat. Diperlukan inventaris perangkat aktual.'),
('3.5.3','J04 J05','Contoh Laravel; nomor versi final dan kompatibilitas harus mengikuti lingkungan serta dokumentasi resmi.'),
('3.5.4','J04 J11','Pembanding pengujian pada perangkat dan peladen; izin, data uji, dan konfigurasi menjadi keputusan penelitian.'),
('3.6','J01','Rentang iterasi dapat dirujuk; jadwal dua belas minggu adalah usulan yang harus disepakati.')]

webrefs=[
('Institut Teknologi Kalimantan','2025a','Panduan Kepenulisan Tugas Akhir ITK',str(ROOT/'PANDUAN TA/[2025] B PANDUAN KEPENULISAN TUGAS AKHIR ITK.pdf')),
('Institut Teknologi Kalimantan','2025b','Template Laporan TA 2025 Prototipe SI',str(ROOT/'TEMPLATE TA/Copy of Template Laporan TA 2025 PROTOTIPE SI.docx.pdf')),
('Institut Teknologi Kalimantan','2026','Panduan TA dan SITASI: Sistem Informasi ITK 2026',str(ROOT/'PANDUAN TA/Panduan TA dan SITASI - Sistem Informasi ITK 2026.pdf')),
('Laravel','t.t.-a','Laravel Sanctum: SPA Authentication','https://laravel.com/framework/docs/12.x/sanctum'),
('Laravel','t.t.-b','Notifications: Database Notifications','https://laravel.com/framework/docs/12.x/notifications'),
('Laravel','t.t.-c','Release Notes and Support Policy','https://laravel.com/framework/docs/releases'),
('Vercel','t.t.','Next.js Documentation: Installation','https://nextjs.org/docs/app/getting-started/installation'),
('WhatsApp','t.t.','How to Use Click to Chat','https://faq.whatsapp.com/5913398998672934')]

bib=['# Daftar pustaka pendamping Bab 3','',
 'Daftar ini memuat sumber yang benar-benar disitasi dalam draf Bab 3. Entri perlu digabungkan dengan pustaka induk laporan melalui pengelola referensi, lalu diberi inden gantung pada Word sesuai panduan ITK.','']
entries=[s['bibliography'] for s in sources]
for name,year,title,url in webrefs:
    if url.startswith('https:'):entries.append(f'{name} ({year}) {title}. Tersedia pada: [{title}]({url}) (Diakses: 25 Oktober 2026).')
    else: entries.append(f'{name} ({year}) {title}. Balikpapan: Institut Teknologi Kalimantan. [Salinan lokal](<{Path(url).as_posix()}>).')
bib+=['\n\n'.join(sorted(entries,key=str.casefold)),'',
 '## Catatan metadata untuk pengelolaan referensi','',
 'Pada Fikri, tahun 2021 dan nama Arthawan Sugih Prabowo mengikuti metadata penerbit; volume 14 nomor 2 tetap merupakan edisi berlabel 2020. Pada Thiovanda, volume dan nomor perlu dilengkapi dari metadata penerbit karena tidak jelas pada PDF, sedangkan tahun dan DOI mengikuti hasil verifikasi terdahulu.','',
 'Singkatan t.t. berarti tanpa tahun pada halaman dokumentasi yang tidak menampilkan tanggal publikasi yang dapat dipastikan. Akhiran a, b, dan c membedakan tiga dokumen Laravel; jangan mengganti t.t. menjadi 2026 hanya karena halaman diakses pada 2026.','']
(OUT/'DAFTAR PUSTAKA BAB 3.md').write_text('\n'.join(bib),encoding='utf-8')

ledger=dict(date='2026-10-25',manuscript='BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md',source_status_scope='Content and page mapping checked now; SINTA coverage follows prior official-record audit except metadata corrections noted; not a fresh all-journal accreditation audit',sources=sources,sections=[dict(section=s,sources=ids.split(),boundary=note) for s,ids,note in mapping],technical_and_guideline_sources=webrefs)
(OUT/'PETA_SUMBER_DAN_SUBBAB.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf-8')

report=['# Checklist jurnal dan sumber untuk Bab 3','',
 '**Kesimpulan:** kumpulan JURNAL sudah memadai sebagai landasan awal metode dan fungsi utama draf Bab 3. Identitas mitra, aturan operasional, spesifikasi perangkat, jadwal, dan hasil evaluasi tetap harus berasal dari data penelitian, bukan diisi seolah telah dibuktikan jurnal.','',
 'Draf memakai dua belas artikel jurnal dan satu prosiding sumber asli PxP. Checklist ini menilai kegunaan isi dan lokator halaman; peringkat SINTA tidak dipakai sebagai pengganti pemeriksaan isi.','',
 '## 1. Arti checklist','',
 '- [x] Sumber tersedia, bagian relevan diperiksa, dan dapat dipakai dalam batas yang dijelaskan.\n- [ ] Data, konfirmasi, atau pemeriksaan tambahan belum tersedia.\n- Tanda selesai pada relevansi isi tidak berarti seluruh kalimat subbab otomatis didukung jurnal.','',
 '## 2. Checklist setiap subbab','',
 '| Subbab | Sumber yang dapat digunakan | Status dan batas penggunaan |',
 '| :--- | :--- | :--- |']
for sec,ids,note in mapping:
    status='[x] Landasan tersedia' if ids else '[ ] Memerlukan sumber primer nonjurnal'
    report.append(f'| {sec} | {ids or "Panduan atau data aktual"} | {status}. {note} |')
report+=['','## 3. Bukti sumber dan halaman','',
 'Nomor PDF merupakan urutan halaman berkas mulai halaman pertama. Nomor cetak merupakan angka yang tertulis pada halaman artikel, sehingga keduanya tidak disamakan.','']
for s in sources:
    loc='; '.join(f"cetak {l['printed']} = PDF {l['pdf_page']}" if l['printed'] else f"PDF {l['pdf_page']} (footer tidak dipakai)" for l in s['locations'])
    uses=[sec for sec,ids,_ in mapping if s['id'] in ids.split()]
    report += [f"### {s['id']}. {s['author']}",'',
      f"- [x] PDF lokal: [{Path(s['file']).name}](<{Path(s['file']).as_posix()}>).",
      '- [x] Lokator: '+loc+'.',
      '- [x] Dapat mendukung: '+s['use'],
      '- Subbab terkait: '+', '.join(uses)+'.',
      '- Batas penggunaan: '+s['limit'],
      '- Status akreditasi arsip: '+s['rank']+'; '+s['rank_scope']+'.',
      '- Catatan periode: '+str(s['rank_note'])+'.',
      f"- Metadata penerbit: [tautan sumber primer]({s['publisher']}).",'']
report+=['## 4. Bagian yang tidak dapat diisi hanya dengan jurnal','',
 '| Kebutuhan | Sumber yang diperlukan | Status |','| :--- | :--- | :--- |',
 '| Nama informan, tanggal wawancara, dan cakupan cabang | Transkrip, rekaman, serta konfirmasi mitra | [ ] Lengkapi tabel identitas dan tanggal |',
 '| WhatsApp manual melalui tombol dan kelas penuh ditolak | Penjelasan pengguna pada percakapan ini, kemudian dokumentasi kebutuhan mitra | [x] Ditetapkan sebagai acuan draf; [ ] arsipkan validasi mitra |',
 '| Pengajuan transfer oleh admin dan keputusan Super Admin | Usulan alur penelitian serta konfirmasi akses rekening dan petugas | [ ] Belum dianggap disetujui mitra |',
 '| Penanganan pembayaran sebagian, tunai, dan setoran | Kebijakan mitra | [ ] Konfirmasi sebelum implementasi |',
 '| Ambang hampir penuh dan kapasitas setiap kelas | Aturan cabang/jenjang dan keputusan pengelola | [ ] Nilai parameter belum diisi sebagai fakta |',
 '| Jumlah peserta serta jadwal UAT | Kesediaan perwakilan mitra | [ ] Tetapkan dan dokumentasikan |',
 '| CPU, RAM, penyimpanan, jaringan, serta versi akhir | Inventaris perangkat dan konfigurasi aplikasi | [ ] Belum tersedia sebagai spesifikasi aktual |',
 '| Kalender kegiatan | Persetujuan jadwal penelitian | [x] Usulan dua belas minggu tersedia; [ ] tanggal kalender belum ditetapkan |',
 '| Pengingat melalui tautan WhatsApp | Dokumentasi resmi WhatsApp | [x] Terverifikasi mekanisme tautan dan pesan terisi |',
 '| Autentikasi, notifikasi, dan kompatibilitas teknologi | Dokumentasi resmi Laravel dan Next.js | [x] Sumber tersedia; [ ] konfigurasi akhir perlu dibekukan |',
 '| TKT 5, HKI, dan struktur enam subbab | Panduan ITK 2026 dan template 2025 | [x] Dimasukkan sebagai target serta rencana, bukan hasil yang sudah tercapai |','',
 '## 5. Sumber yang tidak dipaksakan ke dalam draf','',
 'Artikel Safitri tidak digunakan untuk membuktikan pengingat SPP otomatis karena bukti notifikasinya mempunyai ketidaksesuaian tabel. Artikel Ramadhan tentang keanggotaan/PxP yang tidak ditemukan tidak diganti dengan Ramadhan dan Widodo tentang akuntansi hanya karena nama serta tahunnya serupa.','',
 'Buku teori lama tidak harus dihapus, tetapi tidak ditambahkan jika tidak dibutuhkan klaim dalam Bab 3. Prosiding Dzhurov 2009 tetap relevan sebagai sumber asli PxP, meskipun tidak termasuk terbitan mutakhir dan tidak mempunyai peringkat SINTA nasional.','',
 '## 6. Koreksi terhadap atribusi audit terdahulu','',
 'Audit sebelumnya terlalu cepat menyimpulkan nama Prabowo pada berkas Fikri tidak sesuai. Laman penerbit justru menampilkan nama lengkap I Putu Deny Arthawan Sugih Prabowo dan metadata sitasi tahun 2021; draf ini mengikuti metadata tersebut, sementara label edisinya tetap 2020.','',
 'Daftar pustaka pendamping dan seluruh kemunculan pada draf Bab 3 telah disamakan dengan pilihan ini. Berkas Bab 1 dan Bab 2 lama tidak diubah dalam pekerjaan ini, sehingga konsistensi lintas bab perlu diperbarui saat penggabungan naskah.','']
(OUT/'CHECKLIST JURNAL UNTUK SETIAP SUBBAB BAB 3.md').write_text('\n'.join(report),encoding='utf-8')
print(json.dumps(dict(sources=len(sources),sections=len(mapping),bibliography_entries=len(entries)),ensure_ascii=True))
