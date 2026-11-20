# Koreksi akademik naskah ARTHA

Tanggal pemeriksaan: 25 Oktober 2026. Penilaian ini menempatkan naskah sebagai rancangan Tugas Akhir berbentuk prototipe, sesuai template yang dipilih, bukan sebagai penelitian eksperimen yang wajib mempunyai hipotesis statistik.

## 1. Kesimpulan penilaian dan batas pemeriksaan

Topik dan kebutuhan pengembangan sistem layak dilanjutkan. Akan tetapi, naskah yang tersedia masih memerlukan revisi substansial sebelum menjadi proposal yang siap diajukan, terutama pada ketepatan bukti lapangan, pembandingan metode, kebaruan, dan rancangan evaluasi.

Salinan Bab 1 dengan revisi sitasi telah dibuat pada [BAB 1 revisi sitasi saja](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 1 - PENDAHULUAN (REVISI SITASI SAJA - BERANOTASI).md>). Seluruh redaksi di luar rentang sitasi dipertahankan persis dan naskah asal tidak diubah. Karena beberapa klaim memang tidak benar atau tidak didukung, salinan tersebut merupakan draf beranotasi, bukan naskah bersih yang seluruh pernyataannya sudah benar.

### 1.1 Berkas yang menjadi objek penilaian

| Berkas atau komponen | Cakupan pemeriksaan | Batas kesimpulan |
| :--- | :--- | :--- |
| [Bab 1 versi 11 paragraf](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md>) | Seluruh teks, subbab 1.1 sampai 1.7 | Mengandung dua belas paragraf latar belakang; nama berkas tidak sesuai jumlah aktual |
| [Bab 2](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB_2_TINJAUAN_PUSTAKA.md>) | Seluruh teks, tabel, dan diagram teks subbab 2.1 sampai 2.3 | Tidak disertai daftar pustaka lengkap pada berkas ini |
| Wawancara dan bimbingan | Pencocokan temuan melalui transkrip mentah dan lokator audit sebelumnya, terutama frontdesk, wawancara ketiga, dan Bu Ayu | Keterangan satu informan atau satu cabang tidak otomatis berlaku di seluruh cabang |
| Dokumen kebutuhan, use case, dan skema basis data | Pemeriksaan terarah atas konsistensi peran, pembayaran, WhatsApp, kapasitas, rekonsiliasi, dan cakupan fitur | Bukan audit implementasi kode maupun pengujian aplikasi |
| JURNAL | Audit isi rinci 27 penggunaan rujukan Bab 1 pada 21 sumber; penelusuran teks dan identitas korpus lokal untuk Bab 2 | Tidak semua kalimat Bab 2 memperoleh verifikasi halaman primer sedetail audit Bab 1 |
| Panduan dan template ITK | Persyaratan prototipe, struktur Bab 1, rujukan, serta aturan tata tulis | Tata letak Word/PDF akhir belum dapat dinilai dari Markdown |
| Sampul, judul resmi, abstrak, daftar isi, Bab 3 sampai penutup, daftar pustaka gabungan, dan lampiran final | Belum tersedia sebagai satu naskah skripsi lengkap dalam bahan pemeriksaan | Belum dapat dinilai; tidak dianggap sudah lengkap, salah, atau telah diuji |

Lokasi temuan memakai **baris berkas Markdown asal**, subbab, paragraf, dan nama tabel. Markdown belum mempunyai halaman cetak yang tetap, sehingga nomor halaman skripsi tidak dibuat-buat. Nomor halaman sumber PDF tetap mengikuti audit, dibedakan antara halaman cetak dan urutan halaman PDF.

### 1.2 Arti prioritas

| Prioritas | Makna |
| :--- | :--- |
| Sangat penting | Memengaruhi kebenaran klaim, integritas data, justifikasi metode, atau kemampuan menjawab rumusan masalah. Selesaikan sebelum pengajuan proposal. |
| Penting | Memengaruhi keterlacakan, kelengkapan rancangan, konsistensi ruang lingkup, dan ketepatan interpretasi. Selesaikan dalam revisi proposal. |
| Penyempurnaan | Memperbaiki keterbacaan, pemilihan istilah, dan penyajian. Lakukan setelah substansi stabil. |

## 2. Bab 1: substansi dan kesesuaian dengan bukti

### B1-01. Profil kelembagaan dan jumlah tentor

**Lokasi:** 1.1 paragraf ketiga, baris 15. **Kategori:** substansi dan sumber primer. **Prioritas:** sangat penting.

Jumlah tujuh hingga delapan tentor per cabang dan perkiraan enam puluh tentor belum memiliki dasar hitung lintas cabang yang jelas. Pernyataan “enam dari delapan cabang” juga perlu dipastikan apakah hanya berkaitan dengan layanan TK atau keseluruhan jenjang, sedangkan nama lengkap dan jabatan narasumber belum semuanya terkonfirmasi.

**Cara memperbaiki:** pertama, buat tabel cabang, jenjang layanan, jumlah tentor unik, dan tanggal data. Kedua, bedakan tentor yang mengajar di beberapa cabang agar tidak dihitung dua kali. Ketiga, minta pengelola memvalidasi identitas lembaga, alamat, tanggal berdiri, serta nama dan jabatan informan. Contoh redaksi sementara yang aman: “Bimbel Artha mengelola delapan cabang di Balikpapan. Jumlah tentor aktif pada seluruh cabang masih perlu dikonfirmasi melalui rekapitulasi pengelola.”

### B1-02. Jadwal, tarif, dan batas waktu kas terlalu digeneralisasi

**Lokasi:** 1.1 paragraf keempat, baris 17. **Kategori:** substansi dan efektivitas paragraf. **Prioritas:** penting.

Paragraf ini mencampur banyak jenjang, tarif, sesi, paket, dan batas penutupan kas. Keterangan frontdesk menunjukkan bahwa tarif dapat berbeda antar cabang, sehingga rincian dari satu cabang tidak cukup menjadi ketentuan delapan cabang.

**Cara memperbaiki:** pertama, identifikasi cabang dan tanggal berlakunya setiap tarif. Kedua, pindahkan rincian ke tabel proses bisnis atau lampiran. Ketiga, sisakan hubungan tarif, sesi, dan kebutuhan pencatatan dalam latar belakang. Contoh: “Tarif bimbingan ditentukan berdasarkan jenjang, program, dan ketentuan cabang. Variasi tersebut menjadi dasar kebutuhan pengelolaan tarif yang dapat dikonfigurasi oleh pengelola.” Jangan menyatakan semua cabang wajib menutup kas pukul 19.20 sebelum cakupannya dikonfirmasi.

### B1-03. Bukti wawancara belum ditempelkan pada fakta ARTHA

**Lokasi:** 1.1 paragraf ketiga sampai ketujuh, baris 15 sampai 23. **Kategori:** referensi dan substansi. **Prioritas:** sangat penting.

Artikel ilmiah dapat menjelaskan fungsi sistem atau kasus pembanding, tetapi tidak membuktikan bahwa kejadian yang sama berlangsung di ARTHA. Nama narasumber dalam paragraf kelima belum disertai tanggal wawancara atau rujukan lampiran yang memudahkan pembaca menelusuri keterangannya.

**Cara memperbaiki:** pertama, beri kode informan dan wawancara. Kedua, hubungkan setiap klaim empiris dengan tanggal, cabang, penanda waktu, dan lampiran transkrip yang relevan. Ketiga, gunakan format komunikasi pribadi sesuai keputusan program studi apabila memang diperlukan, tanpa menempatkan transkrip sebagai artikel jurnal. Contoh: “Berdasarkan wawancara dengan staf administrasi cabang [kode dan tanggal], pendaftaran serta pembayaran dicatat dalam buku fisik. Transkrip yang mendasari uraian tersebut disajikan pada Lampiran [nomor].” Isi bagian dalam kurung siku setelah datanya terkonfirmasi.

### B1-04. Alur kas, bukti transfer, dan mutasi bank belum dibedakan

**Lokasi:** 1.1 paragraf keenam, baris 21. **Kategori:** substansi dan analisis proses bisnis. **Prioritas:** sangat penting.

Naskah menghubungkan penyerahan uang tunai, kedatangan berkas, dan pencocokan mutasi rekening sebagai satu rangkaian yang pasti. Transkrip frontdesk membedakan setoran atau laporan harian, buku yang tetap di cabang, dan bukti transfer yang dikirim ke pusat, sehingga hubungan sebab akibat dalam kalimat saat ini belum terbukti.

**Cara memperbaiki:** pertama, gambar alur pembayaran tunai dan transfer secara terpisah. Kedua, tetapkan siapa yang membawa uang, mengirim bukti, memegang rekening, dan memvalidasi transaksi. Ketiga, hilangkan pernyataan bahwa pencocokan bank baru dapat dilakukan setelah berkas fisik tiba apabila bukti transfer dapat dikirim secara digital. Contoh: “Pencatatan penerimaan dilakukan pada cabang, sedangkan konfirmasi transfer melibatkan pengelola pusat. Keterpisahan pencatatan tersebut menjadi dasar kebutuhan penyajian informasi penerimaan yang dapat ditelusuri oleh kedua pihak.”

### B1-05. Risiko belum boleh ditulis sebagai insiden yang terbukti

**Lokasi:** 1.1 paragraf keenam dan ketujuh; 1.6 baris 83; 1.7 baris 109 sampai 113. **Kategori:** substansi. **Prioritas:** sangat penting.

Frasa “kerap terlambat diketahui” menyatakan frekuensi kejadian nyata, sedangkan transkrip frontdesk tidak mengonfirmasi konflik jadwal berulang atau kelas yang benar-benar melebihi kapasitas. Pernyataan risiko keamanan perjalanan juga memerlukan pemisahan dari insiden kehilangan atau kerugian yang sungguh terjadi.

**Cara memperbaiki:** pertama, tandai setiap klaim sebagai kejadian teramati, keterangan informan, potensi risiko, atau kebutuhan pencegahan. Kedua, jika tidak ada catatan kejadian, gunakan rumusan preventif. Contoh: “Pencatatan jadwal yang belum terintegrasi menimbulkan kebutuhan pemeriksaan penugasan lintas cabang. Fitur peringatan dirancang sebagai langkah pencegahan, bukan sebagai bukti bahwa benturan jadwal telah terjadi berulang kali.”

### B1-06. Rentang kapasitas ruang belum sesuai variasi lapangan

**Lokasi:** 1.1 paragraf ketujuh, baris 23. **Kategori:** substansi dan kebutuhan fungsional. **Prioritas:** sangat penting.

Rentang delapan hingga lima belas siswa tidak mewakili seluruh keterangan yang tersedia. Ada kelas awal SD dengan kapasitas pedagogis lebih kecil, sedangkan kapasitas fisik ruang dan jumlah siswa per kelompok bimbingan merupakan dua batas yang berbeda.

**Cara memperbaiki:** pertama, susun matriks ruang, cabang, jenjang, kapasitas fisik, dan batas pedagogis. Kedua, tentukan batas yang dipakai sistem dan pihak yang boleh memberikan pengecualian. Ketiga, pastikan bentuk peringatan atau penolakan konsisten dengan arahan mitra. Contoh: “Kapasitas kelompok belajar berbeda menurut jenjang dan ketersediaan ruang. Sistem dirancang menampilkan informasi keterisian dan peringatan berdasarkan batas yang ditetapkan pengelola.”

### B1-07. Kebaruan perlu dibatasi karena Jia Jia sudah mempunyai manajemen cabang

**Lokasi:** 1.1 paragraf kedelapan, baris 25, dua kalimat sebelum penutup paragraf. **Kategori:** substansi dan penelitian terdahulu. **Prioritas:** sangat penting.

Thiovanda tidak hanya membahas penjadwalan dan pembayaran. Halaman cetak 4, sekaligus urutan PDF 4, memuat pengelolaan cabang dan pemisahan cakupan data admin, sehingga penelitian tersebut merupakan pembanding dekat yang melemahkan klaim bahwa penelitian bimbel terdahulu hanya menangani satu cabang.

**Cara memperbaiki:** pertama, masukkan fitur cabang Jia Jia ke matriks pembanding. Kedua, periksa apakah artikel itu membahas rekonsiliasi pusat, peringatan kapasitas, atau konflik tentor dengan mekanisme yang sama. Ketiga, tulis perbedaan yang benar-benar ditemukan tanpa menyimpulkan semua penelitian di dunia belum melakukannya. Contoh: “Penelitian terdahulu telah membahas penjadwalan, pembayaran, dan pengelolaan cabang. Pengembangan pada ARTHA diarahkan pada penyesuaian alur pencatatan, kewenangan cabang, dan pemantauan penerimaan sesuai kebutuhan mitra.” Klaim tambahan tentang fitur pembeda harus didukung matriks halaman sumber.

### B1-08. Notifikasi WhatsApp Safitri tidak membuktikan seluruh klaim penagihan

**Lokasi:** 1.1 paragraf kedelapan, kalimat tentang Safitri, baris 25. **Kategori:** referensi. **Prioritas:** sangat penting.

Artikel menjelaskan notifikasi jadwal dan fitur pembayaran, tetapi tabel pengujian halaman 2350 mempunyai baris berlabel WhatsApp dengan hasil yang justru membahas logout. Karena itu, artikel tersebut belum cukup menjadi bukti implementasi dan pengujian pengingat SPP otomatis sebagaimana dinyatakan dalam Bab 1.

**Cara memperbaiki:** pertama, bedakan pembuatan tagihan otomatis, pengiriman pesan, dan konfirmasi pesan diterima. Kedua, tulis hanya fungsi yang jelas dijelaskan pada artikel. Contoh: “Safitri dkk. (2026, hlm. 2349 sampai 2350) membahas sistem administrasi dengan fitur notifikasi WhatsApp. Rincian bukti pengujian notifikasi penagihan perlu ditafsirkan secara hati-hati karena terdapat ketidaksesuaian pada tabel pengujiannya.”

### B1-09. Pembandingan metode mengandung atribusi yang salah

**Lokasi:** 1.1 paragraf kesepuluh, baris 29. **Kategori:** metodologi dan referensi. **Prioritas:** sangat penting.

Pernyataan larangan mutlak rangkap peran Scrum bertentangan dengan sumber. Pernyataan bahwa prototyping tidak menyediakan metrik yang memadai untuk sidang, XP membutuhkan mentor agar dapat dikerjakan mandiri, dan RAD tidak cocok untuk diskon atau rekap cabang tidak didukung halaman yang diaudit.

**Cara memperbaiki:** pertama, hapus penilaian “tidak dapat dipertanggungjawabkan” yang tidak memiliki dasar. Kedua, gunakan kriteria proyek yang dapat dibuktikan, yaitu pengembang tunggal, praktik pencatatan proses, kebutuhan pengujian, dan pola umpan balik mitra. Ketiga, jelaskan kecocokan PxP tanpa menyesatkan deskripsi metode lain. Contoh: “PxP dipilih karena menyediakan praktik pengembangan individual yang mencakup pengujian berkelanjutan dan evaluasi proses. Praktik tersebut digunakan untuk mendokumentasikan perkembangan prototipe melalui pencatatan waktu dan galat.” Lengkapi sitasi primer dan rincian implementasinya pada metode.

### B1-10. Waterfall disederhanakan sebagai proses tanpa umpan balik

**Lokasi:** 1.1 paragraf kesepuluh, baris 29. **Kategori:** metodologi. **Prioritas:** penting.

Waterfall memang menekankan tahapan yang terencana, tetapi naskah menyatakan perubahan kebutuhan pada dasarnya tidak dapat ditampung. Pressman halaman cetak 39, urutan PDF 68, menjelaskan persoalan urutan murni dan mencatat umpan balik pada pembahasan model tersebut.

**Cara memperbaiki:** pertama, jelaskan keterbatasan relatif, bukan larangan absolut. Kedua, tunjukkan mengapa pengelolaan perubahan pada proyek ini membutuhkan iterasi yang dipilih. Contoh: “Pendekatan yang lebih terencana memerlukan pengelolaan perubahan apabila kebutuhan direvisi setelah perancangan. Pada penelitian ini, pengembangan bertahap dipilih untuk memfasilitasi evaluasi modul bersama mitra.”

### B1-11. Ketersediaan mitra setiap akhir iterasi belum menjadi fakta terkonfirmasi

**Lokasi:** 1.1 paragraf kesepuluh dan kesebelas, baris 29 sampai 31. **Kategori:** metodologi dan kelayakan pelaksanaan. **Prioritas:** sangat penting.

Keterangan bahwa mitra tidak dapat mendampingi setiap hari dan telah berkomitmen mengevaluasi setiap iterasi belum cukup dibuktikan oleh adanya wawancara awal. Komitmen evaluasi merupakan syarat operasional rencana penelitian dan perlu dinyatakan sebagai rencana sampai ada kesepakatan.

**Cara memperbaiki:** pertama, tentukan penanggung jawab mitra. Kedua, sepakati jadwal, bentuk demonstrasi, dan mekanisme masukan apabila informan berhalangan. Ketiga, catat persetujuan pada notulen atau lembar kesediaan. Contoh: “Evaluasi modul direncanakan bersama perwakilan mitra pada akhir iterasi. Waktu pelaksanaannya disesuaikan dengan kesepakatan yang dicatat dalam jadwal penelitian.”

### B1-12. Batasan ruang lingkup tidak konsisten antarberkas

**Lokasi:** 1.4 baris 61 sampai 65; Bab 2 subbab 2.1.7 dan Gambar 2.2; dokumen kebutuhan. **Kategori:** substansi dan format rancangan. **Prioritas:** sangat penting.

Bab 1 berfokus pada dasbor internal, sedangkan Bab 2 memasukkan landing page promosi publik. Pengingat melalui tautan WhatsApp dalam Bab 1 berbeda dari pengiriman otomatis terjadwal pada dokumen kebutuhan dan use case.

**Cara memperbaiki:** pertama, buat satu tabel ruang lingkup yang disepakati. Kedua, tentukan status landing page sebagai luaran utama, pelengkap, atau di luar lingkup evaluasi. Ketiga, pilih mekanisme WhatsApp yang benar-benar akan dibangun dan samakan seluruh bab, diagram, serta skenario pengujian. Contoh untuk opsi tautan: “Sistem menyiapkan pesan melalui tautan WhatsApp. Pengiriman pesan dilakukan oleh staf setelah memeriksa penerima dan isi pesan.” Jangan memakai contoh ini jika keputusan akhirnya adalah gateway otomatis.

### B1-13. Bukti transfer belum cukup untuk memastikan penerimaan bank

**Lokasi:** 1.4 butir ketiga, baris 63; tujuan kedua, baris 52. **Kategori:** metodologi dan rancangan pengendalian. **Prioritas:** sangat penting.

Mengunggah gambar bukti transfer belum membuktikan bahwa dana telah diterima pada rekening resmi. Rekonsiliasi juga berbeda dari sekadar mengubah status tagihan menjadi lunas atau menyetujui jumlah penerimaan cabang.

**Cara memperbaiki:** pertama, tetapkan siapa yang mempunyai akses mutasi rekening. Kedua, bedakan status menunggu pemeriksaan, terkonfirmasi, ditolak, dan perlu klarifikasi sesuai kebutuhan nyata. Ketiga, catat nomor referensi atau identitas pencocokan serta jejak perubahan. Contoh: “Bukti transfer digunakan sebagai dokumen pendukung pemeriksaan. Konfirmasi penerimaan dilakukan oleh petugas berwenang setelah dicocokkan dengan mutasi rekening resmi.” Kewenangan Admin Cabang atau Super Admin masih harus disepakati bersama mitra.

### B1-14. Operasional delapan cabang berbeda dari pengujian prototipe

**Lokasi:** 1.2 butir pertama, 1.3 butir pertama, dan 1.4 butir kelima, baris 41, 51, 65. **Kategori:** metodologi. **Prioritas:** penting.

Rancangan yang mendukung delapan cabang tidak otomatis berarti penerapan produksi wajib dilakukan serentak pada semuanya. Frasa “tanggal penerapan resmi” belum sesuai apabila penelitian hanya sampai uji prototipe dan belum mempunyai kesepakatan operasional produksi.

**Cara memperbaiki:** pertama, bedakan dukungan struktur delapan cabang, data uji, uji pengguna, dan penerapan produksi. Kedua, tentukan cabang yang menjadi lokasi uji dengan alasan pemilihannya. Contoh: “Struktur data dirancang untuk mendukung delapan cabang. Evaluasi prototipe dilakukan pada lingkungan dan perwakilan pengguna yang ditentukan dalam rancangan pengujian.” Jelaskan pula data awal yang diperlukan walaupun transaksi historis tidak dimigrasikan.

### B1-15. Manfaat dan potensi komersial melampaui bukti yang tersedia

**Lokasi:** 1.5 baris 73 sampai 77 dan 1.6 baris 83 sampai 85. **Kategori:** substansi dan bahasa akademik. **Prioritas:** penting.

Manfaat dapat ditulis sebagai harapan, tetapi “mempercepat”, “tanpa harus menunggu”, dan permintaan pasar “cukup tinggi” mengesankan hasil terukur atau bukti pasar. Klaim SaaS juga menambahkan kebutuhan teknis dan model bisnis yang belum menjadi lingkup prototipe.

**Cara memperbaiki:** pertama, ubah klaim hasil menjadi target yang akan diuji. Kedua, hapus angka atau penilaian pasar yang tidak didukung survei. Ketiga, tempatkan SaaS sebagai kemungkinan pengembangan lanjutan. Contoh: “Prototipe diharapkan membantu penelusuran pembayaran dan penyusunan rekap cabang. Besarnya penghematan waktu belum dapat ditentukan sebelum dilakukan pengukuran pada tugas yang sebanding.”

### B1-16. Kerangka tugas akhir belum menunjukkan tahapan pengembangan

**Lokasi:** 1.7, baris 89 sampai akhir Bab 1. **Kategori:** metodologi dan struktur. **Prioritas:** penting.

Fishbone membantu merangkum dugaan penyebab, tetapi tidak menggambarkan alur lengkap dari penggalian kebutuhan sampai evaluasi prototipe. Beberapa cabang sebab dalam uraian juga mencampur fakta, risiko, dan ketiadaan fitur solusi.

**Cara memperbaiki:** pertama, cocokkan setiap sebab dengan bukti wawancara. Kedua, tambahkan bagan tahapan pengembangan sesuai template, meliputi pengumpulan kebutuhan, perencanaan, iterasi PxP, pengujian pengguna, dan pelaporan. Ketiga, beri sumber “analisis peneliti berdasarkan wawancara [kode]” apabila diagram memang hasil sintesis sendiri. Contoh pengantar: “Kerangka tugas akhir menggambarkan hubungan kebutuhan mitra, tahapan pengembangan, dan evaluasi prototipe. Diagram sebab akibat digunakan untuk merangkum masalah awal, sedangkan alur pengembangan disajikan secara terpisah.”

## 3. Bab 1: bahasa dan penempatan sitasi

### B1-17. Kalimat pengantar dan kalimat manfaat belum efektif

**Lokasi:** pengantar bab baris 5; 1.5 baris 73 dan 77; 1.7 baris 99. **Kategori:** bahasa. **Prioritas:** penting.

Pengantar bab dan manfaat bagi peneliti masing-masing hanya satu kalimat, sehingga belum mengikuti aturan paragraf pada AGENTS.md. Kalimat “Manajemen pusat untuk memantau ...” kehilangan predikat utama, sedangkan “Pada Gambar 1.1 merupakan ...” memakai konstruksi yang tidak lengkap.

**Cara memperbaiki:** pertama, lengkapi subjek dan predikat. Kedua, pisahkan pengantar yang terlalu padat menjadi dua kalimat. Contoh manfaat: “Prototipe menyediakan rekap operasional bagi manajemen pusat. Rekap tersebut diharapkan membantu pemantauan siswa dan penerimaan setiap cabang.” Contoh diagram: “Gambar 1.1 menyajikan kerangka identifikasi masalah operasional ARTHA. Diagram tersebut mengelompokkan faktor yang ditemukan dalam wawancara.”

### B1-18. Kesalahan tanda baca dan konsistensi istilah

**Lokasi:** 1.1 paragraf kesepuluh baris 29; caption Gambar 1.1; seluruh Bab 1. **Kategori:** bahasa dan format. **Prioritas:** penting.

Teks “Beberapa metode alternatif seperti,.” merupakan kalimat rusak yang harus dihapus atau dilengkapi. Bentuk “Gambar 1. 1”, dashboard/dasbor, multicabang/multi-cabang, real-time/waktu nyata, serta tentor/pengajar perlu diseragamkan sesuai pilihan istilah dalam naskah.

**Cara memperbaiki:** pertama, buat daftar istilah baku penelitian. Kedua, gunakan “dasbor”, “multicabang”, dan “waktu nyata” secara konsisten jika memilih padanan Indonesia. Ketiga, cetak miring istilah asing yang belum memiliki padanan menurut ketentuan kampus. Contoh: “Beberapa metode pengembangan dibandingkan berdasarkan ukuran tim, pengelolaan perubahan, dan dokumentasi proses. Hasil pembandingan digunakan untuk menjelaskan pemilihan PxP.”

### B1-19. Sitasi di ujung paragraf tidak boleh menanggung semua klaim

**Lokasi:** 1.1 paragraf pertama dan kedua, baris 11 sampai 13. **Kategori:** referensi. **Prioritas:** sangat penting.

Tiana tidak menjadi sumber Undang-Undang Sistem Pendidikan Nasional, dan Pradana tidak memuat definisi sistem informasi sebagaimana ditulis pada naskah. Menambahkan nomor halaman pada sitasi yang tidak sesuai tidak memperbaiki kecocokan isi.

**Cara memperbaiki:** pertama, pisahkan klaim hukum, definisi, dan temuan studi kasus. Kedua, tempatkan sitasi tepat setelah kalimat yang memang didukung. Ketiga, gunakan sumber definisi yang benar-benar tersedia dan telah dibaca, atau ubah definisi menjadi uraian fungsi yang didukung sumber. Contoh untuk Pradana: “Pradana (2024, hlm. 6858) membahas pemanfaatan sistem informasi dalam pengelolaan data siswa dan keuangan sekolah. Pembahasan tersebut menjadi acuan fungsi administrasi, bukan sumber definisi umum sistem informasi.” Untuk peraturan, tambahkan rujukan hukum primer tersendiri setelah verifikasi dokumen resmi.

## 4. Bab 2: metodologi dan landasan teori

### B2-01. Tabel perbandingan metode belum objektif

**Lokasi:** 2.1.1, Tabel 2.1, baris 20 sampai 36. **Kategori:** metodologi. **Prioritas:** sangat penting.

Istilah “cacat metodologis”, “tidak layak”, dan “sangat tepat dan sahih” mendahului pembuktian. Beberapa karakteristik berasal dari penerapan tertentu tetapi ditulis sebagai aturan universal metode, sehingga tabel lebih menyerupai pembenaran pilihan daripada analisis komparatif.

**Cara memperbaiki:** pertama, gunakan kriteria yang sama untuk semua metode. Kedua, pisahkan karakteristik menurut sumber dari penilaian kesesuaian proyek. Ketiga, beri halaman rujukan per karakteristik dan bukti proyek untuk setiap penilaian. Contoh kolom penilaian: “Memerlukan penyesuaian pada pelaksanaan oleh pengembang tunggal. Penyesuaian tersebut perlu dijelaskan apabila metode ini dipilih.” Pada PxP, tulis juga biaya disiplin pencatatan dan risiko tidak konsistennya praktik individual.

### B2-02. Karakteristik Scrum tidak sesuai panduan yang dikutip

**Lokasi:** 2.1.1, Tabel 2.1 dan paragraf setelahnya, baris 23 sampai 34. **Kategori:** metodologi dan referensi. **Prioritas:** sangat penting.

Naskah menyebut tiga sampai sembilan anggota, larangan rangkap peran, Sprint Backlog yang tidak boleh berubah, serta Burndown Chart sebagai artefak wajib. Scrum Guide 2020 menjelaskan tim biasanya beranggotakan sepuluh orang atau kurang, tiga artefak utama berupa Product Backlog, Sprint Backlog, dan Increment, serta pembaruan rencana sesuai pembelajaran dengan tetap menjaga Sprint Goal.

**Cara memperbaiki:** pertama, gunakan satu versi panduan yang konsisten. Kedua, koreksi keempat butir tersebut dan hilangkan kesimpulan tentang ketidakabsahan akademik berdasarkan larangan rangkap peran. Ketiga, jelaskan bahwa kebolehan PO atau SM berpartisipasi sebagai Developers tidak otomatis membuktikan semua akuntabilitas dapat dipenuhi satu orang. Contoh: “Scrum menempatkan pengelolaan produk dan proses dalam sejumlah akuntabilitas tim. Penelitian ini memilih PxP karena praktiknya secara eksplisit diarahkan kepada pengembang individual.” Sumber pembanding resmi: [Scrum Guide 2020](https://scrumguides.org/scrum-guide.html); lokator lokal peran berada pada cetak 5/PDF 6 dan Daily Scrum pada cetak 9/PDF 10.

### B2-03. Asal usul PxP dan jumlah prinsip perlu dikoreksi

**Lokasi:** 2.1.2, baris 40 sampai 49. **Kategori:** teori dan referensi. **Prioritas:** penting.

Urutan publikasi Agarwal 2008 lalu Dzhurov 2009 tidak dengan sendirinya membuktikan hubungan penyempurnaan langsung. Artikel Dzhurov menjelaskan pelonggaran PSP dengan praktik XP dan mencantumkan enam prinsip, sementara naskah menyebut lima serta menghilangkan perbaikan cacat sejak awal.

**Cara memperbaiki:** pertama, pisahkan dua publikasi sebagai kajian terkait sampai hubungan sejarahnya benar-benar dibuktikan. Kedua, ikuti enam prinsip pada halaman cetak 253/PDF 2, atau nyatakan dengan jelas apabila daftar merupakan ringkasan penulis. Contoh: “Dzhurov dkk. (2009, hlm. 253 sampai 254) mengembangkan PxP dengan menyederhanakan praktik PSP dan mengadopsi sejumlah praktik XP. Prinsipnya mencakup disiplin individual, pencatatan pekerjaan, evaluasi kinerja, pengujian berkelanjutan, perbaikan cacat sejak awal, dan otomatisasi.”

### B2-04. Fibonacci bukan ketentuan asli PxP pada sumber Dzhurov

**Lokasi:** 2.1.2.2 baris 115; 2.1.4 baris 157 sampai 159; Gambar 2.1. **Kategori:** metodologi dan referensi. **Prioritas:** sangat penting.

Sumber primer menjelaskan estimasi tugas berdasarkan kategori dan data proyek sebelumnya, atau perkiraan terbaik ketika data historis belum tersedia. Halaman cetak 254 sampai 255/PDF 3 sampai 4 tidak menetapkan Fibonacci sebagai kewajiban PxP, sehingga atribusi saat ini tidak tepat.

**Cara memperbaiki:** pertama, pilih cara estimasi yang realistis bagi proyek pertama. Kedua, pisahkan estimasi durasi dari story point sebagai satuan usaha relatif. Ketiga, jika Fibonacci dipakai, nyatakan sebagai adaptasi penelitian dan berikan sumber yang benar-benar membahas praktik tersebut. Contoh: “Estimasi awal disusun berdasarkan rincian tugas dan perkiraan waktu pengerjaan. Setelah iterasi pertama, data waktu aktual digunakan untuk memperbaiki estimasi berikutnya.” Jangan mengonversi satu story point menjadi jumlah jam tetap tanpa dasar kalibrasi.

### B2-05. Diagram dan uraian PxP perlu membedakan teori dengan adaptasi proyek

**Lokasi:** Gambar 2.1; 2.1.2.3 sampai 2.1.2.7, baris 117 sampai 135. **Kategori:** metodologi dan format. **Prioritas:** penting.

Persiapan repositori, Next.js, Laravel, dan bentuk dokumentasi UML merupakan pilihan implementasi penelitian ini, bukan seluruhnya tahapan wajib dari sumber primer. Kata “melarang” dokumentasi berlebihan juga lebih keras daripada anjuran memakai alat sederhana pada sumber.

**Cara memperbaiki:** pertama, tampilkan alur asli beserta halaman sumber. Kedua, buat tabel adaptasi berisi aktivitas proyek, luaran, dan kriteria selesai setiap tahap. Ketiga, ganti jaminan “meningkat secara berkelanjutan” menjadi tujuan yang harus dibuktikan data log. Contoh: “Desain disusun secukupnya untuk mendukung modul pada iterasi berjalan. Pemodelan use case dan basis data digunakan sebagai bentuk adaptasi sesuai kebutuhan prototipe.”

### B2-06. TDD perlu mempunyai bukti pelaksanaan yang terpisah dari pengujian sistem

**Lokasi:** 2.1.2.5 dan 2.1.12, baris 125 sampai 127 dan 287 sampai 304. **Kategori:** metodologi. **Prioritas:** sangat penting.

Pernyataan menerapkan TDD belum dapat dibuktikan hanya dengan tabel Black Box Testing yang dibuat setelah sistem selesai. Pengujian unit sebelum kode, perubahan kode, refaktorisasi, dan hasil regresi merupakan bukti proses yang berbeda dari evaluasi alur pengguna.

**Cara memperbaiki:** pertama, tentukan aturan bisnis yang diuji secara otomatis, misalnya perhitungan tagihan dan deteksi irisan jadwal. Kedua, simpan bukti tes gagal sebelum implementasi dan tes lulus sesudahnya beserta riwayat perubahan. Ketiga, kaitkan galat dengan modul dan perbaikannya. Contoh: “Pengujian unit digunakan untuk memeriksa aturan bisnis pada tahap implementasi. Pengujian sistem dan UAT digunakan untuk memeriksa alur terintegrasi serta penerimaan pengguna.”

### B2-07. User story dan kriteria penerimaan belum cukup terukur

**Lokasi:** 2.1.3, Tabel 2.2, baris 147 sampai 151. **Kategori:** metodologi dan rancangan instrumen. **Prioritas:** penting.

Kata “permanen”, “tanpa risiko salah hitung”, dan “akurat” tidak menetapkan kondisi uji yang terbatas. Beberapa butir mengikat kebutuhan pengguna langsung pada pilihan basis data, padahal kriteria penerimaan seharusnya menekankan perilaku yang dapat diamati.

**Cara memperbaiki:** pertama, pisahkan nilai manfaat dari jaminan mutlak. Kedua, tentukan data masukan, kondisi, dan keluaran untuk setiap story. Ketiga, sertakan pengujian akses cabang lain dan contoh perhitungan konkret. Contoh: “Ketika Admin Cabang A menyimpan siswa dengan data wajib lengkap, sistem menampilkan siswa pada daftar Cabang A. Permintaan akun Cabang A untuk membaca data Cabang B ditolak oleh peladen.” Atribusi Three C's dan format user story juga perlu diperiksa langsung sebelum tetap disandarkan pada Beck dan Andres.

### B2-08. Uraian UML dan ERD terlalu menjamin hasil implementasi

**Lokasi:** 2.1.5 sampai 2.1.6, Tabel 2.3 sampai 2.4, baris 161 sampai 199. **Kategori:** teori dan pemodelan. **Prioritas:** penting.

Pembuatan ERD tidak otomatis membuktikan normalisasi 3NF, konsistensi seluruh transaksi, atau efisiensi kueri. Relasi extend juga harus dijelaskan melalui use case tambahan yang memperluas use case dasar pada kondisi tertentu, bukan dengan menyatakan target selalu merupakan fungsi opsional yang dieksekusi.

**Cara memperbaiki:** pertama, pilih notasi ERD yang konsisten antara tabel simbol dan diagram aktual. Kedua, tampilkan ketergantungan fungsional dan alasan pemisahan tabel jika menyatakan 3NF. Ketiga, periksa arah relasi include, extend, dan generalisasi pada diagram dengan sumber pemodelan yang tersedia. Contoh: “ERD digunakan untuk merancang hubungan antarentitas. Pemenuhan normalisasi diperiksa melalui ketergantungan atribut, sedangkan integritas transaksi diuji pada implementasi basis data.” Sumber Kurniawan, Connolly, dan Antar belum dapat dikonfirmasi dari berkas yang ditemukan, sehingga jangan menyatakan telah diaudit halaman per halaman.

## 5. Bab 2: teknologi, pengujian, dan analisis data

### B2-09. Teknologi terpilih bukan bukti otomatis kecepatan dan kebaruan

**Lokasi:** 2.1.7 sampai 2.1.11, baris 201 sampai 285; 2.2 butir ketiga, baris 351 sampai 352. **Kategori:** teori dan analisis. **Prioritas:** sangat penting.

Next.js, pemisahan frontend dan backend, ORM, atau InnoDB tidak otomatis membuat semua sistem lebih cepat, lebih aman, serta lebih mudah dirawat oleh pengembang tunggal. Klaim ukuran CSS kurang dari lima puluh kilobita dan penurunan FCP belum disertai konfigurasi serta pengukuran aplikasi yang dibangun.

**Cara memperbaiki:** pertama, uraikan fungsi teknologi secara netral dan cantumkan versinya. Kedua, pisahkan manfaat potensial dari hasil yang harus diuji. Ketiga, hapus perbandingan monolitik yang merendahkan tanpa pengukuran setara. Contoh: “Pemisahan antarmuka dan layanan API digunakan untuk mengatur pembagian tanggung jawab aplikasi. Dampaknya terhadap kinerja dan kemudahan pemeliharaan bergantung pada implementasi dan tidak diuji sebagai perbandingan arsitektur dalam penelitian ini.”

### B2-10. Uraian Server Components dan REST perlu lebih tepat

**Lokasi:** 2.1.7 baris 203; 2.1.9 baris 215. **Kategori:** teori dan referensi. **Prioritas:** penting.

Server Components tidak cukup dijelaskan sebagai pengiriman HTML murni, karena dokumentasi Next.js juga menjelaskan RSC Payload serta hidrasi Client Components. REST merupakan gaya arsitektur, sedangkan pemakaian JSON dan metode HTTP saja belum membuktikan seluruh batasan REST dipenuhi.

**Cara memperbaiki:** pertama, ringkas konsep yang benar-benar dipakai. Kedua, hindari menambahkan istilah SEO sebagai alasan utama dasbor privat tanpa kaitan kebutuhan. Ketiga, jelaskan kontrak API, otorisasi, dan penanganan galat pada rancangan implementasi. Contoh: “Next.js digunakan untuk menyusun antarmuka pengguna. Komponen peladen dan komponen klien dipilih sesuai kebutuhan penyajian data serta interaksi halaman.” Acuan koreksi: [dokumentasi Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), diperiksa 25 Oktober 2026.

### B2-11. Sanctum tidak selalu berarti bearer token yang disimpan di peramban

**Lokasi:** 2.1.9, baris 217 dan Gambar 2.2. **Kategori:** rancangan keamanan dan referensi. **Prioritas:** sangat penting.

Dokumentasi Sanctum membedakan autentikasi SPA menggunakan cookie sesi dan autentikasi API token. Token juga tidak otomatis memiliki masa kedaluwarsa tertentu pada konfigurasi bawaan, sehingga penjelasan saat ini menetapkan pilihan yang belum dijustifikasi.

**Cara memperbaiki:** pertama, tetapkan domain, jenis klien, dan mekanisme autentikasi yang digunakan. Kedua, pilih mode yang sesuai serta jelaskan sesi, CSRF, pencabutan akses, dan masa berlaku bila memakai token. Ketiga, sesuaikan diagram serta pengujian login dan logout. Contoh: “Mekanisme autentikasi dipilih berdasarkan konfigurasi hubungan antarmuka dan API. Implementasinya mengikuti mode Sanctum yang digunakan dan diuji melalui skenario akses sah, sesi berakhir, serta penolakan akses lintas cabang.” Acuan: [Laravel Sanctum, SPA Authentication dan Token Expiration](https://laravel.com/framework/docs/12.x/sanctum), diperiksa 25 Oktober 2026. Rujukan web ini untuk koreksi teknis, belum dimasukkan ke salinan Bab 1 yang dibatasi pada sumber JURNAL.

### B2-12. Kata sandi, pengujian kotak hitam, dan keamanan dicampur

**Lokasi:** 2.1.12, baris 291; skema basis data baris 360. **Kategori:** metodologi dan istilah. **Prioritas:** penting.

Bcrypt adalah hashing kata sandi, bukan enkripsi yang dirancang untuk dikembalikan ke nilai asli. Pengujian login dari antarmuka tidak cukup membuktikan algoritma penyimpanan kata sandi, sedangkan keberadaan Laravel tidak otomatis menghilangkan XSS, SQL injection, atau salah otorisasi.

**Cara memperbaiki:** pertama, gunakan istilah hashing. Kedua, pisahkan pengujian perilaku login, pemeriksaan konfigurasi penyimpanan, dan pengujian hak akses. Ketiga, pilih klaim keamanan yang benar-benar diperiksa. Contoh: “Pengujian kotak hitam memeriksa penerimaan dan penolakan kredensial. Pemeriksaan penyimpanan kata sandi dilakukan secara terpisah melalui konfigurasi dan implementasi hashing.” Acuan istilah: [Laravel Hashing](https://laravel.com/framework/docs/12.x/hashing).

### B2-13. Tabel contoh pengujian tidak boleh menyerupai hasil aktual

**Lokasi:** 2.1.12, Tabel 2.5, baris 297 sampai 302. **Kategori:** integritas data dan analisis. **Prioritas:** sangat penting.

Tabel diberi pengantar sebagai contoh format, tetapi kolom pengamatan sudah berisi keberhasilan dan semua status ditulis “Valid”. Tanpa bukti pelaksanaan, pembaca dapat salah memahami contoh tersebut sebagai hasil penelitian yang sudah terjadi.

**Cara memperbaiki:** pertama, beri judul tegas “Rancangan kasus uji”. Kedua, kosongkan hasil aktual dan tulis “belum dilaksanakan” pada status. Ketiga, pindahkan hasil nyata ke bab hasil setelah tersedia tanggal, versi aplikasi, penguji, data uji, dan bukti eksekusi. Contoh baris: “Masukan: kredensial salah; keluaran yang diharapkan: akses ditolak; hasil aktual: belum diisi; status: belum diuji.” Jika hasil sebenarnya sudah tersedia, lampirkan buktinya dan jangan lagi menyebut tabel sebagai contoh.

### B2-14. Equivalence Partitioning dan Boundary Value Analysis belum diwujudkan

**Lokasi:** 2.1.12, baris 291 dan Tabel 2.5. **Kategori:** metodologi. **Prioritas:** sangat penting.

Menyebut kedua teknik tidak cukup apabila tabel hanya berisi contoh normal. Tidak terlihat kelas masukan sah/tidak sah serta nilai di bawah, tepat pada, dan di atas batas yang berasal dari ketentuan kebutuhan.

**Cara memperbaiki:** pertama, tentukan batas dari aturan yang telah disepakati, bukan angka buatan. Kedua, uji kapasitas pada C dikurangi satu, C, dan C ditambah satu; uji nominal nol, kurang bayar, tepat bayar, dan pembayaran berlebih sesuai kebijakan. Ketiga, tambahkan jadwal beririsan, jadwal tepat bersambung, tentor lintas cabang, serta pendaftaran serentak pada slot terakhir. Contoh: “Untuk batas kapasitas C, keluaran setiap kasus mengikuti kebijakan peringatan atau penolakan yang disepakati. Nilai C dan kebijakan tersebut dicantumkan pada spesifikasi kebutuhan.”

### B2-15. Pembayaran transfer tidak sama dengan penambahan kas tunai cabang

**Lokasi:** Tabel 2.5 BB-05, baris 301. **Kategori:** analisis proses dan data keuangan. **Prioritas:** sangat penting.

Skenario menyatakan bukti transfer membuat saldo kas cabang bertambah, padahal penerima dana mungkin rekening pusat. Penyamaan tagihan, penerimaan siswa, kas tunai cabang, transfer masuk, dan setoran cabang berpotensi menggandakan hitungan pendapatan.

**Cara memperbaiki:** pertama, tetapkan objek pencatatan pada setiap tahap. Kedua, identifikasi rekening penerima dan siapa pemilik pencatatannya. Ketiga, buat contoh transaksi tunggal dari pembayaran hingga pencocokan bank dan pastikan hanya dihitung satu kali sebagai penerimaan. Contoh: “Pembayaran transfer yang terkonfirmasi memperbarui status penerimaan siswa. Transaksi tersebut dicatat pada kanal transfer dan tidak otomatis menambah saldo kas tunai cabang.”

### B2-16. UAT bukan sekadar kuesioner kepuasan

**Lokasi:** 2.1.13, baris 308 sampai 324. **Kategori:** metodologi dan instrumen. **Prioritas:** sangat penting.

Penerimaan tugas operasional perlu diuji melalui penggunaan nyata atau simulasi tugas yang relevan. Skor persetujuan tidak sendirinya membuktikan akurasi rekening, kesesuaian semua fungsi, atau peningkatan efisiensi.

**Cara memperbaiki:** pertama, susun tugas UAT per peran dan kriteria penerimaannya. Kedua, catat keberhasilan tugas, masalah yang ditemukan, keputusan menerima/menolak, serta perbaikan. Ketiga, gunakan kuesioner hanya untuk konstruk yang memang ingin diukur, misalnya kejelasan tampilan. Contoh: “UAT mengevaluasi kesesuaian alur pendaftaran, pencatatan pembayaran, dan pemantauan cabang. Penilaian persepsi pengguna digunakan sebagai informasi pendukung keputusan penerimaan prototipe.”

### B2-17. Rumus dan kategori Likert belum konsisten

**Lokasi:** Tabel 2.6 dan pengantar UAT, baris 310 sampai 324. **Kategori:** analisis data. **Prioritas:** sangat penting.

Naskah merujuk formula tetapi belum menuliskan rumusnya. Jika skor dihitung sebagai jumlah skor dibagi skor maksimum, skala satu sampai lima memiliki indeks minimum dua puluh persen untuk jawaban lengkap, sehingga rentang nol sampai 19,99 persen tidak mungkin tercapai; label “Ragu-ragu / Cukup Setuju” juga mencampur dua makna respons.

**Cara memperbaiki:** pertama, pilih satu label netral yang konsisten. Kedua, tulis rumus, unit analisis, jumlah butir, jumlah responden, perlakuan data kosong, dan sumber kategori. Ketiga, jangan menafsirkan skor tinggi sebagai “diterima tanpa catatan” apabila fungsi kritis gagal. Contoh formula deskriptif yang dapat dipertimbangkan: “Indeks skor = jumlah skor jawaban valid dibagi skor maksimum jawaban valid, dikalikan seratus persen.” Laporkan keterbatasan rentang minimum dan jangan menggunakannya sebagai persentase peningkatan kinerja. Bila menggunakan transformasi ke skala nol sampai seratus, jelaskan rumus berbeda dan alasan pemilihannya.

### B2-18. Klaim peningkatan efisiensi membutuhkan desain pengukuran tersendiri

**Lokasi:** penutup 2.1.13, baris 324; manfaat Bab 1. **Kategori:** analisis data dan kesimpulan. **Prioritas:** sangat penting.

Black Box Testing dan UAT memadai untuk menilai fungsi serta penerimaan sesuai rancangan, tetapi tidak otomatis membuktikan penghematan waktu atau dampak kausal. Pernyataan “memberikan kepastian” bahwa efisiensi meningkat melampaui data yang direncanakan.

**Cara memperbaiki:** pertama, pilih apakah efisiensi merupakan tujuan yang sungguh diukur. Kedua, bila iya, tetapkan tugas setara, ukuran waktu dan kesalahan, kondisi pelaksanaan, pengulangan, serta keterbatasan pembanding. Ketiga, bila tidak, batasi kesimpulan pada kesesuaian fungsional dan penerimaan. Contoh: “Evaluasi memberikan informasi mengenai kesesuaian fungsi dan penerimaan pengguna pada skenario yang diuji. Dampak terhadap penghematan waktu operasional belum disimpulkan apabila tidak dilakukan pengukuran khusus.”

## 6. Bab 2: penelitian terdahulu, referensi, dan teori pendukung

### B2-19. Identitas sumber belum seluruhnya sesuai berkas primer

**Lokasi:** 2.1.1, 2.1.2, Tabel 2.7. **Kategori:** referensi. **Prioritas:** sangat penting.

Nama berkas tidak selalu mencerminkan identitas artikel. Kesalahan nama penulis, tahun, dan nama jurnal merusak keterlacakan walaupun isi artikelnya relevan.

| Atribusi dalam naskah atau nama berkas | Temuan pada sumber lokal | Tindakan |
| :--- | :--- | :--- |
| Kuhrmann dkk. (2021), 2.1.1 baris 16 | Halaman pertama berkas berjudul Adoption and Suitability menyebut Licorish dkk. (2016), APSEC, hlm. 369 sampai 372, DOI 10.1109/APSEC.2016.062 | Ubah berdasarkan artikel yang benar-benar dipakai; jangan mempertahankan Kuhrmann berdasarkan nama berkas |
| Fikri & Prabowo (2020), berulang pada Bab 2 | PDF buku tamu DPOP menyebut Ahmad Maulana Fikri dan I Putu Deny Arthawan S. P. | Samakan atribusi dengan identitas penulis pada artikel dan metadata penerbit, bukan nama berkas |
| Kismantoro & Ibadi (2026), nama jurnal Tabel 2.7 | PDF menyebut JATI (Jurnal Mahasiswa Teknik Informatika), volume 10 nomor 2, mulai hlm. 3195 | Koreksi nama jurnal, lalu periksa kembali seluruh metadata dan tahun akreditasinya |
| Berkas Scrum2Kanban bernama Mahnic (2018) | Halaman pertama menyebut Christoph Matthies (2018), DOI 10.1145/3194779.3194784 | Jika digunakan kelak, kutip Matthies; belum ditemukan sebagai sitasi eksplisit dalam Bab 2 ini |
| Ramadhan (2026), JISBT pada Tabel 2.7 | Sumber yang dimaksud tidak ditemukan dalam kumpulan PDF yang diperiksa; Ramadhan dan Widodo membahas akuntansi pusat dan cabang, bukan PxP keanggotaan | Jangan menggantinya dengan artikel Ramadhan dan Widodo hanya karena nama/tahun serupa |

**Cara memperbaiki:** pertama, impor metadata dari sumber primer ke pengelola referensi. Kedua, cocokkan penulis, judul, tahun, jurnal, volume, nomor, halaman, dan DOI. Ketiga, perbarui semua kemunculan sitasi secara serentak. Contoh atribusi yang sudah dapat diperbaiki: “Fikri dan Arthawan (2020) menerapkan PxP pada sistem informasi buku tamu.”

### B2-20. Sejumlah teori memakai sumber yang belum tersedia untuk diperiksa

**Lokasi:** 2.1.2 sampai 2.1.13 dan 2.3. **Kategori:** referensi. **Prioritas:** sangat penting.

Sumber seperti Connolly dan Begg (2020), Laudon dan Laudon (2022), Sugiyono (2019), Kurniawan (2018), Hasan dkk. (2024), Lestari dkk. (2023), Febrianto dan Wulansari (2020), Kadek dkk. (2025), Antar dkk. (2025), Nugraha dkk. (2024), Azhariyah dan Mukhlis (2024), Yudin dkk. (2025), Hendartie dkk. (2023), dan Hermansah dkk. (2023) belum memiliki pasangan berkas yang identitasnya dapat dipastikan dari korpus pemeriksaan. Ini berarti belum dapat diverifikasi dari bahan yang ada, bukan keputusan bahwa semua sumber tersebut tidak pernah terbit.

**Cara memperbaiki:** pertama, sediakan metadata lengkap dan salinan bagian yang benar-benar dibaca. Kedua, cocokkan definisi dengan halaman aslinya, termasuk edisi buku. Ketiga, hapus atau ganti atribusi apabila sumber tidak dapat ditelusuri. Contoh penanda kerja: “[Sumber teori dan halaman belum terverifikasi; jangan diajukan sebelum dilengkapi].” Penanda ini hanya untuk draf kerja dan tidak dibawa ke naskah final.

### B2-21. Tabel penelitian terdahulu memuat keterbatasan yang belum dibuktikan

**Lokasi:** 2.2, Tabel 2.7, baris 338 sampai 343. **Kategori:** substansi dan referensi. **Prioritas:** sangat penting.

Tidak dijelaskannya fitur dalam artikel belum selalu berarti sistem pasti tidak mempunyai fitur itu. Penilaian “monolitik tradisional”, “tidak mendukung SPA”, “proses bisnis sederhana”, dan “tanpa interaksi multi-user” memerlukan bukti, bukan asumsi berdasarkan judul atau pilihan framework.

**Cara memperbaiki:** pertama, tambahkan kolom halaman bukti untuk setiap fitur dan hasil. Kedua, bedakan “dinyatakan penulis”, “terlihat pada implementasi”, dan “tidak dijelaskan dalam artikel”. Ketiga, bandingkan terhadap kebutuhan ARTHA, bukan terhadap usia teknologi. Contoh: “Artikel tidak menjelaskan mekanisme rekonsiliasi penerimaan pusat dan cabang. Aspek tersebut belum dapat dibandingkan lebih jauh dari informasi yang tersedia.” Jangan menyebut Laravel pasti memakai Blade apabila artikelnya tidak menjelaskan demikian.

### B2-22. Sintesis penelitian terdahulu belum mengikuti korpus terbaru

**Lokasi:** 2.2, Tabel 2.7 dan tiga celah penelitian, baris 330 sampai 352. **Kategori:** substansi dan relevansi. **Prioritas:** sangat penting.

Artikel tambahan tentang cabang, rekonsiliasi, kapasitas, dan penjadwalan sudah menjadi rujukan Bab 1 tetapi belum terwakili secara memadai pada sintesis Bab 2. Sebaliknya, Tabel 2.7 masih memakai sumber PxP keanggotaan yang belum dapat ditelusuri.

**Cara memperbaiki:** pertama, ganti baris yang tidak dapat diverifikasi dengan sumber yang nyata dan relevan. Kedua, sertakan Thiovanda sebagai pembanding dekat, Ahadi untuk pemisahan kewenangan, Hendri atau Sudirman untuk penerimaan dan pencocokan bank, serta Khafidhoh atau Kabisatullah untuk jadwal/kapasitas. Ketiga, pisahkan kelompok penelitian domain, fitur, dan proses pengembangan agar artikel tidak dipaksa membahas bimbel sekaligus PxP. Contoh sintesis: “Literatur domain digunakan untuk membandingkan fungsi operasional. Literatur PxP digunakan untuk merancang proses pengembangan individual dan dokumentasi evaluasinya.”

### B2-23. Klaim studi pertama dan ribuan siswa belum dapat dipertahankan

**Lokasi:** 2.2 butir pertama dan kedua, baris 346 sampai 349. **Kategori:** substansi dan integritas data. **Prioritas:** sangat penting.

Klaim “studi pertama” memerlukan penelusuran dengan cakupan yang dapat dipertanggungjawabkan, sedangkan jumlah ribuan siswa belum mempunyai rekap primer. Bab 1 sendiri menyebut jumlah siswa aktif belum terdokumentasi terpusat, sehingga kedua bab saling bertentangan.

**Cara memperbaiki:** pertama, hapus klaim prioritas universal. Kedua, gunakan jumlah siswa hanya setelah ada rekap bertanggal. Ketiga, rumuskan kontribusi terapan pada masalah ARTHA, bukan pembuktian superioritas PxP secara umum. Contoh: “Penelitian ini menerapkan PxP pada pengembangan prototipe sesuai kebutuhan ARTHA. Kontribusinya terletak pada rancangan dan evaluasi fungsi yang disepakati bersama mitra.”

### B2-24. Teori pendukung memasukkan fakta dan fitur baru yang belum dibatasi

**Lokasi:** 2.3.1 sampai 2.3.4, baris 362 sampai 384. **Kategori:** substansi dan konsistensi. **Prioritas:** penting.

Barizi merupakan studi sekolah musik, sehingga tidak membuktikan keterlambatan laporan mingguan ARTHA. Subbab ini juga menambahkan presensi siswa, analisis pertumbuhan, intervensi promosi, rapat akhir pekan, dan honor tentor yang belum semuanya diposisikan jelas pada rumusan masalah serta batasan Bab 1.

**Cara memperbaiki:** pertama, pisahkan definisi umum dari uraian kasus ARTHA. Kedua, hapus fakta operasional yang tidak mempunyai bukti primer. Ketiga, masukkan hanya fungsi yang disepakati dan dapat dievaluasi. Contoh: “Sistem informasi manajemen menyajikan informasi untuk mendukung kegiatan operasional dan pengambilan keputusan. Pada prototipe ini, informasi yang disajikan dibatasi pada pendaftaran, pembayaran, penjadwalan, dan rekap cabang sesuai ruang lingkup penelitian.” Sumber definisi tetap harus dilengkapi dan dibaca langsung.

## 7. Kesesuaian judul, rumusan masalah, tujuan, metode, dan simpulan

Judul resmi pada sampul belum tersedia. Dokumen kebutuhan masih mencantumkan landing page, sehingga pilihan judul sebaiknya ditetapkan setelah ruang lingkup diselaraskan. Contoh judul kerja yang sesuai dengan fokus Bab 1 adalah “Pengembangan Prototipe Sistem Informasi Manajemen Operasional Multicabang Berbasis Web Menggunakan Personal Extreme Programming pada Bimbel Artha Balikpapan”; ini usulan untuk dibahas, bukan klaim judul telah disetujui.

### 7.1 Matriks keterlacakan yang perlu dipenuhi

| Rumusan masalah saat ini | Tujuan yang berpasangan | Bukti metode dan hasil yang diperlukan | Batas simpulan yang sah |
| :--- | :--- | :--- | :--- |
| RM 1: integrasi pendaftaran, pembayaran, dan penjadwalan | Tujuan 1 | Kebutuhan tervalidasi, user story, aturan bisnis, skema data, implementasi, hasil uji positif/negatif dan lintas cabang | Fungsi terbangun dan bekerja pada skenario yang diuji; bukan otomatis meningkatkan mutu pembelajaran |
| RM 2: dasbor pusat dan rekonsiliasi | Tujuan 2 | Definisi penerimaan, kas, setoran, mutasi bank; alur pencocokan; hak akses; transaksi contoh dan kasus selisih | Dasbor dan pencocokan memenuhi aturan uji; bukan kepastian seluruh laporan keuangan lembaga akurat |
| RM 3: kesesuaian kebutuhan melalui pengujian dan UAT | Tujuan 3 | Kasus uji tertelusur ke kebutuhan, hasil aktual, daftar perbaikan, tugas UAT, informan/pengguna dan keputusan penerimaan | Tingkat kesesuaian dan penerimaan pada pengguna serta skenario yang benar-benar diperiksa |

Secara struktur, ketiga rumusan masalah sudah mempunyai pasangan tujuan. Kelemahannya terletak pada belum operasionalnya istilah waktu nyata, rekonsiliasi, tingkat kesesuaian, dan cakupan delapan cabang. Hasil, pembahasan, serta simpulan aktual belum tersedia sehingga kesesuaiannya dengan tujuan belum dapat dinilai.

### 7.2 Koreksi rancangan metodologi yang masih harus dilengkapi

| Komponen | Penilaian dan prioritas | Langkah praktis serta contoh bentuk yang diperlukan |
| :--- | :--- | :--- |
| Bentuk tugas akhir | Sangat penting: gunakan kerangka prototipe sesuai panduan | Nyatakan objek, luaran, proses rancang bangun, dan evaluasi mitra. Contoh: “Penelitian berfokus pada pengembangan dan evaluasi prototipe, dengan PxP sebagai metode pengembangan perangkat lunak.” |
| Desain penelitian | Sangat penting: PxP belum menggantikan seluruh desain penelitian | Susun hubungan pengumpulan kebutuhan, analisis, pengembangan iteratif, pengujian, dan pelaporan. Jelaskan kapan data dikumpulkan, siapa sumbernya, serta cara menarik kesimpulan. |
| Populasi, sampel, atau informan | Sangat penting: jumlah dan dasar pemilihan belum tersedia | Untuk wawancara, pilih pihak yang menguasai alur kerja dan jelaskan alasan pemilihannya. Untuk UAT, tentukan cakupan Admin Cabang dan pengelola pusat serta variasi cabang yang diwakili; jangan memakai rumus sampel siswa bila siswa bukan pengguna yang diuji. |
| Wawancara dan observasi | Penting: perlu prosedur yang dapat ditelusuri | Lampirkan panduan pertanyaan, waktu, konteks cabang, rekaman/transkrip dengan izin, serta matriks fakta ke kebutuhan. Jangan menyebut observasi sudah dilakukan apabila belum ada catatan observasi. |
| Analisis kebutuhan | Sangat penting: belum ada matriks bukti ke kebutuhan yang tunggal | Susun kode kebutuhan, sumber, alasan, prioritas, aturan bisnis, dan validasi mitra. Bedakan kebutuhan pengguna dari keputusan peneliti tentang teknologi. |
| Hipotesis | Tidak otomatis diperlukan | Jika tujuannya membangun dan mengevaluasi kesesuaian prototipe, pertanyaan evaluatif dapat memadai. Hipotesis diperlukan jika desain memang menguji hubungan atau perbedaan tertentu, bukan sekadar melengkapi daftar bab. |
| Validitas instrumen | Penting: tidak boleh hanya menyatakan “sudah valid” | Petakan butir ke kebutuhan atau konstruk yang diukur, minta telaah pembimbing/ahli yang relevan, dan perbaiki butir melalui uji keterbacaan pengguna. Catat perubahan dan alasan. |
| Reliabilitas | Bersyarat menurut jenis instrumen | Kuesioner multibutir untuk satu konstruk dapat memerlukan pemeriksaan konsistensi yang sesuai dengan jumlah responden dan tujuan analisis. Cronbach alpha bukan kewajiban otomatis untuk daftar tugas penerimaan atau kumpulan fungsi yang heterogen; jangan membuat angka reliabilitas sebelum data ada. |
| Teknik analisis data | Sangat penting: pisahkan jenis data | Jelaskan sintesis wawancara menjadi kebutuhan, ringkasan hasil kasus uji, keputusan tugas UAT, analisis skor persepsi bila digunakan, dan evaluasi log PxP. Setiap persentase harus mempunyai pembilang, penyebut, dan aturan penanganan kegagalan. |
| Pengukuran waktu nyata | Penting: istilah belum terukur | Tentukan apakah data muncul setelah penyegaran halaman, polling berkala, atau pembaruan otomatis. Tetapkan kriteria waktu respons dari kebutuhan mitra dan uji pada kondisi yang dijelaskan. |
| Evaluasi PxP | Sangat penting bila mengklaim penerapan disiplin PxP | Simpan rencana dan waktu aktual per tugas, galat ditemukan/diperbaiki, bukti tes, perubahan kebutuhan, serta catatan retrospective. Contoh analisis: “Selisih waktu aktual dan estimasi ditelaah per iterasi beserta penyebabnya.” Jangan menyimpulkan PxP lebih unggul dari metode lain tanpa desain pembandingan. |
| Data dan akses | Penting: data anak, bukti transfer, dan rekening memerlukan pembatasan | Gunakan data uji tersamarkan, tetapkan pengguna yang boleh melihat bukti transfer, serta catat izin penggunaan data penelitian. Sajikan hanya data yang diperlukan pada lampiran dan demonstrasi. |
| Luaran prototipe | Penting: rencana harus sesuai panduan | Panduan SI 2026 cetak 4/PDF 11 menyebut TKT 5, evaluasi mitra/calon pengguna, produk, laporan, artikel ilmiah, dan pendaftaran HKI. Masukkan rencana bukti pemenuhan, bukan menyatakan seluruhnya sudah selesai. |

## 8. Konsistensi dokumen pendukung

Pemeriksaan berikut merupakan temuan terarah pada bagian yang berhubungan dengan Bab 1 dan Bab 2. Dokumen pendukung memuat klaim keputusan “final” yang tidak boleh menggantikan transkrip bimbingan atau persetujuan mitra yang dapat ditelusuri.

| Kode dan lokasi | Masalah, kategori, dan prioritas | Cara memperbaiki dan contoh |
| :--- | :--- | :--- |
| D-01: use case baris 389; Bab 1 baris 64 | Gateway terjadwal H-7/H-1/H+3 berbeda dari tautan manual. Substansi, sangat penting. | Pilih mekanisme dan dasar jadwal, lalu perbarui kebutuhan, Bab 1, Bab 2, tabel log, dan kasus uji. Contoh sementara: “Mekanisme pengiriman ditetapkan setelah validasi mitra.” |
| D-02: use case baris 353 sampai 357; bimbingan Bu Ayu tentang peringatan | Penolakan mutlak jadwal/kelas berbeda dari rencana peringatan dan diskresi pengelola. Metodologi, sangat penting. | Bedakan aturan keras yang tidak boleh dilanggar dan aturan yang dapat dikecualikan oleh petugas tertentu. Contoh: “Pengecualian, bila diizinkan mitra, dicatat beserta alasan dan pengguna yang menyetujuinya.” |
| D-03: skema baris 227 sampai 234 dan 443 | Perbandingan expected_revenue dengan actual_revenue lebih dekat ke tagihan versus penerimaan, belum cukup sebagai rekonsiliasi bank. Analisis data, sangat penting. | Tambahkan model penerimaan, setoran, sumber mutasi, pencocokan, dan transaksi belum cocok sesuai lingkup yang dipilih. Contoh: “Selisih tagihan dan penerimaan dilaporkan terpisah dari selisih pencocokan bank.” |
| D-04: skema baris 360 dan use case baris 23 | branch_id NULL dipakai sebagai penanda Super Admin. Rancangan otorisasi, penting. | Pastikan hak akses didasarkan pada peran yang sah dan kebijakan otorisasi, bukan semata nilai NULL. Uji akun tidak sah yang konteks cabangnya kosong dan akses objek cabang lain. |
| D-05: skema baris 405, dokumen kebutuhan bagian masalah 3 | Insiden tentor di dua cabang diklaim pernah terjadi tanpa bukti primer yang sudah ditemukan. Substansi, sangat penting. | Minta tanggal/kasus atau ubah menjadi risiko preventif. Contoh: “Fitur dirancang memeriksa potensi benturan penugasan lintas cabang.” |
| D-06: dokumen kebutuhan bagian website existing | Konten publik yang dapat diambil otomatis dianggap bukti keamanan sangat rendah. Analisis, penting. | Bedakan keterbukaan konten publik dari kerentanan keamanan. Jangan menilai keamanan WordPress, keberadaan API, atau penyimpanan formulir tanpa pemeriksaan teknis yang relevan. |
| D-07: skema baris 334 dan use case baris 557 | Templat WhatsApp disebut berada pada konfigurasi kode, tetapi use case menjanjikan pengeditan melalui tabel wa_templates. Konsistensi rancangan, penting. | Putuskan siapa yang mengubah templat dan bagaimana perubahan diterapkan. Samakan kamus data, antarmuka, dan kriteria penerimaannya. |
| D-08: Bab 1 butir tidak migrasi; kebutuhan master data | Tidak migrasi transaksi historis berbeda dari tidak memerlukan data awal. Substansi, penting. | Tentukan data awal akun, cabang, ruang, tentor, siswa uji, tarif, serta saldo/tagihan awal bila diperlukan. Contoh: “Transaksi historis tidak dimigrasikan, sedangkan data master yang diperlukan disiapkan untuk pengujian.” |

## 9. Referensi, kemutakhiran, dan kemiripan redaksi

### 9.1 Hasil perubahan sitasi Bab 1

Audit sebelumnya mencatat sepuluh penggunaan rujukan didukung, sebelas didukung sebagian, lima tidak didukung, dan satu bertentangan. Pada salinan baru, dua puluh tujuh penggunaan rujukan ditangani melalui dua puluh enam rentang penggantian karena satu rentang memuat Ramadhan serta Sudirman bersamaan.

Enam atribusi yang tidak dapat dipertahankan ditarik dan diganti penanda catatan SIT. Sitasi yang didukung sebagian tetap diberi catatan batas cakupan, sehingga pembaca tidak salah memahami sitasi sebagai pembenaran seluruh kalimat. Buku Beck menggunakan Bab 7 dan nama bagian karena urutan PDF 104 tidak sama dengan nomor halaman cetak yang dapat diverifikasi.

Rincian klaim dan halaman dapat diperiksa pada [laporan audit sitasi](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/AUDIT_SITASI_BAB1_2026-10-25/LAPORAN_AUDIT_SITASI_BAB1.md>) dan [peta halaman sumber](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/AUDIT_SITASI_BAB1_2026-10-25/PETA_CEPAT_HALAMAN_RUJUKAN.md>). Bukti bahwa seluruh redaksi di luar sitasi tetap sama tersedia pada [log perubahan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/AUDIT_SITASI_BAB1_2026-10-25/BUKTI_REVISI_SITASI_SAJA.json>).

### 9.2 Daftar pustaka lengkap belum dapat diperiksa

Berkas Bab 1 dan Bab 2 yang diperiksa belum menyertakan daftar pustaka gabungan lengkap. Oleh karena itu, kesesuaian dua arah antara semua sitasi dan entri pustaka, urutan alfabet, duplikasi, hanging indent, serta ketepatan seluruh DOI belum dapat dinyatakan lulus.

**Prioritas: sangat penting.** Langkah pertama adalah menyusun satu pustaka induk melalui pengelola referensi. Langkah kedua adalah memastikan setiap sitasi mempunyai entri dan setiap entri benar-benar dirujuk. Langkah ketiga adalah memeriksa nama dan tahun berdasarkan artikel, bukan nama file; misalnya rentang Barizi berakhir pada 338, bukan 339, dan nama penulis Fikri perlu disamakan dengan Arthawan.

### 9.3 Kemutakhiran dan status SINTA

Panduan umum ITK 2025 pada cetak 4/PDF 12 menyebut sedikitnya sepuluh rujukan dan proporsi tujuh puluh persen dari sepuluh tahun terakhir. Rubrik **kategori Sangat Baik** seminar proposal prototipe pada panduan SI 2026 cetak 80/PDF 87 menekankan sedikitnya sepuluh pustaka dari lima tahun terakhir; ini perlu dibaca sebagai kriteria rubrik, bukan alasan untuk menghapus seluruh teori klasik yang masih tepat.

Gunakan artikel mutakhir untuk kebutuhan aplikasi dan temuan empiris, sedangkan sumber dasar seperti Dzhurov, Beck, atau Sommerville dapat dipertahankan sesuai fungsi teorinya. Jumlah dan proporsi pustaka final belum dihitung sebagai kelulusan karena daftar pustaka lengkap belum tersedia. Buku dan prosiding internasional tidak dinilai “SINTA berapa” dengan cara yang sama seperti jurnal nasional, dan peringkat SINTA tidak menjamin semua klaim dalam artikel benar.

Pemeriksaan ini tidak melakukan pembaruan status akreditasi semua jurnal per tanggal laporan. Label peringkat pada Tabel 2.7 perlu dicocokkan kembali dengan identitas jurnal dan masa berlaku SK yang mencakup edisi artikel apabila tetap dicantumkan. Untuk naskah skripsi, label SINTA pada setiap baris penelitian terdahulu biasanya bukan pengganti telaah isi dan dapat ditempatkan pada catatan pemilihan referensi.

### 9.4 Penyaringan kemiripan redaksi lokal

Dilakukan pencocokan mekanis dua belas kata berturutan yang telah dinormalisasi pada prosa Bab 1 asal dan Bab 2 terhadap teks dari lima puluh PDF di JURNAL, di luar berkas bukti akreditasi. Pemeriksaan ini tidak menemukan kecocokan persis dengan ambang tersebut pada prosa yang disaring. Hasil dan inventaris korpus tersedia pada [log kemiripan lokal](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/AUDIT_SITASI_BAB1_2026-10-25/INSPEKSI_KORPUS_DAN_KEMIRIPAN_LOKAL.json>).

Hasil tersebut **bukan skor Turnitin, bukan bukti bebas plagiarisme, dan bukan pemeriksaan parafrasa semantik**. Keterbatasannya meliputi sumber di luar folder, teks hasil terjemahan, halaman pindai yang tidak mempunyai teks native, kesamaan pendek, serta baris tabel/diagram yang tidak disertakan sebagai prosa pada penyaringan. Masalah integritas yang sudah nyata pada naskah ini adalah atribusi yang tidak tepat dan klaim yang melampaui bukti, meskipun tidak ditemukan kecocokan kata panjang pada pemeriksaan terbatas ini.

## 10. Bahasa, tabel, gambar, dan format akhir

### 10.1 Pemeriksaan bahasa yang perlu diterapkan lintas bab

| Temuan | Prioritas | Tindakan dan contoh |
| :--- | :--- | :--- |
| Ungkapan penilaian berlebihan: sahih, terbukti paling tepat, kepastian, menjamin | Penting | Ganti dengan fungsi, alasan, atau hasil terukur. Contoh: “dipilih berdasarkan kebutuhan pengembangan individual”, bukan “paling sahih secara ilmiah”. |
| Frasa promosi: elegan, bertenaga, gegas, sangat krusial | Penyempurnaan | Gunakan istilah netral yang sesuai bukti. Contoh: “ORM digunakan untuk mengelola relasi model dan basis data.” |
| Klaim mutu otomatis dari teknologi | Sangat penting | Jelaskan konfigurasi dan pengujian, atau ubah menjadi manfaat potensial. Framework tidak menjamin seluruh kebutuhan keamanan dan kinerja sudah terpenuhi. |
| Paragraf satu kalimat pada Bab 1 | Penting | Tambahkan kalimat penjelas yang bermakna atau gabungkan dengan paragraf yang sesuai. Ketentuan minimal kalimat tidak diterapkan secara kaku pada daftar, judul, dan entri pustaka. |
| Pemakaian istilah asing dan singkatan | Penyempurnaan | Definisikan PxP, UAT, API, dan istilah asing saat kemunculan awal yang relevan. Terapkan huruf miring sesuai panduan dan konsistensi istilah. |
| Dash panjang | Penting | Hilangkan dari prosa naskah akhir dan ganti dengan koma, titik dua, atau penghubung. Garis sintaks tabel dan diagram teks bukan tanda baca prosa; ubah diagram ke gambar yang layak pada dokumen akhir. |
| Angka pada awal kalimat | Penting | Awali kalimat dengan bentuk huruf atau ubah susunan. Nomor pada daftar, label tabel, dan kode pengujian tidak diperlakukan sebagai kalimat prosa. |

### 10.2 Tabel dan gambar

Tabel 2.1 terlalu lebar untuk halaman biasa, sedangkan Tabel 2.7 memuat kalimat panjang pada banyak kolom. Ringkas informasi menjadi dimensi yang relevan, pecah tabel bila perlu, dan pindahkan rincian halaman bukti ke lampiran matriks pustaka. Setiap tabel harus disebut dalam teks, memiliki judul konsisten, dan menyatakan sumber atau status sebagai rancangan peneliti.

Diagram ASCII pada Bab 2 berguna sebagai draf tetapi belum menjadi gambar laporan yang siap cetak. Ganti dengan diagram yang terbaca pada ukuran halaman akhir, bedakan teori asli dari adaptasi, dan gunakan caption serta nomor secara konsisten. Fishbone Bab 1 belum dinilai ulang kualitas visualnya dalam pemeriksaan ini, sehingga keterbacaan teks, ketepatan setiap label pada gambar, dan kecocokan dengan uraian tetap harus diperiksa pada hasil render akhir.

### 10.3 Format Word/PDF belum dapat diputuskan dari Markdown

Panduan ITK 2025 pada cetak 11/PDF 19 memuat ketentuan A4, Times New Roman 12, spasi 1,5, margin cermin dengan sisi dalam 4 cm dan sisi lain 3 cm, serta inden awal 1 cm. Aturan bahasa terdapat pada cetak 12/PDF 20, sedangkan Harvard dan pengelolaan referensi pada cetak 16/PDF 24; SITASI pada nama panduan SI merupakan aplikasi administrasi tugas akhir, bukan nama gaya sitasi.

Pemeriksaan akhir membutuhkan Word/PDF yang telah mengikuti template. Periksa nomor halaman awal dan isi, daftar isi otomatis, judul tabel/gambar, pemenggalan tabel, huruf miring, daftar pustaka alfabetis dengan inden gantung, serta rujukan silang lampiran. Laporan ini tidak menyatakan unsur tersebut sudah benar karena hasil tata letaknya belum tersedia.

## 11. Bab atau bagian yang belum dapat dinilai

| Bagian | Mengapa belum dapat dinilai | Informasi yang harus tersedia |
| :--- | :--- | :--- |
| Sampul dan judul resmi | Hanya judul kerja pada dokumen kebutuhan | Naskah judul yang akan diajukan dan konsistensinya dengan ruang lingkup final |
| Abstrak dan kata kunci | Tidak disertakan pada berkas Bab 1/2 | Abstrak sesuai tahap proposal atau hasil, tanpa mengarang hasil penelitian |
| Bab 3/metode lengkap | Belum tersedia sebagai bab metode utuh | Lokasi dan waktu, informan/pengguna, pengumpulan dan analisis data, tahapan PxP, instrumen dan rencana evaluasi |
| Hasil penelitian | Tidak tersedia hasil aktual beserta bukti | Versi aplikasi, data pengujian, log iterasi, hasil UAT, kasus gagal, serta tindak lanjut |
| Pembahasan | Belum ada hasil aktual untuk ditafsirkan | Analisis per rumusan masalah, kaitan dengan literatur, faktor penyebab, dan keterbatasan |
| Kesimpulan dan saran | Belum tersedia dan belum ada hasil aktual | Jawaban tiap rumusan masalah yang dibatasi bukti, serta saran yang berasal dari keterbatasan nyata |
| Daftar pustaka final | Belum tersedia sebagai daftar gabungan | Semua entri lengkap yang berpasangan dengan sitasi dan gaya yang ditetapkan kampus |
| Lampiran final | Belum disusun sebagai lampiran naskah akhir | Transkrip/izin, validasi kebutuhan, instrumen, bukti uji, rekap analisis, dan dokumen pendukung yang benar-benar ada |

Ketiadaan Bab 4 dan kesimpulan hasil tidak otomatis menjadi kesalahan pada tahap proposal. Sebaliknya, kolom hasil yang belum diuji harus dibiarkan sebagai rancangan, sehingga tidak muncul data atau simpulan seolah penelitian telah selesai.

## 12. Urutan revisi sebelum konsultasi pembimbing

### 12.1 Selesaikan terlebih dahulu

1. Pisahkan fakta wawancara, estimasi, risiko, dan usulan fitur. Hapus atau konfirmasi jumlah tentor, ribuan siswa, benturan berulang, dan frekuensi keterlambatan.
2. Perbaiki alur tunai, transfer, setoran cabang, dan pencocokan mutasi. Tetapkan kewenangan verifikasi serta cara menangani bukti yang belum cocok.
3. Koreksi pembandingan metode pada kedua bab. Prioritaskan kesalahan Scrum, penolakan prototyping, dan ketentuan RAD yang tidak didukung.
4. Revisi kebaruan dengan memasukkan manajemen cabang pada Jia Jia Education. Batasi kontribusi pada kebutuhan ARTHA dan hasil penelusuran yang benar-benar dilakukan.
5. Seragamkan ruang lingkup landing page, dua peran, WhatsApp, peringatan kapasitas, dan penerapan delapan cabang pada semua dokumen.
6. Koreksi metadata dan lengkapi sumber yang belum tersedia, lalu susun daftar pustaka induk. Selesaikan seluruh catatan SIT sebelum membuat naskah bersih.
7. Ubah tabel contoh pengujian menjadi rancangan yang tidak memuat keberhasilan fiktif. Lengkapi rencana UAT, instrumen, rumus, serta aturan keputusan penerimaan.

### 12.2 Siapkan bahan konsultasi yang konkret

1. Bawa satu lembar keputusan ruang lingkup dan satu diagram proses pembayaran yang membedakan kas tunai dari transfer bank.
2. Bawa tabel bukti wawancara dengan kolom klaim, cabang, informan, tanggal, penanda waktu, dan status validasi.
3. Bawa matriks penelitian terdahulu dengan halaman bukti fitur, khususnya Thiovanda, Ahadi, Sudirman/Hendri, Khafidhoh/Kabisatullah, serta sumber PxP.
4. Bawa rancangan metode lengkap yang memetakan kebutuhan, iterasi, luaran, serta evaluasi. Sertakan lembar kesediaan atau jadwal mitra apabila sudah disepakati.
5. Bawa contoh instrumen yang masih kosong: satu kasus uji fungsi, satu kasus akses lintas cabang, satu tugas UAT per peran, dan satu log PxP.
6. Setelah keputusan substansi stabil, rapikan bahasa, gambar, tabel, sitasi, dan format dokumen melalui template resmi.

### 12.3 Penilaian kesiapan

| Tahap | Penilaian saat ini | Alasan |
| :--- | :--- | :--- |
| Konsultasi pembimbing | Layak dibawa sebagai draf kerja dengan daftar masalah | Fokus dan mitra jelas, sedangkan keputusan metodologi serta cakupan membutuhkan pengesahan berdasarkan bukti yang disiapkan |
| Seminar proposal | Belum direkomendasikan sebagai naskah final siap diajukan | Masih ada klaim yang bertentangan dengan sumber, kebaruan terlalu luas, ketidaksesuaian antarberkas, dan rancangan evaluasi yang belum lengkap |
| Seminar hasil | Belum dapat dinilai | Hasil aktual, data pengujian, dan pembahasan belum tersedia dalam bahan pemeriksaan |
| Sidang akhir | Belum dapat dinilai | Naskah lengkap, hasil, kesimpulan, daftar pustaka, lampiran, serta pemenuhan luaran akhir belum tersedia |

Kelemahan utama naskah berada pada kebenaran atribusi dan hubungan antara bukti, kebutuhan, serta klaim capaian. Revisi yang paling bermanfaat bukan memperpanjang latar belakang, melainkan membuat setiap fakta dan keputusan pengembangan dapat ditelusuri sumbernya serta dapat diuji melalui rencana evaluasi yang jelas.

## 13. Penunjuk bukti wawancara dan bimbingan untuk pemeriksaan manual

Penunjuk berikut memakai baris transkrip dan penanda waktu rekaman, bukan nomor halaman laporan. Transkrip otomatis memuat beberapa salah dengar, sehingga nama orang, istilah keuangan, dan kalimat yang ambigu sebaiknya diperiksa kembali pada rekaman sebelum dipakai sebagai kutipan langsung.

| Temuan yang perlu diperhatikan | Lokator primer | Implikasi untuk revisi |
| :--- | :--- | :--- |
| Jumlah staf dan tentor tidak sama di semua cabang | [Frontdesk, baris 601](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:601>), 30:52 sampai 31:10 | Jangan mengalikan jumlah satu cabang sebagai jumlah pasti seluruh cabang |
| Jadwal pada cabang yang diwawancarai telah dibedakan | [Frontdesk, baris 607](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:607>), 31:10 sampai 33:06 | Belum mendukung klaim benturan tentor berulang; tidak pula membuktikan tidak pernah ada konflik di semua cabang |
| Kapasitas ruang berbeda dan penumpukan tidak dikonfirmasi | [Frontdesk, baris 881](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:881>), 45:19 sampai 46:30 | Uraikan kapasitas menurut ruang dan jenjang, lalu bedakan risiko dari kejadian aktual |
| Kapasitas kecil untuk bimbingan awal SD | [Wawancara ketiga, baris 468](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt:468>), 35:25 sampai 38:37 | Rentang delapan hingga lima belas tidak dapat dipakai sebagai aturan universal |
| Penerimaan harian dan penitipan laporan/setoran | [Frontdesk, baris 981](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:981>), 50:38 sampai 51:48 | Penitipan tidak selalu dilakukan oleh kepala cabang; frekuensi harian perlu dibedakan dari rekap bulanan |
| Bukti transfer dikirim ke pengelola pusat | [Frontdesk, baris 1017](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1017>), 52:24 sampai 52:42 | Jangan menyatakan pemeriksaan selalu menunggu berkas fisik tanpa konfirmasi tambahan |
| Informan belum pernah mengalami minus, tetapi mengakui kemungkinan risiko | [Frontdesk, baris 1072](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1072>), 55:24 sampai 56:02 | Risiko pencatatan manual tidak boleh diubah menjadi kerugian aktual yang sudah terjadi |
| Jatuh tempo dan pengingat manual mengikuti kondisi siswa | [Frontdesk, baris 1136](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1136>), 58:19 dan bagian berikutnya | Konfirmasi aturan penagihan sebelum menetapkan jadwal otomatis tetap untuk semua siswa |
| Pemisahan cakupan cabang dan akses pusat | [Bu Ayu, baris 567](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:567>), 27:16 sampai 28:16 | Jadikan kebutuhan otorisasi dan kasus uji lintas cabang |
| Peringatan dan kebijakan kapasitas | [Bu Ayu, baris 627](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:627>), 29:16 sampai 32:07 | Pastikan penolakan sistem tidak bertentangan dengan diskresi yang dibutuhkan pengelola |
| Diskusi perangkapan peran | [Bu Ayu, baris 1102](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:1102>), 46:43 sampai 47:01 | Hindari menggunakan larangan rangkap peran sebagai justifikasi mutlak metode |
| Mutasi rekening, bukti transfer, dan alternatif pembayaran masih dibahas | [Bu Ayu, baris 1387](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:1387>), 01:05:41 sampai 01:08:14 | Jangan menganggap satu opsi sudah disetujui final hanya berdasarkan dokumen ringkasan |
| Struktur uraian latar belakang | [Pak Arif, baris 6](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/PAK ARIF/TRANSKRIP TEKS (TXT)/BIMBINGAN KE 5 (Pak Arif)_WITH_TIMESTAMPS.txt:6>), 02:19 sampai 04:10 | Utamakan alur konteks, profil, masalah, solusi, dan metode; tidak ada dasar menjadikan jumlah paragraf sebagai ukuran mutu tunggal |

Setelah bukti yang ambigu dikonfirmasi, perbarui satu matriks fakta bersama agar seluruh bab menggunakan informasi yang sama. Kutipan langsung, nama, serta angka tetap perlu diperiksa pada sumber primer, terutama ketika hasil transkrip otomatis tidak jelas.
