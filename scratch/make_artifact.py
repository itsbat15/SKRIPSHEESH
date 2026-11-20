import os, sys

target_path = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\LAPORAN_AUDIT_FORENSIK_10_PENELITIAN_TERDAHULU.md'

header = """# LAPORAN AUDIT FORENSIK DAN VERIFIKASI KLAIM EMPIRIS 10 PENELITIAN TERDAHULU (TABEL 2.6)

> [!IMPORTANT]
> **STATUS DOKUMEN NASKAH PROPOSAL:**  
> Berkas naskah proposal skripsi `2.2_Penelitian_Terdahulu.md` **TIDAK MENGALAMI PERUBAHAN APAPUN** pada tahapan ini. Seluruh data ketidaksesuaian, nomor baris kutipan verbatim dari sepuluh jurnal, dan draf usulan kalimat perbaikan disajikan secara utuh dalam dokumen audit ini agar dapat diperiksa serta disetujui terlebih dahulu oleh Mas Ariel.

---

## 1. Ringkasan Eksekutif Hasil Audit Forensik

Pemeriksaan forensik mendalam telah dilaksanakan terhadap sepuluh rujukan penelitian terdahulu yang tercantum pada Tabel 2.6 Proposal Tugas Akhir ARTHA. Setiap klaim atomik pada kolom Permasalahan, Metode, Hasil Penelitian, dan Keterkaitan dicocokkan secara kata per kata terhadap teks penuh jurnal yang tersimpan pada direktori `JURNAL/36_REFERENSI_TXT`. Audit ini berawal dari kejelian Mas Ariel yang menemukan ketidaksesuaian pada rujukan nomor 1 (Fajriansyah dkk., 2026), di mana fitur pencatatan presensi yang berstatus saran penelitian masa depan justru tertulis sebagai hasil penelitian yang telah dibangun.

Berdasarkan penelusuran menyeluruh dari halaman awal hingga halaman akhir pada kesepuluh berkas jurnal acuan, terbukti bahwa temuan serupa juga ditemukan pada beberapa baris rujukan lainnya. Pola ketidaksesuaian tersebut dapat dikelompokkan ke dalam empat klasifikasi utama:
1. **Fitur Saran Masa Depan / Wacana Diklaim Sebagai Hasil**: Modul yang hanya disarankan untuk penelitian lanjutan atau sekadar tertulis pada diagram use case konseptual tanpa diimplementasikan dan diuji, dituliskan seolah-olah telah selesai dibangun (terjadi pada Baris 1, Baris 2, dan Baris 8).
2. **Klaim Pengujian dan Metrik Terlalu Berlebihan (*Overclaim*)**: Munculnya klaim keberhasilan seratus persen tanpa kendala teknis atau efisiensi waktu pemrosesan, padahal jurnal tidak menyajikan tabel pengujian, skenario uji hanya bersifat parsial, atau pengujian efisiensi tersebut sama sekali tidak dilakukan (terjadi pada Baris 1, Baris 2, Baris 4, Baris 5, Baris 6, dan Baris 10).
3. **Penyimpangan Fakta Arsitektur dan Kondisi Empiris Mitra**: Terjadi ketidakakuratan penyebutan platform (seperti aplikasi desktop Windows yang tidak disebutkan platform desktopnya), anggapan unit lokasi tunggal (*single-branch*) pada lembaga yang memiliki cabang di kota lain, serta penghilangan fakta bahwa penelitian hanya mencakup perancangan antarmuka Figma tanpa pembuatan kode program (terjadi pada Baris 1, Baris 3, Baris 4, Baris 5, dan Baris 6).
4. **Penggunaan Diksi Tambahan yang Tidak Ada pada Teks Jurnal**: Pemakaian istilah tertentu pada narasi tabel yang sama sekali tidak muncul di dalam naskah jurnal sumber, seperti kata *transparan*, *okupansi*, dan *akad* (terjadi pada Baris 3, Baris 4, dan Baris 10).

Tabel 1 menyajikan rekapitulasi status verifikasi forensik untuk kesepuluh baris penelitian terdahulu.

### Tabel 1. Rekapitulasi Status Verifikasi Forensik 10 Baris Penelitian Terdahulu

| Baris | Penulis dan Tahun | Objek / Sistem yang Diteliti | Temuan Kritis / Berlebihan Utama | Rekomendasi Tindakan |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Fajriansyah dkk. (2026) | SIMB Bee Hive Tutoring | Presensi adalah saran masa depan; lokasi operasional di Depok dan Tangsel (bukan single-branch); pengujian Black Box tidak dilaporkan di bagian Hasil; notifikasi push adalah saran; SQLite disebut terpusat (bukan lokal). | **Wajib Revisi** (Koreksi modul presensi, status cabang, notifikasi, dan konteks uji). |
| **2** | Tiana dan Gunanto (2026) | Bimbel Web Mobile (Texas Kotabumi) | Presensi dan jadwal hanya ada di Use Case (tidak ada di tabel database, implementasi, maupun pengujian); klaim efisiensi waktu terukur tidak ada di jurnal; belum mencantumkan nama bimbel Texas Kotabumi Lampung Utara. | **Wajib Revisi** (Hapus klaim presensi dan jadwal yang diuji, hapus klaim efisiensi kuantitatif). |
| **3** | Zakaria dkk. (2023) | MandarinPro (Kursus Feng Huang Bali) | Aplikasi berbasis Desktop Windows (bukan web); kata *transparan* tidak ada di jurnal; pengujian menggunakan Alpha dan Beta Testing (bukan Black Box tersirat); risiko kehilangan dan manipulasi tidak disebut (jurnal: pencegahan penyalahgunaan keuangan). | **Wajib Revisi** (Sebutkan platform Desktop Windows, ubah metode uji ke Alpha-Beta, sesuaikan diksi). |
| **4** | Ahadi, Pariyadi, Djauhari (2025) | SIM Hotel Multicabang (Royal Heritage Jambi) | Kata *okupansi* dan *pendapatan keuangan* tidak ada; reservasi antarcabang tidak ada (reservasi per cabang); laporan konsolidasi tidak diuji di Black Box; Black Box hanya lima skenario awal; metode waterfall-iterative. | **Wajib Revisi** (Hapus okupansi dan reservasi antarcabang, sesuaikan batasan pengujian fungsional). |
| **5** | Hendri dkk. (2025) | Prototipe SIA SPP Yayasan Semesta Khatulistiwa | Produk murni rancangan Figma dan UML (tidak ada implementasi kode program); klaim evaluasi perancangan terbukti meningkatkan akurasi tidak ada; verifikasi nontunai dan kuitansi otomatis tidak ada di teks. | **Wajib Revisi** (Tegaskan status produk sebagai rancangan prototipe Figma tanpa implementasi kode). |
| **6** | Sudirman dan Tristianti (2021) | Sistem Rekonsiliasi Kas Bank CV. Lisa Pratama | Klaim pengujian membuktikan eliminasi selisih pembukuan tidak ada di jurnal (tidak ada bab uji); lokasi perusahaan di Semarang tidak ada bukti (Semarang alamat kampus penulis); metode R&D dengan pendekatan SDLC Prototyping. | **Wajib Revisi** (Hapus klaim pembuktian eliminasi selisih, koreksi metode R&D Prototyping, sesuaikan fakta lokasi). |
| **7** | Khafidhoh, Febrianti, Sujono (2026) | Penjadwalan Algoritma Genetika Bimbel AHE | Jurnal menyatakan *meminimalkan* bentrokan (bukan mengeliminasi); bentrokan jadwal hanya untuk pengajar (frasa antarmurid tidak ada); frasa tanpa kesalahan logika dan valid tidak ada; data kuantitatif pengujian tidak disajikan. | **Wajib Revisi** (Ganti kata mengeliminasi menjadi meminimalkan, hapus antarmurid, sesuaikan narasi uji). |
| **8** | Yuanita, Wijayanto, Cahyono (2022) | Sistem Jadwal Terintegrasi MBKM (React-Django) | Validasi otomatis kuota ruangan tidak ada (kata kuota tidak muncul); ketersediaan pengajar tidak ada; klaim meniadakan benturan berlebihan; penulis hanya mengembangkan sisi front-end React.js (bukan sistem utuh). | **Wajib Revisi** (Hapus klaim validasi kuota ruangan, klarifikasi lingkup pengembangan front-end React.js). |
| **9** | Musofa, Fadli, Murniati, Fahmi (2025) | Buku Tamu Digital Diskominfo Lombok Tengah (PxP) | Tiga butir masalah pada tabel tidak ada di teks jurnal; klaim adaptivitas PxP bagi pengembang mandiri tidak dinyatakan di kesimpulan; QR Code dipindai tamu untuk buka form web (bukan modul scanner internal); NIK verifikasi 98,7%. | **Wajib Revisi** (Sesuaikan rumusan masalah riil, perjelas alur QR Code, sesuaikan istilah verifikasi identitas). |
| **10** | Apriyanti, Wati, Najaf (2024) | E-Kavling PT Mutiara Putri Gemilang (PxP) | Klaim 100% tanpa kendala untuk seluruh alur transaksi berlebihan (Black Box hanya tiga skenario pada satu fitur validasi berkas); kata *akad* tidak ada; masalah verifikasi berkas keliru ditempatkan di masalah; uji responsivitas menunjukkan beberapa halaman tidak responsif. | **Wajib Revisi** (Hapus klaim 100% tanpa kendala, hapus kata akad, sesuaikan lingkup uji Black Box riil). |

---

## 2. Laporan Forensik Rinci Per Baris Penelitian

Bagian ini menguraikan analisis pembuktian kata per kata secara terperinci untuk masing-masing baris penelitian terdahulu terhadap naskah asli jurnal sumber.

```
================================================================================
AUDIT BARIS 1: Satria Nur Fajriansyah dkk. (2026)
================================================================================
```

### 2.1. Profil Rujukan Baris 1
- Penulis: Satria Nur Fajriansyah, Muhammad Subaktiar Wijaya, Daffa Arifta Eryana, Alaudin Safa, Harsya Rafif Pramadhan, Arya Wicaksono, Muhammad Ilham Baehaqi, Filius Deivivi, Dandy Nurfajriansyah, dan Sopiyan Apandi.
- Tahun Terbit: 2026.
- Judul Artikel: Rancang Bangun Sistem Informasi Bimbingan Belajar Berbasis Web (Studi Kasus: Bee Hive Tutoring).
- Nama Publikasi: Jurnal Rekayasa Informasi Swadharma (JRIS), Volume 06 Nomor 02 Juli 2026, Halaman 115:126. Akreditasi SINTA 3.
- Berkas Teks Rujukan: `03_Fajriansyah_dkk_2026_JRIS_SINTA3.txt` (1595 baris).

### 2.2. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Pengelolaan operasional bimbingan belajar Bee Hive Tutoring di Tangerang Selatan masih mengandalkan Google Forms, spreadsheets, dan grup WhatsApp. Kondisi konvensional tersebut memicu penjadwalan kelas tutor tidak terstruktur, data peserta didik dan tutor tercecer, pelaporan hasil evaluasi belajar terhambat, serta minimnya proteksi keamanan data akademik.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan Sistem Informasi Bimbingan Belajar (SIMB) berbasis web yang menyediakan layanan pendaftaran daring mandiri, pencatatan presensi, pelaporan log belajar, serta pengiriman notifikasi terpusat. Pengujian fungsional melalui Black Box Testing membuktikan seluruh alur berjalan valid tanpa kendala teknis. Penerapan sistem ini berhasil memangkas durasi pendaftaran siswa baru menjadi di bawah dua detik serta meniadakan potensi benturan jadwal mengajar tutor hingga 0%.
- **Keterkaitan**: Keterkaitan terletak pada kesamaan domain digitalisasi administrasi bimbingan belajar nonformal. Perbedaannya, sistem Bee Hive berfokus pada operasional satu unit lokasi tunggal (single-branch) dengan basis data lokal SQLite, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang terpadu dengan pembatasan hak akses berbasis peran, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).

### 2.3. Verifikasi Klaim Atomik Baris 1
1. **Klaim Pencatatan Presensi pada Hasil Penelitian**:
   - Status: **TIDAK SESUAI / KRITIS**.
   - Bukti Teks: Kata presensi sama sekali tidak ditemukan pada bagian Hasil dan Pembahasan (baris 870:1330). Kata presensi hanya muncul satu kali di seluruh naskah, yaitu pada Bab 5 Kesimpulan dan Saran pada baris 1383:1385: *"pengembangan modul presensi digital secara otomatis untuk mempermudah monitoring kehadiran siswa dan tutor secara real-time"*. Fakta ini membuktikan bahwa presensi merupakan saran penelitian masa depan dan bukan modul yang telah diimplementasikan.
2. **Klaim Operasional Satu Unit Tunggal (Single-Branch)**:
   - Status: **TIDAK SESUAI / KONTRADIKTIF**.
   - Bukti Teks: Naskah jurnal pada baris 260:263 secara eksplisit menyatakan bahwa Bee Hive Tutoring beroperasi di dua kota: *"Bee Hive Tutoring merupakan salah satu bimbingan belajar yang berlokasi di Depok dan Tangerang Selatan..."*. Menyebut sistem Bee Hive berfokus pada unit tunggal bertentangan dengan profil mitra di jurnal. Diksi yang tepat adalah sistem Bee Hive belum memiliki modul pengelolaan multicabang terintegrasi.
3. **Klaim Lokasi Penelitian di Tangerang Selatan**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Walaupun mitra memiliki cabang di Tangerang Selatan, lokasi spesifik pelaksanaan penelitian berada di Kota Depok (baris 27:28 dan baris 413:415: *"dilaksanakan di Bee Hive Tutoring yang berlokasi di Kota Depok"*).
4. **Klaim Pengiriman Notifikasi Terpusat**:
   - Status: **BERLEBIHAN / PERLU DIPERHALUS**.
   - Bukti Teks: Fitur yang dibangun hanyalah pengiriman email konfirmasi pendaftaran akun otomatis via Brevo SMTP (baris 422, baris 835:842, dan baris 1083:1085). Notifikasi push terpusat justru merupakan saran masa depan pada baris 1386:1388: *"penambahan fitur push notification pada aplikasi mobile untuk meningkatkan keterlibatan pengguna"*.
5. **Klaim Hasil Pengujian Black Box Testing**:
   - Status: **BERLEBIHAN**.
   - Bukti Teks: Black Box Testing disebutkan pada tahap perancangan metode (baris 768:771), tetapi pada Bab Hasil dan Pembahasan (baris 870:1330) penulis tidak menyajikan tabel kasus uji, data butir uji fungsional, maupun bukti eksekusi pengujian.
6. **Klaim Basis Data Lokal SQLite**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Jurnal tidak menyebut basis data lokal. Pada baris 35:36 dan baris 420:421, jurnal menyebut: *"penyimpanan terpusat pada basis data SQLite"* yang dipadukan dengan sinkronisasi Google Sheets API.
7. **Klaim Durasi Pendaftaran di Bawah Dua Detik**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Angka kurang dari dua detik tercantum pada baris 1134:1136 sebagai durasi pemrosesan otomatis sistem setelah data pendaftaran disubmit (verifikasi, simpan database, sinkronisasi Sheets, dan kirim email konfirmasi), bukan durasi pengisian formulir pendaftaran oleh siswa.

### 2.4. Pemilahan Fitur Riil vs Saran Masa Depan (Fajriansyah dkk., 2026)
- **Fitur Riil yang Dibangun dan Dilaporkan**: Pendaftaran mandiri siswa baru secara daring, pencatatan log belajar tutor (materi, durasi, catatan), sinkronisasi rekapitulasi ke Google Sheets API, pengiriman email konfirmasi pendaftaran akun via Brevo SMTP, serta manajemen data tutor dan jadwal berbasis Laravel dan SQLite.
- **Fitur Saran Masa Depan**: Modul presensi digital otomatis siswa dan tutor, notifikasi push aplikasi mobile, integrasi pembayaran daring (payment gateway), serta portal khusus pemantauan orang tua murid.

### 2.5. Usulan Teks Koreksi Baris 1
- **Permasalahan**: Pengelolaan operasional bimbingan belajar Bee Hive Tutoring yang berlokasi di Depok dan Tangerang Selatan masih mengandalkan Google Forms, spreadsheets, dan grup WhatsApp. Kondisi konvensional tersebut memicu penjadwalan kelas tutor tidak terstruktur, data peserta didik dan tutor tercecer, pelaporan hasil evaluasi belajar terhambat, serta minimnya proteksi keamanan data akademik lembaga.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan Sistem Informasi Bimbingan Belajar (SIMB) berbasis web menggunakan kerangka kerja Laravel dan basis data SQLite yang menyediakan layanan pendaftaran daring mandiri, pencatatan log belajar tutor, sinkronisasi rekapitulasi data melalui Google Sheets API, serta pengiriman email konfirmasi akun melalui Brevo SMTP. Pengujian fungsional direncanakan menggunakan metode Black Box Testing. Penerapan sistem ini berhasil memangkas durasi pemrosesan verifikasi pendaftaran oleh sistem menjadi di bawah dua detik dibandingkan pemrosesan manual sebelumnya yang memakan waktu sepuluh hingga lima belas menit, serta meniadakan potensi benturan jadwal mengajar tutor hingga nol persen.
- **Keterkaitan**: Keterkaitan terletak pada kesamaan domain digitalisasi administrasi operasional bimbingan belajar nonformal. Perbedaannya, sistem Bee Hive belum dilengkapi modul manajemen multicabang terpusat dan modul presensi kehadiran terintegrasi, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang terpadu dengan pembatasan hak akses berbasis peran, pencatatan presensi siswa, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 2: Irma Tiana dan Sigit Gunanto (2026)
================================================================================
```

### 2.6. Profil Rujukan Baris 2
- Penulis: Irma Tiana dan Sigit Gunanto.
- Tahun Terbit: 2026.
- Judul Artikel: Sistem Informasi Bimbingan Belajar Berbasis Web Mobile.
- Nama Publikasi: Jurnal Komputer Terapan Terpadu Komputer Informasi dan Sistem Informasi (JUKTISI), Volume 4 Nomor 3 2026, Halaman 138:143. Akreditasi SINTA 4.
- Berkas Teks Rujukan: `15_Tiana_Gunanto_2026_JUKTISI_SINTA4.txt` (440 baris).

### 2.7. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Tata kelola administrasi dan operasional akademik bimbingan belajar masih dilaksanakan secara konvensional. Kondisi ini mengakibatkan inefisiensi waktu yang signifikan, memperbesar kerentanan kesalahan pencatatan data akademik, serta menimbulkan kendala dalam pemantauan informasi operasional secara waktu nyata.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi bimbingan belajar berbasis web mobile yang memfasilitasi modul registrasi peserta didik, pencatatan presensi, pengaturan jadwal belajar, serta rekapitulasi data akademik secara terstruktur dan responsif. Pengujian sistem membuktikan bahwa implementasi antarmuka web mobile mampu meningkatkan efisiensi waktu pemrosesan administrasi serta meminimalkan galat entri data operasional lembaga.
- **Keterkaitan**: Keterkaitan terletak pada kesamaan domain digitalisasi tata kelola administrasi dan penjadwalan bimbingan belajar nonformal. Perbedaannya, sistem bimbingan belajar pada penelitian Tiana dan Gunanto dirancang untuk satu unit cabang mandiri tanpa pengelolaan multicabang terpadu, tidak dilengkapi modul rekonsiliasi kas bank, serta tidak menggunakan metode Personal Extreme Programming (PxP).

### 2.8. Verifikasi Klaim Atomik Baris 2
1. **Klaim Modul Pencatatan Presensi**:
   - Status: **BERLEBIHAN / TIDAK DIIMPLEMENTASIKAN**.
   - Bukti Teks: Fitur melihat kehadiran hanya muncul pada diagram Use Case (baris 176) dan Sequence Diagram (baris 220) dari sudut pandang siswa. Dalam struktur tabel basis data (baris 256:289), implementasi antarmuka (baris 291:326), serta tabel pengujian Black Box (Tabel 1, baris 332:358), sama sekali tidak terdapat tabel presensi, formulir presensi, maupun pengujian pencatatan presensi.
2. **Klaim Modul Pengaturan Jadwal Belajar**:
   - Status: **BERLEBIHAN / TIDAK DIIMPLEMENTASIKAN**.
   - Bukti Teks: Serupa dengan presensi, fungsi jadwal hanya muncul sebagai fungsi siswa melihat jadwal belajar (baris 177 dan 214). Modul pembuatan atau pengaturan jadwal belajar oleh staf administrasi tidak pernah dirancang tabel basis datanya dan tidak diuji dalam pengujian sistem.
3. **Klaim Pembuktian Efisiensi Waktu dan Penurunan Galat Entri Data**:
   - Status: **TIDAK ADA DI JURNAL / BERLEBIHAN**.
   - Bukti Teks: Pengujian yang dilaporkan murni pengujian fungsionalitas Black Box terhadap enam skenario (login, kelola data siswa, kelola level, peserta kursus, kelola kelas, dan riwayat pembayaran) dengan hasil Sesuai (baris 332:358). Tidak ada pengujian performa durasi waktu pemrosesan maupun pengukuran galat entri data.
4. **Klaim Modul Registrasi Peserta Didik**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Yang dibangun dan diuji adalah menu kelola data siswa oleh staf administrasi (baris 340:342), bukan registrasi daring mandiri oleh calon murid.
5. **Klaim Lembaga Mitra dan Lokasi**:
   - Status: **PERLU DITAMBAHKAN**.
   - Bukti Teks: Penelitian dilakukan secara khusus pada bimbingan belajar Texas Kotabumi di Kabupaten Lampung Utara (baris 23:24 dan baris 67:68). Tabel eksisting belum mencantumkan identitas lembaga mitra ini.

### 2.9. Pemilahan Fitur Riil vs Rancangan Wacana (Tiana dan Gunanto, 2026)
- **Fitur Riil yang Dibangun dan Diuji**: Autentikasi login pengguna, pengelolaan data siswa oleh admin, pengelolaan data level bimbingan, pendaftaran siswa ke rombongan belajar (peserta kursus), pengelolaan pembagian kelas, serta pencatatan dan peninjauan riwayat pembayaran kursus.
- **Fitur Wacana / Hanya Ada pada UML**: Siswa melihat presensi kehadiran, siswa melihat jadwal belajar, dan siswa melihat nilai akademik.

### 2.10. Usulan Teks Koreksi Baris 2
- **Permasalahan**: Tata kelola administrasi pendaftaran siswa, pengelolaan level paket belajar, dan pencatatan riwayat pembayaran pada bimbingan belajar Texas Kotabumi di Lampung Utara masih dilaksanakan secara konvensional. Kondisi ini mengakibatkan inefisiensi waktu operasional staf, memperbesar kerentanan kesalahan pencatatan data bimbingan, serta menyulitkan penelusuran riwayat iuran kursus siswa.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi bimbingan belajar berbasis web mobile yang memfasilitasi modul manajemen akun pengguna, pengelolaan master data siswa, pengaturan level kursus, pengalokasian peserta kursus ke dalam kelas, serta pencatatan riwayat pembayaran iuran bimbingan. Pengujian sistem menggunakan metode Black Box Testing pada enam skenario fungsi utama membuktikan bahwa seluruh fungsionalitas sistem berjalan sesuai dengan spesifikasi rancangan.
- **Keterkaitan**: Keterkaitan terletak pada kesamaan domain digitalisasi tata kelola administrasi dan pembayaran iuran bimbingan belajar nonformal. Perbedaannya, sistem pada penelitian Tiana dan Gunanto dirancang untuk satu unit lembaga mandiri tanpa pengelolaan multicabang terpadu, tidak mengintegrasikan modul rekonsiliasi mutasi kas bank, serta tidak menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 3: Teddy Marcus Zakaria dkk. (2023)
================================================================================
```

### 2.11. Profil Rujukan Baris 3
- Penulis: Teddy Marcus Zakaria, Julianti Kasih, Natanael Halim, dan Michael Sebastian Gunadi.
- Tahun Terbit: 2023.
- Judul Artikel: Pembangunan Sistem Informasi Administrasi Pembayaran Kursus (Studi Kasus: Kursus Bahasa Mandarin Feng Huang).
- Nama Publikasi: Jurnal Teknik Informatika dan Sistem Informasi (JuTISI), Volume 9 Nomor 1 April 2023, Halaman 13:26. Akreditasi SINTA 3.
- Berkas Teks Rujukan: `05_Zakaria_dkk_2023_JuTISI_SINTA3.txt` (662 baris).

### 2.12. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Tata kelola administrasi pembayaran pada lembaga kursus bahasa Mandarin Feng Huang di Bali masih dijalankan secara manual menggunakan kuitansi kertas dan kartu pembayaran fisik siswa. Prosedur konvensional tersebut memakan waktu lama, memperbesar risiko kehilangan atau manipulasi catatan pembayaran, serta menyulitkan penelusuran status keaktifan murid dan penyusunan laporan keuangan lembaga.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi pembayaran kursus (MandarinPro) yang mengotomatisasi registrasi siswa baru, pemrosesan transaksi iuran kursus, pelacakan riwayat pembayaran, serta penerbitan laporan keuangan yang terstruktur, akurat, dan transparan. Pengujian fungsionalitas membuktikan sistem berjalan valid serta mampu mempercepat pencatatan transaksi kas masuk dan pelaporan keuangan berkala.
- **Keterkaitan**: Keterkaitan terletak pada digitalisasi administrasi pembayaran iuran pendidikan kursus dan pelaporan transaksi kas masuk. Perbedaannya, penelitian Zakaria dkk. diterapkan pada satu lembaga kursus mandiri dengan metode Waterfall konvensional, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang secara terpadu, menerapkan rekonsiliasi mutasi rekening bank oleh Super Admin, serta dikembangkan dengan metode Personal Extreme Programming (PxP).

### 2.13. Verifikasi Klaim Atomik Baris 3
1. **Klaim Diksi "Transparan" pada Laporan Keuangan**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Kata transparan sama sekali tidak ditemukan di seluruh teks jurnal (nol kemunculan). Diksi ini merupakan penambahan subjektif yang tidak bersumber dari naskah.
2. **Klaim Hasil Terstruktur, Akurat, dan Mempercepat Pencatatan**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Frasa tersebut merupakan rumusan tujuan normatif pada abstrak (baris 40:42), bukan simpulan dari pengujian komparatif durasi transaksi.
3. **Klaim Risiko Kehilangan atau Manipulasi Catatan Pembayaran**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Kata kehilangan dan manipulasi tidak digunakan oleh penulis jurnal. Istilah yang tertulis pada baris 32 dan baris 83:84 adalah mencegah terjadinya *"penyalahgunaan keuangan"*.
4. **Klaim Metode Pengujian**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Jurnal tidak menyebut Black Box Testing biasa. Pada baris 146, 158, dan baris 524:585, pengujian secara tegas menggunakan **Alpha Testing** (tujuh skenario fungsional bersama staf internal) dan **Beta Testing** (uji penerimaan pengguna). Pada Alpha Testing tercatat kendala indeks basis data yang langsung diperbaiki oleh pengembang (baris 578:580).
5. **Klaim Platform Aplikasi (Desktop Windows)**:
   - Status: **KRITIS / WAJIB DICANTUMKAN**.
   - Bukti Teks: Sistem MandarinPro yang dibangun **berbasis Desktop Windows** (baris 599:600: *"aplikasi yang dibangun masih berbasis desktop, hanya di sistem operasi Windows"*). Pengembangan aplikasi berbasis web, Android, dan iOS berstatus saran masa depan (baris 605:608).

### 2.14. Pemilahan Fitur Riil vs Saran Masa Depan (Zakaria dkk., 2023)
- **Fitur Riil yang Dibangun dan Diuji**: Aplikasi Desktop Windows MandarinPro, registrasi siswa baru, pembayaran iuran kursus (disertai penanda diskon atau denda), pencatatan presensi sederhana saat siswa membayar, penerbitan kuitansi, penelusuran status keaktifan murid, serta laporan penerimaan kas harian dan bulanan.
- **Fitur Saran Masa Depan**: Pengembangan aplikasi berbasis web dan sistem operasi mobile (Android dan iOS), serta integrasi metode pembayaran daring.

### 2.15. Usulan Teks Koreksi Baris 3
- **Permasalahan**: Tata kelola administrasi pembayaran pada lembaga kursus bahasa Mandarin Feng Huang di Bali masih dijalankan secara semi-manual menggunakan pembukuan spreadsheet dan kuitansi fisik. Prosedur tersebut memakan waktu lama, membuka celah potensi penyalahgunaan keuangan, serta menyulitkan penelusuran status keaktifan murid dan penyusunan laporan penerimaan kas berkala.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi pembayaran kursus berbasis Desktop Windows (MandarinPro) yang mengotomatisasi registrasi siswa baru, pemrosesan pembayaran uang les, pelacakan riwayat pembayaran murid, serta penerbitan laporan penerimaan kas harian dan bulanan. Pengujian sistem melalui Alpha Testing terhadap tujuh skenario fungsionalitas dan Beta Testing kepada pengguna akhir membuktikan bahwa seluruh fungsi transaksi berjalan sesuai dengan kebutuhan operasional lembaga.
- **Keterkaitan**: Keterkaitan terletak pada digitalisasi administrasi pembayaran iuran pendidikan kursus dan pelaporan transaksi kas masuk. Perbedaannya, sistem MandarinPro dibangun berbasis aplikasi desktop Windows untuk satu lembaga kursus mandiri, sedangkan sistem Bimbel ARTHA Balikpapan dirancang berbasis aplikasi web terpadu untuk delapan kantor cabang, menerapkan rekonsiliasi mutasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 4: Ahmad Husna Ahadi, Pariyadi, dan Teuku Djauhari (2025)
================================================================================
```

### 2.16. Profil Rujukan Baris 4
- Penulis: Ahmad Husna Ahadi, Pariyadi, dan Teuku Djauhari.
- Tahun Terbit: 2025.
- Judul Artikel: Pengembangan Sistem Informasi Manajemen Perhotelan Multi Cabang Menggunakan Metode Waterfall.
- Nama Publikasi: Djtechno: Jurnal Teknologi Informasi, Volume 6 Nomor 1 Juli 2025, Halaman 132:144. Akreditasi SINTA 4.
- Berkas Teks Rujukan: `10_Ahadi_dkk_2025_Djtechno_SINTA4.txt` (770 baris).

### 2.17. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Manajemen Hotel Royal Heritage Jambi di Kota Jambi merencanakan ekspansi penambahan unit cabang perhotelan di berbagai wilayah kabupaten/kota lain hingga ke luar Provinsi Jambi. Sistem informasi manajemen eksisting belum mendukung integrasi multicabang, sehingga menyulitkan pemilik dalam memantau operasional, okupansi kamar, dan laporan pendapatan keuangan cabang secara terpusat.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi manajemen multicabang berbasis web yang mengintegrasikan pemantauan operasional, reservasi antarcabang, dan konsolidasi pelaporan transaksi secara terpusat. Pengujian sistem melalui Black Box Testing membuktikan seluruh fungsi operasional berjalan valid sesuai rancangan. Hasil evaluasi menegaskan bahwa sistem telah memenuhi standar kelayakan fungsional untuk mendukung ekspansi cabang dan siap diterapkan pada tahap deployment.
- **Keterkaitan**: Keterkaitan terletak pada arsitektur sistem informasi multicabang dengan isolasi hak akses cabang dan konsolidasi data terpusat bagi pimpinan. Perbedaannya, sistem Ahadi dkk. diterapkan pada sektor industri perhotelan, sedangkan sistem Bimbel ARTHA Balikpapan diterapkan pada domain bimbingan belajar delapan cabang dengan fitur batas kuota ruang kelas, rekonsiliasi kas bank, dan rekayasa perangkat lunak berbasis Personal Extreme Programming (PxP).

### 2.18. Verifikasi Klaim Atomik Baris 4
1. **Klaim Pemantauan Okupansi Kamar**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Kata okupansi atau occupancy sama sekali tidak pernah muncul dalam naskah jurnal (nol kemunculan).
2. **Klaim Laporan Pendapatan Keuangan Cabang**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Kata pendapatan dan keuangan tidak ditemukan dalam konteks laporan operasional cabang pada jurnal. Laporan yang dirancang hanya berupa data transaksi reservasi umum.
3. **Klaim Fitur Reservasi Antarcabang**:
   - Status: **TIDAK ADA / TIDAK SESUAI**.
   - Bukti Teks: Di jurnal, reservasi kamar dilakukan oleh staf front office cabang untuk kamar yang berada di cabang bersangkutan. Tidak terdapat mekanisme transaksi reservasi silang antarcabang.
4. **Klaim Konsolidasi Pelaporan Terpusat Diuji Valid**:
   - Status: **BERLEBIHAN**.
   - Bukti Teks: Laporan hanya tercantum sebagai kebutuhan aktor pimpinan pada tabel use case (Tabel 1 dan 3), namun pada tabel pengujian Black Box (Tabel 4, baris 496:527), menu laporan tidak diuji sama sekali. Pengujian Black Box hanya menguji lima skenario dasar: login, penambahan data cabang baru, penambahan data reservasi, pembayaran reservasi, dan proses check in tamu.
5. **Klaim Metode Waterfall**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Pada baris 224:226, penulis secara spesifik menyebutkan metode yang digunakan adalah *"waterfall-iterative"*, yang memadukan linieritas waterfall dengan tahapan berulang pada desain dan implementasi.

### 2.19. Pemilahan Fitur Riil vs Batasan Pengujian (Ahadi dkk., 2025)
- **Fitur Riil yang Dibangun dan Diuji Black Box**: Autentikasi hak akses pengguna, penambahan master data cabang baru oleh admin pusat, penambahan data reservasi kamar cabang, pencatatan pembayaran reservasi, dan pemrosesan check in tamu.
- **Fitur Belum Diuji pada Pengujian Fungsional**: Pemrosesan check out kamar, pembatalan reservasi, perpindahan kamar, pencetakan laporan berkala, serta isolasi data lintas cabang secara otomatis.

### 2.20. Usulan Teks Koreksi Baris 4
- **Permasalahan**: Manajemen Hotel Royal Heritage Jambi di Kota Jambi merencanakan ekspansi penambahan unit cabang perhotelan di berbagai wilayah kabupaten dan kota lain. Sistem informasi manajemen eksisting belum mendukung pengelolaan multicabang, sehingga menyulitkan manajemen pusat dalam mengelola data cabang baru, reservasi kamar, dan pemantauan transaksi reservasi secara terpadu.
- **Metode**: Waterfall (Waterfall-Iterative).
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi manajemen multicabang berbasis web yang memfasilitasi pendaftaran unit cabang baru, pengelolaan kamar, pencatatan reservasi tamu, pembayaran reservasi, serta pemrosesan check in pada masing-masing cabang. Pengujian fungsional menggunakan Black Box Testing pada lima skenario utama membuktikan sistem berjalan sesuai rancangan dan layak untuk dilanjutkan ke tahap penerapan.
- **Keterkaitan**: Keterkaitan terletak pada penerapan arsitektur sistem informasi multicabang terintegrasi untuk mendukung ekspansi unit operasional. Perbedaannya, sistem Ahadi dkk. diterapkan pada sektor industri perhotelan dengan metode waterfall-iterative, sedangkan sistem Bimbel ARTHA Balikpapan diterapkan pada domain operasional bimbingan belajar delapan cabang dengan validasi kuota kelas, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 5: Hendri dkk. (2025)
================================================================================
```

### 2.21. Profil Rujukan Baris 5
- Penulis: Hendri, Muhammad Alghifary, Herlina Yani Putri, Mutia Rahayu, dan Nurmalasari.
- Tahun Terbit: 2025.
- Judul Artikel: Sistem Informasi Akuntansi Penerimaan Kas Sumbangan Pembinaan Pendidikan (SPP) Menggunakan Metode Waterfall Berbasis Digital.
- Nama Publikasi: Jurnal Sistem Informasi dan Teknologi Peradaban (JUSTIAN), Volume 6 Nomor 1 Januari 2025, Halaman 12:20. Akreditasi SINTA 3.
- Berkas Teks Rujukan: `04_Hendri_dkk_2025_JUSTIAN_SINTA3.txt` (476 baris).

### 2.22. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Tata kelola sistem informasi akuntansi penerimaan kas, khususnya pembayaran Sumbangan Pembinaan Pendidikan (SPP) pada Yayasan Semesta Khatulistiwa di Pontianak, masih menggunakan pencatatan buku kas manual. Sistem manual ini sering menimbulkan ketidakefisienan pembukuan, keterlambatan penerbitan laporan keuangan berkala, serta rentan terhadap risiko kesalahan pencatatan riwayat tagihan murid.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan rancangan prototipe sistem informasi akuntansi penerimaan kas berbasis digital yang memodelkan alur pencatatan iuran SPP, pemantauan tagihan bulanan siswa, serta penyusunan laporan keuangan yayasan. Prototipe sistem menyediakan antarmuka untuk verifikasi transaksi pembayaran nontunai dan penerbitan bukti kuitansi otomatis. Evaluasi perancangan menunjukkan bahwa sistem ini mampu meningkatkan akurasi pembukuan dan mempermudah bendahara dalam mengontrol arus penerimaan kas secara tertib.
- **Keterkaitan**: Keterkaitan terletak pada fokus tata kelola penerimaan kas pembayaran SPP pendidikan dan pencegahan kesalahan pembukuan transaksi siswa. Perbedaannya, penelitian Hendri dkk. berfokus pada analisis kebutuhan dan perancangan prototipe antarmuka pada satu yayasan tanpa implementasi basis data multicabang, sedangkan sistem Bimbel ARTHA Balikpapan membangun aplikasi web operasional terintegrasi pada delapan cabang di Balikpapan dengan metode Personal Extreme Programming (PxP).

### 2.23. Verifikasi Klaim Atomik Baris 5
1. **Klaim Evaluasi Perancangan Terbukti Meningkatkan Akurasi Pembukuan**:
   - Status: **TIDAK ADA DI JURNAL / BERLEBIHAN**.
   - Bukti Teks: Penelitian ini **hanya berhenti pada tahap analisis dan desain antarmuka (Figma)**. Penulis tidak melakukan tahap pengkodean (implementasi program), tidak ada basis data riil, dan tidak melakukan pengujian sistem apa pun. Pernyataan bahwa sistem mampu meningkatkan akurasi pembukuan dan mempermudah bendahara hanyalah harapan teoritis dalam latar belakang (baris 34:36, baris 87:89, dan baris 435:440), bukan hasil evaluasi empiris.
2. **Klaim Verifikasi Transaksi Pembayaran Nontunai**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Kata verifikasi tidak ada di teks. Pada rancangan antarmuka Figma (baris 382:386), penulis hanya memodelkan visual pilihan metode pembayaran digital (OVO, GoPay, Dana, BCA, BNI, dan QRIS).
3. **Klaim Penerbitan Bukti Kuitansi Otomatis**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Kata kuitansi dan otomatis tidak digunakan oleh penulis. Yang dimodelkan pada antarmuka adalah tombol cetak dan cetak ulang bukti pembayaran (baris 381:382 dan baris 410:414).
4. **Klaim Penyusunan Laporan Keuangan Yayasan**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Istilah laporan keuangan yayasan terlalu luas. Yang dirancang secara spesifik adalah menu laporan pembayaran SPP bulanan yang dapat dicetak atau diekspor ke format PDF dan Excel (baris 340:342).
5. **Klaim Status Produk Penelitian**:
   - Status: **KRITIS / WAJIB DITEGASKAN**.
   - Bukti Teks: Produk penelitian ini murni merupakan rancangan antarmuka pengguna pada Figma dan pemodelan diagram UML, bukan perangkat lunak aplikasi web fungsional yang siap pakai.

### 2.24. Pemilahan Hasil Nyata vs Batasan Penelitian (Hendri dkk., 2025)
- **Hasil Nyata yang Dihasilkan**: Dokumen spesifikasi kebutuhan, pemodelan proses bisnis dan data menggunakan diagram UML (Use Case, Activity, Class Diagram), serta perancangan mock-up antarmuka pengguna berbasis Figma untuk pembayaran SPP dan laporan pembayaran.
- **Tahapan yang Tidak Dilaksanakan**: Implementasi pengkodean program, pembuatan basis data fisik, pengujian sistem (Black Box/UAT), dan deployment sistem.

### 2.25. Usulan Teks Koreksi Baris 5
- **Permasalahan**: Tata kelola penerimaan kas pembayaran Sumbangan Pembinaan Pendidikan (SPP) pada Yayasan Semesta Khatulistiwa di Pontianak masih menggunakan pencatatan buku kas manual. Kondisi tersebut memicu ketidakefisienan pembukuan, keterlambatan penyusunan rekapitulasi pembayaran siswa, serta memperbesar risiko selisih catatan penerimaan kas bendahara.
- **Metode**: Waterfall (hanya mencakup tahap analisis kebutuhan dan perancangan sistem).
- **Hasil Penelitian**: Penelitian ini menghasilkan rancangan prototipe antarmuka sistem informasi akuntansi penerimaan kas SPP berbasis Figma beserta pemodelan diagram UML. Rancangan sistem memodelkan menu pencatatan pembayaran SPP, visualisasi opsi kanal pembayaran nontunai, pencetakan bukti pembayaran, serta ekspor rekapitulasi pembayaran siswa ke format PDF dan Excel.
- **Keterkaitan**: Keterkaitan terletak pada fokus tata kelola penerimaan kas pembayaran SPP pendidikan dan pencatatan riwayat transaksi siswa. Perbedaannya, penelitian Hendri dkk. terbatas pada perancangan prototipe antarmuka Figma pada satu yayasan tanpa tahap pengkodean dan pengujian sistem, sedangkan sistem Bimbel ARTHA Balikpapan membangun aplikasi web operasional terintegrasi pada delapan cabang dengan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 6: Bagus Sudirman dan Mawada Tristianti (2021)
================================================================================
```

### 2.26. Profil Rujukan Baris 6
- Penulis: Bagus Sudirman dan Mawada Tristianti.
- Tahun Terbit: 2021.
- Judul Artikel: Perancangan Sistem Informasi Pengendalian Kas Bank Dengan Menggunakan Rekonsiliasi Bank.
- Nama Publikasi: MEANS (Media Informasi Analisa dan Sistem), Volume 6 Nomor 2 Desember 2021, Halaman 136:142. Akreditasi SINTA 4.
- Berkas Teks Rujukan: `11_Sudirman_Tristianti_2021_MEANS_SINTA4.txt` (617 baris).

### 2.27. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Perusahaan CV. Lisa Pratama di Semarang belum mengimplementasikan proses rekonsiliasi kas bank secara rutin dan terkomputerisasi. Kondisi tersebut menyebabkan pencatatan penerimaan dan pengeluaran kas internal sering mengalami perbedaan saldo dengan rekening koran bank, sehingga menyulitkan pengendalian internal dan membuka celah risiko kerugian finansial perusahaan.
- **Metode**: Prototyping.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi pengendalian kas bank berbasis client-server yang mengotomatisasi pencatatan penerimaan dan pengeluaran kas, penerbitan jurnal koreksi penyesuaian, serta pencocokan saldo kas terhadap rekening koran bank. Sistem ini dilengkapi dengan mekanisme pembatasan hak akses untuk menjamin keamanan data transaksi keuangan. Hasil implementasi membuktikan bahwa metode rekonsiliasi kas bank efektif dalam mengeliminasi selisih pembukuan dan memperkuat pengendalian internal perusahaan.
- **Keterkaitan**: Keterkaitan terletak pada penerapan teknik rekonsiliasi mutasi rekening bank untuk mengeliminasi selisih kas antara pembukuan internal dengan rekening bank. Perbedaannya, sistem Sudirman dan Tristianti dibangun berbasis aplikasi desktop client-server pada perusahaan dagang tunggal, sedangkan sistem Bimbel ARTHA Balikpapan mengintegrasikan verifikasi mutasi bank ke dalam arsitektur web multicabang bimbingan belajar dengan metode Personal Extreme Programming (PxP).

### 2.28. Verifikasi Klaim Atomik Baris 6
1. **Klaim Hasil Membuktikan Eliminasi Selisih Pembukuan**:
   - Status: **TIDAK ADA DI JURNAL / BERLEBIHAN**.
   - Bukti Teks: Jurnal sama sekali tidak menyajikan bab atau data pengujian empiris (tidak ada Black Box, White Box, UAT, maupun data perbandingan selisih kas sebelum dan sesudah implementasi). Paragraf kesimpulan (baris 499:510) hanya menyatakan dua hal normatif: sistem berhasil dibangun dengan batasan hak akses kasir/pimpinan dan sistem dapat mempermudah staf dalam membuat laporan kas bank. Klaim membuktikan efektivitas eliminasi selisih adalah klaim naratif tanpa bukti uji.
2. **Klaim Lokasi CV. Lisa Pratama di Semarang**:
   - Status: **TIDAK TEPAT / TANPA BUKTI TEKS**.
   - Bukti Teks: Kata Semarang hanya muncul pada baris afiliasi perguruan tinggi penulis (Universitas STEKOM Semarang, baris 17:18). Jurnal tidak pernah menyebut bahwa kantor operasional CV. Lisa Pratama berlokasi di Semarang. Dokumen justru mengindikasikan keterkaitan dengan wilayah Kabupaten Kendal.
3. **Klaim Pencatatan Sering Mengalami Perbedaan Saldo**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Kata sering tidak didukung data frekuensi kejadian pada jurnal. Masalah yang diuraikan pada baris 79:84 adalah perusahaan belum melakukan rekonsiliasi rutin sehingga manajemen tidak dapat memastikan keselarasan antara saldo pembukuan kas internal dengan rekening koran bank.
4. **Klaim Aplikasi Desktop Client-Server**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Diksi aplikasi desktop client-server tidak dinyatakan secara tegas pada bagian hasil pembahasan. Penulis hanya menyebut bahasa pemrograman Visual Basic pada tinjauan pustaka (baris 297:308).
5. **Klaim Metode Prototyping**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Jurnal menyatakan metodenya adalah Research and Development (R&D) dengan pendekatan siklus hidup pengembangan sistem Prototyping (baris 29:31 dan baris 348:353).

### 2.29. Pemilahan Hasil Nyata vs Klaim Tanpa Uji (Sudirman dan Tristianti, 2021)
- **Hasil Nyata yang Dihasilkan**: Perancangan dan pembuatan antarmuka formulir input penerimaan kas, formulir pengeluaran kas, form rekonsiliasi saldo kas bank, serta pemodelan menu hak akses pimpinan dan kasir.
- **Hal yang Tidak Ada di Jurnal**: Data uji fungsional, pengujian penerimaan pengguna, pengukuran angka penurunan selisih kas, serta evaluasi pengendalian internal secara kuantitatif.

### 2.30. Usulan Teks Koreksi Baris 6
- **Permasalahan**: Pengendalian transaksi kas pada CV. Lisa Pratama belum menerapkan proses rekonsiliasi kas bank secara berkala dan terkomputerisasi. Kondisi tersebut menyebabkan perusahaan tidak dapat memastikan kesesuaian saldo antara catatan kas internal dengan rekening koran bank, sehingga menyulitkan evaluasi arus kas dan pengendalian internal.
- **Metode**: Research and Development (R&D) dengan pendekatan Prototyping.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi pengendalian kas bank yang menyediakan antarmuka pencatatan penerimaan kas, formulir pengeluaran kas, serta fasilitas pencatatan data rekening koran bank guna mempermudah pembuatan laporan rekonsiliasi kas bank. Sistem ini dilengkapi dengan pemisahan hak akses antara staf kasir dan pimpinan untuk menjaga tertib administrasi keuangan.
- **Keterkaitan**: Keterkaitan terletak pada penerapan konsep rekonsiliasi mutasi rekening bank guna mencocokkan pencatatan kas internal dengan rekening bank. Perbedaannya, penelitian Sudirman dan Tristianti berfokus pada pengendalian kas entitas bisnis tunggal menggunakan pendekatan prototyping, sedangkan sistem Bimbel ARTHA Balikpapan mengintegrasikan verifikasi mutasi bank ke dalam arsitektur web multicabang bimbingan belajar dengan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 7: Nur Khafidhoh, Arfia Rahmi Febrianti, dan Sujono (2026)
================================================================================
```

### 2.31. Profil Rujukan Baris 7
- Penulis: Nur Khafidhoh, Arfia Rahmi Febrianti, dan Sujono.
- Tahun Terbit: 2026.
- Judul Artikel: Sistem Penjadwalan Bimbingan Belajar Menggunakan Algoritma Genetika Berbasis Web.
- Nama Publikasi: JTI (Jurnal Teknologi Informasi), Volume 20 Nomor 2 2026, Halaman 1:8. Akreditasi SINTA 4.
- Berkas Teks Rujukan: `12_Khafidhoh_dkk_2026_JTI_SINTA4.txt` (336 baris).

### 2.32. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Pengelolaan jadwal kegiatan belajar mengajar di Bimbingan Belajar Anak Hebat (AHE) Unit Megaluh 7059 di Jombang masih dilakukan secara manual. Mekanisme manual ini sering memicu bentrokan jam mengajar tutor, alokasi beban mengajar guru yang tidak merata, serta menyulitkan orang tua murid dalam menyelaraskan waktu belajar anak secara fleksibel.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem penjadwalan otomatis bimbingan belajar berbasis web yang menerapkan optimasi Algoritma Genetika dengan mempertimbangkan ketersediaan guru, preferensi waktu belajar, dan konfirmasi mengajar. Pengujian fungsional melalui Black Box Testing membuktikan seluruh fitur sistem berjalan valid tanpa kesalahan logika. Sistem terbukti berhasil mengeliminasi bentrokan jadwal antarmurid dan pengajar secara otomatis serta mendistribusikan notifikasi jadwal terpadu kepada orang tua siswa.
- **Keterkaitan**: Keterkaitan terletak pada manajemen otomasi penjadwalan bimbingan belajar untuk mencegah konflik waktu mengajar. Perbedaannya, sistem Bimbel AHE beroperasi pada satu unit belajar mandiri tanpa mekanisme pembatasan kapasitas fisik ruangan multicabang, sedangkan sistem Bimbel ARTHA Balikpapan menggabungkan validasi kuota kapasitas ruang kelas dan ketersediaan tentor pada delapan cabang dengan metode Personal Extreme Programming (PxP).

### 2.33. Verifikasi Klaim Atomik Baris 7
1. **Klaim Mengeliminasi Bentrokan Jadwal Antarmurid dan Pengajar**:
   - Status: **TIDAK SESUAI / KRITIS**.
   - Bukti Teks: Kesalahan terjadi pada dua aspek utama:
     1. Diksi jurnal secara konsisten menuliskan kata *"meminimalkan"* bentrokan jadwal (baris 40, baris 247, dan baris 271), bukan mengeliminasi (bentrokan nol).
     2. Objek bentrokan pada jurnal secara eksklusif hanyalah bentrokan jadwal pengajar (guru). Frasa antarmurid sama sekali tidak pernah muncul di seluruh teks naskah.
2. **Klaim Seluruh Fitur Berjalan Valid Tanpa Kesalahan Logika**:
   - Status: **BERLEBIHAN / TIDAK ADA DI JURNAL**.
   - Bukti Teks: Frasa tanpa kesalahan logika dan kata valid tidak ada di jurnal. Kesimpulan pada baris 325:327 hanya menyatakan: *"seluruh fungsi utama berjalan sesuai dengan perancangan"*. Penulis tidak menyajikan tabel skenario uji maupun metrik pengujian kuantitatif.
3. **Klaim Konfirmasi Mengajar**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Frasa konfirmasi mengajar hanya muncul pada abstrak bahasa Inggris (baris 36). Pada pembahasan teks bahasa Indonesia, penulis menggunakan konsep *"pemerataan jadwal mengajar"* (baris 90 dan baris 269:270).
4. **Klaim Notifikasi Jadwal Terpadu kepada Orang Tua Siswa**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Jurnal memodelkan penyampaian informasi jadwal kepada orang tua murid, namun tidak membangun modul push notification terpadu otomatis.
5. **Klaim Nama Institusi Mitra**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Nama lembaga pada baris 22:23 adalah *"Bimbingan Belajar Anak Hebat (AHE) Megaluh 7059"* (tanpa kata Unit). Jombang adalah lokasi perguruan tinggi penulis (Universitas Pesantren Tinggi Darul Ulum).

### 2.34. Pemilahan Hasil Nyata vs Batasan Pengujian (Khafidhoh dkk., 2026)
- **Hasil Nyata yang Dihasilkan**: Aplikasi web penjadwalan bimbingan belajar yang mengimplementasikan Algoritma Genetika dengan input data ketersediaan waktu pengajar dan preferensi belajar siswa untuk meminimalkan bentrokan jadwal guru.
- **Hal yang Tidak Disajikan di Jurnal**: Nilai parameter genetik (probabilitas crossover, probabilitas mutasi, populasi, generasi), nilai fungsi fitness hasil akhir, serta tabel rincian kasus uji Black Box.

### 2.35. Usulan Teks Koreksi Baris 7
- **Permasalahan**: Pengelolaan jadwal kegiatan belajar mengajar pada Bimbingan Belajar Anak Hebat (AHE) Megaluh 7059 masih dilakukan secara manual. Mekanisme konvensional tersebut berpotensi memicu bentrokan jam mengajar tutor, alokasi beban mengajar guru yang tidak merata, serta menyulitkan penyesuaian jadwal belajar siswa.
- **Metode**: Waterfall.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi penjadwalan bimbingan belajar berbasis web yang menerapkan optimasi Algoritma Genetika dengan mempertimbangkan ketersediaan jam mengajar guru, preferensi waktu belajar siswa, dan pemerataan alokasi mengajar. Pengujian sistem membuktikan bahwa fungsionalitas utama sistem berjalan sesuai perancangan dan mampu meminimalkan potensi konflik jadwal mengajar guru secara terkomputerisasi.
- **Keterkaitan**: Keterkaitan terletak pada pengelolaan otomasi penjadwalan bimbingan belajar guna mencegah konflik waktu mengajar tentor. Perbedaannya, sistem bimbingan belajar AHE berfokus pada penjadwalan satu lokasi dengan optimasi algoritma genetika tanpa validasi batas kuota fisik ruangan, sedangkan sistem Bimbel ARTHA Balikpapan menggabungkan validasi kuota kapasitas ruang kelas dan ketersediaan tentor pada delapan cabang menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 8: Herfina Intan Yuanita, Bangun Wijayanto, dan Teguh Cahyono (2022)
================================================================================
```

### 2.36. Profil Rujukan Baris 8
- Penulis: Herfina Intan Yuanita, Bangun Wijayanto, dan Teguh Cahyono.
- Tahun Terbit: 2022.
- Judul Artikel: Pengembangan Sistem Informasi Penjadwalan Terintegrasi Berbasis Web Menggunakan Pendekatan DevOps: Bagian Front-End.
- Nama Publikasi: Jurnal Teknologi Informasi dan Ilmu Komputer (JUTIF), Volume 3 Nomor 2 Desember 2022, Halaman 135:146. Akreditasi SINTA 2.
- Berkas Teks Rujukan: `01_Yuanita_dkk_2022_JUTIF_SINTA2.txt` (1830 baris).

### 2.37. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Pengelolaan dan penyusunan jadwal terintegrasi yang melibatkan banyak ruang dan kelas menghadapi kendala rumitnya alokasi kapasitas fisik ruangan serta risiko benturan jadwal antarwaktu kegiatan belajar. Proses penjadwalan tanpa validasi batas kuota ruangan memicu kelebihan kapasitas kelas serta ketidakefisienan pemanfaatan fasilitas ruang belajar.
- **Metode**: DevOps.
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem penjadwalan terintegrasi berbasis web yang dilengkapi mekanisme validasi otomatis terhadap kapasitas kuota ruangan, alokasi waktu sesi, serta ketersediaan pengajar untuk mencegah konflik penjadwalan. Pengujian antarmuka dan fungsionalitas membuktikan sistem berhasil meniadakan potensi benturan alokasi ruang dan waktu serta menyajikan informasi ketersediaan jadwal secara terpadu.
- **Keterkaitan**: Keterkaitan terletak pada penerapan mekanisme kendali kuota kapasitas ruang fisik dan pencegahan bentrok alokasi waktu penjadwalan. Perbedaannya, penelitian Yuanita dkk. berfokus pada lingkungan perkuliahan perguruan tinggi dengan pendekatan DevOps dalam tim, sedangkan sistem Bimbel ARTHA Balikpapan menerapkan validasi kapasitas ruang belajar dan ketersediaan tentor pada delapan cabang bimbingan belajar yang dibangun secara mandiri menggunakan metode Personal Extreme Programming (PxP).

### 2.38. Verifikasi Klaim Atomik Baris 8
1. **Klaim Validasi Otomatis Kuota Ruangan**:
   - Status: **TIDAK ADA DI JURNAL / KRITIS**.
   - Bukti Teks: Kata kuota sama sekali tidak pernah muncul di seluruh teks naskah (nol kemunculan). Dalam struktur data sistem, data ruangan hanya dicatat sebagai kode dan nama ruang tanpa atribut kapasitas fisik kursi maupun logika pembatasan kuota siswa.
2. **Klaim Ketersediaan Pengajar dan Meniadakan Potensi Benturan**:
   - Status: **TIDAK ADA DI JURNAL / BERLEBIHAN**.
   - Bukti Teks: Modul ketersediaan jam luang dosen tidak dimodelkan. Pengujian pada kesimpulan (baris 1605:1606) hanya menyatakan: *"sistem berhasil mengenerate tiga model jadwal"*. Penulis tidak pernah mengklaim bahwa benturan jadwal alokasi ruang dan waktu berhasil ditiadakan hingga seratus persen.
3. **Klaim Lingkup Pengembangan Sistem (Front-End Saja)**:
   - Status: **KRITIS / SANGAT PENTING DILURUSKAN**.
   - Bukti Teks: Judul dan isi artikel secara gamblang menyatakan bahwa penelitian Yuanita dkk. **hanya mengembangkan sisi Front-End (antarmuka web React.js)** dalam proyek magang MBKM (baris 24:27 dan baris 287:290). Logika pembuatan jadwal dilakukan di server terpisah (backend Django oleh mahasiswa lain), dan fitur pengunggahan ke SIA kampus masih berupa saran masa depan (baris 1636:1637).
4. **Klaim Permasalahan Kelebihan Kapasitas Kelas**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Masalah riil yang dihadapi fakultas adalah penyusunan jadwal kuliah manual memerlukan waktu berminggu-minggu serta rentan jadwal ganda bagi dosen dan mahasiswa. Masalah kelebihan kapasitas kuota kelas tidak pernah disebut di naskah.
5. **Klaim Penerapan Pendekatan DevOps**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Penulis menerapkan pendekatan DevOps secara parsial, yaitu hanya sampai pada tahap plan, code, build, dan test (baris 314:315). Tahap rilis dan pemantauan produksi belum diimplementasikan.

### 2.39. Pemilahan Hasil Nyata vs Klaim Berlebihan (Yuanita dkk., 2022)
- **Hasil Nyata yang Dihasilkan**: Antarmuka pengguna front-end berbasis React.js untuk manajemen data master (mata kuliah, dosen pengampu, ruang, dan slot waktu), form pengajuan preferensi jadwal, tampilan visual hasil tiga model jadwal kuliah dari server, serta pengujian fungsional front-end Black Box dengan status valid.
- **Hal yang Tidak Ada di Jurnal**: Validasi kuota kapasitas fisik kursi ruangan, deteksi otomatis benturan ketersediaan dosen, serta integrasi langsung ke sistem informasi akademik kampus.

### 2.40. Usulan Teks Koreksi Baris 8
- **Permasalahan**: Penyusunan jadwal perkuliahan terintegrasi di lingkungan perguruan tinggi yang melibatkan banyak kelas dan ruangan menghadapi kendala lamanya durasi kompilasi data manual serta rentannya jadwal ganda perkuliahan.
- **Metode**: DevOps (fokus pada tahapan perencanaan, pengkodean, build, dan pengujian front-end).
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi penjadwalan perkuliahan terintegrasi pada sisi front-end berbasis React.js yang menyediakan antarmuka pengelolaan data master jadwal serta penyajian visual tiga model rekomendasi jadwal hasil generate backend. Pengujian fungsionalitas front-end melalui Black Box Testing membuktikan bahwa antarmuka pengguna berhasil terhubung dengan antarmuka pemrograman aplikasi (API) dan seluruh komponen fungsi berjalan valid sesuai kebutuhan pengguna.
- **Keterkaitan**: Keterkaitan terletak pada digitalisasi perancangan jadwal kegiatan belajar guna mempermudah pengelolaan alokasi waktu dan ruangan. Perbedaannya, penelitian Yuanita dkk. berfokus pada pengembangan antarmuka front-end perkuliahan dalam tim proyek MBKM dengan pendekatan DevOps, sedangkan sistem Bimbel ARTHA Balikpapan membangun sistem penuh (full-stack) mandiri untuk delapan cabang bimbingan belajar dengan validasi kapasitas fisik kelas menggunakan metode Personal Extreme Programming (PxP).

---

```
================================================================================
AUDIT BARIS 9: Aolia Musofa, Sofiansyah Fadli, Wafiah Murniati, dan Hairul Fahmi (2025)
================================================================================
```

### 2.41. Profil Rujukan Baris 9
- Penulis: Aolia Musofa, Sofiansyah Fadli, Wafiah Murniati, dan Hairul Fahmi.
- Tahun Terbit: 2025.
- Judul Artikel: Pengembangan Aplikasi Buku Tamu Digital Menggunakan Metode Personal Extreme Programming.
- Nama Publikasi: Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK), Volume 12 Nomor 1 Februari 2025, Halaman 139:150. Akreditasi SINTA 2.
- Berkas Teks Rujukan: `13_Musofa_dkk_2025_JTIIK_SINTA2.txt` (1747 baris).

### 2.42. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Pengelolaan data kunjungan dan administrasi tamu pada Dinas Komunikasi dan Informatika Kabupaten Lombok Tengah masih memerlukan optimalisasi dalam kecepatan pemrosesan dan transparansi pendataan. Kondisi operasional tersebut memicu keterlambatan perekaman data pengunjung dinas, keterbatasan pelaporan riwayat tamu berkala, serta belum terwujudnya integrasi rekapitulasi data kunjungan secara otomatis.
- **Metode**: Personal Extreme Programming (PxP).
- **Hasil Penelitian**: Penelitian ini menghasilkan Aplikasi Buku Tamu Digital berbasis web yang dikembangkan melalui tujuh tahapan PxP oleh pengembang tunggal dengan integrasi pemindaian QR Code dan pelaporan dinas terpusat. Pengujian fungsional melalui Black Box Testing membuktikan seluruh fungsionalitas berjalan sukses seratus persen, didukung pengujian performa kuantitatif yang menunjukkan waktu tanggap pemindaian QR Code sebesar 312 ms serta akurasi verifikasi data pengunjung mencapai 98,7%. Hasil tersebut membuktikan bahwa PxP sangat adaptif bagi pengembang mandiri dalam membangun aplikasi web yang responsif dan andal.
- **Keterkaitan**: Keterkaitan terletak pada penerapan tujuh tahapan metodologi Personal Extreme Programming (PxP) oleh single developer untuk mewujudkan perangkat lunak yang presisi dan teruji seratus persen. Perbedaannya, penelitian Musofa dkk. berfokus pada aplikasi pelayanan buku tamu satu instansi pemerintah daerah, sedangkan sistem Bimbel ARTHA Balikpapan menerapkan PxP pada sistem operasional komersial delapan kantor cabang yang mengintegrasikan transaksi kas masuk dan penjadwalan kelas multi-ruangan.

### 2.43. Verifikasi Klaim Atomik Baris 9
1. **Klaim Tiga Butir Masalah Spesifik pada Tabel**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Tiga frasa masalah pada tabel eksisting (*"keterlambatan perekaman data pengunjung dinas"*, *"keterbatasan pelaporan riwayat tamu berkala"*, dan *"belum terwujudnya integrasi rekapitulasi data kunjungan secara otomatis"*) tidak tertulis di teks naskah. Masalah riil pada baris 118:126 adalah pencatatan masih menggunakan buku kertas fisik, sulitnya pencarian data tamu lama, serta risiko data hilang dan salah penulisan.
2. **Klaim Adaptivitas PxP bagi Pengembang Mandiri pada Kesimpulan**:
   - Status: **BERLEBIHAN**.
   - Bukti Teks: Kesimpulan artikel (baris 1450:1470) murni melaporkan keberhasilan pembangunan sistem dan hasil metrik pengujian sistem, tanpa ada pernyataan teoritis yang mengklaim pembuktian bahwa *"PxP sangat adaptif bagi pengembang mandiri"*.
3. **Klaim Pengembang Tunggal (Single Developer)**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Naskah artikel ditulis oleh empat orang peneliti (Aolia Musofa dkk.). Istilah pengembang tunggal di jurnal hanya dikutip dari literatur (baris 196:198) sebagai karakteristik umum metodologi PxP, bukan klaim empiris bahwa proyek ini dikerjakan oleh satu orang tanpa kolaborasi.
4. **Klaim Integrasi Pemindaian QR Code**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: QR Code yang disediakan di meja lobi kantor dinas dipindai oleh tamu menggunakan kamera ponsel masing-masing guna **membuka tautan formulir buku tamu web**, bukan aplikasi yang memuat pustaka scanner pemindai internal.
5. **Klaim Akurasi Verifikasi Data Pengunjung 98,7%**:
   - Status: **SESUAI DENGAN PENEGASAN ISTILAH**.
   - Bukti Teks: Angka 98,7% (dengan standar deviasi ±1,2% dari 100 data uji) tercantum pada Tabel 5 baris 1343:1360. Istilah spesifik di jurnal adalah pengujian *"verifikasi identitas tamu"* melalui validasi Nomor Induk Kependudukan (NIK).
6. **Klaim Waktu Tanggap 312 ms dan Pengujian Black Box 100%**:
   - Status: **SESUAI**.
   - Bukti Teks: Waktu respons rata-rata 312 ms (SD ±28 ms dari 30 kali uji) tercantum pada Tabel 5 baris 1343:1354. Black Box menguji 80 butir skenario fungsi dengan tingkat keberhasilan 100% (baris 1308:1320).

### 2.44. Pemilahan Hasil Nyata vs Klaim Interpretatif (Musofa dkk., 2025)
- **Hasil Nyata yang Dihasilkan**: Aplikasi web buku tamu digital dengan tujuh tahapan PxP, formulir input data tamu yang diakses via pindai stiker QR Code, verifikasi format NIK, dashboard grafik kunjungan, ekspor data tamu ke PDF, pengujian Black Box 80/80 (100%), waktu tanggap 312 ms, dan akurasi verifikasi NIK 98,7%.
- **Klaim Interpretatif Tambahan**: Pernyataan bahwa PxP terbukti adaptif dan andal bagi pengembang mandiri.

### 2.45. Usulan Teks Koreksi Baris 9
- **Permasalahan**: Pencatatan data tamu pada Dinas Komunikasi dan Informatika Kabupaten Lombok Tengah masih menggunakan buku register fisik. Mekanisme manual tersebut menyulitkan pencarian arsip riwayat kunjungan, rentan terhadap kerusakan atau kehilangan data, serta memperbesar risiko kesalahan pencatatan data identitas tamu dinas.
- **Metode**: Personal Extreme Programming (PxP) dengan tujuh tahapan terstruktur.
- **Hasil Penelitian**: Penelitian ini menghasilkan Aplikasi Buku Tamu Digital berbasis web yang memfasilitasi pengisian data kunjungan oleh tamu melalui pemindaian tautan QR Code serta penyediaan dashboard statistik kunjungan dan ekspor laporan PDF bagi staf dinas. Pengujian fungsionalitas menggunakan Black Box Testing membuktikan delapan puluh skenario uji berhasil dijalankan dengan persentase seratus persen. Hasil pengujian performa menunjukkan waktu tanggap sistem sebesar 312 ms serta akurasi verifikasi identitas tamu sebesar 98,7%.
- **Keterkaitan**: Keterkaitan terletak pada penerapan metodologi Personal Extreme Programming (PxP) secara komprehensif mulai dari analisis kebutuhan hingga retrospective guna membangun aplikasi web yang teruji fungsionalitas dan performanya. Perbedaannya, penelitian Musofa dkk. diterapkan pada sistem pelayanan tamu instansi pemerintah daerah satu lokasi, sedangkan sistem Bimbel ARTHA Balikpapan menerapkan PxP pada sistem operasional bisnis delapan cabang bimbingan belajar dengan transaksi kas dan validasi kuota ruang kelas.

---

```
================================================================================
AUDIT BARIS 10: Narti Apriyanti, Seftin Fitri Ana Wati, dan Abdul Rezha Efrat Najaf (2024)
================================================================================
```

### 2.46. Profil Rujukan Baris 10
- Penulis: Narti Apriyanti, Seftin Fitri Ana Wati, dan Abdul Rezha Efrat Najaf.
- Tahun Terbit: 2024.
- Judul Artikel: Penerapan Metode Personal Extreme Programming Dalam Pengembangan Website Penjualan Properti.
- Nama Publikasi: Jurnal Aplikasi Teknologi Informasi dan Manajemen (JATI), Volume 5 Nomor 2 Oktober 2024, Halaman 129:139. Akreditasi SINTA 4.
- Berkas Teks Rujukan: `14_Apriyanti_dkk_2024_JATI_SINTA4.txt` (1477 baris).

### 2.47. Teks Eksisting pada Tabel 2.6
- **Permasalahan**: Perusahaan properti PT Mutiara Putri Gemilang di Jombang menghadapi kendala efisiensi operasional dan keterbatasan pemasaran properti akibat sistem pencatatan penjualan kavling yang masih manual. Hal ini memicu risiko data transaksi tercecer, menghambat verifikasi kelengkapan berkas pembeli, serta memperlambat proses persetujuan akad transaksi penjualan.
- **Metode**: Personal Extreme Programming (PxP).
- **Hasil Penelitian**: Penelitian ini menghasilkan sistem informasi penjualan properti secara daring yang mencakup fitur katalog properti, pemesanan daring, pengunggahan berkas administrasi, serta verifikasi bukti transfer pembayaran. Pengujian fungsional melalui Black Box Testing membuktikan seluruh alur transaksi berjalan sukses 100% tanpa kendala. Evaluasi penerimaan sistem melalui User Acceptance Testing (UAT) yang melibatkan 15 responden (13 pengguna, satu direktur, dan satu admin) memperoleh persentase keberhasilan 91% dengan kategori Sangat Baik.
- **Keterkaitan**: Keterkaitan terletak pada efektivitas penerapan metodologi PxP oleh pengembang mandiri dan perancangan alur verifikasi berkas bukti bayar transaksi. Perbedaannya, sistem E-Kavling menangani objek penjualan tanah properti satu lokasi tanpa modul rekonsiliasi saldo kas mutasi bank, sedangkan sistem Bimbel ARTHA Balikpapan mengintegrasikan rekonsiliasi mutasi bank dan pembagian kelas siswa pada delapan cabang bimbingan belajar di Balikpapan.

### 2.48. Verifikasi Klaim Atomik Baris 10
1. **Klaim Black Box Membuktikan Seluruh Alur Transaksi 100% Tanpa Kendala**:
   - Status: **BERLEBIHAN / KRITIS**.
   - Bukti Teks: Tabel Black Box Testing pada jurnal (Tabel 5 baris 843:888) **HANYA MENYAJIKAN TIGA SKENARIO PADA SATU FITUR SAJA**, yaitu fitur validasi berkas pembelian properti oleh admin. Angka 100% sama sekali tidak tertulis pada teks naskah. Selain itu, pada pengujian responsivitas antarmuka perangkat (Tabel 8 baris 1115:1190), beberapa halaman dilaporkan **tidak responsif** pada perangkat mobile Android dan iOS (yaitu halaman validasi berkas, live chat, dan landing page). Menuliskan seluruh alur transaksi berjalan seratus persen tanpa kendala bertentangan dengan tabel pengujian jurnal.
2. **Klaim Hambatan Verifikasi Berkas dan Persetujuan Akad**:
   - Status: **TIDAK ADA DI JURNAL**.
   - Bukti Teks: Kata akad sama sekali tidak pernah muncul di seluruh naskah (nol kemunculan). Selain itu, verifikasi berkas pembeli di jurnal merupakan fitur solusi sistem baru yang dirancang penulis, bukan masalah operasional awal yang tercatat pada latar belakang.
3. **Klaim Verifikasi Bukti Transfer Pembayaran**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Kata transfer tidak digunakan. Metode pembayaran di jurnal mencakup cash, KPR, dan inhouse. Jurnal menggunakan istilah unggah bukti pembayaran oleh pembeli dan validasi bukti pembayaran oleh direktur (baris 805:810).
4. **Klaim UAT 15 Responden dan Skor 91% Sangat Baik**:
   - Status: **SESUAI DENGAN CATATAN INKONSISTENSI INTERNAL JURNAL**.
   - Bukti Teks: Skor 91% Sangat Baik tercantum pada baris 1206:1209. Rincian 15 responden (13 pengguna umum, satu direktur, dan satu admin) tercantum pada abstrak dan tabel perhitungan. Namun terdapat salah ketik internal pada kesimpulan artikel (baris 1275:1277) di mana penulis menuliskan *"dilakukan kepada 1 direktur, 1 admin, dan 1 pengguna"*.
5. **Klaim Pengembang Mandiri**:
   - Status: **PERLU DIPERHALUS**.
   - Bukti Teks: Jurnal memiliki tiga penulis akademisi (Narti Apriyanti dkk.). Karakteristik pengembang tunggal dikutip sebagai justifikasi pemilihan metode PxP (baris 113:116).

### 2.49. Pemilahan Hasil Nyata vs Temuan Pengujian (Apriyanti dkk., 2024)
- **Hasil Nyata yang Dihasilkan**: Website E-Kavling berbasis PxP dengan fitur daftar properti kavling, pemesanan dan pembelian kavling, pengunggahan berkas KTP dan KK oleh pembeli, validasi berkas oleh admin, validasi pembayaran oleh direktur, live chat, serta perolehan skor UAT 91% (Sangat Baik).
- **Keterbatasan Pengujian yang Dilaporkan**: Pengujian Black Box hanya disajikan untuk tiga skenario validasi berkas, serta antarmuka validasi berkas dan live chat belum responsif sempurna pada peramban telepon pintar.

### 2.50. Usulan Teks Koreksi Baris 10
- **Permasalahan**: Pengelolaan dan pemasaran penjualan tanah kavling pada PT Mutiara Putri Gemilang di Kabupaten Jombang masih mengandalkan pencatatan pembukuan manual dan penyebaran brosur fisik. Kondisi tersebut membatasi jangkauan promosi properti, memperbesar risiko catatan transaksi penjualan tercecer, serta memperlambat proses validasi data pembelian konsumen.
- **Metode**: Personal Extreme Programming (PxP).
- **Hasil Penelitian**: Penelitian ini menghasilkan situs web pemasaran dan penjualan properti (E-Kavling) yang memfasilitasi penelusuran daftar kavling, formulir pembelian tanah, pengunggahan berkas administrasi pembeli, serta validasi bukti pembayaran oleh direktur. Pengujian fungsionalitas menggunakan Black Box Testing pada fitur validasi berkas berjalan sesuai rancangan, serta evaluasi penerimaan pengguna (UAT) yang melibatkan lima belas responden memperoleh skor persentase sebesar 91% dengan kategori Sangat Baik.
- **Keterkaitan**: Keterkaitan terletak pada penerapan metodologi Personal Extreme Programming (PxP) dalam merancang alur transaksi penjualan daring dan validasi berkas bukti pembayaran. Perbedaannya, sistem E-Kavling menangani objek penjualan tanah kavling tunggal tanpa modul rekonsiliasi mutasi rekening kas bank, sedangkan sistem Bimbel ARTHA Balikpapan mengintegrasikan rekonsiliasi mutasi bank, manajemen kuota kelas, dan administrasi operasional pada delapan kantor cabang bimbingan belajar.

---

## 3. Matriks Komparasi Usulan Teks Revisi Tabel 2.6

Tabel 2 berikut menyajikan draf perbandingan menyeluruh antara teks eksisting saat ini dengan rumusan teks usulan revisi untuk kesepuluh baris penelitian terdahulu. Seluruh rumusan kalimat usulan telah disusun secara orisinal, patuh terhadap seluruh kaidah penulisan ilmiah ITK (bebas tanda dash panjang em-dash, minimal dua hingga tiga kalimat per paragraf atau sel, tanpa angka numerik di awal kalimat, serta format sitasi Author-Year yang baku).

### Tabel 2. Matriks Komparasi Teks Eksisting vs Teks Usulan Revisi

| No | Teks Eksisting pada Tabel 2.6 (Saat Ini) | Teks Usulan Revisi (Hasil Verifikasi Forensik) | Alasan Pokok Perubahan |
| :---: | :--- | :--- | :--- |
| **1** | **Hasil Penelitian:** Penelitian ini menghasilkan Sistem Informasi Bimbingan Belajar (SIMB) berbasis web yang menyediakan layanan pendaftaran daring mandiri, pencatatan presensi, pelaporan log belajar, serta pengiriman notifikasi terpusat. Pengujian fungsional melalui Black Box Testing membuktikan seluruh alur berjalan valid tanpa kendala teknis. Penerapan sistem ini berhasil memangkas durasi pendaftaran siswa baru menjadi di bawah dua detik serta meniadakan potensi benturan jadwal mengajar tutor hingga 0%.<br><br>**Keterkaitan:** Keterkaitan terletak pada kesamaan domain digitalisasi administrasi bimbingan belajar nonformal. Perbedaannya, sistem Bee Hive berfokus pada operasional satu unit lokasi tunggal (single-branch) dengan basis data lokal SQLite, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang terpadu dengan pembatasan hak akses berbasis peran, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP). | **Hasil Penelitian:** Penelitian ini menghasilkan Sistem Informasi Bimbingan Belajar (SIMB) berbasis web menggunakan kerangka kerja Laravel dan basis data SQLite yang menyediakan layanan pendaftaran daring mandiri, pencatatan log belajar tutor, sinkronisasi rekapitulasi data melalui Google Sheets API, serta pengiriman email konfirmasi akun melalui Brevo SMTP. Pengujian fungsional direncanakan menggunakan metode Black Box Testing. Penerapan sistem ini berhasil memangkas durasi pemrosesan verifikasi pendaftaran oleh sistem menjadi di bawah dua detik dibandingkan pemrosesan manual sebelumnya yang memakan waktu sepuluh hingga lima belas menit, serta meniadakan potensi benturan jadwal mengajar tutor hingga nol persen.<br><br>**Keterkaitan:** Keterkaitan terletak pada kesamaan domain digitalisasi administrasi operasional bimbingan belajar nonformal. Perbedaannya, sistem Bee Hive belum dilengkapi modul manajemen multicabang terpusat dan modul presensi kehadiran terintegrasi, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang terpadu dengan pembatasan hak akses berbasis peran, pencatatan presensi siswa, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP). | 1. Modul pencatatan presensi dihapus dari hasil karena berstatus saran masa depan pada baris 1383:1385.<br>2. Istilah single-branch dikoreksi karena Bee Hive beroperasi di Depok dan Tangsel (baris 260:263).<br>3. Konteks durasi 2 detik diperjelas sebagai waktu pemrosesan verifikasi pendaftaran otomatis sistem. |
| **2** | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi bimbingan belajar berbasis web mobile yang memfasilitasi modul registrasi peserta didik, pencatatan presensi, pengaturan jadwal belajar, serta rekapitulasi data akademik secara terstruktur dan responsif. Pengujian sistem membuktikan bahwa implementasi antarmuka web mobile mampu meningkatkan efisiensi waktu pemrosesan administrasi serta meminimalkan galat entri data operasional lembaga. | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi bimbingan belajar berbasis web mobile yang memfasilitasi modul manajemen akun pengguna, pengelolaan master data siswa, pengaturan level kursus, pengalokasian peserta kursus ke dalam kelas, serta pencatatan riwayat pembayaran iuran bimbingan. Pengujian sistem menggunakan metode Black Box Testing pada enam skenario fungsi utama membuktikan bahwa seluruh fungsionalitas sistem berjalan sesuai dengan spesifikasi rancangan. | 1. Modul presensi dan jadwal belajar dihapus dari hasil karena hanya ada di Use Case (tidak ada di database dan uji).<br>2. Klaim pengujian efisiensi waktu dan penurunan galat dihapus karena tidak ada data ujinya di jurnal.<br>3. Diselaraskan dengan enam skenario uji Black Box riil (Tabel 1 jurnal). |
| **3** | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi pembayaran kursus (MandarinPro) yang mengotomatisasi registrasi siswa baru, pemrosesan transaksi iuran kursus, pelacakan riwayat pembayaran, serta penerbitan laporan keuangan yang terstruktur, akurat, dan transparan. Pengujian fungsionalitas membuktikan sistem berjalan valid serta mampu mempercepat pencatatan transaksi kas masuk dan pelaporan keuangan berkala.<br><br>**Keterkaitan:** Perbedaannya, penelitian Zakaria dkk. diterapkan pada satu lembaga kursus mandiri dengan metode Waterfall konvensional, sedangkan sistem Bimbel ARTHA Balikpapan mengelola delapan kantor cabang secara terpadu... | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi pembayaran kursus berbasis Desktop Windows (MandarinPro) yang mengotomatisasi registrasi siswa baru, pemrosesan pembayaran uang les, pelacakan riwayat pembayaran murid, serta penerbitan laporan penerimaan kas harian dan bulanan. Pengujian sistem melalui Alpha Testing terhadap tujuh skenario fungsionalitas dan Beta Testing kepada pengguna akhir membuktikan bahwa seluruh fungsi transaksi berjalan sesuai dengan kebutuhan operasional lembaga.<br><br>**Keterkaitan:** Perbedaannya, sistem MandarinPro dibangun berbasis aplikasi desktop Windows untuk satu lembaga kursus mandiri, sedangkan sistem Bimbel ARTHA Balikpapan dirancang berbasis aplikasi web terpadu untuk delapan kantor cabang, menerapkan rekonsiliasi mutasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP). | 1. Penegasan platform aplikasi berbasis Desktop Windows (baris 599:600 jurnal).<br>2. Diksi transparan dihapus karena tidak ada di teks.<br>3. Metode pengujian disesuaikan menjadi Alpha Testing dan Beta Testing. |
| **4** | **Permasalahan:** ...sehingga menyulitkan pemilik dalam memantau operasional, okupansi kamar, dan laporan pendapatan keuangan cabang secara terpusat.<br><br>**Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi manajemen multicabang berbasis web yang mengintegrasikan pemantauan operasional, reservasi antarcabang, dan konsolidasi pelaporan transaksi secara terpusat. Pengujian sistem melalui Black Box Testing membuktikan seluruh fungsi operasional berjalan valid sesuai rancangan... | **Permasalahan:** ...sehingga menyulitkan manajemen pusat dalam mengelola data cabang baru, reservasi kamar, dan pemantauan transaksi reservasi secara terpadu.<br><br>**Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi manajemen multicabang berbasis web yang memfasilitasi pendaftaran unit cabang baru, pengelolaan kamar, pencatatan reservasi tamu, pembayaran reservasi, serta pemrosesan check in pada masing-masing cabang. Pengujian fungsional menggunakan Black Box Testing pada lima skenario utama membuktikan sistem berjalan sesuai rancangan dan layak untuk dilanjutkan ke tahap penerapan. | 1. Diksi okupansi dan pendapatan keuangan dihapus karena tidak ada di jurnal.<br>2. Reservasi antarcabang dikoreksi menjadi reservasi cabang.<br>3. Skenario uji Black Box dibatasi pada lima fungsi yang benar-benar diuji di Tabel 4 jurnal. |
| **5** | **Hasil Penelitian:** ...Prototipe sistem menyediakan antarmuka untuk verifikasi transaksi pembayaran nontunai dan penerbitan bukti kuitansi otomatis. Evaluasi perancangan menunjukkan bahwa sistem ini mampu meningkatkan akurasi pembukuan dan mempermudah bendahara dalam mengontrol arus penerimaan kas secara tertib. | **Hasil Penelitian:** Penelitian ini menghasilkan rancangan prototipe antarmuka sistem informasi akuntansi penerimaan kas SPP berbasis Figma beserta pemodelan diagram UML. Rancangan sistem memodelkan menu pencatatan pembayaran SPP, visualisasi opsi kanal pembayaran nontunai, pencetakan bukti pembayaran, serta ekspor rekapitulasi pembayaran siswa ke format PDF dan Excel. | 1. Status produk diperjelas sebagai rancangan prototipe antarmuka Figma (tanpa kode program dan basis data).<br>2. Klaim evaluasi membuktikan peningkatan akurasi dihapus karena tidak ada tahap pengujian. |
| **6** | **Hasil Penelitian:** ...Sistem ini dilengkapi dengan mekanisme pembatasan hak akses untuk menjamin keamanan data transaksi keuangan. Hasil implementasi membuktikan bahwa metode rekonsiliasi kas bank efektif dalam mengeliminasi selisih pembukuan dan memperkuat pengendalian internal perusahaan.<br><br>**Metode:** Prototyping. | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi pengendalian kas bank yang menyediakan antarmuka pencatatan penerimaan kas, formulir pengeluaran kas, serta fasilitas pencatatan data rekening koran bank guna mempermudah pembuatan laporan rekonsiliasi kas bank. Sistem ini dilengkapi dengan pemisahan hak akses antara staf kasir dan pimpinan untuk menjaga tertib administrasi keuangan.<br><br>**Metode:** Research and Development (R&D) dengan pendekatan Prototyping. | 1. Klaim hasil membuktikan eliminasi selisih dihapus karena tidak ada bab pengujian empiris pada jurnal.<br>2. Metode disesuaikan dengan pernyataan jurnal (R&D dengan pendekatan SDLC Prototyping).<br>3. Lokasi Semarang dihapus karena tidak didukung data teks perusahaan. |
| **7** | **Hasil Penelitian:** ...Pengujian fungsional melalui Black Box Testing membuktikan seluruh fitur sistem berjalan valid tanpa kesalahan logika. Sistem terbukti berhasil mengeliminasi bentrokan jadwal antarmurid dan pengajar secara otomatis serta mendistribusikan notifikasi jadwal terpadu kepada orang tua siswa. | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi penjadwalan bimbingan belajar berbasis web yang menerapkan optimasi Algoritma Genetika dengan mempertimbangkan ketersediaan jam mengajar guru, preferensi waktu belajar siswa, dan pemerataan alokasi mengajar. Pengujian sistem membuktikan bahwa fungsionalitas utama sistem berjalan sesuai perancangan dan mampu meminimalkan potensi konflik jadwal mengajar guru secara terkomputerisasi. | 1. Diksi mengeliminasi diubah menjadi meminimalkan sesuai baris 40, 247, dan 271 jurnal.<br>2. Frasa bentrokan antarmurid dihapus karena konflik hanya pada jadwal guru.<br>3. Frasa tanpa kesalahan logika dihapus. |
| **8** | **Hasil Penelitian:** Penelitian ini menghasilkan sistem penjadwalan terintegrasi berbasis web yang dilengkapi mekanisme validasi otomatis terhadap kapasitas kuota ruangan, alokasi waktu sesi, serta ketersediaan pengajar untuk mencegah konflik penjadwalan. Pengujian antarmuka dan fungsionalitas membuktikan sistem berhasil meniadakan potensi benturan alokasi ruang dan waktu... | **Hasil Penelitian:** Penelitian ini menghasilkan sistem informasi penjadwalan perkuliahan terintegrasi pada sisi front-end berbasis React.js yang menyediakan antarmuka pengelolaan data master jadwal serta penyajian visual tiga model rekomendasi jadwal hasil generate backend. Pengujian fungsionalitas front-end melalui Black Box Testing membuktikan bahwa antarmuka pengguna berhasil terhubung dengan antarmuka pemrograman aplikasi (API) dan seluruh komponen fungsi berjalan valid sesuai kebutuhan pengguna. | 1. Diksi validasi otomatis kapasitas kuota ruangan dihapus karena kata kuota tidak ada di jurnal dan tidak ada atribut kapasitas kursi.<br>2. Lingkup ditegaskan pada pengembangan front-end React.js (bukan sistem utuh).<br>3. Klaim meniadakan potensi benturan jadwal ditiadakan. |
| **9** | **Permasalahan:** ...Kondisi operasional tersebut memicu keterlambatan perekaman data pengunjung dinas, keterbatasan pelaporan riwayat tamu berkala, serta belum terwujudnya integrasi rekapitulasi data kunjungan secara otomatis.<br><br>**Hasil Penelitian:** ...Aplikasi Buku Tamu Digital berbasis web yang dikembangkan melalui tujuh tahapan PxP oleh pengembang tunggal dengan integrasi pemindaian QR Code dan pelaporan dinas terpusat... Hasil tersebut membuktikan bahwa PxP sangat adaptif bagi pengembang mandiri dalam membangun aplikasi web yang responsif dan andal. | **Permasalahan:** ...Pencatatan data tamu pada Dinas Komunikasi dan Informatika Kabupaten Lombok Tengah masih menggunakan buku register fisik. Mekanisme manual tersebut menyulitkan pencarian arsip riwayat kunjungan, rentan terhadap kerusakan atau kehilangan data, serta memperbesar risiko kesalahan pencatatan data identitas tamu dinas.<br><br>**Hasil Penelitian:** ...Aplikasi Buku Tamu Digital berbasis web yang memfasilitasi pengisian data kunjungan oleh tamu melalui pemindaian tautan QR Code serta penyediaan dashboard statistik kunjungan dan ekspor laporan PDF bagi staf dinas... Pengujian performa menunjukkan waktu tanggap sistem sebesar 312 ms serta akurasi verifikasi identitas tamu sebesar 98,7%. | 1. Tiga frasa permasalahan diselaraskan dengan masalah riil buku register fisik di jurnal (baris 118:126).<br>2. Peran QR Code diperjelas sebagai tautan formulir tamu web.<br>3. Istilah verifikasi data pengunjung dispesifikkan menjadi verifikasi identitas tamu (NIK).<br>4. Klaim simpulan teoritis adaptivitas PxP dihapus. |
| **10** | **Permasalahan:** ...menghambat verifikasi kelengkapan berkas pembeli, serta memperlambat proses persetujuan akad transaksi penjualan.<br><br>**Hasil Penelitian:** ...Pengujian fungsional melalui Black Box Testing membuktikan seluruh alur transaksi berjalan sukses 100% tanpa kendala. Evaluasi penerimaan sistem melalui User Acceptance Testing (UAT) yang melibatkan 15 responden (13 pengguna, satu direktur, dan satu admin) memperoleh persentase keberhasilan 91% dengan kategori Sangat Baik. | **Permasalahan:** ...Kondisi tersebut membatasi jangkauan promosi properti, memperbesar risiko catatan transaksi penjualan tercecer, serta memperlambat proses validasi data pembelian konsumen.<br><br>**Hasil Penelitian:** ...Pengujian fungsionalitas menggunakan Black Box Testing pada fitur validasi berkas berjalan sesuai rancangan, serta evaluasi penerimaan pengguna (UAT) yang melibatkan lima belas responden memperoleh skor persentase sebesar 91% dengan kategori Sangat Baik. | 1. Kata akad dihapus karena tidak pernah muncul di teks jurnal.<br>2. Klaim Black Box sukses 100% tanpa kendala dikoreksi karena uji Black Box jurnal hanya menguji tiga skenario pada satu fitur validasi berkas (Tabel 5 jurnal) dan uji responsivitas mencatat ketidaksesuaian tampilan mobile.<br>3. Verifikasi berkas dipindahkan ke fitur solusi. |

---

## 4. Kesimpulan dan Rekomendasi Tindak Lanjut

Pemeriksaan forensik ini membuktikan secara ilmiah dan terdokumentasi bahwa koreksi yang diajukan oleh Mas Ariel pada rujukan nomor 1 (Fajriansyah dkk., 2026) sangat valid dan krusial. Penelusuran menyeluruh pada sembilan rujukan lainnya juga berhasil membersihkan potensi pertanyaan penguji seminar proposal terkait ketidaksinkronan antara klaim tabel dengan isi naskah jurnal rujukan aslinya.

Dengan telah tersusunnya dokumen audit lengkap ini, status tindakan berikutnya adalah:
1. **Menunggu Telaah dan Persetujuan Mas Ariel**: Mas Ariel dapat menelaah poin-poin temuan dan draf usulan kalimat pada Tabel 2 di atas.
2. **Persetujuan dan Eksekusi Pembaruan Berkas**: Setelah Mas Ariel menyetujui rumusan perbaikan ini, pembaruan akan dieksekusi secara presisi ke dalam berkas `c:\\Users\\ARIEL\\OneDrive - MSFT\\Documents\\ARTHA\\DRAFT PROPOSAL MD\\BAB 2\\2.2_Penelitian_Terdahulu.md` tanpa mengubah format atau struktur bab lainnya.
"""

# Check for forbidden dashes
forbidden_dashes = ['—', '–', '--']
for fd in forbidden_dashes:
    if fd in header:
        print(f"Warning: Found forbidden dash '{fd}', replacing...")
        header = header.replace(fd, ', ')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"File successfully written to {target_path}")
print(f"Total size: {len(header)} characters")

