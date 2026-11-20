# Catatan penyusunan dan pemeriksaan draf Bab 3

Draf disusun untuk penelitian berjudul “Pengembangan Sistem Informasi Manajemen Operasional Berbasis Web untuk Bimbingan Belajar Artha Balikpapan”. Berkas utama merupakan bahan revisi proposal dengan struktur jalur prototipe, bukan laporan bahwa aplikasi dan pengujian telah selesai.

## G.1 Ringkasan kesiapan naskah

**Kategori: perlu revisi mayor sebelum menjadi dokumen final pengajuan.** Draf sudah lengkap secara susunan dan mempunyai rancangan fungsi serta evaluasi, tetapi data pelaksanaan tertentu belum tersedia dan tata letak Word belum diterapkan.

**Skor kelengkapan draf kerja: 65 dari 100**, berdasarkan tiga belas dari dua puluh butir pada tabel berikut yang telah terpenuhi. Skor ini merupakan indeks pemeriksaan biner atas kelengkapan paket yang tersedia, bukan nilai akademik resmi ITK, bukan prediksi nilai seminar, dan bukan skor keberhasilan prototipe.

| No. | Aspek pemeriksaan paket | Terpenuhi |
| :--- | :--- | :--- |
| 1 | Enam subbab utama sesuai template | Ya |
| 2 | Penomoran tidak melebihi tiga level | Ya |
| 3 | Prosa minimal dua kalimat setiap paragraf | Ya |
| 4 | Tidak memakai dash panjang dalam prosa | Ya |
| 5 | Tidak mengawali kalimat prosa dengan angka | Ya |
| 6 | Tidak memakai kata ganti orang pertama dalam prosa | Ya |
| 7 | Tabel mempunyai nomor, judul, dan pengacuan | Ya |
| 8 | Gambar tersedia dan disebut dalam teks | Ya |
| 9 | Sitasi langsung di dalam teks tanpa penanda SIT | Ya |
| 10 | Sumber jurnal/prosiding mempunyai peta halaman | Ya |
| 11 | Tiga tujuan dipetakan ke rancangan evaluasi | Ya |
| 12 | Tidak mengarang hasil uji atau skor penerimaan | Ya |
| 13 | WhatsApp manual dan kapasitas penuh mengikuti penjelasan pengguna | Ya |
| 14 | Spesifikasi perangkat aktual sudah tercatat | Belum |
| 15 | Versi akhir perangkat lunak telah dibekukan | Belum |
| 16 | Peserta dan instrumen UAT telah dikonfirmasi serta divalidasi | Belum |
| 17 | Tanggal kalender penelitian telah disepakati | Belum |
| 18 | Wewenang pembayaran, tunai/setoran, dan parameter kapasitas telah dikonfirmasi mitra | Belum |
| 19 | Metadata tambahan dan cakupan SK seluruh edisi rujukan sudah lengkap | Belum |
| 20 | Tata letak Word/PDF final sudah diperiksa | Belum |

Kekuatan utama draf adalah pemisahan kewenangan pengguna, kejelasan sumber landasan, serta rancangan pengujian yang dapat ditelusuri ke kebutuhan. Penghitungan penerimaan juga membedakan pengajuan transfer, pembayaran terkonfirmasi, dan setoran agar tidak terjadi penghitungan ganda.

Kelemahan yang masih perlu diselesaikan adalah konfirmasi aturan keuangan, informasi pelaksanaan UAT, spesifikasi aktual, jadwal kalender, dan konsistensi dengan Bab 1 serta Bab 2. Penambahan data dilakukan berdasarkan dokumen atau persetujuan yang nyata, bukan dengan mengisi angka perkiraan sebagai fakta.

## G.2 Matriks keselarasan antarbagian

| Rumusan masalah dan tujuan Bab 1 | Batasan yang digunakan | Pelaksanaan dalam Bab 3 | Hasil dan simpulan | Status |
| :--- | :--- | :--- | :--- | :--- |
| RM/Tujuan 1: integrasi pendaftaran, pembayaran, dan jadwal | Dua peran, akses cabang, administrasi internal | 3.3 prosedur; 3.4 kebutuhan, data, dan skenario | Belum tersedia; akan dilaporkan berdasarkan hasil implementasi serta kasus uji | Selaras pada rancangan |
| RM/Tujuan 2: dasbor pusat dan pencocokan penerimaan dengan bank | Pemeriksaan manual, tanpa API bank, pemisahan penerimaan dan setoran | KF-12/KF-13, BB-14/BB-15, UAT-05/UAT-06 | Belum tersedia; tidak mengklaim rekonsiliasi saldo akuntansi lengkap | Kurang selaras sampai istilah waktu nyata dan cakupan rekonsiliasi Bab 1 dipertegas |
| RM/Tujuan 3: kesesuaian fungsi melalui Black Box Testing dan UAT | Pengujian terstruktur serta perwakilan pengguna yang relevan | 3.3.6 dan 3.3.8, kasus uji dan tugas penerimaan | Belum tersedia; tidak menyimpulkan penghematan waktu tanpa pengukuran | Selaras pada rancangan, instrumen dan peserta masih perlu dikonfirmasi |

Ketiadaan hasil aktual merupakan keadaan wajar pada tahap proposal. Tabel tersebut tidak digunakan untuk menyatakan hasil atau kesimpulan sudah selaras, melainkan untuk menunjukkan bukti apa yang harus dihasilkan agar tujuan dapat dijawab.

## G.3 Catatan koreksi dan pelengkapan per kategori

### Temuan 1

**Kategori:** metodologi. **Prioritas:** sangat penting. **Letak:** 3.1.2, 3.4.1, dan 3.4.3.

**Teks draf:** “Pengajuan bukti transfer oleh Admin Cabang dan pemeriksaan oleh Super Admin digunakan sebagai rancangan awal pengendalian pembayaran.” Kalimat ini sengaja tidak menyatakan bahwa mitra telah menyetujui pembagian tersebut.

**Permasalahan:** akses mutasi rekening, pemilik kewenangan pemeriksaan, pembayaran tunai, dan pembayaran sebagian belum dikonfirmasi. Template 3.3 dan 3.4 mengharuskan prosedur serta konsep prototipe dapat menjadi acuan pelaksanaan.

**Langkah perbaikan:** petakan pihak penerima dana, pengaju bukti, pemeriksa, dan penerima setoran; minta pengelola meninjau alurnya; kemudian dokumentasikan keputusan. Setelah disetujui, contoh redaksi dapat berbunyi “Bukti transfer diajukan oleh Admin Cabang dan diverifikasi oleh Super Admin yang berwenang memeriksa mutasi rekening. Keputusan pemeriksaan disimpan bersama identitas petugas dan waktu tindakan.”

### Temuan 2

**Kategori:** substansi. **Prioritas:** penting. **Letak:** 3.4.2.

**Teks draf:** “Ambang hampir penuh dinyatakan sebagai parameter sisa tempat yang dapat ditetapkan pengelola.” Kapasitas penuh telah diperlakukan sebagai penolakan penambahan siswa, sesuai penjelasan pengguna.

**Permasalahan:** kapasitas setiap kelas, perbedaan ruang dan kelompok, serta nilai ambang belum tersedia sebagai daftar yang divalidasi. Template 3.4 dan 3.5 memerlukan kebutuhan serta parameter yang dapat menjadi acuan pengujian.

**Langkah perbaikan:** buat tabel cabang, ruang, jenjang, kelas, kapasitas, dan ambang; konfirmasikan kepada pengelola; kemudian gunakan nilai yang sama dalam data induk serta kasus uji. Contoh redaksi setelah angka disepakati adalah “Peringatan hampir penuh ditampilkan ketika sisa tempat memenuhi ambang yang ditetapkan pada data kelas. Penambahan peserta ditolak apabila jumlah keanggotaan aktif telah mencapai kapasitas.”

### Temuan 3

**Kategori:** metodologi dan instrumen. **Prioritas:** sangat penting. **Letak:** 3.3.8 dan hubungan dengan Bab 2.

**Teks draf:** “Instrumen UAT terdiri atas lembar tugas, pengamatan pelaksanaan, catatan masalah, dan keputusan penerimaan.” Tugas UAT disiapkan sebagai rancangan awal dan belum dianggap sebagai instrumen yang telah divalidasi.

**Permasalahan:** Bab 2 lama menempatkan kuesioner Likert sebagai pusat pengujian, sedangkan draf baru memakai tugas operasional sebagai dasar penerimaan. Rubrik proposal dan ketentuan evaluasi mitra pada panduan SI 2026 cetak 4/PDF 11 membutuhkan penjelasan evaluasi yang sesuai tujuan, bukan skor kepuasan yang dianggap membuktikan seluruh fungsi.

**Langkah perbaikan:** tetapkan peran yang diuji, jumlah dan alasan pemilihan peserta, penelaah instrumen, serta bentuk persetujuan pengguna. Sesuaikan Bab 2 dengan metode final; kuesioner persepsi dapat ditambahkan jika memang diperlukan, dengan butir, konstruk, sumber, dan analisis tersendiri.

### Temuan 4

**Kategori:** format dan spesifikasi. **Prioritas:** penting. **Letak:** 3.5.2 dan 3.5.3.

**Teks draf:** “Angka kapasitas aktual tidak dinyatakan sebelum perangkat pengembangan dan lokasi pengujian dipastikan.” Penjelasan ini mencegah spesifikasi perangkat ditulis seolah telah digunakan.

**Permasalahan:** template 3.5 meminta rincian spesifikasi teknis, sedangkan tabel saat ini baru menetapkan jenis informasi yang perlu dicatat. Draf belum dapat dinyatakan final pada bagian tersebut.

**Langkah perbaikan:** catat perangkat yang benar-benar akan dipakai, pilih pasangan versi layanan yang kompatibel, simpan berkas penguncian dependensi, dan perbarui tabel. Contoh bentuk final ialah “Pengembangan dilakukan menggunakan [perangkat dan kapasitas aktual]. Versi antarmuka, layanan, dan basis data dicatat pada Tabel 3.16.” Bagian dalam kurung siku hanya contoh pelengkapan, bukan teks siap diajukan.

### Temuan 5

**Kategori:** jadwal. **Prioritas:** penting. **Letak:** 3.3.2 dan 3.6.

**Teks draf:** “Jadwal awal disusun selama dua belas minggu relatif dengan empat iterasi pengembangan.” Alokasi tersebut merupakan usulan, bukan batas waktu yang sudah disetujui pembimbing atau mitra.

**Permasalahan:** template 3.6 meminta jadwal yang sesuai tahapan dan kondisi pelaksanaan. Jadwal relatif belum cukup untuk mengatur pertemuan pengguna atau memastikan tenggat akademik.

**Langkah perbaikan:** cocokan alokasi dengan kalender akademik, waktu tersedia, dan kesediaan mitra; ubah minggu relatif menjadi tanggal; sesuaikan jumlah tugas bila tidak muat. Rincian estimasi pertama tetap perlu ditinjau kembali setelah satu iterasi menghasilkan data waktu aktual.

### Temuan 6

**Kategori:** sitasi dan metadata. **Prioritas:** sangat penting. **Letak:** sumber Fikri, Thiovanda, serta status SINTA pada checklist.

**Teks audit lama:** atribusi “Fikri dan Arthawan (2020)” serta anggapan bahwa Prabowo pada nama berkas merupakan penulis yang salah. Pemeriksaan penerbit saat ini menunjukkan nama lengkap I Putu Deny Arthawan Sugih Prabowo dan metadata sitasi tahun 2021, dengan edisi berlabel Desember 2020.

**Permasalahan:** nama penulis dan tahun perlu konsisten menurut Panduan ITK 2025 bagian 3.7, cetak 16/PDF 24. Bukti peringkat jurnal juga tidak otomatis menetapkan cakupan akreditasi pada setiap edisi.

**Langkah perbaikan:** gunakan metadata penerbit yang dicatat pada pustaka pendamping, perbarui kemunculan pada Bab 1/2 saat penggabungan, lengkapi volume/nomor Thiovanda, serta simpan SK yang mencakup edisi jika peringkat SINTA menjadi syarat pemilihan. Status yang belum dipastikan tetap ditandai terbuka pada checklist sumber.

### Temuan 7

**Kategori:** bahasa dan tabel-gambar. **Prioritas:** penyempurnaan. **Letak:** seluruh draf dan Tabel 3.17.

**Teks draf:** naskah tersedia dalam Markdown dengan gambar PNG dan SVG. Judul, pengacuan, serta penomoran telah disediakan, tetapi format halaman Word belum diterapkan.

**Permasalahan:** ukuran huruf, margin cermin, spasi, inden, posisi caption, nomor halaman, dan pemenggalan tabel tidak dapat dipastikan dari Markdown. Acuannya adalah Panduan ITK 2025 cetak 11 sampai 16/PDF 19 sampai 24 serta template yang digunakan.

**Langkah perbaikan:** pindahkan isi ke Word, gunakan Times New Roman 12 dan ketentuan bab 14 tebal, terapkan spasi serta margin resmi, dan letakkan caption sesuai panduan. Tabel jadwal yang lebar dapat ditempatkan pada halaman lanskap dengan menjaga keterbacaan dan konsistensi nomor halaman.

## G.4 Daftar periksa wajib sebelum pengajuan

| No. | Item | Status |
| :--- | :--- | :--- |
| 1 | Anotasi ukuran huruf bawaan template dihapus | [x] |
| 2 | Bab menggunakan BAB 3 dan penomoran desimal | [x] |
| 3 | Penomoran tidak sampai tingkat keempat | [x] |
| 4 | Prosa minimal dua kalimat setiap paragraf | [x] |
| 5 | Tidak ada kalimat prosa berawal angka | [x] |
| 6 | Tidak ada dash panjang sebagai tanda baca prosa | [x] |
| 7 | Istilah asing yang digunakan dalam prosa ditandai atau dipadankan | [x] Pemeriksaan draf |
| 8 | Kata ganti orang pertama tidak digunakan dalam prosa | [x] |
| 9 | Tabel bernomor dan disebut sebelum kemunculannya | [x] |
| 10 | Gambar bernomor, tersedia, dan disebut dalam teks | [x] |
| 11 | Penempatan caption dan keterbacaan pada Word telah diperiksa | [ ] |
| 12 | Sitasi author-year langsung di dalam teks | [x] |
| 13 | Sumber di dalam teks mempunyai entri pustaka pendamping | [x] |
| 14 | Metadata tambahan dan SK edisi yang belum pasti telah dilengkapi | [ ] |
| 15 | TKT 5 ditulis sebagai target dengan rencana evaluasi mitra | [x] |
| 16 | Rencana laporan, artikel, dan HKI telah disebutkan | [x] |
| 17 | Enam subbab Bab 3 telah terisi | [x] |
| 18 | Diagram alir sesuai prosedur pada 3.3 | [x] |
| 19 | Kebutuhan fungsional/nonfungsional serta hak akses tersedia | [x] |
| 20 | Kasus uji belum diberi hasil fiktif | [x] |
| 21 | Jumlah peserta, tanggal UAT, dan validasi instrumen telah dicatat | [ ] |
| 22 | Aturan pembayaran serta ambang kelas telah disetujui mitra | [ ] |
| 23 | Versi perangkat lunak dan perangkat aktual telah dicatat | [ ] |
| 24 | Jadwal kalender telah disepakati | [ ] |
| 25 | Bab 1 dan Bab 2 telah diselaraskan dengan rancangan ini | [ ] |

## G.5 Langkah sebelum konsultasi pembimbing

1. Bawa draf Bab 3, checklist sumber, dan diagram proses pembayaran untuk membahas batas kewenangan Admin Cabang serta Super Admin.
2. Tetapkan kapasitas kelas dan ambang hampir penuh bersama mitra, tanpa mengubah aturan penolakan kelas penuh yang telah dijelaskan pengguna.
3. Tentukan perwakilan UAT serta validasi isi tugas pengujian. Rekam alasan pemilihan dan keterbatasan cakupan cabang.
4. Periksa jadwal dua belas minggu terhadap waktu yang tersedia. Ubah alokasi dan tanggal berdasarkan estimasi tugas serta kesediaan mitra.
5. Lengkapi spesifikasi aktual dan versi perangkat lunak, kemudian sesuaikan rancangan diagram apabila pilihan teknologi berubah.
6. Gabungkan pustaka pendamping melalui pengelola referensi dan perbarui metadata lintas bab. Dokumen teknis resmi melengkapi jurnal untuk konfigurasi, bukan menggantikan penelitian terdahulu.
7. Terapkan template Word dan periksa hasil PDF sebelum menyatakan naskah siap diajukan. Tidak ada hasil penelitian, kelulusan fungsi, atau skor UAT yang boleh diisi sebelum pelaksanaan.

Paket ini layak digunakan sebagai bahan konsultasi rancangan. Kesiapan seminar hasil dan sidang akhir belum dapat dinilai karena implementasi, hasil pengujian, pembahasan, dan kesimpulan belum menjadi bagian dari bahan yang tersedia.
