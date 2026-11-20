# BAB 3
# RANCANGAN PROTOTIPE

Bab ini menjelaskan bagaimana prototipe sistem informasi manajemen operasional ARTHA akan dikembangkan untuk Bimbingan Belajar Artha Balikpapan. Pembahasan dimulai dari gambaran sistem, kemudian dilanjutkan dengan tahapan pengembangan, prosedur penelitian, rancangan fungsi, spesifikasi teknis, dan jadwal pengerjaan. Keenam bagian tersebut mengikuti susunan laporan tugas akhir jalur prototipe (Institut Teknologi Kalimantan, 2025b).

## 3.1 Garis Besar Prototipe

Bimbingan Belajar Artha Balikpapan mengelola delapan cabang dengan kegiatan administrasi yang mencakup pendaftaran siswa, penempatan kelas, penjadwalan tentor, serta pembayaran biaya belajar. Kegiatan tersebut perlu dihubungkan agar informasi yang dicatat pada cabang dapat digunakan pula oleh pengelola pusat. Untuk kebutuhan tersebut, prototipe ARTHA dirancang sebagai sistem informasi berbasis web dengan dua peran pengguna, yaitu Admin Cabang dan Super Admin.

### 3.1.1 Objek dan Konteks Pengembangan

Pengembangan ARTHA berangkat dari penelaahan wawancara dengan pengelola dan staf administrasi mengenai cara mereka mencatat serta menggunakan data operasional. Hasil penelaahan menjadi dasar untuk menghubungkan data siswa, jadwal, dan pembayaran dalam satu sistem. Rancangan integrasi ini juga merujuk penelitian sistem bimbel yang membahas hubungan antarfungsi tersebut (Fajriansyah dkk., 2026, hlm. 116, 124 sampai 125; Gunawan dkk., 2025, hlm. 424).

### 3.1.2 Ruang Lingkup dan Pengguna Prototipe

Pembagian peran dalam ARTHA mengikuti pekerjaan administrasi cabang dan kebutuhan pengawasan pusat. Admin Cabang mengelola data pada cabang penugasannya, sementara Super Admin melihat informasi lintas cabang dan menjalankan pengendalian sesuai kewenangannya. Pemisahan akses semacam ini dibahas oleh Ahadi dkk. (2025, hlm. 764 sampai 765) serta Thiovanda (2026, hlm. 4) dalam pengelolaan informasi berdasarkan cabang.

Pada kegiatan penagihan, admin dapat membuka daftar tunggakan dan memilih tombol WhatsApp untuk menyiapkan pesan kepada wali siswa. Sistem mengisi nomor serta rincian tagihan, kemudian admin memeriksa dan mengirim pesan melalui WhatsApp. Untuk penempatan siswa, informasi keterisian membantu admin memilih kelas yang masih tersedia; penambahan ditolak ketika penuh dan tempat kembali terbuka setelah keanggotaan siswa diakhiri.

Alur pembayaran transfer dirancang dengan membagi tugas pengajuan bukti kepada Admin Cabang dan pemeriksaan dana masuk kepada Super Admin. Pembagian kewenangan rekening serta petugas pemeriksanya akan ditetapkan bersama mitra sebelum digunakan. Dengan cakupan administrasi internal tersebut, prototipe menyediakan pencocokan penerimaan secara manual, sementara pembelajaran daring, pengiriman WhatsApp otomatis, dan integrasi bank otomatis berada di luar lingkup pengembangan.

### 3.1.3 Pendekatan Pengembangan Prototipe

Pengembangan ARTHA dikerjakan secara individual menggunakan metode *Personal Extreme Programming* (PxP). Prosesnya mencakup penggalian kebutuhan, perencanaan, inisialisasi iterasi, perancangan, implementasi, pengujian sistem, dan evaluasi iterasi (Dzhurov dkk., 2009, hlm. 253 sampai 256). Penerapan metode ini pada pengembangan sistem informasi juga dijelaskan oleh Fikri dan Arthawan Sugih Prabowo (2021, hlm. 103 sampai 105), yang menjadi rujukan dalam menyusun pekerjaan pengembangan ARTHA.

### 3.1.4 Luaran yang Ditargetkan

Hasil yang ditargetkan dari penelitian ini adalah prototipe perangkat lunak beserta dokumentasi pengembangan dan evaluasinya bersama calon pengguna. Pengembangan diarahkan pada TKT 5 sebagaimana ketentuan tugas akhir prototipe (Institut Teknologi Kalimantan, 2026, hlm. 4). Pencapaiannya akan dijelaskan melalui bukti pelaksanaan dan hasil evaluasi yang diperoleh selama penelitian.

Dokumentasi pengembangan disusun bersamaan dengan pengerjaan sistem agar dapat digunakan dalam laporan tugas akhir, artikel ilmiah, dan bahan pengajuan HKI. Bagian hasil nantinya memuat fungsi yang telah dibangun, pelaksanaan pengujian, serta keputusan penerimaan mitra. Dengan cara ini, uraian produk dapat dibaca bersama proses dan hasil penilaiannya.

## 3.2 Tahapan Pembuatan Prototipe

Pembuatan prototipe dimulai dengan memahami kebutuhan pengguna, kemudian berlanjut ke perencanaan dan pengembangan fungsi secara bertahap. Setiap tahap menghasilkan bahan yang digunakan pada pekerjaan berikutnya, dengan ruang perbaikan ketika ditemukan masalah atau perubahan kebutuhan. Hubungan antartahap dan jalur perulangannya ditunjukkan pada Gambar 3.1.

![Diagram alir pembuatan prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_1_Alur_Pembuatan_Prototipe.png>)

**Gambar 3.1 Alur Pembuatan Prototipe Sistem Informasi ARTHA**

Sumber: Dzhurov dkk. (2009, hlm. 254 sampai 256), telah diolah dengan penambahan evaluasi pengguna dan penyiapan luaran penelitian.

Kebutuhan yang telah dirumuskan digunakan untuk memilih pekerjaan pada setiap iterasi. Pengembang merancang dan mengimplementasikan fungsi tersebut, lalu memeriksa kesesuaiannya melalui pengujian sistem. Pada akhir iterasi, hasil pekerjaan dibahas bersama catatan waktu, galat, dan usulan perbaikan untuk menentukan langkah berikutnya.

Apabila hasil pengujian belum memenuhi kriteria, pengembang memperbaiki fungsi yang bermasalah dan menjalankan pengujian ulang sebelum menutup iterasi. Pekerjaan yang masih tersisa kemudian dimasukkan ke iterasi berikutnya sesuai prioritas dan ketergantungannya. Setelah fungsi siap dievaluasi oleh pengguna, proses berlanjut ke UAT.

Masukan pengguna pada UAT ditindaklanjuti sesuai jenis perubahannya. Perubahan kebutuhan dibahas kembali pada penggalian kebutuhan dan perencanaan, sedangkan kesalahan fungsi ditangani melalui perbaikan serta pengujian ulang. Hasil tindak lanjut menjadi bahan untuk menentukan penerimaan dan menyiapkan luaran prototipe.

UAT dilaksanakan setelah modul melewati pemeriksaan awal agar pengguna dapat mencoba alur kerja yang telah dipersiapkan. Penerapan PxP bersama pengujian sistem dan evaluasi pengguna dijelaskan oleh Apriyanti dkk. (2024, hlm. 3680, 3683 sampai 3685). Dalam penelitian ARTHA, tugas evaluasi disusun berdasarkan pekerjaan administrasi cabang dan pengawasan pusat.

Kegiatan dan luaran pada setiap tahap dirangkum dalam Tabel 3.1 untuk melengkapi diagram pada Gambar 3.1. Penjelasan mengenai cara melaksanakan kegiatan tersebut disajikan pada Subbab 3.3. Urutan ini menghubungkan gambaran proses dengan pekerjaan yang akan dilakukan selama pengembangan.

**Tabel 3.1 Tahapan dan Luaran Pembuatan Prototipe**

| Tahap | Kegiatan utama | Luaran yang direncanakan |
| :--- | :--- | :--- |
| Penggalian kebutuhan | Telaah transkrip, studi literatur, klarifikasi proses, dan validasi kebutuhan | Matriks bukti kebutuhan, daftar fungsi, serta batasan |
| Perencanaan | Penentuan prioritas, rincian tugas, estimasi durasi, dan pembagian iterasi | Rencana iterasi dan daftar tugas |
| Inisialisasi iterasi | Pemilihan tugas, penetapan data uji, dan kriteria penyelesaian | Rencana kerja iterasi |
| Perancangan | Penyusunan model akses, proses, data, dan antarmuka | Rancangan modul pada iterasi berjalan |
| Implementasi | Pengujian unit, pengodean, dan perbaikan struktur kode | Modul aplikasi dan bukti pengujian unit |
| Pengujian sistem | Pelaksanaan kasus uji dan pengujian ulang perbaikan | Hasil uji dan catatan galat |
| Evaluasi iterasi | Perbandingan estimasi dengan waktu aktual dan telaah galat | Catatan evaluasi serta tindakan perbaikan |
| UAT dan analisis evaluasi | Pelaksanaan tugas pengguna dan pencatatan keputusan penerimaan | Hasil penerimaan, masukan, dan daftar tindak lanjut |
| Dokumentasi dan luaran | Penyusunan laporan, artikel, serta dokumen produk | Dokumentasi penelitian dan bahan pengajuan HKI |

## 3.3 Prosedur

Prosedur penelitian menjelaskan cara menjalankan tahapan pengembangan mulai dari penggalian kebutuhan sampai evaluasi pengguna. Pada setiap tahap, sumber informasi, instrumen, dan hasil pekerjaan dicatat untuk digunakan pada tahap berikutnya. Uraian ini menjadi pedoman pelaksanaan sekaligus penghubung antara kebutuhan mitra dan fungsi yang akan diuji.

### 3.3.1 Penggalian Kebutuhan (*Requirements*)

Penggalian kebutuhan dimulai dengan membaca kembali transkrip wawancara pengelola dan staf administrasi Artha. Informasi di dalamnya dikelompokkan menurut kegiatan pendaftaran, penentuan tarif, pembayaran, pengelolaan kelas, penjadwalan tentor, dan pelaporan cabang. Pengelompokan ini membantu menemukan hubungan antarkegiatan serta pertanyaan yang masih perlu dijelaskan oleh mitra.

Klarifikasi dilakukan kepada pihak yang memahami dan menjalankan proses terkait. Pengelola pusat menjelaskan kebutuhan pemantauan serta pembagian kewenangan, sedangkan staf administrasi menjelaskan pekerjaan pencatatan pada cabang. Pemilihan informan mengikuti tanggung jawab tersebut agar informasi diperoleh dari pihak yang sesuai.

Setiap kegiatan klarifikasi dilengkapi catatan informan, cabang yang diwakili, tanggal, dan alasan pemilihannya. Keterangan yang khusus berlaku pada satu cabang akan dibahas dengan pengelola untuk menentukan apakah ketentuan serupa juga berlaku di cabang lain. Jumlah serta identitas atau kode informan kemudian dicantumkan dalam dokumentasi penelitian.

Tabel 3.2 menunjukkan bahan wawancara yang sudah tersedia dan topik klarifikasi yang masih diperlukan. Catatan ini membantu menentukan informasi yang dapat digunakan serta hal yang perlu ditanyakan kembali. Tanggal pada notulensi akan dicocokkan dengan bukti asli sebelum dilengkapi dalam dokumentasi pelaksanaan.

**Tabel 3.2 Sumber Kebutuhan dan Status Bukti**

| Kode | Sumber dan cakupan | Informasi yang digunakan | Tanggal dan status |
| :--- | :--- | :--- | :--- |
| S-01 | Wawancara pertama pengelola | Pendaftaran, paket, dan kebutuhan administrasi | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-02 | Wawancara kedua, Om Anang | Sistem lama, kebutuhan integrasi, dan akses cabang | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-03 | Wawancara ketiga, Mama Radit | Tarif, potongan, penerimaan, dan pencocokan bank | Transkrip tersedia; tanggal perlu pemeriksaan |
| S-04 | Wawancara frontdesk, konteks Cabang 5 | Pelaksanaan pendaftaran, jatuh tempo, ruang, dan pelaporan harian | Transkrip tersedia; cakupan cabang diklarifikasi |
| S-05 | Bimbingan Bu Ayu dan Pak Arif | Batas lingkup, keluwesan aturan, metode, dan evaluasi | Transkrip tersedia; arahan dipetakan ke rancangan |
| S-06 | Penjelasan pengguna selama penyusunan | WhatsApp manual dan penolakan kelas penuh | Keputusan rancangan pengguna; bukan persetujuan seluruh mitra |
| S-07 | Pengelola keuangan dan admin yang ditunjuk | Pemeriksa rekening, tarif berlaku, setoran, serta parameter kapasitas | Klarifikasi lanjutan belum dilaksanakan |

Berkas sumber dan penanda waktu wawancara dihimpun dalam lampiran agar bagian yang dirujuk mudah ditemukan kembali. Keterangan tentang tarif atau peristiwa tertentu tetap disertai konteks cabangnya. Pengelola kemudian diminta menjelaskan cakupan ketentuan tersebut ketika digunakan untuk merancang fungsi lintas cabang.

Wawancara lanjutan dilakukan secara semiterstruktur, dengan topik utama yang telah disiapkan dan pertanyaan tambahan mengikuti jawaban informan. Cara ini memberi ruang untuk membahas perbedaan keterangan maupun rincian proses yang belum jelas. Topik wawancara dan pemeriksaan dokumen disajikan pada Tabel 3.3, sedangkan pertanyaan rinci ditempatkan pada lampiran.

**Tabel 3.3 Rancangan Topik Wawancara dan Pemeriksaan Dokumen**

| Topik | Informasi yang ditelusuri | Pihak atau dokumen yang relevan |
| :--- | :--- | :--- |
| Pendaftaran | Data wajib, penetapan cabang, penempatan kelas, dan perubahan keanggotaan | Admin Cabang, formulir atau buku pendaftaran |
| Tarif dan tagihan | Periode, tanggal jatuh tempo, variasi tarif, serta kewenangan diskon | Pengelola dan catatan tarif yang berlaku |
| Pembayaran transfer | Penerima dana, pengajuan bukti, akses mutasi, pemeriksa, dan koreksi | Admin Cabang dan petugas keuangan pusat |
| Pembayaran tunai | Penerimaan, kuitansi, penyimpanan kas, dan penyerahan setoran | Admin Cabang dan penerima setoran pusat |
| Kelas | Kapasitas fisik, kapasitas kelompok, ambang hampir penuh, dan siswa keluar | Pengelola cabang dan daftar peserta kelas |
| Jadwal | Identitas tentor, hari, waktu, ruangan, dan pemeriksaan lintas cabang | Pengelola jadwal dan buku jadwal |
| Pelaporan | Periode laporan, dasar penghitungan, status pemeriksaan, dan kebutuhan pusat | Pengelola pusat dan contoh rekap yang diizinkan |
| Evaluasi | Pengguna yang bersedia, tugas yang diuji, dan waktu pelaksanaan | Perwakilan mitra yang ditunjuk |

Penjelasan informan dilengkapi dengan dokumen yang penggunaannya diizinkan, seperti kuitansi, daftar siswa, jadwal, rekap pembayaran, dan bukti transfer. Dokumen tersebut membantu memahami informasi yang dicatat serta perpindahannya dari cabang ke pusat. Jika dilakukan pengamatan langsung, waktu, kegiatan yang diamati, dan hasilnya dicatat tersendiri sebagai pelengkap keterangan wawancara.

Informasi yang terkumpul dianalisis dengan mengelompokkan kebutuhan, membandingkan keterangan yang berbeda, dan membahas bagian yang masih memerlukan klarifikasi. Kebutuhan yang telah diperjelas kemudian dirumuskan menjadi fungsi serta cerita pengguna. Penyusunan kebutuhan dalam bentuk *user story* merujuk contoh pada Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105) serta Sidiq dkk. (2025, hlm. 37).

Kebutuhan yang dirumuskan diberi kode dan dihubungkan dengan sumber, cakupan cabang, serta hasil peninjauannya. Catatan ini juga membedakan kebutuhan yang berasal dari kendala yang telah dijelaskan informan dan fungsi pencegahan yang diusulkan dalam rancangan. Perbedaan tersebut membantu mitra menilai alasan pengembangan setiap fungsi.

Ringkasan proses dan kebutuhan kemudian ditinjau bersama perwakilan mitra yang berwenang. Masukan dari peninjauan digunakan untuk memperbaiki uraian fungsi sebelum pekerjaan dibagi ke dalam iterasi. Jika terdapat perubahan, versi sebelumnya tetap disimpan agar alasan penyesuaiannya dapat ditelusuri.

### 3.3.2 Perencanaan (*Planning*)

Kebutuhan yang telah dirumuskan dibagi menjadi tugas analisis, perancangan, pengodean, pengujian, dan perbaikan. Pengembang memperkirakan waktu setiap tugas berdasarkan rincian pekerjaan, lalu memperbarui perkiraan tersebut menggunakan durasi aktual pada pekerjaan sejenis. Cara ini mengikuti penggunaan data pekerjaan dalam perencanaan PxP (Dzhurov dkk., 2009, hlm. 254 sampai 255).

Pengembangan direncanakan dalam empat iterasi dengan memperhatikan urutan kebutuhan data dan hubungan antarfungsi. Akun, cabang, siswa, kelas, serta tarif disiapkan lebih dahulu karena digunakan pada penempatan, penjadwalan, pembayaran, dan pelaporan. Pembagian pekerjaan beserta ketergantungannya disajikan pada Tabel 3.4.

**Tabel 3.4 Rencana Iterasi dan Ketergantungan Kebutuhan**

| Iterasi | Kebutuhan dan cerita pengguna | Lingkup pekerjaan | Prasyarat dan keluaran |
| :--- | :--- | :--- | :--- |
| I-01 | KF-01, KF-02, KF-03, KF-06, KF-14; US dengan nomor yang sama | Akun, cabang, siswa, ruang, kelas, serta dasar tarif dan tagihan | Data dasar dan pembatasan akses dapat diperiksa |
| I-02 | KF-04, KF-05; US-04 dan US-05 | Keanggotaan, kapasitas, jadwal, serta pemeriksaan irisan | Master I-01 tersedia; kelas penuh dan konflik diuji |
| I-03 | KF-07, KF-08, KF-09, KF-10; US dengan nomor yang sama | Tunai, pengajuan transfer, pemeriksaan, serta tautan WhatsApp | Tagihan tersedia; layanan pencocokan transfer dasar dibuat agar verifikasi dapat diuji |
| I-04 | KF-11, KF-12, KF-13; US dengan nomor yang sama | Setoran, rekap pusat, pencocokan, serta integrasi | Penerimaan I-03 tersedia; transaksi sumber dapat ditelusuri |

Pada I-03, pemeriksaan transfer memerlukan data rekening dan referensi dana masuk agar pengajuan dapat diputuskan. Karena itu, komponen pencocokan dasar disiapkan bersama modul pembayaran. Pengembangannya dilanjutkan pada I-04 untuk mencakup setoran tunai dan rekap yang menghubungkan seluruh proses penerimaan.

Setiap iterasi direncanakan berlangsung dua minggu, sesuai rentang iterasi PxP satu sampai tiga minggu (Dzhurov dkk., 2009, hlm. 255). Alokasi ini akan dirinci menjadi estimasi jam per tugas sebelum iterasi dimulai. Jadwal dua belas minggu pada Subbab 3.6 digunakan sebagai rencana awal yang akan disesuaikan dengan kebutuhan dan ketersediaan waktu pelaksanaan.

Masukan baru dari mitra dibahas dengan melihat fungsi yang terdampak, ketergantungan pekerjaan, dan kebutuhan pengujiannya. Keputusan perubahan dicatat bersama sumber permintaan serta pengaruhnya terhadap jadwal. Rincian estimasi dan formulir perubahan disimpan pada lampiran untuk mendukung penyesuaian rencana kerja.

### 3.3.3 Inisialisasi Iterasi (*Iteration Initialization*)

Pada awal setiap iterasi, pengembang memilih tugas dari rencana kerja sesuai prioritas yang telah ditentukan. Tugas tersebut dilengkapi kode kebutuhan, penanggung jawab, estimasi waktu, data uji, dan kriteria selesai. Kelengkapan ini memberi gambaran tentang pekerjaan yang harus dihasilkan serta cara memeriksanya.

Data uji disiapkan sebelum pengerjaan untuk menggambarkan kegiatan pada cabang yang berbeda. Selain kondisi normal, data mencakup masukan yang tidak sah dan keadaan batas yang dapat memengaruhi proses. Identitas siswa serta bukti pembayaran menggunakan data buatan atau tersamarkan sesuai izin mitra.

Perubahan kode disimpan dalam repositori dengan penanda versi agar perkembangan modul dapat diikuti. Waktu pengerjaan dicatat per tugas, mulai dari analisis dan perancangan sampai pengujian serta perbaikan. Catatan tersebut digunakan untuk membandingkan rencana dan pelaksanaan ketika iterasi dievaluasi.

Penyelesaian tugas diperiksa berdasarkan kriteria penerimaan dan galat yang masih terbuka. Tugas selesai secara teknis apabila kriterianya terpenuhi dan tidak menyisakan galat kritis. Hasil tersebut kemudian menjadi bahan evaluasi mitra, dengan keputusan penerimaan pengguna dicatat tersendiri.

### 3.3.4 Perancangan (*Design*)

Perancangan menerjemahkan kebutuhan pada iterasi berjalan ke dalam gambaran fungsi yang akan dibangun. Pengembang menyusun pembagian kewenangan, alur pekerjaan pengguna, hubungan data, serta susunan antarmuka. Rancangan ini menjadi acuan ketika fungsi diimplementasikan dan diuji.

Model dipilih sesuai kebutuhan modul agar dapat membantu pengembang memahami proses sebelum menulis kode. Penggunaan rancangan sederhana mengikuti penjelasan Dzhurov dkk. (2009, hlm. 255), sementara Fikri dan Arthawan Sugih Prabowo (2021, hlm. 104) menunjukkan penggunaan rancangan basis data dan antarmuka dalam pengembangan sistem. Pada ARTHA, model tersebut disusun untuk memperjelas pekerjaan pengguna dan hubungan antardata.

Pada proses pembayaran, rancangan membedakan penerimaan uang siswa, pemeriksaan transfer, dan penyerahan kas cabang. Ketiganya mempunyai pelaksana serta waktu pencatatan yang berbeda. Pemisahan ini menjaga agar uang yang sudah dicatat sebagai penerimaan tidak dihitung lagi ketika dipindahkan ke pusat.

Pengelolaan kelas dirancang dengan membedakan ruang fisik, kelompok belajar, dan keanggotaan siswa. Jumlah anggota aktif digunakan untuk menentukan ketersediaan tempat pada kelas yang dipilih. Ketika siswa keluar, keanggotaannya diakhiri dan riwayatnya tetap tersimpan sebagai bagian dari perjalanan belajar siswa pada kelas tersebut.

Setiap rancangan diperiksa kembali dengan melihat kebutuhan dan kasus uji yang berkaitan. Pemeriksaan ini membantu menemukan aturan yang perlu diperjelas sebelum memengaruhi struktur data atau alur aplikasi. Pertanyaan yang muncul dibahas melalui klarifikasi mitra, kemudian hasilnya digunakan untuk menyempurnakan rancangan.

### 3.3.5 Implementasi (*Implementation*)

Implementasi mengubah rancangan menjadi fungsi aplikasi melalui pengujian unit, pengodean, dan refaktorisasi. Pengujian disusun sebelum kode dilengkapi, lalu struktur kode diperbaiki setelah fungsi memenuhi hasil yang diharapkan. Urutan ini mengikuti praktik implementasi PxP pada Dzhurov dkk. (2009, hlm. 255).

Praktik *Test-Driven Development* (TDD) dipusatkan pada aturan bisnis yang dapat diperiksa secara otomatis. Pada ARTHA, aturan tersebut mencakup penghitungan sisa tagihan, penolakan penambahan siswa ke kelas penuh, dan pemeriksaan irisan jadwal tentor. Pemilihan ini mengarahkan pengujian pada logika yang menentukan hasil pekerjaan pengguna.

Untuk setiap aturan, pengembang lebih dahulu menyusun pengujian dengan hasil yang diharapkan. Kode kemudian dilengkapi sampai pengujian tersebut lulus. Hasil pengujian sebelum dan sesudah perbaikan disimpan bersama perubahan kode sebagai dokumentasi pelaksanaan TDD.

Setelah fungsi bekerja sesuai pengujian, struktur kode ditinjau agar pembagian tanggung jawabnya lebih jelas dan pengulangan dapat dikurangi. Refaktorisasi dilakukan dengan mempertahankan perilaku fungsi yang telah diperiksa. Pengujian dijalankan kembali setelahnya untuk memastikan perubahan struktur tetap menghasilkan keluaran yang sama.

Antarmuka dan layanan data dihubungkan secara bertahap mengikuti fungsi yang sedang dikerjakan. Pada setiap permintaan, peladen memeriksa peran pengguna serta cabang pemilik data sebelum memberikan akses. Dengan demikian, pembatasan akses tetap berlaku ketika pengguna mengubah alamat halaman atau identitas objek pada permintaan.

### 3.3.6 Pengujian Sistem (*System Testing*)

Pengujian sistem memeriksa apakah fungsi aplikasi menghasilkan keluaran sesuai kebutuhan melalui pendekatan kotak hitam atau *Black Box Testing*. Penerapan pengujian ini dalam pengembangan PxP dijelaskan oleh Apriyanti dkk. (2024, hlm. 3679, 3683). Kasus ARTHA disusun berdasarkan pekerjaan pengguna, terutama pembatasan akses, kapasitas kelas, dan pencatatan transaksi.

Pengembang menjalankan kasus pengujian pada lingkungan terpisah menggunakan data buatan atau tersamarkan. Sebelum pengujian dimulai, versi aplikasi, perangkat, zona waktu, dan keadaan data awal dicatat. Informasi ini digunakan ketika kasus perlu diulang atau hasilnya dibandingkan setelah perbaikan.

Tabel 3.5 menampilkan beberapa kasus yang berkaitan dengan risiko utama pengelolaan data dan transaksi. Rincian seluruh kasus BB-01 sampai BB-33 tersedia pada lampiran pengujian. Kasus tersebut dihubungkan dengan kebutuhan melalui kelompok PU-01 sampai PU-14 pada Tabel 3.13.

**Tabel 3.5 Contoh Kasus Pengujian Sistem**

| Kode | Kondisi yang diperiksa | Keluaran yang diharapkan | Pelaksanaan |
| :--- | :--- | :--- | :--- |
| BB-01 | Akun cabang meminta objek cabang lain | Akses ditolak dan objek tidak dikirim | Belum diuji |
| BB-07 | Dua permintaan mengisi satu tempat terakhir | Hanya satu keanggotaan aktif baru tersimpan | Belum diuji |
| BB-14 | Pengajuan dikembalikan kemudian diajukan ulang | Pengajuan lama tetap tersimpan dan pengajuan baru tertaut | Belum diuji |
| BB-16 | Persetujuan transfer dikirim berulang | Penerimaan, alokasi, serta pencocokan hanya berlaku sekali | Belum diuji |
| BB-17 | Admin membuka pesan tunggakan | Nomor dan isi sesuai; pembukaan tidak dianggap bukti terkirim | Belum diuji |
| BB-20 | Setoran kas dicocokkan dengan dana bank | Status setoran berubah tanpa menambah penerimaan siswa | Belum diuji |

Pelaksanaan setiap kasus dicatat mulai dari prasyarat dan langkah pengujian sampai masukan, keluaran yang diharapkan, hasil aktual, serta bukti yang diperoleh. Masalah yang ditemukan dikelompokkan menurut dampaknya terhadap fungsi. Akses cabang tanpa kewenangan, pembayaran yang dihitung ganda, dan pelampauan kapasitas diperlakukan sebagai galat kritis.

Fungsi yang gagal diuji diperbaiki, kemudian diperiksa kembali dengan kasus yang sama dan kasus lain yang berkaitan. Hasil uji ulang dihubungkan dengan versi aplikasi serta hasil sebelumnya. Catatan ini memperlihatkan perubahan dari kondisi awal sampai perbaikan dinyatakan memenuhi kriteria.

### 3.3.7 Evaluasi Iterasi (*Retrospective*)

Evaluasi iterasi dilakukan untuk memahami hasil pekerjaan dan kendala yang muncul selama pengembangan. Pengembang membandingkan rencana dengan waktu aktual, meninjau galat serta perubahan kebutuhan, dan memeriksa tugas yang belum selesai. Hasil pembahasan digunakan untuk menentukan perbaikan cara kerja dan pekerjaan berikutnya.

Catatan pelaksanaan memberi dasar untuk memperbaiki perkiraan waktu dan proses pengembangan, sebagaimana dijelaskan dalam PxP oleh Dzhurov dkk. (2009, hlm. 256). Sidiq dkk. (2025, hlm. 45) juga membahas perubahan kebutuhan serta perbedaan durasi dalam pelaksanaan proyeknya. Karena itu, waktu implementasi dicatat sebagai bagian dari keseluruhan waktu pengembangan agar penyebab perbedaannya dapat dipahami.

Unsur yang digunakan dalam evaluasi iterasi dirangkum pada Tabel 3.6. Catatan waktu, galat, perubahan, dan usulan perbaikan diisi selama pekerjaan berlangsung. Dengan pencatatan tersebut, evaluasi menggunakan pengalaman pengerjaan yang masih dapat diperiksa kembali.

**Tabel 3.6 Unsur Dokumentasi Evaluasi Iterasi**

| Dokumen | Unsur yang dicatat | Penggunaan analisis |
| :--- | :--- | :--- |
| Catatan waktu | Kode tugas, kategori, estimasi, waktu mulai, waktu selesai, dan durasi aktual | Selisih estimasi dan aktual beserta penyebabnya |
| Catatan galat | Kode galat, versi, pemicu, tingkat kepentingan, perbaikan, dan uji ulang | Galat terbuka, galat terselesaikan, dan pola kesalahan |
| Catatan perubahan | Asal permintaan, kebutuhan terdampak, keputusan, dan perubahan jadwal | Perubahan ruang lingkup dan tindak lanjut |
| Usulan perbaikan proses | Masalah, bukti, tindakan, dan hasil pemeriksaan berikutnya | Penyesuaian cara kerja pada iterasi selanjutnya |

Perbandingan waktu dilakukan pada tugas yang sama dengan mengurangkan estimasi dari durasi aktual. Selisihnya kemudian dibahas bersama penyebab yang tercatat selama pengerjaan. Penjelasan ini membantu membedakan pengaruh perubahan kebutuhan dari waktu yang digunakan untuk memperbaiki kesalahan kode.

Hasil evaluasi digunakan untuk menyusun perkiraan yang lebih sesuai, menata pekerjaan yang tersisa, dan memperbaiki pengujian pada iterasi berikutnya. Formulir lengkap catatan waktu, galat, perubahan, serta evaluasi disimpan pada lampiran pelaksanaan. Bagian utama laporan menyajikan hasil yang diperlukan untuk menjelaskan perkembangan proses.

### 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi

Pengujian penerimaan pengguna atau *User Acceptance Testing* (UAT) memberi kesempatan kepada petugas cabang dan pengelola pusat untuk mencoba alur kerja ARTHA. Peserta dipilih secara bertujuan dengan mempertimbangkan kewenangan, pengalaman menjalankan tugas, kesediaan, dan proses yang akan dinilai. Pemilihan ini menghubungkan kegiatan evaluasi dengan pekerjaan pengguna sistem.

Peserta direncanakan mewakili Admin Cabang dan Super Admin, dengan jumlah, nama, cabang, serta waktu pelaksanaan yang akan disepakati bersama mitra. Seorang peserta dapat menjalankan beberapa tugas sesuai kewenangannya. Hasil evaluasi akan dijelaskan menurut peran dan cabang yang terwakili agar cakupan penerimaannya terlihat.

Sebelum pengguna mencoba aplikasi, pengembang menyiapkan versi uji, cadangan data awal, akun menurut peran, data simulasi, dan panduan singkat. Fungsi utama serta hak akses diperiksa lebih dahulu agar peserta dapat mengikuti tugas yang diberikan. Persiapan ini juga menyediakan kondisi awal yang sama ketika suatu tugas perlu diulang.

Pelaksanaan UAT diawali dengan penjelasan tujuan, data yang digunakan, serta persetujuan pencatatan bukti. Peserta kemudian menjalankan tugas, sementara pengembang mengamati hasil dan mencatat kesulitan maupun bantuan yang diberikan. Jika langkah tugas perlu disesuaikan selama pelaksanaan, perubahan tersebut dicatat bersama hasilnya.

Tabel 3.7 merangkum tugas UAT berdasarkan pekerjaan masing-masing peran, dengan A menunjukkan Admin Cabang dan S menunjukkan Super Admin. Lembar pelaksanaannya memuat identitas atau kode peserta, versi aplikasi, langkah, hasil aktual, bantuan, keputusan, alasan, dan bukti. Catatan tersebut digunakan untuk membahas penerimaan setiap alur kerja.

**Tabel 3.7 Rancangan Tugas Penerimaan Berdasarkan Kebutuhan**

| Kode | Peran | Tugas | Dasar penerimaan |
| :--- | :--- | :--- | :--- |
| UAT-01 | A dan S | Masuk, memeriksa cakupan akses, dan keluar | Akun sesuai peran dan data cabang lain terlindungi |
| UAT-02 | A | Mendaftarkan dan memperbarui siswa | Data wajib benar dan riwayat tetap tersedia |
| UAT-03 | A dan S | Menyiapkan kelas serta ruang | Batas kelas sesuai ruang dan parameter terlihat |
| UAT-04 | A | Menambah peserta, memeriksa penuh, lalu mengakhiri keanggotaan | Penambahan ditolak saat penuh dan tempat kembali tersedia setelah keluar |
| UAT-05 | A | Menyusun serta menyunting jadwal | Irisan relevan ditampilkan tanpa benturan dengan jadwal sendiri |
| UAT-06 | A dan S | Memilih tarif dan menerbitkan tagihan periode | Tarif tepat dan tagihan tidak terbit ganda |
| UAT-07 | A | Mencatat uang tunai dan mencetak kuitansi | Penerimaan sah tercatat satu kali |
| UAT-08 | A | Mengajukan transfer untuk beberapa tagihan siswa yang sama | Alokasi benar dan pengajuan belum melunasi tagihan |
| UAT-09 | S | Memeriksa transfer, mengembalikan, atau menyetujui | Keputusan dan referensi dana masuk dapat ditelusuri |
| UAT-10 | A | Membuka pesan WhatsApp dari tunggakan | Nomor, periode, nominal, dan jatuh tempo sesuai |
| UAT-11 | A dan S | Menyerahkan serta menerima setoran tunai | Daftar pembayaran sumber dan petugas tercatat |
| UAT-12 | A dan S | Menelusuri ringkasan ke transaksi sumber | Total, periode, cabang, dan status sesuai |
| UAT-13 | S | Mencocokkan penerimaan dengan contoh mutasi | Referensi tidak dipakai ganda dan setoran tidak menjadi pendapatan baru |
| UAT-14 | S | Mengelola akun dan data induk | Perubahan hanya dilakukan petugas berwenang |

Sebelum digunakan, instrumen UAT ditinjau bersama pembimbing dan perwakilan mitra untuk memastikan langkahnya dapat dipahami dan sesuai dengan kebutuhan yang dinilai. Keterlibatan pengguna dalam evaluasi pengembangan PxP dijelaskan oleh Apriyanti dkk. (2024, hlm. 3683 sampai 3685). Pada ARTHA, keterlibatan tersebut diwujudkan melalui tugas administrasi yang dapat dicoba dan diamati hasilnya.

Hasil setiap tugas ditetapkan sebagai diterima, memerlukan perbaikan, atau belum dapat dievaluasi, dengan alasan yang dicatat pada lembar pelaksanaan. Kendala akibat data yang belum tersedia dibahas terpisah dari kesalahan fungsi aplikasi. Setelah perbaikan dilakukan, tugas terkait dijalankan kembali pada versi yang dicantumkan.

Hasil pengujian sistem dirangkum dengan menunjukkan jumlah kasus yang direncanakan, telah dijalankan, lulus, gagal, dan belum dijalankan. Persentase kelulusan dihitung dari kasus yang lulus dibandingkan kasus yang dijalankan. Cakupan pengujian dihitung dari kasus yang dijalankan terhadap seluruh kasus yang direncanakan, sehingga kedua ukuran menjelaskan hal yang berbeda.

Analisis UAT disusun menurut pelaksanaan tugas pada setiap peserta dan versi aplikasi. Persentase penerimaan dihitung dari pelaksanaan tugas yang diterima dibandingkan pelaksanaan tugas yang telah dievaluasi. Tugas yang belum dievaluasi dan hasil pengujian ulang dilaporkan tersendiri untuk melengkapi gambaran penerimaan pengguna.

Keputusan penerimaan menyeluruh mempertimbangkan penyelesaian tugas penting dan penanganan galat kritis yang masih terbuka. Hasilnya dibahas menurut integrasi fungsi, pemantauan penerimaan, dan kesesuaian dengan kebutuhan pengguna. Pembahasan mengikuti data evaluasi yang dikumpulkan, sedangkan kesimpulan tentang penghematan waktu memerlukan pengukuran pembanding tersendiri.

Setelah masukan UAT ditindaklanjuti, pengembang menyiapkan versi serah uji beserta panduan penggunaan, daftar keterbatasan, prosedur pencadangan, dan berita acara evaluasi. Bahan tersebut menjelaskan kondisi prototipe ketika diserahkan serta pekerjaan yang masih perlu dilanjutkan. Pemakaian untuk operasional kemudian ditentukan bersama mitra sesuai hasil evaluasi dan kesiapan penggunaannya.

## 3.4 Konsep Prototipe

Konsep prototipe menjelaskan bagaimana kegiatan administrasi Artha diterjemahkan menjadi fungsi, pembagian peran, dan hubungan data dalam sistem. Rancangan ini menghubungkan kebutuhan yang telah ditelusuri dengan pilihan proses serta tampilan yang akan dikembangkan. Bagian yang masih memerlukan keputusan operasional dibahas bersama mitra melalui matriks kebutuhan dan contoh alur kerja.

### 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan

Dalam rancangan ARTHA, pencatatan pada cabang dihubungkan dengan kebutuhan pengelola pusat untuk melihat dan menelusuri penerimaan. Data yang dimasukkan admin digunakan kembali dalam pemeriksaan pembayaran serta penyusunan rekap. Kajian penerimaan SPP pada Hendri dkk. (2025, hlm. 124 sampai 125) menjadi rujukan untuk memahami pencatatan dan penelusuran bukti pada proses tersebut.

Tabel 3.8 memperlihatkan hubungan antara proses berjalan yang ditelusuri dan alur yang diusulkan dalam sistem. Perbandingan ini membantu menjelaskan perubahan pekerjaan dari pencatatan cabang menuju penggunaan data terpusat. Rincian kebijakan pembayaran dan penetapan pemeriksa akan dibahas dengan pihak yang mempunyai kewenangan rekening.

**Tabel 3.8 Proses Berjalan dan Proses Usulan**

| Proses | Dasar yang ditelusuri | Rancangan usulan |
| :--- | :--- | :--- |
| Pendaftaran | Catatan siswa dan pilihan layanan pada cabang | Identitas siswa terpusat dengan pembatasan akses cabang |
| Kelas | Pemeriksaan peserta dan ruang oleh petugas | Hitungan peserta aktif, peringatan hampir penuh, dan penolakan saat penuh |
| Jadwal | Catatan serta komunikasi pengelola | Pemeriksaan irisan tentor dan ruang menurut hari, waktu, serta masa berlaku |
| Penagihan | Jatuh tempo dan pengingat oleh admin | Daftar tunggakan, pratinjau pesan, serta tombol WhatsApp manual |
| Transfer | Bukti disampaikan kepada pihak pengelola | Pengajuan Admin Cabang, pemeriksaan dana masuk, dan keputusan Super Admin |
| Tunai dan setoran | Penerimaan cabang dan penyerahan kepada pusat | Pembayaran siswa, penyerahan kas, serta setoran bank dicatat terpisah |
| Pelaporan | Penghimpunan catatan cabang | Rekap berdasarkan transaksi sah, periode, kanal, dan cabang historis |

Ketika menerima pembayaran, admin memilih satu atau beberapa tagihan milik siswa pada cabang transaksi yang sama. Sistem mencatat penerimaan sebagai satu transaksi, kemudian membaginya ke dalam rincian alokasi tagihan. Jumlah seluruh alokasi harus sama dengan nominal pembayaran agar kewajiban yang dilunasi dan uang yang diterima tetap sesuai.

Pengajuan transfer dimulai dengan pencatatan rincian pembayaran dan unggahan bukti oleh admin. Selama menunggu verifikasi, nominal tersebut belum mengurangi sisa tagihan. Pemeriksa menyetujui pengajuan setelah dana masuk sesuai, atau mengembalikannya disertai alasan; perbaikan kemudian diajukan melalui transaksi baru yang tetap terhubung dengan pengajuan lama.

Pada pembayaran tunai, admin menyelesaikan pencatatan setelah uang diterima sehingga penerimaan dan alokasi tagihannya dapat diproses. Rancangan awal menggunakan pelunasan sebesar sisa kewajiban pada setiap tagihan yang dipilih. Jika mitra menetapkan kebijakan cicilan, aturan pembayaran sebagian akan ditambahkan setelah ketentuannya diperjelas.

Kas yang diterima cabang dapat dihimpun untuk diserahkan ke pusat dengan mencantumkan pembayaran sumber, penyerah, penerima, dan waktu penerimaan. Ketika uang tersebut disetorkan ke bank, rekening tujuan, bukti, serta waktu setornya dicatat sebagai tahap berikutnya. Kedua tahap menggambarkan perpindahan dana yang sama, sehingga nilainya tidak dihitung kembali sebagai penerimaan siswa.

Pencocokan pada prototipe menghubungkan satu dana masuk bank dengan satu transfer siswa atau satu setoran kas yang nominal penuhnya sama. Setelah petugas memeriksa kesesuaian tersebut, referensi bank dihubungkan dengan transaksi sumber. Dana gabungan, selisih biaya, dan pencocokan sebagian dicatat untuk tindak lanjut karena penanganannya berada di luar cakupan pencocokan awal.

Hubungan pencatatan pusat dan cabang dipelajari melalui Ramadhan dan Widodo (2026, bagian pembahasan), sedangkan pencocokan catatan internal dengan bank merujuk Sudirman dan Tristianti (2021, hlm. 126 sampai 127). Kedua rujukan membantu menjelaskan kebutuhan rekap serta pemeriksaan dana pada ARTHA. Dalam penyajiannya, sisa kewajiban siswa dipisahkan dari selisih pencocokan agar informasi penagihan dan penerimaan dapat dibaca dengan tepat.

### 3.4.2 Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional menggambarkan pekerjaan yang perlu dilayani sistem, mulai dari pengelolaan siswa sampai pemantauan penerimaan. Setiap kebutuhan dirumuskan bersama keluaran yang diharapkan agar dapat diterjemahkan ke dalam rancangan dan pengujian. Daftar kebutuhan tersebut disajikan pada Tabel 3.9.

**Tabel 3.9 Rancangan Kebutuhan Fungsional**

| Kode | Fungsi | Hasil yang diharapkan |
| :--- | :--- | :--- |
| KF-01 | Autentikasi dan kewenangan | Akses berdasarkan peran serta cabang; sesi dapat diakhiri |
| KF-02 | Pengelolaan siswa | Identitas, kontak wali, jenjang termasuk TK, dan status tercatat |
| KF-03 | Pengelolaan kelas dan ruang | Kapasitas kelompok, kapasitas ruang, serta ambang hampir penuh tersedia |
| KF-04 | Keanggotaan dan kapasitas | Peserta aktif dihitung, kelas penuh ditolak, dan keluar membuka tempat |
| KF-05 | Pengelolaan jadwal | Irisan tentor dan ruang diperiksa menurut masa berlaku |
| KF-06 | Tarif dan tagihan | Variasi cabang, sesi, siklus, potongan berwenang, dan periode tersimpan |
| KF-07 | Penerimaan tunai | Penerimaan, alokasi tagihan, dan kuitansi dicatat satu kali |
| KF-08 | Pengajuan transfer | Bukti dan alokasi diajukan tanpa langsung melunasi tagihan |
| KF-09 | Pemeriksaan transfer | Persetujuan atau pengembalian beserta riwayat keputusan tersimpan |
| KF-10 | Tautan WhatsApp | Nomor dan pesan tunggakan disiapkan untuk dikirim oleh admin |
| KF-11 | Setoran tunai | Penyerahan ke pusat dibedakan dari penyetoran ke rekening |
| KF-12 | Dasbor dan laporan | Data cabang serta antrean pemeriksaan ditelusuri ke transaksi sumber |
| KF-13 | Pencocokan penerimaan | Transfer atau setoran dihubungkan ke referensi bank secara manual |
| KF-14 | Data induk dan akun | Tahun ajaran, cabang, akun, tentor, mapel, dan rekening diatur berwenang |

Pada penjadwalan, pengelola menyusun penugasan tentor dan ruang dengan bantuan informasi tentang waktu yang beririsan. Calon jadwal yang berkonflik dapat disimpan nonaktif untuk ditinjau, sementara ketentuan pengaktifan pengecualian akan ditetapkan bersama mitra. Penelitian Khafidhoh dkk. (2026, hlm. 15 sampai 16, 19) menjadi rujukan kebutuhan penjadwalan bimbel; rancangan ARTHA menggunakan pemeriksaan konflik tanpa mengadopsi penyusunan jadwal otomatis dengan algoritma genetika.

Ketersediaan kelas ditentukan dengan membandingkan jumlah anggota aktif dan batas peserta yang ditetapkan. Pemeriksaan kapasitas serta irisan waktu mempunyai rujukan pada Kabisatullah dan Noprisson (2026, hlm. 94). Pada ARTHA, nilai kapasitas dan aturan penambahan siswa mengikuti kebutuhan kelas serta ketentuan mitra.

Pengelola menentukan ambang hampir penuh berdasarkan sisa tempat yang ingin ditampilkan sebagai peringatan. Nilainya berada pada rentang satu sampai kapasitas kelas, sedangkan kondisi penuh ditentukan ketika jumlah peserta aktif mencapai batas tersebut. Indikator keterisian ini ditampilkan terpisah dari status operasional kelas agar kelas aktif atau ditutup tetap dapat dibedakan.

Jumlah peserta diperiksa kembali oleh peladen ketika penempatan disimpan. Langkah ini diperlukan karena kelas yang masih tersedia saat halaman dibuka dapat terisi oleh petugas lain sebelum penyimpanan selesai. Apabila dua petugas menambahkan siswa secara bersamaan, sistem menggunakan keadaan terbaru untuk menjaga jumlah peserta tetap dalam kapasitas.

Pesan penagihan disusun dari data siswa, periode, sisa tagihan, dan tanggal jatuh tempo yang dipilih admin. Nomor wali menggunakan format internasional, sedangkan isi pesan dikodekan agar dapat dibuka melalui tautan WhatsApp. Pembentukan tautan mengikuti mekanisme *click to chat* pada dokumentasi WhatsApp (WhatsApp, t.t.).

Saat admin memilih tombol WhatsApp, sistem mencatat permintaan pembukaan tautan untuk membantu penelusuran tindak lanjut tagihan. Admin kemudian memeriksa percakapan dan mengirim pesan melalui WhatsApp. Karena pengiriman berlangsung di luar ARTHA, catatan tindakan tersebut tidak menunjukkan apakah pesan telah terkirim, diterima, atau dibaca.

Selain fungsi operasional, rancangan memperhatikan cara sistem membatasi akses, menjaga data, dan menyajikan informasi kepada pengguna. Kebutuhan nonfungsional pada Tabel 3.10 menjadi dasar pemeriksaan aspek tersebut. Target kinerja yang memerlukan ukuran kuantitatif akan ditetapkan sebelum pengukuran dilakukan.

**Tabel 3.10 Rancangan Kebutuhan Nonfungsional**

| Kode | Aspek | Kriteria pemeriksaan |
| :--- | :--- | :--- |
| KNF-01 | Pembatasan akses | Akun cabang tidak memperoleh data cabang lain melalui halaman maupun permintaan layanan |
| KNF-02 | Integritas transaksi | Pengiriman ulang permintaan tidak menyebabkan pembayaran atau keanggotaan tercatat ganda |
| KNF-03 | Ketertelusuran | Pengajuan, keputusan, perubahan, dan petugas terkait dapat diperiksa |
| KNF-04 | Kerahasiaan bukti | Berkas pembayaran tidak tersedia melalui tautan publik tanpa pemeriksaan kewenangan |
| KNF-05 | Kemudahan penggunaan | Tugas UAT dapat dijalankan sesuai alur peran dan kesalahan masukan dijelaskan |
| KNF-06 | Kesesuaian tampilan | Fungsi inti dapat digunakan pada ukuran layar komputer dan telepon yang diuji |
| KNF-07 | Konsistensi data | Ringkasan sesuai transaksi sumber pada periode dan status yang sama |
| KNF-08 | Pemulihan | Cadangan data dan berkas dapat dipulihkan pada lingkungan uji |
| KNF-09 | Kinerja | Waktu tanggapan fungsi inti diukur dengan kondisi perangkat, jaringan, dan jumlah data yang dicatat |

### 3.4.3 Peran Pengguna dan Matriks Hak Akses

Hak akses dibagi menurut pekerjaan pengguna dan cabang yang menjadi tanggung jawabnya. Pemisahan data cabang serta akses pemantauan pusat dibahas pada Ahadi dkk. (2025, hlm. 764 sampai 765) dan Thiovanda (2026, hlm. 4). Dalam ARTHA, pembagian tersebut diterapkan melalui peran Admin Cabang dan Super Admin.

Tabel 3.11 menunjukkan fungsi yang dapat dijalankan setiap peran dan cakupan data yang dapat diakses. Pembagian ini menjadi acuan pada halaman aplikasi maupun layanan pengolahan data. Kewenangan keuangan yang masih perlu ditetapkan akan dibahas bersama mitra sebelum alur pembayaran diterapkan.

**Tabel 3.11 Matriks Hak Akses Pengguna**

| Fungsi | Admin Cabang | Super Admin |
| :--- | :--- | :--- |
| Siswa dan keanggotaan | Mengelola sesuai cabang penugasan | Memantau seluruh cabang dan melakukan koreksi berwenang |
| Kelas dan jadwal | Mengelola pada cabangnya sesuai aturan | Memantau lintas cabang dan menangani penyesuaian berwenang |
| Tarif dan parameter kelas | Menggunakan tarif; mengelola kelas sesuai penugasan | Menetapkan tarif, kapasitas, dan ambang sesuai kewenangan |
| Penerimaan tunai | Mencatat penerimaan dan menyiapkan setoran | Memeriksa rekap serta penerimaan setoran |
| Transfer siswa | Mengajukan bukti dan membuat pengajuan ulang yang tertaut | Memeriksa dana masuk serta menyetujui atau mengembalikan |
| Tautan WhatsApp | Mengakses tagihan serta nomor wali pada cabangnya | Memantau tindak lanjut tanpa perlu mengirim pesan berulang |
| Dasbor | Melihat data cabangnya | Melihat agregat dan rincian seluruh cabang |
| Akun pengguna | Menggunakan akun yang diberikan | Membuat, menonaktifkan, dan mengatur penugasan akun |

Sistem memeriksa peran yang diberikan pada akun dan hubungan pengguna dengan objek data pada setiap permintaan. Identitas cabang membantu menentukan cakupan akses, tetapi nilai cabang yang kosong tidak memberikan hak Super Admin. Dengan pemeriksaan tersebut, izin mengikuti penugasan yang sah.

Tentor dan wali murid terlibat dalam proses operasional sebagai sumber data penjadwalan dan tujuan komunikasi. Dalam rancangan inti, keduanya tidak memerlukan akun dasbor. Admin mengelola penugasan tentor dan menggunakan nomor wali untuk menjalankan komunikasi yang berkaitan dengan tagihan.

### 3.4.4 Cerita Pengguna (*User Story*) dan Kriteria Penerimaan

Cerita pengguna menjelaskan fungsi dari sudut pandang orang yang akan menjalankannya, dengan menghubungkan tindakan dan manfaat yang dibutuhkan. Setiap cerita dilengkapi kriteria penerimaan untuk memperjelas hasil yang akan diperiksa. Bentuk penyusunannya merujuk Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105), sedangkan cerita pada Tabel 3.12 disesuaikan dengan pekerjaan pengguna ARTHA.

**Tabel 3.12 Cerita Pengguna dan Kriteria Penerimaan**

| Kode | Peran dan tindakan | Manfaat | Kriteria penerimaan |
| :--- | :--- | :--- | :--- |
| US-01 | Pengguna masuk dan keluar sesuai peran | Akses data sesuai tugas | Akses Admin Cabang ke cabang lain ditolak; Super Admin sesuai kewenangan; sesi keluar tidak dapat dipakai |
| US-02 | Admin mendaftarkan serta memperbarui siswa | Data siswa dapat ditelusuri | Data wajib lengkap; penonaktifan tidak menghapus transaksi |
| US-03 | Admin menyiapkan kelas; Super Admin menetapkan ruang dan kapasitas | Batas peserta terlihat sebelum penempatan | Kapasitas kelas sesuai ruang dan ambang sisa tempat tersimpan |
| US-04 | Admin mengelola masuk dan keluar kelas | Tempat tersedia serta riwayat benar | Penuh menolak penambahan; keluar membuka satu tempat |
| US-05 | Admin menyusun jadwal | Potensi irisan diketahui | Konflik tentor lintas cabang dan ruang terkait ditampilkan |
| US-06 | Super Admin menetapkan tarif dan Admin menerbitkan tagihan | Kewajiban mengikuti ketentuan berlaku | Cabang, sesi, periode, potongan, serta nilai historis tepat |
| US-07 | Admin menerima pembayaran tunai | Penerimaan sah dan kuitansi tercatat | Total alokasi benar dan pengiriman ulang tidak menggandakan transaksi |
| US-08 | Admin mengajukan transfer | Bukti dapat diperiksa pusat | Status menunggu; beberapa tagihan satu siswa dialokasikan dengan benar |
| US-09 | Super Admin memeriksa transfer | Dana masuk terkonfirmasi | Persetujuan dengan referensi unik; pengembalian mempunyai alasan |
| US-10 | Admin membuka pesan tunggakan | Pesan sesuai kewajiban siswa | Nomor, periode, nominal, dan jatuh tempo benar; pengiriman manual |
| US-11 | Admin menyerahkan dan pusat menerima kas | Perpindahan dana dapat ditelusuri | Penerimaan pusat dibedakan dari penyetoran bank |
| US-12 | Pengguna menelusuri dasbor sesuai kewenangan | Ringkasan mempunyai transaksi sumber | Pengajuan tertunda terpisah dan cabang historis tidak berubah |
| US-13 | Super Admin mencocokkan penerimaan | Dana yang cocok dapat dikenali | Satu referensi bank tidak digunakan untuk dua sumber |
| US-14 | Super Admin mengelola data induk dan akun | Akses serta parameter dasar terkendali | Perubahan berwenang tercatat tanpa menghapus riwayat |

Tabel 3.13 menghubungkan kebutuhan dengan sumber, cerita pengguna, *use case*, iterasi, dan kelompok pemeriksaannya. Pemetaan ini membantu mengikuti satu kebutuhan sejak dirumuskan sampai diuji. Seluruh kebutuhan termasuk lingkup inti, dengan urutan pengerjaan mengikuti ketergantungan pada Tabel 3.4.

**Tabel 3.13 Keterlacakan Kebutuhan sampai Evaluasi**

| Kebutuhan | Sumber | Cerita | Use case | Iterasi | Pemeriksaan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KF-01 | S-02/S-05 | US-01 | UC-00 | I-01 | PU-01; UAT-01 |
| KF-02 | S-01/S-04 | US-02 | UC-01 | I-01 | PU-02; UAT-02 |
| KF-03 | S-04/S-06 | US-03 | UC-02 | I-01 | PU-03; UAT-03 |
| KF-04 | S-06 | US-04 | UC-03 | I-02 | PU-04; UAT-04 |
| KF-05 | S-02/S-04/S-05 | US-05 | UC-04 | I-02 | PU-05; UAT-05 |
| KF-06 | S-01/S-03/S-04 | US-06 | UC-05 | I-01 | PU-06; UAT-06 |
| KF-07 | S-03/S-04 | US-07 | UC-06 | I-03 | PU-07; UAT-07 |
| KF-08 | S-03/S-06/S-07 | US-08 | UC-07 | I-03 | PU-08; UAT-08 |
| KF-09 | S-03/S-06/S-07 | US-09 | UC-08 | I-03 | PU-09; UAT-09 |
| KF-10 | S-04/S-06 | US-10 | UC-09 | I-03 | PU-10; UAT-10 |
| KF-11 | S-03/S-04/S-07 | US-11 | UC-10 | I-04 | PU-11; UAT-11 |
| KF-12 | S-02/S-03 | US-12 | UC-12 | I-04 | PU-12; UAT-12 |
| KF-13 | S-03/S-07 | US-13 | UC-11 | I-04 | PU-13; UAT-13 |
| KF-14 | S-02/S-05/S-07 | US-14 | UC-13 | I-01 | PU-14; UAT-14 |

Setiap kelompok PU memuat kondisi normal, pengecualian, serta keadaan batas yang perlu diperiksa pada fungsi terkait. Rincian kasusnya dijabarkan melalui kode BB dan dihubungkan dengan tabel sumber, bukti pelaksanaan, serta status validasi pada lampiran keterlacakan. Dengan hubungan ini, pengembang dapat melihat bagian kebutuhan yang sudah diperiksa dan yang masih perlu diuji.

### 3.4.5 Pemodelan Kasus Penggunaan (*Use Case*) dan Skenario

Pemodelan kasus penggunaan atau *use case* memperlihatkan hubungan antara pengguna dan fungsi yang mereka jalankan di dalam sistem. Penggunaan model ini merujuk Ahadi dkk. (2025, hlm. 765). Diagram ARTHA pada Gambar 3.2 menyajikan tujuan pengguna yang kemudian dijelaskan lebih lanjut melalui skenario.

![Use case inti sistem ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_2_Use_Case_Inti.png>)

**Gambar 3.2 Diagram Kasus Penggunaan Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan ARTHA.

Rancangan mencakup empat belas kasus penggunaan, yaitu UC-00 sampai UC-13, yang melibatkan Admin Cabang dan Super Admin. Contoh alur lintas peran ditunjukkan pada Tabel 3.14 melalui proses pengajuan serta pemeriksaan transfer. Skenario lengkap dan peta perubahan kode sebelumnya tersedia pada dokumen use case pendamping.

**Tabel 3.14 Skenario Pengajuan dan Pemeriksaan Transfer**

| Unsur | Rancangan |
| :--- | :--- |
| Identitas | UC-07 pengajuan transfer dan UC-08 pemeriksaan transfer |
| Pelaksana | Admin Cabang sebagai pengaju; Super Admin sebagai pemeriksa berwenang |
| Prasyarat | Akun sah, tagihan tersedia, rekening resmi aktif, dan kewenangan pemeriksa telah ditetapkan |
| Pengajuan | Pilih tagihan satu siswa serta cabang, isi nominal, tanggal dan rekening, unggah bukti, lalu kirim |
| Keadaan antara | Status menunggu verifikasi; tagihan belum dilunasi dan antrean tampil pada dasbor |
| Pemeriksaan | Bandingkan identitas, nominal, rekening, dan tanggal dengan referensi dana masuk yang dicatat manual |
| Persetujuan | Kunci transaksi terkait, periksa ulang sisa tagihan serta referensi, lalu simpan keputusan dan pencocokan satu kali |
| Pengembalian | Simpan alasan; perbaikan menghasilkan pengajuan baru dengan tautan ke pengajuan lama |
| Pengecualian | Bukti tidak terbaca, nominal berbeda, referensi sudah digunakan, sisa tagihan berubah, atau akses tidak berwenang |
| Pascakondisi | Riwayat tersimpan; hanya pembayaran terkonfirmasi mengurangi sisa; kuitansi final terbit setelah persetujuan |

Diagram menampilkan tujuan pengguna, sementara langkah pemeriksaan formulir dan kewenangan dijelaskan di dalam skenario. Setiap skenario memuat alur normal serta pengecualian yang mungkin dihadapi ketika fungsi dijalankan. Pembagian ini membuat hubungan pengguna dengan sistem tetap mudah dibaca tanpa menghilangkan aturan akses pada setiap tindakan.

### 3.4.6 Perancangan Basis Data

Penyimpanan data ARTHA dirancang secara terpusat dengan dua puluh tiga tabel yang saling berhubungan. Identitas, keanggotaan kelas, tagihan, pembayaran, serta perpindahan dana dipisahkan agar perubahan pada satu proses tetap dapat ditelusuri dalam riwayatnya. Hubungan data utama ditampilkan pada Gambar 3.3, sedangkan ERD lengkap dan kamus data disediakan pada dokumen basis data pendamping.

![Hubungan konseptual data ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_3_Model_Data_Konseptual.png>)

**Gambar 3.3 Hubungan Data Utama Prototipe ARTHA**

Sumber: rancangan penelitian berdasarkan pemisahan proses operasional.

Tabel 3.15 mengelompokkan tabel berdasarkan kegiatan yang dilayaninya. Pada pembayaran, hubungan dengan tagihan dicatat melalui rincian alokasi agar satu penerimaan dapat digunakan untuk beberapa tagihan siswa yang sama. Pengelompokan ini membantu menjelaskan fungsi masing-masing data dalam alur operasional.

**Tabel 3.15 Kelompok Tabel dan Hubungan Utama**

| Kelompok | Tabel | Hubungan utama |
| :--- | :--- | :--- |
| Periode dan kewenangan | `academic_years`, `branches`, `users` | Tahun ajaran, cabang penugasan, dan peran pengguna |
| Identitas dan kompetensi | `students`, `mentors`, `subjects`, `mentor_subjects` | Kontak wali serta satu identitas tentor untuk pemeriksaan lintas cabang |
| Kelas dan jadwal | `class_rooms`, `classes`, `class_schedules`, `class_enrollments` | Ruang fisik, kelompok, masa jadwal, serta riwayat keanggotaan |
| Kewajiban | `fee_tariffs`, `bills` | Tarif menurut cabang, sesi, dan siklus; tagihan menyimpan nilai aktual |
| Penerimaan | `payments`, `payment_allocations`, `payment_reviews` | Induk pembayaran, pembagian ke tagihan, dan keputusan pemeriksaan |
| Perpindahan kas | `cash_batches`, `cash_batch_items` | Satu kelompok penyerahan memuat pembayaran tunai sumber |
| Pencocokan bank | `bank_accounts`, `bank_entries`, `bank_matches` | Rekening resmi, dana masuk manual, dan satu sumber yang dicocokkan |
| Ketertelusuran | `reminder_actions`, `activity_logs` | Tindakan membuka WhatsApp serta perubahan penting oleh petugas |

Atribut dan aturan yang memengaruhi ketepatan pencatatan dirangkum pada Tabel 3.16. Jumlah peserta aktif, sisa tagihan, keterlambatan, serta ringkasan penerimaan dihitung dari data yang menjadi sumbernya. Dengan cara ini, informasi yang ditampilkan tetap mengikuti perubahan pada keanggotaan dan transaksi.

**Tabel 3.16 Atribut dan Kendala Kritis Rancangan Data**

| Objek | Atribut atau hubungan penting | Kendala rancangan |
| :--- | :--- | :--- |
| Pengguna | Peran, cabang penugasan, status | Cabang kosong tidak memberikan hak Super Admin |
| Kelas | `max_students`, `near_full_remaining` | Peserta aktif tidak melebihi kapasitas; ambang belum diisi dengan angka kebijakan tanpa validasi |
| Keanggotaan | Siswa, kelas, waktu masuk, waktu keluar, alasan | Tidak ada dua keanggotaan aktif siswa pada kelas yang sama; masuk kembali membuat riwayat baru |
| Jadwal | Hari, jam, rentang tanggal, tentor, ruang, status | Periksa masa berlaku, cabang ruang, irisan, dan pengecualian jadwal yang disunting |
| Tagihan | Cabang historis, periode, tarif, nilai, potongan beralasan | Periode tidak ganda dan perubahan tarif tidak mengubah tagihan lama |
| Pembayaran | Siswa, cabang historis, kanal, status, pengajuan asal | Pengajuan ulang tertaut; pengajuan menunggu atau dikembalikan belum menjadi penerimaan |
| Alokasi | Pembayaran, tagihan, nominal | Siswa serta cabang sama; total sesuai pembayaran dan tidak melebihi sisa sah |
| Pemeriksaan | Pengajuan, petugas, keputusan, waktu, alasan | Riwayat tidak ditimpa dan keputusan final hanya berlaku sekali |
| Pencocokan | Dana masuk dan salah satu sumber | Sumber berupa transfer atau setoran; nominal penuh sama dan referensi tidak dipakai ganda |

Siswa ditempatkan pada kelas aktif yang memiliki jadwal serta ruang dengan kapasitas memadai. Jika ruang atau batas kelas diubah, sistem memeriksa kembali kesesuaiannya dengan jumlah peserta aktif. Pemeriksaan dan penyimpanan dilakukan dalam transaksi yang sama agar perubahan tetap menjaga ketersediaan tempat.

Cabang pemilik tagihan dan pembayaran disimpan sesuai keadaan ketika transaksi dicatat. Riwayat penerimaan karena itu tetap berada pada cabang asal meskipun profil siswa kemudian berpindah cabang. Sisa tagihan dihitung dari kewajiban dikurangi alokasi pembayaran sah, sementara penanda lewat jatuh tempo ditentukan terpisah dari tingkat pelunasannya.

Skema fisik akan diterapkan pada MySQL dengan mesin transaksi InnoDB. Sebelum digunakan, hubungan kunci, indeks, penguncian, dan batas nilai diperiksa melalui migrasi serta pengujian implementasi. Hasil pemeriksaan tersebut digunakan untuk memastikan rancangan penyimpanan bekerja sesuai kebutuhan aplikasi.

### 3.4.7 Perancangan Antarmuka

Rancangan antarmuka mengikuti urutan pekerjaan pengguna agar informasi dan tindakan dapat ditemukan pada halaman yang sesuai. Enam layar inti pada Gambar 3.4 sampai Gambar 3.9 menggambarkan kegiatan administrasi cabang dan pemantauan pusat. Hubungan layar dengan cerita pengguna serta tindakan utamanya dirangkum pada Tabel 3.17.

**Tabel 3.17 Rancangan Antarmuka Inti**

| Layar | Cerita pengguna | Tindakan utama |
| :--- | :--- | :--- |
| Dasbor cabang | US-08, US-10, US-12 | Memilih tindak lanjut transaksi serta keterisian |
| Keanggotaan kelas | US-03, US-04 | Menambah peserta atau mengakhiri keanggotaan |
| Pengajuan transfer | US-08 | Memilih tagihan dan mengirim bukti |
| Pemeriksaan transfer | US-09 | Memeriksa dana masuk dan mengambil keputusan |
| Tunggakan WhatsApp | US-10 | Memeriksa pesan dan membuka WhatsApp |
| Dasbor pusat dan pencocokan | US-11, US-12, US-13 | Menelusuri setoran, penerimaan, dan referensi bank |

Nama, angka, dan transaksi pada gambar menggunakan data simulasi untuk memperlihatkan alur penggunaan. Setiap indikator warna dilengkapi label teks agar keadaan kelas atau pembayaran tetap dapat dipahami. Istilah status juga digunakan secara konsisten dengan skenario dan kamus data.

Dasbor Admin Cabang pada Gambar 3.4 menempatkan tunggakan, pengajuan transfer yang menunggu pemeriksaan, dan keterisian kelas sebagai informasi tindak lanjut. Admin dapat membuka rincian dari ringkasan tersebut untuk melanjutkan pekerjaan pada cabangnya. Susunan ini mendukung pengajuan pembayaran, penagihan, dan penelusuran informasi pada US-08, US-10, serta US-12.

![Dasbor Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_4_Dasbor_Cabang.png>)

**Gambar 3.4 Dasbor Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Pada halaman keanggotaan dalam Gambar 3.5, admin dapat membandingkan jumlah peserta aktif, kapasitas, dan sisa tempat sebelum menempatkan siswa. Peringatan hampir penuh membantu pemilihan kelas, sedangkan tombol penambahan dinonaktifkan ketika penuh. Tindakan mengakhiri keanggotaan mencatat tanggal dan alasan tanpa menghapus siswa, sesuai kebutuhan pada US-03 serta US-04.

![Penempatan dan Keanggotaan Kelas](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_5_Keanggotaan_Kelas.png>)

**Gambar 3.5 Penempatan dan Keanggotaan Kelas**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Formulir pada Gambar 3.6 menghubungkan pengajuan transfer dengan siswa, cabang, tagihan yang dipilih, jumlah alokasi, rekening tujuan, dan bukti pembayaran. Setelah dikirim, pengajuan pada US-08 masuk ke status menunggu verifikasi. Jika pengajuan dikembalikan, formulir perbaikan tetap memperlihatkan hubungannya dengan pengajuan sebelumnya.

![Pengajuan Transfer oleh Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_6_Pengajuan_Transfer.png>)

**Gambar 3.6 Pengajuan Transfer oleh Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Layar Super Admin pada Gambar 3.7 menyandingkan pengajuan transfer dengan rincian dana masuk yang dicatat petugas berwenang. Pada alur US-09 ini, pemeriksa menilai kesesuaian nominal dan referensi sebelum memberikan persetujuan. Apabila pengajuan perlu dikembalikan, alasan wajib diisi agar admin mengetahui bagian yang harus diperbaiki.

![Pemeriksaan Transfer oleh Super Admin](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_7_Pemeriksaan_Transfer.png>)

**Gambar 3.7 Pemeriksaan Transfer oleh Super Admin**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Halaman tunggakan pada Gambar 3.8 menyediakan periode, sisa tagihan, jatuh tempo, nomor wali, dan pratinjau pesan sebelum admin menjalankan US-10. Tombol WhatsApp membuka percakapan dengan pesan terisi untuk diperiksa dan dikirim oleh admin. Sistem mencatat tindakan pembukaan tautan, sedangkan status pengiriman pesan tetap berada di luar pencatatan ARTHA.

![Tunggakan dan Pratinjau Pesan WhatsApp](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_8_Tunggakan_WhatsApp.png>)

**Gambar 3.8 Tunggakan dan Pratinjau Pesan WhatsApp**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Dasbor pusat pada Gambar 3.9 menyajikan tunggakan, penerimaan sah, pengajuan tertunda, dan dana yang telah dicocokkan dalam kelompok informasi yang berbeda. Melalui US-12 dan US-13, petugas dapat membuka sumber transfer atau setoran untuk menelusuri nominal serta referensi banknya. Penelusuran tersebut mempertahankan hubungan dengan pembayaran asal, sehingga setoran tidak dihitung kembali sebagai penerimaan siswa.

![Dasbor Pusat dan Pencocokan Penerimaan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_9_Dasbor_Pusat_Pencocokan.png>)

**Gambar 3.9 Dasbor Pusat dan Pencocokan Penerimaan**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

## 3.5 Spesifikasi Teknis

Spesifikasi teknis menjelaskan perangkat dan komponen yang digunakan untuk mewujudkan rancangan ARTHA. Informasi ini mencakup perangkat lunak, perangkat keras, arsitektur, serta lingkungan pengembangan dan pengujian. Versi dan konfigurasi yang digunakan pada evaluasi akan dicatat sebagai konteks hasil pengujian.

### 3.5.1 Arsitektur Sistem

ARTHA dirancang dengan memisahkan antarmuka web, layanan pengolahan data, dan penyimpanan. Next.js menyajikan halaman pengguna, Laravel menjalankan aturan bisnis serta layanan data, sedangkan MySQL menyimpan data terpusat. Pembagian ini menempatkan pengolahan setiap permintaan pada komponen yang sesuai.

Gambar 3.10 memperlihatkan hubungan pengguna dengan antarmuka, layanan aplikasi, dan penyimpanan data. Diagram juga menunjukkan tindakan yang berlangsung melalui WhatsApp dan pemeriksaan mutasi rekening. Hubungan tersebut menjadi dasar untuk menjelaskan bagian yang diolah aplikasi dan bagian yang tetap dijalankan petugas.

![Arsitektur prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_10_Arsitektur_Prototipe.png>)

**Gambar 3.10 Arsitektur Prototipe Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan akses multicabang dan pemisahan proses pengelolaan data.

Akses pengguna direncanakan menggunakan Laravel Sanctum dengan sesi berbasis kuki untuk antarmuka milik aplikasi sendiri. Konfigurasi domain, perlindungan permintaan, dan masa berlaku sesi disesuaikan dengan lingkungan penerapan. Pengaturannya akan diperiksa sebelum pengujian pengguna dengan merujuk dokumentasi Laravel (Laravel, t.t.-a).

Pengajuan transfer yang belum diputuskan ditampilkan sebagai antrean pada dasbor Super Admin berdasarkan status transaksinya. Antrean ini menjadi tempat pemeriksa menemukan pekerjaan yang perlu ditindaklanjuti. Jika mitra memerlukan penanda notifikasi telah dibaca, fasilitas notifikasi tersimpan Laravel dapat ditambahkan setelah kebutuhan tersebut disepakati (Laravel, t.t.-b).

Dasbor mengambil data terbaru yang tersimpan ketika halaman dibuka atau dimuat kembali setelah tindakan pengguna. Dengan mekanisme ini, istilah waktu nyata merujuk pada informasi terbaru yang diminta dari layanan terpusat. Pembaruan serentak tanpa pemuatan ulang pada semua perangkat belum menjadi mekanisme yang dijanjikan dalam rancangan.

Kebutuhan pembaruan berkala dan batas waktu tanggapan akan dibahas bersama mitra sesuai cara penggunaan dasbor. Hasil pembahasan digunakan untuk menetapkan kriteria penerimaan sebelum pengukuran. Mekanisme yang diterapkan dan waktu tanggapannya kemudian dijelaskan pada bab hasil.

### 3.5.2 Perangkat Keras

Komputer pengembangan digunakan untuk menjalankan penyunting kode, antarmuka web, layanan aplikasi, dan basis data lokal. Kebutuhan perangkat pengguna ditentukan menurut tugas administrasi serta lingkungan evaluasi bersama mitra. Tabel 3.18 merangkum perangkat yang tersedia dan rincian yang masih perlu dilengkapi sebelum pengujian.

**Tabel 3.18 Ketersediaan dan Rencana Perangkat Keras**

| Perangkat | Informasi tersedia | Pelengkapan sebelum pengujian |
| :--- | :--- | :--- |
| Komputer penyusunan | Laptop pengembang berbasis Windows 11 Home 64-bit | AMD Ryzen 5 5600H (6 core, 12 thread, hingga 4,2 GHz), RAM 24 GB DDR4, NVMe SSD 512 GB, dan NVIDIA GeForce RTX 3050 |
| Komputer pengguna | Direncanakan untuk tugas administrasi cabang dan pusat | Perangkat, resolusi, peramban, dan jaringan ditetapkan bersama mitra |
| Telepon uji | Direncanakan untuk tampilan sempit dan tautan WhatsApp | Sistem operasi, ukuran layar, peramban, serta aplikasi WhatsApp dicatat |
| Peladen uji | Diperlukan untuk akses evaluasi mitra | Kapasitas, penyimpanan privat, domain, serta konfigurasi jaringan belum ditetapkan |
| Perangkat cetak | Digunakan jika pencetakan kuitansi masuk tugas evaluasi | Kertas dan pengaturan cetak dikonfirmasi |

Spesifikasi perangkat yang digunakan dicatat bersama kondisi jaringan pada saat pengujian. Catatan tersebut membantu menjelaskan lingkungan tempat fungsi ARTHA dijalankan dan hasilnya diperoleh. Inventaris perangkat pengguna maupun peladen uji akan dilengkapi sesuai perangkat yang dipilih untuk evaluasi.

### 3.5.3 Perangkat Lunak dan Versi Teknologi

Proyek antarmuka `website-artha` telah mempunyai berkas penguncian dependensi yang digunakan untuk mencatat versi komponen. Versi pada Tabel 3.19 diperiksa dari berkas tersebut pada 25 Oktober 2026. Tabel juga menjelaskan pilihan layanan, penyimpanan, dan perangkat pendukung yang akan digunakan dalam pengembangan terintegrasi.

**Tabel 3.19 Pilihan Teknologi dan Status Versi**

| Komponen | Pilihan dan bukti tersedia | Status penggunaan |
| :--- | :--- | :--- |
| Antarmuka | Next.js 16.2.12 dan React 19.2.4 pada `package-lock.json` | Tersedia pada proyek lokal; versi evaluasi dibekukan sebelum UAT |
| Tata tampilan | Tailwind CSS 4.3.3 pada `package-lock.json` | Tersedia pada proyek antarmuka |
| Layanan aplikasi | Laravel 11.x dan PHP 8.3 (tersedia PHP 8.3.30 pada Laragon) | Penyedia layanan data dan RESTful API; dependensi dikelola melalui Composer |
| Autentikasi | Laravel Sanctum berbasis sesi untuk antarmuka milik aplikasi | Direncanakan; konfigurasi domain dan sesi diperiksa pada implementasi |
| Basis data | MySQL Community Server 8.0 dan 8.4 LTS pada Laragon | DBMS dengan mesin InnoDB untuk transaksi atomik dan integritas data |
| Dependensi | Pengelola paket JavaScript dan Composer | Berkas penguncian disimpan bersama versi kode |
| Pengujian | Pengujian unit aturan bisnis serta pengujian layanan dan antarmuka | Perangkat, versi, dan perintah ditetapkan setelah lingkungan layanan tersedia |
| Dokumentasi | Markdown, diagram PNG/SVG, dan pengelola referensi | Sumber diagram serta matriks rancangan disimpan untuk penelusuran |

Konfigurasi lingkungan antarmuka mengikuti kebutuhan instalasi pada dokumentasi resmi Next.js (Vercel, t.t.). Pasangan PHP dan Laravel diperiksa menurut kompatibilitas serta kebijakan dukungannya, kemudian dicatat bersama lingkungan evaluasi (Laravel, t.t.-c). Langkah ini menyamakan acuan versi pada pengembangan dan pengujian.

Berkas dependensi, pengaturan layanan, dan konfigurasi koneksi disimpan sebagai bagian dokumentasi teknis proyek. Sebelum pengujian terintegrasi, pengembang melengkapi versi layanan yang digunakan serta memeriksa hasil migrasi basis data. Informasi tersebut menjadi acuan untuk menyiapkan ulang lingkungan dengan konfigurasi yang sama.

### 3.5.4 Lingkungan Implementasi dan Pengujian

Pengembangan dan evaluasi mitra menggunakan lingkungan yang terpisah agar kegiatan pengujian dapat dijalankan dengan data yang telah disiapkan. Pengujian awal memakai data buatan atau tersamarkan. Data nyata digunakan sesuai izin mitra dan dibatasi pada informasi yang diperlukan untuk menjalankan tugas evaluasi.

Bukti pembayaran disimpan pada penyimpanan privat dan hanya dapat dibuka setelah sistem memeriksa kewenangan pengguna. Kredensial koneksi, kata sandi, serta akses rekening dikelola terpisah dari bahan laporan. Pengaturan ini juga berlaku pada repositori terbuka dan gambar hasil pengujian agar informasi akses tidak ikut ditampilkan.

Waktu kejadian disimpan dalam UTC, kemudian ditampilkan menggunakan zona waktu Asia/Makassar sesuai operasional Balikpapan. Tanggal kewajiban dan jatuh tempo mengikuti kalender operasional yang sama. Setiap tagihan menggunakan tanggal yang telah ditetapkan pada datanya.

Untuk memeriksa pembatasan akses, lingkungan evaluasi disiapkan dengan akun simulasi minimal dua cabang dan satu akun pusat. Akun tersebut digunakan pada data uji yang mewakili pekerjaan kedua peran. Jumlah data, jaringan, versi, dan perangkat dicatat saat pelaksanaan, sedangkan peserta evaluasinya ditetapkan bersama mitra.

Data awal mencakup kelas yang masih tersedia, hampir penuh, dan penuh, serta jadwal yang beririsan dan tagihan dengan siklus berbeda. Pengajuan transfer yang dikembalikan dan setoran tunai juga disiapkan untuk mencoba perubahan status serta tindak lanjutnya. Setelah data dimuat, fungsi diperiksa dan cadangan awal disimpan agar keadaan yang sama dapat dipulihkan ketika kasus perlu diulang.

Pencadangan dilakukan terhadap basis data dan berkas pendukung yang saling berkaitan. Pengembang kemudian mencoba pemulihan pada lingkungan uji untuk memeriksa apakah data serta berkas dapat digunakan kembali. Hasil pemeriksaan ini menjadi bagian dokumentasi kemampuan pemulihan prototipe.

## 3.6 Jadwal Pembuatan Prototipe

Pengembangan direncanakan selama dua belas minggu relatif, dengan empat iterasi yang masing-masing dialokasikan dua minggu. Dokumentasi wawancara dan rancangan yang telah tersedia per 25 Oktober 2026 menjadi bahan awal pelaksanaan. Tanggal mulai implementasi serta evaluasi akan ditetapkan bersama pembimbing dan mitra.

Tabel 3.20 menyajikan alokasi kegiatan dari klarifikasi kebutuhan sampai penyiapan luaran. Bahan wawancara dan rancangan yang sudah tersedia digunakan kembali serta dilengkapi sesuai kebutuhan pelaksanaan. Minggu pertama dihitung dari tanggal mulai yang akan disepakati, sehingga tabel berfungsi sebagai rencana pembagian waktu.

**Tabel 3.20 Rencana Jadwal Pelaksanaan Prototipe**

| Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Klarifikasi bukti dan aturan mitra | X | X | | | | | | | | | | |
| Estimasi tugas, instrumen, dan lingkungan | | X | | | | | | | | | | |
| I-01: data dasar dan akses | | | X | X | | | | | | | | |
| I-02: keanggotaan dan jadwal | | | | | X | X | | | | | | |
| I-03: pembayaran dan WhatsApp | | | | | | | X | X | | | | |
| I-04: setoran, laporan, pencocokan | | | | | | | | | X | X | | |
| UAT, perbaikan, dan uji ulang | | | | | | | | | | | X | X |
| Dokumentasi waktu, galat, dan rancangan | | X | X | X | X | X | X | X | X | X | X | X |
| Penyiapan serah uji, laporan, artikel, HKI | | | | | | | | | | | X | X |

Pengujian unit, pengujian sistem, dan evaluasi dilakukan di dalam setiap iterasi agar hasilnya dapat digunakan pada pekerjaan berikutnya. Alokasi mingguan kemudian dirinci menjadi jam tugas dan tanggal pelaksanaan sebelum kegiatan dimulai. Jika kebutuhan atau ketersediaan mitra berubah, jadwal disesuaikan bersama catatan pengaruhnya terhadap pekerjaan yang tersisa.

Penyusunan laporan mengikuti panduan kepenulisan ITK, sedangkan bahan luaran prototipe disiapkan sesuai ketentuan program studi (Institut Teknologi Kalimantan, 2025a; Institut Teknologi Kalimantan, 2026). Perkembangan pekerjaan dan perubahan jadwal dicatat sepanjang pelaksanaan. Catatan tersebut menghubungkan rencana awal dengan proses yang nantinya dijelaskan dalam laporan.