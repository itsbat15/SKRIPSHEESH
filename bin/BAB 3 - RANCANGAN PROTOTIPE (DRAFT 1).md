BAB 3
RANCANGAN PROTOTIPE

Bab ini memaparkan rancangan prototipe sistem informasi manajemen operasional berbasis web yang dikembangkan untuk Bimbingan Belajar Artha Balikpapan. Pemaparan mencakup garis besar prototipe beserta justifikasi pemilihan metode pengembangan, tahapan siklus hidup Personal Extreme Programming (PxP) yang diterapkan, prosedur teknis dari setiap tahapan pengembangan, konsep kebutuhan fungsional dan nonfungsional sistem, spesifikasi teknis lingkungan komputasi yang digunakan, serta jadwal pelaksanaan pembuatan prototipe secara keseluruhan.

3.1 Garis Besar Prototipe

Bimbingan Belajar Artha Balikpapan merupakan lembaga pendidikan nonformal yang saat ini mengelola delapan cabang aktif di Kota Balikpapan, Kalimantan Timur. Berdasarkan hasil observasi dan wawancara yang dilakukan kepada pengelola, seluruh proses operasional harian seperti pendaftaran siswa baru, pencatatan pembayaran SPP, pembuatan kuitansi, dan penjadwalan tentor masih dilaksanakan secara manual menggunakan buku besar kertas A4 dan arsip fisik. Kondisi tersebut menyebabkan terjadinya duplikasi data antarcabang, keterlambatan pelaporan ke pusat, serta ketidakmampuan pimpinan untuk memantau kondisi operasional seluruh cabang secara bersamaan dan tepat waktu (Pradana, 2024).

Prototipe yang dikembangkan dalam tugas akhir ini adalah sebuah sistem informasi manajemen operasional berbasis web multipengguna yang dirancang untuk menjawab permasalahan tersebut secara menyeluruh. Sistem ini memiliki dua peran pengguna utama, yaitu Admin Cabang yang bertugas mengelola data operasional di tingkat cabang masing-masing, dan Super Admin yang memiliki kewenangan memantau seluruh cabang sekaligus melalui satu dasbor terpusat. Modul utama yang dirancang mencakup: registrasi siswa baru, pencatatan dan kuitansi digital SPP, penjadwalan tentor dengan mekanisme pencegahan bentrok jadwal dan pembatasan kuota ruang, notifikasi WhatsApp otomatis kepada wali murid, serta dasbor rekonsiliasi kas multicabang untuk pimpinan (Fajriansyah dkk., 2026; Ahadi dkk., 2025).

Prototipe ini dirancang untuk mencapai Tingkat Kesiapan Teknologi (TKT) Level 5, yaitu teknologi telah diuji dan divalidasi secara fungsional pada lingkungan nyata bersama mitra, sesuai dengan ketentuan jalur tugas akhir bentuk Prototipe Program Studi Sistem Informasi ITK (Panduan TA dan SITASI Sistem Informasi ITK, 2026). Metode pengembangan yang dipilih adalah Personal Extreme Programming (PxP), yaitu adaptasi dari kerangka kerja Extreme Programming (XP) yang secara khusus dirancang untuk pengembang mandiri (autonomous developer) (Dzhurov dkk., 2009). Pemilihan PxP dilandasi oleh tiga pertimbangan utama. Pertama, pengembangan tugas akhir ini dilaksanakan oleh satu orang pengembang sehingga metode berbasis tim seperti Scrum tidak sesuai konteksnya. Kedua, PxP terbukti diterapkan secara berhasil pada berbagai proyek sistem informasi berbasis web di Indonesia oleh pengembang tunggal (Fikri & Arthawan, 2020; Sidiq dkk., 2025; Apriyanti dkk., 2024). Ketiga, siklus iteratif PxP memungkinkan penyesuaian berkelanjutan terhadap kebutuhan mitra yang dapat berubah selama proses pengembangan berlangsung (Fahrijal & Hartawan, 2024). Luaran tugas akhir ini akan disiapkan pula sebagai bahan permohonan Hak Kekayaan Intelektual berupa Hak Cipta perangkat lunak kepada Direktorat Jenderal Kekayaan Intelektual.

3.2 Tahapan Pembuatan Prototipe

Pengembangan prototipe sistem informasi manajemen operasional Bimbel Artha Balikpapan dilaksanakan menggunakan siklus hidup Personal Extreme Programming (PxP) yang terdiri dari tujuh tahapan iteratif. PxP merupakan proses pengembangan perangkat lunak yang dirancang khusus untuk pengembang yang bekerja secara mandiri, dengan memadukan praktik-praktik terbaik dari Personal Software Process (PSP) dan Extreme Programming (XP) secara ringan dan dapat diterapkan tanpa birokrasi yang berlebihan (Dzhurov dkk., 2009). Penerapan PxP dalam konteks pengembangan sistem informasi di Indonesia telah dibuktikan mampu menghasilkan perangkat lunak berkualitas dalam durasi yang efisien, sebagaimana dilaporkan oleh Fikri & Arthawan (2020) pada proyek SI Buku Tamu Balikpapan, Priatmaja dkk. (2022) pada proyek SI Laboratorium Informatika dan Komputer, serta Sidiq dkk. (2025) pada proyek SI Surat Menyurat.

Siklus hidup PxP bersifat iteratif dan berulang. Apabila pada tahap Retrospektif ditemukan temuan yang memerlukan perbaikan substantif atau terdapat kebutuhan baru dari mitra, maka proses pengembangan kembali ke tahap Inisialisasi Iterasi untuk memulai iterasi berikutnya. Satu proyek pengembangan PxP dapat terdiri dari beberapa siklus iterasi hingga seluruh kebutuhan fungsional terpenuhi dan mitra menyatakan penerimaan terhadap sistem (Dzhurov dkk., 2009; Apriyanti dkk., 2024). Gambar 3.1 menyajikan diagram alir tahapan pembuatan prototipe yang menggambarkan hubungan, urutan, dan jalur perulangan antartahapan PxP tersebut. Tujuh tahapan dalam siklus PxP yang diterapkan pada pengembangan prototipe ini adalah sebagai berikut.

1. Kebutuhan (Requirements)
2. Perencanaan (Planning)
3. Inisialisasi Iterasi (Iteration Initialization)
4. Perancangan (Design)
5. Implementasi (Implementation)
6. Pengujian Sistem (System Testing)
7. Retrospektif (Retrospective)

[Gambar 3.1 Diagram Alir Tahapan Pembuatan Prototipe Menggunakan Metode PxP]
Catatan mahasiswa: Buat flowchart 7 tahapan PxP berurutan (kotak persegi panjang) dihubungkan anak panah ke bawah, ditambah anak panah umpan balik dari kotak "Retrospektif" kembali ke kotak "Inisialisasi Iterasi" dengan label "Iterasi Berikutnya". Gunakan draw.io atau Figma.

3.3 Prosedur

Subbab ini menjabarkan prosedur teknis dari setiap tahapan siklus hidup PxP yang dilaksanakan dalam pengembangan prototipe. Setiap prosedur diuraikan secara berurutan sesuai dengan alur yang digambarkan pada Gambar 3.1.

3.3.1 Prosedur Analisis Kebutuhan

Tahap analisis kebutuhan merupakan titik awal pengembangan prototipe yang bertujuan mengidentifikasi seluruh kebutuhan fungsional dan nonfungsional sistem secara komprehensif. Pressman & Maxim (2015) mendefinisikan analisis kebutuhan sebagai proses menemukan, mendokumentasikan, dan memvalidasi layanan serta batasan yang harus dipenuhi oleh suatu sistem perangkat lunak. Sommerville (2011) menambahkan bahwa kualitas analisis kebutuhan menentukan arah seluruh siklus pengembangan, sehingga kesalahan pada tahap ini berpotensi menimbulkan biaya perbaikan yang jauh lebih tinggi di tahap implementasi.

Pengumpulan kebutuhan pada penelitian ini dilaksanakan melalui tiga teknik yang saling melengkapi. Pertama, observasi langsung dilakukan di kantor cabang Bimbel Artha Balikpapan guna mengamati alur kerja operasional harian yang sesungguhnya, termasuk cara pencatatan buku besar, proses pembuatan kuitansi manual, dan mekanisme koordinasi antarcabang yang berjalan saat ini. Kedua, wawancara mendalam dilaksanakan bersama dua narasumber utama, sebagaimana dicantumkan pada Tabel 3.1. Ketiga, studi dokumentasi dilakukan terhadap buku besar kertas A4, arsip kuitansi fisik, dan formulir pendaftaran yang selama ini digunakan oleh mitra (Fajriansyah dkk., 2026; Kismantoro & Ibadi, 2026). Temuan dari seluruh teknik pengumpulan data tersebut kemudian diformulasikan menjadi daftar user stories yang menjadi dasar perancangan kebutuhan fungsional sistem pada subbab 3.4.1.

Tabel 3.1 Profil Narasumber Penelitian

| No. | Nama | Jabatan | Peran dalam Sistem |
|:---:|:-----|:--------|:-------------------|
| 1 | Ibu Emi Ratnawati, S.E. | Pimpinan / Ketua Bimbel Artha | Super Admin |
| 2 | Kak Agian Isna | Staf Administrasi / Kasir | Admin Cabang |

3.3.2 Prosedur Perencanaan

Tahap perencanaan bertujuan memetakan seluruh kebutuhan fungsional yang telah diidentifikasi ke dalam rencana kerja yang terstruktur dan realistis. Dalam kerangka kerja PxP, perencanaan dilakukan melalui mekanisme permainan perencanaan (planning game) yang menghasilkan daftar user stories berbobot (story points) dan disusun ke dalam daftar prioritas fitur (product backlog) berdasarkan urutan kepentingan fungsional (Beck, 2004). Setiap user story dalam product backlog kemudian dikelompokkan ke dalam tiga siklus iterasi rilis, mengadaptasi pola yang diterapkan oleh Sidiq dkk. (2025) dan Fikri & Arthawan (2020) dalam proyek PxP mereka.

Tabel 3.2 menyajikan pemetaan modul sistem ke dalam tiga siklus iterasi yang direncanakan beserta estimasi durasi penyelesaian setiap modul. Estimasi durasi bersifat tentatif dan dapat disesuaikan berdasarkan temuan pada tahap retrospektif setiap iterasi. Fleksibilitas penyesuaian jadwal ini merupakan salah satu kelebihan utama PxP dibandingkan metode pengembangan berurutan seperti Waterfall, di mana penyesuaian dapat dilakukan tanpa mengorbankan konsistensi keseluruhan proyek (Fahrijal & Hartawan, 2024).

Tabel 3.2 Pemetaan Modul ke Siklus Iterasi PxP

| Iterasi | Modul yang Dikembangkan | Estimasi Durasi |
|:-------:|:------------------------|:---------------:|
| Iterasi I | Fondasi basis data terpusat, manajemen akun pengguna, modul registrasi siswa baru, pencatatan pembayaran SPP, kuitansi digital | 3 minggu |
| Iterasi II | Modul penjadwalan tentor, pencegahan bentrok jadwal, pembatasan kuota ruang kelas, notifikasi tautan WhatsApp kepada wali murid | 3 minggu |
| Iterasi III | Dasbor Super Admin rekapitulasi kas multicabang, laporan keuangan antarcabang, pengujian penerimaan pengguna (UAT) menyeluruh | 3 minggu |

3.3.3 Prosedur Inisialisasi Iterasi

Inisialisasi iterasi menandai dimulainya setiap siklus pengembangan baru dalam kerangka kerja PxP. Pada tahap ini, pengembang memilih sejumlah user story dari product backlog yang akan menjadi fokus iterasi berjalan, berdasarkan urutan prioritas yang telah ditetapkan pada tahap perencanaan (Dzhurov dkk., 2009). Pemilihan dilakukan dengan mempertimbangkan ketergantungan antara modul (module dependency) sehingga modul fondasi dikerjakan lebih dahulu sebelum modul yang bergantung padanya. Sebagai contoh, fondasi basis data dan modul autentikasi pengguna harus selesai pada Iterasi I sebelum modul penjadwalan dan notifikasi pada Iterasi II dapat dibangun.

Selain penetapan lingkup iterasi, tahap inisialisasi juga mencakup persiapan lingkungan pengembangan secara teknis, meliputi pembaruan repositori kode ke kondisi terkini, inisialisasi struktur skema basis data untuk modul yang akan dikerjakan, konfigurasi lingkungan peladen lokal, serta penetapan kriteria selesai (definition of done) yang harus dipenuhi oleh setiap modul sebelum iterasi dinyatakan berhasil (Sidiq dkk., 2025). Kriteria selesai tersebut menjadi acuan objektif pada saat pengujian sistem dan retrospektif di akhir iterasi.

3.3.4 Prosedur Perancangan

Tahap perancangan bertujuan menghasilkan seperangkat artefak desain yang menjadi cetak biru implementasi sistem. Pressman & Maxim (2015) mendefinisikan perancangan perangkat lunak sebagai proses translasi kebutuhan menjadi representasi yang dapat dievaluasi kualitasnya sebelum implementasi dimulai. Beck (2004) menegaskan bahwa dalam kerangka XP dan PxP, perancangan harus tetap sesederhana mungkin sesuai kebutuhan iterasi berjalan (simple design) sambil mempertahankan kemampuan untuk berkembang seiring iterasi berikutnya (evolving design).

Perancangan pada proyek ini mencakup tiga lapisan artefak. Pertama, pemodelan perilaku sistem menggunakan diagram UML, meliputi Use Case Diagram untuk menggambarkan cakupan fungsi sistem dari perspektif setiap aktor pengguna, Activity Diagram untuk memodelkan alur kerja proses bisnis utama, dan Sequence Diagram untuk menggambarkan interaksi antarkomponen sistem dalam menyelesaikan setiap skenario penggunaan (Sommerville, 2011; Fajriansyah dkk., 2026). Gambar 3.2 menyajikan Use Case Diagram, Gambar 3.3 menyajikan Activity Diagram proses pencatatan SPP, dan Gambar 3.4 menyajikan Sequence Diagram alur login sistem.

[Gambar 3.2 Use Case Diagram Sistem Informasi Manajemen Bimbel Artha Balikpapan]
[Gambar 3.3 Activity Diagram Proses Pencatatan SPP dan Penerbitan Kuitansi Digital]
[Gambar 3.4 Sequence Diagram Alur Autentikasi dan Verifikasi Peran Pengguna]

Kedua, pemodelan struktur basis data dilakukan menggunakan Entity Relationship Diagram (ERD) untuk menggambarkan entitas dan hubungan logis antartabel, dilanjutkan dengan Physical Data Model (PDM) yang merepresentasikan implementasi fisik skema basis data MySQL (Ahadi dkk., 2025). Gambar 3.5 menyajikan ERD dan Gambar 3.6 menyajikan PDM sistem.

[Gambar 3.5 Entity Relationship Diagram (ERD) Basis Data Sistem]
[Gambar 3.6 Physical Data Model (PDM) Basis Data MySQL Sistem]

Ketiga, perancangan antarmuka pengguna dilaksanakan menggunakan perangkat Figma, dimulai dari kerangka antarmuka berkemampuan rendah (wireframe) hingga prototipe antarmuka beresolusi tinggi yang mencerminkan tampilan nyata sistem (Thiovanda, 2026; Karpina dkk., 2025). Gambar 3.7 menyajikan prototipe antarmuka beberapa halaman utama sistem hasil perancangan.

[Gambar 3.7 Prototipe Antarmuka Tinggi (High-Fidelity Mockup) Halaman-Halaman Utama Sistem]

Catatan mahasiswa: Gambar 3.2 hingga 3.7 merupakan placeholder. Buat diagram UML menggunakan draw.io atau StarUML, ERD dan PDM menggunakan MySQL Workbench atau dbdiagram.io, dan mockup menggunakan Figma. Setiap gambar wajib diberi nomor dan judul di bawahnya sesuai format ITK.

3.3.5 Prosedur Implementasi

Tahap implementasi adalah tahap di mana seluruh rancangan yang telah dihasilkan pada tahap perancangan diwujudkan menjadi kode program yang berfungsi. Pengembangan menggunakan arsitektur Model-View-Controller (MVC) yang memisahkan logika bisnis, antarmuka pengguna, dan pengelolaan basis data ke dalam lapisan yang independen satu sama lain, sehingga memudahkan pemeliharaan dan pengembangan di masa mendatang (Karpina dkk., 2025). Bahasa pemrograman yang digunakan adalah PHP untuk logika sisi peladen, HTML dan CSS untuk struktur dan tampilan antarmuka, serta JavaScript untuk interaktivitas sisi klien. Sistem manajemen basis data yang digunakan adalah MySQL.

Selama tahap implementasi, salah satu praktik utama PxP yang diterapkan adalah refaktorisasi kode secara berkesinambungan (continuous refactoring). Refaktorisasi dilakukan setelah setiap modul selesai dikodekan guna memastikan kode tetap bersih, mudah dibaca, dan bebas dari redundansi logika (Beck, 2004). Praktik ini terbukti efektif dalam menjaga kualitas kode jangka panjang pada proyek yang dikerjakan oleh pengembang tunggal. Implementasi fitur notifikasi WhatsApp dilakukan menggunakan mekanisme tautan WhatsApp yang dapat diklik dari antarmuka sistem tanpa memerlukan layanan pihak ketiga berbayar, mengadaptasi pendekatan yang digunakan oleh Safitri dkk. (2026) dan Sari dkk. (2023).

3.3.6 Prosedur Pengujian Sistem

Pengujian sistem dilaksanakan menggunakan metode Black Box Testing, yaitu metode pengujian perangkat lunak yang mengevaluasi kesesuaian keluaran sistem terhadap masukan tertentu tanpa memperhatikan struktur internal kode program (Pressman & Maxim, 2015). Sommerville (2011) menjelaskan bahwa Black Box Testing berorientasi pada perspektif pengguna, sehingga sangat tepat digunakan untuk memvalidasi kebutuhan fungsional yang telah didefinisikan pada tahap analisis kebutuhan.

Teknik pengujian yang diterapkan adalah Equivalence Partitioning dan Boundary Value Analysis. Equivalence Partitioning membagi domain masukan ke dalam kelas-kelas ekuivalen sehingga setiap kelas cukup diuji dengan satu kasus uji yang representatif. Boundary Value Analysis secara khusus menguji nilai-nilai di batas setiap kelas, di mana galat paling sering muncul (Pressman & Maxim, 2015). Pendekatan pengujian ini telah diterapkan secara konsisten pada proyek-proyek SI berbasis PxP di Indonesia (Sidiq dkk., 2025; Apriyanti dkk., 2024; Tiana & Gunanto, 2026). Kriteria kelulusan pengujian fungsional yang ditetapkan adalah: seluruh butir skenario pengujian pada setiap modul utama mencapai 100% hasil "Valid/Berhasil" tanpa ditemukan galat kritis yang menghentikan alur operasional utama. Tabel 3.3 menyajikan contoh format skenario pengujian Black Box Testing yang digunakan untuk mendokumentasikan hasil pengujian setiap modul.

Tabel 3.3 Contoh Format Skenario Pengujian Black Box Testing per Modul

| No. | Skenario Uji | Data Masukan | Hasil yang Diharapkan | Hasil Aktual | Status |
|:---:|:-------------|:-------------|:----------------------|:-------------|:------:|
| 1 | Login dengan kredensial valid | Email dan kata sandi terdaftar | Berhasil masuk dan diarahkan ke halaman dasbor sesuai peran | — | — |
| 2 | Login dengan kata sandi salah | Email benar, kata sandi keliru | Muncul pesan galat "Kata sandi tidak sesuai" | — | — |
| 3 | Tambah data siswa baru dengan data lengkap | Semua kolom terisi dan valid | Data tersimpan dan muncul di daftar siswa | — | — |
| 4 | Tambah data siswa — kolom nama dikosongkan | Nama dikosongkan | Muncul pesan validasi "Nama wajib diisi" | — | — |
| 5 | Pencatatan SPP dengan nominal valid | Nominal angka positif | Transaksi tersimpan dan kuitansi dapat dicetak | — | — |
| ... | ... | ... | ... | — | — |

Catatan mahasiswa: Kolom "Hasil Aktual" dan "Status" diisi setelah pengujian dilaksanakan di BAB 4. Tambahkan baris untuk setiap skenario pengujian dari seluruh modul yang dikembangkan.

3.3.7 Prosedur Retrospektif

Tahap retrospektif merupakan tahap evaluasi akhir dari setiap siklus iterasi PxP, sekaligus menjadi pintu keputusan apakah pengembangan dinyatakan selesai atau perlu dilanjutkan ke iterasi berikutnya. Pada tahap ini, dilaksanakan dua kegiatan utama secara berurutan. Kegiatan pertama adalah evaluasi internal oleh pengembang, meliputi pencatatan temuan selama iterasi berlangsung, identifikasi hambatan teknis yang ditemui, dan penetapan perbaikan yang perlu dilakukan pada iterasi berikutnya (Dzhurov dkk., 2009). Kegiatan kedua adalah pelaksanaan User Acceptance Testing (UAT) bersama pihak mitra, yaitu pengelola Bimbel Artha Balikpapan, yang dilaksanakan setelah seluruh iterasi rilis selesai pada iterasi ketiga.

UAT dilaksanakan menggunakan instrumen kuesioner berskala Likert dengan rentang satu hingga lima, yang mencakup butir-butir pertanyaan mengenai kemudahan penggunaan, kegunaan fitur, ketepatan informasi yang disajikan, dan kelayakan sistem secara keseluruhan (Apriyanti dkk., 2024). Kriteria penerimaan yang ditetapkan adalah persentase skor rata-rata keseluruhan mencapai minimal 80% dari skor maksimum, yang dikategorikan sebagai "Sangat Layak" (Gunawan dkk., 2025). Apabila hasil UAT belum memenuhi kriteria tersebut, maka identifikasi temuan dan perbaikan dilakukan sebelum versi final sistem diserahterimakan kepada mitra. Tabel 3.4 menyajikan kisi-kisi instrumen kuesioner UAT yang digunakan.

Tabel 3.4 Kisi-Kisi Instrumen Kuesioner User Acceptance Testing (UAT) Skala Likert

| No. | Aspek Penilaian | Indikator Butir Pertanyaan | Skala |
|:---:|:----------------|:---------------------------|:-----:|
| 1 | Kemudahan Penggunaan | Antarmuka sistem mudah dipahami tanpa panduan khusus | 1 hingga 5 |
| 2 | Kemudahan Penggunaan | Navigasi antarhalaman berjalan dengan intuitif | 1 hingga 5 |
| 3 | Kegunaan Fitur | Fitur pencatatan SPP sudah sesuai kebutuhan operasional | 1 hingga 5 |
| 4 | Kegunaan Fitur | Penjadwalan tentor membantu menghindari bentrok jadwal | 1 hingga 5 |
| 5 | Kegunaan Fitur | Notifikasi WhatsApp mempermudah komunikasi dengan wali murid | 1 hingga 5 |
| 6 | Ketepatan Informasi | Data yang ditampilkan akurat dan konsisten antarcabang | 1 hingga 5 |
| 7 | Ketepatan Informasi | Laporan kas mencerminkan kondisi keuangan sebenarnya | 1 hingga 5 |
| 8 | Kelayakan Keseluruhan | Sistem layak digunakan dalam operasional Bimbel Artha | 1 hingga 5 |

3.4 Konsep Prototipe

Subbab ini memaparkan konsep prototipe yang terdiri dari kebutuhan fungsional dalam format user stories, kebutuhan nonfungsional, dan arsitektur konseptual sistem secara keseluruhan.

3.4.1 Kebutuhan Fungsional

Kebutuhan fungsional sistem diformulasikan dalam format user stories sesuai praktik yang dianjurkan dalam kerangka kerja XP dan PxP (Beck, 2004). Setiap user story disusun dari perspektif pengguna dengan format: "Sebagai [peran], saya ingin [fungsi], sehingga [manfaat]." Format ini memastikan bahwa setiap fitur yang dikembangkan berakar pada kebutuhan nyata pengguna, bukan asumsi pengembang semata (Fikri & Arthawan, 2020). Kebutuhan fungsional yang ditetapkan mencakup modul: registrasi siswa baru, pencatatan dan kuitansi digital SPP, penjadwalan tentor, pembatasan kuota ruang kelas, notifikasi WhatsApp wali murid, dasbor rekapitulasi kas multicabang, serta manajemen akun pengguna (Abadi dkk., 2025; Khafidhoh dkk., 2026; Kabisatullah & Noprisson, 2026; Ramadhan & Widodo, 2026).

Tabel 3.5 menyajikan daftar user stories yang ditetapkan berdasarkan hasil analisis kebutuhan bersama narasumber Bimbel Artha Balikpapan, dikelompokkan berdasarkan peran pengguna.

Tabel 3.5 Daftar User Stories per Peran Pengguna

| ID | Peran | Judul | Deskripsi | Kriteria Penerimaan |
|:--:|:------|:------|:----------|:--------------------|
| US-01 | Admin Cabang | Login sistem | Sebagai Admin Cabang, saya ingin masuk ke sistem dengan akun khusus cabang, sehingga hanya saya yang dapat mengakses data cabang saya. | Sistem menampilkan halaman dasbor cabang setelah login berhasil; akun Admin Cabang lain tidak dapat mengakses data cabang ini. |
| US-02 | Admin Cabang | Registrasi siswa baru | Sebagai Admin Cabang, saya ingin mendaftarkan siswa baru ke sistem, sehingga data siswa tersimpan secara digital tanpa perlu buku tulis. | Data siswa berhasil tersimpan dan dapat dicari serta diperbarui kapan saja. |
| US-03 | Admin Cabang | Pencatatan pembayaran SPP | Sebagai Admin Cabang, saya ingin mencatat pembayaran SPP setiap siswa, sehingga riwayat pembayaran tersimpan secara otomatis dan terurut. | Setiap transaksi SPP berhasil dicatat dengan tanggal, nominal, dan status lunas atau belum lunas. |
| US-04 | Admin Cabang | Cetak kuitansi digital | Sebagai Admin Cabang, saya ingin mencetak kuitansi pembayaran dalam format PDF, sehingga dapat diberikan kepada wali murid tanpa kertas formulir manual. | Kuitansi PDF berhasil diunduh dan memuat nama siswa, tanggal, nominal, dan identitas cabang. |
| US-05 | Admin Cabang | Penjadwalan tentor | Sebagai Admin Cabang, saya ingin menjadwalkan sesi belajar tentor, sehingga tidak terjadi tumpang tindih jadwal di ruang yang sama. | Sistem menolak penjadwalan yang bentrok dan menampilkan pesan peringatan kepada pengguna. |
| US-06 | Admin Cabang | Pembatasan kuota ruang | Sebagai Admin Cabang, saya ingin membatasi jumlah siswa per sesi belajar, sehingga kapasitas ruang tidak terlampaui. | Sistem menolak pendaftaran sesi apabila kuota telah penuh dan menampilkan sisa kuota secara real-time. |
| US-07 | Admin Cabang | Notifikasi WhatsApp | Sebagai Admin Cabang, saya ingin mengirimkan notifikasi tagihan SPP kepada wali murid melalui WhatsApp, sehingga pengingat dapat dilakukan tanpa menelepon satu per satu. | Tombol tautan WhatsApp tersedia pada daftar tagihan dan mengisi pesan otomatis kepada nomor wali murid yang terdaftar. |
| US-08 | Super Admin | Dasbor multicabang | Sebagai Super Admin, saya ingin memantau rekap kas dan operasional seluruh cabang dalam satu dasbor, sehingga kondisi setiap cabang dapat dipantau tanpa mengunjungi tiap lokasi. | Dasbor menampilkan ringkasan pendapatan, jumlah siswa aktif, dan status operasional per cabang secara real-time. |
| US-09 | Super Admin | Laporan keuangan antarcabang | Sebagai Super Admin, saya ingin mengunduh laporan keuangan gabungan seluruh cabang dalam format Excel, sehingga rekonsiliasi kas dapat dilakukan secara efisien. | Laporan Excel berhasil diunduh, memuat rincian pemasukan per cabang, per periode, dan total keseluruhan. |
| US-10 | Super Admin | Manajemen akun Admin Cabang | Sebagai Super Admin, saya ingin membuat, mengubah, dan menonaktifkan akun Admin Cabang, sehingga kontrol akses sistem berada sepenuhnya di tangan pimpinan. | Akun Admin Cabang berhasil dibuat dan hanya Super Admin yang dapat mengakses fitur manajemen akun ini. |

3.4.2 Kebutuhan Nonfungsional

Selain kebutuhan fungsional, sistem harus memenuhi sejumlah kebutuhan nonfungsional yang berkaitan dengan kualitas operasional sistem secara keseluruhan. Sommerville (2011) mendefinisikan kebutuhan nonfungsional sebagai batasan terhadap layanan atau fungsi yang disediakan sistem, yang sering kali lebih kritis daripada kebutuhan fungsional itu sendiri karena kegagalannya dapat membuat seluruh sistem tidak dapat diterima oleh pengguna. Pressman & Maxim (2015) mengelompokkan kebutuhan nonfungsional ke dalam beberapa kategori utama, yaitu keamanan, keandalan, kegunaan, kinerja, dan keterpeliharaan.

Tabel 3.6 menyajikan daftar kebutuhan nonfungsional sistem informasi manajemen Bimbel Artha Balikpapan beserta indikator terukurnya.

Tabel 3.6 Daftar Kebutuhan Nonfungsional Sistem

| No. | Aspek | Kebutuhan | Indikator Terukur |
|:---:|:------|:----------|:------------------|
| 1 | Keamanan | Sistem menerapkan kendali akses berbasis peran (Role-Based Access Control) yang memisahkan hak akses Super Admin dan Admin Cabang secara ketat | Pengguna dengan peran Admin Cabang tidak dapat mengakses halaman yang dikhususkan untuk Super Admin |
| 2 | Keandalan | Sistem mampu menangani transaksi data bersamaan dari delapan cabang tanpa terjadi konflik atau kehilangan data | Uji simulasi delapan pengguna aktif serentak berhasil tanpa galat |
| 3 | Kegunaan | Antarmuka dirancang intuitif bagi staf administrasi yang tidak memiliki latar belakang teknologi informasi | Skor UAT pada aspek kemudahan penggunaan mencapai minimal 80% |
| 4 | Kompatibilitas | Sistem dapat diakses melalui peramban web modern tanpa instalasi perangkat lunak tambahan | Sistem berfungsi normal pada Google Chrome, Mozilla Firefox, dan Microsoft Edge versi terkini |
| 5 | Keterpeliharaan | Kode program mengikuti standar penulisan dan arsitektur MVC sehingga mudah dipelihara dan dikembangkan lebih lanjut | Tidak ada fungsi dengan panjang lebih dari 50 baris kode; setiap modul memiliki komentar deskriptif |

3.4.3 Arsitektur Konseptual Sistem

Sistem informasi manajemen Bimbel Artha Balikpapan dirancang menggunakan arsitektur client-server berbasis web, di mana seluruh logika bisnis dan basis data dipusatkan pada satu peladen yang dapat diakses oleh semua kantor cabang melalui jaringan internet menggunakan peramban web (Pressman & Maxim, 2015). Model arsitektur ini dipilih karena memungkinkan konsistensi data secara real-time antarcabang tanpa memerlukan replikasi atau sinkronisasi data secara manual, sebagaimana dibuktikan oleh Ahadi dkk. (2025) pada sistem manajemen hotel multicabang dan Fajriansyah dkk. (2026) pada sistem informasi bimbel terpusat. Admin Cabang dari delapan kantor cabang dapat mengakses sistem secara bersamaan melalui jaringan internet, sementara Super Admin memiliki jalur akses yang sama namun dengan hak akses yang lebih luas mencakup seluruh data lintas cabang.

Gambar 3.8 menyajikan diagram arsitektur konseptual sistem yang menggambarkan hubungan antara delapan kantor cabang Bimbel Artha Balikpapan, Super Admin, dan peladen basis data terpusat.

[Gambar 3.8 Diagram Arsitektur Konseptual Client-Server Sistem Informasi Bimbel Artha Balikpapan]

Catatan mahasiswa: Buat diagram sederhana yang menampilkan 8 ikon komputer berlabel nama cabang dan 1 ikon Super Admin, semuanya terhubung melalui garis ke simbol awan (internet), yang kemudian terhubung ke ikon peladen berlabel "Database Server Terpusat". Gunakan draw.io, Figma, atau PowerPoint.

3.5 Spesifikasi Teknis

Subbab ini memaparkan spesifikasi lingkungan komputasi yang digunakan dalam proses pengembangan dan pengoperasian prototipe, mencakup kebutuhan perangkat keras, perangkat lunak, dan konfigurasi operasional.

3.5.1 Kebutuhan Perangkat Keras

Tabel 3.7 menyajikan spesifikasi perangkat keras yang digunakan selama proses pengembangan prototipe, serta spesifikasi minimum perangkat yang dibutuhkan di sisi pengguna pada kantor cabang Bimbel Artha Balikpapan.

Tabel 3.7 Spesifikasi Perangkat Keras

| Komponen | Spesifikasi Pengembang | Spesifikasi Minimum Pengguna |
|:---------|:-----------------------|:-----------------------------|
| Prosesor | [Isi sesuai spesifikasi perangkat Anda] | Intel Core i3 generasi ke-8 atau setara |
| Memori RAM | [Isi sesuai spesifikasi perangkat Anda] | 4 GB |
| Penyimpanan | [Isi sesuai spesifikasi perangkat Anda] | 10 GB ruang kosong tersedia |
| Koneksi Internet | [Isi kecepatan koneksi internet Anda] | Minimal 5 Mbps stabil |
| Peramban Web | Google Chrome / Mozilla Firefox | Google Chrome / Firefox / Edge versi terbaru |

Catatan mahasiswa: Isi kolom "Spesifikasi Pengembang" dengan spesifikasi aktual laptop atau komputer yang Anda gunakan selama mengerjakan tugas akhir ini.

3.5.2 Kebutuhan Perangkat Lunak

Tabel 3.8 menyajikan seluruh perangkat lunak yang digunakan dalam proses pengembangan prototipe, mulai dari sistem operasi, bahasa pemrograman, kerangka kerja, sistem manajemen basis data, hingga perangkat perancangan antarmuka (Karpina dkk., 2025; Sidiq dkk., 2025).

Tabel 3.8 Daftar Perangkat Lunak yang Digunakan dalam Pengembangan

| No. | Kategori | Nama Perangkat Lunak | Versi | Fungsi |
|:---:|:---------|:---------------------|:-----:|:-------|
| 1 | Sistem Operasi | Windows 11 | — | Sistem operasi utama pengembang |
| 2 | Bahasa Pemrograman | PHP | [Isi versi] | Logika sisi peladen (server-side logic) |
| 3 | Bahasa Pemrograman | JavaScript | ES6+ | Interaktivitas sisi klien (client-side) |
| 4 | Bahasa Markah | HTML5 dan CSS3 | — | Struktur dan tampilan antarmuka pengguna |
| 5 | Kerangka Kerja | [Isi nama framework PHP Anda] | [Isi versi] | Struktur arsitektur MVC aplikasi |
| 6 | Basis Data | MySQL | [Isi versi] | Sistem manajemen basis data relasional |
| 7 | Peladen Lokal | XAMPP / Laragon | [Isi versi] | Lingkungan pengembangan lokal (localhost) |
| 8 | Rancang Antarmuka | Figma | — | Perancangan wireframe dan mockup antarmuka |
| 9 | Pengelola Kode | Visual Studio Code | — | Lingkungan pengembangan terpadu (IDE) |
| 10 | Pengujian | Google Chrome DevTools | — | Pengujian fungsional dan inspeksi antarmuka |

Catatan mahasiswa: Isi kolom "Versi" dengan versi perangkat lunak yang sesungguhnya Anda gunakan. Apabila Anda menggunakan kerangka kerja PHP tertentu seperti Laravel atau CodeIgniter, cantumkan namanya dan versinya di baris nomor 5.

3.5.3 Lingkungan Operasional dan Konfigurasi

Selama tahap pengembangan, sistem dijalankan pada lingkungan peladen lokal menggunakan XAMPP atau Laragon. Basis data MySQL dikonfigurasi dengan skema terpusat yang mencakup seluruh tabel untuk semua cabang dalam satu basis data, dengan pembedaan data antarcabang menggunakan kunci asing (foreign key) yang merujuk ke tabel cabang (Karpina dkk., 2025; Sidiq dkk., 2025). Pendekatan basis data terpusat ini memastikan integritas referensial antarcabang dapat dijaga secara otomatis oleh mesin basis data tanpa intervensi pengembang.

Keamanan sesi pengguna diterapkan melalui mekanisme autentikasi berbasis sesi PHP dengan enkripsi kata sandi menggunakan algoritma bcrypt. Setiap sesi pengguna menyimpan informasi peran dan identitas cabang sehingga seluruh permintaan data yang masuk ke peladen dapat difilter dan diotorisasi berdasarkan peran tersebut. Untuk keperluan penerapan pada lingkungan mitra, sistem akan dipasang pada layanan hosting web berbasis Linux dengan spesifikasi yang memadai untuk menampung delapan koneksi aktif secara bersamaan dari seluruh cabang Bimbel Artha Balikpapan.

3.6 Jadwal Pembuatan Prototipe

Pengembangan prototipe sistem informasi manajemen Bimbel Artha Balikpapan direncanakan berlangsung selama dua belas minggu, terbagi ke dalam tiga siklus iterasi PxP dan beberapa kegiatan pendukung yang berjalan paralel. Penyusunan jadwal merujuk pada kerangka perencanaan iterasi PxP yang dikemukakan oleh Dzhurov dkk. (2009), serta praktik penyusunan jadwal yang diterapkan pada proyek-proyek PxP serupa di Indonesia (Fikri & Arthawan, 2020; Sidiq dkk., 2025). Tabel 3.9 menyajikan jadwal pelaksanaan pembuatan prototipe secara mingguan beserta milestone capaian utama setiap fase pengembangan.

Tabel 3.9 Jadwal Pelaksanaan Pembuatan Prototipe (Gantt Chart)

| No. | Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | Milestone Capaian |
|:---:|:---------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|:---:|:---:|:------------------|
| 1 | Studi literatur dan analisis kebutuhan | X | X | | | | | | | | | | | Daftar user stories final tersusun |
| 2 | Perencanaan dan penyusunan product backlog | | X | X | | | | | | | | | | Product backlog dan jadwal iterasi |
| 3 | Perancangan UML, ERD, PDM, dan mockup | | | X | X | | | | | | | | | Seluruh artefak desain selesai |
| 4 | Iterasi I: Fondasi DB, registrasi, SPP, kuitansi | | | | X | X | X | | | | | | | Modul Iterasi I siap diuji |
| 5 | Pengujian Black Box Iterasi I dan retrospektif | | | | | | X | | | | | | | Laporan uji Iterasi I |
| 6 | Iterasi II: Penjadwalan, kuota ruang, WhatsApp | | | | | | | X | X | X | | | | Modul Iterasi II siap diuji |
| 7 | Pengujian Black Box Iterasi II dan retrospektif | | | | | | | | | X | | | | Laporan uji Iterasi II |
| 8 | Iterasi III: Dasbor Super Admin, rekonsiliasi kas | | | | | | | | | | X | X | | Modul Iterasi III siap diuji |
| 9 | Pengujian Black Box Iterasi III dan UAT mitra | | | | | | | | | | | X | X | Laporan UAT dan persetujuan mitra |
| 10 | Penyusunan laporan akhir dan dokumen HKI | | | | | | | | | | | | X | Laporan TA dan draft Hak Cipta siap |

Keterangan: M = Minggu ke-. X = Periode aktif kegiatan pada minggu tersebut.

Berdasarkan Tabel 3.9, terdapat empat milestone capaian utama yang menjadi penanda kemajuan proyek. Pertama, seluruh artefak perancangan meliputi diagram UML, ERD, PDM, dan prototipe antarmuka harus diselesaikan sebelum memasuki Iterasi I pada minggu ke-4. Kedua, setiap iterasi diakhiri dengan sesi pengujian fungsional dan retrospektif yang menghasilkan laporan tertulis sebagai dasar evaluasi lanjut. Ketiga, UAT bersama mitra dilaksanakan setelah Iterasi III selesai, yakni pada minggu ke-11 dan ke-12, guna memvalidasi keseluruhan sistem dalam kondisi operasional nyata. Keempat, penyusunan laporan akhir dan dokumen draft Hak Cipta dilaksanakan secara paralel dengan kegiatan UAT pada minggu terakhir pengembangan.
