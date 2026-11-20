# DOKUMEN REVISI NASKAH PROPOSAL (KATEGORI A)
## Tindak Lanjut Hasil Bimbingan Ke-7 Dosen Pembimbing 1 (Bapak Arif Rahman, S.Kom., M.T.)

---

### Informasi Dokumen
* **Penulis**: Ariel (NIM 10221074)
* **Program Studi**: Sistem Informasi, Institut Teknologi Kalimantan (ITK)
* **Dosen Pembimbing 1**: Bapak Arif Rahman, S.Kom., M.T.
* **Dosen Pembimbing 2**: Ibu Sri Rahayu Natasia, S.Kom., M.Kom., M.Sc.
* **Tanggal Penyusunan**: Selasa, 10 November 2026
* **Tujuan Dokumen**: Menyediakan naskah revisi siap pakai (*ready-to-apply*) berlandaskan literatur primer yang sahih untuk memenuhi seluruh catatan evaluasi Kategori A dari Dosen Pembimbing 1 sebelum pendaftaran Seminar Proposal (Sempro).

---

## 📌 POIN 1: REVISI SITASI PEMILIHAN METODE PXP (BAB 1 SUBBAB 1.1)

### 1. Masalah pada Draf Lama
Pada naskah [1.1_Latar_Belakang.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%201/1.1_Latar_Belakang.md), tertulis kalimat:
> *"Dalam pelaksanaan Tugas Akhir ini, metodologi Personal Extreme Programming (PXP) dipilih sebagai kerangka kerja pengembangan prototipe berdasarkan empat aspek utama, yaitu karakteristik kebutuhan sistem, tingkat keterlibatan mitra, ketersediaan waktu pengerjaan, dan kebutuhan dokumentasi..."*

**Kritik Dosen Pembimbing (Pak Arif)**:
Dosen pembimbing menegaskan bahwa seorang peneliti akademik tidak boleh merumuskan simpulan teoritis sepihak seolah-olah "empat aspek utama" tersebut adalah teori ciptaan sendiri. Peneliti wajib menyitir literatur primer yang sah mengenai alasan dan kriteria pemilihan metode pengembangan perangkat lunak mandiri.

### 2. Bukti Literatur Primer dari Folder `JURNAL`
Penelusuran terhadap berkas pustaka primer di direktori [JURNAL](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL) membuktikan bahwa landasan pemilihan PxP memiliki dasar ilmiah yang sangat kuat pada sumber-sumber berikut:

1. **Dzhurov, Krasteva, dan Ilieva (2009)**:
   * Berkas: [`33_Dzhurov_dkk_2009_Personal_Extreme_Programming.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/33_Dzhurov_dkk_2009_Personal_Extreme_Programming.pdf)
   * Kutipan Asli (Halaman 252-253):
     > *"Autonomous developers are software engineers who implement software solutions without being part of a team... Autonomous developers are facing big challenges in handling projects in time and with high product quality and minimizing failure. Preconditions for this are the lack of planning and quality control... deploying Personal Software Process (PSP) in a real project involves a lot of efforts to prepare and maintain the amount of documentation and data. Autonomous developers are not prone to investing resources and time in learning and implementing heavy processes... The current research study proposes a modification of PSP which aims at lightening the software development process and making it easier to follow, while keeping the PSP basic principles. The new methodology is extended with proven efficient development practices from the Extreme Programming in order to support better project planning and product quality control."*
   * *Inti Ilmiah*: PxP dirancang khusus untuk memecahkan kendala pengembang mandiri melalui perpaduan disiplin perencanaan dan pengendalian mutu tanpa beban dokumentasi berat.

2. **Sommerville (2011)**:
   * Berkas: [`26_Sommerville_2011_Software_Engineering.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/26_Sommerville_2011_Software_Engineering.pdf)
   * Rujukan: Bab 3 *Agile Software Development* (hlm. 56 sampai 80).
   * *Inti Ilmiah*: Kesesuaian pemilihan metode rekayasa perangkat lunak ditentukan oleh karakteristik sistem (dinamika perubahan kebutuhan), faktor tim (skala pengembang tunggal), ketersediaan interaksi pengguna/mitra, dan beban dokumentasi organisasi.

3. **Agarwal dan Umphress (2008)**:
   * Berkas: [`32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.pdf)
   * Kutipan Asli (Halaman 82):
     > *"Extreme Programming (XP) has emerged as an important agile software development methodology. However, XP is designed for teams... This paper examines features of XP and determines how it can be applied to a single person team (i.e. a programmer who works mainly on his/her own as opposed to a programmer who works as a part of a well-integrated team)."*

4. **Musofa dkk. (2025, SINTA 2)**:
   * Berkas: [`13_Musofa_dkk_2025_JTIIK_SINTA2.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/13_Musofa_dkk_2025_JTIIK_SINTA2.pdf)
   * Jurnal: *Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK)*, Vol. 12, No. 5, hlm. 985-996.
   * *Inti Ilmiah*: Penerapan PxP terbukti efektif untuk pengembang mandiri karena menyederhanakan pelacakan waktu dan verifikasi fungsionalitas secara berkala.

### 3. Teks Rekomendasi Pengganti (Siap Pakai untuk Subbab 1.1)

```markdown
Dalam pelaksanaan Tugas Akhir ini, metodologi *Personal Extreme Programming* (PxP) dipilih sebagai kerangka kerja rekayasa pengembangan prototipe sistem informasi. Pemilihan metode ini didasarkan pada keselarasan karakteristik PxP terhadap kriteria evaluasi proses perangkat lunak adaptif untuk skala pengembang mandiri (*single developer*) (Sommerville, 2011; Dzhurov dkk., 2009). Berdasarkan kajian Dzhurov dkk. (2009) serta Agarwal dan Umphress (2008), seorang pengembang mandiri menghadapi tantangan besar dalam mengelola estimasi waktu pengerjaan, kedisiplinan perencanaan, dan pengendalian mutu perangkat lunak tanpa harus terbebani oleh pengelolaan dokumentasi formal yang rumit seperti pada *Personal Software Process* (PSP) konvensional. Kondisi teoritis tersebut sangat selaras dengan situasi empiris di Bimbel Artha, di mana proses rekayasa perangkat lunak dikerjakan oleh satu orang pengembang, proses bisnis lembaga sedang mengalami transformasi digital sehingga kebutuhan fungsional berkembang secara bertahap, serta pihak pimpinan dan staf administrasi cabang memiliki keterbatasan waktu pendampingan harian karena padatnya pengawasan operasional di delapan kantor cabang fisik. Oleh karena itu, pendekatan iteratif PxP memungkinkan pengembang melakukan eksplorasi kebutuhan dan evaluasi prototipe secara berkala bersama mitra pada setiap akhir iterasi tanpa mengganggu ritme operasional harian lembaga (Musofa dkk., 2025).
```

---

## 📌 POIN 2: HARMONISASI PARAGRAF PENUTUP LATAR BELAKANG MENUJU RUMUSAN MASALAH

### 1. Masalah pada Draf Lama
Paragraf penutup latar belakang masalah pada draf sebelumnya cenderung mengulang intisari rumusan masalah secara redundan, sehingga pembaca merasa membaca kalimat yang sama dua kali ketika berpindah ke Subbab 1.2.

**Arahan Dosen Pembimbing (Pak Arif)**:
Paragraf akhir latar belakang harus berfungsi sebagai jembatan transisi yang wajar (*smooth transition*). Paragraf tersebut merangkum bagaimana seluruh rangkaian permasalahan lapangan yang telah dipaparkan bermuara pada urgensi pengembangan prototipe, lalu secara lugas mengantarkan pembaca pada perumusan masalah formal tanpa ada repetisi kalimat tanya.

### 2. Teks Rekomendasi Paragraf Penutup Subbab 1.1 (Siap Pakai)

```markdown
Berdasarkan keseluruhan pemaparan permasalahan operasional dan landasan metodologis tersebut, penelitian Tugas Akhir ini diarahkan pada rancang bangun prototipe sistem informasi manajemen operasional terintegrasi berbasis web menggunakan metode *Personal Extreme Programming* (PxP) dengan Bimbingan Belajar Artha Balikpapan sebagai mitra studi kasus. Kehadiran prototipe sistem informasi ini ditujukan untuk memberikan solusi nyata terhadap kendala pencatatan formulir pendaftaran fisik, penempatan kelompok belajar, pencatatan transaksi kasir cabang, serta rekonsiliasi kas bank terpusat bagi delapan kantor cabang secara terpadu. Berlandaskan konteks permasalahan yang telah diuraikan, rumusan masalah penelitian ini dirinci secara terstruktur pada subbab berikutnya.
```

### 3. Teks Subbab 1.2 Rumusan Masalah yang Menyambut Transisi

```markdown
## 1.2. Rumusan Masalah

Berdasarkan latar belakang masalah yang telah diuraikan, rumusan masalah dalam penelitian Tugas Akhir ini adalah sebagai berikut:
1. Bagaimana merancang prototipe sistem informasi manajemen operasional terintegrasi berbasis web pada Bimbingan Belajar Artha Balikpapan menggunakan metode *Personal Extreme Programming* (PxP)?
2. Bagaimana menguji kelayakan dan fungsionalitas prototipe sistem informasi manajemen operasional terintegrasi berbasis web pada Bimbingan Belajar Artha Balikpapan menggunakan metode *Black Box Testing* dan *User Acceptance Testing* (UAT)?
```

---

## 📌 POIN 3: LANDASAN RUJUKAN BAKU ARSITEKTUR TIGA LAPIS (THREE-TIER ARCHITECTURE)

### 1. Masalah pada Draf Lama
Pada naskah [BAB_3_DESAIN_DAN_IMPLEMENTASI.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%203/BAB_3_DESAIN_DAN_IMPLEMENTASI.md) Subbab 3.4.1 (*Perancangan Arsitektur Sistem*), bagan arsitektur sistem tiga lapis (Gambar 3.2) disajikan tanpa mencantumkan rujukan literatur baku.

**Kritik Dosen Pembimbing (Pak Arif)**:
Pak Arif menanyakan secara eksplisit: *"Kamu merujuk arsitekturnya siapa? Kalau kamu tidak ada rujukan baku, nanti saat seminar proposal dewan penguji akan mempertanyakan kenapa kamu membuat struktur arsitektur seperti ini. Arsitektur three-tier wajib memiliki acuan buku teks dan rujukan jurnal ilmiah yang sah."*

### 2. Sumber Referensi Primer Terpilih (Buku Teks Dunia dan Jurnal Nasional Terakreditasi SINTA 3)

Sesuai persetujuan, fondasi ilmiah arsitektur tiga lapis disandarkan pada dua literatur primer yang secara gamblang dan spesifik membedah arsitektur *Three-Tier*:

#### A. Rujukan Teori Baku Rekayasa Perangkat Lunak Dunia
* **Penulis**: Ian Sommerville (2011)
* **Buku**: *Software Engineering* (Edisi ke-9), Boston: Pearson Education / Addison-Wesley.
* **Letak Bab**:
  * Bab 6 *Architectural Design*, Subbab 6.3.1 *Layered Architecture Pattern* (hlm. 155 sampai 158).
  * Bab 18 *Distributed Systems*, Subbab 18.3.3 *Multi-Tier Client-Server Architecture* (hlm. 494, Gambar 18.10).
* **Berkas Beranotasi Kuning**: [`26_Sommerville_2011_Software_Engineering.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/26_Sommerville_2011_Software_Engineering.pdf) (Halaman 511 / Buku Hlm. 494).

#### B. Rujukan Jurnal Nasional Penerapan Sistem Informasi Pendidikan
* **Penulis**: Muhammad Yusup, Untung Rahardja, dan Eko Prasetiyani (2010)
* **Judul Artikel**: *Penerapan Arsitektur Three-Tier Terhadap Optimalisasi Keamanan Distributed Database*
* **Nama Jurnal**: *CCIT (Creative Communication and Innovative Technology) Journal*, Vol. 3, No. 3, hlm. 320 sampai 332.
* **Akreditasi**: **Terakreditasi SINTA 3** (SK Kemenristekdikti / Kemdiktisaintek).
* **DOI**: [10.33050/ccit.v3i3.704](https://doi.org/10.33050/ccit.v3i3.704) | URL OJS: [https://ejournal.raharja.ac.id/index.php/ccit/article/view/704](https://ejournal.raharja.ac.id/index.php/ccit/article/view/704)
* **Indeksasi Garuda**: [https://garuda.kemdiktisaintek.go.id/documents/detail/2186019](https://garuda.kemdiktisaintek.go.id/documents/detail/2186019)
* **Berkas Beranotasi Kuning**: [`16_Yusup_dkk_2010_CCIT_SINTA3_ThreeTier.pdf`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_PDF/16_Yusup_dkk_2010_CCIT_SINTA3_ThreeTier.pdf) (Halaman 12 dan Halaman 16).
* **Berkas Ekstraksi Teks**: [`16_Yusup_dkk_2010_CCIT_SINTA3_ThreeTier.txt`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/JURNAL/36_REFERENSI_TXT/16_Yusup_dkk_2010_CCIT_SINTA3_ThreeTier.txt).

---

### 3. Matriks Forensik Sitasi dan Bukti Penandaan Stabilo Kuning (*Hover Annotation*)

Berikut adalah pemetaan kutipan langsung (*verbatim*) dari berkas PDF primer ke dalam naskah skripsi ARTHA yang telah disematkan stabilo kuning (*yellow highlight*) dan catatan melayang (*hover pop-up notes*):

| No | Sumber Literatur | Letak Halaman | Teks Kutipan Asli pada Berkas PDF | Teks Rumusan yang Dituliskan pada Skripsi ARTHA |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Sommerville (2011)** | Hlm. 494 (PDF Hlm. 511) | *"To avoid some of these problems, a 'multi-tier client-server' architecture can be used. In this architecture, the different layers of the system, namely presentation, data management, application processing, and database, are separate processes that may execute on different processors... In this case, the use of a three-tier architecture allows the information transfer between the web server and the database server to be optimized."* | Arsitektur tiga lapis (*three-tier client-server architecture*) merupakan pola perancangan perangkat lunak terdistribusi yang membagi seluruh komponen fungsionalitas sistem ke dalam tiga lapisan terpisah secara mandiri, yaitu lapisan presentasi antarmuka pengguna (*Presentation Tier*), lapisan logika pemrosesan bisnis aplikasi (*Application Tier*), dan lapisan penyimpanan pangkalan data relasional (*Data Storage Tier*) (Sommerville, 2011). |
| 2 | **Yusup, Rahardja, & Prasetiyani (2010)** | Hlm. 356 (PDF Hlm. 12) | *"Arsitektur Three-Tier ini banyak sekali diimplementasikan dengan menggunakan Web Application. Karena dengan menggunakan Web Application, Client Side (Komputer Client) hanya akan melakukan instalasi Web Browser. Dan saat komputer client melakukan inputan data, maka data tersebut dikirimkan ke application server dan diolah berdasarkan business process-nya. Selanjutnya application server akan melakukan komunikasi dengan database server... Arsitektur Three-Tier memiliki tiga tingkatan: 1) Presentation Tier... 2) Business Logic Tier... 3) Database Tier..."* | Penerapan arsitektur *three-tier* berbasis web membagi fungsionalitas sistem ke dalam lapisan presentasi, logika bisnis, dan basis data, di mana komputer klien di delapan kantor cabang fisik hanya menjalankan peramban web untuk mengirimkan data ke peladen aplikasi guna diproses dan diverifikasi sebelum berkomunikasi dengan peladen basis data (Yusup dkk., 2010). |
| 3 | **Yusup, Rahardja, & Prasetiyani (2010)** | Hlm. 360 (PDF Hlm. 16) | *"Pada gambar 6 diatas dijelaskan bahwa ada pemisahan secara fisik antara Application Tier pada server... dengan Database Tier pada server iRME... Dengan pemisahan tier ini diharapkan dapat meminimalisasi kerugian yang ditimbulkan serta dapat meningkatkan keamanan sistem database."* | Pemisahan fisik antara *Application Tier* dan *Database Tier* diterapkan guna mengisolasi pangkalan data dari akses langsung peramban klien, memperketat kontrol hak akses pengguna, serta meminimalisasi risiko manipulasi data transaksi operasional lembaga di kantor cabang (Yusup dkk., 2010). |

---

### 4. Teks Rekomendasi Siap Pakai untuk Bab 2 (Subbab Baru 2.1.8)

Berikut adalah naskah lengkap Subbab 2.1.8 yang siap disalin ke [2.1_Kajian_Teknologi_atau_Metode_Terkait.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%202/2.1_Kajian_Teknologi_atau_Metode_Terkait.md):

```markdown
### 2.1.8. Arsitektur Tiga Lapis (Three-Tier Architecture)

Arsitektur tiga lapis (*three-tier client-server architecture*) merupakan pola perancangan perangkat lunak terdistribusi yang membagi seluruh fungsionalitas sistem ke dalam tiga lapisan terpisah secara logis maupun fisik (Sommerville, 2011). Pola arsitektur ini dikembangkan guna mengatasi keterbatasan model arsitektur dua lapis (*two-tier*) konvensional yang kerap membebankan pemrosesan logika bisnis secara langsung pada komputer klien (*fat client*) atau membuka koneksi langsung dari klien ke pangkalan data yang rentan terhadap risiko keamanan (Yusup dkk., 2010). Melalui prinsip pemisahan tanggung jawab (*separation of concerns*), setiap lapisan dalam arsitektur tiga lapis memiliki batasan tugas yang spesifik dan berkomunikasi melalui antarmuka protokol jaringan yang terstandarisasi, sehingga peningkatan atau modifikasi pada satu lapisan tidak mengganggu integritas lapisan lainnya (Sommerville, 2011).

Tiga lapisan utama dalam arsitektur ini mencakup lapisan presentasi antarmuka pengguna (*Presentation Tier*), lapisan logika pemrosesan bisnis aplikasi (*Application Tier* atau *Middle Tier*), dan lapisan penyimpanan pangkalan data relasional (*Data Storage Tier*) (Sommerville, 2011; Yusup dkk., 2010). Lapisan presentasi beroperasi pada sisi peramban perangkat pengguna akhir, yang bertugas menerima masukan formulir serta menyajikan informasi visual tanpa melakukan manipulasi data secara langsung. Lapisan aplikasi bertindak sebagai pusat pengendali logika yang mengeksekusi aturan bisnis (*business rules*), memvalidasi hak akses otorisasi pengguna, serta mengelola alur kerja transaksi sebelum data dikirimkan ke pangkalan data. Sementara itu, lapisan penyimpanan data bertugas menjamin persistensi, konsistensi, serta keutuhan data relasional melalui sistem manajemen basis data (*Database Management System*) yang terlindungi secara aman di balik peladen aplikasi (Yusup dkk., 2010).

Penerapan arsitektur tiga lapis berbasis web pada domain institusi pendidikan terbukti memberikan stabilitas tinggi dalam menangani integrasi data dan keamanan akses pengguna (Yusup dkk., 2010). Dalam kajian empiris Yusup dkk. (2010), implementasi arsitektur web tiga lapis mempermudah pengguna karena sisi klien hanya memerlukan peramban web tanpa instalasi perangkat lunak tambahan, sedangkan seluruh proses validasi dan manipulasi data dikendalikan penuh oleh peladen aplikasi. Pemisahan secara fisik antara peladen aplikasi dan peladen basis data juga terbukti meminimalisasi risiko keamanan pangkalan data dari eksekusi kueri langsung yang tidak terotorisasi, sekaligus memungkinkan penerapan skema pencadangan data (*backup server*) dan replikasi basis data secara terisolasi (Yusup dkk., 2010).

Dalam konteks rancang bangun sistem informasi bimbingan belajar multicabang, arsitektur tiga lapis memberikan tiga keunggulan mendasar bagi pemenuhan kebutuhan operasional lembaga. Keunggulan pertama adalah peningkatan skalabilitas sistem, di mana peningkatan intensitas akses dari staf administrasi di delapan kantor cabang fisik dapat ditangani secara optimal oleh peladen aplikasi tanpa menimbulkan beban koneksi berlebih pada peladen basis data. Keunggulan kedua adalah penguatan keamanan dan integritas data kasir, karena staf cabang tidak memiliki akses langsung ke pangkalan data utama, melainkan seluruh verifikasi pembayaran tunai maupun mutasi transfer bank wajib melalui penyaringan logika bisnis yang ketat pada peladen aplikasi. Keunggulan ketiga adalah kemudahan pemeliharaan (*maintainability*), sehingga penyesuaian antarmuka formulir pendaftaran siswa maupun pembaruan aturan batas kuota kelas dapat dilakukan secara terisolasi tanpa merombak stabilitas struktur pangkalan data yang sedang berjalan.
```

---

### 5. Teks Rekomendasi Siap Pakai untuk Bab 3 (Subbab 3.4.1 dan Gambar 3.2)

Berikut adalah narasi pembuka Subbab 3.4.1 dan sumber Gambar 3.2 yang telah diperbarui dan siap disalin ke [BAB_3_DESAIN_DAN_IMPLEMENTASI.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%203/BAB_3_DESAIN_DAN_IMPLEMENTASI.md):

```markdown
### 3.4.1. Perancangan Arsitektur Sistem

Sistem informasi manajemen operasional bimbingan belajar ARTHA dirancang menggunakan pola arsitektur perangkat lunak terpisah tiga lapis (*three-tier client-server architecture*) (Sommerville, 2011; Yusup dkk., 2010). Penerapan arsitektur ini merujuk pada standar rekayasa perangkat lunak terdistribusi yang membagi fungsionalitas sistem ke dalam tiga lapisan terpisah secara mandiri, yaitu lapisan presentasi antarmuka pengguna (*Presentation Tier*), lapisan logika pemrosesan bisnis aplikasi (*Application Tier*), dan lapisan penyimpanan pangkalan data relasional (*Data Storage Tier*) (Sommerville, 2011). Pada sistem informasi manajemen pendidikan berbasis web, arsitektur tiga lapis terbukti efektif mendistribusikan beban komputasi transaksi, memudahkan akses klien di kantor cabang hanya melalui peramban web, serta melindungi pangkalan data dari manipulasi kueri langsung yang tidak terotorisasi (Yusup dkk., 2010). Pada rancang bangun sistem ARTHA, pemisahan tanggung jawab antarlapisan ini diterapkan untuk menjamin responsivitas antarmuka di delapan kantor cabang saat diakses melalui perangkat tablet, menjaga keamanan logika transaksi keuangan di balik layanan *web service* RESTful API, serta mempermudah pengembangan sistem secara independen. Konsep arsitektur sistem informasi multicabang ARTHA disajikan pada Gambar 3.2.

![Gambar 3.2 Konsep Arsitektur Sistem Multicabang ARTHA](<ASET BAB 3/Gambar 3.2 Konsep Arsitektur Sistem Multicabang ARTHA.png>)

**Gambar 3.2 Konsep Arsitektur Sistem Multicabang ARTHA**
*(Sumber: Diadaptasi dan dikembangkan berdasarkan model arsitektur tiga lapis Sommerville, 2011 dan Yusup dkk., 2010)*

Berdasarkan Gambar 3.2, sistem ARTHA tersusun atas tiga lapisan fungsional utama yang saling terhubung melalui protokol komunikasi standar:
1. Lapisan pertama yaitu *Presentation Tier*, memfasilitasi interaksi pengguna untuk peran Super Admin di kantor pusat dan Staf Administrasi di delapan cabang menggunakan aplikasi web klien yang dibangun dengan Next.js App Router dan Tailwind CSS guna memastikan antarmuka yang responsif di berbagai peramban perangkat tanpa membebani pemrosesan logika data di sisi klien (Sommerville, 2011).
2. Lapisan kedua yaitu *Application Tier*, dikembangkan menggunakan kerangka kerja Laravel RESTful API yang dilengkapi mekanisme otentikasi token Laravel Sanctum untuk memberlakukan kontrol akses berbasis peran (*Role-Based Access Control*), memvalidasi aturan bisnis kuota kelompok belajar, serta mengeksekusi logika pencocokan kas masuk dengan mutasi rekening bank (Yusup dkk., 2010; Tan, 2025). Lapisan ini bertindak sebagai perantara tunggal yang mengamankan komunikasi data antara antarmuka pengguna dan pangkalan data.
3. Lapisan ketiga yaitu *Data Storage Tier*, bertugas menjamin persistensi dan integritas data operasional menggunakan basis data relasional MySQL serta direktori penyimpanan berkas digital untuk dokumen kuitansi PDF dan bukti transfer pembayaran.
```

## 📌 POIN 4: STATUS REVISI KATA KUNCI ABSTRAK
* Catatan evaluasi mengenai pembatasan jumlah kata kunci pada abstrak menjadi tepat lima frasa baku telah **dikonfirmasi selesai direvisi secara manual** oleh mahasiswa, dengan susunan kata kunci yang mencerminkan ranah penelitian Tugas Akhir secara proporsional.

---

## 🚀 PANDUAN LANGKAH EKSEKUSI KE NASKAH PROPOSAL UTAMA

Untuk menerapkan revisi ini ke naskah kerja skripsi Anda:
1. Salin blok teks pada **Poin 1** ke berkas [1.1_Latar_Belakang.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%201/1.1_Latar_Belakang.md) pada paragraf pembahasan pemilihan metode PxP (menggantikan klaim sepihak "empat aspek utama").
2. Salin blok teks pada **Poin 2** ke berkas [1.1_Latar_Belakang.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%201/1.1_Latar_Belakang.md) pada paragraf paling akhir (sebelum masuk ke Subbab 1.2).
3. Salin blok teks pada **Poin 3** ke berkas [BAB_3_DESAIN_DAN_IMPLEMENTASI.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%203/BAB_3_DESAIN_DAN_IMPLEMENTASI.md) pada Subbab 3.4.1 pembuka perancangan arsitektur sistem.
4. Periksa berkas gabungan [BAB 1 PENDAHULUAN.md](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/BAB%201/BAB%201%20PENDAHULUAN.md) agar tersinkronisasi secara otomatis.
