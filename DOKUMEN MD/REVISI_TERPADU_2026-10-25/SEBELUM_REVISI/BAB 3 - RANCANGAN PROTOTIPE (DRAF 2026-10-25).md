# BAB 3
# RANCANGAN PROTOTIPE

Bab ini menguraikan rancangan prototipe sistem informasi manajemen operasional berbasis web untuk Bimbingan Belajar Artha Balikpapan. Pembahasan mencakup garis besar prototipe, tahapan pembuatan, prosedur pengembangan, konsep sistem, spesifikasi teknis, dan rencana jadwal pelaksanaan. Susunan subbab mengikuti template tugas akhir jalur prototipe (Institut Teknologi Kalimantan, 2025b).

## 3.1 Garis Besar Prototipe

Prototipe dirancang untuk mengintegrasikan pencatatan siswa, pembayaran SPP, pengelolaan kelas, penjadwalan tentor, dan pemantauan cabang dalam satu sistem. Struktur data disiapkan untuk mendukung delapan cabang, dengan pembatasan kewenangan antara Admin Cabang dan Super Admin.

### 3.1.1 Objek dan Konteks Pengembangan

Objek pengembangan adalah pengelolaan operasional Bimbel Artha Balikpapan. Kebutuhan awal ditelusuri melalui transkrip wawancara yang tersedia dalam dokumentasi penelitian, kemudian diperiksa kembali melalui klarifikasi bersama pihak yang menguasai proses terkait.

Pencatatan pembayaran, penempatan siswa, serta pemantauan pusat digunakan sebagai dasar penetapan fungsi prototipe. Pengembangan fungsi tersebut mempunyai pembanding pada penelitian sistem bimbel yang mengintegrasikan data siswa, jadwal, dan pembayaran (Fajriansyah dkk., 2026, hlm. 116, 124 sampai 125; Gunawan dkk., 2025, hlm. 424).

Informasi dari penelitian terdahulu digunakan sebagai acuan rancangan, sedangkan kondisi ARTHA ditetapkan berdasarkan bukti lapangan. Angka jumlah siswa, jumlah tentor, frekuensi kesalahan, dan besarnya penghematan waktu tidak digunakan sebagai hasil penelitian sebelum tersedia data yang dapat diperiksa.

### 3.1.2 Ruang Lingkup dan Pengguna Prototipe

Pengguna sistem dibatasi pada Admin Cabang dan Super Admin. Admin Cabang mengelola data operasional sesuai cabang penugasannya, sedangkan Super Admin memantau seluruh cabang dan menjalankan fungsi pengendalian sesuai kewenangan yang ditetapkan.

Pembatasan data cabang dan pemantauan pusat mempunyai acuan pembanding pada Ahadi dkk. (2025, hlm. 764 sampai 765). Pengelolaan siswa berdasarkan cabang juga dijelaskan oleh Thiovanda (2026, hlm. 4), sehingga rancangan ARTHA ditempatkan sebagai penyesuaian kebutuhan mitra dan tidak dinyatakan sebagai sistem bimbel multicabang yang pertama.

Fungsi pengingat pembayaran menggunakan tautan WhatsApp yang dibuka oleh Admin Cabang. Nomor penerima dan isi pesan disiapkan oleh sistem, sedangkan pemeriksaan serta pengiriman pesan dilakukan oleh admin.

Pengelolaan kapasitas dilakukan melalui peringatan ketika kelas hampir penuh dan penolakan penambahan peserta ketika kapasitas telah tercapai. Tempat kembali tersedia setelah keanggotaan siswa pada kelas tersebut diakhiri, tanpa menghapus riwayat keikutsertaannya.

Pengajuan bukti transfer oleh Admin Cabang dan pemeriksaan oleh Super Admin digunakan sebagai rancangan awal pengendalian pembayaran. Kewenangan akses rekening, petugas pemeriksa, dan prosedur pembayaran tunai akan dikonfirmasi kepada mitra sebelum fungsi pembayaran ditetapkan sebagai kebutuhan final.

Prototipe difokuskan pada layanan administrasi internal. Pembelajaran daring, penilaian akademik siswa, pengiriman WhatsApp otomatis, dan integrasi otomatis dengan bank tidak dimasukkan dalam rancangan inti ini.

### 3.1.3 Pendekatan Pengembangan Prototipe

Pengembangan dilakukan dengan metode *Personal Extreme Programming* (PxP). Metode ini mengarahkan pengembangan individual melalui pencatatan pekerjaan, pengujian berkelanjutan, dan evaluasi proses berdasarkan data pelaksanaan (Dzhurov dkk., 2009, hlm. 253 sampai 256).

Tahapan yang digunakan meliputi penggalian kebutuhan, perencanaan, inisialisasi iterasi, perancangan, implementasi, pengujian sistem, dan evaluasi iterasi. Penerapan PxP pada sistem buku tamu menjadi pembanding penyusunan kebutuhan, rencana rilis, dan rancangan antarmuka (Fikri & Arthawan Sugih Prabowo, 2021, hlm. 103 sampai 105).

Pelaksanaan penelitian juga mencakup pengumpulan data kebutuhan dan evaluasi bersama calon pengguna. Dengan demikian, PxP digunakan sebagai metode pengembangan perangkat lunak, sedangkan prosedur pengumpulan serta analisis data dijelaskan untuk mendukung keterlacakan keputusan penelitian.

### 3.1.4 Luaran yang Ditargetkan

Luaran yang ditargetkan berupa perangkat lunak prototipe, dokumentasi kebutuhan dan rancangan, bukti pelaksanaan iterasi, serta hasil pengujian bersama perwakilan mitra. Dokumen kebutuhan, kasus uji, hasil evaluasi, dan simpulan dihubungkan melalui kode kebutuhan agar pencapaiannya dapat ditelusuri.

Pengembangan diarahkan pada pemenuhan Tingkat Kesiapan Teknologi (TKT) 5 sesuai ketentuan tugas akhir prototipe. Evaluasi dilakukan bersama mitra atau calon pengguna pada lingkungan pengujian yang relevan, sedangkan bukti pencapaian dicatat untuk pemeriksaan pembimbing dan program studi (Institut Teknologi Kalimantan, 2026, hlm. 4).

Dokumentasi produk juga disiapkan untuk penyusunan laporan, artikel ilmiah, dan pendaftaran Hak Kekayaan Intelektual (HKI). Pemenuhan luaran tersebut dilaporkan berdasarkan bukti pelaksanaan, sehingga tidak dinyatakan telah tercapai pada tahap rancangan.

## 3.2 Tahapan Pembuatan Prototipe

Tahapan pembuatan disusun sebagai alur kerja dari penggalian kebutuhan sampai penyiapan luaran. Gambar 3.1 menyajikan urutan tersebut beserta perulangan evaluasi dan perbaikan yang direncanakan.

![Diagram alir pembuatan prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_1_Alur_Pembuatan_Prototipe.png>)

**Gambar 3.1 Alur Pembuatan Prototipe Sistem Informasi ARTHA**

Sumber: Dzhurov dkk. (2009, hlm. 254 sampai 256), telah diolah dengan penambahan evaluasi pengguna dan penyiapan luaran penelitian.

Penggalian kebutuhan dan perencanaan menjadi dasar pemilihan pekerjaan setiap iterasi. Setelah implementasi, fungsi yang selesai diperiksa melalui pengujian sistem, kemudian waktu kerja, galat, dan usulan perbaikan ditelaah pada evaluasi iterasi.

Apabila masih terdapat fungsi yang direncanakan, pengembangan dilanjutkan ke inisialisasi iterasi berikutnya. Apabila masukan pengguna mengubah kebutuhan, perubahan dicatat dan dinilai kembali sebelum dimasukkan dalam rencana pekerjaan.

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

Wawancara lanjutan dilakukan secara semiterstruktur dengan panduan topik yang tetap memungkinkan pertanyaan klarifikasi. Topik instrumen disajikan pada Tabel 3.2, sedangkan pertanyaan rinci dan catatan pelaksanaan akan ditempatkan pada lampiran.

**Tabel 3.2 Rancangan Topik Wawancara dan Pemeriksaan Dokumen**

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

Perencanaan dilakukan dengan memecah kebutuhan menjadi tugas teknis dan memperkirakan waktu pengerjaan setiap tugas. Estimasi awal menggunakan rincian pekerjaan dan perkiraan terbaik, kemudian diperbaiki berdasarkan waktu aktual iterasi yang telah selesai.

Pendekatan tersebut mengikuti penjelasan Dzhurov dkk. (2009, hlm. 254 sampai 255) tentang pemanfaatan kategori tugas dan data pekerjaan sebelumnya. Deret Fibonacci tidak ditetapkan sebagai ketentuan wajib PxP dalam rancangan ini.

Prioritas ditentukan berdasarkan kepentingan operasional, ketergantungan antarfungsi, dan risiko kesalahan. Identitas cabang, akun, serta pembatasan akses dikerjakan lebih awal karena menjadi dasar penyimpanan siswa, kelas, dan transaksi.

Rencana awal dibagi menjadi empat iterasi sebagaimana ditunjukkan pada Tabel 3.3. Pembagian tersebut merupakan usulan pelaksanaan penelitian, sehingga dapat disesuaikan setelah kebutuhan dan kapasitas waktu pengembangan dikonfirmasi.

**Tabel 3.3 Usulan Pembagian Iterasi Pengembangan**

| Iterasi | Fokus pekerjaan | Ketergantungan dan bukti penyelesaian |
| :--- | :--- | :--- |
| Iterasi pertama | Akun, kewenangan cabang, data cabang, siswa, ruang, dan tarif | Struktur data dasar tersedia dan pengujian akses cabang dapat dijalankan |
| Iterasi kedua | Keanggotaan kelas, indikator kapasitas, jadwal, dan pemeriksaan benturan | Data siswa dan ruang tersedia; kasus batas kapasitas serta irisan jadwal diperiksa |
| Iterasi ketiga | Tagihan, penerimaan, pengajuan transfer, pemeriksaan, dan tautan WhatsApp | Data tarif dan siswa tersedia; nominal, status, serta tujuan pesan diperiksa |
| Iterasi keempat | Dasbor pusat, rekap cabang, pencocokan penerimaan, dan integrasi | Data uji terintegrasi tersedia; ringkasan dan jejak transaksi dapat ditelusuri |

Setiap iterasi direncanakan berlangsung dua minggu sebagai alokasi awal, bukan hasil estimasi yang telah dibuktikan. Durasi ini berada dalam rentang satu sampai tiga minggu yang dijelaskan oleh Dzhurov dkk. (2009, hlm. 255), sedangkan tanggal kalender ditetapkan setelah jadwal penelitian disepakati.

Masukan mitra dicatat sebagai permintaan perubahan dengan uraian dampak terhadap fungsi, waktu, dan pengujian. Permintaan yang mengubah ruang lingkup akan dibahas sebelum menjadi pekerjaan tambahan, sehingga perubahan tidak dimasukkan tanpa penilaian kapasitas pengembangan.

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

Pengujian sistem dilakukan untuk memeriksa kesesuaian fungsi terhadap kebutuhan tanpa menjadikan struktur kode sebagai objek utama pemeriksaan. Penerapan pengujian kotak hitam atau *Black Box Testing* bersama pengembangan PxP ditunjukkan oleh Apriyanti dkk. (2024, hlm. 3679, 3683).

Kasus uji mencakup masukan normal, masukan tidak sah, batas kapasitas, perubahan status, dan akses lintas cabang. Pemilihan kasus tersebut merupakan penyesuaian rancangan terhadap risiko operasional ARTHA, bukan penyalinan seluruh kasus dari penelitian pembanding.

Setiap kasus mencatat identitas kebutuhan, prasyarat, langkah, data masukan, keluaran yang diharapkan, hasil aktual, dan bukti pelaksanaan. Tabel 3.4 menyajikan rancangan kasus uji awal, sehingga kolom hasil belum dinyatakan berhasil sebelum pelaksanaan.

**Tabel 3.4 Rancangan Kasus Pengujian Sistem**

| Kode | Kondisi atau masukan | Keluaran yang diharapkan | Status pelaksanaan |
| :--- | :--- | :--- | :--- |
| BB-01 | Akun Cabang A meminta data siswa Cabang B | Akses ditolak dan data Cabang B tidak dikirim | Belum diuji |
| BB-02 | Data wajib pendaftaran tidak lengkap | Penyimpanan ditolak dengan penjelasan kolom yang harus dilengkapi | Belum diuji |
| BB-03 | Jumlah peserta satu tempat di bawah kapasitas | Penambahan satu peserta diperbolehkan dan kelas menjadi penuh | Belum diuji |
| BB-04 | Jumlah peserta telah sama dengan kapasitas | Penambahan peserta ditolak tanpa mengubah keanggotaan | Belum diuji |
| BB-05 | Keanggotaan peserta di kelas penuh diakhiri | Riwayat tersimpan dan satu tempat kembali tersedia | Belum diuji |
| BB-06 | Dua pengajuan memperebutkan satu tempat terakhir | Hanya satu penambahan tersimpan dan kapasitas tidak terlampaui | Belum diuji |
| BB-07 | Tentor memiliki penugasan beririsan pada dua cabang | Peringatan konflik ditampilkan sebelum jadwal ditetapkan | Belum diuji |
| BB-08 | Admin mengajukan bukti transfer | Status menjadi menunggu verifikasi dan belum dihitung sebagai penerimaan terkonfirmasi | Belum diuji |
| BB-09 | Super Admin menyetujui transfer yang sesuai | Pembayaran terkonfirmasi satu kali dan sisa tagihan diperbarui | Belum diuji |
| BB-10 | Super Admin mengembalikan pengajuan | Alasan tersimpan dan admin dapat melakukan perbaikan | Belum diuji |
| BB-11 | Permintaan persetujuan pembayaran dikirim berulang | Transaksi tidak dihitung atau dicocokkan dua kali | Belum diuji |
| BB-12 | Tagihan telah lewat jatuh tempo dan belum lunas | Daftar tunggakan serta tautan pesan sesuai siswa ditampilkan | Belum diuji |
| BB-13 | Tautan WhatsApp dibuka | Nomor wali dan isi pesan benar; sistem tidak mengklaim pesan telah diterima | Belum diuji |
| BB-14 | Rekap seluruh cabang dibandingkan dengan transaksi terkonfirmasi | Jumlah sesuai transaksi sumber dan pengajuan tertunda disajikan terpisah | Belum diuji |
| BB-15 | Satu referensi mutasi dipakai pada dua transaksi | Penggunaan ganda ditolak atau ditandai untuk klarifikasi sebelum disahkan | Belum diuji |

Galat dicatat dengan kode, fungsi terdampak, kondisi pemicu, tingkat kepentingan, dan tindakan perbaikan. Galat kritis mencakup kebocoran data cabang, penghitungan pembayaran ganda, serta pelampauan kapasitas yang bertentangan dengan aturan sistem.

Fungsi yang diperbaiki diperiksa kembali melalui kasus semula dan kasus terkait. Hasil sebelum perbaikan tidak dihapus, sehingga perubahan status pengujian dapat ditelusuri.

### 3.3.7 Evaluasi Iterasi (*Retrospective*)

Evaluasi iterasi dilakukan dengan membandingkan rencana pekerjaan dan data pelaksanaan. Waktu aktual, perubahan kebutuhan, galat, serta pekerjaan yang belum selesai ditelaah untuk menentukan perbaikan iterasi berikutnya.

Pemanfaatan data proyek dalam evaluasi merupakan bagian proses PxP pada Dzhurov dkk. (2009, hlm. 256). Sidiq dkk. (2025, hlm. 45) juga melaporkan perubahan kebutuhan dan perbedaan durasi, sehingga waktu implementasi perlu dibedakan dari keseluruhan waktu pengembangan.

Tabel 3.5 menyajikan unsur pencatatan proses yang direncanakan. Formulir diisi selama pelaksanaan, bukan direkonstruksi sebagai angka perkiraan setelah proyek selesai.

**Tabel 3.5 Unsur Dokumentasi Evaluasi Iterasi**

| Dokumen | Unsur yang dicatat | Penggunaan analisis |
| :--- | :--- | :--- |
| Catatan waktu | Kode tugas, kategori, estimasi, waktu mulai, waktu selesai, dan durasi aktual | Selisih estimasi dan aktual beserta penyebabnya |
| Catatan galat | Kode galat, versi, pemicu, tingkat kepentingan, perbaikan, dan uji ulang | Galat terbuka, galat terselesaikan, dan pola kesalahan |
| Catatan perubahan | Asal permintaan, kebutuhan terdampak, keputusan, dan perubahan jadwal | Perubahan ruang lingkup dan tindak lanjut |
| Usulan perbaikan proses | Masalah, bukti, tindakan, dan hasil pemeriksaan berikutnya | Penyesuaian cara kerja pada iterasi selanjutnya |

Selisih durasi dihitung dengan mengurangkan estimasi dari waktu aktual pada tugas yang sama. Nilai tersebut ditafsirkan bersama penyebabnya, sehingga keterlambatan karena perubahan kebutuhan tidak disamakan dengan kesalahan pengodean.

Hasil evaluasi digunakan untuk memperbaiki estimasi, pembagian tugas, atau pengujian berikutnya. Data ini tidak digunakan untuk menyimpulkan PxP lebih unggul daripada metode lain karena penelitian tidak merancang eksperimen pembandingan metode.

### 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi

Pengujian penerimaan pengguna atau *User Acceptance Testing* (UAT) direncanakan bersama perwakilan Admin Cabang dan Super Admin. Peserta dipilih berdasarkan keterlibatan dalam tugas yang diuji, kewenangan operasional, dan kesediaan mengikuti evaluasi.

Pemilihan peserta tidak didasarkan pada jumlah siswa karena siswa tidak menjadi pengguna langsung dasbor internal. Jumlah peserta, cabang yang diwakili, pengalaman tugas, dan keterbatasan keterwakilan akan dicatat sebelum hasil penerimaan ditafsirkan.

Pengujian dilakukan setelah pemeriksaan fungsi awal agar peserta dapat menjalankan tugas dengan data uji yang disiapkan. Tugas penerimaan dibedakan menurut peran sebagaimana dirangkum pada Tabel 3.6.

**Tabel 3.6 Rancangan Tugas Pengujian Penerimaan Pengguna**

| Kode | Peran | Tugas yang dijalankan | Dasar penerimaan |
| :--- | :--- | :--- | :--- |
| UAT-01 | Admin Cabang | Mendaftarkan siswa dan menempatkannya pada kelas tersedia | Data benar, cabang sesuai, dan keanggotaan tersimpan |
| UAT-02 | Admin Cabang | Memeriksa kelas hampir penuh, kelas penuh, dan siswa keluar | Informasi sesuai kondisi dan aturan kapasitas diterapkan |
| UAT-03 | Admin Cabang | Mengajukan transfer dan menindaklanjuti pengembalian pengajuan | Bukti, nominal, status, dan alasan dapat ditelusuri |
| UAT-04 | Admin Cabang | Memilih tunggakan lalu membuka pesan WhatsApp | Penerima, periode, nominal, dan jatuh tempo sesuai tagihan |
| UAT-05 | Super Admin | Memeriksa pengajuan transfer menggunakan contoh mutasi yang diizinkan | Keputusan dan jejak pemeriksaan tersimpan dengan benar |
| UAT-06 | Super Admin | Menelusuri rekap cabang ke transaksi sumber | Ringkasan sesuai data dan kanal penerimaan dapat dibedakan |
| UAT-07 | Pengelola jadwal sesuai kewenangan | Memeriksa penugasan tentor yang beririsan | Konflik terlihat dan keputusan perubahan dapat dicatat |

Instrumen UAT terdiri atas lembar tugas, pengamatan pelaksanaan, catatan masalah, dan keputusan penerimaan. Setiap tugas diberi status diterima, memerlukan perbaikan, atau belum dapat dievaluasi, disertai alasan dan bukti yang relevan.

Kesesuaian instrumen diperiksa dengan memetakan setiap tugas terhadap kebutuhan dan tujuan penelitian. Keterbacaan langkah serta kesesuaian kewenangan ditinjau bersama pembimbing dan perwakilan mitra sebelum pelaksanaan.

Apriyanti dkk. (2024, hlm. 3683 sampai 3685) menggunakan kuesioner dalam evaluasi pengguna pada sistem yang dikembangkannya. Penelitian ini mengadaptasi keterlibatan pengguna dan pencatatan evaluasi, sedangkan keputusan penerimaan diarahkan pada tugas operasional yang dapat diperiksa secara langsung.

Kuesioner skala Likert tidak digunakan sebagai satu-satunya dasar penerimaan dalam rancangan ini. Oleh karena instrumen utama berupa tugas yang berbeda, konsistensi internal antarseluruh tugas tidak diperlakukan sebagai satu konstruk psikometrik yang harus menghasilkan koefisien reliabilitas tunggal.

Analisis hasil pengujian sistem dilakukan dengan mencatat jumlah kasus yang direncanakan, dijalankan, lulus, gagal, dan belum dijalankan. Persentase kelulusan dihitung dari kasus yang lulus dibagi kasus yang dijalankan, sedangkan cakupan pelaksanaan dihitung dari kasus yang dijalankan dibagi kasus yang direncanakan.

Analisis UAT menyajikan jumlah tugas yang diterima, memerlukan perbaikan, dan belum dievaluasi untuk setiap peran. Apabila persentase penerimaan disajikan, penyebutnya hanya tugas yang telah dievaluasi, sedangkan tugas yang belum dievaluasi tetap dilaporkan secara terpisah.

Persentase keseluruhan tidak menggantikan pemeriksaan fungsi kritis. Prototipe belum dinyatakan diterima secara menyeluruh apabila terdapat galat kritis yang belum diperbaiki atau tugas penting yang belum dievaluasi.

Hasil evaluasi dilaporkan menurut tiga tujuan penelitian, yaitu integrasi fungsi, pemantauan dan pencocokan penerimaan, serta kesesuaian kebutuhan pengguna. Penghematan waktu operasional tidak dinyatakan sebagai hasil apabila tidak dilakukan pengukuran khusus dengan tugas pembanding yang setara.

## 3.4 Konsep Prototipe

Konsep prototipe disusun sebagai rancangan awal yang akan diperiksa bersama mitra. Kebutuhan yang berasal dari penjelasan operasional, pilihan teknis, dan usulan pengendalian dibedakan dalam matriks keterlacakan agar dasar setiap keputusan tetap jelas.

### 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan

Transkrip wawancara digunakan untuk menelusuri pencatatan siswa, pembayaran, kapasitas kelas, serta penyerahan informasi kepada pengelola. Keterangan mengenai periode laporan, petugas penerima setoran, dan aturan cabang akan diklarifikasi apabila berbeda antarsumber.

Pencatatan SPP dan penelusuran bukti pembayaran mempunyai pembanding pada Hendri dkk. (2025, hlm. 124 sampai 125). Penelitian tersebut berupa analisis dan rancangan antarmuka, sehingga tidak digunakan sebagai bukti bahwa prosedur pemeriksaan ARTHA sudah diterapkan.

Tabel 3.7 menyajikan hubungan antara proses yang ditelusuri dan proses usulan. Uraian pada kolom usulan merupakan rancangan pengembangan, bukan laporan hasil implementasi.

**Tabel 3.7 Ringkasan Proses Berjalan dan Proses Usulan**

| Proses | Dasar kondisi yang ditelusuri | Proses usulan |
| :--- | :--- | :--- |
| Pendaftaran | Data siswa dan pembayaran dicatat pada dokumen cabang | Pencatatan siswa terpusat dengan pembatasan cabang |
| Penempatan kelas | Petugas memeriksa kelas dan ruang yang tersedia | Pemeriksaan peserta aktif, peringatan hampir penuh, dan penolakan kelas penuh |
| Jadwal tentor | Jadwal serta penyesuaian ditelusuri melalui catatan dan komunikasi pengelola | Jadwal terpusat dengan pemeriksaan irisan penugasan |
| Pengingat SPP | Tagihan ditelusuri dan komunikasi dilakukan oleh petugas | Daftar tunggakan dengan tautan WhatsApp dan pesan sesuai tagihan |
| Transfer siswa | Bukti diteruskan kepada pihak pengelola yang memeriksa pembayaran | Pengajuan oleh Admin Cabang dan keputusan pemeriksaan oleh Super Admin |
| Penerimaan tunai | Uang diterima pada cabang dan penyerahan kepada pusat mempunyai proses tersendiri | Pencatatan penerimaan dan setoran dipisahkan dengan bukti serta petugas penerima |
| Pemantauan pusat | Informasi cabang dihimpun dari catatan operasional | Dasbor lintas cabang dengan status pengajuan, penerimaan, dan pencocokan |

Pengelolaan pembayaran transfer dimulai ketika Admin Cabang memilih tagihan dan mengajukan bukti. Pengajuan diberi status menunggu verifikasi dan ditampilkan dalam daftar pemeriksaan Super Admin.

Super Admin memeriksa nominal, tanggal, tujuan rekening, serta referensi pembayaran dengan mutasi rekening yang berhak diaksesnya. Apabila sesuai, pembayaran disetujui; apabila belum sesuai, pengajuan dikembalikan dengan alasan agar dapat diperbaiki.

Nominal pengajuan yang belum disetujui disajikan terpisah dari penerimaan terkonfirmasi. Tagihan dinyatakan lunas setelah nilai pembayaran yang disetujui memenuhi kewajibannya, sedangkan kebijakan pembayaran sebagian dikonfirmasi sebelum diterapkan.

Penerimaan tunai dicatat saat dana diterima petugas cabang sesuai prosedur yang disepakati. Penyerahan dana ke pusat dicatat sebagai setoran dari penerimaan tersebut, sehingga tidak dihitung sebagai pembayaran siswa yang baru.

Pencocokan penerimaan dirancang untuk menghubungkan transaksi tercatat dengan bukti dana yang diperiksa pusat. Pemisahan catatan per cabang dan penghimpunan rekap mempunyai acuan pada Ramadhan dan Widodo (2026, bagian pembahasan), sedangkan perbedaan catatan internal dengan bank dibahas oleh Sudirman dan Tristianti (2021, hlm. 126 sampai 127).

Ruang lingkup pencocokan dibatasi pada penerimaan yang terkait dengan kegiatan prototipe. Penyusunan seluruh laporan akuntansi, penyesuaian bunga, dan rekonsiliasi saldo seluruh rekening tidak dinyatakan sebagai luaran apabila tidak menjadi kebutuhan yang disepakati.

### 3.4.2 Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional disusun dari proses operasional dan tujuan pengembangan. Tabel 3.8 menyajikan kebutuhan awal beserta hasil yang diharapkan agar dapat diturunkan menjadi kasus pengujian.

**Tabel 3.8 Rancangan Kebutuhan Fungsional**

| Kode | Fungsi | Hasil yang diharapkan |
| :--- | :--- | :--- |
| KF-01 | Autentikasi dan pembatasan kewenangan | Pengguna masuk sesuai peran dan cakupan cabang |
| KF-02 | Pengelolaan siswa | Data siswa wajib dapat disimpan, diperbarui, dan ditelusuri |
| KF-03 | Pengelolaan kelas dan keanggotaan | Peserta aktif dan riwayat masuk atau keluar kelas tercatat |
| KF-04 | Pemeriksaan kapasitas | Peringatan hampir penuh tersedia dan penambahan pada kelas penuh ditolak |
| KF-05 | Pengelolaan jadwal | Ruang, tentor, dan waktu terhubung dengan pemeriksaan potensi benturan |
| KF-06 | Pengelolaan tarif dan tagihan | Nilai tagihan, periode, jatuh tempo, serta penyesuaian berwenang dapat ditelusuri |
| KF-07 | Pencatatan penerimaan tunai | Pembayaran tunai dan kuitansi dicatat sesuai prosedur yang disepakati |
| KF-08 | Pengajuan pembayaran transfer | Nominal, tagihan, dan bukti masuk dalam daftar menunggu verifikasi |
| KF-09 | Pemeriksaan transfer | Super Admin menyetujui atau mengembalikan pengajuan dengan jejak pemeriksaan |
| KF-10 | Tautan penagihan WhatsApp | Nomor dan pesan disiapkan sesuai tagihan yang dipilih |
| KF-11 | Notifikasi dalam dasbor | Super Admin dapat menemukan pengajuan yang belum diperiksa |
| KF-12 | Dasbor dan rekap cabang | Data diringkas menurut cabang, periode, kanal, dan status transaksi |
| KF-13 | Pencocokan dan setoran | Transaksi sumber, penyerahan dana, referensi mutasi, dan selisih dapat ditelusuri |
| KF-14 | Pengelolaan data induk dan akun | Super Admin mengatur akun, cabang, ruang, tentor, dan parameter sesuai kewenangan |

Penjadwalan pada ARTHA diarahkan untuk membantu pemeriksaan konflik pada jadwal yang disusun pengelola. Khafidhoh dkk. (2026, hlm. 15 sampai 16, 19) digunakan sebagai pembanding kebutuhan penjadwalan bimbel, sedangkan algoritma genetika pada penelitian tersebut tidak diadopsi sebagai fitur penyusunan jadwal otomatis.

Kapasitas diperiksa dengan membandingkan jumlah keanggotaan aktif terhadap batas kelas. Kabisatullah dan Noprisson (2026, hlm. 94) memberikan pembanding validasi batas kapasitas dan irisan waktu, tetapi nilai kapasitas serta kebijakan penambahan siswa ditetapkan dari kebutuhan ARTHA.

Ambang hampir penuh dinyatakan sebagai parameter sisa tempat yang dapat ditetapkan pengelola. Ambang tersebut tidak boleh melampaui kapasitas, sedangkan kelas dengan jumlah peserta sama dengan kapasitas selalu berstatus penuh.

Pemeriksaan dilakukan kembali pada peladen saat penyimpanan, termasuk ketika dua petugas mengajukan penempatan secara bersamaan. Penghitungan tidak hanya bergantung pada angka yang telah ditampilkan di layar karena data tersebut dapat berubah setelah dibuka pengguna lain.

Pesan WhatsApp memuat identitas siswa yang diperlukan, periode, sisa tagihan, dan tanggal jatuh tempo. Tautan menggunakan nomor internasional dan pesan yang dikodekan sesuai mekanisme *click to chat* pada dokumentasi WhatsApp (WhatsApp, t.t.).

Riwayat pembukaan tautan dapat dicatat sebagai tindakan admin. Catatan tersebut tidak diberi makna pesan terkirim, diterima, atau dibaca karena pengiriman berlangsung di luar sistem prototipe.

Tabel 3.9 menyajikan kebutuhan nonfungsional yang menyertai fungsi utama. Kriteria pengujiannya dirumuskan sebagai perilaku yang dapat diperiksa, sedangkan batas kuantitatif kinerja akan ditetapkan sebelum pengukuran dilaksanakan.

**Tabel 3.9 Rancangan Kebutuhan Nonfungsional**

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

Tabel 3.10 menyajikan matriks kewenangan awal. Kewenangan keuangan yang belum disepakati akan diperiksa sebelum rancangan pembayaran diterapkan pada lingkungan mitra.

**Tabel 3.10 Matriks Hak Akses Pengguna**

| Fungsi | Admin Cabang | Super Admin |
| :--- | :--- | :--- |
| Siswa dan keanggotaan | Mengelola sesuai cabang penugasan | Memantau seluruh cabang dan melakukan koreksi berwenang |
| Kelas dan jadwal | Mengelola pada cabangnya sesuai aturan | Memantau lintas cabang dan menangani penyesuaian berwenang |
| Tarif dan parameter | Menggunakan ketentuan yang berlaku | Mengelola ketentuan sesuai persetujuan mitra |
| Penerimaan tunai | Mencatat penerimaan dan menyiapkan setoran | Memeriksa rekap serta penerimaan setoran |
| Transfer siswa | Mengajukan bukti dan memperbaiki pengajuan | Memeriksa dan mengambil keputusan verifikasi |
| Tautan WhatsApp | Mengakses tagihan serta nomor wali pada cabangnya | Memantau tindak lanjut tanpa perlu mengirim pesan berulang |
| Dasbor | Melihat data cabangnya | Melihat agregat dan rincian seluruh cabang |
| Akun pengguna | Menggunakan akun yang diberikan | Membuat, menonaktifkan, dan mengatur penugasan akun |

Nilai identitas cabang yang kosong tidak digunakan sebagai satu-satunya dasar pemberian hak Super Admin. Setiap permintaan tetap diperiksa berdasarkan peran yang sah dan kewenangan terhadap objek data yang diakses.

Tentor dan wali murid tidak diberi akun dasbor dalam rancangan inti. Data tentor digunakan untuk penjadwalan, sedangkan nomor wali digunakan sebagai tujuan komunikasi yang dijalankan admin.

### 3.4.4 Cerita Pengguna (*User Story*) dan Kriteria Penerimaan

Kebutuhan utama dirangkum menjadi *user story* dengan peran, tindakan, manfaat, dan kriteria penerimaan. Contoh penggunaannya terdapat pada Fikri dan Arthawan Sugih Prabowo (2021, hlm. 105), sedangkan rumusan pada Tabel 3.11 disusun untuk tugas operasional ARTHA.

Kriteria penerimaan digunakan untuk memeriksa keluaran yang dapat diamati. Pernyataan seperti selalu aman atau tanpa risiko kesalahan tidak digunakan karena tidak menetapkan kondisi pengujian yang terbatas.

**Tabel 3.11 Rancangan Cerita Pengguna dan Kriteria Penerimaan**

| Kode | Peran dan kebutuhan | Manfaat | Kriteria penerimaan |
| :--- | :--- | :--- | :--- |
| US-01 | Admin Cabang mengakses data sesuai penugasan | Bekerja pada cabang yang menjadi tanggung jawabnya | Akses Cabang A ke data Cabang B ditolak oleh peladen |
| US-02 | Admin Cabang mendaftarkan siswa | Data pendaftaran dapat ditelusuri | Data wajib lengkap tersimpan pada cabang yang benar |
| US-03 | Admin Cabang menempatkan siswa pada kelas | Ketersediaan tempat diketahui sebelum penyimpanan | Penempatan diterima jika masih ada tempat dan ditolak saat penuh |
| US-04 | Admin Cabang mengakhiri keanggotaan kelas | Tempat dan riwayat peserta tetap sesuai | Peserta aktif berkurang satu tanpa menghapus riwayat |
| US-05 | Admin Cabang menyusun jadwal tentor | Potensi irisan penugasan terlihat | Konflik tentor dan ruang ditampilkan dengan rincian waktu |
| US-06 | Admin Cabang mengajukan bukti transfer | Pusat dapat melakukan pemeriksaan | Pengajuan masuk daftar menunggu verifikasi dan belum melunasi tagihan |
| US-07 | Super Admin memeriksa transfer | Penerimaan terkonfirmasi dapat dibedakan | Persetujuan memperbarui pembayaran satu kali; pengembalian menyimpan alasan |
| US-08 | Admin Cabang membuka pesan tunggakan | Penyusunan pesan mengikuti data tagihan | Nomor, periode, nominal, dan jatuh tempo benar sebelum pesan dikirim |
| US-09 | Super Admin menelusuri rekap penerimaan | Ringkasan cabang mempunyai transaksi sumber | Total dapat diperiksa menurut cabang, periode, kanal, dan status |
| US-10 | Super Admin memeriksa pencocokan penerimaan | Dana yang sudah dan belum cocok dapat dibedakan | Referensi pemeriksaan dan selisih tercatat tanpa penghitungan ganda |

### 3.4.5 Pemodelan Kasus Penggunaan (*Use Case*) dan Skenario

Diagram kasus penggunaan (*use case*) digunakan untuk menggambarkan hubungan pengguna dengan fungsi inti. Gambar 3.2 menyajikan batas sistem serta dua aktor pengguna, sedangkan rincian skenario disusun untuk menjelaskan proses utama dan alternatifnya.

![Use case inti sistem ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_2_Use_Case_Inti.png>)

**Gambar 3.2 Diagram Kasus Penggunaan Inti Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan ARTHA; penggunaan pemodelan dibandingkan dengan Ahadi dkk. (2025, hlm. 765).

Diagram difokuskan pada tujuan pengguna dan tidak menjadikan setiap pemeriksaan formulir sebagai fungsi yang terpisah. Pembatasan akses tetap diterapkan pada seluruh skenario meskipun tidak digambarkan sebagai hubungan tambahan pada setiap elips.

Tabel 3.12 menyajikan skenario pengajuan dan pemeriksaan transfer sebagai contoh proses lintas peran. Skenario lengkap fungsi lain disusun dengan unsur yang sama pada lampiran perancangan.

**Tabel 3.12 Rancangan Skenario Pengajuan dan Pemeriksaan Transfer**

| Unsur | Rancangan skenario |
| :--- | :--- |
| Identitas | UC-04 pencatatan pembayaran dan UC-07 pemeriksaan transfer |
| Aktor | Admin Cabang sebagai pengaju dan Super Admin sebagai pemeriksa |
| Prasyarat | Pengguna telah masuk, tagihan tersedia, dan kewenangan rekening pemeriksa telah dikonfirmasi |
| Alur pengajuan | Admin memilih tagihan, mencatat nominal dan tanggal, mengunggah bukti, lalu mengirim pengajuan |
| Keadaan antara | Status menunggu verifikasi dan pengajuan ditampilkan dalam dasbor Super Admin |
| Alur pemeriksaan | Super Admin membuka rincian, memeriksa referensi mutasi yang berwenang diakses, dan menentukan keputusan |
| Alur persetujuan | Pembayaran ditandai terverifikasi, identitas pemeriksa disimpan, dan sisa tagihan dihitung ulang |
| Alur pengembalian | Alasan dicatat dan pengajuan dapat diperbaiki oleh admin tanpa menghapus riwayat keputusan |
| Kondisi pengecualian | Bukti tidak terbaca, nominal tidak cocok, referensi sudah digunakan, atau kewenangan pemeriksa tidak sesuai |
| Pascakondisi | Pengajuan dan keputusan dapat ditelusuri; pembayaran tidak dihitung ganda |

### 3.4.6 Perancangan Basis Data

Basis data disusun secara terpusat dengan hubungan cabang pada data operasional yang memerlukannya. Identitas siswa, keanggotaan kelas, tagihan, dan pembayaran dipisahkan karena masing-masing mempunyai riwayat serta perubahan yang berbeda.

Gambar 3.3 menyajikan model konseptual data utama, sedangkan Tabel 3.13 menjelaskan fungsi setiap kelompok data. Diagram belum diperlakukan sebagai bukti bahwa seluruh tabel fisik telah memenuhi normalisasi atau telah diimplementasikan.

![Model konseptual data ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_3_Model_Data_Konseptual.png>)

**Gambar 3.3 Model Konseptual Data Utama Prototipe**

Sumber: rancangan penelitian berdasarkan kebutuhan dan pemisahan proses operasional ARTHA.

**Tabel 3.13 Kelompok Data dan Hubungan Utama**

| Kelompok data | Isi pokok | Hubungan dan aturan |
| :--- | :--- | :--- |
| Cabang | Identitas dan status cabang | Menjadi rujukan pengguna, siswa, ruang, dan kegiatan cabang |
| Pengguna | Akun, peran, penugasan, dan status | Hak akses diperiksa melalui peran dan objek cabang |
| Siswa | Identitas yang diperlukan dan kontak wali | Terhubung dengan keanggotaan serta tagihan |
| Kelas dan ruang | Kelompok belajar, lokasi, batas kapasitas, serta status | Kapasitas kelompok diperiksa terhadap ketentuan ruang dan jenjang |
| Keanggotaan | Siswa, kelas, tanggal masuk, tanggal keluar, dan status | Jumlah peserta dihitung dari keanggotaan aktif pada kelas |
| Tentor dan jadwal | Pengajar, kelas, ruang, hari, waktu mulai, dan waktu selesai | Irisan waktu diperiksa pada identitas tentor dan ruang terkait |
| Tarif dan tagihan | Dasar tarif, periode, jatuh tempo, nilai, dan penyesuaian berwenang | Nilai tagihan lama tetap dapat ditelusuri ketika tarif berubah |
| Pembayaran | Tagihan, nominal, kanal, tanggal, bukti, dan status | Pengajuan transfer dibedakan dari pembayaran terkonfirmasi |
| Pemeriksaan pembayaran | Pembayaran, pemeriksa, keputusan, waktu, dan alasan | Riwayat pengembalian dan pengajuan ulang tidak ditimpa |
| Setoran kas | Cabang, transaksi asal, nominal, penyerah, dan penerima | Setoran merujuk penerimaan yang sudah dicatat, bukan pendapatan baru |
| Pencocokan penerimaan | Asal transaksi, referensi mutasi, nominal cocok, dan catatan selisih | Satu referensi tidak dipakai ulang tanpa penanganan yang dapat dijelaskan |
| Jejak aktivitas dan notifikasi | Tindakan penting serta pengajuan yang belum diperiksa | Pembacaan notifikasi berbeda dari keputusan verifikasi |

Pencocokan bank menggunakan salah satu asal transaksi, yaitu transfer siswa atau setoran kas ke rekening. Referensi mutasi dicatat melalui pemeriksaan manual atau dokumen terbatas yang diizinkan, tanpa mengasumsikan adanya koneksi langsung dengan layanan bank.

Rincian hubungan, kunci, aturan nilai kosong, dan ketergantungan atribut dijabarkan kembali pada skema fisik sebelum implementasi. Aturan transaksi diterapkan untuk mencegah persetujuan pembayaran ganda dan pengisian tempat kelas yang melampaui kapasitas.

### 3.4.7 Perancangan Antarmuka

Antarmuka disusun berdasarkan urutan pekerjaan setiap peran. Informasi yang memerlukan tindak lanjut, seperti pengajuan transfer dan tagihan lewat jatuh tempo, ditempatkan pada dasbor pengguna yang berwenang.

Tabel 3.14 menyajikan rancangan halaman dan unsur tampilannya. Rancangan visual rinci dikembangkan dari susunan tersebut, kemudian diperiksa melalui tugas UAT dan masukan pengguna.

**Tabel 3.14 Rancangan Halaman Antarmuka**

| Halaman | Informasi dan tindakan utama | Pengguna |
| :--- | :--- | :--- |
| Dasbor cabang | Ringkasan siswa, kapasitas, tunggakan, dan status pengajuan | Admin Cabang |
| Siswa dan keanggotaan | Formulir siswa, daftar kelas, indikator keterisian, dan perubahan keanggotaan | Admin Cabang |
| Jadwal | Daftar tentor, ruang, waktu, dan rincian potensi benturan | Admin Cabang dan Super Admin sesuai kewenangan |
| Tagihan | Periode, jatuh tempo, nominal, sisa, dan tautan WhatsApp | Admin Cabang |
| Pengajuan transfer | Formulir pembayaran, unggah bukti, status, dan alasan pengembalian | Admin Cabang |
| Pemeriksaan pembayaran | Daftar menunggu verifikasi, bukti, referensi pemeriksaan, dan keputusan | Super Admin |
| Dasbor pusat | Penyaring cabang/periode, penerimaan terkonfirmasi, dan pengajuan tertunda | Super Admin |
| Pencocokan penerimaan | Transaksi sumber, setoran, referensi mutasi, serta catatan selisih | Super Admin |

Warna indikator disertai label teks agar maknanya tidak hanya bergantung pada warna. Kelas penuh menampilkan jumlah peserta dan kapasitas, sedangkan penolakan penambahan menjelaskan alasan serta pilihan mencari kelas lain.

Perubahan status pembayaran menggunakan istilah yang sama pada daftar, rincian, dan laporan. Bukti transfer yang belum diperiksa tidak ditampilkan sebagai tagihan lunas, sedangkan pengembalian pengajuan selalu menampilkan alasan yang dapat ditindaklanjuti.

## 3.5 Spesifikasi Teknis

Spesifikasi teknis disusun sebagai kebutuhan awal implementasi prototipe. Versi perangkat lunak, kapasitas perangkat, dan konfigurasi pengujian akan dibekukan serta dicatat sebelum hasil pengujian digunakan untuk penarikan simpulan.

### 3.5.1 Arsitektur Sistem

Arsitektur dirancang dengan pemisahan antarmuka web dan layanan pengolahan data. Next.js digunakan pada antarmuka, Laravel digunakan untuk aturan bisnis dan layanan data, sedangkan MySQL digunakan sebagai penyimpanan terpusat.

Gambar 3.4 menyajikan hubungan pengguna, antarmuka, layanan, penyimpanan, dan proses eksternal. Pemilihan arsitektur merupakan keputusan teknis penelitian, sehingga tidak digunakan sebagai bukti otomatis bahwa prototipe lebih cepat atau lebih aman daripada arsitektur lain.

![Arsitektur prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_4_Arsitektur_Prototipe.png>)

**Gambar 3.4 Arsitektur Prototipe Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan akses multicabang dan pemisahan proses pengelolaan data.

Autentikasi direncanakan menggunakan fasilitas Laravel Sanctum dengan sesi berbasis kuki untuk antarmuka milik aplikasi sendiri. Konfigurasi domain, perlindungan permintaan, serta masa sesi disesuaikan dengan lingkungan penerapan dan diperiksa sebelum pengujian pengguna (Laravel, t.t.-a).

Pengajuan pembayaran menghasilkan notifikasi dalam dasbor Super Admin melalui penyimpanan notifikasi aplikasi. Mekanisme penyimpanan dan penyajiannya mengikuti dokumentasi notifikasi Laravel, sedangkan notifikasi WhatsApp atau surel otomatis tidak menjadi kebutuhan inti (Laravel, t.t.-b).

Data dasbor dimuat dari layanan terpusat saat halaman dibuka atau diperbarui setelah tindakan pengguna. Istilah waktu nyata pada rancangan ini dibatasi pada informasi tersimpan terbaru yang dimuat melalui layanan, bukan jaminan pembaruan serentak tanpa pemuatan ulang pada seluruh perangkat.

Kebutuhan pembaruan berkala dan batas waktu tanggapan akan diperiksa bersama mitra sebelum ditetapkan sebagai kriteria penerimaan. Mekanisme yang akhirnya digunakan serta hasil pengukurannya dicatat pada bab hasil agar tidak terjadi perbedaan antara istilah dan pelaksanaan.

### 3.5.2 Perangkat Keras

Perangkat keras pengembangan direncanakan berupa komputer yang dapat menjalankan penyunting kode, peramban, layanan aplikasi, dan basis data lokal. Perangkat pengguna berupa komputer atau telepon yang dapat mengakses lingkungan uji dan membuka tautan WhatsApp.

Tabel 3.15 menyajikan kebutuhan perangkat menurut fungsinya. Angka kapasitas aktual tidak dinyatakan sebelum perangkat pengembangan dan lokasi pengujian dipastikan.

**Tabel 3.15 Rencana Kebutuhan Perangkat Keras**

| Perangkat | Fungsi | Informasi yang dicatat sebelum pengujian |
| :--- | :--- | :--- |
| Komputer pengembangan | Pengodean, menjalankan layanan lokal, dan pengujian | Prosesor, memori, ruang penyimpanan, dan sistem operasi |
| Perangkat uji komputer | Pengujian tugas administrasi melalui peramban | Resolusi, peramban, versi, dan kondisi jaringan |
| Telepon uji | Pemeriksaan tampilan dan pembukaan tautan WhatsApp | Sistem operasi, peramban, dan ketersediaan aplikasi WhatsApp |
| Peladen lingkungan uji | Penyajian aplikasi kepada perwakilan mitra | Kapasitas layanan, versi lingkungan, akses, dan lokasi penyimpanan |
| Perangkat cetak apabila digunakan | Pemeriksaan keterbacaan kuitansi | Ukuran kertas dan konfigurasi cetak yang tersedia |

Kemampuan perangkat diperiksa melalui pelaksanaan fungsi inti pada data uji yang dijelaskan. Spesifikasi yang dicatat menjadi konteks hasil pengujian, sehingga hasil satu perangkat tidak digeneralisasi sebagai kemampuan seluruh perangkat pengguna.

### 3.5.3 Perangkat Lunak dan Versi Teknologi

Pemilihan perangkat lunak mempertimbangkan kebutuhan sistem dan kesesuaian antarkomponen. Daftar komponen pada Tabel 3.16 merupakan rencana teknologi, sedangkan versi terpasang akan dicatat melalui berkas konfigurasi dan penguncian dependensi.

**Tabel 3.16 Rencana Perangkat Lunak Pengembangan**

| Komponen | Pilihan rancangan | Ketentuan pencatatan versi |
| :--- | :--- | :--- |
| Antarmuka | Next.js dan React | Versi utama serta pembaruan yang digunakan dibekukan sebelum pengujian |
| Tata tampilan | Tailwind CSS | Versi dan konfigurasi pembangunan dicatat bersama antarmuka |
| Layanan aplikasi | Laravel dan PHP | Pasangan versi dipilih berdasarkan kompatibilitas dan dukungan yang masih berlaku |
| Autentikasi | Laravel Sanctum | Mode sesi serta konfigurasi domain dan keamanan dicatat |
| Basis data | MySQL dengan dukungan transaksi | Versi, mesin penyimpanan, zona waktu, dan aturan koneksi dicatat |
| Pengelolaan dependensi | Pengelola paket JavaScript dan Composer | Berkas penguncian dependensi disimpan bersama kode |
| Pengujian | Perangkat uji unit dan layanan yang sesuai dengan teknologi terpilih | Versi, konfigurasi, dan cara menjalankan pengujian didokumentasikan |
| Pemodelan dan dokumentasi | Perangkat penyusun diagram serta pengelola referensi | Berkas sumber diagram dan basis data referensi disimpan |

Persyaratan lingkungan Next.js diperiksa melalui dokumentasi instalasi resmi sesuai versi yang dipilih (Vercel, t.t.). Pasangan PHP dan Laravel diperiksa melalui kebijakan rilis yang berlaku, sehingga versi pada artikel terdahulu tidak langsung diperlakukan sebagai versi implementasi penelitian ini (Laravel, t.t.-c).

Artikel berbasis Laravel digunakan sebagai pembanding penerapan pada sistem informasi, bukan sumber tunggal untuk seluruh konfigurasi teknis. Pilihan versi akhir perlu disesuaikan dengan lingkungan yang tersedia dan dicatat agar pelaksanaan pengujian dapat diulang.

### 3.5.4 Lingkungan Implementasi dan Pengujian

Lingkungan pengembangan dipisahkan dari lingkungan evaluasi mitra. Data buatan atau tersamarkan digunakan untuk pengujian awal, sedangkan penggunaan data nyata dibatasi sesuai izin dan kebutuhan tugas yang diperiksa.

Berkas bukti pembayaran disimpan pada lokasi yang memerlukan pemeriksaan kewenangan. Kata sandi, pengaturan koneksi, dan kredensial rekening tidak dimasukkan ke laporan, repositori terbuka, atau gambar hasil pengujian.

Periode tagihan, waktu pengajuan, dan waktu pemeriksaan menggunakan zona waktu operasional Balikpapan. Penghitungan jatuh tempo didasarkan pada tanggal yang ditetapkan untuk tagihan, sehingga tidak diasumsikan seluruh siswa mempunyai tanggal jatuh tempo yang sama.

Pengujian bersama mitra direncanakan pada lingkungan yang mewakili alur administrasi cabang dan pemantauan pusat. Jumlah akun, jumlah data, kondisi jaringan, versi aplikasi, serta perangkat yang digunakan dicatat agar konteks hasil evaluasi dapat diketahui.

Pencadangan mencakup basis data dan berkas pendukung yang saling berkaitan. Pemulihan diperiksa pada lingkungan uji sebelum dinyatakan sebagai kemampuan prototipe.

## 3.6 Jadwal Pembuatan Prototipe

Jadwal awal disusun selama dua belas minggu relatif dengan empat iterasi pengembangan. Minggu pertama dihitung sejak dimulainya pelaksanaan yang disepakati, sehingga tabel ini tidak menyatakan tanggal penelitian yang belum ditetapkan.

Tabel 3.17 menunjukkan pembagian kegiatan mingguan dari pemeriksaan kebutuhan sampai penyusunan luaran. Pengujian unit, pengujian sistem, dan evaluasi iterasi dilaksanakan dalam setiap iterasi, sedangkan evaluasi lintas fungsi dijadwalkan setelah integrasi.

**Tabel 3.17 Rencana Jadwal Pembuatan Prototipe**

| Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Telaah literatur dan bukti wawancara | X | X | | | | | | | | | | |
| Klarifikasi serta validasi kebutuhan | X | X | | | | | | | | | | |
| Perencanaan tugas dan instrumen | | X | | | | | | | | | | |
| Iterasi pertama | | | X | X | | | | | | | | |
| Iterasi kedua | | | | | X | X | | | | | | |
| Iterasi ketiga | | | | | | | X | X | | | | |
| Iterasi keempat | | | | | | | | | X | X | | |
| Evaluasi penerimaan dan tindak lanjut | | | | | | | | | | | X | X |
| Dokumentasi pengembangan | | X | X | X | X | X | X | X | X | X | X | X |
| Penyiapan laporan, artikel, dan HKI | | | | | | | | | | | X | X |

Alokasi tersebut disesuaikan kembali setelah estimasi tugas dan ketersediaan mitra dikonfirmasi. Apabila masukan evaluasi membutuhkan perubahan fungsi, jadwal revisi dicatat beserta pengaruhnya terhadap kegiatan berikutnya.

Dokumentasi disusun selama proses pengembangan agar bukti kebutuhan, perubahan, dan hasil uji tidak terkumpul hanya pada akhir kegiatan. Penyusunan laporan serta referensi mengikuti panduan kepenulisan ITK, sedangkan bukti pemenuhan luaran dilaporkan sesuai ketentuan tugas akhir prototipe (Institut Teknologi Kalimantan, 2025a; Institut Teknologi Kalimantan, 2026).
