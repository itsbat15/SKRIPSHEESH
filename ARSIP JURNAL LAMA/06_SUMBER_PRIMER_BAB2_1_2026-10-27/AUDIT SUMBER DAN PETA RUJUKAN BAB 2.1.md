# Validasi panduan dan kelengkapan sumber Bab 2.1

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
| 2.1.1 Sistem Informasi Manajemen dan Pengembangannya | Cukup untuk dasar | Laudon dan Laudon (2014); Sommerville (2011); Pressman (2010) |
| 2.1.2 Personal Extreme Programming | Cukup untuk dasar | Dzhurov, Krasteva, dan Ilieva (2009); Beck dan Andres (2004) |
| 2.1.3 User Stories | Ada, perlu diperkuat | Beck dan Andres (2004); Cohn (2004), ditambah cuplikan resmi buku dan artikel penulis |
| 2.1.4 Use Case Diagram | Cukup, diperkuat standar | Sommerville (2011); OMG UML 2.5.1 (2017) |
| 2.1.5 Business Process Model and Notation | Belum ada sumber khusus yang memadai | OMG BPMN 2.0.2 (2013), ditambahkan |
| 2.1.6 Class Diagram | Cukup, diperkuat standar | Sommerville (2011); OMG UML 2.5.1 (2017) |
| 2.1.7 Entity Relationship Diagram | Ada, perlu sumber asal dan notasi | Pressman (2010); Chen (1976), ditambah cuplikan penulis; dokumentasi Mermaid untuk notasi implementasi |
| 2.1.8 Next.js | Belum ada dokumentasi primer lokal | Vercel, dokumentasi Next.js; React, Managing State, ditambahkan |
| 2.1.9 Tailwind CSS | Belum ada dokumentasi primer lokal | Tailwind Labs, dokumentasi Tailwind CSS, ditambahkan |
| 2.1.10 Laravel | Ada contoh penerapan, belum cukup untuk teori teknis | Laravel, dokumentasi resmi Sanctum, Authorization, Validation, Database dan Eloquent, ditambahkan |
| 2.1.11 REST API | Belum ada sumber asal REST lokal | Fielding (2000); Fielding, Nottingham, dan Reschke (2022), RFC 9110, ditambahkan |
| 2.1.12 MySQL | Ada contoh penggunaan, perlu manual resmi | Oracle, MySQL 8.4 Reference Manual, ditambahkan sebagai tautan resmi |
| 2.1.13 Black Box Testing | Cukup untuk dasar, diperkuat silabus | Pressman (2010); ISTQB CTFL v4.0.1 (2024), ditambahkan |
| 2.1.14 User Acceptance Testing | Cukup untuk dasar, diperkuat silabus | Sommerville (2011); ISTQB Acceptance Testing v1.0 (2019), ditambahkan |

## 4. Lokator dan batas penggunaan

Nomor cetak dan nomor urut PDF dibedakan agar rujukan mudah diperiksa. Untuk HTML, gunakan judul bagian dan URL; jangan membuat nomor halaman yang tidak tersedia.

### 2.1.1 Sistem Informasi Manajemen dan Pengembangannya

Laudon cetak 45 sampai 48/PDF 47 sampai 50; Sommerville Bab 2, cetak 28 sampai 55/PDF 45 sampai 72, dan cetak 63/PDF 80 untuk pertimbangan pemilihan pendekatan.

Gunakan PDF Laudon edisi ke-13 global tahun 2014. Klaim tahun 2020 atau 2022 harus memakai edisi lain yang memang tersedia, bukan PDF ini.

### 2.1.2 Personal Extreme Programming

Dzhurov cetak 253 sampai 256/PDF 2 sampai 5; Beck salinan digital PDF 109 sampai 110 untuk stories dan siklus mingguan, serta PDF 120 untuk test-first.

Dzhurov merupakan sumber asli PxP berbentuk prosiding, bukan jurnal SINTA. Sidiq dan Apriyanti menjadi contoh penerapan, bukan pengganti sumber dasar.

### 2.1.3 User Stories

Cohn cetak 4 sampai 5/PDF 13 sampai 14 untuk definisi dan tiga aspek; cetak 17/PDF 26 untuk INVEST. Template kalimat tiga bagian dijelaskan dalam artikel resmi Cohn yang ditautkan.

Berkas Cohn hanya bab contoh 61 halaman, bukan buku lengkap. Cohn tidak dinyatakan sebagai pencipta awal seluruh konsep user stories.

### 2.1.4 Use Case Diagram

Sommerville cetak 124 sampai 126/PDF 141 sampai 143; OMG Bab 18, cetak 639 dan seterusnya/PDF 681 dan seterusnya.

Gunakan spesifikasi OMG untuk makna include dan extend. Contoh penerapan jurnal bukan standar notasi UML.

### 2.1.5 Business Process Model and Notation

Bab 7, terutama §7.3.1 dan Tabel 7.1, cetak 26 sampai 28/PDF 56 sampai 58. Halaman sampul menyebut Desember 2013; katalog formal mencatat adopsi Januari 2014.

BPMN bukan bagian UML. Pesan antarpool dan urutan aktivitas di dalam proses tidak boleh digambarkan dengan jenis garis yang sama tanpa mengikuti aturannya.

### 2.1.6 Class Diagram

Sommerville cetak 129 sampai 133/PDF 146 sampai 150; OMG §11.4 Classes, cetak 194 sampai 195/PDF 236 sampai 237 sebagai titik masuk.

Jelaskan atribut, operasi, hubungan, dan multiplicity. Jangan menyamakan class diagram dengan tabel ERD atau membuat diagram yang tidak digunakan pada Bab 3.

### 2.1.7 Entity Relationship Diagram

Pressman cetak 165 sampai 166/PDF 194 sampai 195; Chen cetak 9 sampai 13/PDF 1 sampai 5 pada cuplikan yang tersedia.

Cuplikan Chen hanya lima halaman pertama dari artikel 28 halaman. Notasi Crow’s Foot tidak boleh seluruhnya diatribusikan kepada cuplikan Chen; gunakan dokumentasi notasi yang benar-benar dipakai.

### 2.1.8 Next.js

Dokumentasi Next.js: halaman pengantar dan Layouts and Pages; React: Managing State. Gunakan judul bagian, URL, dan tanggal akses karena halaman HTML tidak memiliki halaman cetak tetap.

Dokumentasi berubah. Bedakan fungsi yang tersedia dalam dokumentasi dari versi dan fitur yang benar-benar dipakai proyek.

### 2.1.9 Tailwind CSS

Styling with Utility Classes dan Responsive Design; lokator menggunakan judul bagian serta URL.

Framework tampilan tidak otomatis membuktikan kemudahan penggunaan, aksesibilitas, atau kepuasan pengguna.

### 2.1.10 Laravel

Sanctum: SPA Authentication; Authorization: Gates dan Policies; Validation: form/input validation; Database: Database Transactions; Eloquent: pengantar model.

Dokumentasi seri 12.x dipakai sebagai referensi versi yang jelas, bukan bukti proyek sudah memakai Laravel 12. Mode SPA Sanctum menggunakan sesi berbasis kuki; token CSRF berbeda dari personal access token.

### 2.1.11 REST API

Fielding Bab 5 dimulai cetak 76/PDF 94; §5.1.3 Stateless cetak 78/PDF 96 dan §5.1.5 Uniform Interface cetak 81/PDF 99. RFC 9110 §9 untuk metode dan §15 untuk status.

Disertasi merupakan sumber asli REST, bukan buku atau jurnal SINTA. HTTP, JSON, dan CRUD saja belum cukup membuktikan seluruh batasan REST dipenuhi; uraikan arsitektur secara jujur.

### 2.1.12 MySQL

General Information; §15.1.20.5 FOREIGN KEY Constraints; §17.7.2 InnoDB Transaction Model. Ketiga halaman diverifikasi lewat layanan web, tetapi unduhan HTML langsung ditolak server.

Pilih versi basis data implementasi yang konsisten. Dukungan transaksi tidak berarti sistem otomatis memenuhi seluruh aturan bisnis atau kepatuhan perbankan.

### 2.1.13 Black Box Testing

Pressman cetak 497 sampai 498/PDF 526 sampai 527; ISTQB §4.2.1 EP halaman 39 dan §4.2.2 BVA halaman 40, sama dengan nomor PDF.

EP dan BVA tidak menggantikan semua skenario alur, perubahan status, otorisasi, atau akses serentak. Tentukan varian BVA dan kaitkan nilai uji dengan aturan yang benar-benar dipilih.

### 2.1.14 User Acceptance Testing

Sommerville cetak 228 sampai 230/PDF 245 sampai 247; ISTQB §1.1.2 halaman 11, §2.1 halaman 15, Bab 3 halaman 19 sampai 21, dan §4.1.2 halaman 25.

UAT tidak selalu memakai Likert. Sullivan dan Artino (2013) ditemukan untuk pendamping analisis Likert bila diperlukan, tetapi bukan sumber awal Likert atau standar ambang kelayakan.

## 5. Sumber primer yang ditambahkan

Tujuh PDF di bawah diperoleh dari situs standar, universitas asal, atau situs penulis. Label lengkap atau cuplikan menunjukkan isi yang benar-benar tersedia; berkas cuplikan tidak diperlakukan sebagai buku atau artikel lengkap.

- [OMG_UML_2.5.1_2017.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/OMG_UML_2.5.1_2017.pdf>); [sumber unduhan](https://www.omg.org/spec/UML/2.5.1/PDF).
- [OMG_BPMN_2.0.2_2013.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/OMG_BPMN_2.0.2_2013.pdf>); [sumber unduhan](https://www.omg.org/spec/BPMN/2.0.2/PDF).
- [Fielding_2000_Disertasi_REST.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/Fielding_2000_Disertasi_REST.pdf>); [sumber unduhan](https://ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf).
- [Chen_1976_ER_Model_CUPLIKAN_5_HALAMAN.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/Chen_1976_ER_Model_CUPLIKAN_5_HALAMAN.pdf>); [sumber unduhan](https://www.csc.lsu.edu/~chen/pdf/erd-5-pages.pdf).
- [Cohn_2004_User_Stories_Applied_BAB_CONTOH_RESMI.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/Cohn_2004_User_Stories_Applied_BAB_CONTOH_RESMI.pdf>); [sumber unduhan](https://cdn.sanity.io/files/qe2cvmjb/production/f5cca0d23709325c8f6c720152230cbaad532bdb.pdf).
- [ISTQB_CTFL_v4.0.1_2024.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/ISTQB_CTFL_v4.0.1_2024.pdf>); [sumber unduhan](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf).
- [ISTQB_Acceptance_Testing_v1.0_2019.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/ISTQB_Acceptance_Testing_v1.0_2019.pdf>); [sumber unduhan](https://istqb.org/wp-content/uploads/2024/11/ISTQB-CT-AcT_Syllabus_v1.0_2019.pdf).

Cuplikan Cohn berjumlah 61 halaman dan meliputi bagian terpilih, bukan seluruh buku; misalnya Bab 6 yang hanya disebut pada daftar isi tidak boleh dinyatakan telah dibaca lengkap. Cuplikan Chen berjumlah lima halaman, yaitu cetak 9 sampai 13 dari artikel asal pada halaman 9 sampai 36.

OMG UML dan BPMN merupakan spesifikasi primer yang otoritatif untuk notasi, tetapi versi yang dipakai bukan berarti versi pertama sepanjang sejarah notasi tersebut. Demikian pula, Cohn (2004) adalah rujukan utama user stories yang dipilih, bukan klaim bahwa Cohn menciptakan user stories.

## 6. Dokumentasi resmi dan hasil penyimpanan

Dokumentasi disimpan sebagai HTML jika server mengizinkan, sedangkan URL tetap menjadi alamat rujukan utama. Salinan lokal tidak menjamin seluruh tautan, skrip, atau tampilan halaman berfungsi tanpa internet.

| Sumber | Status | URL |
| :--- | :--- | :--- |
| Nextjs_Dokumentasi | HTML tersimpan dan judul diperiksa | [Buka sumber](https://nextjs.org/docs) |
| Nextjs_Layouts_Pages | HTML tersimpan dan judul diperiksa | [Buka sumber](https://nextjs.org/docs/app/getting-started/layouts-and-pages) |
| React_Managing_State | HTML tersimpan dan judul diperiksa | [Buka sumber](https://react.dev/learn/managing-state) |
| Tailwind_Utility_Classes | HTML tersimpan dan judul diperiksa | [Buka sumber](https://tailwindcss.com/docs/styling-with-utility-classes) |
| Tailwind_Responsive_Design | HTML tersimpan dan judul diperiksa | [Buka sumber](https://tailwindcss.com/docs/responsive-design) |
| Laravel_12_Sanctum | HTML tersimpan dan judul diperiksa | [Buka sumber](https://laravel.com/docs/12.x/sanctum) |
| Laravel_12_Authorization | HTML tersimpan dan judul diperiksa | [Buka sumber](https://laravel.com/docs/12.x/authorization) |
| Laravel_12_Validation | HTML tersimpan dan judul diperiksa | [Buka sumber](https://laravel.com/docs/12.x/validation) |
| Laravel_12_Database | HTML tersimpan dan judul diperiksa | [Buka sumber](https://laravel.com/docs/12.x/database) |
| Laravel_12_Eloquent | HTML tersimpan dan judul diperiksa | [Buka sumber](https://laravel.com/docs/12.x/eloquent) |
| MySQL_84_Introduction | Tautan saja; server menolak unduhan HTML | [Buka sumber](https://dev.mysql.com/doc/refman/8.4/en/introduction.html) |
| MySQL_84_Transaction_Model | Tautan saja; server menolak unduhan HTML | [Buka sumber](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html) |
| MySQL_84_Foreign_Keys | Tautan saja; server menolak unduhan HTML | [Buka sumber](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html) |
| HTTP_Semantics_RFC9110_2022 | HTML tersimpan dan judul diperiksa | [Buka sumber](https://www.rfc-editor.org/rfc/rfc9110.html) |
| Mermaid_ERD_Notation | HTML tersimpan dan judul diperiksa | [Buka sumber](https://mermaid.js.org/syntax/entityRelationshipDiagram) |
| Cohn_Three_Part_Template | HTML tersimpan dan judul diperiksa | [Buka sumber](https://www.mountaingoatsoftware.com/agile/why-the-three-part-user-story-template-works-so-well) |
| Sullivan_Artino_2013_Likert_OPSIONAL | Tautan saja; respons unduhan berupa pemeriksaan peramban, bukan artikel | [Buka sumber](https://pmc.ncbi.nlm.nih.gov/articles/PMC3886444/) |

Untuk dokumentasi tanpa tahun publikasi yang dapat dipastikan, gunakan penulis lembaga dan t.t. disertai tanggal akses 27 Oktober 2026. Jangan memakai 2026 sebagai tahun publikasi hanya karena halaman diakses pada tahun tersebut; beberapa dokumen lembaga yang sama perlu dibedakan secara konsisten oleh pengelola referensi.

## 7. Kedudukan jurnal SINTA dan sumber nonjurnal

Pekerjaan ini tidak menambahkan jurnal nasional baru karena kekurangan teori lebih tepat dipenuhi oleh sumber asli, standar, dan dokumentasi resmi. Akreditasi SINTA tidak berlaku untuk buku, disertasi, prosiding internasional, spesifikasi OMG, silabus ISTQB, atau dokumentasi perangkat lunak; artikel klasik Chen merupakan artikel internasional sumber awal model ER, bukan jurnal nasional yang diperingkat SINTA.

Jurnal penerapan dalam koleksi dapat dipakai sebagai contoh hasil implementasi apabila klaimnya sesuai dengan isi artikel. Pembaruan pemeriksaan SINTA pada 27 Oktober 2026 telah mengonfirmasi cakupan edisi Apriyanti, INET, Ahadi, Pratama, dan Fikri, sedangkan edisi Sidiq 2025 serta Priatmaja 2022 masih belum terverifikasi.

Laporan terpisah berada pada `JURNAL/VERIFIKASI_ULANG_SINTA_BAB2_1_2026-10-27/HASIL VERIFIKASI SINTA SUMBER BAB 2.1.md`, lengkap dengan keputusan dan halaman bukti. Peringkat historis Multitek edisi 2020 memiliki dasar peringkat 3, sehingga tidak boleh otomatis mengikuti tampilan peringkat jurnal sekarang, yaitu 4.

## 8. Peringatan khusus saat melanjutkan draf yang sudah tersedia

Berkas BAB_2_TINJAUAN_PUSTAKA.md yang sudah ada ternyata belum mengikuti seluruh keputusan susunan terakhir dan masih memuat beberapa klaim komparasi yang telah dikoreksi sebelumnya. Contohnya adalah larangan mutlak perangkapan peran Scrum dan ketidakmungkinan penerapan RAD; penambahan sumber pada pekerjaan ini tidak membuat klaim tersebut menjadi benar.

Gunakan Laudon dan Laudon (2014) untuk PDF edisi ke-13 global yang tersedia. Nama buku atau tahun baru, misalnya Connolly dan Begg (2020), tidak boleh diperlakukan telah tersedia hanya karena ditulis dalam draf; sumber yang benar-benar diperoleh perlu dicatat dan isinya diperiksa.

Rujukan asal REST menjelaskan batasan stateless, sedangkan rancangan autentikasi ARTHA menggunakan sesi. Jelaskan pilihan implementasi secara akurat dan hindari mengklaim semua batasan REST telah dipenuhi hanya karena aplikasi memakai JSON serta endpoint HTTP; keputusan teknis lebih rinci perlu diselaraskan pada Bab 3.

## 9. Hasil dan pekerjaan berikutnya

Setiap subbab kini mempunyai rujukan kerja yang dapat ditelusuri, baik dari koleksi awal maupun sumber primer yang ditambahkan. Hal ini merupakan kesiapan pustaka untuk mulai menulis, bukan pengesahan akhir setiap paragraf, gambar, formula, atau instrumen yang nanti digunakan.

Gunakan panduan revisi pendamping untuk mulai menyusun subbab secara berurutan, kemudian audit klaim dan halaman setelah paragrafnya terbentuk. Naskah Bab 2 yang sudah ada, Bab 1, dan Bab 3 tidak diubah oleh pekerjaan ini.

## 10. Tautan sumber lokal utama yang sudah tersedia

Sumber berikut tetap dipakai tanpa digandakan atau diubah. Nomor halaman relevan sudah dipetakan pada Bagian 4.

- [1666784540laudon-management-information-systems-13th-global-edition-c2014-1.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/1666784540laudon-management-information-systems-13th-global-edition-c2014-1.pdf>)
- [Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf>)
- [ebook-pressman-sw-engineering.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/ebook-pressman-sw-engineering.pdf>)
- [Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf>)
- [Personal Extreme Programming - Agile for Autonomous Developer - S3T 2009 - Dzhurov dkk - 2009.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal Extreme Programming - Agile for Autonomous Developer - S3T 2009 - Dzhurov dkk - 2009.pdf>)


## 11. Pembaruan kelengkapan berkas setelah pemeriksaan lanjutan

Manual MySQL 8.4 lengkap kini tersedia melalui situs resmi Oracle, meskipun unduhan langsung dari downloads.mysql.com ditolak. Salinan ini memiliki 6.438 halaman, mendokumentasikan seri 8.4 sampai 8.4.9, dan mencantumkan tanggal pembentukan dokumen 21 April 2026; salinan ini tidak dinyatakan sebagai manual patch terbaru pada situs MySQL.

Rujukan awal yang telah diperiksa adalah What is MySQL pada cetak 4/PDF 36, InnoDB and the ACID Model pada cetak 3152/PDF 3184, serta InnoDB Transaction Model pada cetak 3234/PDF 3266. Status tautan saja pada Bagian 6 merupakan catatan percobaan awal dan tidak lagi berarti bahwa manual MySQL belum tersedia secara lokal.

[Manual MySQL resmi Oracle](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/06_SUMBER_PRIMER_BAB2_1_2026-10-27/MySQL_8.4_Reference_Manual_ORACLE_RESMI.pdf>) menjadi salinan baca lokal. Untuk kode spesifik patch, rujukan harus tetap dicocokkan dengan versi yang benar-benar dipasang pada proyek.
