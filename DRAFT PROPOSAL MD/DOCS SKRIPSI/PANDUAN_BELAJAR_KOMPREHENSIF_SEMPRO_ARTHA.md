# Panduan Belajar Komprehensif Seminar Proposal (Sempro) Tugas Akhir

**Judul Penelitian**: Rancang Bangun Sistem Informasi Manajemen Operasional Bimbingan Belajar Berbasis Web Menggunakan Metode Personal Extreme Programming (Studi Kasus: Bimbel ARTHA Balikpapan)  
**Penyusun**: Ariel Itsbat Nurhaq (NIM 10231018)  
**Program Studi**: Sistem Informasi, Institut Teknologi Kalimantan (ITK) 2026  
**Dosen Pembimbing**: Arif Wicaksono Septyanto, M.Kom. & Sri Rahayu Natasia, S.Kom., M.Si., M.Sc.  
**Dokumen Sumber**: [Proposal Tugas Akhir_10231018.pdf](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/DRAFT%20PROPOSAL%20MD/DOCS%20SKRIPSI/PENGAJUAN%20SEMPRO/Proposal%20Tugas%20Akhir_10231018.pdf)

---

## Daftar Isi Panduan Belajar
1. **Blok 1**: Fondasi Masalah Empiris dan Urgensi Penelitian (*The Problem & Context*)
2. **Blok 2**: Ruang Lingkup dan Kendali Batasan Sistem (*The Scope Management*)
3. **Blok 3**: Metodologi Personal Extreme Programming (*The Engineering Lifecycle*)
4. **Blok 4**: Bedah Mendalam 15 Sub-subbab Kajian Teori Bab 2.1 (*Theoretical Foundations*)
5. **Blok 5**: Analisis Kesenjangan Riset 10 Penelitian Terdahulu Bab 2.2 (*Research Gap & Novelty*)
6. **Blok 6**: Rekayasa Proses Bisnis BPMN As-Is vs To-Be Bab 3.4 (*Business Process Reengineering*)
7. **Blok 7**: Arsitektur Tiga Lapis dan Isolasi Multicabang Bab 3.4.1 (*System Architecture*)
8. **Blok 8**: Pemodelan UML dan Perancangan Basis Data ERD Bab 3.4.6 & 3.4.7 (*Interaction & Data Models*)
9. **Blok 9**: Rencana Pengujian Black Box dan User Acceptance Testing (*Verification & Validation*)
10. **Blok 10**: Matriks Benang Merah Keterlacakan Hulu ke Hilir (*The Golden Thread Matrix*)

---

## Blok 1: Fondasi Masalah Empiris dan Urgensi Penelitian (*The Problem & Context*)

### 1.1 Profil Mitra dan Skala Operasional
Bimbingan Belajar (Bimbel) ARTHA Balikpapan didirikan pada tanggal 10 Oktober 1997 dan telah melayani masyarakat Kota Balikpapan selama hampir tiga dekade. Lembaga ini telah berkembang hingga memiliki delapan cabang aktif yang tersebar di Balikpapan, yang dinamai Artha 1 sampai Artha 8. Secara keseluruhan, lembaga ini menaungi sekitar 60 orang tentor pengajar dan melayani sekitar 2.400 siswa dari jenjang TK, SD, SMP, hingga SMA. 

Setiap kantor cabang beroperasi secara mandiri dengan struktur tim yang terdiri dari satu orang kepala cabang, satu orang staf administrasi, serta tentor pengajar. Meskipun memiliki skala operasional yang besar, pengelolaan administrasi dan keuangan di seluruh cabang masih dilakukan secara manual dan terisolasi tanpa adanya sistem informasi terpusat.

### 1.2 Empat Titik Masalah Kritis (*Pain Points*) di Lapangan
Berdasarkan hasil wawancara empiris bersama Pimpinan Lembaga (Ibu Emi Ratnawati, S.E.) dan Staf Administrasi Cabang (Kak Agian Isna), ditemukan empat masalah utama yang menjadi pembenaran ilmiah penelitian ini:

1. **Pencatatan Buku Besar Kertas A4 yang Terisolasi**: Pendaftaran siswa baru hanya ditulis manual pada lembaran formulir kecil lalu disalin ke buku besar berukuran A4 di masing-masing cabang. Buku tersebut hanya memuat nama, nomor telepon, asal sekolah, dan tabel riwayat SPP tanpa riwayat data akademik yang lengkap. Format fisik ini rentan hilang, rusak, dan menyulitkan penelusuran ketika terjadi pergantian staf cabang.
2. **Anomali Jam Tutup Kasir vs Jam Operasional KBM**: Staf cabang diwajibkan menutup pembukuan kas harian pada pukul 19.20 WITA, sementara kegiatan bimbingan belajar masih berlangsung hingga pukul 20.30 WITA. Kondisi ini menyebabkan transaksi yang terjadi setelah pukul 19.20 WITA tidak tercatat pada buku kas hari tersebut, sehingga memicu selisih perhitungan kas harian dan ketidaksesuaian laporan.
3. **Risiko Pengantaran Uang Fisik dan Verifikasi Transfer Lambat**: Uang tunai hasil transaksi harian dikumpulkan oleh kepala cabang untuk diantarkan langsung secara fisik ke kantor pusat pada malam hari, sementara buku besar tetap berada di cabang. Untuk pembayaran non-tunai melalui transfer bank, pemilik lembaga harus memeriksa mutasi rekening m-banking di ponsel satu per satu secara manual berdasarkan secarik kertas memo rekapan cabang.
4. **Pemeriksaan Tunggakan SPP Manual**: Tanggal jatuh tempo pembayaran SPP mengacu pada tanggal awal pendaftaran siswa. Tanpa sistem notifikasi otomatis, staf administrasi harus membuka lembaran kartu SPP siswa satu per satu secara manual untuk mencari siswa yang menunggak, sehingga penagihan sering terlambat dan arus kas lembaga terganggu.

### 1.3 Landasan Yuridis dan Teori Penguat
Penelitian ini berlandaskan pada Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional, yang mengakui pendidikan nonformal bimbingan belajar sebagai jalur pendidikan sah pelengkap sekolah formal. Pada aspek manajemen sistem, penelitian ini berpedoman pada teori Kenneth C. Laudon dan Jane P. Laudon (2020), yang menyatakan bahwa sistem informasi manajemen berfungsi mengumpulkan, memproses, menyimpan, dan mendistribusikan data transaksi operasional harian menjadi laporan manajerial terpusat guna mendukung pengambilan keputusan strategis.

---

## Blok 2: Ruang Lingkup dan Kendali Batasan Sistem (*The Scope Management*)

### 2.1 Penetapan Dua Peran Pengguna Utama
Akses operasional sistem informasi ARTHA dibatasi secara tegas pada dua peran pengguna internal lembaga, yaitu:
* **Super Admin (Pemilik Lembaga / Manajemen Pusat)**: Memiliki hak akses penuh untuk mengelola data master kantor cabang, akun staf, memvalidasi bukti transfer bank, memantau tunggakan SPP seluruh cabang, menyetujui rekonsiliasi kas harian, serta mengunduh laporan keuangan konsolidasi multicabang.
* **Staf Administrasi Cabang**: Memiliki hak akses operasional yang diisolasi khusus pada cabang tempatnya bertugas, mencakup pendaftaran siswa baru, pemilihan kelompok belajar, pencatatan pembayaran tunai, pengunggahan bukti transfer siswa cabang, pencetakan kuitansi resmi, serta penginputan rekonsiliasi fisik kasir harian cabang.

### 2.2 Justifikasi Akademis Batasan yang Dikecualikan (*Out of Scope*)
Dalam sidang Sempro, dosen penguji kerap menanyakan mengapa fitur-fitur tertentu tidak dibuat. Anda wajib menguasai alasan logis pembatasan berikut:
1. **Tidak Membangun Learning Management System (LMS) / Kelas Daring**: Fokus utama penelitian adalah efisiensi administrasi operasional dan akuntansi kas internal lembaga. Siswa dan tentor tidak diberikan akun login karena interaksi bimbingan belajar tetap dilaksanakan secara tatap muka fisik di ruang kelas.
2. **Tidak Mengintegrasikan Payment Gateway Pihak Ketiga**: Lembaga bimbingan belajar lokal memiliki sensitivitas tinggi terhadap potongan biaya transaksi per pembayaran (*transaction fee*). Selain itu, orang tua siswa terbiasa membayar tunai di meja kasir cabang atau transfer langsung ke rekening bank lembaga, sehingga verifikasi transfer semi-otomatis oleh pemilik lembaga dinilai paling realistis dan hemat biaya operasional.
3. **Pengingat WhatsApp Berbasis URL Link (Bukan API Bot Berbayar)**: Pengiriman pengingat tunggakan SPP diarahkan melalui skema tautan URL `wa.me` langsung dari sistem ke aplikasi WhatsApp staf. Strategi ini dipilih untuk menghindari biaya langganan bulanan penyedia WhatsApp Business API resmi yang memberatkan keuangan mitra UMKM bimbingan belajar.

---

## Blok 3: Metodologi Personal Extreme Programming (*The Engineering Lifecycle*)

### 3.1 Mengapa Memilih PxP Dibandingkan Metode Lain?
Metodologi Personal Extreme Programming (PxP) dipilih karena memenuhi kriteria rekayasa perangkat lunak adaptif untuk pengembang tunggal (*solo developer*) berlandaskan kajian Agarwal & Umphress (2008) serta Dzhurov, Krasteva, dan Ilieva (2009):
* **Komparasi vs Waterfall**: Waterfall menuntut kebutuhan fungsional beku sejak awal dan bersifat sekuensial kaku, sehingga tidak mampu mengakomodasi perubahan proses bisnis operasional ARTHA yang berkembang dinamis.
* **Komparasi vs Scrum**: Scrum mewajibkan pembagian peran tim formal yang banyak (Product Owner, Scrum Master, Development Team) serta rapat harian (*daily standup*) yang tidak cocok untuk pengembang mandiri.
* **Komparasi vs Extreme Programming (XP) Konvensional**: XP konvensional mewajibkan praktik pemrograman berpasangan (*pair programming*) dua orang pemrogram di satu komputer dan keterlibatan pengguna penuh di ruangan (*on-site customer*), yang mustahil dipenuhi karena peneliti bekerja sendiri dan mitra sibuk mengelola delapan cabang.
* **Komparasi vs Rapid Application Development (RAD)**: RAD menuntut komitmen waktu wawancara pengguna yang sangat tinggi pada tahap konstruksi, padahal pengelola dan staf cabang memiliki keterbatasan waktu akibat padatnya pelayanan harian.

### 3.2 Siklus Tujuh Tahapan Inti PxP
Pelaksanaan rekayasa perangkat lunak PxP pada sistem ARTHA dijalankan melalui tujuh tahapan siklus berulang:
1. **Requirements (Analisis Kebutuhan)**: Menggali masalah operasional bersama mitra dan mendefinisikannya ke dalam bentuk User Stories yang dilengkapi *acceptance criteria*.
2. **Planning (Perencanaan)**: Memetakan ketergantungan antarmodul, memberikan estimasi bobot kompleksitas Story Points, dan mengalokasikan fitur ke dalam siklus iterasi.
3. **Iteration Initialization (Inisialisasi Iterasi)**: Menyiapkan lingkungan pengembangan yang bersih, konfigurasi repositori Git dan branch, serta memilih paket User Stories prioritas tertinggi untuk dikerjakan.
4. **Design (Perancangan)**: Menerapkan prinsip Simple Design untuk memodelkan proses bisnis BPMN To-Be, Use Case Diagram, Activity Diagram, basis data ERD, serta wireframe low-fidelity.
5. **Implementation (Implementasi)**: Menerapkan siklus mikro berkelanjutan antara Unit Testing, Code, dan Refactor guna memastikan fungsi kode berjalan benar sebelum dilakukan optimasi struktur program.
6. **System Testing (Pengujian Sistem)**: Memverifikasi fungsionalitas sistem menggunakan metode Black Box Testing (Equivalence Partitioning dan Boundary Value Analysis) serta mendokumentasikan log perbaikan bug.
7. **Retrospective (Retrospeksi)**: Mengevaluasi pencapaian Story Points, membandingkan estimasi waktu pengerjaan dengan durasi kerja riil, mendemonstrasikan hasil ke mitra, serta meninjau log kesalahan sebelum melangkah ke iterasi berikutnya.

Rangkaian siklus PxP tersebut kemudian ditutup dengan dua tahapan final, yaitu **User Acceptance Testing (UAT)** bersama pemilik lembaga dan staf cabang, serta **Deployment** sistem ke lingkungan *cloud hosting* publik.

### 3.3 Target Pengerjaan Empat Siklus Iterasi ARTHA
Beban kerja pengembangan sistem dibagi ke dalam empat iterasi bertahap:
* **Iterasi 1 (Bobot 18 Story Points)**: Fokus pada modul fondasi, mencakup login autentikasi multi-cabang (US-01), manajemen pengguna dan cabang (US-02), pendaftaran siswa baru (US-03), serta pemilihan rombel dan validasi kapasitas kelas (US-04).
* **Iterasi 2 (Bobot 15 Story Points)**: Fokus pada transaksi kasir cabang, mencakup pencatatan pembayaran tunai pendaftaran dan SPP (US-05), pencetakan kuitansi PDF resmi otomatis (US-06), serta pengunggahan berkas bukti transfer bank (US-07).
* **Iterasi 3 (Bobot 18 Story Points)**: Fokus pada pengawasan dan verifikasi pusat, mencakup dashboard validasi bukti transfer pusat (US-08), kalkulasi otomatis parameter tanggal jatuh tempo SPP (US-09), serta daftar indikator tunggakan dan tautan pengingat WhatsApp (US-10).
* **Iterasi 4 (Bobot 16 Story Points)**: Fokus pada akuntansi dan pelaporan akhir, mencakup penginputan rekonsiliasi kas harian tutup kasir cabang (US-11) serta dashboard konsolidasi rekapitulasi keuangan multicabang (US-12).

---

## Blok 4: Bedah Mendalam 15 Sub-subbab Kajian Teori Bab 2.1 (*Theoretical Foundations*)

Bab 2 Subbab 2.1 memuat lima belas kajian teknologi dan metode yang menjadi fondasi ilmiah prototipe ARTHA. Berikut adalah bedah lengkap konsep kunci masing-masing sub-subbab:

### 2.1.1 Sistem Informasi Manajemen (SIM)
* **Definisi dan Tokoh**: Kenneth C. Laudon dan Jane P. Laudon (2020) mendefinisikan sistem informasi sebagai rangkaian komponen yang saling terhubung untuk mengumpulkan, mengolah, menyimpan, dan menyebarkan informasi. SIM beroperasi pada lapisan manajemen menengah guna memantau dan mengendalikan kinerja rutin organisasi.
* **Konsep Kunci**: Siklus informasi mencakup komponen *Input* (data formulir pendaftaran dan setoran uang), *Processing* (kalkulasi kuota dan pembukuan kas), *Output* (kuitansi, rekonsiliasi kas, dan laporan keuangan), serta *Feedback* (evaluasi tunggakan siswa).
* **Korelasi pada ARTHA**: SIM mengubah data transaksi kasir yang tersebar di delapan cabang fisik menjadi rekapitulasi konsolidasi terpadu di meja pemilik lembaga.

### 2.1.2 Personal Extreme Programming (PxP)
* **Definisi dan Tokoh**: Diinisiasi oleh R. Agarwal dan D. Umphress (2008) melalui konsep *Single Person Team*, lalu distandarisasi secara formal oleh Y. Dzhurov, I. Krasteva, dan S. Ilieva (2009). PxP mengawinkan fleksibilitas Extreme Programming (XP) dengan kedisiplinan pencatatan waktu dari Personal Software Process (PSP).
* **Konsep Kunci**: Penerapan tujuh tahapan terstruktur yang adaptif, pemangkasan beban dokumentasi formal yang berlebihan, serta perulangan iterasi jangka pendek.
* **Korelasi pada ARTHA**: Memfasilitasi Anda sebagai peneliti tunggal untuk membangun sistem skala menengah secara terukur dan disiplin tanpa memerlukan tim pengembang besar.

### 2.1.3 Business Process Model and Notation (BPMN)
* **Definisi dan Tokoh**: Marlon Dumas, Marcello La Rosa, Jan Mendling, dan Hajo A. Reijers (2018) menstandarisasi BPMN sebagai diagram alur kerja grafis yang menjembatani komunikasi antara analis bisnis dan pengembang perangkat lunak. Didukung penerapan perangkat lunak Bizagi Modeler oleh A. Yusmar, Y. Nurhadryani, dan I. Hermadi (2023).
* **Konsep Kunci**: Terdiri atas empat elemen pokok, yaitu *Flow Objects* (Event, Task, Gateway), *Connecting Objects* (Sequence Flow, Message Flow), *Swimlanes* (Pool sebagai batas organisasi, Lane sebagai peran tanggung jawab), dan *Data Artifacts* (Data Object, Data Store).
* **Korelasi pada ARTHA**: Digunakan untuk memetakan kondisi operasional lama (*As-Is*) berbasis dokumen kertas dan merancang alur kerja baru (*To-Be*) yang terdigitalisasi.

### 2.1.4 User Stories
* **Definisi dan Tokoh**: Mike Cohn (2004) memperkenalkan User Stories sebagai instrumen penggalian kebutuhan tangkas berbasis pendekatan *Card, Conversation, Confirmation*. Diperkuat oleh A. Febrianto, A. Wulansari, dan L. Latipah (2020).
* **Konsep Kunci**: Format baku dituliskan dalam pola: *"As a [peran pengguna], I want to [tindakan fungsi], So that [tujuan/manfaat]"*, yang wajib disertai kriteria penerimaan (*acceptance criteria*) sebagai tolok ukur pengujian fungsional.
* **Korelasi pada ARTHA**: Menjadi jembatan komunikasi praktis antara Anda dengan Ibu Emi dan staf administrasi cabang tanpa menggunakan dokumen spesifikasi formal yang kaku.

### 2.1.5 Use Case Diagram
* **Definisi dan Tokoh**: Bagian dari Unified Modeling Language (UML) yang dimutakhirkan secara kritis oleh Tri Astoto Kurniawan (2018) dalam mengevaluasi kesalahan umum pemodelan di lapangan.
* **Konsep Kunci**: Menggambarkan batasan sistem (*system boundary*), aktor pengguna, serta fungsionalitas sistem bernilai nyata bagi pengguna. Kurniawan (2018) menegaskan bahwa use case bukan dekomposisi tombol grafis (bukan fungsi klik simpan/cari), dan relasi *extend* hanya digunakan untuk alur percabangan yang bersifat opsional.
* **Korelasi pada ARTHA**: Digunakan untuk merancang 12 fungsionalitas utama sistem dengan pemisahan wewenang antara Super Admin dan Staf Cabang secara benar.

### 2.1.6 Activity Diagram
* **Definisi dan Tokoh**: Diagram UML prosedural yang menggambarkan aliran kontrol logika dari suatu aktivitas ke aktivitas lain (Sommerville, 2011; Kurniawan, 2018).
* **Konsep Kunci**: Memuat elemen *initial state*, *activity state*, *decision node*, *fork/join*, *final state*, serta kolom jalur wewenang (*swimlane*).
* **Korelasi pada ARTHA**: Digunakan untuk memodelkan tiga alur bisnis paling kritis, yaitu pendaftaran dan pembayaran kasir, verifikasi bukti transfer, serta rekonsiliasi kas harian cabang.

### 2.1.7 Entity Relationship Diagram (ERD)
* **Definisi dan Tokoh**: Diperkenalkan oleh Peter Pin-Shan Chen (1976) melalui artikel klasiknya *Toward a Unified View of Data*. Diperkuat oleh R.B. Wibagso dan N. Lia (2020) mengenai metodologi DBLC.
* **Konsep Kunci**: Notasi Chen membedakan objek entitas (persegi panjang), atribut data (elips), relasi keterhubungan (belah ketupat), serta kardinalitas relasi (1:1, 1:N, M:N). Penggunaan entitas asosiatif diperlukan untuk mengurai relasi banyak-ke-banyak menjadi dua relasi satu-ke-banyak.
* **Korelasi pada ARTHA**: Digunakan untuk merancang arsitektur konseptual basis data sepuluh entitas dengan entitas asosiatif `enrollments` dan Foreign Key `branch_id`.

### 2.1.8 Arsitektur Tiga Lapis (*Three-Tier Architecture*)
* **Definisi dan Tokoh**: M. Yusup, U. Rahardja, dan E. Prasetiyani (2010) serta Ian Sommerville (2011) mendefinisikan arsitektur tiga lapis sebagai pemisahan fisik dan fungsional sistem perangkat lunak.
* **Konsep Kunci**: Terbagi menjadi tiga tingkatan, yaitu *Presentation Tier* (lapisan antarmuka pengguna), *Application Tier* (lapisan pemrosesan logika operasional), dan *Data Storage Tier* (lapisan basis data).
* **Korelasi pada ARTHA**: Menjamin keamanan data keuangan lembaga karena antarmuka web di tablet cabang tidak dapat memanipulasi basis data secara langsung tanpa melalui validasi logika backend Laravel.

### 2.1.9 Next.js
* **Definisi dan Tokoh**: Kerangka kerja berbasis React yang dikaji penerapannya oleh Widarti dan M. Akbar (2026) untuk aplikasi web akademik terintegrasi.
* **Konsep Kunci**: Menghadirkan fitur *Server-Side Rendering* (SSR), *App Router*, dan otomatisasi pemisahan kode (*code splitting*).
* **Korelasi pada ARTHA**: Digunakan pada *Presentation Tier* agar pemuatan awal halaman kasir dan dashboard di tablet kantor cabang berlangsung cepat dan responsif.

### 2.1.10 Tailwind CSS
* **Definisi dan Tokoh**: Kerangka kerja desain web berbasis kelas utilitas yang dikaji komparasi efektivitasnya oleh M.F. Santoso (2025) terhadap Bootstrap.
* **Konsep Kunci**: Menggunakan pendekatan *utility-first* yang memungkinkan penyusunan tampilan kustom secara langsung pada berkas kode komponen. Mekanisme *purge CSS* saat proses *build* menghasilkan ukuran berkas aset antarmuka yang sangat ringkas (di bawah 50 KB).
* **Korelasi pada ARTHA**: Memberikan rancangan tata letak dashboard yang bersih, seragam, dan adaptif saat diakses dari tablet kasir maupun layar laptop kantor pusat.

### 2.1.11 Laravel
* **Definisi dan Tokoh**: Kerangka kerja backend PHP modern berpola Model-View-Controller (MVC) yang dikaji implementasi middleware multi-user oleh R. Tan (2025).
* **Konsep Kunci**: Menyediakan fitur *Eloquent ORM*, otomatisasi migrasi skema tabel, serta ekosistem autentikasi token menggunakan *Laravel Sanctum*.
* **Korelasi pada ARTHA**: Mengelola seluruh logika validasi transaksi di *Application Tier* serta menjamin isolasi hak akses data cabang (*Role-Based Access Control*).

### 2.1.12 REST API
* **Definisi dan Tokoh**: Pola arsitektur antarmuka layanan web berbasis standar HTTP yang dikaji oleh Penidas Fiodinggo Tanaem dkk. (2016) serta Haryono, P. Rosyani, dan Ardiansyah (2025).
* **Konsep Kunci**: Bersifat *stateless*, memanfaatkan metode HTTP baku (GET, POST, PUT, DELETE), serta menggunakan format *JavaScript Object Notation* (JSON) yang terstruktur dan ringan.
* **Korelasi pada ARTHA**: Menjadi jembatan pertukaran data yang aman antara aplikasi web frontend Next.js dengan server backend Laravel.

### 2.1.13 MySQL
* **Definisi dan Tokoh**: Sistem manajemen basis data relasional (RDBMS) yang dikaji kepatuhan transaksinya oleh Ilham, P. Rosyani, dan Ardiansyah (2026).
* **Konsep Kunci**: Menggunakan mesin penyimpanan *InnoDB* yang mendukung *Foreign Key constraint* dan menjamin kepatuhan prinsip ACID (*Atomicity, Consistency, Isolation, Durability*). Prinsip atomik menjamin setiap operasi penambahan mutasi kas dan pengubahan status tagihan diselesaikan secara tuntas atau dibatalkan sepenuhnya jika terjadi eror sistem.
* **Korelasi pada ARTHA**: Menjadi tempat penyimpanan data terpusat sepuluh entitas operasional ARTHA guna menjamin integritas transaksi keuangan antar delapan cabang.

### 2.1.14 Black Box Testing
* **Definisi dan Tokoh**: Metode pengujian fungsionalitas perangkat lunak dari sudut pandang eksternal tanpa melihat struktur kode internal program (Sommerville, 2011; Fadhilasari, M.P. Sari, dan Fathurrahman, 2024).
* **Konsep Kunci**: Menerapkan dua teknik utama, yaitu *Equivalence Partitioning* (membagi rentang masukan data menjadi partisi valid dan tidak valid) serta *Boundary Value Analysis* (menguji titik-titik nilai batas kritis pada form input).
* **Korelasi pada ARTHA**: Digunakan oleh peneliti pada setiap tahap *System Testing* di siklus iterasi PxP untuk menguji validasi kuota rombel dan form input nominal pembayaran.

### 2.1.15 User Acceptance Testing (UAT)
* **Definisi dan Tokoh**: Pengujian penerimaan akhir yang dilakukan langsung oleh calon pengguna sistem untuk memvalidasi kesesuaian alur kerja perangkat lunak terhadap kebutuhan operasional nyata (Sommerville, 2011; Narti Apriyanti, S.F.A. Wati, dan A.R.E. Najaf, 2024).
* **Konsep Kunci**: Instrumen pengujian menggunakan daftar periksa skenario tugas (*Test Cases Checklist*) yang dinilai menggunakan kuesioner skala Likert lima tingkat, serta disahkan melalui dokumen Berita Acara Penerimaan (*Sign-Off*).
* **Korelasi pada ARTHA**: Menjadi penentu kelayakan akhir prototipe bersama Ibu Emi (pemilik) dan perwakilan staf administrasi cabang sebelum sistem dipublikasikan ke server produksi.

---

## Blok 5: Analisis Kesenjangan Riset 10 Penelitian Terdahulu Bab 2.2 (*Research Gap & Novelty*)

Tabel 2.6 pada proposal memuat sepuluh penelitian terdahulu yang relevan. Anda wajib memahami perbedaan mendasar antara penelitian-penelitian tersebut dengan penelitian tugas akhir Anda:

```
+---------------------------------------------------------------------------------------------------+
|                            PETA KESENJANGAN RISET (RESEARCH GAP) ARTHA                            |
+---------------------------------------------------------------------------------------------------+
| Penelitian Terdahulu di Bidang Bimbel / Kursus       | Penelitian Terdahulu di Bidang Multicabang |
| (Fajriansyah 2026, Tiana 2026, Zakaria 2023,         | (Ahadi dkk. 2025, Ramadhan & Widodo 2026)  |
| Khafidhoh 2026, Barizi 2023, Safitri 2026)           |                                            |
|                                                      |                                            |
| -> FOKUS: Otomasi administrasi, jadwal, SPP, WA      | -> FOKUS: Arsitektur multicabang, RBAC,    |
| -> LIMITASI: Hanya mengelola 1 CABANG TUNGGAL        |           pencatatan kas kantor pusat      |
|                                                      | -> LIMITASI: Bidang perhotelan & retail    |
+------------------------------------------------------+--------------------------------------------+
                                          \                  /
                                           \                /
                                            v              v
+---------------------------------------------------------------------------------------------------+
|                                KONTRIBUSI KEBATUAN SISTEM ARTHA                                   |
| "Mengintegrasikan seluruh proses bisnis bimbel (pendaftaran, kuota rombel, kuitansi PDF, SPP WA)  |
|  dengan arsitektur multicabang 8 kantor cabang, isolasi data per cabang (NFR-05), verifikasi slip |
|  transfer pusat, dan rekonsiliasi kas harian terpadu menggunakan metode solo developer PxP."      |
+---------------------------------------------------------------------------------------------------+
```

### Rincian Keterkaitan 10 Penelitian Terdahulu:
1. **Fajriansyah dkk. (2026)**: Mengembangkan SIM Bimbel Bee Hive Tangerang Selatan. *Keterkaitan*: Menjadi rujukan modul integrasi pendaftaran siswa dan pembayaran SPP, namun Bee Hive hanya berupa satu cabang mandiri.
2. **Tiana & Gunanto (2026)**: Membangun sistem bimbel berbasis web mobile di Texas Kotabumi. *Keterkaitan*: Menjadi acuan modul pendaftaran dan penjadwalan, namun sistem tersebut menggunakan metode sekuensial Waterfall dan hanya satu cabang.
3. **Zakaria dkk. (2023)**: Merancang sistem pembayaran kursus Mandarin Feng Huang Bali. *Keterkaitan*: Menjadi acuan otomasi kuitansi dan eliminasi kartu pembayaran manual, namun tidak memiliki fitur multicabang.
4. **Ahadi, Pariyadi, dan Djauhari (2025)**: SIM Hotel Royal Heritage multicabang berbasis Laravel. *Keterkaitan*: Menjadi rujukan utama rancangan *Role-Based Access Control* (RBAC) pemisahan hak akses Owner pusat dan PIC Cabang.
5. **Hendri dkk. (2025)**: Sistem akuntansi penerimaan kas SPP Yayasan Semesta Khatulistiwa. *Keterkaitan*: Menjadi rujukan pemisahan pencatatan kas kasir untuk mencegah selisih pembukuan kas harian.
6. **Sudirman & Tristianti (2021)**: Sistem pengendalian kas bank rekonsiliasi pada CV. Lisa Pratama. *Keterkaitan*: Menjadi landasan perancangan alur rekonsiliasi kas fisik cabang dengan pencatatan mutasi sistem.
7. **Khafidhoh, Febrianti, dan Sujono (2026)**: Sistem penjadwalan tentor Bimbel AHE. *Keterkaitan*: Membuktikan pentingnya sistem penjadwalan terpusat untuk menghindari ketimpangan jam mengajar tentor.
8. **Yuanita, Wijayanto, dan Cahyono (2022)**: Sistem penjadwalan perkuliahan terintegrasi SIA Unsoed. *Keterkaitan*: Menjadi acuan logika pengecekan batas kapasitas ruang kelas secara digital.
9. **Musofa dkk. (2025)**: Implementasi metode PxP pada aplikasi buku tamu Diskominfo Lombok Tengah. *Keterkaitan*: Menjadi rujukan metodologis tahapan PxP dan pembagian siklus retrospeksi bagi pengembang tunggal.
10. **Apriyanti, Wati, dan Najaf (2024)**: Sistem penjualan properti dengan metode PxP. *Keterkaitan*: Menjadi acuan tata cara evaluasi kelayakan sistem berbasis User Acceptance Testing (UAT) pada proyek perangkat lunak PxP.

---

## Blok 6: Rekayasa Proses Bisnis BPMN As-Is vs To-Be Bab 3.4 (*Business Process Reengineering*)

### 6.1 Perbandingan Lima Alur Kerja Utama
Transformasi operasional dari kondisi berjalan (*As-Is*) menuju kondisi usulan (*To-Be*) dirangkum secara komparatif:

| Aktivitas Operasional | Kondisi Berjalan (As-Is / Manual) | Perancangan Usulan (To-Be / Sistem ARTHA) | Dampak Efisiensi Solusi |
| :--- | :--- | :--- | :--- |
| **1. Pendaftaran Siswa** | Formulir kertas kecil diisi orang tua, lalu staf cabang menyalin ulang secara manual ke Buku Besar A4. | Staf cabang menginput data siswa langsung ke aplikasi web ARTHA yang tersimpan ke database MySQL terpusat. | Menghilangkan duplikasi tulis dua kali, mencegah salah catat, dan arsip data aman dari kerusakan fisik. |
| **2. Pembayaran Kasir Tunai** | Staf mencatat nominal di kolom bulan Buku Besar, menulis kuitansi kertas rangkap dua, dan mencap kartu SPP. | Staf mengklik tombol konfirmasi bayar di web, mutasi kas cabang otomatis bertambah, dan kuitansi resmi PDF terbit seketika. | Mempercepat transaksi di meja kasir, kuitansi berstempel digital rapi, dan mutasi tercatat secara *real-time*. |
| **3. Pembayaran Transfer Bank** | Orang tua memperlihatkan ponsel ke staf, staf mencatat di memo kertas, pemilik mengecek mutasi m-banking di ponsel malam hari. | Staf mengunggah foto bukti transfer ke aplikasi web, pemilik lembaga memvalidasi dana masuk langsung dari dashboard pusat. | Menyediakan arsip bukti transfer digital yang valid, mencegah bukti transfer palsu, dan status tagihan lunas seketika. |
| **4. Pengawasan Jatuh Tempo SPP** | Staf memeriksa lembaran kartu SPP siswa satu per satu secara manual untuk mencari siswa yang menunggak. | Sistem menetapkan tanggal daftar sebagai parameter jatuh tempo siklus berikutnya dan memunculkan indikator warna merah serta tombol WhatsApp. | Mencegah tunggakan menumpuk tanpa disadari, penagihan lebih cepat, dan menjaga kestabilan arus kas lembaga. |
| **5. Rekonsiliasi Kas Harian** | Staf cabang membuat secarik kertas rekapan memo yang disetorkan bersama uang fisik tunai pada malam hari ke kantor pusat. | Staf menginput penghitungan fisik brankas ke form tutup kasir web, sistem mengkalkulasi selisih, dan pemilik memantau posisi kas secara terpusat. | Meniadakan risiko hilangnya kertas rekapan fisik, mempercepat rekonsiliasi kas, dan memberikan transparansi keuangan delapan cabang. |

---

## Blok 7: Arsitektur Tiga Lapis dan Isolasi Multicabang Bab 3.4.1 (*System Architecture*)

### 7.1 Pembagian Tanggung Jawab Three-Tier Architecture
Sistem ARTHA menerapkan pola arsitektur terpisah (*decoupled architecture*) yang disajikan pada Gambar 3.2:

```
+-----------------------------------------------------------------------------------+
| 1. PRESENTATION TIER (Klien Antarmuka Web)                                        |
|    - Next.js App Router, Tailwind CSS, Axios Client                              |
|    - Diakses melalui Tablet Staf di 8 Cabang & Laptop Pemilik di Kantor Pusat    |
+-----------------------------------------------------------------------------------+
                                         |
                                HTTPS Request (Token Sanctum)
                                JSON Response
                                         v
+-----------------------------------------------------------------------------------+
| 2. APPLICATION TIER (Server Logika Bisnis & Validasi API)                        |
|    - Framework Laravel RESTful API, Laravel Sanctum, Middleware RBAC             |
|    - Validasi kuota rombel, kalkulasi tagihan SPP, audit kasir, isolasi cabang    |
+-----------------------------------------------------------------------------------+
                                         |
                                SQL Queries (Prinsip ACID)
                                Result Sets Data
                                         v
+-----------------------------------------------------------------------------------+
| 3. DATA STORAGE TIER (Penyimpanan Basis Data & Berkas Digital)                   |
|    - Database MySQL InnoDB (10 Entitas Relasional)                                |
|    - File Storage Server (Direktori Berkas PDF Kuitansi & Bukti Transfer Bank)   |
+-----------------------------------------------------------------------------------+
```

### 7.2 Mekanisme Isolasi Data Cabang (Kepatuhan NFR-05)
Kebutuhan non-fungsional NFR-05 menetapkan bahwa staf satu cabang dilarang melihat atau memanipulasi data transaksi dari cabang lain:
* **Penempatan Kolom Foreign Key `branch_id`**: Seluruh tabel transaksi operasional (`users`, `students`, `study_groups`, `tuition_bills`, `payments`, `daily_reconciliations`) memiliki kolom `branch_id`.
* **Pengamanan Tingkat Kueri Backend (*Query Scope Isolation*)**: Saat staf cabang melakukan login, token Sanctum menyimpan identitas cabangnya. Setiap kueri data yang dieksekusi oleh Laravel API secara otomatis disisipi klausa `WHERE branch_id = auth()->user()->branch_id`. Hal ini memastikan isolasi data terkunci pada tingkat server database dan tidak dapat ditembus meskipun antarmuka web dimodifikasi.
* **Hak Istimewa Super Admin**: Akun pemilik lembaga memiliki nilai `branch_id = NULL`, yang memberikan wewenang lintas cabang (*global scope*) untuk mengamati rekapitulasi data dari seluruh delapan cabang.

---

## Blok 8: Pemodelan UML dan Perancangan Basis Data ERD Bab 3.4.6 & 3.4.7 (*Design Models*)

### 8.1 Pemodelan Use Case Diagram (Gambar 3.5)
Batasan sistem ARTHA melingkupi dua belas fungsionalitas utama yang dipetakan ke dalam dua aktor pengguna internal lembaga:
* **Fungsionalitas Staf Administrasi Cabang**: (1) Melakukan Login Sesuai Cabang, (2) Mendaftarkan Siswa Baru, (3) Memilih Kelompok Belajar dan Memvalidasi Kuota, (4) Mencatat Pembayaran Tunai, (5) Menerbitkan Kuitansi PDF, (6) Mengunggah Bukti Transfer, (7) Mengakses Pengingat WhatsApp Tunggakan, dan (8) Menginput Rekonsiliasi Kas Fisik Tutup Kasir.
* **Fungsionalitas Super Admin (Pemilik Lembaga)**: (1) Mengelola Akun Pengguna dan Cabang, (2) Memvalidasi Berkas Bukti Transfer Bank, (3) Memantau Rekapitulasi Tunggakan SPP Multicabang, dan (4) Mengunduh Laporan Konsolidasi Keuangan Multicabang.
* **Aturan Relasi UML**: Relasi `<<include>>` diterapkan pada use case Mendaftarkan Siswa Baru yang secara otomatis mengeksekusi use case Memilih Kelompok Belajar. Relasi `<<extend>>` diterapkan pada use case Mengunggah Bukti Transfer sebagai perluasan kondisional jika pembayaran dilakukan melalui jalur non-tunai.

### 8.2 Tiga Activity Diagram Transaksi Kritis
1. **Pendaftaran Siswa dan Pembayaran Tunai (Gambar 3.6)**: Menghubungkan jalur wewenang Staf Administrasi, Antarmuka Web Next.js, dan Server API Laravel. Aktivitas diawali dari input form, validasi kuota rombel, pencatatan mutasi kas, hingga otomatisasi pengunduhan kuitansi PDF resmi.
2. **Validasi Bukti Transfer Bank (Gambar 3.7)**: Mengatur mekanisme verifikasi dua arah antara staf cabang yang mengunggah berkas dengan pemilik lembaga di dashboard pusat yang mencocokkan mutasi rekening sebelum status transaksi disahkan menjadi lunas.
3. **Rekonsiliasi Kas Harian Antarcabang (Gambar 3.8)**: Menggambarkan penutupan kasir cabang pada malam hari, di mana staf memasukkan rincian fisik uang brankas untuk dihitung selisihnya secara otomatis terhadap catatan transaksi sistem, yang selanjutnya diverifikasi dan disetujui oleh pemilik lembaga.

### 8.3 Perancangan ERD Konseptual Notasi Chen (Gambar 3.9)
Basis data relasional ARTHA dibangun atas sepuluh entitas data yang dikelompokkan ke dalam tiga klaster fungsional utama:
1. **Klaster Master dan Hak Akses**:
   * `branches`: Menyimpan data identitas delapan kantor cabang fisik (alamat, nomor telepon, kuota operasional).
   * `users`: Menyimpan kredensial akun staf dan pemilik lengkap dengan peran (*role*) dan Foreign Key `branch_id`.
2. **Klaster Akademik dan Pendaftaran**:
   * `course_packages`: Menyimpan katalog paket bimbingan belajar, jenjang kelas, dan tarif SPP bulanan standar.
   * `students`: Menyimpan biodata lengkap siswa, kontak orang tua, dan asal sekolah.
   * `study_groups`: Menyimpan data rombongan belajar cabang, slot jadwal hari dan jam sesi, nama tentor, serta kapasitas maksimum kelas (8-15 siswa).
   * `enrollments`: **Entitas asosiatif penengah** yang menghubungkan relasi many-to-many antara siswa, rombel, dan paket belajar, serta menyimpan kolom parameter siklus jatuh tempo `due_day`.
3. **Klaster Transaksi Keuangan dan Pengendalian Mutasi**:
   * `tuition_bills`: Menyimpan tagihan iuran bulanan siswa yang diterbitkan otomatis sistem setiap bulan berdasarkan tanggal pendaftaran.
   * `payments`: Menyimpan catatan transaksi penyelesaian tagihan di meja kasir cabang (metode tunai atau transfer, tanggal bayar, nominal uang).
   * `payment_proofs`: Menyimpan direktori berkas foto bukti transfer bank, nama bank pengirim, serta status verifikasi oleh pemilik.
   * `daily_reconciliations`: Menyimpan rekapan kas tutup kasir harian cabang, total uang fisik brankas, total mutasi sistem, dan selisih kas.

---

## Blok 9: Rencana Pengujian Black Box dan User Acceptance Testing (*Verification & Validation*)

### 9.1 Pengujian Fungsional Black Box Testing (Subbab 3.3.6)
Pengujian sistem dilakukan tanpa memeriksa kode program internal, melainkan berfokus pada kebenaran fungsionalitas antarmuka melalui dua teknik terstandarisasi:
* **Equivalence Partitioning**: Membagi masukan data pengguna ke dalam kelas valid dan tidak valid. Contoh pengujian pada form pendaftaran: masukan nomor telepon berupa angka 10-13 digit diklasifikasikan sebagai partisi valid, sedangkan masukan huruf atau karakter kurang dari 10 digit ditolak dengan pesan galat yang informatif.
* **Boundary Value Analysis**: Menguji keandalan sistem pada nilai batas ekstrim. Contoh pengujian kapasitas rombel: jika daya tampung kelas ditetapkan 10 siswa, sistem diuji pada kondisi terisi 9 siswa (tombol pilih aktif), tepat 10 siswa (peringatan kuota penuh muncul), dan percobaan input siswa ke-11 (sistem secara otomatis menolak dan menonaktifkan tombol simpan).

### 9.2 Pengujian Penerimaan Pengguna / UAT (Subbab 3.3.8)
UAT dilaksanakan setelah empat siklus iterasi PxP tuntas dibangun guna memastikan prototipe disetujui oleh mitra:
* **Partisipan Pengujian**: Melibatkan Ibu Emi Ratnawati (pemilik lembaga) untuk pengujian modul manajerial pusat, serta perwakilan staf administrasi cabang untuk pengujian modul kasir dan pendaftaran.
* **Instrumen Evaluasi**: Menggunakan *UAT Test Cases Checklist* yang menguji seluruh skenario use case, dilengkapi kuesioner evaluasi kegunaan (*usability*) berbasis skala Likert lima poin (Sangat Tidak Setuju hingga Sangat Setuju).
* **Bukti Kelayakan Formal**: Pengujian diakhiri dengan penandatanganan dokumen Berita Acara Penerimaan Sistem (*Sign-Off Document*) sebagai pengesahan bahwa prototipe telah memenuhi seluruh kebutuhan operasional Bimbel ARTHA.

---

## Blok 10: Matriks Benang Merah Keterlacakan Hulu ke Hilir (*The Golden Thread Matrix*)

Tabel di bawah membuktikan keterkaitan logis naskah proposal Anda dari latar belakang masalah di Bab 1 hingga pengujian di Bab 3:

| Masalah Empiris di Lapangan (Bab 1.1) | Alur Solusi Usulan To-Be (Bab 3.4.3) | Kode Kebutuhan Sistem (Bab 3.4.4) | Cerita Pengguna User Story (Bab 3.4.5) | Diagram Perancangan UML & ERD (Bab 3.4.6 & 3.4.7) | Pengujian & Evaluasi Akhir (Bab 3.3.6 & 3.3.8) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pendaftaran formulir kertas ganda & risiko arsip hilang** | Alur To-Be Poin 1 & 2: Penginputan pendaftaran langsung ke aplikasi web terpusat. | **FR-03**: Form input siswa lengkap biodata dan pilihan program. | **US-03**: Staf menginput data siswa dari form fisik ke web. | **Gambar 3.5** (UC-02), **Gambar 3.6**, Entitas `students` & `enrollments`. | Black Box validasi kelengkapan form, UAT uji registrasi siswa baru. |
| **Bentrokan ruang kelas & kapasitas rombel tidak terpantau** | Alur To-Be Poin 1: Pengecekan sisa kuota sesi belajar secara langsung di web. | **FR-04**: Otomasi validasi kapasitas maksimum rombel kelas cabang. | **US-04**: Staf memilih kelompok belajar yang masih tersedia kuota. | **Gambar 3.5** (UC-03), Relasi `study_groups` dengan kapasitas kelas. | Boundary Value Analysis uji batas kuota 10-15 siswa, UAT alokasi kelas. |
| **Kuitansi kertas hilang & mutasi kasir tidak tercatat real-time** | Alur To-Be Poin 3: Pencatatan kasir web dengan penerbitan kuitansi PDF resmi. | **FR-05 & FR-06**: Pencatatan pembayaran dan penerbitan bukti PDF resmi. | **US-05 & US-06**: Staf mencatat uang tunai dan mengunduh kuitansi PDF. | **Gambar 3.5** (UC-04 & UC-05), Entitas `payments` & `tuition_bills`. | Black Box uji pencetakan PDF stempel digital, UAT transaksi kasir meja. |
| **Pengecekan transfer manual via m-banking pribadi di ponsel** | Alur To-Be Poin 4: Unggah berkas slip bayar dan validasi terpusat oleh pemilik. | **FR-07 & FR-08**: Pengunggahan berkas bukti transfer dan dashboard validasi pusat. | **US-07 & US-08**: Staf unggah foto transfer, Super Admin validasi dana masuk. | **Gambar 3.5** (UC-06 & UC-07), **Gambar 3.7**, Entitas `payment_proofs`. | Black Box uji unggah file JPG/PNG max 2MB, UAT konfirmasi pelunasan transfer. |
| **Kartu SPP dibuka manual & penagihan tunggakan terlambat** | Alur To-Be Poin 5: Penetapan tanggal daftar sebagai siklus jatuh tempo otomatis. | **FR-09 & FR-10**: Penguncian tanggal tempo & daftar indikator pengingat WhatsApp. | **US-09 & US-10**: Sistem terbitkan tagihan tempo & staf klik tautan WhatsApp. | **Gambar 3.5** (UC-08), Atribut `due_day` pada entitas `enrollments`. | Black Box uji tanggal jatuh tempo otomatis, UAT pengiriman pesan pengingat WA. |
| **Kertas rekapan kas malam hari rentan hilang & kasir tutup 19.20** | Alur To-Be Poin 5: Rekapitulasi mutasi kas harian otomatis dan tutup kasir web. | **FR-11 & FR-12**: Pencatatan kas harian cabang & dashboard konsolidasi pusat. | **US-11 & US-12**: Staf input kas fisik brankas, pemilik pantau grafik 8 cabang. | **Gambar 3.5** (UC-09 & UC-10), **Gambar 3.8**, Entitas `daily_reconciliations`. | Black Box uji kalkulasi otomatis selisih kas, UAT sign-off rekapitulasi pemilik. |

---

## Petunjuk Cara Belajar Menuju Sempro

1. **Kuasai Alur Cerita, Bukan Menghafal Kata**: Saat ujian, pahami bahwa seluruh modul dibangun atas dasar keluhan nyata Ibu Emi dan staf ARTHA. Jadikan masalah lapangan di Blok 1 sebagai fondasi dalam menjelaskan setiap diagram dan tabel di hadapan dosen penguji.
2. **Kaitkan Teori dengan Kasus Nyata**: Ketika ditanya mengenai teori pada Blok 4, selalu sambungkan definisi ilmiah tersebut dengan manfaat praktisnya bagi operasional bimbel ARTHA (contoh: prinsip ACID MySQL dikaitkan dengan jaminan uang SPP tidak hilang saat jaringan internet cabang terputus).
3. **Pegang Matriks Benang Merah**: Gunakan Blok 10 sebagai peta navigasi cepat. Jika dosen penguji meloncat dari pertanyaan masalah ke pertanyaan tabel basis data, Anda dapat menelusuri jalurnya secara instan dan menjawabnya dengan runtut.
