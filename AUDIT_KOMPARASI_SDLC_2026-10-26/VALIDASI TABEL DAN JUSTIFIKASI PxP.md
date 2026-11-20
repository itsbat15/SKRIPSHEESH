# Validasi tabel komparasi SDLC dan justifikasi pemilihan PxP

Pemeriksaan dilakukan pada 26 Oktober 2026 terhadap Bagian 3 dalam `KOMPARASI_DAN_JUSTIFIKASI_METODE_SDLC.md`, khususnya baris 588 sampai 597. Berkas asal dipertahankan, sedangkan koreksi dan usulan pengganti disajikan dalam dokumen ini.

## 1. Kesimpulan pemeriksaan

Tabel belum layak digunakan tanpa revisi karena beberapa klaim bertentangan dengan sumber, terlalu mutlak, atau menggunakan nomor halaman yang tidak sesuai. Pemilihan PxP masih masuk akal untuk ARTHA, tetapi tabel saat ini lebih menyerupai pembenaran atas pilihan yang sudah ditentukan daripada perbandingan yang berimbang.

Pernyataan bahwa hanya PxP yang sah secara akademik, metode lain cacat, dan PxP menjamin kualitas perlu dihapus. Literatur mendukung kesesuaian karakteristik proses dengan konteks proyek, bukan kemenangan mutlak satu metode untuk seluruh proyek mandiri.

Terdapat delapan dimensi dan lima pendekatan, sehingga pemeriksaan berikut mencakup empat puluh sel isi. Status “didukung” berarti pokok uraian sesuai sumber yang diperiksa, bukan bukti bahwa metode tersebut pasti berhasil pada ARTHA.

## 2. Sumber dan lokator pemeriksaan manual

Nomor halaman PDF dihitung dari halaman pertama berkas, sedangkan halaman tercetak mengikuti angka di dalam halaman. Kode S1 sampai S10 di bawah merupakan indeks audit agar tabel temuan dapat dibaca dengan ringkas.

| Kode | Sumber yang benar dan bagian yang diperiksa | Halaman tercetak | Halaman PDF |
| :--- | :--- | :--- | :--- |
| S1 | Sommerville (2011), *Software Engineering*, edisi kesembilan, §2.1.1 Waterfall | 30 sampai 32 | 47 sampai 49 |
| S2 | Sommerville (2011), §3.2 pemilihan pendekatan dan §3.3 XP | 63 sampai 65 | 80 sampai 82 |
| S3 | Pressman (2010), *Software Engineering: A Practitioner's Approach*, edisi ketujuh, halaman yang dipakai tabel sebagai dukungan RAD | 45 sampai 47 | 74 sampai 76 |
| S4 | Pratama, E. A., Krisgianti, S., dan Paramita, H. M. (2023), artikel inventaris aset Desa Rempoah, §3.2 dan Gambar 2 | 53 sampai 54; identitas artikel pada 49 | 5 sampai 6; identitas pada 1 |
| S5 | Schwaber dan Sutherland (2020), *The Scrum Guide*, Scrum Team, Sprint, Daily Scrum, Artifacts, Increment, Definition of Done | 5; 7; 9 sampai 12 | 6; 8; 10 sampai 13 |
| S6 | Beck dan Andres (2004), *Extreme Programming Explained*, edisi kedua, pembahasan perubahan cakupan XP, Sit Together, Pair Programming, Weekly Cycle, Test-First Programming | Penomoran cetak tidak tersedia secara konsisten pada salinan digital ini | 40; 95 sampai 96; 104 sampai 105; 110 sampai 111; 120 |
| S7 | Dzhurov, Krasteva, dan Ilieva (2009), *Personal Extreme Programming: An Agile Process for Autonomous Developers* | 252 sampai 258 | 1 sampai 7 |
| S8 | Royce (1970), *Managing the Development of Large Software Systems*, kritik alur sederhana, umpan balik, dan pelibatan pelanggan | 329 sampai 330; bagian akhir tentang pelanggan | 2 sampai 3; telusuri subjudul Customer pada berkas |
| S9 | Sidiq, A. L., Marthasari, G. I., dan Aminudin (2025), *Implementasi Metode Personal Extreme Programming Pada Pengembangan Sistem Informasi Surat Menyurat*, Jurnal Jaring SainTek 7(1), 35 sampai 46 | Identitas dan abstrak pada 35; halaman 48 tidak terdapat pada artikel ini | 1 dari 12 halaman |
| S10 | Kurniawan, I., dan Sani, R. R. (2019), *Pemodelan SCRUM dalam Pengembangan Sistem Informasi Kesehatan pada Klinik Ar-Rokhim Sragen Kabupaten Sragen*, Journal of Information System 4(1), 76 sampai 86 | Identitas pada 76; halaman 149 tidak terdapat pada artikel ini | 1 dari 11 halaman |

Salinan teks per halaman disimpan dalam `TEKS_SUMBER_PER_HALAMAN.json` dan `TEKS_SUMBER_PER_HALAMAN_PDFIUM.json`. Gambar `BUKTI_HALAMAN.png` menampilkan halaman Pressman, RAD, PxP, dan Scrum yang membantu memeriksa temuan utama.

## 3. Audit empat puluh sel tabel

### 3.1 Waterfall

| Dimensi | Status | Temuan dan koreksi | Rujukan |
| :--- | :--- | :--- | :--- |
| Ukuran tim dan peran | Tidak didukung | Waterfall tidak menetapkan tim harus menengah atau besar serta tidak mewajibkan sekat departemen. Halaman 32 juga memuat contoh Cleanroom yang tidak boleh digeneralisasikan menjadi struktur wajib Waterfall. | S1, cetak 31 sampai 32, PDF 48 sampai 49 |
| Tahapan | Didukung dengan koreksi atribusi | Lima tahap sesuai Sommerville. Diagram Royce memuat susunan yang lebih terperinci, sehingga jangan menyebut kedua sumber memberikan lima tahap yang sama. | S1, cetak 31/PDF 48; S8, PDF 2 |
| Perubahan kebutuhan | Sebagian didukung | Pembagian fase menyulitkan perubahan dan dapat menimbulkan pengerjaan ulang. Kata “ditolak” dan biaya “sangat mahal” sebagai kepastian harus diganti dengan risiko biaya dan perubahan dokumen. | S1, cetak 31 sampai 32/PDF 48 sampai 49 |
| Rilis dan umpan balik | Terlalu mutlak | Penyerahan sistem lengkap umumnya mengikuti integrasi dan pengujian, tetapi tidak berarti pengguna dilarang melihat artefak sebelumnya. Royce justru mengkritik pengujian terlambat dan membahas perbaikan alur. | S1, cetak 31/PDF 48; S8, PDF 2 sampai 3 |
| Keterlibatan pengguna | Sebagian didukung | Konsultasi pengguna dilakukan pada kebutuhan. Tidak ada dasar untuk menyatakan komunikasi hanya boleh pada awal dan akhir. | S1, cetak 31/PDF 48 |
| Kualitas | Tidak lengkap | Waterfall pada sumber mencakup uji unit serta integrasi dan uji sistem. Menggambarkannya hanya sebagai pengujian fungsional akhir mengabaikan uji unit. | S1, cetak 31/PDF 48 |
| Dokumentasi | Sebagian didukung | Dokumen setiap tahap dan persetujuan memang dijelaskan. Keharusan dokumen “tebal” serta penandatanganan bersama untuk setiap proyek tidak didukung. | S1, cetak 31/PDF 48 |
| Kelayakan ARTHA | Kesimpulan terlalu mutlak | Kurang diprioritaskan ketika aturan bisnis masih memerlukan klarifikasi. Tidak ada dasar menyimpulkan semua penerapan Waterfall tidak layak atau pasti gagal. | S1 dan interpretasi terhadap keputusan ARTHA |

### 3.2 RAD

| Dimensi | Status | Temuan dan koreksi | Rujukan |
| :--- | :--- | :--- | :--- |
| Ukuran tim dan peran | Salah rujukan | Pressman cetak 46 membahas Spiral. Klaim beberapa tim paralel bukan ketentuan yang dibuktikan oleh halaman tersebut ataupun artikel RAD yang dipakai. | S3, cetak 46/PDF 75; S4 |
| Tahapan | Pokoknya didukung, lokator perlu diperbaiki | Tiga ruang siklus ditampilkan pada cetak 54: perencanaan syarat, workshop desain, dan implementasi. Analisis serta desain dijelaskan di dalam workshop; rentang 51 sampai 54 terlalu luas untuk menunjuk tahapan. | S4, cetak 54/PDF 6 |
| Perubahan kebutuhan | Salah rujukan | Pressman cetak 46 bukan pembahasan RAD. Artikel RAD mendukung perulangan analisis dan desain sampai rancangan dihasilkan, tanpa pembatasan perubahan hanya boleh dalam jadwal workshop tertentu. | S3; S4, cetak 54/PDF 6 |
| Rilis dan umpan balik | Tidak terverifikasi dari sumber yang ditunjuk | Angka 60 sampai 90 hari tidak dibuktikan oleh Pressman cetak 45 karena halaman itu membahas Spiral. Durasi pembangunan proyek juga berbeda dari frekuensi rilis. | S3, cetak 45/PDF 74 |
| Keterlibatan pengguna | Sebagian didukung | Demonstrasi rancangan kepada pengguna didukung. Kewajiban hadir terus-menerus tidak dinyatakan pada halaman 52 yang justru membahas teori sistem dan aset. | S4, cetak 52 dan 54/PDF 4 dan 6 |
| Kualitas | Salah rujukan dan terlalu sempit | Pressman cetak 47 membahas Spiral. Artikel RAD menyebut pengujian pada rancangan dan prototipe, bukan kualitas semata-mata bergantung pada pustaka siap pakai. | S3, cetak 47/PDF 76; S4, cetak 54/PDF 6 |
| Dokumentasi | Tidak didukung sebagai peringkat umum | Artikel memperlihatkan artefak dan tahapan penelitian. Artikel tidak menetapkan beban dokumentasi semua proyek RAD pasti “sedang”. | S4, cetak 53 sampai 54/PDF 5 sampai 6 |
| Kelayakan ARTHA | Tidak cukup bukti | Kesibukan mitra tidak membuktikan workshop mustahil. Alasan yang lebih relevan adalah penelitian membutuhkan disiplin teknis dan pencatatan personal yang belum dirinci dalam model RAD yang dibandingkan. | S4 dibandingkan dengan S7; jadwal mitra harus dikonfirmasi |

### 3.3 Scrum

| Dimensi | Status | Temuan dan koreksi | Rujukan |
| :--- | :--- | :--- | :--- |
| Ukuran tim dan peran | Keliru | Panduan 2020 menyebut biasanya sepuluh orang atau kurang, bukan tiga sampai sembilan. Panduan tidak memuat larangan mutlak perangkapan yang dinyatakan tabel; Product Owner atau Scrum Master yang mengerjakan Sprint Backlog dapat ikut sebagai Developers. | S5, cetak 5 dan 9/PDF 6 dan 10 |
| Tahapan | Sebagian didukung | Empat acara berlangsung di dalam Sprint; Sprint sendiri juga merupakan acara. Batas resmi Sprint adalah satu bulan atau kurang, bukan minimum wajib satu minggu. Acara Scrum bukan urutan fase analisis, desain, dan implementasi. | S5, cetak 7 sampai 10/PDF 8 sampai 11 |
| Perubahan kebutuhan | Bertentangan dengan sumber | Yang dilindungi adalah Sprint Goal. Cakupan dapat diklarifikasi dan dinegosiasikan bersama Product Owner selama tujuan tersebut tidak terancam. | S5, cetak 7 dan 11/PDF 8 dan 12 |
| Rilis dan umpan balik | Sebagian didukung | Increment harus dapat digunakan dan memenuhi Definition of Done. Penyerahan dapat dilakukan sebelum Sprint berakhir, sehingga akhir Sprint bukan satu-satunya waktu rilis. | S5, cetak 11 sampai 12/PDF 12 sampai 13 |
| Keterlibatan pengguna | Terlalu mutlak | Sprint Review melibatkan pemangku kepentingan. Panduan tidak mewajibkan Product Owner hadir mendampingi pengembang setiap hari; Daily Scrum ditujukan kepada Developers. | S5, cetak 9/PDF 10 |
| Kualitas | Pokoknya didukung | Definition of Done dan tanggung jawab mutu jelas. Scrum tidak menetapkan teknik pengodean tertentu, tetapi tetap dapat dipadukan dengan TDD, integrasi berkelanjutan, dan peninjauan kode. | S5, cetak 5 dan 12/PDF 6 dan 13 |
| Dokumentasi | Keliru | Tiga artefak adalah Product Backlog, Sprint Backlog, dan Increment. Burndown merupakan pilihan pemantauan, bukan pengganti Increment atau artefak wajib keempat. | S5, cetak 8 dan 10 sampai 12/PDF 9 dan 11 sampai 13 |
| Kelayakan ARTHA | Tidak didukung | Hapus label cacat metodologis berdasarkan larangan peran yang tidak ada. Scrum kurang diprioritaskan sebagai kerangka utama karena kebutuhan utama penelitian adalah pengendalian pekerjaan dan kualitas pengembang individual; praktik rekayasa tambahan tetap perlu dirumuskan. | S5 dibandingkan dengan S7; penilaian kontekstual |

### 3.4 Extreme Programming

| Dimensi | Status | Temuan dan koreksi | Rujukan |
| :--- | :--- | :--- | :--- |
| Ukuran tim dan peran | Sebagian didukung | Pair Programming memang praktik utama. Batas mutlak dua sampai sepuluh anggota tidak didukung oleh Beck edisi kedua, yang membahas penerapan XP pada beragam ukuran tim. | S6, PDF 40 dan 104 sampai 105 |
| Tahapan | Atribusi tidak tepat | Ringkasan empat kegiatan umum tidak otomatis merupakan empat tahap baku Beck edisi kedua. Gunakan siklus rilis XP Sommerville cetak 65 atau jelaskan bahwa tabel merangkum praktik, bukan mengutip diagram empat tahap dari Beck. | S2, cetak 65/PDF 82; S6, Bab 7 |
| Perubahan kebutuhan | Sebagian didukung | XP menerima perubahan melalui siklus pendek dan desain yang dapat disesuaikan. Perubahan tetap menggunakan waktu dan upaya; klaim tanpa penalti biaya desain dihapus. | S6, PDF 40 dan 110 sampai 111 |
| Rilis dan umpan balik | Rentang tidak tepat untuk edisi rujukan | Beck edisi kedua menjelaskan Weekly Cycle. Salinan yang diperiksa pada PDF 110 secara eksplisit membedakannya dari dua atau tiga minggu yang dianjurkan pada edisi pertama. | S6, PDF 110 sampai 111 |
| Keterlibatan pengguna | Sebagian didukung, berlebihan | Kolaborasi pelanggan penting, tetapi tidak boleh disederhanakan menjadi kewajiban semua pengguna duduk di meja kerja setiap hari. Beck juga membahas bahwa tim terdistribusi dapat menerapkan XP. | S6, PDF 95 sampai 96; S2, cetak 65/PDF 82 |
| Kualitas | Pokok praktik benar, sumber kurang tepat | Test-first, refaktorisasi, dan pairing didukung literatur XP. Artikel Williams tentang pairing tidak sendirian membuktikan keseluruhan aturan TDD dan refaktorisasi XP. | S6, PDF 104 dan 120; S2, cetak 65/PDF 82 |
| Dokumentasi | Sebagian didukung | Cerita pengguna dan pengujian penting. Menetapkan beban pasti sangat ringan mengabaikan dokumen yang tetap dibutuhkan untuk desain, serah terima, dan pelaporan TA. | S2, cetak 63 dan 65/PDF 80 dan 82 |
| Kelayakan ARTHA | Terlalu mutlak | Penyesuaian XP untuk individu tetap mungkin. PxP lebih langsung menyediakan adaptasi personal beserta pencatatan kerja dan retrospeksi, sehingga alasan memilihnya adalah kesesuaian adaptasi, bukan ketidaksahan XP. | S6; S7, cetak 253 sampai 256/PDF 2 sampai 5 |

### 3.5 Personal Extreme Programming

| Dimensi | Status | Temuan dan koreksi | Rujukan |
| :--- | :--- | :--- | :--- |
| Ukuran tim dan peran | Didukung | Ditujukan bagi pengembang individual. Jumlah penulis artikel atau delapan cabang pengguna tidak sama dengan jumlah pengembang. | S7, cetak 252 sampai 253/PDF 1 sampai 2 |
| Tahapan | Didukung | Tujuh fase dan tiga subfase implementasi terlihat pada Gambar 1. Perencanaan dan kebutuhan dapat ditinjau ulang jika kebutuhan berubah. | S7, cetak 254 sampai 256/PDF 3 sampai 5 |
| Perubahan kebutuhan | Didukung dengan batasan | Rencana tugas dapat direvisi. Sumber juga menyatakan kebutuhan biasanya ditentukan terlebih dahulu dan relatif stabil, sehingga jangan menggambarkan PxP sebagai proses tanpa perencanaan awal. | S7, cetak 254/PDF 3 |
| Rilis dan umpan balik | Sebagian didukung | Iterasi dapat berlangsung satu sampai tiga minggu dan dapat menghasilkan kandidat rilis atau versi rilis. Tidak setiap iterasi dijamin menjadi modul siap dipakai operasional. Sitasi Ramadhan yang ditunjuk tidak ditemukan. | S7, cetak 255 sampai 256/PDF 4 sampai 5 |
| Keterlibatan pengguna | Interpretasi ARTHA, bukan aturan sumber | Sumber memberi dasar kebutuhan dan pemeriksaan kesesuaian. Tidak ada jaminan PxP tidak membebani mitra atau ketentuan mitra hanya boleh dilibatkan pada akhir iterasi; jadwal validasi harus disepakati. | S7, cetak 254 sampai 256/PDF 3 sampai 5 |
| Kualitas | Praktik didukung, hasil tidak dijamin | TDD, Coding Standard, Code Reviews, dan Defect Recording tercantum. Tingkat kualitas tetap harus dibuktikan melalui hasil pengujian, bukan disimpulkan dari nama metode. | S7, cetak 253 sampai 255/PDF 2 sampai 4 |
| Dokumentasi dan metrik | Pokoknya didukung | Catatan durasi, cacat, dan usulan perbaikan memang dipakai. Kata “ilmiah” tidak menjadikannya lebih unggul otomatis; Sidiq halaman 48 merupakan lokator yang tidak sesuai artikel. | S7, cetak 254 sampai 257/PDF 3 sampai 6; S9 |
| Kelayakan ARTHA | Kesimpulan terlalu mutlak | PxP merupakan pilihan yang dapat dipertanggungjawabkan bila praktiknya benar-benar dilaksanakan. Sumber tidak menetapkan PxP sebagai satu-satunya metode sah, tidak menjamin bebas cacat, dan tidak memastikan kesesuaian waktu mitra. | S7, terutama cetak 256 sampai 258/PDF 5 sampai 7 |

## 4. Masalah identitas sumber yang harus dibereskan

Beberapa kekeliruan bersifat bibliografis, sedangkan satu berkas memiliki isi yang berbeda dari judul pada namanya. Pemeriksaan ini menilai PDF yang benar-benar tersedia, sehingga nama berkas tidak diperlakukan sebagai bukti identitas artikel.

| Rujukan dalam dokumen | Hasil pemeriksaan PDF | Tindakan |
| :--- | :--- | :--- |
| Pratama, B. C., Hidayat, dan Nurfaizah | PDF inventaris aset Desa Rempoah ditulis Eva Argarini Pratama, Sinta Krisgianti, dan Hanny Mitya Paramita. Tahun 2023, Infotek 6(1), 49 sampai 59, DOI 10.29408/jit.v6i1.7313. | Ganti nama penulis pada daftar pustaka. Bentuk singkat Pratama dkk. dapat dipertahankan setelah entri lengkap benar. |
| Fikri, M. R. dan Prabowo, R. D. A., Jurnal Sistem Informasi ITK | PDF memuat Ahmad Maulana Fikri dan I Putu Deny Arthawan S. P., pada Multitek Indonesia 14(2), edisi Desember 2020. Identitas ini berbeda dari nama penulis dan nama jurnal yang ditulis dalam komparasi. | Cocokkan dengan metadata penerbit. Tahun edisi 2020 dan tanggal terbit daring 2021 perlu dipilih secara konsisten; jangan menyalin identitas penulis yang keliru. |
| Sidiq, U., Prabowo, dan Hidayat, Jurnal Ilmiah Komputasi 24(1), 45 sampai 56 | PDF memuat Alfin Lutfi Sidiq, Gita Indah Marthasari, dan Aminudin; Jurnal Jaring SainTek 7(1), 35 sampai 46. | Perbaiki identitas serta halaman. Hapus lokator 48 karena berada di luar rentang artikel. |
| Kurniawan, D. dan Sani, klinik gigi Semarang, 4(2), 146 sampai 156 | PDF memuat Ikhwansyah Kurniawan dan Ramadhan Rakhmat Sani, klinik Ar-Rokhim Sragen, 4(1), 76 sampai 86. | Perbaiki penulis, judul, lokasi studi, edisi, dan halaman. Lokator 149 tidak berlaku. |
| Mishra dan Alzoubi, Software Quality Journal 31, 881 sampai 923 | PDF yang tersedia adalah *Structured software development versus agile software development: a comparative analysis*, International Journal of System Assurance Engineering and Management 14(4), 1504 sampai 1522, DOI 10.1007/s13198-023-01958-5. | Ganti metadata dan cari ulang lokator. Halaman 886 tidak merujuk halaman tercetak PDF ini. |
| Fahrijal dan Hartawan, “Perbandingan XP vs PxP”, 154 sampai 162 | Isi PDF adalah *Perancangan Aplikasi Web Pengawasan Perangkat NTE oleh Teknisi di Unit Warehouse PT. Telkom Akses Jakarta Pusat*, Taufik Fahrijal dan Rumadi Hartawan, Jurnal Manajemen Informatika Jayakarta 4(4), 367 sampai 382. Abstraknya menyebut metode prototype. | Jangan gunakan sebagai bukti perbandingan XP dengan PxP. Berkas tetap dipertahankan, tetapi entri komparatifnya harus dikeluarkan atau diganti sumber yang benar. |
| Asri, Fajri, dan Syahrul, 284 sampai 288 | PDF memuat *Comparing Traditional and Agile Software Development Approaches: Case of Personal Extreme Programming*, Sri Andriati Asri, I Gusti Made Agung Sunaya, Putu Manik Prihatini, dan Widyadi Setiawan; halaman pertama 561. | Perbaiki penulis dan judul. Jangan menggunakan halaman 286 untuk PDF ini. |
| Ramadhan (2026), keanggotaan dan penjadwalan PxP, halaman 92 | Berkas yang ditautkan tidak ditemukan pada folder JURNAL saat pemeriksaan. | Tandai belum terverifikasi dan lepaskan dukungannya dari tabel sampai dokumen tersedia. |

Daftar tersebut bukan audit akreditasi SINTA. Artikel jurnal, prosiding konferensi, buku, dan panduan resmi tetap harus dibedakan jenis sumbernya.

## 5. Usulan tabel pengganti

Tabel berikut merangkum temuan yang dapat dipertanggungjawabkan tanpa memberi nilai kemenangan sebelum pelaksanaan penelitian. Seluruh penilaian khusus ARTHA pada baris terakhir merupakan pertimbangan peneliti yang perlu diselaraskan dengan data lapangan.

| Dimensi | Waterfall | RAD, model pada Pratama dkk. | Scrum 2020 | XP | PxP |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Fokus proses | Pengembangan melalui fase yang direncanakan dan didokumentasikan (S1). | Percepatan pengembangan melalui perencanaan, workshop rancangan, dan implementasi (S4). | Kerangka pengelolaan produk adaptif melalui Sprint dan inspeksi bersama (S5). | Pengembangan iteratif dengan kolaborasi dan praktik rekayasa yang saling mendukung (S2, S6). | Pengendalian pekerjaan pengembang individual melalui praktik XP dan disiplin personal (S7). |
| Struktur pelaksana | Model tidak menentukan jumlah minimum pengembang (S1). | Artikel yang diperiksa tidak menentukan jumlah minimum atau kewajiban tim paralel (S4). | Scrum Team memiliki tiga akuntabilitas, dengan ukuran biasanya sepuluh orang atau kurang (S5). | Pair Programming merupakan praktik utama; ukuran tim bukan batas mutlak dua sampai sepuluh orang (S6). | Secara eksplisit ditujukan bagi pengembang individual (S7). |
| Pengaturan kegiatan | Lima tahap dari analisis kebutuhan sampai operasi dan pemeliharaan (S1). | Perencanaan syarat, workshop analisis dan desain, serta implementasi (S4). | Sprint memuat Planning, Daily Scrum, Review, dan Retrospective (S5). | Cerita pengguna, perencanaan singkat, pengembangan, integrasi, pengujian, dan rilis (S2, S6). | Requirements, Planning, Iteration Initialization, Design, Implementation, System Testing, Retrospective (S7). |
| Penanganan perubahan | Perubahan dimungkinkan, tetapi dapat memerlukan revisi dokumen dan pengulangan fase (S1). | Analisis dan desain dapat diulang sampai rancangan yang diperlukan diperoleh (S4). | Cakupan dapat dinegosiasikan selama tidak membahayakan Sprint Goal (S5). | Kebutuhan diprioritaskan dalam siklus pendek; perubahan tetap membutuhkan upaya (S6). | Rencana tugas dapat ditinjau ulang jika kebutuhan berubah (S7). |
| Hasil dan umpan balik | Penyerahan sistem mengikuti integrasi dan pengujian; artefak tahap sebelumnya tetap dapat ditinjau (S1). | Rancangan ditunjukkan kepada pengguna dan prototipe diuji (S4). | Increment memenuhi Definition of Done dan dapat diserahkan sebelum akhir Sprint (S5). | Weekly Cycle pada Beck edisi kedua mengarahkan perangkat lunak yang dapat disebarkan pada akhir minggu (S6). | Iterasi satu sampai tiga minggu dapat menghasilkan kandidat rilis atau versi rilis (S7). |
| Pengendalian kualitas | Uji unit, integrasi, dan uji sistem merupakan bagian proses (S1). | Artikel menyebut pengujian aplikasi dan kesesuaian prototipe; teknik tambahan perlu dirumuskan (S4). | Definition of Done menetapkan ukuran kualitas; teknik rekayasa dipilih sesuai kebutuhan (S5). | Test-first, pairing, integrasi, dan perbaikan desain mendukung kualitas (S2, S6). | TDD, standar kode, peninjauan personal, serta pencatatan dan perbaikan cacat mendukung kualitas (S7). |
| Catatan proses | Dokumen hasil fase dan persetujuan perkembangan proses (S1). | Artefak rancangan dan pengujian mengikuti kebutuhan pengembangan yang dijelaskan artikel (S4). | Product Backlog, Sprint Backlog, Increment, beserta komitmennya (S5). | Cerita pengguna, rencana siklus, dan pengujian; dokumentasi proyek tetap dapat ditambahkan (S2, S6). | Rencana tugas, durasi aktual, cacat, dan usulan perbaikan proses (S7). |
| Pertimbangan ARTHA | Kurang diprioritaskan bila aturan bisnis belum cukup stabil. | Tetap mungkin, tetapi rancangan penelitian harus menambahkan disiplin rekayasa serta pencatatan personal yang diperlukan. | Tetap mungkin dengan pengaturan akuntabilitas dan kegiatan yang nyata; kebutuhan utama penelitian lebih dekat pada proses rekayasa personal. | Tetap mungkin melalui adaptasi, tetapi adaptasi personalnya harus dijelaskan dan dibuktikan. | Dipilih karena tersedia hubungan langsung antara perencanaan tugas individual, implementasi teruji, pemeriksaan sistem, dan evaluasi proses. |

Dalam naskah proposal, kode indeks S1 sampai S7 perlu diganti dengan sitasi Author-Year sesuai baris sumber di Bagian 2. Indeks dipakai di sini untuk memudahkan audit, bukan sebagai gaya sitasi akhir skripsi.

## 6. Alasan kuat memilih PxP selain jumlah pengembang

### 6.1 Pengendalian risiko perubahan aturan bisnis

Aturan verifikasi transfer, pembayaran sebagian, penyerahan tunai, dan ambang hampir penuh masih memiliki keputusan yang perlu dikonfirmasi. PxP menyediakan revisi rencana tugas ketika kebutuhan berubah serta siklus implementasi dan pemeriksaan yang dapat diulang (Dzhurov dkk., 2009, hlm. 254 sampai 256).

Alasan ini mendukung pemilihan proses iteratif, tetapi belum membedakan PxP dari Scrum, XP, atau RAD secara sendirian. Pembeda yang lebih kuat adalah penggabungannya dengan perencanaan tugas personal, catatan durasi, serta pemeriksaan cacat dalam satu proses yang memang dirumuskan untuk individu.

### 6.2 Pengujian aturan transaksi sejak implementasi

Risiko ARTHA tidak hanya terletak pada tampilan formulir, tetapi juga pada saldo, status pembayaran, batas akses cabang, dan kapasitas kelas. Praktik TDD serta pengujian sistem pada PxP memberikan tempat yang jelas untuk menguji aturan tersebut sebelum modul dinyatakan selesai (Dzhurov dkk., 2009, hlm. 254 sampai 256).

Contohnya adalah pengujian bahwa transfer berstatus submitted belum mengurangi tagihan dan kelas penuh menolak penambahan siswa. Pengujian integrasi serta akses serentak tetap perlu dirancang karena uji unit tidak membuktikan seluruh perilaku sistem; TDD juga tersedia dalam XP dan dapat ditambahkan pada Scrum atau RAD.

### 6.3 Estimasi berdasarkan pekerjaan teknis dan perbaikan estimasi

Kebutuhan seperti pencatatan transfer dapat dipecah menjadi validasi masukan, penyimpanan bukti, pembatasan akses, pemeriksaan status, dan pengujian. PxP menghubungkan tugas teknis tersebut dengan estimasi dan durasi aktual, sehingga keterlambatan dapat ditelusuri secara lebih konkret daripada hanya menyebut persentase modul selesai (Dzhurov dkk., 2009, hlm. 254 sampai 256).

Data historis proyek sebelumnya tidak harus dibuat-buat jika belum tersedia. Sumber asli mengizinkan estimasi terbaik pada awalnya, kemudian data pekerjaan nyata dipakai untuk memperbaiki estimasi berikutnya pada retrospeksi, sebagaimana dijelaskan pada halaman 255.

### 6.4 Validasi hasil bertahap yang masih terintegrasi

Pekerjaan dapat diatur berdasarkan alur yang dapat diperiksa, misalnya siswa dan kelas, tagihan dan pembayaran, lalu penerimaan pusat dan laporan. PxP menyediakan iterasi yang dapat menghasilkan kandidat rilis, sehingga rancangan dapat dibahas bersama mitra sebelum seluruh pengembangan selesai (Dzhurov dkk., 2009, hlm. 255 sampai 256).

Urutan tersebut merupakan rancangan ARTHA, bukan urutan modul wajib dalam teori PxP. Setiap iterasi tetap harus menguji fitur yang sudah dibuat bersama fitur baru agar integrasi antarmodul tidak terabaikan.

### 6.5 Keterlacakan pelaksanaan penelitian

Catatan kebutuhan, tugas, perubahan, hasil uji, durasi, dan cacat dapat menunjukkan apa yang dikerjakan serta alasan revisinya. PxP secara eksplisit memelihara log selama proses dan menggunakan data tersebut untuk retrospeksi, sehingga bukti pelaksanaan dapat dikaitkan dengan keputusan perancangan (Dzhurov dkk., 2009, hlm. 254 sampai 256).

Manfaat ini bukan bukti bahwa PxP otomatis lebih ilmiah daripada metode lain. Kekuatan akademiknya baru muncul jika catatan benar-benar dibuat selama pengerjaan, konsisten dengan versi kode, dan digunakan dalam pembahasan hasil.

### 6.6 Besarnya penyesuaian proses yang perlu dilakukan

RAD dan Scrum tetap dapat digunakan, tetapi peneliti masih perlu merinci bagaimana praktik pengodean, pemeriksaan personal, serta pencatatan estimasi dilaksanakan dalam konteks penelitian ini. XP lebih dekat dengan kebutuhan teknis tersebut, sedangkan PxP telah merumuskan adaptasi untuk pekerjaan individual dengan menggabungkan praktik XP dan disiplin PSP (Dzhurov dkk., 2009, hlm. 253 sampai 254).

Pertimbangan ini merupakan kesesuaian rancangan proses, bukan hasil eksperimen yang membuktikan PxP lebih murah atau lebih cepat pada ARTHA. Keputusan memilihnya harus disertai kesanggupan menjalankan praktiknya; tujuh judul tahapan tanpa log, pengujian, dan retrospeksi belum cukup membuktikan penerapan PxP.

## 7. Alasan tidak memilih alternatif yang lebih dapat dipertahankan

| Pendekatan | Alasan yang dapat digunakan | Batas kejujuran argumen |
| :--- | :--- | :--- |
| Waterfall | Penelitian memerlukan ruang penyesuaian aturan bisnis sebelum seluruh alur dibekukan. | Hanya alasan awal memilih pendekatan iteratif; tidak cukup membuktikan PxP lebih tepat daripada semua pendekatan iteratif lain. |
| RAD | Fokus komparasi ini juga mencakup pengujian sejak implementasi dan pengukuran kerja individual, yang belum dijabarkan dalam model RAD pada artikel pembanding. | RAD dapat dilengkapi praktik yang sama. Jangan mengklaim workshop mustahil tanpa bukti ketersediaan mitra. |
| Scrum | Penelitian membutuhkan proses teknis personal secara rinci, sedangkan Scrum terutama memberi kerangka akuntabilitas, inspeksi, adaptasi, dan pengelolaan produk. | Scrum dapat memakai praktik XP. Jangan mengklaim perangkapan peran secara mutlak dilarang. |
| XP | Praktik rekayasanya sesuai, tetapi penerapan individual memerlukan penjelasan adaptasi pairing, koordinasi, dan pengendalian pekerjaan personal. | Adaptasi XP tetap sah untuk dikaji. PxP dipilih karena adaptasi individual tersebut sudah dijelaskan secara eksplisit dalam sumber. |
| Prototyping | Tepat untuk memperjelas kebutuhan melalui purwarupa, tetapi strategi purwarupa saja belum menjabarkan seluruh disiplin pengembangan dan pengukuran personal yang dipilih. | Luaran prototipe tidak mewajibkan metode Prototyping; purwarupa antarmuka juga dapat dibuat dalam PxP. |

Ketersediaan mitra merupakan syarat praktis semua pendekatan yang memerlukan umpan balik. Jangan menyimpulkan bahwa PxP cocok ketika mitra sama sekali tidak tersedia, sebab validasi kebutuhan dan evaluasi hasil tetap membutuhkan keterlibatan pengguna.

## 8. Narasi justifikasi yang dapat diadaptasi

Personal Extreme Programming (PxP) dipilih karena menyediakan proses pengembangan individual yang menghubungkan perencanaan tugas, implementasi berbasis pengujian, pengujian sistem, dan evaluasi proses. Dalam penelitian ARTHA, hubungan tersebut diperlukan untuk mengembangkan fungsi siswa, kelas, pembayaran, dan laporan yang memiliki aturan saling berkaitan. Dzhurov dkk. (2009, hlm. 254 sampai 256) menjelaskan bahwa rencana tugas dapat direvisi ketika kebutuhan berubah dan data pelaksanaan digunakan dalam retrospeksi.

Pemilihan PxP juga mempertimbangkan kebutuhan pengendalian kualitas pada pencatatan pembayaran, pembatasan akses cabang, dan kapasitas kelas. Praktik pengujian sejak implementasi, peninjauan kode, serta pencatatan cacat digunakan untuk memeriksa aturan tersebut secara bertahap (Dzhurov dkk., 2009, hlm. 253 sampai 255). Hasil penerapan tetap dinilai melalui bukti pengujian dan evaluasi pengguna, sehingga keberhasilan sistem tidak disimpulkan hanya dari metode yang digunakan.

RAD, Scrum, dan XP juga mendukung pengembangan yang adaptif, sehingga fleksibilitas kebutuhan tidak digunakan sebagai satu-satunya pembeda. PxP diprioritaskan karena adaptasi proses individual, pencatatan durasi tugas, dan evaluasi perbaikan proses telah dijelaskan dalam sumber dasarnya. Penerapannya pada penelitian ini akan dibuktikan melalui rencana iterasi, catatan pelaksanaan, hasil pengujian, dan tindak lanjut retrospeksi.

## 9. Penyesuaian mengikuti arahan bimbingan

Transkrip bimbingan Pak Arif pada 07:25 sampai 08:37 menekankan perbandingan pendekatan yang memiliki karakteristik sebanding serta alasan pemilihannya. Transkrip tersebut tidak menetapkan lima metode tertentu sebagai jumlah atau daftar wajib, sehingga Waterfall sebaiknya cukup menjadi pembanding pengantar dan analisis utama diarahkan pada alternatif iteratif.

Daftar langkah berikut dapat dipakai sebelum komparasi dibawa kembali ke bimbingan. Urutannya mendahulukan kesalahan sumber, kemudian perbaikan argumentasi, lalu bukti penerapan yang harus disiapkan.

1. Perbaiki identitas penulis, jurnal, judul, tahun, dan halaman pada daftar pustaka yang ditandai pada Bagian 4.
2. Keluarkan dukungan “Perbandingan XP vs PxP” dari berkas Fahrijal karena isi dokumennya berbeda, serta lepaskan sitasi Ramadhan sampai sumber tersedia.
3. Ganti tabel lama dengan perbandingan berimbang yang memisahkan karakteristik sumber dari penilaian ARTHA.
4. Hapus larangan perangkapan Scrum, penguncian mutlak isi Sprint, dokumen Waterfall wajib tebal, dan jaminan keunggulan PxP.
5. Selaraskan pembahasan sebelum tabel, panduan narasi verbal, matriks pembelaan, dan kesimpulan karena klaim keliru yang sama juga diulang pada bagian tersebut.
6. Tetapkan bukti penerapan PxP berupa tugas, estimasi, catatan waktu, catatan cacat, pengujian, dan retrospeksi, dengan rincian yang realistis untuk dikerjakan.
7. Konfirmasi jadwal validasi mitra dan aturan bisnis yang masih terbuka, tanpa menyatakan ketidaksediaan mitra sebagai fakta yang belum dibuktikan.

Pemeriksaan ini tidak mengubah Bab 3, use case, basis data, atau dokumen komparasi asal. Kesimpulan yang dapat dibawa ke dosen adalah bahwa PxP merupakan pilihan yang beralasan untuk rancangan proses ARTHA, dengan kewajiban membuktikan penerapannya dan mengakui bahwa alternatif lain tetap dapat digunakan.

## 10. Tautan berkas sumber yang diperiksa

Tautan berikut mengarah ke salinan PDF lokal yang menjadi dasar pemeriksaan. Judul tampilan mengikuti nama berkas agar mudah ditemukan, tetapi identitas bibliografis yang benar tetap mengikuti catatan audit pada Bagian 4.

- [Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf>)
- [ebook-pressman-sw-engineering.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/ebook-pressman-sw-engineering.pdf>)
- [Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/BUKU/Extreme-Programming-Explained-2nd-Edition-Kent-Beck.pdf>)
- [Scrum Guide 2020 - Schwaber & Sutherland - Official.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Scrum Guide 2020 - Schwaber & Sutherland - Official.pdf>)
- [Personal Extreme Programming - Agile for Autonomous Developer - S3T 2009 - Dzhurov dkk - 2009.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Personal Extreme Programming - Agile for Autonomous Developer - S3T 2009 - Dzhurov dkk - 2009.pdf>)
- [Penerapan Metode RAD - Infotek - Pratama dkk - 2023.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Penerapan Metode RAD - Infotek - Pratama dkk - 2023.pdf>)
- [Perbandingan XP vs PxP pada Implementasi Software - Fahrijal & Hartawan - 2024.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Perbandingan XP vs PxP pada Implementasi Software - Fahrijal & Hartawan - 2024.pdf>)
- [SI Buku Tamu DPOP Balikpapan - PxP - Fikri & Prabowo (ITK) - 2020.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI Buku Tamu DPOP Balikpapan - PxP - Fikri & Prabowo (ITK) - 2020.pdf>)
- [SI Surat Menyurat - Personal Extreme Programming (PxP) - Sidiq dkk - 2025.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI Surat Menyurat - Personal Extreme Programming (PxP) - Sidiq dkk - 2025.pdf>)
- [PxP vs Waterfall - Job Training App - ICST 2018 - Asri dkk - 2018.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/PxP vs Waterfall - Job Training App - ICST 2018 - Asri dkk - 2018.pdf>)
- [Strengthening the Case for Pair Programming - IEEE Software - Williams dkk - 2000.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Strengthening the Case for Pair Programming - IEEE Software - Williams dkk - 2000.pdf>)
- [Structured vs Agile Development Comparative Analysis - Mishra & Alzoubi - Springer - 2023.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Structured vs Agile Development Comparative Analysis - Mishra & Alzoubi - Springer - 2023.pdf>)
- [Pemodelan SCRUM Klinik Ar-Rokhim - JOINS - Kurniawan & Sani - 2019.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/04_FITUR_DAN_TEKNOLOGI_PENDUKUNG/Pemodelan SCRUM Klinik Ar-Rokhim - JOINS - Kurniawan & Sani - 2019.pdf>)
- [Managing the Development of Large Software Systems - Waterfall - WESCON - Royce - 1970.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/01_FONDASI_DAN_KOMPARASI_METODOLOGI/Managing the Development of Large Software Systems - Waterfall - WESCON - Royce - 1970.pdf>)
