# Rencana Bab 2 dan pemilihan penelitian terdahulu ARTHA

Dokumen ini disusun pada 27 Oktober 2026 sebagai panduan penulisan, bukan sebagai Bab 2 yang sudah selesai. Dasar penyesuaiannya adalah template prototipe terbaru, dua berkas Bab 1 dalam folder draf, Bab 3 revisi template terbaru versi copy, serta PDF pustaka yang tersedia.

## 1. Struktur utama mengikuti template

Template menetapkan Bab 2 berjudul Tinjauan Pustaka dengan urutan 2.1 Kajian Teknologi atau Metode Terkait, 2.2 Penelitian Terdahulu, dan 2.3 Dasar Teori Pendukung yang bersifat opsional. Ketentuan tersebut berada pada halaman tercetak 4 sampai 5 atau halaman PDF 17 sampai 18 dari template prototipe.

Untuk ARTHA, bagian 2.3 disarankan tetap dipakai karena pengelolaan cabang, pencatatan penerimaan, serta kapasitas kelas membutuhkan penjelasan konsep. Rincian judul pada tingkat ketiga berikut merupakan rekomendasi sesuai kebutuhan penelitian, bukan daftar subbab wajib dari template.

### Usulan susunan lengkap

```text
BAB 2 TINJAUAN PUSTAKA

2.1 Kajian Teknologi atau Metode Terkait
    2.1.1 Prototipe dan Pengembangan Sistem Informasi
    2.1.2 Perbandingan Pendekatan Pengembangan dan Dasar Pemilihan PxP
    2.1.3 Personal Extreme Programming
    2.1.4 Arsitektur Aplikasi Web dan Komunikasi API
    2.1.5 Teknologi Pendukung Pengembangan ARTHA
    2.1.6 Pengujian Fungsional dengan Black Box Testing
    2.1.7 Pengujian Penerimaan Pengguna

2.2 Penelitian Terdahulu
    2.2.1 Sistem Informasi Bimbingan Belajar dan Kursus
    2.2.2 Pengelolaan Multicabang, Pembayaran, dan Batas Sumber Daya
    2.2.3 Penerapan PxP dan Evaluasi Sistem
    2.2.4 Sintesis Perbandingan dan Posisi Penelitian ARTHA

2.3 Dasar Teori Pendukung
    2.3.1 Sistem Informasi Manajemen Operasional
    2.3.2 Administrasi Bimbingan Belajar
    2.3.3 Pengelolaan Data Multicabang dan Pembatasan Hak Akses
    2.3.4 Tagihan, Penerimaan Pembayaran, dan Pencocokan Mutasi Bank
    2.3.5 Kapasitas Kelas dan Benturan Jadwal
    2.3.6 Kebutuhan Sistem, Pemodelan Proses, dan Basis Data Relasional
```

Subbab 2.2.1 sampai 2.2.3 dapat disajikan sebagai kelompok uraian yang diikuti satu tabel perbandingan terpadu. Pemisahan kelompok bertujuan memudahkan pembaca memahami fungsi sumber, bukan mengharuskan pengulangan artikel pada beberapa tabel.

## 2. Sepuluh artikel yang diprioritaskan

Daftar berikut merupakan prioritas berdasarkan kedekatan isi, bukan pernyataan bahwa seluruh edisinya baru saja diverifikasi akreditasi SINTA. Tahun Thiovanda, edisi 14(1), dan tanggal terbit 21 Januari 2026 berhasil dicocokkan kembali dengan laman penerbit pada pemeriksaan ini.

| No. | Artikel dan kedudukan | Bagian yang dapat dipakai | Batas perbandingan yang perlu dijelaskan | Lokator awal pemeriksaan manual |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Fajriansyah dkk. (2026), sistem informasi Bimbel Bee Hive; pembanding operasional bimbel | Integrasi pendaftaran, siswa, tentor, jadwal, pembayaran, dan laporan kegiatan. | Hasil efisiensi pada Bee Hive tidak menjadi hasil ARTHA. Periksa cara pengukuran sebelum menyalin angka waktu atau klaim benturan nol persen. | Cetak 115 sampai 116 dan 124 sampai 125; PDF 1 sampai 2 dan 10 sampai 11. |
| 2 | Gunawan dkk. (2025), sistem informasi Bimbel RSDC; pembanding fungsi dan pengujian | Registrasi, jadwal, presensi, pembayaran, pembagian pengguna, dan pengujian kotak hitam. | Metode Waterfall dan peran pengguna berbeda. Jangan menyimpulkan metode ARTHA lebih unggul hanya karena berbeda. | Cetak 424 dan 432; PDF 1 dan 9. |
| 3 | Thiovanda (2026), penjadwalan dan pembayaran les Jia Jia Education; pembanding paling dekat untuk cabang dan kewenangan | Pengelolaan cabang, head admin dan admin cabang, data siswa, jadwal, serta verifikasi pembayaran. | Artikel sudah membahas cabang. Klaim bahwa seluruh penelitian bimbel terdahulu hanya satu cabang harus dihindari. Perbandingan harus menelusuri pencocokan mutasi, alur setoran tunai, batas kelas, dan bukti uji yang memang dijelaskan. | Cetak/PDF 1, 3, 4, dan 5; Gambar 9 tentang cabang, Gambar 11 tentang siswa, Gambar 15 tentang verifikasi pembayaran. |
| 4 | Ahadi, Pariyadi, dan Djauhari (2025), sistem manajemen hotel multicabang; pembanding struktur organisasi | Pembatasan akses berdasarkan aktor, pencatatan transaksi per cabang, serta dashboard pemilik. | Objek hotel dan empat aktor berbeda dari ARTHA. Sistem ini bukan dasar tunggal teori keamanan atau alasan wajib dua peran. | Cetak 764 sampai 765; PDF 7 sampai 8. |
| 5 | Hendri dkk. (2025), penerimaan kas SPP Yayasan Semesta Khatulistiwa; pembanding administrasi penerimaan | Kebutuhan pencatatan pembayaran, pengendalian penerimaan, dan rancangan informasi pembayaran. | Luaran berupa analisis dan rancangan prototipe Figma. Jangan dipaparkan sebagai aplikasi transaksi yang telah diterapkan penuh. | Cetak 124 sampai 125; PDF 1 sampai 2, dilanjutkan halaman rancangan. |
| 6 | Sudirman dan Tristianti (2021), pengendalian kas bank CV Lisa Pratama; pembanding pencocokan keuangan | Pencocokan catatan perusahaan dan rekening bank serta penelusuran selisih. | Rekonsiliasi saldo akuntansi lebih luas daripada pencocokan penerimaan pembayaran. ARTHA tidak otomatis menerapkan seluruh rekonsiliasi perusahaan. | Cetak 126 sampai 129; PDF 1 sampai 4. |
| 7 | Khafidhoh, Febrianti, dan Sujono (2026), penjadwalan Bimbel AHE; pembanding kendala jadwal | Ketersediaan tentor, waktu belajar, dan potensi benturan jadwal. | Artikel menggunakan algoritma genetika untuk penjadwalan otomatis. ARTHA hanya merencanakan pemeriksaan dan peringatan konflik, sehingga algoritmanya tidak diklaim digunakan. | Cetak 15 sampai 16 dan 19; PDF 1 sampai 2 dan 5. |
| 8 | Kabisatullah dan Noprisson (2026), RapaTrack; pembanding validasi kapasitas dan waktu | Batas kapasitas, irisan waktu, waktu mulai dan selesai, serta pengujian validasi. | Objeknya ruang rapat perusahaan, Android, dan CSP. Kapasitas kelas siswa aktif berbeda dari jumlah peserta satu reservasi; seluruh CSP tidak otomatis menjadi metode ARTHA. | Cetak 93 sampai 95; PDF 5 sampai 7, terutama cetak 94/PDF 6. |
| 9 | Sidiq, Marthasari, dan Aminudin (2025), sistem surat menyurat dengan PxP; pembanding proses pengembangan | Perubahan user story, perencanaan iterasi, pengujian, serta perbandingan estimasi dan realisasi. | Objeknya surat menyurat. Waktu implementasi 37 hari harus dibedakan dari total pengembangan 50 hari; jangan disimpulkan bahwa seluruh proyek PxP pasti lebih cepat. | Cetak 35, 37 sampai 38, dan 45; PDF 1, 3 sampai 4, dan 11. |
| 10 | Apriyanti, Wati, dan Najaf (2024), website e-kavling; pembanding PxP dan evaluasi | PxP, unggah bukti pembayaran, pemeriksaan transaksi, Black Box Testing, dan UAT. | UAT artikel menggunakan kuesioner dan jumlah peserta tidak konsisten antarbagian. Skor 91% tidak dapat dijadikan target wajib ARTHA atau disamakan dengan penerimaan tugas. | Cetak 3678, 3683 sampai 3685; PDF 1 dan 6 sampai 8. |

Sepuluh artikel tersebut memberikan kelompok pembanding yang saling melengkapi tanpa menuntut satu artikel memuat semua kebutuhan ARTHA. Jumlah sepuluh merupakan rekomendasi pemilihan yang terarah, bukan jumlah minimum penelitian terdahulu yang diwajibkan template.

## 3. Artikel tambahan dan sumber yang tidak perlu masuk tabel utama

Artikel lain tetap dapat dipakai untuk mendukung uraian tertentu meskipun tidak dimasukkan ke sepuluh baris utama. Bila suatu artikel dipilih untuk menggantikan artikel inti, alasan penggantian sebaiknya berdasarkan kedekatan fungsi, kualitas bukti, atau kelengkapan identitasnya.

| Sumber yang tersedia | Penggunaan yang disarankan | Pertimbangan |
| :--- | :--- | :--- |
| Kismantoro dan Ibadi (2026), kursus INET Komputer | Tambahan kuat atau pengganti salah satu pembanding bimbel; mendukung Laravel, Agile, pembayaran, serta Black Box dan UAT. | Relevan secara fungsi dan teknologi. Gunakan istilah Agile sebagaimana artikel, tanpa otomatis menyebut penerapannya sebagai Scrum atau PxP. |
| Ramadhan dan Widodo (2026), Rams Dimsum | Pendukung 2.3.3 dan 2.3.4 tentang pencatatan cabang dan informasi pusat. | Studi kualitatif akuntansi, bukan hasil pengembangan aplikasi. Salinan saat ini berjumlah 15 halaman; bagian relevan terdapat pada PDF 14 sampai 15, sehingga lokator PDF 17 dari catatan lama tidak digunakan. |
| Barizi, Anshary, dan Sumarni (2023), sekolah musik ABC | Tambahan pembanding administrasi siswa, kursus, pembayaran, dan jadwal. | Aplikasi Java dan MySQL; tetap berguna untuk fungsi meskipun platform berbeda. |
| Safitri, Listyorini, dan Supriyati (2026), Bimbel Ilman Nafi | Pendukung 2.2.1 dan pembanding mekanisme komunikasi. | Artikel membahas notifikasi otomatis; ARTHA menggunakan tombol tautan WhatsApp dan pengiriman manual. |
| Tiana dan Gunanto (2026), bimbel web-mobile | Alternatif pembanding administrasi bimbel atau konteks 2.3.2. | Pilih bila ada temuan yang belum diwakili Bee Hive, RSDC, dan Jia Jia. |
| Abadi, Wasino, dan Lina (2025), pembayaran SPP dan penggajian guru | Pendukung 2.3.4 atau alternatif pembanding pembayaran. | Fokus ambil pada pembayaran, sebab penggajian tidak otomatis menjadi lingkup ARTHA. |
| Karpina dkk. (2025), pembayaran LOOP Coding | Alternatif pembanding pembayaran dan rekap periodik. | Manfaatnya bertumpang tindih dengan sumber pembayaran utama; tidak harus ditambahkan sekadar memperbanyak tabel. |
| Fikri dan Arthawan Sugih Prabowo, buku tamu DPOP | Pendukung penerapan PxP pada konteks lokal; alternatif baris metodologi. | Cocokkan penulis dan kebijakan tahun sitasi: edisi Desember 2020 dan metadata terbit daring 2021. Jangan menyalin nama dari dokumen komparasi lama yang keliru. |
| Priatmaja, Nuryasin, dan Suharso (2022), laboratorium Infokom | Alternatif pembanding PxP yang relevan untuk administrasi kegiatan. | Identitas pada PDF: REPOSITOR 4(4), 429 sampai 439. Bukan 4(1) atau penulis Prabowo dan Ginanjar sebagaimana dokumen komparasi lama. |
| Amelia dkk. (2026), monitoring belajar AHE | Cadangan, bukan prioritas tabel utama. | Monitoring belajar dan WhatsApp Gateway lebih jauh dari dashboard administrasi internal yang direncanakan. |
| Pradana (2024), peran TI dalam manajemen pendidikan | Pendukung konteks 2.3.1 dan 2.3.2. | Kajian literatur umum, sehingga tidak disamakan dengan implementasi sistem sejenis. |
| Astiti (2023), company profile XP | Tidak diprioritaskan untuk penelitian terdahulu utama. | Objek company profile lebih jauh dari transaksi, pengaturan cabang, dan administrasi bimbel. |
| Suputra dkk. (2026), sistem siswa dengan XP | Cadangan untuk contoh implementasi XP. | Pakai bila diperlukan pada perbandingan metode; teori XP tetap bertumpu pada sumber dasarnya. |
| Kurniawan dan Sani (2019), Scrum klinik | Contoh implementasi Scrum pada 2.1.2, bukan pembanding fungsi utama ARTHA. | Aturan Scrum dirujuk dari Scrum Guide 2020, bukan generalisasi seluruh pernyataan artikel penerapan. |
| Pratama, Krisgianti, dan Paramita (2023), RAD inventaris aset desa | Contoh penerapan RAD pada 2.1.2. | Berkas di folder 01 dan 04 memuat artikel yang sama; hitung satu sumber, bukan dua penelitian. |
| Putra (2022), absensi dengan prototyping | Contoh prototyping bila diperlukan di 2.1.1. | Fokus absensi pegawai tidak menjadi fungsi utama rancangan ARTHA. |
| Sari, Geges, dan Hasanah (2023), pembayaran dengan WhatsApp API dan Midtrans | Pembanding opsional terhadap batas lingkup pembayaran dan komunikasi. | Tidak menjadi dasar menyatakan ARTHA memakai payment gateway atau WhatsApp API. |

Buku, panduan metode, dan prosiding dasar ditempatkan terutama pada kajian metode dan dasar teori. PDF pada folder `JURNAL/BAB 1` yang merupakan salinan bertanda tidak dihitung sebagai penelitian baru, sedangkan SK akreditasi merupakan bukti status jurnal dan bukan artikel penelitian.

## 4. Isi dan rujukan setiap subbab

| Subbab | Isi yang diperlukan | Sumber yang dipakai atau masih perlu dilengkapi |
| :--- | :--- | :--- |
| 2.1.1 | Pengertian luaran prototipe, pengembangan sistem, dan perbedaan produk prototipe dengan metode Prototyping. | Template dan panduan ITK untuk bentuk luaran; Sommerville dan Pressman untuk proses serta prototyping. |
| 2.1.2 | Perbandingan pendekatan adaptif dan alasan pemilihan berdasarkan karakter proyek, pengendalian kualitas, dan pencatatan individual. | Sommerville; Beck dan Andres; Scrum Guide 2020; Pratama dkk. sebagai contoh RAD; audit komparasi yang telah dikoreksi. Waterfall cukup pembanding pengantar. |
| 2.1.3 | Prinsip, tahapan, praktik, perencanaan tugas, pencatatan waktu dan cacat, serta retrospeksi PxP. | Dzhurov dkk. (2009) sebagai sumber dasar; Sidiq, Apriyanti, Priatmaja, dan Fikri sebagai penerapan. |
| 2.1.4 | Hubungan peramban, antarmuka, API, server, basis data, serta autentikasi dan otorisasi. | Buku rekayasa perangkat lunak dan dokumentasi resmi teknologi. Diagram arsitektur ARTHA secara rinci ditempatkan di Bab 3. |
| 2.1.5 | Peran Next.js, React, Laravel, Sanctum, MySQL, dan tautan WhatsApp yang digunakan. | Dokumentasi resmi masing-masing; jurnal hanya contoh penggunaan. Versi, konfigurasi, dan perangkat rinci berada di Bab 3. |
| 2.1.6 | Pengujian berdasarkan spesifikasi, hasil yang diharapkan, serta EP dan BVA jika tetap dijanjikan di Bab 3. | Literatur atau silabus pengujian primer perlu dilengkapi secara lokal. Artikel yang hanya menyebut Black Box tidak otomatis mendukung teknik EP dan BVA. |
| 2.1.7 | Tujuan penerimaan pengguna, kriteria penerimaan, evaluasi berbasis tugas, pencatatan kendala, dan uji ulang. | Literatur pengujian sebagai dasar; Apriyanti dan INET sebagai contoh penerapan. Hindari menyamakan skor kepuasan dengan keberhasilan tugas. |
| 2.2 | Masalah, pendekatan, fitur, teknologi, bukti evaluasi, serta hubungan dan batas pembanding terhadap ARTHA. | Sepuluh artikel prioritas dan sumber tambahan bila diperlukan. |
| 2.3.1 | Data, informasi, proses, keluaran, dan informasi untuk pengelolaan operasional. | Laudon dan Laudon yang tersedia adalah edisi ke-13 global, hak cipta 2014. Jangan menggunakan tahun 2020 untuk PDF ini. |
| 2.3.2 | Pendidikan nonformal dan administrasi bimbel, termasuk siswa, tentor, jadwal, dan pembayaran. | UU 20/2003 sesuai pasal yang relevan; artikel bimbel; wawancara digunakan sebagai bukti kondisi ARTHA, bukan teori universal. |
| 2.3.3 | Data berdasarkan cabang, akses berdasarkan peran dan objek, serta informasi yang dihimpun pusat. | Ahadi dan Thiovanda sebagai penerapan; buku atau dokumentasi otorisasi untuk konsep dasar. Dua peran ARTHA tetap keputusan rancangan. |
| 2.3.4 | Tagihan, penerimaan tunai, pengajuan transfer, verifikasi, setoran cabang, dan pencocokan mutasi. | Hendri; Sudirman dan Tristianti; Ramadhan dan Widodo. Batas pencocokan operasional ARTHA harus dibedakan dari laporan keuangan dan rekonsiliasi akuntansi penuh. |
| 2.3.5 | Kapasitas kelas dan ruang, siswa aktif, kondisi hampir penuh dan penuh, serta irisan jadwal. | Kabisatullah dan Noprisson; Khafidhoh; batas aktual dan pengecualian berasal dari mitra. Tidak perlu teori algoritma genetika lengkap jika tidak digunakan. |
| 2.3.6 | Kebutuhan fungsional dan nonfungsional, cerita pengguna, use case, skenario, serta entitas, relasi, kunci dan integritas data. | Sommerville dan Pressman; sumber primer UML dan basis data dapat dilengkapi. Contoh ERD pada jurnal tidak menggantikan teori relasi atau normalisasi. |

Penjelasan teknologi tidak perlu menjadi kamus panjang tentang semua bahasa dan alat yang muncul pada artikel. Konsep yang diterangkan dipilih karena dipakai untuk memahami desain, implementasi, atau pengujian ARTHA.

## 5. Bentuk tabel penelitian terdahulu

Template memberikan contoh kolom nomor, nama dan tahun, serta hasil yang memuat teknologi dan fitur atau metode utama. Bentuk yang lebih analitis dapat disajikan dengan kolom tambahan apabila tetap mudah dibaca dan mengikuti persetujuan pembimbing.

| Kolom | Isi yang dicatat |
| :--- | :--- |
| Nama, tahun, dan objek | Identitas benar serta konteks studi. |
| Masalah dan tujuan | Masalah yang benar-benar diteliti, bukan fakta ARTHA yang dipindahkan ke artikel. |
| Metode dan teknologi | Pisahkan pendekatan penelitian, metode pengembangan, teknik khusus, dan perangkat lunak. |
| Fitur serta hasil pengujian | Nyatakan fitur dan bukti evaluasi yang dilaporkan sumber; tandai bila rincian pengujian tidak dijelaskan. |
| Keterkaitan dan pembeda ARTHA | Jelaskan bagian yang diadaptasi dan lingkup yang berbeda, tanpa merendahkan atau mengarang kekurangan penelitian terdahulu. |
| Lokator sumber | Catatan kerja halaman untuk pemeriksaan; dapat dipindah ke peta rujukan pendamping jika tabel proposal terlalu lebar. |

Jika tabel menjadi terlalu lebar dalam Word, gunakan tiga kolom sesuai contoh template dan pisahkan isi sel hasil menjadi teknologi, metode, fitur, serta evaluasi. Persamaan, perbedaan, dan posisi ARTHA kemudian diuraikan dalam paragraf sintesis setelah tabel.

## 6. Posisi penelitian dan celah yang perlu dirumuskan secara hati-hati

Artikel Thiovanda telah menampilkan cabang, pembatasan admin berdasarkan cabang, serta verifikasi pembayaran oleh head admin. Oleh sebab itu, klaim Bab 1 bahwa penelitian sejenis belum membahas bimbel multicabang tidak dapat dipertahankan secara umum hanya berdasarkan kumpulan artikel ini.

Posisi yang lebih layak dikaji adalah penyesuaian sistem terhadap alur spesifik ARTHA yang menghubungkan administrasi cabang, pencatatan penerimaan tunai dan transfer, pencocokan dana masuk di pusat, serta pengendalian kapasitas dan jadwal. Fitur tersebut perlu dibandingkan satu per satu dengan isi penelitian terdekat, dengan menggunakan ungkapan “belum dijelaskan secara rinci dalam artikel yang ditelaah” apabila bukti hanya berupa ketiadaan uraian dalam naskah.

Penggunaan PxP memperjelas cara pengembangan dan bukti proses yang akan dikumpulkan, tetapi mengganti metode saja tidak otomatis menghasilkan kebaruan. Kontribusi yang dapat dipertanggungjawabkan berasal dari kesesuaian rancangan dengan masalah ARTHA dan hasil evaluasi yang nantinya benar-benar dilaksanakan.

## 7. Penyelarasan sebelum mulai menulis

Terdapat ketidaksesuaian yang masih terlihat antara Bab 1 dan Bab 3 mengenai petugas verifikasi transfer. Bab 1 versi revisi malam menyebut Admin Cabang memverifikasi, sedangkan rancangan Bab 3 menempatkan keputusan pada Super Admin; hal ini perlu diselaraskan sebelum peran tersebut dijadikan dasar penjelasan Bab 2.

Langkah berikut dapat dilakukan tanpa menunggu seluruh Bab 2 ditulis. Pekerjaannya dimulai dari matriks sumber agar paragraf yang disusun memiliki rujukan yang jelas.

1. Gunakan sepuluh artikel prioritas sebagai daftar kerja awal, kemudian baca metode dan hasil setiap artikel sebelum mengisi tabel final.
2. Pertahankan jurnal tambahan untuk kebutuhan teori atau aspek fungsi yang belum terwakili, tanpa menambahkan semua artikel ke tabel utama.
3. Perbaiki identitas sumber sesuai PDF dan penerbit, terutama Sidiq, Priatmaja, Fikri, dan buku Laudon.
4. Susun matriks perbandingan yang secara eksplisit memasukkan Thiovanda sebagai pembanding multicabang terdekat.
5. Lengkapi sumber primer pengujian, UML, dan basis data bila uraian pada buku yang tersedia belum mencukupi. Sumber baru tidak harus jurnal bila konsepnya berasal dari standar atau dokumentasi resmi.
6. Sinkronkan petugas verifikasi transfer dan batas pencocokan penerimaan dengan Bab 1 dan Bab 3.
7. Verifikasi cakupan akreditasi edisi untuk artikel yang masih bertanda belum pasti pada audit sebelumnya, jika seluruh baris utama diwajibkan berasal dari edisi terakreditasi oleh pembimbing.

## 8. Batas pemeriksaan

Sebanyak 27 berkas PDF dalam empat kelompok artikel aplikasi telah diekstraksi untuk pemetaan ini, termasuk dua salinan artikel RAD yang sama. Buku, sumber dasar metode, template, dan audit sumber terdahulu digunakan untuk membagi fungsi rujukan; pemeriksaan ini bukan penulisan narasi lengkap Bab 2 atau audit SINTA baru untuk seluruh koleksi.

Berkas yang bernama perbandingan XP dan PxP tetapi berisi aplikasi NTE tidak dipakai sebagai bukti perbandingan metode. Sumber Ramadhan dan Widodo tentang akuntansi pusat dan cabang berbeda dari sumber “Ramadhan keanggotaan dan penjadwalan PxP” yang tidak ditemukan pada audit komparasi.

Metadata Thiovanda diverifikasi pada [laman penerbit](https://journal.untar.ac.id/index.php/jiksi/article/view/36813), sedangkan identitas Sidiq dicocokkan dengan [Jurnal Jaring SainTek](https://ejurnal.ubharajaya.ac.id/index.php/jaring-saintek/article/view/744). Pemeriksaan ulang tersebut memperbaiki metadata yang sebelumnya masih belum lengkap tanpa menganggap status penerbitan sama dengan status akreditasi.

## 9. Tautan sepuluh artikel prioritas

Tautan berikut mengarah ke berkas asli dalam koleksi JURNAL. Gunakan lokator pada Bagian 2 untuk memeriksa bagian yang akan dirujuk sebelum menulis parafrase.

- [SI Bimbel Bee Hive - Efisiensi Operasional - JRIS - Fajriansyah dkk - 2026.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/02_STUDI_KASUS_BIMBEL_DAN_KURSUS/SI Bimbel Bee Hive - Efisiensi Operasional - JRIS - Fajriansyah dkk - 2026.pdf>)
- [SI Bimbel RSDC - Web - Waterfall - RJTI - Gunawan dkk - 2025.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/02_STUDI_KASUS_BIMBEL_DAN_KURSUS/SI Bimbel RSDC - Web - Waterfall - RJTI - Gunawan dkk - 2025.pdf>)
- [SI Penjadwalan & Pembayaran Les Jia Jia Education - Web - Thiovanda.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/02_STUDI_KASUS_BIMBEL_DAN_KURSUS/SI Penjadwalan & Pembayaran Les Jia Jia Education - Web - Thiovanda.pdf>)
- [01_Multicabang_Hotel_Laravel_Djtechno_Ahadi_2025.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/01_Multicabang_Hotel_Laravel_Djtechno_Ahadi_2025.pdf>)
- [05_Penerimaan Kas.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/05_Penerimaan Kas.pdf>)
- [06_Rekonsiliasi_Kas_Bank_MEANS_Sudirman_2021.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/06_Rekonsiliasi_Kas_Bank_MEANS_Sudirman_2021.pdf>)
- [03_Penjadwalan_Bimbel_AHE_JTI_Khafidhoh_2026.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/03_Penjadwalan_Bimbel_AHE_JTI_Khafidhoh_2026.pdf>)
- [04_Kapasitas_Ruang_RapaTrack_JUSIBI_Kabisatullah_2026.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/05_REFERENSI_TAMBAHAN_TERVERIFIKASI_SINTA/04_Kapasitas_Ruang_RapaTrack_JUSIBI_Kabisatullah_2026.pdf>)
- [SI Surat Menyurat - Personal Extreme Programming (PxP) - Sidiq dkk - 2025.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/SI Surat Menyurat - Personal Extreme Programming (PxP) - Sidiq dkk - 2025.pdf>)
- [Website E-Kavling - PxP & UAT - JATI - Apriyanti dkk - 2024.pdf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU/Website E-Kavling - PxP & UAT - JATI - Apriyanti dkk - 2024.pdf>)
