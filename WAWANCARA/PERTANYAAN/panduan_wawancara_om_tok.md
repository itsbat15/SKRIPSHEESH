# DOKUMEN PANDUAN WAWANCARA ULTRA-DETAIL & MENDALAM
**(Narasumber: Om Tok - Pemilik / Owner & Super Admin Bimbel Artha Balikpapan)**

**Mitra Penelitian**: Bimbingan Belajar (Bimbel) Artha Balikpapan (8 Cabang)  
**Penyusun**: Mahasiswa Tugas Akhir  
**Topik Skripsi**: Rancang Bangun Website Landing Page dan Sistem Informasi Dashboard Pendaftaran Berbasis Multi-User dan Analitik Geografis (Studi Kasus: Bimbel Artha Balikpapan)  
**Acuan Format**: Template Laporan Tugas Akhir ITK 2025 (`Template_Laporan_TA_2025_PROYEK_FIX.docx.pdf`)

---

## 📌 BAGIAN 1: Ringkasan Eksekutif & Presentasi Topik (Executive Brief untuk Om Tok)

*(Disampaikan di awal pertemuan sebagai pengantar resmi sebelum memasuki sesi wawancara mendalam).*

### 1. Urgensi & Latar Belakang Proyek
Bimbel Artha berdiri sejak **10 Oktober 1997 (28+ tahun)** dan telah sukses berkembang memiliki **8 cabang operasional** di Balikpapan. Namun, pendaftaran siswa dan pencatatan kasir selama puluhan tahun masih dilakukan secara **manual pada buku fisik A4** di tiap cabang. Hal ini memicu 4 risiko utama:
1. **Risiko Pelapukan & Kehilangan Data**: Berkas buku A4 bertumpuk di kantor cabang, rentan rusak, lapuk, atau terselip.
2. **Keterbatasan Pencarian & Rekapitulasi**: Om Tok sulit melihat total pendaftaran, sisa kuota kelas, atau rekap SPP 8 cabang secara *real-time*.
3. **Proses Penagihan SPP Manual**: Staf harus mengecek buku A4 satu per satu dan menghubungi WhatsApp wali murid secara manual.
4. **Data Belum Dimanfaatkan**: Data sebaran alamat rumah siswa dan sekolah asal selama ini hanya menumpuk tanpa diolah menjadi wawasan strategi bisnis (*Business Intelligence*).

### 2. Solusi 2 Sistem Utama yang Dirancang
1. **Website Landing Page Modern (Frontend Next.js)**: Media branding & promosi publik yang menampilkan profil lembaga, 8 lokasi cabang interaktif (Google Maps), daftar program belajar, galeri kegiatan, artikel tips edukasi, dan form pendaftaran online langsung terhubung ke WhatsApp official cabang.
2. **Sistem Informasi Dashboard Terpusat (Backend Laravel + PostgreSQL/MySQL)**: Menggantikan buku A4 manual dengan sistem digital terpusat berarsitektur **5 Role User**:
   * **Role 1: Super Admin / Owner (Om Tok)**: Akses penuh ke seluruh cabang, Executive Dashboard (omzet & statistik 8 cabang), Laporan Keuangan/Payroll, serta **Fitur Analitik Geografis (*Geographic Heatmap*)** untuk rekomendasi penentuan lokasi cabang baru (Artha 9/10) dan **Analitik Demografi Sekolah Asal** penyuplai murid terbanyak.
   * **Role 2: Kepala Cabang**: Monitoring target & operasional cabang.
   * **Role 3: Frontdesk / Admin Cabang**: Digitalisasi pendaftaran walk-in kasir, penagihan SPP otomatis via WhatsApp, cetak kuitansi & kartu siswa.
   * **Role 4: Tentor / Pengajar**: Jadwal mengajar & absensi/nilai siswa.
   * **Role 5: Siswa / Orang Tua**: Portal wali murid (notifikasi SPP, jadwal les, rapor nilai).

---

## 📋 BAGIAN 2: Pertanyaan Wawancara Ultra-Detail & Mendalam (Pemetaan ke Bab 1, 2, & 3 Template TA ITK 2025)

---

### 🔹 MODUL 1: SEJARAH, PROFIL, & LEGALITAS MITRA
*`[Guna Mengisi BAB 1 - Subbab 1.1 Latar Belakang, 1.6 Relevansi, & 1.8 Mitra]`*

#### 1.1 Sejarah & Milestone Perkembangan
* **1.1.1** Boleh diceritakan Om Tok, bagaimana awal mula berdirinya Bimbel Artha pada 10 Oktober 1997 di Balikpapan? Siapa pendiri utamanya dan apa latar belakang pendiriannya?
* **1.1.2** Bagaimana kronologi perkembangan penambahan cabang dari Artha 1 hingga Artha 8? (Tahun berapa cabang 1, 2, 3... dst dibuka?).
* **1.1.3** Apa pertimbangan utama Om Tok saat itu dalam memilih lokasi 8 cabang tersebut? (Apakah berdasarkan dekat sekolah tertentu, kepadatan pemukiman, atau ketersediaan ruko?).

#### 1.2 Profil, Visi-Misi, & Legalitas
* **1.2.1** Apa Visi, Misi, dan Motto resmi Bimbel Artha dalam mendidik generasi muda di Balikpapan?
* **1.2.2** Apa saja keunggulan utama / *Unique Selling Proposition (USP)* Bimbel Artha dibanding bimbingan belajar pesaing lainnya di Balikpapan?
* **1.2.3** Bagaimana status perizinan/legalitas resmi lembaga Bimbel Artha di Dinas Pendidikan Kota Balikpapan? (Untuk dicantumkan pada bagian profil mitra di Laporan TA).

#### 1.3 Struktur Organisasi & Tata Kelola
* **1.3.1** Bagaimana struktur organisasi manajemen Bimbel Artha secara keseluruhan saat ini? (Mohon gambaran pembagian tugas dari Om Tok sebagai Owner/Super Admin, Kepala Cabang, Admin Frontdesk, hingga Tentor).
* **1.3.2** Berapa total staf operasional dan total tentor/pengajar yang aktif di 8 cabang saat ini?

---

### 🔹 MODUL 2: PROSES BISNIS BERJALAN & SOP OPERASIONAL (*AS-IS PROCESS*)
*`[Guna Mengisi BAB 1 - Subbab 1.2 Rumusan Masalah, BAB 2 - Subbab 2.2 Standar Mitra, & BAB 3 - Subbab 3.2 Flowchart]`*

#### 2.1 Alur Pendaftaran Siswa (SOP Walk-in Kasir & Online)
* **2.1.1** Bagaimana alur langkah demi langkah ketika calon wali murid datang ke cabang untuk mendaftar (*Walk-in*)?
* **2.1.2** Data spesifik apa saja yang dicatat di **Buku Pendaftaran A4**?
  * *Pengecekan Detail Field*: Nama Siswa, NIK/NISN, Tempat/Tgl Lahir, Jenis Kelamin, Agama, Alamat Lengkap, Kelurahan/Kecamatan, Sekolah Asal, Kelas, Nama Ayah/Ibu, No WA Ortu, Pekerjaan Ortu, Program Les yang Dipilih, Hari/Shift Les yang Diinginkan.
  * *Pertanyaan*: Dari data tersebut, mana yang paling sering tidak diisi atau sering salah ditulis oleh wali murid?
* **2.1.3** Apakah ada syarat berkas fisik yang wajib diserahkan? (Misal: pasfoto, fotokopi rapot/KK).

#### 2.2 Aturan Pembagian Kelas & Kapasitas (*Class Plotting Rules*)
* **2.2.1** Berapa kapasitas maksimal siswa dalam 1 ruang kelas? *(Apakah ketat maksimal 10 anak/kelas?)*.
* **2.2.2** Bagaimana prosedur menentukan jadwal les siswa? (Apakah siswa bisa memilih hari Senin-Rabu-Jumat / Selasa-Kamis-Sabtu, dan shift jam berapa saja yang tersedia?).
* **2.2.3** Bagaimana alur penanganan jika suatu kelas di cabang tertentu sudah penuh (*overcapacity*)? Apakah dirujuk ke cabang Artha terdekat lainnya?

#### 2.3 Skema Biaya, SPP, & Kuitansi Pembayaran
* **2.3.1** Apa saja komponen biaya pendaftaran di Bimbel Artha?
  * *Rincian*: Biaya Pendaftaran Awal, Biaya SPP Bulanan, Biaya Modul/Buku Les, Biaya Seragam/Kaos, Biaya Try Out.
* **2.3.2** Bagaimana skema tarif SPP per jenjang saat ini? (Calistung/TK, SD Kelas 1-5, SD Kelas 6/TKA, SMP Kelas 7-8, SMP Kelas 9, SMA Kelas 10-11, SMA Kelas 12/UTBK-SNBT, Bahasa Inggris).
* **2.3.3** Apakah ada potongan harga / diskon khusus? (Misal: diskon kakak-adik, diskon bayar lunas 1 tahun, diskon anak berprestasi).
* **2.3.4** Bagaimana aturan jatuh tempo pembayaran SPP setiap bulan? (Tanggal berapa batas akhir bayar? Apakah ada denda keterlambatan?).
* **2.3.5** Metode pembayaran apa saja yang diterima saat ini? (Tunai di kasir, Transfer Bank, QRIS). Bagaimana kuitansi fisik diterbitkan?

#### 2.4 Alur Akademik, Absensi, & Penilaian Tentor
* **2.4.1** Bagaimana cara tentor mencatat kehadiran (*presensi*) siswa setiap pertemuan kelas saat ini?
* **2.4.2** Bagaimana alur pelaksanaan Try Out dan rekapitulasi nilai siswa? Berapa kali Try Out diadakan dalam satu semester?
* **2.4.3** Apakah ada lembar Laporan Perkembangan Siswa / Rapor Les bulanan yang dibagikan ke orang tua?

---

### 🔹 MODUL 3: EVALUASI PERMASALAHAN NYATA & RISIKO SISTEM MANUAL
*`[Guna Mengisi BAB 1 - Subbab 1.1 Latar Belakang, 1.2 Rumusan Masalah, & 1.5 Urgensi Proyek]`*

#### 3.1 Kendala Manajemen 8 Cabang bagi Owner (Om Tok)
* **3.1.1** Seberapa sering Om Tok keliling mengawasi 8 cabang? Masalah operasional apa yang paling sering dilaporkan oleh staf kasir/frontdesk kepada Om Tok?
* **3.1.2** Berapa lama waktu yang dibutuhkan Om Tok jika ingin mengetahui total rekapitulasi pendaftar baru atau total omzet SPP dari 8 cabang secara keseluruhan saat ini?
* **3.1.3** Apakah pernah terjadi perbedaan laporan keuangan (*selisih uang kasir*) antara catatan di buku A4 cabang dengan uang tunai yang disetorkan?

#### 3.2 Risiko Fisik & Kehilangan Data Buku A4
* **3.2.1** Di mana berkas-berkas buku A4 pendaftaran tahun-tahun sebelumnya disimpan saat ini?
* **3.2.2** Apakah pernah terjadi insiden berkas rusak (lapuk, terkena air, rayap) atau buku pendaftaran terselip sehingga data alumni/siswa lama hilang?
* **3.2.3** Seberapa sulit menemukan data siswa lama jika wali murid datang menanyakan riwayat les atau meminta bukti kuitansi ulang?

#### 3.3 Kendala Penagihan SPP & Follow-up Calon Siswa
* **3.3.1** Berapa persen estimasi wali murid yang terlambat membayar SPP setiap bulannya karena lupa tanggal jatuh tempo?
* **3.3.2** Bagaimana proses staf kasir melakukan penagihan SPP saat ini? (Apakah WA manual satu per satu? Berapa jam waktu staf terbuang untuk ini?).
* **3.3.3** Jika ada calon siswa yang bertanya via WA/Instagram tapi belum mendaftar (*leads*), bagaimana staf mengarahkan dan mem-follow up mereka saat ini?

---

### 🔹 MODUL 4: SPESIFIKASI KEBUTUHAN SISTEM BARU & HAK AKSES (*TO-BE SYSTEM & PERMISSIONS*)
*`[Guna Mengisi BAB 1 - Subbab 1.3 Tujuan & 1.4 Batasan, serta BAB 3 - Subbab 3.4 Desain System]`*

#### 4.1 Ekspektasi Utama Om Tok sebagai Super Admin
* **4.1.1** Apa 3 target indikator keberhasilan paling utama yang Om Tok harapkan setelah sistem baru (Landing Page + Dashboard) ini resmi dipakai?
* **4.1.2** Tampilan ringkasan (*Executive Dashboard*) seperti apa yang Om Tok ingin lihat pertama kali saat login sebagai Super Admin? (Misal: Grafik Total Siswa Aktif 8 Cabang, Ranking Cabang Terlaris, Total Omzet SPP Bulan Ini, Notifikasi SPP Menunggak).

#### 4.2 Matriks Hak Akses 5 User Role (*Authorization Rules*)
Mohon konfirmasi Om Tok mengenai batasan kewenangan masing-masing role:

1. **Role Super Admin / Owner (Om Tok)**:
   * [ ] Akses penuh seluruh data 8 cabang.
   * [ ] Hak tambah/hapus/edit akun staf kasir & tentor.
   * [ ] Hak approval pengeluaran dana operasional cabang.
   * [ ] Akses laporan keuangan Laba/Rugi & ekspor Excel/PDF.

2. **Role Kepala Cabang / Branch Manager**:
   * [ ] Hanya bisa melihat data di cabangnya sendiri.
   * [ ] Hak memantau target pendaftaran & kinerja tentor cabang.
   * [ ] Hak pengajuan anggaran pengeluaran cabang ke Om Tok.

3. **Role Frontdesk / Admin Kasir Cabang**:
   * [ ] Hak menginput pendaftaran siswa baru *walk-in*.
   * [ ] Hak menginput pembayaran SPP & mencetak kuitansi digital.
   * [ ] *Pertanyaan*: Bolehkah staf kasir menghapus (*delete*) data siswa jika ada kesalahan input, atau harus minta izin Om Tok?
   * [ ] *Pertanyaan*: Bolehkah staf kasir memberikan diskon bayar sendiri tanpa approval Om Tok?

4. **Role Tentor / Pengajar**:
   * [ ] Hanya bisa melihat jadwal mengajar diri sendiri & list siswa di kelasnya.
   * [ ] Hak mengisi absensi kehadiran siswa & input nilai Try Out.
   * [ ] *Pertanyaan*: Bolehkah tentor melihat nomor HP/WA orang tua siswa, atau hanya nama siswa saja?

5. **Role Siswa / Orang Tua (Portal Wali Murid)**:
   * [ ] Melihat jadwal les & pengumuman bimbel.
   * [ ] Melihat rekap absensi & Rapor Hasil Try Out anak.
   * [ ] Melihat rincian tagihan SPP & mendownload bukti kuitansi digital.

#### 4.3 Integrasi WhatsApp Gateway & Notifikasi Otomatis
* **4.3.1** Apakah Om Tok setuju jika sistem dilengkapi fitur **WhatsApp Gateway Automatic Engine**?
* **4.3.2** Notifikasi WA otomatis apa saja yang ingin diaktifkan?
  * [ ] WA Pesan Selamat Datang & Bukti Pendaftaran Sukses ke Wali Murid.
  * [ ] WA Notifikasi Kuitansi Pembayaran SPP Digital setelah bayar di kasir.
  * [ ] WA Pengingat H-3 dan H-1 Jatuh Tempo SPP Bulanan secara otomatis.
  * [ ] WA Broadcast Pengumuman Libur / Jadwal Try Out Massal ke seluruh wali murid.

---

### 🔹 MODUL 5: VISI PENGEMBANGAN BISNIS & ANALITIK DATA (*BUSINESS INTELLIGENCE / BI*)
*`[Guna Mengisi BAB 1 - Subbab 1.5 Urgensi & 1.6 Relevansi Industri, serta BAB 3 - Subbab 3.4 Desain Inovasi]`*

#### 5.1 Fitur Inovasi 1: Pemetaan Geografis Potensi Cabang Baru (*Geographic Heatmap*)
* **5.1.1** Jika di masa depan Bimbel Artha ingin membuka cabang ke-9 atau ke-10, wilayah/kecamatan mana di Balikpapan yang menurut Om Tok paling potensial namun belum terjangkau 8 cabang saat ini?
* **5.1.2** Apakah Om Tok setuju jika sistem baru dilengkapi peta interaktif (*Heatmap*) yang memetakan titik koordinat rumah seluruh siswa Artha di Balikpapan?
* **5.1.3** Bagaimana peta ini membantu Om Tok dalam mengambil keputusan pembukaan cabang baru atau rute jemputan siswa di masa depan?

#### 5.2 Fitur Inovasi 2: Analisis Demografi Sekolah Asal (*School Origin Analytics*)
* **5.2.1** Sekolah (SD, SMP, SMA di Balikpapan) mana saja yang selama ini menjadi penyuplai murid terbanyak ke Bimbel Artha?
* **5.2.2** Apakah selama ini Bimbel Artha mengadakan program promosi khusus ke sekolah-sekolah tertentu (misal: *School-to-School Roadshow*, pembagian brosur di gerbang sekolah, sponsorship event sekolah)?
* **5.2.3** Apakah Om Tok membutuhkan grafik peringkat 10 sekolah penyuplai murid terbanyak di dashboard Super Admin untuk menentukan sasaran promosi sekolah setiap ajaran baru?

---

## 📌 BAGIAN 3: Checklist Berkas & Dokumen Fisik yang Harus Diminta

Sebelum mengakhiri sesi wawancara dengan Om Tok, pastikan Anda meminta/mengambil foto berkas pendukung berikut untuk lampiran Laporan TA:

1. [ ] **Buku Pendaftaran A4 Fisik**: Foto 1-2 lembar isi buku pendaftaran fisik cabang (blur/samarkan nama jika rahasia).
2. [ ] **Kuitansi SPP Fisik**: Foto lembaran kuitansi kertas pembayaran kasir saat ini.
3. [ ] **Struktur Tarif Biaya Resmi**: Lembaran/brosur rincian biaya pendaftaran & SPP per program saat ini.
4. [ ] **Daftar Kontak & Alamat 8 Cabang**: Alamat presisi, titik lokasi Google Maps, dan No WA Official Artha 1 s/d 8.
5. [ ] **Logo Resmi Bimbel Artha**: File digital logo resolusi tinggi (PNG/Vector) untuk branding website & header laporan kuitansi.
