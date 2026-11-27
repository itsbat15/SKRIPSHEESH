### Slide 1: Halaman Judul dan Pembukaan (Menit 00:00 sampai 00:35)

Assalamualaikum warahmatullahi wabarakatuh. Yang terhormat Dosen Pembimbing Satu Bapak Arif Wicaksono Septyanto, M.Kom., Dosen Pembimbing Dua Ibu Sri Rahayu Natasia, S.Kom., M.Si., M.Sc., Dosen Penguji Satu Bapak M. Ihsan Alfani Putera, S.Tr.Kom., M.Kom., dan Dosen Penguji Dua Bapak Ir. I Putu Deny Arthawan Sugih Prabowo, S.Kom., M.Eng.

Perkenankan saya, Ariel Itsbat Nurhaq NIM 10231018, mempresentasikan proposal Tugas Akhir berjudul "Rancang Bangun Sistem Informasi Manajemen Operasional Bimbingan Belajar Berbasis Web Menggunakan Metode Personal Extreme Programming, Studi Kasus: Bimbel Artha Balikpapan".

### Slide 2: Outline Presentasi (Menit 00:35 sampai 00:55)

Presentasi ini terdiri atas sebelas pokok bahasan. Pemaparan dimulai dari latar belakang, rumusan masalah, tujuan, batasan, serta manfaat dan dampak penelitian.

Selanjutnya, saya memaparkan penelitian terdahulu, lima belas konsep tinjauan pustaka beserta keterkaitannya, kerangka tugas akhir, arsitektur sistem, proses bisnis As-Is, dan rencana jadwal pengerjaan.

### Slide 3 dan Slide 4: Latar Belakang Masalah (Menit 00:55 sampai 02:25)

Pada Slide 3, objek penelitian ini adalah Bimbingan Belajar Artha Balikpapan yang berdiri sejak 10 Oktober 1997. Lembaga ini memiliki delapan cabang aktif bernama Artha 1 sampai Artha 8, dengan 60 tentor yang melayani sekitar 2.400 siswa jenjang TK hingga SMA. Setiap cabang dipimpin satu kepala cabang dan satu staf administrasi untuk mengelola pendaftaran, pengaturan sesi kelas harian, membuat rekap harian serta penagihan SPP dengan tarif bervariasi.

Berdasarkan wawancara bersama Ketua Bimbel Artha, Ibu Emi Ratnawati, S.E., dan staf cabang, pendaftaran siswa baru di delapan cabang masih dicatat pada buku besar fisik A4 yang tersimpan terpisah tanpa salinan cadangan dengan format pencatatan yang terbatas. Selanjutnya pada saat transaksi berlangsung, staf harus menerbitkan kuitansi rangkap dua, serta menghitung penyesuaian potongan biaya secara manual, sementara pembukuan kas wajib ditutup pukul 19.20 WITA sedangkan kelas sesi terakhir berakhir pukul 20.30 WITA. Akibatnya, riwayat administrasi rentan rusak atau hilang serta menyulitkan pelacakan status aktif siswa ketika terjadi pergantian staf cabang.

Dari kendala tersebut melemahkan pemantauan langsung di manajemen pusat. Kepala cabang hanya menyerahkan uang tunai dan selembar kertas rekapan ke kantor pusat di Artha 2 tanpa membawa buku besar, sehingga selisih sulit diverifikasi dan berisiko di perjalanan. Pembayaran transfer pun diperiksa manual terhadap mutasi rekening tanpa pantauan langsung.

Oleh sebab itu, dikembangkan sistem informasi manajemen operasional multicabang berbasis web terpusat menggunakan metode Personal Extreme Programming atau PXP. Pemilihan PXP memberi fleksibilitas bagi pengembang tunggal untuk merilis modul bertahap bersama mitra yang waktunya terbatas oleh operasional delapan cabang.

### Slide 5: Rumusan Masalah (Menit 02:25 sampai 02:55)

Terdapat dua rumusan masalah dalam Tugas Akhir ini. Pertama, bagaimana mengembangkan prototipe sistem informasi manajemen operasional bimbel multicabang berbasis web dengan metode PXP yang mengintegrasikan pendaftaran siswa, penempatan kelompok belajar, dan pembayaran SPP cabang ke dashboard rekonsiliasi pusat.

Kedua, bagaimana hasil evaluasi kesesuaian fungsional dan penerimaan pengguna melalui pengujian Black Box Testing dan User Acceptance Testing bagi pemilik lembaga serta staf cabang.

### Slide 6: Tujuan Penelitian (Menit 02:55 sampai 03:20)

Selaras dengan rumusan tersebut, tujuan pertama adalah mengembangkan prototipe sistem informasi manajemen operasional berbasis web bagi Bimbel Artha dengan metode PXP guna menyatukan layanan delapan cabang dan dashboard pengawasan kas pusat.

Tujuan kedua adalah mengevaluasi kelayakan fungsional serta penerimaan pengguna akhir terhadap prototipe melalui uji Black Box Testing dan User Acceptance Testing.

### Slide 7: Batasan Rancangan (Menit 03:20 sampai 03:55)

Prototipe ini memiliki empat batasan rancangan utama. Pertama, sistem berfokus pada dashboard operasional internal bagi dua peran saja, yakni Staf Administrasi Cabang sebagai Admin dan Pemilik Lembaga sebagai Super Admin.

Kedua, fitur belajar daring, bank soal, dan pelaporan nilai siswa tidak disertakan. Ketiga, sistem tidak memakai payment gateway sehingga pembayaran transfer diverifikasi manual oleh pusat lewat unggahan bukti transfer. Keempat, pengingat kepada wali murid dikirimkan melalui tautan WhatsApp yang diakses langsung dari sistem.

### Slide 8: Manfaat dan Dampak (Menit 03:55 sampai 04:35)

Sistem ini ditujukan memberi manfaat bagi tiga pihak. Bagi mitra Bimbel Artha, buku besar delapan cabang didigitalisasi ke database terpusat guna memantau kas, jumlah siswa aktif, serta mencegah hilangnya data saat pergantian staf. Bagi pengguna, staf cabang bekerja lebih cepat sementara pemilik dapat mencocokkan mutasi kas delapan cabang langsung dari sistem.

Bagi peneliti, tugas akhir ini menjadi wadah penerapan PXP pada kasus multicabang serta memperkaya kajian transformasi digital pendidikan nonformal. Secara fungsional, sistem memangkas waktu rekapitulasi bulanan, membantu staf fokus melayani siswa, dan memfasilitasi deteksi dini tunggakan SPP.

### Slide 9: Penelitian Terdahulu (Menit 04:35 sampai 05:25)

Dari sepuluh studi terdahulu yang dikaji pada Bab 2 proposal, Slide 9 menyoroti dua penelitian paling erat yang sama-sama memakai metode PXP. Pertama, penelitian Aolia Musofa dan rekan tahun 2025 menghasilkan aplikasi buku tamu digital melalui tujuh tahap PXP dengan hasil Black Box Testing seratus persen pada delapan puluh skenario uji. Perbedaannya, penelitian ini diterapkan pada satu instansi dinas, sedangkan sistem ARTHA mengintegrasikan kas dan kuota delapan cabang bimbel.

Kedua, penelitian Narti Apriyanti dan rekan tahun 2024 merancang situs e-kavling memakai PXP dengan modul validasi bukti transfer manual dan hasil UAT mencapai 91 persen dari tiga belas pengguna. Kesamaan mekanisme validasi manual tanpa payment gateway tersebut menjadi acuan utama modul pembayaran dan rekonsiliasi sistem ARTHA.

### Slide 10: Tinjauan Pustaka Bagian Pertama (Menit 05:25 sampai 08:00)

Pada Slide 10, terdapat sembilan konsep teori dan pemodelan yang langsung dihubungkan penerapannya ke dalam sistem ARTHA.

- **Sistem Informasi Manajemen**: Menurut Laudon dan Laudon tahun 2014, SIM adalah sistem pengolah data transaksi rutin menjadi laporan manajerial berkala guna mendukung kendali dan keputusan manajemen. Di ARTHA, konsep ini menyatukan transaksi pendaftaran dan SPP delapan cabang ke dashboard terpusat bagi Pemilik Lembaga.
- **Personal Extreme Programming**: PXP karya Dzhurov dan rekan memadukan Extreme Programming dan Personal Software Process menjadi tujuh tahapan iteratif bagi pengembang tunggal. Di proyek ini, PXP dipilih karena pengerjaan dilakukan mandiri oleh satu mahasiswa dengan evaluasi berkala menyesuaikan kesibukan mitra.
- **Business Process Model and Notation**: BPMN menurut Dumas dan rekan merupakan standar diagram alur kerja berisi event, task, gateway, swimlane, dan artefak data. Saya memakai BPMN di Bizagi Modeler untuk memetakan alur manual As-Is serta merancang alur digital To-Be.
- **User Stories**: User Stories menurut Cohn tahun 2004 adalah deskripsi kebutuhan ringkas dari sudut pandang pengguna beserta kriteria penerimaan. Seluruh kebutuhan ARTHA dirumuskan ke dalam dua belas User Stories US-01 hingga US-12 yang dibobotkan ke empat iterasi sekaligus menjadi tolok ukur uji.
- **Use Case Diagram**: Diagram UML ini memetakan batasan sistem dan interaksi aktor dengan layanan sistem melalui asosiasi, include, dan extend. Di ARTHA, diagram ini memodelkan dua belas fungsi utama Admin Cabang dan Super Admin, termasuk kewajiban cek kuota saat mendaftar dan unggah bukti transfer kondisional.
- **Activity Diagram**: Diagram UML ini memvisualisasikan urutan aksi, percabangan, aliran paralel, dan swimlane tanggung jawab. Pada proposal, diagram ini merinci alur transaksi pendaftaran tunai, validasi transfer, serta tutup kasir harian dan pemantauan tunggakan SPP.
- **Entity Relationship Diagram**: ERD merupakan pemodelan konseptual entitas, atribut, dan kardinalitas relasi untuk mencegah redundansi data. Rancangan ERD ARTHA mencakup sepuluh entitas dan enam belas relasi dengan Cabang sebagai induk guna mengisolasi data antarcabang.
- **Three-Tier Architecture**: Pola arsitektur ini memisahkan sistem menjadi lapisan presentasi, logika aplikasi, dan penyimpanan data secara mandiri. Pemisahan ini diterapkan di ARTHA agar antarmuka cabang, aturan bisnis, dan database tetap terstruktur serta mudah dipelihara.
- **Next.js**: Next.js merupakan framework React dengan dukungan Server-Side Rendering, App Router, dan middleware server untuk memuat halaman cepat sekaligus mengamankan endpoint API. Di ARTHA, Next.js membangun antarmuka web responsif bagi tablet cabang dan laptop manajemen pusat.

### Slide 11: Tinjauan Pustaka Bagian Kedua (Menit 08:00 sampai 09:40)

Melanjutkan ke Slide 11, berikut enam konsep teknologi implementasi serta metode pengujian yang digunakan beserta keterkaitannya.

- **Tailwind CSS**: Tailwind CSS menurut Santoso tahun 2025 adalah framework penataan gaya utility-first yang menyusun tampilan responsif memakai kelas utilitas secara langsung. Di ARTHA, framework ini memastikan tampilan formulir dan dashboard rapi pada tablet sentuh sepuluh koma satu inci di cabang maupun layar laptop pusat.
- **Laravel**: Laravel menurut Tan tahun 2025 adalah framework PHP berpola Model-View-Controller dengan Eloquent ORM dan middleware otorisasi peran. Pada sisi backend ARTHA, Laravel mengeksekusi logika validasi kuota, jatuh tempo SPP, rekonsiliasi kas, serta pengamanan token melalui Laravel Sanctum.
- **REST API**: REST API merupakan arsitektur komunikasi stateless melalui HTTP dan format JSON menggunakan metode GET, POST, PUT, dan DELETE. Di ARTHA, REST API menjadi penghubung pertukaran data terstruktur antara antarmuka Next.js delapan cabang dan backend Laravel pusat.
- **MySQL**: MySQL adalah sistem manajemen basis data relasional yang menegakkan validasi schema-on-write, kunci relasi, serta prinsip transaksi ACID. MySQL digunakan pada lapisan data ARTHA sebagai pangkalan data terpusat guna mencegah pencatatan transaksi keuangan yang terpotong atau parsial.
- **Black Box Testing**: Metode pengujian ini memeriksa kesesuaian input dan output fungsi tanpa meninjau kode program internal, dioptimalkan lewat Equivalence Partitioning dan Boundary Value Analysis. Di ARTHA, teknik ini menguji skenario valid, tidak valid, hingga batas ekstrem kuota kelas pada fase System Testing.
- **User Acceptance Testing**: UAT adalah pengujian akhir bersama pengguna langsung memakai skenario operasional nyata dan kuesioner Skala Likert lima poin. Di ARTHA, UAT melibatkan Pemilik Lembaga dan Staf Cabang untuk memastikan sistem layak diterima dan digunakan.

### Slide 12: Kerangka Tugas Akhir (Menit 09:40 sampai 11:55)

Pada Slide 12 yang merujuk Gambar 1.1 Bab 1 proposal, alur pengerjaan dibagi ke dalam inisiasi penelitian, siklus rekayasa PXP, serta evaluasi UAT dan publikasi sistem.

Tahap awal **Identifikasi Masalah** dilakukan lewat observasi dokumen fisik dan wawancara di delapan cabang, menghasilkan rumusan masalah dan model proses berjalan As-Is. Berikutnya **Studi Literatur** menelaah teori SIM, arsitektur web, PXP, dan metode uji guna menghasilkan landasan teori dan penentuan perangkat teknologi.

Memasuki siklus PXP, tahap **Requirements** menggali kebutuhan rinci guna menghasilkan dua belas kebutuhan fungsional, enam kebutuhan non-fungsional, matriks RBAC, serta dua belas User Stories dengan Acceptance Criteria. Selanjutnya **Planning** menilai ketergantungan modul dan bobot Story Points guna memetakan jadwal ke dalam empat iterasi.

Setiap iterasi diawali **Iteration Initialization** untuk memilih User Stories prioritas dan memecahnya menjadi daftar tugas teknis sebagai target iterasi berjalan. Kemudian tahap **Design** menerjemahkan kebutuhan memakai prinsip Simple Design untuk menghasilkan proses bisnis To-Be, Use Case Diagram, Activity Diagram, ERD sepuluh entitas, arsitektur tiga lapis, dan wireframe low-fidelity.

Tahap **Implementation** menjalankan prinsip Test-Driven Development melalui tiga sub-tahap berurutan. Proses dimulai dari **Unit Testing** untuk membuat uji validasi logika terlebih dahulu, diikuti **Code** guna membangun antarmuka Next.js, REST API Laravel, dan migrasi MySQL, serta **Refactor** untuk merapikan struktur kode sehingga menghasilkan modul yang lolos uji unit.

Berikutnya, **System Testing** menguji fungsionalitas dan keamanan Sanctum memakai Black Box Testing untuk menghasilkan log uji dan perbaikan bug bila ditemukan. Setiap siklus ditutup dengan **Retrospective** guna membandingkan realisasi terhadap estimasi dan mendemonstrasikan modul ke mitra untuk menghimpun umpan balik.

Percabangan **Perlu Iterasi Lanjutan** mengembalikan alur ke Iteration Initialization bila masih ada modul tersisa, atau berlanjut ke **User Acceptance Testing** bila keempat iterasi selesai. Pengujian UAT bersama pemilik dan staf cabang menggunakan checklist uji dan kuesioner Skala Likert guna menghasilkan Berita Acara Penerimaan Sistem, yang sesuai Gambar 1.1 proposal diteruskan ke tahap **Deployment** di Vercel serta Hostinger sebelum selesai.

### Slide 13: Arsitektur Sistem (Menit 11:55 sampai 13:05)

Pada Slide 13, rancangan teknis ARTHA menerapkan pola **Three-Tier Architecture** sesuai Subbab 3.4.1 proposal guna memisahkan lapisan tampilan, logika bisnis, dan penyimpanan data.

Lapisan pertama yaitu **Presentation Tier** melayani interaksi Pemilik Lembaga selaku Super Admin dan Staf Cabang selaku Admin melalui tablet frontdesk maupun komputer. Antarmuka dibangun memakai **Next.js App Router** dan **Tailwind CSS** yang responsif serta menyembunyikan detail endpoint server dari peramban pengguna.

Antara lapisan pertama dan kedua terjadi pertukaran data terenkripsi berupa **HTTPS Request** dan kembalian **JSON Response**. Lapisan tengah yaitu **Application Tier** berbasis **Laravel** yang menyediakan **REST API** serta **Laravel Sanctum** untuk autentikasi token dan pembatasan akses RBAC per cabang. Di lapisan ini pula logika pendaftaran, validasi kuota, jatuh tempo SPP, dan rekonsiliasi kas diproses.

Selanjutnya, komunikasi ke lapisan paling kanan berjalan lewat pengiriman **Query SQL** dan penerimaan **Result Sets**. Lapisan ketiga atau **Data Storage Tier** yang disebut Data Tier pada proposal menggunakan satu database **MySQL** terpusat berprinsip ACID guna menjaga akurasi dan konsistensi data transaksi delapan cabang.

### Slide 14: Proses Bisnis As-Is (Menit 13:05 sampai 14:20)

Pada Slide 14 ditampilkan pemetaan proses bisnis berjalan **As-Is** berstandar BPMN pada Bizagi Modeler dengan tiga jalur peran atau swimlane, yakni **Wali Murid atau Siswa**, **Staf Administrasi Cabang**, serta **Manajemen Pusat**.

Alur dimulai saat Wali Murid berkonsultasi mengenai program dan hari belajar, lalu staf cabang memeriksa sisa kursi secara manual pada artefak **Buku Jadwal**. Jika cocok, wali murid mengisi lembar formulir fisik, kemudian staf menyalin ulang biodata siswa ke artefak **Buku Besar Cabang** berukuran A4 yang rawan menimbulkan duplikasi data.

Alur lalu masuk ke gerbang keputusan eksklusif **Metode Pembayaran**. Pada jalur **Transfer**, wali murid mentransfer dana dan menunjukkan bukti transfer yang difoto staf untuk dikirim lewat WhatsApp tanpa arsip cabang, lalu siswa mengikuti kegiatan belajar. Pada jalur **Tunai**, staf menerima uang, menulis kuitansi manual rangkap dua, serta memperbarui **Kartu SPP Bulanan**.

Setelah pembayaran tunai, gerbang paralel membagi dua jalur serentak, yaitu siswa masuk kelas dan staf menulis memo rekap kas pukul 19.20 WITA pada artefak **Selembar Kertas**. Uang tunai dan lembar rekapan dititipkan melalui pengajar ke kantor pusat Artha 2, di mana **Manajemen Pusat** memeriksa mutasi lewat aplikasi **m-Banking** pada malam hari guna menuntaskan rekonsiliasi delapan cabang. Bersama pengecekan manual jatuh tempo SPP, alur inilah yang memicu lima kendala operasional pada Tabel 3.1 proposal.

### Slide 15: Rencana Jadwal (Menit 14:20 sampai 14:45)

Pada Slide 15 yang mengacu Tabel 3.12 proposal, jadwal pengerjaan berlangsung selama delapan bulan dari Oktober 2026 hingga Mei 2027. Studi Literatur berjalan kontinu sepanjang periode penelitian.

Tahap Requirements dan Planning dituntaskan hingga Desember 2026, kemudian tahap Iteration Initialization, Design, Implementation, System Testing, dan Retrospective berjalan tumpang tindih pada Januari hingga April 2027 untuk menyelesaikan empat iterasi PXP. Bulan Mei 2027 dialokasikan dua minggu untuk UAT bersama mitra dan ditutup Deployment pada dua minggu terakhir.

### Slide 16: Penutup dan Ucapan Terima Kasih (Menit 14:45 sampai 15:00)

Demikian pemaparan rancangan proposal Tugas Akhir saya mengenai Sistem Informasi Manajemen Operasional Bimbel Artha Balikpapan. Terima kasih atas perhatian Bapak dan Ibu pembimbing serta penguji, waktu selanjutnya saya serahkan kepada pimpinan sidang untuk sesi diskusi. Wassalamualaikum warahmatullahi wabarakatuh.

---

## Catatan Penyelarasan PPT dengan Proposal Sebelum Seminar

Ketika menyinkronkan isi `PPT SEMPRO.pdf` dengan `Proposal Tugas Akhir_Ariel Itsbat N_10231018.pdf`, terdapat beberapa detail teknis minor yang perlu menjadi perhatian presenter. Penyelarasan berikut membantu menjaga keutuhan argumen bila penguji memeriksa slide dan berkas cetak secara bersamaan.

- **Urutan Pencatatan Pendaftaran dan Transaksi pada Slide 3**: Pada Slide 3 PPT tertulis frasa bahwa seluruh pencatatan transaksi mengandalkan buku besar A4, sedangkan pada Subbab 1.1 halaman 3 proposal dijelaskan secara lebih rinci bahwa **pendaftaran siswa baru** yang terlebih dahulu dicatat pada buku besar A4 dengan format terbatas, lalu **pada saat transaksi berlangsung** staf menerbitkan kuitansi rangkap dua, membubuhkan paraf kartu SPP, dan menghitung potongan manual. Narasi lisan untuk Slide 3 di atas telah disesuaikan mengikuti urutan Bab 1.1 proposal agar konsisten saat dipresentasikan maupun saat penguji membaca dokumen proposal.
- **Kotak Deployment pada Slide 12**: Pada Gambar 1.1 halaman 12 proposal terdapat kotak tahap **Deployment** tepat setelah kotak User Acceptance Testing menuju Selesai, sedangkan pada diagram di Slide 12 alur dari UAT langsung mengarah ke Selesai. Narasi di atas telah menambahkan penjelasan Deployment di akhir Slide 12 agar tetap sinkron dengan proposal dan Slide 15 Rencana Jadwal, atau Anda dapat menambahkan satu kotak Deployment pada Slide 12 bila masih sempat menyunting salindia.
- **Salah Ketik Ringan pada Slide 10 dan Slide 11**: Pada Slide 10 tertulis `Three Tierr Architecture` karena kelebihan satu huruf r, dan pada Slide 11 tertulis `User Accaptance Testing` karena huruf a kedua seharusnya e menjadi `Acceptance`. Narasi lisan sudah disesuaikan dengan istilah yang benar, namun merapikan kedua teks tersebut pada slide akan membuat tampilan presentasi makin profesional.
- **Penjelasan Hasil Uji pada Slide 9 dan Slide 13**: Pada Slide 9 kolom Hasil milik Apriyanti tertulis keberhasilan Black Box sebesar seratus persen pada seluruh transaksi, sedangkan pada Tabel 2.6 proposal tertulis pengujian Black Box berhasil pada fungsi yang diuji dengan nilai UAT 91 persen. Sementara itu, pada Slide 13 label lapisan ketiga tertulis `DATA STORAGE TIER` sedangkan pada Gambar 3.2 proposal tertulis `DATA TIER`, yang keduanya merujuk pada basis data MySQL yang sama sehingga narasi sudah menjembatani kedua istilah dan angka tersebut secara mulus.
