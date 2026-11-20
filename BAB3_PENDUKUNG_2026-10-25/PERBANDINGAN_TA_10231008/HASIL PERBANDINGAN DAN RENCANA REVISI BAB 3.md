# Pembelajaran dari TA 10231008 dan rencana revisi Bab 3 ARTHA

Dokumen ini membandingkan berkas TA_10231008.pdf dengan draf Bab 3 ARTHA bertanggal 25 Oktober 2026. Status lulus seminar proposal mengikuti informasi pengguna, sedangkan penilaian isi didasarkan pada berkas yang tersedia dan tidak dimaksudkan untuk menilai ulang kelulusan mahasiswa tersebut.

## 1. Kesimpulan penilaian

Draf Bab 3 ARTHA tetap layak digunakan sebagai naskah induk, tetapi perlu dibuat lebih konkret dan lebih ringkas. Pelajaran paling berguna dari proposal pembanding adalah keterhubungan antara aktor, kebutuhan, rancangan layar, komponen teknis, dan pelaksanaan implementasi.

Perubahan yang disarankan bukan mengganti PxP menjadi XP atau mengganti UAT menjadi SUS. Perubahan utama adalah menambahkan artefak rancangan yang dapat diperiksa, menjelaskan pelaksanaan pengujian dan penyerahan prototipe, serta memindahkan penjelasan audit yang berulang ke catatan pendamping.

Penilaian difokuskan pada Bab 3 proposal pembanding, yaitu halaman cetak 39 sampai 66 atau urutan PDF 50 sampai 77. Beberapa bagian Bab 4 diperiksa untuk melihat bagaimana rancangan dihubungkan dengan implementasi dan pengujian, tanpa menganggap laporan hasil tersebut sebagai bukti eksekusi yang telah diverifikasi secara independen.

## 2. Identitas dan perbedaan yang memengaruhi pembandingan

| Aspek | Proposal pembanding | ARTHA | Implikasi |
| :--- | :--- | :--- | :--- |
| Objek | Aplikasi SITASI ITK berbasis mobile | Administrasi bimbel multicabang berbasis web | Kebutuhan dan antarmuka harus disesuaikan dengan tugas pengguna |
| Metode | Extreme Programming (XP) | Personal Extreme Programming (PxP) | Tahapan tidak disalin langsung; pertahankan proses individual dan pencatatan PxP |
| Pengguna | Mahasiswa, dosen, serta tenaga kependidikan pada bagian yang diperiksa | Admin Cabang dan Super Admin | Jangan menambah peran hanya mengikuti pembanding |
| Evaluasi pengguna | SUS disebut pada cetak 62 sampai 63/PDF 73 sampai 74 | UAT berbasis tugas direncanakan pada 3.3.8 | SUS merupakan pilihan tambahan bila ada tujuan evaluasi kegunaan, bukan kewajiban karena teman menggunakannya |
| Komunikasi | Notifikasi aplikasi mobile melalui layanan push | Tombol WhatsApp dengan pesan terisi dan notifikasi dalam dasbor | Tidak perlu mengikuti Expo atau pengiriman pesan otomatis |
| Struktur Bab 3 | Desain dan Implementasi, lima subbab utama | Rancangan Prototipe, enam subbab utama | ARTHA tetap mengikuti template yang dipilih |
| Jenis dokumen yang tersedia | Memuat Bab 3, isi Bab 4, serta Bab 5 yang masih mempunyai teks template | Draf rancangan Bab 3 | Adanya isi Bab 4 tidak membuktikan semua bagian perlu diselesaikan sebelum sempro |

Sumber struktur baku ARTHA adalah template prototipe ITK, cetak 6 sampai 7 atau PDF 19 sampai 20. Keberhasilan seminar proposal pada contoh tidak otomatis menjadikan semua pilihan struktur, redaksi, atau instrumennya sebagai aturan umum untuk penelitian lain.

## 3. Hal yang dapat dipelajari dari proposal pembanding

### 3.1 Konsep produk segera terlihat

Pada cetak 39/PDF 50, pembaca langsung diperlihatkan diagram konsep yang menghubungkan aplikasi, layanan data, dan notifikasi. Diagram tersebut membantu menjelaskan bentuk produk sebelum pembaca masuk ke rincian prosedur.

ARTHA sudah mempunyai gambar arsitektur pada 3.5.1, tetapi gambaran produk pada 3.1 masih didominasi penjelasan tekstual. Perbaikannya dapat dilakukan melalui rujukan silang ke gambar arsitektur yang sama atau penempatan gambar tersebut lebih awal, tanpa menggandakan gambar identik di dua tempat.

### 3.2 Kebutuhan pengguna dijelaskan sampai kondisi penerimaannya

Pada cetak 46/PDF 57, peran pengguna dijelaskan dalam tabel. Pada cetak 47 sampai 56/PDF 58 sampai 67, kebutuhan dirinci dengan peran, tindakan yang diinginkan, dan kriteria penerimaan yang menyebut kondisi, status, serta tanggapan sistem.

ARTHA telah mempunyai tabel hak akses dan sepuluh cerita pengguna, sehingga tidak perlu menyalin panjang tabel pembanding. Peningkatan yang diperlukan adalah kelengkapan cakupan kebutuhan dan pemetaan setiap kebutuhan ke cerita pengguna, iterasi, serta kasus uji yang sesuai.

### 3.3 Rancangan antarmuka benar-benar diperlihatkan

Pada cetak 58 sampai 61/PDF 69 sampai 72, proposal pembanding menampilkan rancangan login, dasbor, bimbingan, penambahan bimbingan, akademik, profil, dan notifikasi. Ini merupakan pembeda yang nyata dari draf ARTHA, yang pada 3.4.7 baru mempunyai tabel rencana halaman.

ARTHA sebaiknya menambahkan rancangan layar untuk alur yang menjadi inti penelitian. Jumlah gambar tidak perlu disamakan dengan pembanding, karena relevansi alur lebih penting daripada banyaknya tampilan.

### 3.4 Komponen dan layanan mempunyai fungsi yang dijelaskan

Pada cetak 41 sampai 42/PDF 52 sampai 53, React Native, Laravel, Expo, layanan notifikasi, dan penyimpanan dijelaskan menurut fungsinya. Pada cetak 63 sampai 65/PDF 74 sampai 76, uraian tersebut dihubungkan dengan penerapan aplikasi.

ARTHA sudah mempunyai tabel komponen, tetapi sebagian kolom masih menjelaskan apa yang akan dicatat nanti. Bagian ini perlu diubah bertahap menjadi pilihan dan konfigurasi yang benar-benar akan digunakan, tanpa mengisi versi atau perangkat yang belum diketahui.

### 3.5 Pengujian dihubungkan dengan implementasi

Pada cetak 62/PDF 73, pengujian unit, pengodean, dan refaktorisasi disebut sebagai kegiatan implementasi. Bagian Bab 4, misalnya cetak 85 sampai 88/PDF 96 sampai 99, memperlihatkan cara penulis menghubungkan kode, pengujian, dan perubahan struktur.

Pelajaran untuk ARTHA adalah menyiapkan bukti proses sejak pengembangan, bukan memindahkan contoh hasil teman ke Bab 3. Urutan pengujian sebelum kode pada TDD tetap mengikuti rancangan PxP dan sumber primer yang dipilih untuk ARTHA.

### 3.6 Penyerahan prototipe merupakan kegiatan yang jelas

Pada cetak 63/PDF 74, terdapat uraian deployment sebagai penyiapan hasil agar dapat digunakan. Pada ARTHA, penyerahan akses lingkungan uji, penyiapan akun, pemeriksaan konfigurasi, dan pengarahan penggunaan belum menjadi prosedur yang cukup eksplisit.

ARTHA perlu menjelaskan kegiatan tersebut sesuai produk web. Penyerahan prototipe untuk evaluasi mitra tidak otomatis berarti penerapan produksi penuh pada delapan cabang.

## 4. Matriks edit yang disarankan pada Bab 3 ARTHA

Lokasi ARTHA menggunakan subbab dan baris Markdown pada versi yang diperiksa. Nomor halaman cetak ARTHA belum tersedia karena naskah belum dipindahkan ke tata letak Word final.

| Kode | Lokasi ARTHA | Tindakan | Perbaikan yang disarankan | Bukti pembanding | Prioritas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | 3.1, baris 6 sampai 46 | Padatkan | Satukan uraian objek, ruang lingkup, metode, dan luaran menjadi gambaran produk yang lebih singkat; pertahankan keputusan inti | Cetak 39 sampai 40/PDF 50 sampai 51 | Penting |
| R-02 | 3.2 dan Gambar 3.1, baris 48 sampai 78 | Perjelas | Tambahkan kondisi keputusan untuk perbaikan, iterasi berikutnya, dan penerimaan pengguna; uraikan urutan tes, kode, dan refaktorisasi pada implementasi | Diagram pada cetak 44/PDF 55 | Penting |
| R-03 | 3.3.1, baris 84 sampai 113 | Tambahkan | Tabel sumber data atau informan: peran, cakupan cabang, topik, tanggal, dan status bukti; pisahkan wawancara yang sudah ada dari rencana klarifikasi | Tabel aktor pada cetak 46/PDF 57 | Sangat penting |
| R-04 | 3.3.2, baris 115 sampai 136 | Tambahkan | Pemetaan cerita pengguna ke prioritas, ketergantungan, iterasi, dan estimasi tugas; jelaskan dasar empat iterasi | Planning pada cetak 58/PDF 69; rencana per iterasi pada cetak 80/PDF 91 | Sangat penting |
| R-05 | 3.3.5 dan 3.3.7, baris 160 sampai 170 serta 204 sampai 223 | Pertahankan dan ringkas | Pertahankan TDD, log waktu, log galat, dan evaluasi; pindahkan rincian format log ke lampiran pendamping | Contoh hubungan implementasi dan pengujian pada cetak 85 sampai 88/PDF 96 sampai 99 | Penting |
| R-06 | 3.3.6 dan 3.3.8, baris 172 sampai 259 | Lengkapi | Tentukan pelaksana, peserta, lingkungan, data, waktu, kriteria keputusan, dan bukti; pertahankan hasil aktual sebagai belum diuji | Pengujian sistem dan SUS pada cetak 62 sampai 63/PDF 73 sampai 74 | Sangat penting |
| R-07 | 3.3.8 dan 3.5.4 | Tambahkan | Prosedur penyiapan lingkungan uji, akun, panduan singkat, pencadangan, serta penyerahan prototipe kepada mitra | Deployment pada cetak 63/PDF 74 | Penting |
| R-08 | 3.4.2 dan 3.4.4, baris 297 sampai 390 | Selaraskan | Buat satu matriks KF, cerita pengguna, iterasi, dan kasus uji; jangan menganggap semua kebutuhan sudah terwakili oleh sepuluh cerita pengguna | Tabel cerita pengguna pada cetak 47 sampai 56/PDF 58 sampai 67 | Sangat penting |
| R-09 | 3.4.5, baris 392 sampai 419 | Perjelas | Bedakan tujuan mengajukan transfer, memverifikasi transfer, dan mencocokkan setoran; sesuaikan diagram serta skenario | Kriteria status dan tindakan menurut peran pada cetak 48 sampai 52/PDF 59 sampai 63 | Penting |
| R-10 | 3.4.6, baris 421 sampai 452 | Perdalam | Lengkapi hubungan ruang, kelas, tarif, tagihan, pemeriksaan, dan referensi pencocokan; tambahkan kamus data ringkas untuk bagian berisiko | Pembelajaran dari kebutuhan yang terperinci, bukan karena pembanding mewajibkan ERD tertentu | Penting |
| R-11 | 3.4.7, baris 454 sampai 475 | Tambahkan | Empat sampai enam rancangan layar inti beserta penjelasan fungsi dan cerita pengguna terkait | Rancangan layar pada cetak 58 sampai 61/PDF 69 sampai 72 | Sangat penting |
| R-12 | 3.5, baris 477 sampai 550 | Konkretkan | Nyatakan pilihan komponen, fungsi, serta konfigurasi yang sudah diketahui; pisahkan perangkat pengembangan, lingkungan mitra, dan layanan eksternal | Tabel komponen dan layanan pada cetak 41 sampai 42/PDF 52 sampai 53 | Penting |
| R-13 | 3.6, baris 552 sampai akhir | Sesuaikan | Gunakan kalender dan estimasi tugas ARTHA; bedakan kegiatan yang sudah dilaksanakan dari rencana berikutnya | Gantt kalender pada cetak 66/PDF 77 | Penting |
| R-14 | Seluruh bab | Kurangi | Pindahkan penjelasan audit, pembatasan interpretasi berulang, dan pembahasan artikel pembanding yang terlalu panjang ke catatan pendamping atau Bab 2 | Gaya pembanding lebih banyak menjelaskan produk dan pekerjaan konkret | Penyempurnaan |

### 4.1 Tambahan yang paling mendesak: rancangan layar inti

Tambahan antarmuka sebaiknya difokuskan pada pekerjaan yang membedakan ARTHA dari sistem pencatatan biasa. Rancangan berikut merupakan daftar layar yang perlu disusun, bukan klaim bahwa gambar tersebut sudah tersedia dalam draf saat ini.

| Layar yang disarankan | Unsur yang perlu terlihat | Hubungan dengan penelitian |
| :--- | :--- | :--- |
| Dasbor Admin Cabang | Tunggakan, pengajuan menunggu pemeriksaan, dan indikator kapasitas | Menunjukkan prioritas pekerjaan admin |
| Penempatan siswa pada kelas | Kapasitas, peserta aktif, sisa tempat, peringatan hampir penuh, dan penolakan kelas penuh | Menjelaskan KF-03/KF-04 dan US-03/US-04 |
| Pengajuan transfer | Siswa, tagihan, periode, nominal, tanggal, bukti, dan status pengajuan | Menjelaskan KF-08 dan US-06 |
| Pemeriksaan transfer Super Admin | Bukti, rujukan dana masuk, tombol persetujuan/pengembalian, dan alasan | Menjelaskan KF-09 dan US-07 |
| Tunggakan dan pesan WhatsApp | Nomor wali, periode, sisa tagihan, tanggal jatuh tempo, dan pratinjau pesan | Menjelaskan KF-10 dan US-08 |
| Dasbor pusat dan pencocokan | Penyaring cabang/periode, penerimaan terkonfirmasi, pengajuan tertunda, serta transaksi sumber | Menjelaskan KF-12/KF-13 dan US-09/US-10 |

Contoh penjelasan setelah gambar: “Rancangan halaman pemeriksaan menampilkan pengajuan transfer yang belum diputuskan. Super Admin dapat membuka bukti, mencatat rujukan pemeriksaan dana masuk, kemudian menyetujui atau mengembalikan pengajuan disertai alasan.”

### 4.2 Tambahan matriks keterlacakan tanpa menggandakan tabel

ARTHA sudah mempunyai empat belas kebutuhan fungsional, sepuluh cerita pengguna, lima belas kasus uji awal, dan tujuh tugas UAT. Jumlah tersebut tidak harus sama, tetapi hubungannya perlu ditunjukkan agar satu kebutuhan tidak hilang dari pengembangan atau evaluasi.

| Contoh kebutuhan | Cerita pengguna terkait | Kasus uji awal | Tugas UAT | Catatan perbaikan |
| :--- | :--- | :--- | :--- | :--- |
| KF-01 pembatasan akses | US-01 | BB-01 | Tambahkan pemeriksaan akses sesuai peran | Login dan akses lintas cabang perlu dibedakan |
| KF-03/KF-04 kelas dan kapasitas | US-03/US-04 | BB-03 sampai BB-06 | UAT-02 | Tambahkan kasus ambang hampir penuh yang mengikuti parameter |
| KF-08 pengajuan transfer | US-06 | BB-08 | UAT-03 | Data wajib dan format bukti perlu kasus tersendiri |
| KF-09 pemeriksaan transfer | US-07 | BB-09 sampai BB-11 | UAT-05 | Bedakan bukti tidak sesuai dan pengajuan ulang |
| KF-10 tautan WhatsApp | US-08 | BB-12/BB-13 | UAT-04 | Pembukaan tautan tidak dianggap pesan terkirim |
| KF-12/KF-13 rekap dan pencocokan | US-09/US-10 | BB-14/BB-15 | UAT-06 | Penerimaan tunai dan setoran tidak dihitung ganda |

Matriks lengkap dapat diletakkan pada lampiran atau menggabungkan kolom rujukan pada tabel yang sudah ada. Kebutuhan tarif, pembayaran tunai, notifikasi dalam dasbor, serta pengelolaan akun perlu diperiksa cakupannya karena belum semuanya mempunyai cerita pengguna dan kasus uji tersendiri pada contoh awal.

### 4.3 Tambahan prosedur penyiapan dan penyerahan prototipe

Penyiapan prototipe untuk UAT dapat dimasukkan pada 3.3.8 sebelum pelaksanaan tugas pengguna. Konfigurasi lingkungannya tetap dijelaskan pada 3.5.4 agar prosedur dan spesifikasi tidak mengulang uraian yang sama.

Urutan yang disarankan adalah penyiapan lingkungan uji, pemuatan data uji, pembuatan akun per peran, pemeriksaan akses, pengarahan singkat, pelaksanaan tugas, serta pencatatan hasil. Setelah evaluasi, perubahan dan versi yang diserahkan dicatat bersama panduan penggunaan serta mekanisme pencadangan.

Contoh redaksi: “Sebelum evaluasi, prototipe ditempatkan pada lingkungan uji yang dapat diakses oleh perwakilan mitra. Akun, data uji, dan panduan tugas disiapkan sesuai kewenangan pengguna, kemudian akses serta fungsi utama diperiksa sebelum UAT dimulai.”

## 5. Bagian yang perlu dikurangi atau dipindahkan

### 5.1 Uraian berulang antara garis besar, prosedur, dan konsep

Mekanisme WhatsApp, kapasitas, pembayaran, dan pembatasan cabang saat ini muncul pada 3.1, 3.3, 3.4, serta 3.5. Pengulangan diperlukan jika tujuannya berbeda, tetapi uraian yang sama tidak perlu dijelaskan lengkap pada setiap tempat.

Pembagian yang disarankan adalah 3.1 untuk gambaran produk, 3.3 untuk cara pengembangan dan evaluasi, 3.4 untuk aturan serta artefak rancangan, dan 3.5 untuk komponen teknis. Rujukan silang digunakan apabila pembaca memerlukan rincian yang sudah dijelaskan pada subbab lain.

### 5.2 Kalimat audit yang lebih sesuai sebagai catatan kerja

Pada 3.1.1 terdapat penjelasan bahwa angka tertentu tidak dipakai sebelum ada bukti. Pada 3.1.2 juga terdapat penjelasan bahwa ARTHA tidak dinyatakan sebagai bimbel multicabang yang pertama, sedangkan beberapa bagian lain mengulang keterbatasan penafsiran artikel pembanding.

Kehati-hatian tersebut penting selama penyusunan, tetapi sebagian lebih tepat berada pada catatan audit atau Bab 2. Naskah Bab 3 cukup menyatakan data yang digunakan, sumbernya, prosedur validasi, serta batas rancangan yang berpengaruh pada pelaksanaan.

### 5.3 Penjelasan statistik yang tidak digunakan dalam rancangan

Pada 3.3.8 terdapat penjelasan mengapa seluruh tugas UAT tidak diperlakukan sebagai satu konstruk psikometrik. Penjelasan panjang mengenai koefisien konsistensi internal dapat dipindahkan ke catatan metode apabila memang tidak digunakan kuesioner multibutir untuk suatu konstruk.

Bagian utama cukup menjelaskan instrumen berbasis tugas, pemeriksaan keterbacaan, kesesuaian isi, cara pencatatan, dan keputusan penerimaan. Jika instrumen persepsi ditambahkan, pembahasan validitas dan analisisnya harus disesuaikan dengan instrumen tersebut.

### 5.4 Detail formulir dan seluruh kasus uji

Catatan waktu, galat, perubahan, dan seluruh kasus uji tidak perlu dihapus karena berkaitan dengan penerapan PxP. Namun, format lengkap dapat ditempatkan di lampiran, sedangkan Bab 3 menampilkan ringkasan unsur, contoh kasus berisiko, dan penjelasan pengolahannya.

Pemindahan tersebut bertujuan memperjelas alur baca, bukan mengurangi bukti. Semua kebutuhan tetap harus mempunyai cara pemeriksaan yang dapat ditelusuri.

## 6. Bagian ARTHA yang perlu dipertahankan

1. Enam subbab utama sesuai template: garis besar, tahapan, prosedur, konsep, spesifikasi, dan jadwal.
2. Penggalian kebutuhan yang membedakan keterangan satu cabang dari ketentuan seluruh cabang.
3. Pembatasan data antarcabang dan pemeriksaan kewenangan pada peladen.
4. Pengajuan bukti transfer yang belum otomatis dianggap sebagai pembayaran lunas.
5. Pemisahan penerimaan siswa, setoran kas, dan pencocokan bank agar transaksi tidak dihitung ganda.
6. Aturan hampir penuh, penuh, serta pembukaan tempat setelah keanggotaan siswa berakhir.
7. Pengingat WhatsApp melalui tombol manual sesuai penjelasan pengguna.
8. Pengujian unit dan bukti urutan tes, kode, serta refaktorisasi apabila TDD diterapkan.
9. Pencatatan waktu, galat, perubahan kebutuhan, serta evaluasi iterasi sebagai bukti proses PxP.
10. Pemisahan rancangan kasus uji dari hasil aktual dan pemisahan penerimaan pengguna dari klaim peningkatan efisiensi.

Komponen tersebut berkaitan langsung dengan kebutuhan dan risiko ARTHA. Tidak adanya pembahasan yang sama pada contoh teman bukan alasan untuk menghapusnya.

## 7. Pilihan yang tidak perlu diikuti secara otomatis

### 7.1 Tidak mengganti struktur resmi karena contoh berbeda

Proposal pembanding memakai judul Bab 3 Desain dan Implementasi dengan lima subbab utama, sedangkan template yang dipilih ARTHA memakai Rancangan Prototipe dengan enam subbab. Struktur ARTHA tetap dipertahankan sampai ada arahan resmi yang berbeda dari pembimbing atau program studi.

Penomoran 3.3.3.1 pada pembanding juga tidak perlu disalin. Penomoran ARTHA cukup sampai tiga level sesuai ketentuan yang telah diberikan pengguna.

### 7.2 Tidak mengganti PxP menjadi XP

Proposal teman menyebut XP pada lembar persetujuan dan isi metode. Penelitian ARTHA telah diarahkan pada PxP, sehingga penjelasan inisialisasi iterasi, pencatatan individual, dan evaluasi proses tetap diperlukan.

Status seminar proposal teman tidak membuktikan salah satu metode selalu lebih tepat untuk seluruh proyek. Pemilihan metode dijelaskan berdasarkan cara penelitian ARTHA akan dilaksanakan dan praktik yang benar-benar dijalankan.

### 7.3 Tidak menambahkan SUS sebagai syarat kelulusan

Proposal teman menggunakan SUS setelah pengguna mencoba aplikasi, sebagaimana dijelaskan pada cetak 62 sampai 63/PDF 73 sampai 74. ARTHA dapat tetap menggunakan UAT berbasis tugas untuk menilai penerimaan alur operasional.

Apabila penelitian juga ingin mengukur persepsi kegunaan antarmuka secara terstandar, SUS dapat dipertimbangkan sebagai instrumen tambahan dengan sumber dan analisisnya sendiri. Brooke menjelaskan SUS sebagai pengukuran persepsi kegunaan, sehingga skor tersebut tidak diperlakukan sebagai bukti langsung bahwa semua fungsi telah benar atau pekerjaan nyata menjadi lebih cepat. Rujukan primer pelengkap: [Brooke (2013), SUS: A Retrospective](https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Brooke_February_2013.pdf).

### 7.4 Tidak otomatis menambah pengujian jalur kode pada seluruh fungsi

Bab 4 pembanding menampilkan pengujian jalur dan kompleksitas kode, misalnya cetak 87/PDF 98. Teknik tersebut dapat relevan untuk tujuan tertentu, tetapi bukan alasan untuk mewajibkan perhitungan yang sama pada semua fungsi ARTHA.

Pengujian ARTHA lebih dahulu dipusatkan pada aturan kritis, seperti kapasitas, irisan jadwal, otorisasi cabang, dan penghitungan pembayaran. Teknik tambahan digunakan jika membantu memeriksa risiko atau klaim tertentu dan dapat dilaksanakan dengan benar.

### 7.5 Tidak menyalin target teknis dan kalender penelitian

Aplikasi pembanding memerlukan teknologi mobile dan layanan push, sedangkan ARTHA memerlukan aplikasi web serta tautan WhatsApp. Keduanya mempunyai kebutuhan penyimpanan, akses, dan pengujian yang berbeda.

Jadwal pembanding menampilkan Februari sampai November pada cetak 66/PDF 77. Durasi tersebut tidak menjadi ketentuan minimum, sedangkan usulan dua belas minggu pada draf ARTHA juga belum dapat dianggap final tanpa estimasi tugas dan kalender penelitian yang nyata.

## 8. Contoh pemadatan garis besar prototipe

Contoh berikut dapat digunakan sebagai arah revisi 3.1, kemudian disesuaikan dengan rincian yang telah disepakati. Sitasi metode dipertahankan, sedangkan uraian audit dipindahkan ke catatan pendamping.

> Prototipe yang dikembangkan berupa sistem informasi manajemen operasional berbasis web untuk Bimbel Artha Balikpapan. Sistem dirancang untuk mengintegrasikan pencatatan siswa, keanggotaan kelas, penjadwalan tentor, pembayaran SPP, dan pemantauan penerimaan pada delapan cabang.
>
> Pengguna sistem terdiri atas Admin Cabang dan Super Admin. Admin Cabang mengelola data sesuai penugasannya, sedangkan Super Admin memantau informasi lintas cabang dan menjalankan pemeriksaan pembayaran sesuai kewenangan yang ditetapkan bersama mitra.
>
> Pengingat pembayaran disediakan melalui tombol WhatsApp dengan nomor serta pesan yang disiapkan berdasarkan tagihan. Pada pengelolaan kelas, sistem menampilkan peringatan hampir penuh dan menolak penambahan siswa setelah kapasitas tercapai, sementara riwayat siswa keluar tetap disimpan.
>
> Pengembangan menggunakan PxP melalui penggalian kebutuhan, perencanaan, inisialisasi iterasi, perancangan, implementasi, pengujian sistem, dan evaluasi iterasi (Dzhurov dkk., 2009, hlm. 254 sampai 256). Luaran yang disiapkan meliputi prototipe, dokumentasi pengembangan, hasil evaluasi mitra, laporan, artikel ilmiah, serta dokumen pengajuan HKI sesuai panduan tugas akhir prototipe.

## 9. Pemeriksaan kritis atas contoh yang tidak perlu ditiru

Terdapat beberapa ketidakkonsistenan dalam berkas pembanding yang menunjukkan bahwa contoh tetap perlu dibaca secara kritis. Catatan berikut relevan untuk mencegah masalah yang sama muncul pada ARTHA dan tidak dimaksudkan sebagai penilaian kelulusan teman.

| Bagian pembanding | Hal yang terlihat | Pelajaran untuk ARTHA |
| :--- | :--- | :--- |
| Cetak 46/PDF 57 | Kalimat pengantar menyebut empat aktor, sedangkan tabel yang ditampilkan memuat tiga | Samakan jumlah aktor dengan daftar dan diagram |
| Cetak 50/PDF 61 | Kode US-13 dipakai pada dua judul kebutuhan | Gunakan kode kebutuhan yang unik |
| Cetak 44/PDF 55 dan cetak 45/PDF 56 | Diagram ringkas tidak menampilkan semua tahap pendukung yang dijelaskan dalam prosedur | Jelaskan batas diagram atau tampilkan tahap yang diperlukan agar alur dan prosedur selaras |
| Cetak 44/PDF 55 dan cetak 62/PDF 73 | Diagram implementasi menampilkan kode kemudian tes, sedangkan teks menyebut tes sebelum kode | Samakan urutan proses, terutama jika mengklaim TDD |
| Cetak 63 sampai 65/PDF 74 sampai 76 | Pengacuan nomor tabel tidak selalu sama dengan judul tabel yang tampil | Gunakan penomoran dan rujukan silang yang konsisten |
| Daftar isi PDF 9 dibanding PDF 50 | Awal Bab 3 di daftar isi berbeda dengan halaman cetak bab pada berkas ini | Perbarui daftar isi setelah tata letak berubah |
| Cetak 117/PDF 128 | Bab 5 masih memuat instruksi template | Hapus anotasi template dan jangan menganggap seluruh berkas merupakan naskah final yang bersih |

## 10. Urutan revisi yang direkomendasikan

1. Tetapkan narasi ringkas produk ARTHA dan pertahankan enam subbab utama template.
2. Lengkapi tabel sumber kebutuhan serta pemetaan KF, cerita pengguna, iterasi, dan pengujian.
3. Perjelas alur pembayaran lintas peran dan aturan kelas yang akan ditampilkan pada layar.
4. Buat rancangan antarmuka inti pada 3.4.7, disertai penjelasan dua sampai tiga kalimat per gambar.
5. Perbaiki diagram alir agar keputusan mengulang, memperbaiki, dan menutup iterasi terbaca jelas.
6. Lengkapi prosedur UAT dan penyiapan prototipe berdasarkan peserta, lingkungan, serta bukti pelaksanaan yang akan digunakan.
7. Konkretkan spesifikasi dan jadwal menggunakan data yang tersedia; tandai keputusan yang belum ditetapkan sebagai rencana.
8. Pindahkan rincian log, seluruh kasus uji, dan penjelasan audit berulang ke lampiran atau catatan pendamping.
9. Selaraskan kembali Bab 1 dan Bab 2 setelah rancangan pelaksanaan stabil.

Revisi yang paling memberi nilai tambah adalah memperlihatkan bentuk prototipe dan cara setiap kebutuhan akan dibuktikan. Menambah teori atau meniru jumlah halaman pembanding tidak menggantikan kebutuhan akan artefak rancangan yang jelas dan prosedur yang dapat dilaksanakan.

## 11. Penunjuk berkas sumber

- [Proposal pembanding TA_10231008.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/REFERENSI TA PXP/TA_10231008.pdf>).
- [Draf Bab 3 ARTHA yang diperiksa](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md>).
- [Template prototipe ITK yang menjadi acuan struktur](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/TEMPLATE TA/Copy of Template Laporan TA 2025 PROTOTIPE SI.docx.pdf>).
- [Panduan tugas akhir SI ITK 2026](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/PANDUAN TA/Panduan TA dan SITASI - Sistem Informasi ITK 2026.pdf>).

Salinan teks per halaman dan gambar halaman terpilih disimpan pada folder perbandingan ini untuk membantu pemeriksaan manual. Naskah sumber dan draf Bab 3 yang dibandingkan tetap menjadi dokumen terpisah dari rekomendasi ini.
