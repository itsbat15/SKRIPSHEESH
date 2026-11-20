# NOTULENSI WAWANCARA MITRA 2: EVALUASI SISTEM INFORMASI LAMA DAN KEBUTUHAN OPERASIONAL TEKNIS
## Narasumber: Bapak Anang (Om Anang - Manajemen & Operasional Teknis Bimbel Artha)

---

### Informasi Pelaksanaan Wawancara
* **Hari, Tanggal**: Senin, 29 Juli 2026
* **Waktu Pelaksanaan**: Pukul 15.30 sampai 16.46 WITA (Durasi Audio: 75 Menit 59 Detik)
* **Tempat Pelaksanaan**: Kantor Pusat Bimbingan Belajar Artha, Balikpapan
* **Narasumber**: Bapak Anang (Om Anang - Pimpinan Operasional Teknis Lembaga)
* **Pewawancara**: Ariel (NIM. 10221074)
* **Topik Wawancara**: Penelusuran Riwayat Website Lama, Evaluasi Infrastruktur Server, dan Perancangan Arsitektur Sistem Informasi Multicabang
* **Berkas Sumber Audio**: [`WAWANCARA KEDUA SKRIPSI (OM ANANG).m4a`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/WAWANCARA/REKAMAN%20AUDIO%20(M4A)/WAWANCARA%20KEDUA%20SKRIPSI%20(OM%20ANANG).m4a)
* **Berkas Transkrip Timestamp**: [`WAWANCARA KEDUA SKRIPSI (OM ANANG)_WITH_TIMESTAMPS.txt`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP%20TEKS%20(TXT)/WAWANCARA%20KEDUA%20SKRIPSI%20(OM%20ANANG)_WITH_TIMESTAMPS.txt)

---

## 📌 RINGKASAN EKSEKUTIF HASIL WAWANCARA

Pertemuan mendalam bersama Om Anang difokuskan pada penelusuran rekam jejak teknologi informasi yang pernah diterapkan di Bimbingan Belajar Artha. Lembaga sebelumnya memiliki situs web profil yang dikembangkan oleh pihak ketiga penyedia jasa domain dan pengembang lepas asal Yogyakarta. Namun, situs web tersebut terbukti memiliki ketergantungan eksternal yang sangat tinggi, rentan mengalami kendala kehabisan memori server, serta sama sekali tidak memiliki modul fungsional untuk mengelola transaksi pendaftaran, keuangan SPP, maupun penjadwalan kelas di delapan cabang.

Dari sesi evaluasi teknis ini, disepakati keputusan strategis bahwa sistem informasi manajemen operasional yang diajukan peneliti akan dibangun dari awal (*from scratch*) dengan arsitektur web modern yang mandiri. Sistem baru ini diproyeksikan untuk mengintegrasikan basis data seluruh cabang, memetakan asal sekolah siswa secara otomatis sebagai dasar penentuan strategi promosi, mendistribusikan jadwal mengajar tentor secara transparan melalui gawai seluler, serta memfasilitasi pelaporan transaksi harian langsung ke manajemen pusat tanpa ketergantungan pihak ketiga.

---

## 📋 NOTULENSI RINCI PER TEMA PEMBAHASAN

### 1. Riwayat Pengembangan dan Kelemahan Website Lama (Menit 00:00 hingga 11:20)
* **Identifikasi Pengembang dan Kontrak Domain**:
  Narasumber menjelaskan bahwa situs web Artha sebelumnya dipesan melalui agensi jasa penyedia domain bernama Dominensia. Agensi tersebut kemudian melimpahkan pekerjaan pemrograman kepada pihak ketiga perorangan, yaitu seorang pengembang bernama Mas Jabah Hidayat yang berdomisili di Yogyakarta. Untuk urusan administrasi domain, lembaga telah memegang hak akses mandiri, namun untuk urusan pemeliharaan (*maintenance*) dan struktur basis data masih bergantung penuh pada pihak Yogyakarta.
* **Biaya Operasional dan Keterbatasan Server**:
  Lembaga mengalokasikan biaya langganan domain dan peladen (*hosting*) berkisar satu juta rupiah per tahun yang berada dalam skema kompartemen bersama (*shared hosting*). Situs web lama kerap mengalami galat (*error*) berupa kehabisan memori alokasi peladen saat diakses oleh banyak pengguna. Kondisi tersebut memaksa lembaga untuk terus meminta bantuan pengembang di Yogyakarta guna menaikkan batas memori peladen secara manual.
* **Keputusan Membangun Sistem Baru Secara Mandiri**:
  Peneliti memberikan dua opsi teknis kepada pimpinan lembaga, yaitu memperbarui kode sumber lama atau membangun sistem informasi yang sepenuhnya baru. Om Anang secara tegas memilih untuk membangun sistem baru. Beliau beralasan bahwa sistem baru akan memberikan kemandirian penuh bagi lembaga, menghilangkan ketergantungan pada pihak ketiga di luar kota, serta memungkinkan kustomisasi fitur yang sesuai dengan alur bisnis nyata di lapangan.

---

### 2. Strategi Konten Web dan Pemanfaatan Data Siswa (Menit 11:20 hingga 25:20)
* **Kebutuhan Konten Informatif versus Arsip Foto**:
  Narasumber menekankan bahwa antarmuka publik situs web lembaga selama ini hanya dipenuhi dokumentasi foto kegiatan yang pasif sehingga kurang menarik minat calon siswa. Lembaga membutuhkan situs web yang memuat artikel edukatif, kiat belajar, serta informasi kurikulum resmi guna mendongkrak visibilitas daring dan keterlibatan calon pelanggan di Kota Balikpapan.
* **Pemisahan Antarmuka Publik dan Dasbor Administrasi Internal**:
  Peneliti dan narasumber menyepakati pemisahan arsitektur antarmuka menjadi dua zona utama. Zona pertama merupakan halaman muka umum (*landing page*) yang dapat diakses oleh publik untuk membaca profil lembaga, jadwal program, serta informasi promosi. Zona kedua merupakan portal internal terproteksi yang mensyaratkan autentikasi akun staf administrasi cabang, kasir, dan pimpinan untuk menjalankan transaksi operasional.

---

### 3. Integrasi Data Delapan Cabang dan Analisis Demografi Pendaftar (Menit 25:20 hingga 34:49)
* **Sentralisasi Basis Data Transaksi Cabang**:
  Kebutuhan paling mendesak bagi manajemen pusat adalah memantau volume pendaftaran di delapan cabang secara waktu nyata (*real-time*). Selama ini, kantor pusat tidak dapat mengetahui berapa jumlah siswa yang mendaftar pada hari berjalan di cabang lain karena pencatatan masih terisolasi di buku besar masing-masing cabang.
* **Fitur Pemetaan Asal Sekolah (Demografi Siswa)**:
  Sistem baru dituntut mampu merekam asal sekolah setiap calon siswa yang mendaftar, baik dari tingkat sekolah dasar, sekolah menengah pertama, hingga sekolah menengah atas. Data ini sangat krusial bagi manajemen guna menganalisis sekolah mana saja yang menjadi kantong siswa terbesar bagi Artha. Dengan demikian, tim pemasaran dapat mengalokasikan distribusi brosur dan sosialisasi program secara terarah dan efisien berdasarkan data empiris sistem.

---

### 4. Manajemen Penjadwalan Kelas dan Akses Pengajar (Menit 34:49 hingga 46:25)
* **Standarisasi Struktur Sesi Belajar Harian**:
  Narasumber merinci pembagian tiga sesi bimbingan reguler yang berlaku di seluruh cabang Artha:
  1. *Sesi Pertama*: Berlangsung pada pukul 15.30 hingga 17.00 WITA, umumnya diprioritaskan untuk jenjang sekolah dasar.
  2. *Sesi Kedua*: Berlangsung pada pukul 17.00 hingga 18.30 WITA, dialokasikan untuk jenjang sekolah menengah pertama.
  3. *Sesi Ketiga*: Berlangsung pada pukul 19.00 hingga 20.30 WITA, dialokasikan untuk jenjang sekolah menengah atas.
* **Kendala Komunikasi Jadwal Mengajar Tentor**:
  Selama ini, para guru atau tentor harus datang langsung ke cabang atau menelepon meja depan hanya untuk memastikan jadwal mengajar harian mereka. Kondisi ini kerap memicu salah paham jadwal dan kekosongan ruang kelas.
* **Solusi Akses Digital bagi Pengajar**:
  Om Anang meminta agar sistem menyediakan antarmuka responsif yang dapat dibuka melalui peramban ponsel pintar milik pengajar. Melalui fitur tersebut, setiap pengajar dapat melihat jadwal penugasan mengajar, lokasi cabang, ruangan kelas, serta daftar siswa yang dibimbing secara mandiri.

---

### 5. Inovasi Portal Pembelajaran dan Integrasi Media Sosial (Menit 46:26 hingga 60:16)
* **Wacana Penyediaan Modul Video Edukasi Terproteksi**:
  Narasumber tertarik untuk mengadopsi model layanan bimbingan modern layaknya platform digital nasional seperti Ruangguru dan Ganesha Operation. Lembaga merencanakan adanya fitur video rekaman pembahasan soal yang diunggah ke dalam sistem. Namun, akses terhadap video edukasi ini dibatasi secara ketat, yakni hanya siswa yang status administrasinya terverifikasi aktif membayar SPP bulanan yang diberikan hak akses.
* **Konsolidasi Akun Pemasaran Cabang**:
  Diskusi menyinggung maraknya akun media sosial cabang (seperti akun Instagram cabang Artha 1 hingga 8) yang kondisinya terbengkalai dan tidak pernah diperbarui sejak tahun-tahun sebelumnya. Om Anang menghendaki adanya standarisasi tautan resmi di dalam situs web baru agar masyarakat terarah ke saluran komunikasi resmi lembaga di bawah kendali manajemen pusat.

---

### 6. Evaluasi Alur Logistik Kas dan Koordinasi Lapangan (Menit 60:17 hingga 75:59)
* **Ketergantungan pada Kurir Titipan Fisik**:
  Om Anang mengonfirmasi bahwa alur perpindahan dana tunai dan buku rekapan fisik antarcabang selama ini sangat mengandalkan sistem titipan antarguru atau kepala cabang yang melintas antarkantor. Cara ini diakui memiliki risiko keamanan tinggi, potensi tercecer di perjalanan, serta keterlambatan dalam pelaporan keuangan bulanan.
* **Dukungan Penuh terhadap Proyek Tugas Akhir**:
  Om Anang menyatakan kesiapan penuh jajaran operasional lembaga untuk membantu peneliti dalam menyediakan data operasional, formulir pendaftaran fisik, serta membuka akses pengujian prototipe perangkat lunak di cabang yang ditunjuk.

---

## 📌 BUTIR TINDAK LANJUT (*ACTION ITEMS*)
1. Peneliti merancang basis data terpusat (*centralized database*) yang memisahkan tabel pengguna publik, siswa, tentor, staf kasir cabang, dan manajemen pusat.
2. Peneliti merancang modul analitik pendaftaran yang mampu mengelompokkan data demografi siswa berdasarkan sekolah asal secara visual.
3. Peneliti menyiapkan modul jadwal bimbingan terintegrasi dengan struktur waktu tiga sesi harian yang dapat diakses secara fleksibel melalui telepon genggam.
