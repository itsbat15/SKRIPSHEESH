# BAB 3
# RANCANGAN PROTOTIPE

Bab ini menguraikan rancangan prototipe sistem informasi manajemen operasional berbasis web untuk Bimbingan Belajar Artha Balikpapan. Pembahasan mencakup garis besar prototipe, tahapan pembuatan, prosedur pengembangan, konsep sistem, spesifikasi teknis, dan rencana jadwal pelaksanaan. Susunan subbab mengikuti template tugas akhir jalur prototipe (Institut Teknologi Kalimantan, 2025b).

## 3.1 Garis Besar Prototipe

Prototipe ARTHA berupa sistem informasi manajemen operasional berbasis web untuk Bimbel Artha Balikpapan. Sistem menghubungkan administrasi siswa, kelas, jadwal, tagihan, dan penerimaan pada delapan cabang melalui kewenangan Admin Cabang serta Super Admin.

### 3.1.1 Objek dan Konteks Pengembangan

Kebutuhan pengembangan bersumber dari dokumentasi wawancara pengelola dan staf administrasi Artha. Penelitian sistem bimbel digunakan sebagai pembanding integrasi data siswa, jadwal, dan pembayaran (Fajriansyah dkk., 2026, hlm. 116, 124 sampai 125; Gunawan dkk., 2025, hlm. 424).

### 3.1.2 Ruang Lingkup dan Pengguna Prototipe

Admin Cabang mengelola kegiatan pada cabang penugasannya, sedangkan Super Admin memantau lintas cabang dan menjalankan pengendalian berwenang. Pemisahan akses cabang dan pemantauan pusat mempunyai pembanding pada Ahadi dkk. (2025, hlm. 764 sampai 765) serta Thiovanda (2026, hlm. 4).

Pengingat tunggakan menggunakan tombol WhatsApp dengan nomor dan pesan yang disiapkan sistem, kemudian dikirim oleh admin. Pengelolaan kelas menyediakan peringatan hampir penuh dan menolak penambahan ketika penuh, sementara tempat kembali tersedia setelah keanggotaan siswa diakhiri.

Pembayaran transfer dirancang melalui pengajuan Admin Cabang dan pemeriksaan Super Admin, dengan kewenangan rekening yang akan divalidasi bersama mitra. Lingkup inti mencakup administrasi internal dan pencocokan penerimaan manual, sedangkan pengiriman WhatsApp otomatis, integrasi bank otomatis, serta pembelajaran daring berada di luar lingkup tersebut.

### 3.1.3 Pendekatan Pengembangan Prototipe

Pengembangan individual menggunakan metode *Personal Extreme Programming* (PxP), yang meliputi penggalian kebutuhan, perencanaan, inisialisasi iterasi, perancangan, implementasi, pengujian sistem, dan evaluasi iterasi (Dzhurov dkk., 2009, hlm. 253 sampai 256). Penelitian Fikri dan Arthawan Sugih Prabowo (2021, hlm. 103 sampai 105) menjadi pembanding penerapannya pada pengembangan sistem informasi.

### 3.1.4 Luaran yang Ditargetkan

Luaran yang ditargetkan meliputi perangkat lunak prototipe, dokumentasi pengembangan, dan bukti evaluasi bersama calon pengguna. Pengembangan diarahkan pada TKT 5 sesuai panduan tugas akhir prototipe, dengan bukti pencapaian yang akan diperiksa berdasarkan pelaksanaan (Institut Teknologi Kalimantan, 2026, hlm. 4).

Dokumentasi disiapkan untuk laporan, artikel ilmiah, dan bahan pengajuan HKI. Hasil pengujian dan penerimaan mitra akan dilaporkan setelah kegiatan dilaksanakan.

## 3.2 Tahapan Pembuatan Prototipe

Tahapan pembuatan disusun sebagai alur kerja dari penggalian kebutuhan sampai penyiapan luaran. Gambar 3.1 menyajikan urutan tersebut beserta perulangan evaluasi dan perbaikan yang direncanakan.

![Diagram alir pembuatan prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_1_Alur_Pembuatan_Prototipe.png>)

**Gambar 3.1 Alur Pembuatan Prototipe Sistem Informasi ARTHA**

Sumber: Dzhurov dkk. (2009, hlm. 254 sampai 256), telah diolah dengan penambahan evaluasi pengguna dan penyiapan luaran penelitian.

Penggalian kebutuhan dan perencanaan menjadi dasar pemilihan pekerjaan setiap iterasi. Setelah implementasi, fungsi yang selesai diperiksa melalui pengujian sistem, kemudian waktu kerja, galat, dan usulan perbaikan ditelaah pada evaluasi iterasi.

Hasil pengujian yang belum memenuhi kriteria dikembalikan ke implementasi untuk diperbaiki dan diuji ulang sebelum iterasi ditutup. Setelah evaluasi iterasi, pekerjaan tersisa diarahkan ke inisialisasi berikutnya, sedangkan fungsi yang siap diarahkan ke UAT.

Masukan UAT yang mengubah kebutuhan dikembalikan ke penggalian kebutuhan serta perencanaan. Masukan yang hanya memerlukan koreksi fungsi dikembalikan ke pekerjaan perbaikan, kemudian diuji ulang sebelum keputusan penerimaan dan penyiapan luaran.

Evaluasi penerimaan pengguna dilakukan pada modul yang telah memenuhi pemeriksaan awal. Penggabungan pengembangan PxP dengan pengujian sistem dan evaluasi pengguna mempunyai contoh penerapan pada Apriyanti dkk. (2024, hlm. 3680, 3683 sampai 3685), tetapi instrumen penelitian ini disesuaikan dengan tugas operasional ARTHA.

Tabel 3.1 merangkum kegiatan dan luaran setiap tahap pada Gambar 3.1. Rincian pelaksanaannya dijelaskan pada Subbab 3.3 agar hubungan antara diagram dan prosedur dapat diperiksa.

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

Prosedur menjelaskan pelaksanaan setiap kegiatan pada diagram alir. Instrumen, sumber data, pemeriksaan hasil, dan bentuk dokumentasi ditetapkan agar pengembangan dapat ditelusuri dari kebutuhan sampai evaluasi.

### 3.3.1 Penggalian Kebutuhan (*Requirements*)

Penggalian kebutuhan diawali dengan penelaahan transkrip wawancara pengelola dan staf administrasi yang telah tersedia. Setiap informasi dipetakan menurut topik, yaitu pendaftaran, tarif, pembayaran, pengelolaan kelas, jadwal tentor, dan pelaporan cabang.

Informan klarifikasi dipilih berdasarkan tanggung jawab serta pengetahuan terhadap proses yang diperiksa. Pengelola pusat digunakan sebagai sumber kebutuhan pemantauan dan kewenangan, sedangkan staf administrasi digunakan sebagai sumber pelaksanaan pencatatan pada cabang.

Jumlah informan, identitas atau kode, cabang yang diwakili, tanggal, serta alasan pemilihannya akan dicatat dalam dokumentasi penelitian. Keterangan satu cabang tidak diberlakukan sebagai ketentuan seluruh cabang sebelum cakupannya dipastikan kepada pengelola.

Tabel 3.2 membedakan dokumen yang telah tersedia dari klarifikasi yang masih direncanakan. Tanggal pelaksanaan akan dicocokkan dengan bukti asli karena penulisan tanggal pada notulensi belum seluruhnya tervalidasi.

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

Indeks berkas, penanda waktu, dan batas penafsiran disimpan pada lampiran sumber kebutuhan. Catatan tarif atau peristiwa pada satu cabang digunakan sesuai konteksnya sampai pengelola menetapkan cakupan yang lebih luas.

Wawancara lanjutan dilakukan secara semiterstruktur dengan panduan topik yang tetap memungkinkan pertanyaan klarifikasi. Topik instrumen disajikan pada Tabel 3.3, sedangkan pertanyaan rinci dan catatan pelaksanaan akan ditempatkan pada lampiran.

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

Dokumen yang dapat ditelaah meliputi contoh kuitansi, daftar siswa, jadwal, rekap pembayaran, serta contoh bukti transfer yang penggunaannya diizinkan mitra. Apabila pengamatan langsung dilakukan, waktu, objek, dan hasilnya dicatat secara terpisah dari keterangan wawancara.

Analisis kebutuhan dilakukan dengan mengelompokkan informasi, menandai pernyataan yang berbeda, dan mengubah kebutuhan yang telah diklarifikasi menjadi fungsi sistem. Pencatatan kebutuhan dalam bentuk *user story* mempunyai contoh pada Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105) serta Sidiq dkk. (2025, hlm. 37).

Setiap kebutuhan diberi kode, sumber, cakupan cabang, dan status validasi. Pernyataan faktual, potensi risiko, dan usulan fitur dibedakan agar kebutuhan preventif tidak ditulis sebagai kejadian yang sudah berulang.

Validasi dilakukan dengan meminta perwakilan mitra meninjau ringkasan proses dan kebutuhan yang berkaitan dengan kewenangannya. Perubahan setelah peninjauan disimpan dalam riwayat revisi, kemudian digunakan sebagai dasar perencanaan iterasi.

### 3.3.2 Perencanaan (*Planning*)

Perencanaan dilakukan dengan memecah kebutuhan menjadi tugas analisis, perancangan, pengodean, pengujian, dan perbaikan. Estimasi awal menggunakan rincian pekerjaan, kemudian diperbarui berdasarkan durasi aktual pada tugas sejenis (Dzhurov dkk., 2009, hlm. 254 sampai 255).

Empat iterasi diusulkan berdasarkan ketergantungan data dan proses pada Tabel 3.4. Akun, cabang, siswa, kelas, dan tarif menjadi prasyarat penempatan, penjadwalan, transaksi, serta rekap pusat.

**Tabel 3.4 Rencana Iterasi dan Ketergantungan Kebutuhan**

| Iterasi | Kebutuhan dan cerita pengguna | Lingkup pekerjaan | Prasyarat dan keluaran |
| :--- | :--- | :--- | :--- |
| I-01 | KF-01, KF-02, KF-03, KF-06, KF-14; US dengan nomor yang sama | Akun, cabang, siswa, ruang, kelas, serta dasar tarif dan tagihan | Data dasar dan pembatasan akses dapat diperiksa |
| I-02 | KF-04, KF-05; US-04 dan US-05 | Keanggotaan, kapasitas, jadwal, serta pemeriksaan irisan | Master I-01 tersedia; kelas penuh dan konflik diuji |
| I-03 | KF-07, KF-08, KF-09, KF-10; US dengan nomor yang sama | Tunai, pengajuan transfer, pemeriksaan, serta tautan WhatsApp | Tagihan tersedia; layanan pencocokan transfer dasar dibuat agar verifikasi dapat diuji |
| I-04 | KF-11, KF-12, KF-13; US dengan nomor yang sama | Setoran, rekap pusat, pencocokan, serta integrasi | Penerimaan I-03 tersedia; transaksi sumber dapat ditelusuri |

Pencocokan transfer pada I-03 memakai komponen dasar rekening dan referensi bank yang diperlukan untuk persetujuan. Pada I-04, komponen tersebut diperluas untuk pencocokan setoran tunai dan rekap lintas proses.

Setiap iterasi dialokasikan dua minggu sebagai rencana awal dalam rentang iterasi PxP satu sampai tiga minggu (Dzhurov dkk., 2009, hlm. 255). Rincian jam per tugas belum ditetapkan dan akan diisi sebelum iterasi dimulai, sedangkan kalender dua belas minggu pada Subbab 3.6 masih bersifat relatif.

Permintaan perubahan dicatat bersama sumber, kebutuhan terdampak, ketergantungan, serta pengaruhnya terhadap waktu dan pengujian. Formulir estimasi dan perubahan ditempatkan pada lampiran pelaksanaan agar penambahan pekerjaan tetap dapat ditelusuri.

### 3.3.3 Inisialisasi Iterasi (*Iteration Initialization*)

Pada awal iterasi, daftar tugas dipilih dari rencana yang telah diperiksa. Setiap tugas dilengkapi kode kebutuhan, penanggung jawab pengembangan, estimasi waktu, data uji, dan kriteria selesai.

Data uji disiapkan untuk mewakili cabang yang berbeda dan kondisi normal maupun tidak sah. Identitas siswa dan bukti pembayaran menggunakan data buatan atau data tersamarkan sesuai izin mitra.

Perubahan perangkat lunak disimpan dalam repositori kode dengan penanda versi. Pencatatan waktu dilakukan per tugas agar durasi analisis, perancangan, pengodean, pengujian, serta perbaikan dapat dibedakan.

Tugas dinyatakan selesai secara teknis apabila kriteria penerimaannya terpenuhi dan tidak terdapat galat kritis yang belum ditangani. Penerimaan oleh mitra dicatat tersendiri, sehingga selesainya pengodean tidak disamakan dengan persetujuan pengguna.

### 3.3.4 Perancangan (*Design*)

Perancangan dilakukan untuk modul yang akan dikerjakan pada iterasi berjalan. Model yang disusun meliputi kewenangan pengguna, alur tugas, hubungan data, dan susunan antarmuka.

Pemilihan artefak disesuaikan dengan kebutuhan implementasi, sebagaimana anjuran penggunaan alat desain sederhana pada Dzhurov dkk. (2009, hlm. 255). Fikri dan Arthawan Sugih Prabowo (2021, hlm. 104) juga menggunakan rancangan basis data dan antarmuka sebagai bagian pengembangan sistem.

Rancangan proses memisahkan penerimaan pembayaran siswa, pemeriksaan transfer, dan penyerahan kas cabang. Pemisahan ini diperlukan agar pencatatan penerimaan tidak dihitung kembali sebagai pendapatan baru ketika dana disetorkan ke pusat.

Rancangan kelas memisahkan ruang fisik, kelompok belajar, dan keanggotaan siswa. Kapasitas diperiksa berdasarkan peserta aktif pada kelompok yang dipilih, sedangkan riwayat siswa keluar tetap disimpan untuk penelusuran data.

Rancangan modul kemudian diperiksa terhadap kebutuhan dan kasus uji yang terkait. Apabila ditemukan aturan yang belum jelas, pertanyaan klarifikasi dicatat sebelum aturan tersebut diterapkan pada kode.

### 3.3.5 Implementasi (*Implementation*)

Implementasi dilakukan melalui pengujian unit, pengodean fungsi, dan refaktorisasi. Urutan pengujian sebelum kode dan perbaikan struktur mengikuti praktik implementasi PxP yang dijelaskan oleh Dzhurov dkk. (2009, hlm. 255).

Penerapan *Test-Driven Development* (TDD) diprioritaskan pada aturan bisnis yang dapat diuji secara otomatis. Aturan tersebut meliputi penghitungan sisa tagihan, penolakan penambahan kelas penuh, dan pemeriksaan irisan waktu penugasan tentor.

Untuk setiap aturan, pengujian disusun sebelum fungsi dilengkapi, kemudian kode dikembangkan sampai keluaran yang diharapkan terpenuhi. Bukti pengujian gagal, pengujian lulus, dan perubahan terkait disimpan agar penerapan TDD dapat diperiksa.

Kode yang telah memenuhi pengujian ditinjau untuk mengurangi pengulangan dan memperjelas pembagian tanggung jawab. Setelah refaktorisasi, pengujian dijalankan kembali untuk memastikan fungsi sebelumnya tetap bekerja sesuai kriteria.

Integrasi antarmuka dan layanan data dilakukan secara bertahap. Pemeriksaan akses diterapkan pada peladen, sehingga perubahan alamat halaman atau identitas objek oleh pengguna tidak memberikan akses ke data cabang lain.

### 3.3.6 Pengujian Sistem (*System Testing*)

Pengujian sistem menggunakan pendekatan kotak hitam atau *Black Box Testing* untuk memeriksa keluaran terhadap kebutuhan. Penerapannya bersama PxP mempunyai pembanding pada Apriyanti dkk. (2024, hlm. 3679, 3683), sedangkan kasus ARTHA disusun dari aturan akses, kelas, dan transaksi.

Pengembang melaksanakan pemeriksaan pada lingkungan uji terpisah dengan data buatan atau tersamarkan. Identitas versi, perangkat, zona waktu, dan data awal dicatat sebelum kasus dijalankan agar hasil dapat diperiksa ulang.

Tabel 3.5 menampilkan contoh kasus berisiko, sedangkan seluruh kasus BB-01 sampai BB-33 disimpan pada lampiran pengujian. Kelompok pemeriksaan PU-01 sampai PU-14 menghubungkan kasus tersebut dengan kebutuhan fungsional pada Tabel 3.13.

**Tabel 3.5 Contoh Kasus Pengujian Sistem**

| Kode | Kondisi yang diperiksa | Keluaran yang diharapkan | Pelaksanaan |
| :--- | :--- | :--- | :--- |
| BB-01 | Akun cabang meminta objek cabang lain | Akses ditolak dan objek tidak dikirim | Belum diuji |
| BB-07 | Dua permintaan mengisi satu tempat terakhir | Hanya satu keanggotaan aktif baru tersimpan | Belum diuji |
| BB-14 | Pengajuan dikembalikan kemudian diajukan ulang | Pengajuan lama tetap tersimpan dan pengajuan baru tertaut | Belum diuji |
| BB-16 | Persetujuan transfer dikirim berulang | Penerimaan, alokasi, serta pencocokan hanya berlaku sekali | Belum diuji |
| BB-17 | Admin membuka pesan tunggakan | Nomor dan isi sesuai; pembukaan tidak dianggap bukti terkirim | Belum diuji |
| BB-20 | Setoran kas dicocokkan dengan dana bank | Status setoran berubah tanpa menambah penerimaan siswa | Belum diuji |

Setiap kasus merekam prasyarat, langkah, masukan, keluaran yang diharapkan, hasil aktual, serta bukti pelaksanaan. Galat kritis meliputi akses cabang tanpa kewenangan, penghitungan pembayaran ganda, dan pelampauan kapasitas kelas.

Perbaikan diperiksa melalui pengulangan kasus gagal beserta kasus terkait. Hasil sebelum perbaikan tetap disimpan dan dihubungkan dengan versi yang diperiksa ulang.

### 3.3.7 Evaluasi Iterasi (*Retrospective*)

Evaluasi iterasi dilakukan dengan membandingkan rencana pekerjaan dan data pelaksanaan. Waktu aktual, perubahan kebutuhan, galat, serta pekerjaan yang belum selesai ditelaah untuk menentukan perbaikan iterasi berikutnya.

Pemanfaatan data proyek dalam evaluasi merupakan bagian proses PxP pada Dzhurov dkk. (2009, hlm. 256). Sidiq dkk. (2025, hlm. 45) juga melaporkan perubahan kebutuhan dan perbedaan durasi, sehingga waktu implementasi perlu dibedakan dari keseluruhan waktu pengembangan.

Tabel 3.6 menyajikan unsur pencatatan proses yang direncanakan. Formulir diisi selama pelaksanaan, bukan direkonstruksi sebagai angka perkiraan setelah proyek selesai.

**Tabel 3.6 Unsur Dokumentasi Evaluasi Iterasi**

| Dokumen | Unsur yang dicatat | Penggunaan analisis |
| :--- | :--- | :--- |
| Catatan waktu | Kode tugas, kategori, estimasi, waktu mulai, waktu selesai, dan durasi aktual | Selisih estimasi dan aktual beserta penyebabnya |
| Catatan galat | Kode galat, versi, pemicu, tingkat kepentingan, perbaikan, dan uji ulang | Galat terbuka, galat terselesaikan, dan pola kesalahan |
| Catatan perubahan | Asal permintaan, kebutuhan terdampak, keputusan, dan perubahan jadwal | Perubahan ruang lingkup dan tindak lanjut |
| Usulan perbaikan proses | Masalah, bukti, tindakan, dan hasil pemeriksaan berikutnya | Penyesuaian cara kerja pada iterasi selanjutnya |

Selisih durasi dihitung dengan mengurangkan estimasi dari waktu aktual pada tugas yang sama. Nilai tersebut ditafsirkan bersama penyebabnya, sehingga keterlambatan karena perubahan kebutuhan tidak disamakan dengan kesalahan pengodean.

Hasil evaluasi digunakan untuk memperbaiki estimasi, pembagian tugas, atau pengujian berikutnya. Formulir lengkap catatan waktu, galat, perubahan, dan evaluasi ditempatkan pada lampiran pelaksanaan.

### 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi

Pengujian penerimaan pengguna atau *User Acceptance Testing* (UAT) dilakukan bersama petugas yang menjalankan administrasi cabang dan pengawasan pusat. Pemilihan peserta dilakukan secara bertujuan menurut kewenangan, pengalaman tugas, kesediaan, dan cakupan proses yang diuji.

Rencana peserta mencakup sekurang-kurangnya perwakilan kedua peran, sedangkan nama, jumlah akhir, cabang, serta waktu pertemuan ditetapkan bersama mitra. Petugas yang sama dapat menilai beberapa tugas sesuai kewenangannya, tetapi penerimaan satu cabang tidak digeneralisasi sebagai pendapat seluruh delapan cabang.

Sebelum UAT, pengembang menyiapkan versi uji, cadangan awal, akun terpisah, data simulasi, dan panduan singkat. Pemeriksaan awal memastikan fungsi inti dapat dijalankan serta peserta hanya memperoleh hak yang diperlukan untuk tugasnya.

Pelaksanaan diawali pengarahan tujuan, penjelasan data uji, dan persetujuan pencatatan bukti. Peserta kemudian menjalankan tugas tanpa perubahan langkah yang tidak terdokumentasi, sedangkan pengembang mengamati, mencatat bantuan yang diberikan, dan menyimpan hasil sesuai kode tugas.

Tabel 3.7 merangkum tugas penerimaan dengan A sebagai Admin Cabang dan S sebagai Super Admin. Lembar rinci memuat identitas peserta atau kode, versi aplikasi, langkah, hasil aktual, bantuan, keputusan, alasan, serta penunjuk bukti.

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

Instrumen diperiksa keterbacaan dan kesesuaian isinya oleh pembimbing serta perwakilan mitra sebelum pelaksanaan. Penggunaan evaluasi bersama pengguna mempunyai pembanding pada Apriyanti dkk. (2024, hlm. 3683 sampai 3685), sedangkan instrumen ARTHA berbentuk tugas operasional.

Setiap pelaksanaan tugas diberi keputusan diterima, memerlukan perbaikan, atau belum dapat dievaluasi, disertai alasan. Kegagalan akibat data yang belum tersedia dibedakan dari galat aplikasi, kemudian tugas yang diperbaiki diuji ulang pada versi yang dicatat.

Analisis pengujian sistem menyajikan jumlah kasus direncanakan, dijalankan, lulus, gagal, dan belum dijalankan. Persentase kelulusan dihitung terhadap kasus yang dijalankan, sedangkan cakupan pelaksanaan dihitung terhadap kasus yang direncanakan.

Analisis UAT menggunakan satuan pelaksanaan tugas per peserta dan per versi yang dinyatakan jelas. Penerimaan dihitung dari pelaksanaan tugas yang diterima dibagi pelaksanaan tugas yang telah dievaluasi, sedangkan tugas belum dievaluasi serta hasil uji ulang tetap dilaporkan terpisah.

Penerimaan menyeluruh memerlukan selesainya tugas penting dan tidak adanya galat kritis yang terbuka. Hasil dibahas menurut integrasi fungsi, pemantauan penerimaan, dan kesesuaian kebutuhan, tanpa menyatakan penghematan waktu apabila pengukuran pembanding tidak dilakukan.

Setelah tindak lanjut, pengembang menyiapkan versi serah uji, panduan penggunaan, daftar keterbatasan, prosedur pencadangan, dan berita acara evaluasi. Penyerahan untuk pemakaian operasional dilakukan sesuai persetujuan mitra, sehingga akses uji tidak otomatis diperlakukan sebagai penerapan produksi.

## 3.4 Konsep Prototipe

Konsep prototipe disusun sebagai rancangan awal yang akan diperiksa bersama mitra. Kebutuhan yang berasal dari penjelasan operasional, pilihan teknis, dan usulan pengendalian dibedakan dalam matriks keterlacakan agar dasar setiap keputusan tetap jelas.

### 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan

Proses usulan menghubungkan pencatatan cabang dengan pengawasan pusat melalui transaksi yang dapat ditelusuri. Kajian penerimaan SPP pada Hendri dkk. (2025, hlm. 124 sampai 125) digunakan sebagai pembanding pencatatan serta penelusuran bukti.

Tabel 3.8 merangkum perubahan proses yang dirancang. Rincian kebijakan pembayaran dan petugas pemeriksa akan divalidasi kepada pihak yang mempunyai kewenangan rekening.

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

Satu pembayaran dirancang untuk satu siswa dan satu cabang transaksi, dengan alokasi ke satu atau beberapa tagihan. Jumlah alokasi harus sama dengan nominal pembayaran, sedangkan tagihan yang dipilih harus berasal dari siswa serta cabang yang sama.

Transfer diajukan dengan status menunggu verifikasi dan belum mengurangi sisa tagihan. Persetujuan dilakukan setelah pemeriksa berwenang mencocokkan dana masuk; pengembalian menyimpan alasan, sedangkan perbaikan diajukan sebagai transaksi baru yang tertaut pada pengajuan sebelumnya.

Pembayaran tunai dihitung sebagai penerimaan setelah uang diterima dan pencatatan diselesaikan. Pada rancangan awal, setiap tagihan yang dipilih dilunasi sebesar sisa kewajibannya; fasilitas cicilan baru diaktifkan jika kebijakannya telah divalidasi.

Penyerahan kas ke pusat memuat pembayaran asal, penyerah, penerima, dan waktu penerimaan. Penyetoran ke bank merupakan tahap berikutnya yang mempunyai rekening, bukti, serta waktu sendiri, sehingga keduanya tidak menghasilkan pendapatan siswa yang baru.

Pencocokan prototipe dibatasi pada satu dana masuk bank untuk satu transfer siswa atau satu setoran kas dengan nominal penuh yang sama. Dana gabungan beberapa sumber, selisih biaya, serta pencocokan sebagian ditandai untuk tindak lanjut di luar cakupan pencocokan prototipe.

Pemisahan pencatatan pusat dan cabang mempunyai pembanding pada Ramadhan dan Widodo (2026, bagian pembahasan). Sudirman dan Tristianti (2021, hlm. 126 sampai 127) menjadi acuan pembahasan pencocokan catatan internal dengan bank, sedangkan sisa tagihan siswa disajikan terpisah dari selisih pencocokan.

### 3.4.2 Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional disusun dari proses operasional dan tujuan pengembangan. Tabel 3.9 menyajikan kebutuhan awal beserta hasil yang diharapkan agar dapat diturunkan menjadi kasus pengujian.

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

Penjadwalan pada ARTHA membantu pemeriksaan konflik pada jadwal yang disusun pengelola. Calon jadwal berkonflik dapat disimpan nonaktif untuk ditinjau, sedangkan pengaktifan pengecualian belum diberlakukan sebelum kebijakannya ditetapkan bersama mitra. Khafidhoh dkk. (2026, hlm. 15 sampai 16, 19) digunakan sebagai pembanding kebutuhan penjadwalan bimbel, sedangkan algoritma genetika pada penelitian tersebut tidak diadopsi sebagai fitur penyusunan jadwal otomatis.

Kapasitas diperiksa dengan membandingkan jumlah keanggotaan aktif terhadap batas kelas. Kabisatullah dan Noprisson (2026, hlm. 94) memberikan pembanding validasi batas kapasitas dan irisan waktu, tetapi nilai kapasitas serta kebijakan penambahan siswa ditetapkan dari kebutuhan ARTHA.

Ambang hampir penuh dinyatakan sebagai parameter sisa tempat yang dapat ditetapkan pengelola. Ambang sisa tempat bernilai satu sampai kapasitas kelas, sedangkan kondisi penuh dihitung dari jumlah peserta aktif dan tidak menggantikan status operasional kelas.

Pemeriksaan dilakukan kembali pada peladen saat penyimpanan, termasuk ketika dua petugas mengajukan penempatan secara bersamaan. Penghitungan tidak hanya bergantung pada angka yang telah ditampilkan di layar karena data tersebut dapat berubah setelah dibuka pengguna lain.

Pesan WhatsApp memuat identitas siswa yang diperlukan, periode, sisa tagihan, dan tanggal jatuh tempo. Tautan menggunakan nomor internasional dan pesan yang dikodekan sesuai mekanisme *click to chat* pada dokumentasi WhatsApp (WhatsApp, t.t.).

Permintaan pembukaan tautan dicatat sebagai tindakan admin. Catatan tersebut tidak diberi makna pesan terkirim, diterima, atau dibaca karena pengiriman berlangsung di luar sistem prototipe.

Tabel 3.10 menyajikan kebutuhan nonfungsional yang menyertai fungsi utama. Kriteria pengujiannya dirumuskan sebagai perilaku yang dapat diperiksa, sedangkan batas kuantitatif kinerja akan ditetapkan sebelum pengukuran dilaksanakan.

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

Hak akses ditetapkan berdasarkan peran dan hubungan pengguna dengan cabang. Pemisahan cakupan data pada artikel Ahadi dkk. (2025, hlm. 764 sampai 765) dan Thiovanda (2026, hlm. 4) menjadi pembanding, sedangkan susunan dua peran pada prototipe mengikuti ruang lingkup ARTHA.

Tabel 3.11 menyajikan matriks kewenangan awal. Kewenangan keuangan yang belum disepakati akan diperiksa sebelum rancangan pembayaran diterapkan pada lingkungan mitra.

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

Nilai identitas cabang yang kosong tidak digunakan sebagai satu-satunya dasar pemberian hak Super Admin. Setiap permintaan tetap diperiksa berdasarkan peran yang sah dan kewenangan terhadap objek data yang diakses.

Tentor dan wali murid tidak diberi akun dasbor dalam rancangan inti. Data tentor digunakan untuk penjadwalan, sedangkan nomor wali digunakan sebagai tujuan komunikasi yang dijalankan admin.

### 3.4.4 Cerita Pengguna (*User Story*) dan Kriteria Penerimaan

Cerita pengguna disusun dengan peran, tindakan, manfaat, serta kriteria penerimaan yang dapat diamati. Penyusunannya mempunyai pembanding pada Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105), sedangkan isi Tabel 3.12 berasal dari kebutuhan ARTHA.

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

Tabel 3.13 menghubungkan setiap kebutuhan dengan sumber, cerita pengguna, use case, iterasi, dan kelompok pemeriksaan. Prioritas seluruh kebutuhan adalah inti, sedangkan urutan pengerjaannya mengikuti ketergantungan pada Tabel 3.4.

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

Kelompok PU mencakup kasus normal, pengecualian, dan batas yang relevan, bukan satu hasil uji tunggal. Matriks rinci menghubungkan kelompok tersebut dengan kasus BB, tabel sumber, bukti, dan status validasi pada lampiran keterlacakan.

### 3.4.5 Pemodelan Kasus Penggunaan (*Use Case*) dan Skenario

Pemodelan kasus penggunaan atau *use case* menggambarkan tujuan pengguna di dalam batas sistem. Penggunaan model ini mempunyai pembanding pada Ahadi dkk. (2025, hlm. 765), sedangkan Gambar 3.2 memakai katalog yang telah diselaraskan dengan rancangan data ARTHA.

![Use case inti sistem ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_2_Use_Case_Inti.png>)

**Gambar 3.2 Diagram Kasus Penggunaan Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan ARTHA.

Katalog memuat empat belas tujuan UC-00 sampai UC-13 dengan dua aktor pengguna. Tabel 3.14 merangkum contoh proses lintas peran, sedangkan seluruh skenario dan peta perubahan kode lama disimpan pada dokumen use case pendamping.

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

Pembatasan akses berlaku pada setiap tindakan dan objek yang diproses. Diagram tidak memisahkan setiap validasi formulir menjadi tujuan pengguna tersendiri, sedangkan skenario menjelaskan kondisi normal serta pengecualiannya.

### 3.4.6 Perancangan Basis Data

Basis data terpusat dirancang menjadi dua puluh tiga tabel yang memisahkan identitas, keanggotaan, kewajiban, penerimaan, dan perpindahan dana. Gambar 3.3 menampilkan hubungan transaksi utama, sedangkan ERD lengkap serta kamus data tersedia pada dokumen basis data pendamping.

![Hubungan konseptual data ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_3_Model_Data_Konseptual.png>)

**Gambar 3.3 Hubungan Data Utama Prototipe ARTHA**

Sumber: rancangan penelitian berdasarkan pemisahan proses operasional.

Tabel 3.15 merangkum pengelompokan tabel beserta fungsinya. Hubungan pembayaran dan tagihan memakai rincian alokasi agar satu penerimaan dapat digunakan untuk beberapa tagihan siswa yang sama.

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

Tabel 3.16 menjelaskan atribut dan kendala yang paling memengaruhi ketepatan prototipe. Penghitungan peserta aktif, sisa tagihan, kondisi terlambat, dan ringkasan penerimaan diturunkan dari data sumber, bukan angka yang dapat diubah secara terpisah.

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

Penempatan peserta memerlukan kelas aktif dengan jadwal dan ruang yang memenuhi kapasitas kelompok. Perubahan ruang atau batas kelas diperiksa kembali terhadap peserta aktif, sedangkan hitungan serta penyimpanannya dilindungi oleh transaksi yang sama.

Laporan menggunakan cabang yang tersimpan pada transaksi agar perpindahan siswa tidak memindahkan riwayat penerimaan. Sisa tagihan dihitung dari nilai kewajiban dikurangi alokasi pembayaran sah, sedangkan penanda lewat jatuh tempo dihitung terpisah dari tingkat pelunasannya.

Skema fisik ditargetkan pada MySQL dengan mesin transaksi InnoDB. Rancangan kunci, indeks, penguncian, dan aturan nilai akan diperiksa melalui migrasi serta pengujian implementasi sebelum dinyatakan berjalan.

### 3.4.7 Perancangan Antarmuka

Antarmuka disusun menurut urutan kerja dan kewenangan pengguna. Gambar 3.4 sampai Gambar 3.9 memperlihatkan enam rancangan layar inti, sedangkan Tabel 3.17 menghubungkan layar dengan tugas pengguna.

**Tabel 3.17 Rancangan Antarmuka Inti**

| Layar | Cerita pengguna | Tindakan utama |
| :--- | :--- | :--- |
| Dasbor cabang | US-08, US-10, US-12 | Memilih tindak lanjut transaksi serta keterisian |
| Keanggotaan kelas | US-03, US-04 | Menambah peserta atau mengakhiri keanggotaan |
| Pengajuan transfer | US-08 | Memilih tagihan dan mengirim bukti |
| Pemeriksaan transfer | US-09 | Memeriksa dana masuk dan mengambil keputusan |
| Tunggakan WhatsApp | US-10 | Memeriksa pesan dan membuka WhatsApp |
| Dasbor pusat dan pencocokan | US-11, US-12, US-13 | Menelusuri setoran, penerimaan, dan referensi bank |

Angka, nama, serta transaksi pada rancangan layar merupakan data simulasi dan tidak menunjukkan kondisi keuangan mitra. Penanda warna disertai teks, sedangkan istilah status mengikuti skenario serta kamus data yang sama.

Gambar 3.4 memperlihatkan rancangan dasbor admin cabang. Dasbor cabang menampilkan tunggakan, pengajuan transfer menunggu pemeriksaan, dan keterisian kelas sesuai cabang pengguna. Daftar tindak lanjut menghubungkan ringkasan dengan transaksi sumber untuk mendukung US-08, US-10, dan US-12.

![Dasbor Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_4_Dasbor_Cabang.png>)

**Gambar 3.4 Dasbor Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Gambar 3.5 memperlihatkan rancangan penempatan dan keanggotaan kelas. Halaman keanggotaan menampilkan kapasitas, peserta aktif, sisa tempat, serta peringatan hampir penuh untuk US-03 dan US-04. Tombol penambahan dinonaktifkan ketika penuh, sedangkan tindakan mengakhiri keanggotaan menyimpan tanggal serta alasan tanpa menghapus siswa.

![Penempatan dan Keanggotaan Kelas](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_5_Keanggotaan_Kelas.png>)

**Gambar 3.5 Penempatan dan Keanggotaan Kelas**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Gambar 3.6 memperlihatkan rancangan pengajuan transfer oleh admin cabang. Formulir pengajuan menampilkan siswa, cabang, tagihan yang dipilih, jumlah alokasi, rekening tujuan, serta bukti transfer untuk US-08. Pengiriman menghasilkan status menunggu verifikasi, sedangkan perbaikan dari pengajuan yang dikembalikan tetap memperlihatkan hubungan dengan pengajuan sebelumnya.

![Pengajuan Transfer oleh Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_6_Pengajuan_Transfer.png>)

**Gambar 3.6 Pengajuan Transfer oleh Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Gambar 3.7 memperlihatkan rancangan pemeriksaan transfer oleh super admin. Layar pemeriksaan menyandingkan pengajuan dengan rincian dana masuk yang dimasukkan petugas berwenang untuk US-09. Persetujuan memerlukan nominal dan referensi yang sesuai, sedangkan pengembalian mewajibkan alasan yang dapat ditindaklanjuti admin.

![Pemeriksaan Transfer oleh Super Admin](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_7_Pemeriksaan_Transfer.png>)

**Gambar 3.7 Pemeriksaan Transfer oleh Super Admin**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Gambar 3.8 memperlihatkan rancangan tunggakan dan pratinjau pesan whatsapp. Halaman tunggakan menampilkan periode, sisa tagihan, jatuh tempo, nomor wali, dan pratinjau pesan untuk US-10. Tombol membuka WhatsApp dengan pesan terisi, sementara pengiriman tetap dilakukan admin dan catatan tindakan tidak menunjukkan status pesan terkirim.

![Tunggakan dan Pratinjau Pesan WhatsApp](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_8_Tunggakan_WhatsApp.png>)

**Gambar 3.8 Tunggakan dan Pratinjau Pesan WhatsApp**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Gambar 3.9 memperlihatkan rancangan dasbor pusat dan pencocokan penerimaan. Dasbor pusat membedakan tunggakan, penerimaan sah, pengajuan tertunda, dan dana yang telah dicocokkan untuk US-12 serta US-13. Petugas dapat membuka sumber transfer atau setoran, memeriksa referensi bank, dan menelusuri nominal tanpa menghitung setoran sebagai pendapatan siswa yang baru.

![Dasbor Pusat dan Pencocokan Penerimaan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_9_Dasbor_Pusat_Pencocokan.png>)

**Gambar 3.9 Dasbor Pusat dan Pencocokan Penerimaan**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

## 3.5 Spesifikasi Teknis

Spesifikasi teknis disusun sebagai kebutuhan awal implementasi prototipe. Versi perangkat lunak, kapasitas perangkat, dan konfigurasi pengujian akan dibekukan serta dicatat sebelum hasil pengujian digunakan untuk penarikan simpulan.

### 3.5.1 Arsitektur Sistem

Arsitektur dirancang dengan pemisahan antarmuka web dan layanan pengolahan data. Next.js digunakan pada antarmuka, Laravel digunakan untuk aturan bisnis dan layanan data, sedangkan MySQL digunakan sebagai penyimpanan terpusat.

Gambar 3.10 menyajikan hubungan pengguna, antarmuka, layanan, penyimpanan, dan proses eksternal. Pemilihan arsitektur merupakan keputusan teknis penelitian, sehingga tidak digunakan sebagai bukti otomatis bahwa prototipe lebih cepat atau lebih aman daripada arsitektur lain.

![Arsitektur prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_10_Arsitektur_Prototipe.png>)

**Gambar 3.10 Arsitektur Prototipe Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan akses multicabang dan pemisahan proses pengelolaan data.

Autentikasi direncanakan menggunakan fasilitas Laravel Sanctum dengan sesi berbasis kuki untuk antarmuka milik aplikasi sendiri. Konfigurasi domain, perlindungan permintaan, serta masa sesi disesuaikan dengan lingkungan penerapan dan diperiksa sebelum pengujian pengguna (Laravel, t.t.-a).

Antrean pengajuan menunggu pemeriksaan ditampilkan dari status transaksi pada dasbor Super Admin. Apabila mitra memerlukan status notifikasi dibaca, fasilitas notifikasi tersimpan Laravel dapat ditambahkan sebagai perluasan setelah kebutuhannya disepakati (Laravel, t.t.-b).

Data dasbor dimuat dari layanan terpusat saat halaman dibuka atau diperbarui setelah tindakan pengguna. Istilah waktu nyata pada rancangan ini dibatasi pada informasi tersimpan terbaru yang dimuat melalui layanan, bukan jaminan pembaruan serentak tanpa pemuatan ulang pada seluruh perangkat.

Kebutuhan pembaruan berkala dan batas waktu tanggapan akan diperiksa bersama mitra sebelum ditetapkan sebagai kriteria penerimaan. Mekanisme yang akhirnya digunakan serta hasil pengukurannya dicatat pada bab hasil agar tidak terjadi perbedaan antara istilah dan pelaksanaan.

### 3.5.2 Perangkat Keras

Perangkat pengembangan perlu menjalankan penyunting kode, antarmuka web, layanan aplikasi, dan basis data lokal. Tabel 3.18 membedakan informasi yang telah diketahui dari rincian perangkat yang masih perlu dicatat sebelum pengujian.

**Tabel 3.18 Ketersediaan dan Rencana Perangkat Keras**

| Perangkat | Informasi tersedia | Pelengkapan sebelum pengujian |
| :--- | :--- | :--- |
| Komputer penyusunan | Laptop pengembang berbasis Windows 11 Home 64-bit | AMD Ryzen 5 5600H (6 core, 12 thread, hingga 4,2 GHz), RAM 24 GB DDR4, NVMe SSD 512 GB, dan NVIDIA GeForce RTX 3050 |
| Komputer pengguna | Direncanakan untuk tugas administrasi cabang dan pusat | Perangkat, resolusi, peramban, dan jaringan ditetapkan bersama mitra |
| Telepon uji | Direncanakan untuk tampilan sempit dan tautan WhatsApp | Sistem operasi, ukuran layar, peramban, serta aplikasi WhatsApp dicatat |
| Peladen uji | Diperlukan untuk akses evaluasi mitra | Kapasitas, penyimpanan privat, domain, serta konfigurasi jaringan belum ditetapkan |
| Perangkat cetak | Digunakan jika pencetakan kuitansi masuk tugas evaluasi | Kertas dan pengaturan cetak dikonfirmasi |

Kapasitas perangkat tidak ditetapkan dari spesifikasi artikel terdahulu. Inventaris aktual dan kondisi jaringan dicatat bersama hasil agar konteks pelaksanaan dapat diperiksa.

### 3.5.3 Perangkat Lunak dan Versi Teknologi

Ruang kerja telah mempunyai proyek antarmuka `website-artha` dengan berkas penguncian dependensi. Versi pada Tabel 3.19 diperiksa dari berkas tersebut pada 25 Oktober 2026 dan belum menunjukkan bahwa layanan administrasi serta basis data telah selesai diimplementasikan.

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

Kebutuhan lingkungan antarmuka diperiksa terhadap dokumentasi resmi Next.js sesuai versi yang akhirnya digunakan (Vercel, t.t.). Pasangan PHP dan Laravel dipilih menurut kompatibilitas serta kebijakan dukungan yang berlaku, kemudian dicatat bersama lingkungan evaluasi (Laravel, t.t.-c).

Keberadaan dependensi lokal digunakan sebagai bukti pilihan teknologi yang tersedia, bukan hasil pengujian prototipe. Versi layanan, konfigurasi koneksi, dan hasil migrasi akan dilengkapi sebelum pengujian terintegrasi.

### 3.5.4 Lingkungan Implementasi dan Pengujian

Lingkungan pengembangan dipisahkan dari lingkungan evaluasi mitra. Data buatan atau tersamarkan digunakan untuk pengujian awal, sedangkan penggunaan data nyata dibatasi sesuai izin dan kebutuhan tugas yang diperiksa.

Berkas bukti pembayaran disimpan pada lokasi yang memerlukan pemeriksaan kewenangan. Kata sandi, pengaturan koneksi, dan kredensial rekening tidak dimasukkan ke laporan, repositori terbuka, atau gambar hasil pengujian.

Waktu kejadian disimpan dalam UTC dan ditampilkan dalam zona waktu Asia/Makassar untuk operasional Balikpapan. Tanggal kewajiban dan jatuh tempo menggunakan kalender operasional tersebut, dengan tanggal yang ditetapkan pada setiap tagihan.

Pengujian bersama mitra menggunakan akun simulasi minimal dua cabang dan satu akun pusat agar pembatasan data dapat diperiksa. Jumlah data uji, kondisi jaringan, versi, dan perangkat dicatat; cakupan tersebut merupakan rencana pengujian, bukan jumlah peserta yang sudah hadir.

Data awal memuat kelas tersedia, hampir penuh, penuh, jadwal beririsan, beberapa siklus tagihan, transfer dikembalikan, serta setoran tunai. Pemeriksaan awal dilakukan setelah pemuatan data dan pencadangan, kemudian keadaan awal dipulihkan bila diperlukan untuk mengulang kasus.

Pencadangan mencakup basis data dan berkas pendukung yang saling berkaitan. Pemulihan diperiksa pada lingkungan uji sebelum dinyatakan sebagai kemampuan prototipe.

## 3.6 Jadwal Pembuatan Prototipe

Rencana pengembangan disusun selama dua belas minggu relatif dengan empat iterasi dua mingguan. Penelaahan wawancara dan penyusunan rancangan telah memiliki artefak per 25 Oktober 2026, sedangkan tanggal mulai implementasi serta evaluasi belum disepakati.

Tabel 3.20 menunjukkan alokasi pelaksanaan berikutnya dan tidak digunakan untuk mengklaim bahwa kegiatan yang telah terdokumentasi harus diulang seluruhnya. Minggu pertama dimulai pada tanggal yang akan ditetapkan bersama pembimbing dan mitra.

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

Pengujian unit, pengujian sistem, dan evaluasi iterasi berlangsung di dalam setiap alokasi iterasi. Rincian jam tugas dan tanggal kalender dilengkapi sebelum pelaksanaan, kemudian disesuaikan apabila terdapat perubahan kebutuhan atau ketersediaan mitra.

Penyusunan laporan mengikuti panduan kepenulisan ITK, sedangkan luaran prototipe dilaporkan sesuai ketentuan program studi (Institut Teknologi Kalimantan, 2025a; Institut Teknologi Kalimantan, 2026). Jadwal akhir dicatat bersama versi rencana agar perubahan dari usulan awal dapat diperiksa.
