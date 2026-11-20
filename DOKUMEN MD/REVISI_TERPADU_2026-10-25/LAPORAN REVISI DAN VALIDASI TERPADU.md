# Laporan revisi dan validasi terpadu ARTHA

Catatan versi: laporan ini merekam revisi terpadu sebelum perubahan struktur menjadi lima subbab utama. Susunan Bab 3 terkini dijelaskan pada [laporan restrukturisasi proposal](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/RESTRUKTURISASI_PROPOSAL_2026-10-25/LAPORAN PENYESUAIAN STRUKTUR BAB 3.md>).

Revisi dilakukan pada dokumen use case, rancangan basis data, serta Bab 3 pada 25 Oktober 2026. Berkas asli sebelum revisi tersimpan pada folder SEBELUM_REVISI agar perubahan dapat dibandingkan tanpa kehilangan rancangan terdahulu.

## 1. Berkas yang digunakan setelah revisi

Ketiga berkas utama telah diperbarui langsung pada lokasi semula. Dokumen pendamping memuat rincian yang tidak perlu memenuhi badan Bab 3, termasuk kasus uji, log, sumber kebutuhan, dan keputusan terbuka.

| Berkas | Isi setelah revisi |
| :--- | :--- |
| [Use case dan skenario](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/PERANCANGAN USE CASE & SKENARIO.md>) | Empat belas UC, skenario normal dan alternatif, aturan lintas proses, serta peta perubahan nomor lama |
| [Basis data dan ERD](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md>) | Dua puluh tiga tabel, 241 atribut, 51 kunci asing, kamus data, dan aturan transaksi |
| [Bab 3 revisi](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md>) | Enam subbab utama, dua puluh tabel, sepuluh gambar, serta prosedur pengembangan dan evaluasi |
| [Matriks keterlacakan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/MATRIKS KETERLACAKAN KEBUTUHAN.md>) | Empat belas KF, US, kelompok PU, tugas UAT, serta hubungan dengan UC, tabel, dan iterasi |
| [Lampiran pengujian](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/LAMPIRAN PENGUJIAN DAN PELAKSANAAN.md>) | Tiga puluh tiga rancangan kasus BB, lembar hasil, catatan PxP, instrumen UAT, dan penyiapan serah uji |
| [Sumber dan keputusan terbuka](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/SUMBER KEBUTUHAN DAN KEPUTUSAN TERBUKA.md>) | Lokator wawancara, status keputusan, dan daftar penyelarasan Bab 1 serta Bab 2 |

## 2. Perubahan substansi utama

WhatsApp diperbarui menjadi tindakan manual melalui tombol dengan nomor serta pesan yang disiapkan berdasarkan tunggakan. Catatan hanya menunjukkan permintaan tautan oleh admin dan tidak membuktikan pesan terkirim, diterima, atau dibaca.

Pembayaran induk dipisahkan dari alokasi tagihan dan keputusan pemeriksaan. Pengajuan transfer belum melunasi tagihan, sedangkan pengajuan yang dikembalikan diperbaiki melalui baris baru yang mempertahankan hubungan dengan bukti serta keputusan lama.

Penerimaan tunai, penyerahan ke pusat, penyetoran ke bank, serta pencocokan dana masuk dipisahkan. Perpindahan uang tidak dihitung kembali sebagai penerimaan siswa, dan sisa tagihan tidak dipakai sebagai pengganti selisih pencocokan bank.

Jumlah peserta kelas diturunkan dari interval keanggotaan aktif. Penambahan saat penuh ditolak, pengakhiran keanggotaan membuka tempat, dan masuk kembali membentuk interval baru tanpa menghapus sejarah.

Rancangan jadwal menggunakan peringatan dan peninjauan konflik, dengan calon jadwal dapat disimpan nonaktif. Pengaktifan pengecualian konflik memerlukan kebijakan mitra, sedangkan pemeriksaan ruang, tentor, kelas, masa berlaku, serta jadwal sendiri dibedakan.

Tarif dapat dibedakan menurut cabang, sesi, program, jenjang, siklus, dan masa berlaku. Potongan aktual serta nilai historis berada pada tagihan, sehingga nominal Rp200.000 tidak dipatok sebagai pengurangan setiap tagihan seluruh siswa.

## 3. Tindak lanjut terhadap dua puluh sembilan temuan audit

Tabel berikut menjelaskan bagaimana temuan sebelumnya ditangani pada tingkat rancangan. Status diperbaiki berarti isi dokumen telah diselaraskan, bukan bahwa aplikasi atau kebijakan mitra telah lulus evaluasi.

| Temuan | Perubahan yang diterapkan | Batas yang masih terbuka |
| :--- | :--- | :--- |
| F01 WhatsApp otomatis | UC-09 dan reminder_actions menggantikan penjadwal serta status pengiriman | Pemeriksaan tautan pada perangkat dilakukan saat implementasi |
| F02 Pembagian pemeriksa | Admin mengajukan dan Super Admin memeriksa sebagai rancangan kerja yang konsisten | Kewenangan rekening dan perubahan batasan Bab 1 menunggu penetapan |
| F03 Pengembalian dan pengajuan ulang | payments.resubmission_of_id dan keputusan final pada payment_reviews | Uji riwayat serta penyimpanan privat belum dijalankan |
| F04 Bukti bukan pelunasan | Hanya cash recorded dan bank_transfer verified menjadi penerimaan sah | Prosedur tunai dan cicilan perlu validasi |
| F05 Beberapa periode | payment_allocations menghubungkan satu pembayaran dengan beberapa tagihan siswa dan cabang yang sama | Penggunaan proses ditinjau bersama mitra |
| F06 Makna rekonsiliasi | bank_entries dan bank_matches memisahkan pencocokan dari tunggakan | Batas satu sumber penuh dan pengecualian perlu ditinjau |
| F07 Setoran tunai | cash_batches dan cash_batch_items menelusuri sumber serta perpindahan kas | Petugas dan jadwal penyerahan ditetapkan mitra |
| F08 Variasi tarif | fee_tariffs mempunyai cakupan cabang, sesi, dan masa berlaku | Nilai serta aturan nyata belum dibekukan |
| F09 Potongan tetap | Potongan aktual, alasan, dan pemberi persetujuan berada pada bills | Nominal serta cakupan potongan ditetapkan mitra |
| F10 Paket dianggap bulanan | Siklus bulanan, semester, tahunan, dan sekali dibedakan | Daftar paket yang berlaku diperlukan |
| F11 Rujukan tabel hilang | Matriks aktif memakai seluruh nama tabel skema revisi | Tidak ada empat tabel konfigurasi yang dijanjikan tetapi tidak tersedia |
| F12 Pengaturan melalui dasbor | Tarif dan parameter kelas tersimpan; templat awal melalui konfigurasi berversi | Editor templat dasbor berada di luar inti |
| F13 Siswa keluar | Interval masuk, keluar, alasan, dan masuk kembali dijelaskan | Data uji keanggotaan belum dieksekusi |
| F14 Daftar tunggu | Dikeluarkan dari fungsi inti | Dapat dipertimbangkan pada pengembangan berikutnya |
| F15 Ambang tanpa dasar | Ambang menjadi parameter kelas; beban tentor berupa durasi | Nilai ambang dan kriteria beban memerlukan ketentuan mitra |
| F16 Kapasitas serentak | Pemeriksaan peladen dan penguncian kelas dirancang pada semua jalur perubahan | Pembuktian transaksi serentak memerlukan aplikasi |
| F17 Benturan jadwal | Masa berlaku, hari, irisan, status, kelas, ruang, dan pengecualian diri dijelaskan | Kebijakan pengecualian serta uji serentak belum dijalankan |
| F18 Konsistensi cabang | Pemeriksaan objek, ruang, siswa, dan cabang menjadi aturan peladen | Penempatan lintas cabang belum diaktifkan sebelum kebijakannya ditetapkan |
| F19 Riwayat cabang | Cabang historis disimpan pada tagihan dan pembayaran | Uji pemindahan siswa belum dijalankan |
| F20 Pelunasan dan terlambat | Kondisi pelunasan dan lewat jatuh tempo dihitung terpisah | Hasil dasbor belum merupakan hasil implementasi |
| F21 Nilai dan duplikasi | Kunci bisnis, batas nominal, keputusan tunggal, dan referensi unik dijelaskan | Migrasi SQL serta batas fisik belum dieksekusi |
| F22 TK dan paket | Jenjang termasuk TK serta siklus biaya dibedakan dari program | Formulir dan ketentuan nyata perlu diperiksa pada UAT |
| F23 Arah UML | Diagram disederhanakan menjadi asosiasi tujuan pengguna | Tidak menggunakan relasi include atau extend yang tidak diperlukan |
| F24 Tujuan tercampur | Kelas, keanggotaan, jadwal, pengajuan, pemeriksaan, serta pencocokan dipisahkan | Nomor lama harus dibaca melalui peta migrasi |
| F25 Otorisasi | Peran dan objek cabang menjadi dasar izin; cabang kosong tidak memberikan hak pusat | Uji akses dilakukan pada layanan dan antarmuka |
| F26 Statistik dokumen | Jumlah UC, tabel, relasi, dan artefak dihitung ulang | Hitungan tidak dianggap bukti kualitas atau penerimaan |
| F27 Klaim lapangan | Jumlah tentor dan insiden yang belum terbukti tidak dinyatakan sebagai fakta | Tanggal pada notulensi perlu dicocokkan dengan bukti asli |
| F28 Lingkup tambahan | Daftar tunggu otomatis, kartu anggota, QRIS, dan integrasi publik dipisahkan dari inti | Penambahan fitur memerlukan dasar kebutuhan serta waktu |
| F29 Pengurangan tabel | MySQL InnoDB dipilih sebagai sasaran; jumlah tabel mengikuti kebutuhan hubungan | Versi dan implementasi fisik belum dibekukan |

## 4. Pelaksanaan sembilan revisi Bab 3

Enam subbab template tetap dipertahankan dan uraian produk dipadatkan pada bagian awal. Penambahan rincian difokuskan pada artefak serta prosedur yang diperlukan untuk melaksanakan pengembangan dan evaluasi.

| Poin | Perubahan | Status |
| :--- | :--- | :--- |
| Narasi produk dan struktur | Garis besar lebih ringkas; enam subbab utama dipertahankan | Diterapkan |
| Sumber dan keterlacakan | Sumber S-01 sampai S-07; pemetaan empat belas KF/US/UC/PU/UAT | Diterapkan |
| Pembayaran dan kapasitas | Alur lintas peran, riwayat, alokasi, kelas penuh, serta siswa keluar dijelaskan | Diterapkan sebagai rancangan, kewenangan mitra masih terbuka |
| Rancangan antarmuka | Enam layar pada Gambar 3.4 sampai Gambar 3.9 dengan tiga kalimat penjelas per gambar | Diterapkan; seluruh data simulasi |
| Diagram alir | Keputusan gagal uji, iterasi berikutnya, UAT, dan perubahan kebutuhan diperlihatkan | Diterapkan |
| UAT dan penyiapan | Pemilihan peserta, urutan kegiatan, data, lingkungan, keputusan, bukti, dan serah uji | Diterapkan sebagai prosedur; peserta belum ditetapkan |
| Spesifikasi dan jadwal | Versi antarmuka diperiksa dari lockfile lokal; perangkat, layanan, dan kalender diberi status | Diterapkan sejauh bukti tersedia; bukan semua spesifikasi telah final |
| Pemindahan rincian | Seluruh kasus, lembar log, dan catatan sumber berada pada lampiran pendamping | Diterapkan |
| Keselarasan Bab 1 dan Bab 2 | Daftar perubahan antarbab disiapkan pada register keputusan | Belum mengubah Bab 1 dan Bab 2; menunggu keputusan yang memengaruhi isinya |

## 5. Pemeriksaan yang telah dilaksanakan

Pemeriksaan basis data lulus lima belas pemeriksaan struktur, sedangkan pemeriksaan Bab 3 lulus dua puluh satu pemeriksaan bentuk naskah, sumber, dan berkas. Pemeriksaan terpadu lulus tujuh puluh enam pemeriksaan pemetaan, relasi yang dinyatakan, tautan, gambar, serta konsistensi kode.

Pemeriksaan silang isi juga menemukan dan memperbaiki ketidaksesuaian pelaksana UAT jadwal, asosiasi Super Admin pada pengelolaan ruang, serta redaksi yang semula menyiratkan pembahasan mitra telah dilakukan. Kasus benturan ruang, pembatalan transaksi secara utuh, dan kelompok kas lintas periode ditambahkan ke rancangan pengujian.

| Bukti pemeriksaan | Isi |
| :--- | :--- |
| [Validasi terpadu](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/HASIL VALIDASI TERPADU.json>) | Pemeriksaan terpadu, hitungan artefak, hash berkas, serta batas pemeriksaan |
| [Validasi basis data](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/VALIDASI_BASIS_DATA.json>) | Kesamaan kamus data, ERD, metadata, kunci asing, serta kardinalitas |
| [Pemeriksaan Bab 3](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/HASIL PEMERIKSAAN DRAF.json>) | Bentuk paragraf, urutan tabel/gambar, referensi sumber, dan tautan lokal |
| [Montage gambar](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/REVISI_TERPADU_2026-10-25/KONTAK_GAMBAR_REVISI.png>) | Ringkasan visual sepuluh gambar untuk pemeriksaan manual |

PNG telah dibuka dan SVG telah diperiksa sebagai XML, disertai pemeriksaan visual diagram serta antarmuka inti. Hal tersebut tidak membuktikan tata letak halaman Word, keterbacaan pada ukuran cetak akhir, atau keberhasilan fungsi aplikasi.

## 6. Batas hasil dan langkah sebelum konsultasi

Ketiga dokumen lebih konsisten sebagai rancangan proposal, tetapi belum merupakan skema produksi, laporan pengujian aplikasi, atau pengesahan kebijakan mitra. Tidak ada migrasi SQL, pengujian transaksi serentak, maupun UAT yang dinyatakan telah dilaksanakan.

Sebelum konsultasi, pembahasan perlu difokuskan pada kewenangan pemeriksaan rekening, tarif dan potongan, kapasitas aktual, serta batas pencocokan. Peserta UAT, tanggal pelaksanaan, perangkat, versi layanan, serta kalender pengembangan perlu dilengkapi sebelum rancangan dibekukan.

Bab 1 yang masih menyebut verifikasi Admin Cabang perlu disesuaikan apabila usulan pemeriksaan pusat ditetapkan. Bab 2 juga perlu mengikuti UAT berbasis tugas dan cakupan pencocokan manual pada Bab 3, sedangkan halaman Word/PDF final diperiksa setelah penggabungan naskah.
