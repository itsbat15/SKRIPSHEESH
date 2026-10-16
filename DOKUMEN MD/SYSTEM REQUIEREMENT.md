# DOKUMEN BIMBINGAN & DISKUSI TUGAS AKHIR / SKRIPSI
**(Versi Terbaru — Telah Diperbarui Berdasarkan Hasil Wawancara Mitra & Bimbingan Ke-3 Bersama Pak Arif)**

**Judul Penelitian**: Rancang Bangun Website Landing Page dan Sistem Informasi Manajemen Operasional Terintegrasi Berbasis Web Multi-User (Studi Kasus: Bimbel Artha Balikpapan)  
**Mitra Penelitian**: Bimbingan Belajar (Bimbel) Artha Balikpapan (8 Cabang Aktif)  
**Penyusun**: Mahasiswa Tugas Akhir — Institut Teknologi Kalimantan (ITK)  
**Dosen Pembimbing 1**: Pak Arif  
**Dosen Pembimbing 2**: Bu Ayu *(rekomendasi Pak Arif — konfirmasi)*  
**Tanggal Dokumen Awal**: 29 Juli 2026  
**Tanggal Pembaruan Terakhir**: 21 September 2026  

---

## 📋 Riwayat Pembaruan Dokumen

| Versi | Tanggal | Perubahan Utama |
| :--- | :--- | :--- |
| v1.0 | 29 Juli 2026 | Dokumen awal bimbingan pertama — scope 5 role, analitik geografis |
| v2.0 | 21 September 2026 | Scope direvisi menjadi 2 role berdasarkan hasil wawancara mitra & bimbingan ke-3. Judul, metode, dan detail fitur diperbarui sesuai arahan Pak Arif |

---

## 📌 1. Executive Summary

Dokumen ini merangkum perkembangan dan keputusan terakhir yang telah disepakati antara mahasiswa, mitra (Bimbel Artha Balikpapan), dan Dosen Pembimbing (Pak Arif) hingga Bimbingan Ke-3, meliputi:
1. **Permasalahan Nyata & Tervalidasi** dari hasil 3 sesi wawancara lapangan langsung dengan Bimbel Artha.
2. **Analisis Website Existing** yang sudah rentan dari sisi keamanan dan belum terintegrasi dengan manajemen internal.
3. **Scope & Arsitektur Teknologi Final** yang telah disederhanakan dan disetujui Pak Arif.
4. **Perancangan 2 Role User Final** (Admin & Super Admin) beserta detail menu dan fitur masing-masing.
5. **Metode Pengembangan: PxP (Personal Extreme Programming)** yang disetujui Pak Arif.
6. **Rencana Kerja & Tahapan Selanjutnya**.

---

## 🚨 2. Latar Belakang & Urgensi Permasalahan

Bimbingan Belajar (Bimbel) Artha adalah lembaga pendidikan non-formal terpercaya di Kota Balikpapan yang berdiri sejak **10 Oktober 1997** (±29 tahun) dengan struktur lembaga yang dipimpin oleh **Ibu Emi Ratnawati, S.E. (Ketua)** dan **Bapak Miskam Yudianto / Om Tok (Wakil Ketua / Pendiri)**. Saat ini Bimbel Artha memiliki **8 cabang operasional aktif** di Balikpapan (Artha 1 s.d. Artha 8) dengan total lebih dari **60 tentor pengajar** dan kapasitas gabungan mencapai **±2.000+ siswa aktif** di seluruh jenjang (TK, SD, SMP, dan SMA).

### 4 Permasalahan Utama yang Menjadi Rumusan Masalah TA:

#### Masalah 1 — Digitalisasi Pendaftaran (Urgensi: 🔴 KRITIS)
- Seluruh proses pendaftaran siswa baru di 8 cabang selama 29 tahun dilakukan **100% manual** menggunakan **Buku Besar A4 fisik** per cabang.
- Kolom yang dicatat di buku besar hanya: `No`, `Nama Murid`, `No. Telepon`, `Sekolah Asal`, dan `Tabel SPP 12 bulan (Juli–Juni)`. **Tidak ada kolom alamat/tempat tinggal siswa sama sekali.**
- Risiko nyata: kertas lapuk, berkas terselip, sulit mencari data siswa lama, tidak ada rekapitulasi terpusat antar 8 cabang.
- Kapasitas beberapa cabang besar (Artha 1) mencapai 400–450 siswa — menjadikan pengelolaan data manual semakin tidak skalabel.

#### Masalah 2 — Digitalisasi Pembayaran SPP (Urgensi: 🔴 KRITIS)
- Penagihan SPP dilakukan **manual oleh staf admin** dengan mengecek buku catatan satu per satu, lalu mengirimkan pesan tagihan via WhatsApp secara individual.
- Sering terjadi keterlambatan pembayaran 1–2 bulan karena wali murid lupa tanggal jatuh tempo.
- Tidak ada sistem peringatan otomatis (reminder) yang terpusat.
- Pencatatan kasir rawan salah hitung dan tidak transparan antar cabang dengan kantor pusat.
- **Tarif SPP Riil (Tervalidasi dari Wawancara Mitra)**:
  - SD: Rp 330.000 – Rp 340.000 / bulan
  - SMP: Rp 350.000 / bulan
  - SMA Kelas 10–11: Rp 380.000 / bulan
  - SMA Kelas 12: Sistem paket (misal Rp 2.250.000 lunas)
  - Biaya Modul/Buku Les: Rp 200.000 (terpisah dari SPP)
  - Diskon kakak-adik: potongan Rp 200.000 atau menjadi Rp 300.000–Rp 330.000/bulan

#### Masalah 3 — Manajemen Plotting Guru, Ruangan & Jadwal (Urgensi: 🟠 TINGGI)
- Penjadwalan guru dan pembagian kelas bersifat sangat kompleks karena setiap cabang memiliki kapasitas ruangan berbeda, dan setiap jenjang memiliki aturan kapasitas yang berbeda pula.
- **Aturan Kapasitas Kelas Riil (Tervalidasi dari Mitra)**:
  - SD Kelas 1: maks **5 siswa** per tentor (bimbingan intensif calistung)
  - SD Kelas 2: maks **6–7 siswa**
  - SD Kelas 3–6: maks **8–10 siswa**
  - SMP: maks **10–12 siswa** (ruang standar), maks **14 siswa** (ruang besar)
  - SMA: maks **12–14 siswa**
- Pernah terjadi kasus di mana satu tentor dijadwalkan di dua lokasi secara bersamaan akibat komunikasi yang tidak terstruktur (via WA grup saja).
- Manajemen tidak bisa melihat beban jam mengajar masing-masing tentor secara visual — sehingga distribusi beban mengajar tidak merata.

#### Masalah 4 — Monitoring & Validasi Hasil Revenue oleh Manajemen (Urgensi: 🟠 TINGGI)
- Rekapitulasi pendapatan 8 cabang masih dilakukan secara manual: masing-masing cabang menyerahkan laporan kertas saat rapat mingguan setiap hari Sabtu di Artha 1.
- Pimpinan pusat (Ibu Emi) tidak dapat melihat *real-time* posisi kas dan pendapatan seluruh cabang tanpa menunggu laporan fisik.
- Tidak ada sistem perbandingan performa cabang satu dengan yang lain secara visual dan historis.

---

## 🔍 3. Analisis Website Existing (bimbelartha.id)

Berdasarkan hasil *scraping* & audit yang telah dilakukan pada domain [https://bimbelartha.id/](https://bimbelartha.id/):

| Parameter | Kondisi Website Existing | Evaluasi |
| :--- | :--- | :--- |
| **CMS / Platform** | WordPress v6.7.5 + Beaver Builder | Berbasis *website builder* pihak ketiga. Tidak memiliki API dan tidak terintegrasi ke sistem manajemen internal apapun. |
| **Keamanan** | Tidak menggunakan PHP kustom, rentan *scraping* | Saat proses riset, peneliti berhasil men-*scraping* data konten website secara terbuka — keamanan sangat rendah. |
| **Form Pendaftaran** | Formulir kontak sederhana bawaan WordPress | Data yang diisi hanya masuk ke email — tidak tersimpan di database manapun. |
| **Integrasi Cabang** | Teks statis 8 alamat cabang | Tidak ada peta interaktif. Calon wali murid sulit menemukan cabang terdekat. |
| **Responsivitas Mobile** | Kurang optimal | Tampilan belum sepenuhnya adaptif di perangkat mobile. |

> **Kesimpulan**: Website existing perlu **digantikan sepenuhnya** dengan website baru berbasis Next.js yang modern, aman, dan terhubung langsung ke sistem manajemen internal.

---

## 🛠️ 4. Arsitektur Teknologi & Stack Final

Sistem dibangun menggunakan arsitektur **Decoupled (Terpisah) antara Frontend dan Backend**:

```
┌─────────────────────────────────────────────────────────┐
│  BAGIAN DEPAN (Publik): Website Landing Page             │
│  Framework: Next.js 16 + Tailwind CSS + Framer Motion    │
│  Halaman: Beranda, Profil, Program, Peta 8 Cabang, CTA  │
└─────────────────────────────┬───────────────────────────┘
                              │ Tombol "Masuk" / /admin
                              ▼
┌─────────────────────────────────────────────────────────┐
│  BAGIAN DALAM (Private): Dashboard Admin & Super Admin   │
│  Frontend Dashboard: Next.js / React + Shadcn UI         │
│  Backend API: Laravel (PHP) + Eloquent ORM               │
│  Database: MySQL / PostgreSQL                            │
│  Notifikasi: WhatsApp Gateway (Fonnte / WA-Web)          │
└─────────────────────────────────────────────────────────┘
```

**Catatan Teknis dari Pak Arif (Bimbingan Ke-3)**:
- Akses dashboard melalui route `/admin` setelah login.
- Tidak menggunakan **payment gateway pihak ketiga** (DOKU, Midtrans, dll.) — cukup tampilkan nomor rekening resmi bimbel untuk transfer manual, admin verifikasi secara manual.
- Notifikasi jatuh tempo SPP menggunakan **WhatsApp Gateway** (bukan email) karena lebih cepat dibaca oleh wali murid.

---

## 👥 5. Perancangan 2 Role User Final

Berdasarkan arahan mitra dan keputusan bersama Pak Arif di Bimbingan Ke-3, scope **ditetapkan menjadi 2 Role User** dengan pertimbangan:
- SDM staf pengajar dan admin Bimbel Artha belum siap mengadaptasi sistem yang terlalu kompleks (5 role).
- Mitra secara tegas meminta fokus pada **pendaftaran dan pengelolaan kelas** sebagai prioritas utama.
- Sistem tetap dapat dikembangkan ke lebih banyak role di masa mendatang.

### 🔄 Alur Keterhubungan Data 2 Role:

```
  [Admin Cabang]  ──── input data ────►  [Database Terpusat]
        │                                        │
        │ (Input pendaftaran, SPP,               │
        │  plotting kelas, jadwal)               ▼
        │                                [Super Admin / Owner]
        │                                  (Monitoring semua
        └──────────────────────────────►   cabang, revenue,
                                           laporan, validasi)
```

---

### 🟡 ROLE 1: ADMIN (Frontdesk / Pengelola Operasional Cabang)

**Siapa aktornya**: Staf operasional/kasir yang bertugas di meja depan setiap cabang Artha 1 s.d. Artha 8.  
**Tujuan Utama**: Menggantikan seluruh proses pencatatan manual di Buku Besar A4 dengan sistem digital yang terintegrasi.

#### 📋 Menu & Sub-menu Detail:

##### 🏠 Menu 1.1 — Dashboard Operasional Cabang
Halaman ringkasan status cabang hari ini dan bulan berjalan.
- **Kartu Statistik Cepat**:
  - Total siswa aktif di cabang ini (SD / SMP / SMA)
  - Jumlah pendaftar baru bulan ini
  - Jumlah siswa yang SPP-nya belum lunas bulan ini
  - Kapasitas kelas: berapa yang sudah penuh, berapa yang masih tersedia
- **Tabel Kelas Hari Ini**: Ringkasan jadwal les yang berjalan hari ini, ruang berapa, tentor siapa, berapa siswa hadir

---

##### 👤 Menu 1.2 — Pendaftaran Siswa Baru (Pengganti Buku Besar A4)
Form input data pendaftaran siswa baru yang datang langsung ke cabang (*walk-in*).
- **Field Data Siswa**:
  - Nama Lengkap Siswa
  - Tempat & Tanggal Lahir
  - Jenis Kelamin
  - Nama Wali Murid / Orang Tua
  - Nomor WhatsApp Aktif (wajib diisi — untuk reminder SPP)
  - Asal Sekolah (nama sekolah yang sedang diikuti)
  - Jenjang (TK / SD / SMP / SMA) & Kelas (1–12)
  - Alamat / Kelurahan Tempat Tinggal *(field baru — tidak ada di buku manual sebelumnya)*
- **Pilihan Program Les**: SD / SMP / SMA (dengan tarif yang muncul otomatis)
- **Tanggal Mulai Les**: Sistem otomatis menyesuaikan ke jadwal awal bulan atau minggu terdekat
- **Status Pembayaran Awal**: Lunas / Cicil / Belum Bayar
- **Tombol Cetak Bukti Pendaftaran (PDF)**
- **Validator Saudara Kandung**: Jika ada siswa kakak/adik yang terdaftar, diskon otomatis muncul (potongan Rp 200.000 atau tarif menjadi Rp 300.000–330.000)

---

##### 🏫 Menu 1.3 — Plotting Kelas & Penjadwalan
Mengelola pembagian siswa ke kelas dan penjadwalan tentor sesuai kapasitas ruangan.
- **Tampilan Visual Kapasitas Kelas**:
  - Setiap kelas ditampilkan sebagai kartu dengan indikator warna:
    - 🟢 Hijau: Masih tersedia (< 80% penuh)
    - 🟡 Kuning: Hampir penuh (80–99%)
    - 🔴 Merah: Penuh / Closed
- **Aturan Validator Kapasitas Otomatis (sesuai data mitra)**:
  - SD Kelas 1: Maks 5 siswa
  - SD Kelas 2: Maks 6–7 siswa
  - SD Kelas 3–6: Maks 8–10 siswa
  - SMP: Maks 10–12 siswa (ruang standar) / 14 siswa (ruang besar)
  - SMA: Maks 12–14 siswa
  - *(Sistem menolak penambahan siswa jika kuota sudah penuh)*
- **Waiting List**: Jika kelas penuh, siswa baru masuk antrian. Admin tinggal input nama & nomor WA. Sistem otomatis mengirim notifikasi WA jika ada slot yang kosong.
- **Plotting Tentor ke Kelas**: Pilih tentor yang tersedia sesuai mata pelajaran dan hari/jam yang diinginkan siswa
- **Deteksi Bentrok Jadwal Tentor**: Sistem memberikan peringatan jika tentor yang dipilih sudah terjadwal di kelas lain pada waktu yang sama

---

##### 💰 Menu 1.4 — Kasir & Manajemen SPP
Pencatatan pembayaran SPP bulanan dan biaya lainnya.
- **Form Input Pembayaran**:
  - Pilih nama siswa (autocomplete dari database)
  - Pilih bulan yang dibayarkan (bisa lebih dari 1 bulan sekaligus)
  - Nominal yang dibayarkan (otomatis terisi sesuai tarif jenjang, bisa diedit untuk diskon)
  - Metode bayar: Tunai / Transfer Bank / QRIS
  - Untuk Transfer/QRIS: Upload foto bukti transfer (konfirmasi manual oleh admin)
- **Informasi Rekening**: Sistem menampilkan nomor rekening resmi bimbel — tidak ada integrasi payment gateway otomatis
- **Cetak Kuitansi PDF**: Kuitansi otomatis ter-generate setelah pembayaran dikonfirmasi
- **Trigger WhatsApp Reminder Otomatis**:
  - H-7 jatuh tempo: WA reminder pertama ke nomor wali murid
  - H-1 jatuh tempo: WA reminder kedua (lebih mendesak)
  - H+3 keterlambatan: WA tagihan keterlambatan
  - Template pesan WA bisa dikustomisasi oleh Super Admin
- **Riwayat Pembayaran Siswa**: Tabel 12 bulan per tahun ajaran (mirip format buku besar manual, tapi digital)

---

##### 🗂️ Menu 1.5 — Master Data Siswa Cabang
Kelola database semua siswa yang terdaftar di cabang ini.
- **Tabel Data Siswa** dengan kolom: Nama, Kelas, Jenjang, Tentor, Hari/Jam Les, Status SPP Bulan Ini, Aksi
- **Filter**: Jenjang, Status SPP (Lunas / Belum Lunas / Terlambat), Kelas, Tentor
- **Fitur Ekspor**: Unduh data siswa cabang ke format Excel / CSV
- **Detail Siswa**: Klik untuk melihat riwayat lengkap pembayaran SPP, plotting kelas, dan absensi
- **Cetak Kartu Siswa / Kartu Anggota (PDF)**
- **Status Alumni**: Tandai siswa yang sudah selesai/keluar sebagai Alumni (tidak dihapus dari database)

---

##### 📊 Menu 1.6 — Laporan Harian Cabang
Ringkasan transaksi dan aktivitas di cabang untuk hari/bulan berjalan.
- Total pemasukan SPP hari ini / bulan ini
- Daftar siswa yang sudah bayar dan belum bayar bulan ini
- Rekap jumlah siswa per jenjang (SD / SMP / SMA)
- Rekap kapasitas kelas yang terisi vs tersedia
- **Cetak Laporan PDF** untuk diserahkan ke Super Admin (manajemen pusat)

---

### 🔴 ROLE 2: SUPER ADMIN (Owner / Manajemen Pusat)

**Siapa aktornya**: **Ibu Emi Ratnawati, S.E. (Ketua / Direktur)**, **Bapak Miskam Yudianto / Om Tok (Wakil Ketua / Pendiri)**, dan **Bapak Subagio, S.Sos. (Bendahara)**.  
**Tujuan Utama**: Memantau dan mengelola performa seluruh 8 cabang secara terpusat dan *real-time* tanpa harus menunggu laporan kertas mingguan.

#### 📋 Menu & Sub-menu Detail:

##### 🏆 Menu 2.1 — Executive Multi-Branch Dashboard
Halaman utama yang memberikan gambaran menyeluruh kondisi seluruh 8 cabang dalam satu layar.
- **KPI Cards (Kartu Ringkasan Eksekutif)**:
  - 👥 Total Siswa Aktif Seluruh Cabang (dengan rincian SD / SMP / SMA)
  - 💰 Total Revenue Bulan Ini (gabungan 8 cabang)
  - 🏆 Cabang dengan Pendapatan Tertinggi Bulan Ini
  - ⚠️ Jumlah Siswa dengan SPP Belum Lunas (seluruh cabang)
- **Filter Fleksibel** *(sesuai permintaan Ibu Emi di wawancara)*:
  - Filter per cabang (Artha 1 s.d. Artha 8, atau All)
  - Filter per periode (bulan & tahun)
  - Filter per jenjang (SD / SMP / SMA / All)
- **Grafik Visualisasi**:
  - **Line Chart**: Tren revenue bulanan per tahun (Jan–Des)
  - **Bar Chart**: Perbandingan jumlah siswa aktif antar 8 cabang
  - **Donut Chart**: Distribusi siswa per jenjang (SD vs SMP vs SMA)
  - **Heatmap**: Rekap pembayaran SPP semua cabang (bulan mana yang paling banyak tunggakan)

---

##### 💳 Menu 2.2 — Monitoring & Validasi Revenue 8 Cabang
Melihat detail pemasukan SPP dari setiap cabang dan memvalidasinya dengan catatan rekening bank pusat.
- **Tabel Revenue Per Cabang**: Artha 1–8, menampilkan: Target SPP bulan ini, Sudah dibayar, Belum dibayar, Selisih
- **Detail Transaksi Per Cabang**: Klik cabang tertentu untuk melihat daftar lengkap pembayaran hari per hari
- **Filter periode**: Pilih bulan dan tahun yang ingin diperiksa
- **Rekonsiliasi Rekening**: Admin pusat bisa menandai laporan cabang sebagai "Sudah Divalidasi" setelah pengecekan rekening bank
- **Ekspor Laporan**: Unduh rekap revenue seluruh cabang ke Excel/PDF untuk arsip dan evaluasi bulanan

---

##### 👨‍🏫 Menu 2.3 — Monitoring Beban Mengajar Tentor (Seluruh Cabang)
Visualisasi distribusi beban kerja seluruh tentor di 8 cabang *(fitur yang ditekankan Pak Arif di Bimbingan ke-3)*.
- **Grid/Tabel Beban Mengajar**:
  - Setiap baris: Nama Tentor
  - Setiap kolom: Cabang tempat mengajar, total jam per minggu, jumlah kelas aktif
- **Indikator Warna**:
  - 🟢 Hijau: Beban normal (1–5 kelas/minggu)
  - 🟡 Kuning: Beban sedang (6–8 kelas/minggu)
  - 🔴 Merah: Beban berlebihan (>8 kelas/minggu) — perlu redistribusi
- **Grafik Bar**: Perbandingan visual total jam mengajar antar tentor — memudahkan Super Admin melihat siapa yang paling banyak dan paling sedikit bebannya
- **Filter per Cabang**: Lihat beban tentor hanya di cabang tertentu
- **Cetak PDF Jadwal Tentor**: Cetak rangkuman jadwal tentor untuk dibagikan (tanpa perlu tentor login ke sistem)

---

##### 🏢 Menu 2.4 — Kelola Data 8 Cabang (Master Cabang)
Manajemen data master seluruh cabang Artha.
- **Tabel 8 Cabang**: Artha 1–8 dengan kolom: Nama Cabang, Alamat, No. WA Resmi, Jumlah Ruang Kelas, Kapasitas Total Siswa, Status Aktif
- **Edit Data Cabang**: Update informasi, nomor WA, atau kapasitas ruangan
- **Peta Lokasi 8 Cabang**: Tampilan Google Maps dengan marker 8 lokasi cabang (terkoneksi dengan landing page publik)

---

##### ⚙️ Menu 2.5 — Master Data & Konfigurasi Sistem
Pengaturan data utama yang digunakan di seluruh sistem.
- **Master Tarif Les**:
  - Atur tarif SPP per jenjang (SD / SMP / SMA per kelas) — bisa diubah tanpa perlu ubah kode
  - Atur biaya modul/buku
  - Atur jenis dan nominal diskon (diskon kakak-adik, dll.)
- **Master Program Belajar**: Daftar paket/program yang tersedia (Reguler, Intensif, dll.)
- **Template Pesan WhatsApp**: Kustomisasi teks pesan reminder SPP, konfirmasi pendaftaran, dan pengumuman
- **Tahun Ajaran Aktif**: Pengaturan tahun ajaran dan periode yang sedang berjalan

---

##### 👤 Menu 2.6 — Manajemen Akun Pengguna
Kelola akun login untuk seluruh Admin yang bertugas di 8 cabang.
- **Tabel Daftar Akun**: Nama, Cabang yang dikelola, Role, Status Aktif, Terakhir Login
- **Tambah Akun Admin Baru**: Ketika ada staf admin baru di salah satu cabang
- **Nonaktifkan Akun**: Ketika staf admin resign/pindah
- **Reset Password**: Bantu admin cabang yang lupa password

---

## 🔬 6. Metode Pengembangan: PxP (Personal Extreme Programming)

Metode pengembangan yang digunakan adalah **PxP (Personal Extreme Programming)**, sebuah turunan dari XP yang bersifat iteratif, adaptif, dan cocok untuk proyek dengan mitra yang kebutuhannya masih berkembang selama proses pengerjaan.

**Alasan Pemilihan PxP (disetujui Pak Arif di Bimbingan Ke-3)**:
> *"Mungkin cocok dengan melihat kondisinya. Kita belum tau ke depannya kayak apa, jadi fleksibel. Ada perubahan-perubahan, kita butuh dapat masukan mitra terus."* — Pak Arif, Bimbingan Ke-3

**Siklus Sprint PxP yang Akan Dijalani**:

```
Sprint 0 — Analisis & Perencanaan
  (Wawancara mitra, use case, ERD, prototipe UI)
        ↓
Sprint 1 — Modul Pendaftaran & Master Data Siswa
  (Form pendaftaran, database siswa, validasi kelas)
        ↓
Sprint 2 — Modul Kasir & Billing SPP
  (Pencatatan pembayaran, kuitansi PDF, WA reminder)
        ↓
Sprint 3 — Modul Plotting Kelas & Jadwal
  (Validator kapasitas, deteksi bentrok, waiting list)
        ↓
Sprint 4 — Dashboard Super Admin & Revenue
  (Multi-branch dashboard, grafik, validasi rekening)
        ↓
Sprint 5 — Pengujian & UAT
  (User Acceptance Test bersama mitra Bimbel Artha)
```

---

## 🔍 7. Analisis Website Existing (bimbelartha.id) — Tetap Relevan

*(Tidak ada perubahan dari analisis awal — tetap menjadi justifikasi mengapa website baru perlu dibangun)*

| Parameter | Kondisi Existing | Evaluasi |
| :--- | :--- | :--- |
| Platform | WordPress v6.7.5 + Beaver Builder | Tidak aman, mudah di-scraping, tidak bisa terintegrasi ke sistem internal |
| Form Pendaftaran | Formulir kontak bawaan WP | Data tidak masuk ke database manapun |
| Integrasi Cabang | Teks statis saja | Tidak ada peta interaktif lokasi 8 cabang |
| Keamanan | Sangat rentan | Peneliti berhasil men-scraping data website secara terbuka |

---

## 📅 8. Rencana Kerja & Status Saat Ini

| Tahap | Aktivitas | Status |
| :--- | :--- | :---: |
| **Tahap 1** | Wawancara Mitra (3 Sesi), Scraping & Audit Website Existing | ✅ Selesai |
| **Tahap 2** | Bimbingan 1, 2, 3 — Persetujuan Konsep, Scope, Role & Metode | ✅ Selesai |
| **Tahap 3** | **Penyusunan Bab 1 & Penetapan Judul Final** | 🔄 Saat ini |
| **Tahap 4** | Perancangan Use Case Diagram, Activity Diagram & ERD | ⬜ Berikutnya |
| **Tahap 5** | Prototipe UI/UX (Landing Page + Dashboard) → Konsultasi ke Pak Arif | ⬜ Segera |
| **Tahap 6** | Implementasi Sprint 1–4 (Next.js + Laravel + MySQL) | ⬜ |
| **Tahap 7** | Pengujian UAT Bersama Mitra Bimbel Artha | ⬜ |

---

## ❓ 9. Poin Diskusi & Keputusan yang Sudah Disepakati

| Topik | Keputusan | Disetujui Oleh |
| :--- | :--- | :--- |
| Jumlah Role User | **2 Role**: Admin & Super Admin | Pak Arif + Mitra |
| Metode Pengembangan | **PxP (Pragmatic XP)** | Pak Arif |
| Payment Gateway | **Tidak digunakan** — cukup transfer bank manual | Pak Arif |
| Notifikasi ke Wali Murid | **WhatsApp Gateway** (bukan email) | Pak Arif + Mitra |
| Landing Page | **Wajib dibangun** (gantikan WordPress lama) | Pak Arif + Mitra |
| Dashboard Tentor | Tentor **tidak perlu login** — cetak PDF jadwal saja (kecuali ada fitur input yang diperlukan) | Pak Arif |
| Penulisan Bab 1 | **Sudah boleh dimulai** | Pak Arif |
| Rekomendasi Pembimbing 2 | **Bu Ayu** (alt: Bu Gita) | Pak Arif |
