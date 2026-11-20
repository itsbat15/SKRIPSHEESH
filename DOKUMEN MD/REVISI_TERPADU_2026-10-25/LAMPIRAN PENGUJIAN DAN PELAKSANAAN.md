# Lampiran rancangan pengujian dan pelaksanaan ARTHA

Lampiran ini memuat kasus uji, bentuk pencatatan PxP, dan lembar penerimaan untuk mendukung Bab 3. Seluruh kasus masih berstatus belum diuji dan tidak merupakan laporan keberhasilan aplikasi.

## 1. Kasus pengujian sistem

Nilai kapasitas, nama cabang, dan transaksi pada prasyarat merupakan data simulasi yang akan disiapkan pengembang. Versi aplikasi, kondisi awal, hasil aktual, serta penunjuk bukti harus dicatat pada saat pelaksanaan.

| Kode | Kelompok | Prasyarat atau data uji | Langkah pokok | Keluaran yang diharapkan | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| BB-01 | PU-01 | Akun Admin Cabang A dan siswa B tersedia | Masuk sebagai A; minta rincian siswa B melalui halaman dan layanan | Akses ditolak dan data B tidak dikirim | Belum diuji |
| BB-02 | PU-02 | Formulir siswa baru tersedia | Kosongkan kolom wajib; simpan; lengkapi termasuk jenjang TK; simpan kembali | Data tidak lengkap ditolak; data lengkap tersimpan pada cabang benar | Belum diuji |
| BB-03 | PU-03 | Ruang uji berkapasitas dua belas dan kelas belum aktif | Atur kapasitas kelas melebihi ruang; perbaiki dan isi ambang sisa tempat yang sah | Kapasitas tidak sah ditolak; batas serta ambang sah dapat disimpan | Belum diuji |
| BB-04 | PU-04 | Kelas kapasitas dua belas berisi sebelas peserta aktif | Tambahkan satu peserta yang memenuhi syarat | Peserta menjadi dua belas dan kondisi penuh ditampilkan | Belum diuji |
| BB-05 | PU-04 | Kelas sudah penuh | Coba tambah peserta melalui antarmuka dan permintaan langsung | Penambahan ditolak dan jumlah aktif tidak berubah | Belum diuji |
| BB-06 | PU-04 | Kelas penuh dengan riwayat peserta tersedia | Akhiri satu keanggotaan beserta alasan; masukkan kembali siswa jika syarat terpenuhi | Tempat terbuka; masuk kembali memakai interval baru tanpa menghapus yang lama | Belum diuji |
| BB-07 | PU-04 | Dua sesi admin dan satu tempat terakhir | Kirim dua permintaan penempatan secara bersamaan | Hanya satu peserta baru aktif; kapasitas tidak terlampaui | Belum diuji |
| BB-08 | PU-05 | Tentor yang sama memiliki jadwal berlaku di Cabang A | Buat jadwal pada cabang lain dengan hari, masa berlaku, dan jam beririsan | Peringatan irisan tentor ditampilkan tanpa membuka rincian cabang lain kepada akun yang tidak berwenang | Belum diuji |
| BB-09 | PU-05 | Jadwal aktif, nonaktif, dan periode berbeda tersedia | Sunting jadwal tanpa mengubah jam; coba tanggal yang tidak beririsan | Tidak muncul benturan dengan dirinya sendiri atau jadwal yang tidak relevan | Belum diuji |
| BB-10 | PU-06 | Tarif uji berbeda menurut cabang, sesi, dan siklus | Pilih siswa serta periode; terbitkan tagihan dari tarif yang tepat | Tarif sesuai cakupan, periode paket benar, dan nilai aktual tersimpan | Belum diuji |
| BB-11 | PU-06 | Tagihan paket semester dan tagihan bulanan tersedia | Ulangi penerbitan untuk periode sama; coba penerbitan paket sebagai tagihan bulanan | Duplikasi ditolak dan paket tidak diterbitkan bulanan tanpa dasar | Belum diuji |
| BB-12 | PU-07 | Siswa memiliki dua tagihan belum lunas | Catat pembayaran tunai untuk keduanya; ulangi permintaan yang sama | Alokasi sesuai sisa, kuitansi tunggal, dan penerimaan dihitung sekali | Belum diuji |
| BB-13 | PU-08 | Tagihan dan rekening tujuan aktif tersedia | Unggah bukti dan ajukan pembayaran transfer | Status submitted; antrean tampil; sisa tagihan belum berkurang | Belum diuji |
| BB-14 | PU-08/PU-09 | Pengajuan transfer telah dikembalikan beserta alasan | Buat pengajuan perbaikan melalui tindakan pengajuan ulang | Baris baru merujuk pengajuan lama; bukti dan keputusan lama tetap tersedia | Belum diuji |
| BB-15 | PU-09/PU-13 | Pengajuan dua tagihan dan satu dana masuk sesuai tersedia | Periksa rekening, nominal, tanggal, dan referensi; setujui | Satu match dan review tersimpan; pembayaran verified; sisa berkurang sesuai alokasi | Belum diuji |
| BB-16 | PU-09 | Pengajuan telah berhasil disetujui | Kirim ulang permintaan persetujuan, termasuk permintaan serentak | Tidak ada penerimaan, keputusan, kuitansi, atau match kedua | Belum diuji |
| BB-17 | PU-10 | Tagihan lewat jatuh tempo dengan sisa dan nomor wali sah | Periksa pratinjau; buka tautan WhatsApp | Nomor, siswa, periode, sisa, dan jatuh tempo sesuai; log hanya tindakan tautan | Belum diuji |
| BB-18 | PU-10 | Nomor wali tidak sah atau tagihan sudah lunas | Coba bentuk tautan dari kondisi tersebut | Tautan penagihan ditolak atau dinonaktifkan dengan alasan yang dapat dipahami | Belum diuji |
| BB-19 | PU-11 | Pembayaran tunai sah satu cabang tersedia | Masukkan dalam kelompok kas; ajukan penyerahan; pusat mencatat penerimaan | Pembayaran asal unik; penyerah dan penerima tercatat; belum otomatis dianggap disetor bank | Belum diuji |
| BB-20 | PU-11/PU-13 | Kas diterima pusat dan kemudian disetor ke rekening resmi | Catat setoran; cocokkan dana masuk nominal penuh; periksa total penerimaan | Status perpindahan dapat ditelusuri; setoran tidak menambah penerimaan siswa | Belum diuji |
| BB-21 | PU-12 | Siswa mempunyai transaksi lama lalu dipindah cabang secara berwenang | Bandingkan rekap sebelum dan setelah pemindahan; telusuri rincian | Penerimaan historis tetap pada cabang transaksi dan tidak berlipat karena alokasi | Belum diuji |
| BB-22 | PU-13 | Referensi mutasi sudah dipakai atau nominal berbeda | Coba cocokkan untuk sumber lain; coba sumber berbeda nominal | Penggunaan ulang dan pencocokan nominal tidak sesuai ditolak; selisih ditampilkan | Belum diuji |
| BB-23 | PU-14 | Akun cabang dan akun Super Admin aktif tersedia | Ubah peran, data rekening, atau tahun aktif dengan kedua akun | Hanya kewenangan yang sah diterima; perubahan tercatat dan tahun aktif konsisten | Belum diuji |
| BB-24 | PU-09/PU-13/PU-14 | Bukti transfer privat dan rekening resmi tersedia | Minta bukti atau referensi melalui akun tidak berwenang serta tautan langsung | Akses ditolak dan data privat tidak tersedia melalui alamat publik | Belum diuji |
| BB-25 | PU-08/PU-09 | Dua pengajuan berbeda menunjuk sisa tagihan yang sama | Setujui pengajuan pertama; coba setujui pengajuan kedua | Validasi ulang menolak alokasi yang melampaui sisa; dana tidak dihitung ganda | Belum diuji |
| BB-26 | PU-03/PU-04 | Kelas aktif mempunyai peserta dan ruang memadai | Pindahkan ke ruang lebih kecil atau turunkan kapasitas di bawah jumlah aktif | Perubahan yang melanggar daya tampung ditolak tanpa mengubah riwayat peserta | Belum diuji |
| BB-27 | PU-06 | Tarif normal dan potongan yang telah diotorisasi tersedia sebagai data uji | Terbitkan tagihan dengan alasan serta pemberi persetujuan; ubah tarif berikutnya | Potongan aktual tertelusur dan tagihan lama tidak berubah | Belum diuji |
| BB-28 | PU-14 | Cadangan basis data dan berkas bukti dari versi uji tersedia | Pulihkan pada lingkungan terpisah; periksa relasi serta akses berkas | Data dan bukti dapat diakses sesuai kewenangan tanpa ketidaksesuaian relasi | Belum diuji |
| BB-29 | PU-05 | Ruang Cabang B dan kelas Cabang A tersedia | Buat jadwal kelas A menggunakan ruang B tanpa kebijakan lintas cabang | Penetapan tidak sah ditolak; waktu selesai harus sesudah mulai | Belum diuji |
| BB-30 | PU-01/PU-14 | Akun cabang kehilangan penugasan atau sesi telah diakhiri | Akses ulang layanan dengan sesi lama atau cabang kosong | Tidak memperoleh akses operasional atau hak Super Admin dari cabang kosong | Belum diuji |
| BB-31 | PU-05 | Dua kelas memiliki sesi pada ruang sama; satu kelas memiliki dua calon sesi | Buat sesi beririsan dengan tentor berbeda pada ruang sama; ulangi untuk kelas sama pada ruang berbeda | Konflik ruang dan konflik kelompok masing-masing ditampilkan; calon jadwal nonaktif sampai peninjauan selesai | Belum diuji |
| BB-32 | PU-09/PU-13 | Pengajuan submitted dan rujukan bank cocok tersedia pada lingkungan uji | Simulasikan kegagalan penyimpanan setelah match mulai dibuat sebelum keputusan tersimpan; periksa keadaan akhir | Seluruh transaksi dibatalkan; tidak ada match, review, kuitansi, atau pelunasan sebagian yang tertinggal | Belum diuji |
| BB-33 | PU-12/PU-13 | Kelompok kas memuat pembayaran dua bulan dan dicocokkan pada bulan ketiga | Bandingkan penerimaan dan dana cocok pada filter bulan penerimaan serta filter tanggal pencocokan | Perbandingan memakai sumber dan periode yang sama; tanggal pencocokan tidak memindahkan penerimaan atau membuat selisih palsu | Belum diuji |

Pengujian serentak memerlukan dua sesi atau pengirim permintaan yang benar-benar dijalankan bersamaan, bukan sekadar mengklik berurutan. Bukti mencakup permintaan, hasil masing-masing, dan pemeriksaan keadaan akhir pada versi aplikasi yang sama.

## 2. Lembar hasil kasus

Satu lembar diisi untuk satu pelaksanaan kasus pada satu versi. Ketika dilakukan uji ulang, lembar baru ditautkan pada hasil sebelumnya agar kegagalan tidak terhapus.

| Unsur | Isian saat pelaksanaan |
| :--- | :--- |
| Kode kasus, kebutuhan, dan versi | Belum dilaksanakan |
| Pelaksana, tanggal, serta lingkungan | Belum dilaksanakan |
| Data awal dan langkah aktual | Belum dilaksanakan |
| Keluaran aktual dan penunjuk bukti | Belum dilaksanakan |
| Hasil lulus, gagal, atau terhalang | Belum dilaksanakan |
| Kode galat dan hubungan uji ulang | Belum dilaksanakan |

## 3. Pencatatan waktu dan evaluasi PxP

Durasi dicatat per tugas beserta kategorinya agar waktu pengodean tidak dicampur dengan seluruh waktu proyek. Estimasi pertama diisi sebelum pengerjaan dan diperbarui pada rencana berikutnya dengan merujuk waktu aktual.

| Dokumen | Kolom yang disiapkan |
| :--- | :--- |
| Estimasi tugas | Kode tugas, KF/US, iterasi, prasyarat, uraian, kategori, estimasi jam, dasar estimasi, pelaksana |
| Waktu aktual | Kode tugas, tanggal, mulai, selesai, jeda, durasi bersih, versi, catatan |
| Galat | Kode, kasus pemicu, versi, dampak, prioritas, pelaksana perbaikan, versi perbaikan, uji ulang, status |
| Perubahan | Sumber, tanggal, kebutuhan terdampak, alasan, keputusan, pengaruh jadwal, penanggung jawab |
| Evaluasi iterasi | Rencana dan hasil, selisih waktu, galat terbuka, penyebab, tindakan berikutnya, keputusan menutup atau mengulang |

## 4. Penyiapan dan lembar UAT

Peserta menjalankan tugas sesuai kewenangan pada data simulasi setelah lingkungan lolos pemeriksaan awal. Instrumen perlu ditinjau pembimbing dan perwakilan mitra sebelum dipakai untuk keputusan penerimaan.

| Unsur | Rencana pencatatan |
| :--- | :--- |
| Pemilihan peserta | Peran, pengalaman tugas, cabang, alasan pemilihan, kesediaan; jumlah belum ditetapkan |
| Validasi isi | Nama penelaah, tanggal, pemetaan kebutuhan, catatan bahasa dan perbaikan instrumen |
| Lingkungan | Versi, URL terbatas, perangkat, peramban, jaringan, zona waktu, akun uji |
| Pengarahan | Tujuan, data simulasi, panduan, batas bantuan, persetujuan pencatatan |
| Pelaksanaan tugas | Kode UAT-01 sampai UAT-14, peserta, langkah, hasil aktual, bantuan, bukti |
| Keputusan | Diterima, memerlukan perbaikan, atau belum dievaluasi, disertai alasan |
| Tindak lanjut | Masalah, kebutuhan terdampak, versi perbaikan, tanggal uji ulang, keputusan berikutnya |
| Bukti evaluasi | Lembar keputusan atau berita acara, catatan pengamatan, tangkapan layar yang diizinkan |

Tugas UAT-01 sampai UAT-14 mengikuti urutan KF-01 sampai KF-14 pada Bab 3 dan dokumen use case. Jumlah pelaksanaan bergantung pada peserta yang berwenang, sehingga satu tugas yang dijalankan dua peserta dicatat sebagai dua pelaksanaan.

## 5. Persiapan penyerahan prototipe

Versi yang diserahkan untuk evaluasi dilengkapi panduan dan daftar keterbatasan. Penggunaan untuk operasional nyata memerlukan kesepakatan mitra tentang akses, data, dukungan, dan pencadangan.

| Urutan | Pemeriksaan atau bukti |
| :--- | :--- |
| Penyiapan lingkungan | Dependensi, konfigurasi privat, basis data, berkas, jaringan, dan zona waktu diperiksa |
| Data serta akun | Data simulasi dimuat; akun dua cabang dan pusat diperiksa kewenangannya |
| Pemeriksaan awal | Login, siswa, kelas, pembayaran, serta rekap diuji sebelum pengguna hadir |
| Pencadangan | Basis data dan berkas dicadangkan; pemulihan diperiksa pada lingkungan terpisah |
| Evaluasi | Tugas, hasil, galat, bantuan, dan keputusan dicatat |
| Perbaikan | Galat penting diperbaiki dan diuji ulang; versi sebelumnya tetap dapat ditelusuri |
| Serah uji | Versi, panduan, keterbatasan, daftar akun berwenang, dan berita acara disiapkan |

## 6. Analisis hasil yang akan digunakan

Persentase lulus menggunakan jumlah kasus lulus dibagi kasus yang dijalankan, sedangkan cakupan menggunakan kasus dijalankan dibagi kasus direncanakan. Apabila tidak ada kasus dijalankan, persentase tidak dihitung dan dilaporkan belum tersedia.

Penerimaan UAT dihitung per pelaksanaan tugas yang telah dievaluasi dengan versi serta peserta yang disebutkan. Hasil uji ulang dan tugas belum dievaluasi tetap dilaporkan, sehingga angka agregat tidak menyembunyikan galat kritis atau ketidakterwakilan proses.
