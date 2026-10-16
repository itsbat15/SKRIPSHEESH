# BAB 1

## PENDAHULUAN

Bab ini memaparkan kerangka awal perancangan prototipe Tugas Akhir yang berfokus pada pengembangan sistem informasi manajemen operasional berbasis web untuk Bimbingan Belajar Artha Balikpapan. Pokok bahasan di dalamnya mencakup latar belakang permasalahan yang mendorong dirancangnya prototipe, rumusan masalah, tujuan yang ingin dicapai, batasan rancangan, manfaat bagi berbagai pihak, potensi dampak fungsional dan komersial, serta kerangka tahapan pengembangan prototipe berbasis metode Personal Extreme Programming (PxP).

---

## 1.1 Latar Belakang

Bimbingan belajar merupakan salah satu bentuk satuan pendidikan nonformal yang berfungsi menunjang dan melengkapi proses pembelajaran siswa di luar jam sekolah formal. Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional mengakui pendidikan nonformal sebagai jalur yang sah dalam mendukung pencapaian kompetensi akademik peserta didik. Pelayanan yang dijalankan dalam bimbingan belajar mencakup pendampingan materi pelajaran, penguatan pemahaman kurikulum, dan persiapan menghadapi ujian. Keberhasilan penyelenggaraan bimbingan belajar ditopang oleh keterpaduan berbagai elemen, mulai dari peserta didik, tentor pengajar, ketersediaan ruang kelas, hingga pengaturan jadwal bimbingan. Seluruh elemen tersebut saling berkaitan dalam menciptakan kegiatan belajar yang efektif dan teratur, sehingga tata kelola operasional yang tertata dengan baik sangat diperlukan agar pelayanan dapat berjalan tertib dan tepat sasaran (Tiana & Gunanto, 2026).

Untuk mewujudkan tata kelola operasional yang tertata tersebut, pemanfaatan sistem informasi memegang peranan yang mendasar. Sistem informasi merupakan seperangkat prosedur yang dirancang untuk mengumpulkan, mengolah, menyimpan, dan mendistribusikan informasi kepada pihak-pihak yang membutuhkan (Pradana, 2024). Dalam lingkup lembaga pendidikan, sistem informasi berfungsi mendukung tertib administrasi, mulai dari pencatatan data peserta didik, pengelolaan pembayaran berkala, hingga pengaturan jadwal pengajar (Maliki dkk., 2024). Penggunaan sistem informasi berbasis web memungkinkan data operasional dihimpun pada satu basis data terpusat sehingga mempermudah pengelola dalam memantau kegiatan lembaga secara langsung dan transparan.

Salah satu lembaga pendidikan nonformal yang terus berupaya mengelola operasional pelayanannya adalah Bimbingan Belajar (Bimbel) Artha Balikpapan, yang beralamat di Jalan Pandan Wangi, Kecamatan Balikpapan Barat, Kota Balikpapan, Kalimantan Timur. Lembaga ini didirikan pada 10 Oktober 1997 dan telah melayani masyarakat selama hampir 29 tahun. Seiring bertambahnya kepercayaan peserta didik dan wali murid, Bimbel Artha berkembang hingga memiliki delapan cabang aktif yang tersebar di Kota Balikpapan, yang dinamai Artha 1 sampai Artha 8. Secara keseluruhan, delapan cabang tersebut melayani lebih dari 2.000 siswa aktif per tahun dari jenjang TK, SD, SMP, sampai SMA, dengan didampingi oleh sekitar 60 tentor pengajar.

Berdasarkan hasil wawancara dengan pengelola, ditemukan bahwa seluruh administrasi operasional di delapan cabang masih dikerjakan secara manual. Pendaftaran siswa baru dicatat pada buku besar kertas berukuran A4 yang disimpan terpisah di setiap cabang. Buku tersebut hanya memuat nama siswa, nomor telepon wali, asal sekolah, dan tabel riwayat pembayaran SPP selama dua belas bulan. Alamat tempat tinggal siswa tidak dicatat, tidak ada rekapitulasi data terpusat, dan data satu cabang tidak dapat dilihat dari cabang lain. Kondisi ini membuat riwayat data lama berisiko hilang apabila kertas rusak, pendaftaran ganda antarcabang sulit terdeteksi, serta riwayat pembayaran seorang siswa memerlukan waktu lama untuk ditelusuri. Permasalahan serupa ditemukan pada sistem penagihan SPP. Tarif yang berlaku saat ini adalah Rp330.000 sampai Rp340.000 per bulan untuk SD, Rp350.000 untuk SMP, dan Rp380.000 untuk SMA kelas 10 dan 11, sedangkan siswa SMA kelas 12 menggunakan sistem paket. Besaran tarif tersebut tidak selalu diterapkan secara kaku, karena pengelola memberikan penyesuaian biaya bagi keluarga kurang mampu serta potongan khusus bagi siswa yang berstatus kakak-beradik. Dalam penagihan, staf administrasi memeriksa status pembayaran satu per satu pada buku catatan kemudian mengirimkan pesan tagihan melalui WhatsApp kepada masing-masing wali murid secara individual. Tidak ada pengingat otomatis dan tidak ada rekap tunggakan terpusat, sehingga penagihan berpotensi terlewat. Pada tingkat manajemen pusat, laporan pendapatan dari delapan cabang diserahkan dalam bentuk kertas tanpa berkas digital, lalu dicocokkan dengan catatan mutasi rekening bank satu per satu. Dengan cara ini, posisi keuangan seluruh cabang tidak dapat dipantau secara langsung, dan hasil rekap sangat bergantung pada ketelitian pencatatan di tiap cabang.

Persoalan operasional berikutnya berkaitan dengan pembagian siswa ke kelas dan pengaturan jadwal tentor. Setiap jenjang pendidikan memiliki batas kapasitas siswa per kelas yang berbeda, mulai dari 5 siswa untuk SD kelas 1, 6-7 siswa untuk SD kelas 2, 8-10 siswa untuk SD kelas 3 sampai 6, 10-14 siswa untuk SMP, hingga 12-14 siswa untuk SMA tergantung ukuran ruang kelas di masing-masing cabang. Cabang terbesar tercatat dapat menampung hingga sekitar 400 siswa, sehingga koordinasi penempatan siswa dan tentor tanpa sistem terpusat menjadi sangat rumit untuk dikendalikan. Dalam operasionalnya, pernah terjadi kondisi jadwal ganda ketika seorang tentor dijadwalkan mengajar di dua cabang berbeda pada waktu yang bersamaan, karena koordinasi hanya berjalan melalui grup percakapan WhatsApp. Di samping itu, jumlah kelas yang diampu setiap tentor tidak dapat dipantau secara visual, sehingga pengontrolan distribusi beban mengajar menjadi sulit dan sempat memunculkan keluhan mengenai ketidakmerataan pembagian jadwal bimbingan antartentor.

Menyikapi berbagai kendala operasional tersebut, pengembangan prototipe sistem informasi manajemen berbasis web menjadi langkah penyelesaian yang tepat bagi Bimbel Artha. Sistem berbasis web memungkinkan data operasional dari delapan cabang terhubung langsung ke satu basis data terpusat, sehingga pengelola di tingkat pusat dapat memantau kondisi keuangan, jumlah siswa aktif, dan kegiatan cabang secara langsung. Penyimpanan data secara digital sekaligus menjaga riwayat data tetap terjaga ketika staf administrasi berganti, yang menurut pengelola cukup sering terjadi di cabang. Prototipe yang dikembangkan dalam Tugas Akhir ini memuat modul pendaftaran yang mengunci penambahan siswa apabila kapasitas kelas telah penuh, modul kasir yang mencatat pembayaran SPP dan memicu pengingat jatuh tempo ke WhatsApp wali murid, modul penjadwalan tentor yang mendeteksi potensi jadwal ganda serta menampilkan beban jam mengajar, dan dasbor pimpinan untuk mempermudah pencocokan penerimaan kas dengan catatan mutasi rekening bank dari delapan cabang.

Sejumlah penelitian terdahulu menunjukkan bahwa pengembangan sistem informasi mampu menangani permasalahan serupa pada lembaga pendidikan nonformal. Ramadhan (2021) membangun sistem informasi untuk Bimbel Indo Prestasi yang mengotomatisasi pencatatan data siswa, pendaftaran, dan pembayaran SPP guna menggantikan pembukuan manual. Maliki dkk. (2024) merancang sistem berbasis web pada Bimbel BNF yang mengintegrasikan pengelolaan data siswa, guru, kelas, jadwal, dan pembayaran. Barizi dkk. (2023) merancang sistem administrasi berbasis desktop pada sekolah kursus musik yang menyatukan modul pembayaran dan penjadwalan dalam satu platform. Thiovanda (2026) membangun sistem pencatatan penjadwalan dan pembayaran les berbasis web pada Jia Jia Education guna mengurangi benturan jadwal dan mempercepat pengelolaan transaksi. Safitri dkk. (2026) mengembangkan sistem informasi manajemen Bimbel Ilman Nafi dengan fitur notifikasi otomatis melalui WhatsApp untuk penagihan SPP dan komunikasi antara pengelola, tentor, dan wali murid. Seluruh penelitian tersebut menjadi acuan fungsional bagi modul-modul yang dikembangkan dalam prototipe ini. Akan tetapi, Bimbel Artha memiliki kebutuhan tambahan yang belum dibahas pada penelitian-penelitian tersebut, yaitu pengelolaan operasional delapan cabang secara bersamaan dengan pemantauan terpusat oleh pimpinan lembaga.

Dalam pelaksanaan Tugas Akhir ini, metodologi Personal Extreme Programming (PxP) dipilih sebagai kerangka kerja pengembangan prototipe perangkat lunak. PxP merupakan turunan dari Extreme Programming yang dirancang khusus untuk pengembang tunggal, memungkinkan satu orang menangani seluruh proses mulai dari eksplorasi kebutuhan hingga pengujian sistem (Fikri & Arthawan, 2020; Sidiq dkk., 2025). Metode ini menekankan iterasi pendek, pengembangan fitur secara bertahap berdasarkan prioritas kebutuhan pengguna, dan penyempurnaan prototipe berdasarkan masukan langsung dari mitra di setiap akhir siklus (Ramadhan, 2026). Fleksibilitas PxP sangat sesuai dengan karakteristik Tugas Akhir ini, karena mitra dapat memberikan masukan secara rutin tanpa harus terlibat secara teknis, sehingga cocok dengan keterbatasan waktu pengelola yang menjalankan operasional delapan cabang secara bersamaan. PxP juga mengedepankan prinsip kesederhanaan dan desain yang berkembang seiring iterasi, tanpa mengorbankan kualitas sistem secara keseluruhan (Apriyanti dkk., 2024). Dengan demikian, penggunaan metode PxP mendukung kolaborasi yang praktis antara peneliti dan mitra serta mendorong pengembangan prototipe yang benar-benar sesuai dengan kebutuhan operasional Bimbel Artha.

Berdasarkan keseluruhan uraian permasalahan dan landasan tersebut, Tugas Akhir ini diarahkan untuk merancang prototipe sistem informasi manajemen operasional terintegrasi berbasis web multipengguna dengan metode Personal Extreme Programming (PxP), menggunakan Bimbingan Belajar Artha Balikpapan sebagai mitra pengembangan.

---

## 1.2 Rumusan Masalah

Berdasarkan permasalahan yang telah dipaparkan pada latar belakang, rumusan masalah dalam Tugas Akhir ini dijabarkan ke dalam beberapa pertanyaan penelitian sebagai berikut:

1. Bagaimana merancang prototipe modul pendaftaran siswa digital yang menggantikan sistem buku besar kertas di delapan cabang, serta dilengkapi dengan pengelolaan batas kapasitas kelas secara otomatis?
2. Bagaimana merancang prototipe modul kasir dan pembayaran SPP yang mencatat riwayat transaksi secara digital serta mengirimkan pengingat jatuh tempo kepada wali murid melalui WhatsApp?
3. Bagaimana merancang prototipe modul penjadwalan tentor yang mendeteksi potensi bentrok jadwal secara otomatis dan menyajikan visualisasi beban mengajar seluruh tentor lintas cabang?
4. Bagaimana merancang prototipe dasbor terpusat bagi Super Admin yang menyajikan ringkasan pendapatan, jumlah siswa, dan perbandingan kinerja delapan cabang secara _real-time_, serta memfasilitasi pencocokan laporan pendapatan dengan catatan mutasi rekening bank?
5. Bagaimana tingkat kesesuaian prototipe yang dirancang dengan kebutuhan fungsional mitra, berdasarkan hasil pengujian _Black Box Testing_ dan _User Acceptance Testing_ (UAT) bersama pengelola Bimbel Artha?

---

## 1.3 Tujuan

Tujuan dari pelaksanaan Tugas Akhir ini adalah merancang prototipe sistem informasi manajemen operasional berbasis web untuk Bimbel Artha Balikpapan yang mencakup modul pendaftaran siswa digital dengan pengelolaan kapasitas kelas terpusat, modul kasir dan pembayaran SPP dengan notifikasi jatuh tempo melalui WhatsApp, modul penjadwalan tentor dengan deteksi bentrok jadwal otomatis, serta dasbor Super Admin untuk pemantauan kinerja delapan cabang secara _real-time_ dan pencocokan laporan keuangan dengan mutasi rekening bank.

---

## 1.4 Batasan Rancangan

Agar prototipe dapat diselesaikan secara optimal dalam batas waktu pelaksanaan Tugas Akhir, ruang lingkup rancangan dibatasi sebagai berikut:

1. Prototipe berfokus pada dasbor manajemen operasional internal dengan dua peran pengguna, yaitu Admin Cabang (staf operasional di masing-masing cabang) dan Super Admin (pimpinan pusat). Pembatasan peran ini ditetapkan setelah mitra meminta pengembangan difokuskan pada pengelolaan pendaftaran dan kapasitas kelas, karena kesiapan literasi digital staf cabang terhadap sistem yang lebih kompleks masih perlu diperhatikan. Tentor tidak memiliki hak akses ke dalam sistem, dan pembagian jadwal disampaikan melalui lembar jadwal cetak.
2. Fitur pembelajaran daring, bank soal, dan pelaporan perkembangan nilai akademik siswa tidak termasuk ke dalam ruang lingkup, karena fokus utama prototipe adalah efisiensi administrasi operasional.
3. Prototipe tidak mengintegrasikan _payment gateway_ pihak ketiga. Pembayaran SPP melalui transfer bank diverifikasi secara manual oleh Admin Cabang berdasarkan bukti transfer yang diunggah ke sistem.
4. Notifikasi kepada wali murid dikirimkan melalui tautan WhatsApp yang diakses langsung dari sistem, dan tidak melalui surel, karena nomor WhatsApp dinilai lebih aktif digunakan dan lebih cepat dibaca oleh wali murid.
5. Prototipe tidak mencakup pembangunan aplikasi seluler. Seluruh akses operasional dilakukan melalui antarmuka web yang responsif pada peramban komputer maupun gawai.
6. Data transaksi dan pembukuan fisik sebelum prototipe dioperasikan tidak dimigrasikan ke dalam basis data baru. Prototipe mulai beroperasi dengan data baru sejak tanggal penerapan resmi di mitra.
7. Pengembangan sisi _backend_ menggunakan _framework_ Laravel (PHP) dengan basis data MySQL yang menyediakan antarmuka RESTful API, sedangkan sisi _frontend_ dasbor menggunakan _framework_ Next.js (React).

---

## 1.5 Manfaat

Pengembangan prototipe ini memberikan manfaat konkret bagi tiga pihak yang terlibat langsung dalam pelaksanaan Tugas Akhir ini.

Bagi mitra, yaitu Bimbel Artha Balikpapan, prototipe menghadirkan sistem pencatatan pendaftaran siswa dan riwayat pembayaran SPP secara digital yang menggantikan buku besar kertas yang digunakan di delapan cabang. Manajemen pusat memperoleh kemampuan memantau kondisi keuangan, jumlah siswa aktif, dan kinerja masing-masing cabang secara langsung melalui satu dasbor terpusat. Selain itu, prototipe memberikan mitigasi terhadap risiko kehilangan data akibat pergantian staf administrasi yang cukup sering terjadi di cabang, serta membantu penjadwalan tentor agar terhindar dari bentrok jadwal antarcabang.

Bagi pengguna langsung sistem, yaitu Admin Cabang dan Super Admin, prototipe mempercepat alur kerja operasional harian yang selama ini dilakukan secara manual. Admin Cabang tidak perlu lagi memeriksa buku catatan satu per satu untuk memastikan status pembayaran, karena sistem menyajikan informasi tersebut secara langsung. Super Admin dapat mencocokkan laporan pendapatan dari delapan cabang dengan catatan mutasi rekening bank langsung dari dasbor, tanpa harus menunggu berkas laporan fisik dari setiap cabang.

Bagi peneliti, Tugas Akhir ini memberikan pengalaman langsung dalam menerapkan metode Personal Extreme Programming (PxP) pada pengembangan sistem berskala menengah dengan mitra yang proses bisnisnya masih berkembang. Penerapan PxP pada bimbingan belajar multicabang memperluas variasi studi kasus rekayasa perangkat lunak yang selama ini lebih banyak dijumpai pada domain instansi pemerintahan atau sanggar seni, sekaligus memperkaya kajian transformasi digital pada sektor pendidikan nonformal di Indonesia.

---

## 1.6 Potensi Dampak Fungsional/Komersial

Pada lingkup fungsional, prototipe ini diharapkan menjadi fondasi operasional digital bagi Bimbel Artha yang selama ini bergantung sepenuhnya pada pencatatan manual. Apabila prototipe diterapkan secara penuh di delapan cabang, pengelola dapat memangkas waktu rekapitulasi laporan keuangan bulanan yang saat ini dilakukan secara manual dari masing-masing cabang. Pengurangan beban kerja administrasi tersebut memungkinkan staf cabang untuk lebih berfokus pada pelayanan peserta didik, bukan pada pencatatan yang berulang dan rentan kesalahan. Prototipe juga memfasilitasi deteksi dini terhadap tunggakan SPP dan bentrok jadwal tentor yang selama ini kerap terlambat diketahui, sehingga permasalahan operasional dapat ditangani lebih cepat sebelum berdampak pada kualitas layanan.

Pada lingkup komersial, rancangan antarmuka dan arsitektur sistem yang dikembangkan dalam prototipe ini dapat dikembangkan lebih lanjut menjadi produk perangkat lunak berbasis _Software as a Service_ (SaaS) yang ditawarkan kepada lembaga bimbingan belajar lain di Kalimantan Timur maupun nasional. Permintaan terhadap sistem manajemen operasional bimbel yang terjangkau dan mudah digunakan cukup tinggi, mengingat sebagian besar lembaga sejenis masih beroperasi secara manual seperti kondisi Bimbel Artha saat ini. Modul multicabang yang tersedia dalam prototipe ini merupakan keunggulan kompetitif yang belum banyak ditemukan pada solusi serupa di segmen pendidikan nonformal skala menengah.

---

## 1.7 Kerangka Tugas Akhir

Berikut adalah Diagram _Fishbone_ untuk Kerangka Tugas Akhir ini. Diagram tersebut menggambarkan hubungan antara permasalahan yang dihadapi, faktor penyebab yang teridentifikasi, serta solusi yang diharapkan dari prototipe yang dirancang.

![Gambar 1. 1 Diagram Fishbone Kerangka Pemikiran Penelitian](Gambar%201.1%20Diagram%20Fishbone%20Bimbel%20Artha.png)

<p align="center"><b>Gambar 1. 1 Diagram Fishbone Kerangka Pemikiran Penelitian</b></p>

Gambar 1.1 merupakan kerangka pemikiran yang menggambarkan pentingnya pengembangan prototipe sistem informasi manajemen terpusat untuk operasional multicabang Bimbel Artha Balikpapan. Diagram ini disusun berdasarkan pendekatan _fishbone_ atau sebab-akibat, yang menunjukkan empat faktor utama penyebab permasalahan, yaitu _Man_, _Machine_, _Material_, dan _Method_.

Pada kategori _Man_, permasalahan yang dihadapi adalah staf administrasi di kantor cabang kerap berganti, sehingga pemahaman terhadap alur kerja dan pencatatan manual tidak berkesinambungan. Selain itu, pimpinan pusat kesulitan memantau aktivitas operasional harian di delapan cabang secara bersamaan karena tidak tersedia media pemantauan langsung.

Faktor _Machine_ mengindikasikan bahwa belum tersedia sistem informasi manajemen berbasis web yang menghubungkan seluruh cabang secara _real-time_. Tidak adanya sistem ini juga berarti belum ada modul penjadwalan yang dapat mendeteksi bentrok jadwal tentor antarcabang secara otomatis, maupun fitur pengingat jatuh tempo pembayaran SPP ke WhatsApp wali murid.

Pada faktor _Material_, seluruh pencatatan pendaftaran siswa dan riwayat pembayaran SPP masih menggunakan buku besar kertas A4 yang tersimpan secara terpisah di setiap cabang. Kondisi ini membuat data tidak dapat diakses lintas cabang, berkas rentan hilang atau rusak, serta data alamat siswa tidak lengkap sehingga sebaran geografis peserta didik tidak bisa dianalisis.

Sedangkan pada faktor _Method_, pengendalian kapasitas kelas masih dilakukan dengan menghitung baris di buku kertas sehingga rawan _overcapacity_. Penagihan SPP dikerjakan satu per satu melalui pesan WhatsApp pribadi dan berisiko terlewat, sedangkan pencocokan laporan kas cabang dengan mutasi bank masih dilakukan secara manual dan membutuhkan waktu yang cukup lama.

Berdasarkan identifikasi dari keempat faktor tersebut, dapat disimpulkan bahwa inti permasalahan adalah belum adanya sistem informasi manajemen terpusat yang mampu mendukung pencatatan, penjadwalan, penagihan, dan pelaporan operasional delapan cabang secara efisien dan akurat. Oleh karena itu, dalam Tugas Akhir ini akan dikembangkan prototipe sistem informasi manajemen operasional multicabang sebagai solusi digital yang mengintegrasikan seluruh data cabang ke dalam satu basis data terpusat dan mendukung transformasi pengelolaan Bimbel Artha Balikpapan.

Pengembangan prototipe tersebut dirancang menggunakan metodologi Personal Extreme Programming (PxP) yang terdiri atas tujuh tahapan terstruktur:

1. **Analisis Kebutuhan (_Requirements_)**: Kebutuhan fungsional dirumuskan dari hasil wawancara, observasi, dan penelaahan dokumen operasional. Tahap ini menghasilkan daftar kebutuhan fungsional dalam format kisah pengguna (_user stories_) yang dilengkapi dengan kriteria penerimaan (_acceptance criteria_) sebagai tolok ukur pengujian prototipe.
2. **Perencanaan (_Planning_)**: Peneliti dan mitra menyusun rencana rilis global serta jadwal pengembangan prototipe. Seluruh kisah pengguna diprioritaskan berdasarkan urgensi kebutuhan operasional dan diberi estimasi bobot kerja, lalu dibagi ke dalam beberapa siklus rilis yang terukur bagi pengembang tunggal.
3. **Inisialisasi Iterasi (_Iteration Initialization_)**: Pada awal setiap siklus iterasi, peneliti memilih sejumlah kisah pengguna yang akan dikerjakan pada siklus berjalan. Kisah pengguna tersebut dijabarkan menjadi daftar tugas teknis beserta estimasi rentang waktu penyelesaiannya.
4. **Perancangan (_Design_)**: Arsitektur dan pemodelan prototipe untuk modul yang dikerjakan pada iterasi aktif dirancang melalui pembuatan diagram _Unified Modeling Language_ (UML) seperti _use case diagram_, perancangan skema basis data (_Entity Relationship Diagram_ / ERD), serta pembuatan _wireframe_ antarmuka dasbor Admin Cabang dan Super Admin.
5. **Implementasi (_Implementation_)**: Penulisan kode program dilakukan secara modular menggunakan Next.js pada sisi _frontend_ dan Laravel RESTful API pada sisi _backend_. Tahapan ini disertai pengujian unit (_unit testing_) dan penataan ulang kode (_refactoring_) guna menjaga kebersihan struktur perangkat lunak.
6. **Pengujian Prototipe (_System Testing_)**: Setiap modul yang telah selesai dibangun diuji secara menyeluruh menggunakan metode _Black Box Testing_. Pengujian ini memvalidasi bahwa seluruh fungsi berjalan sesuai spesifikasi dan kriteria penerimaan sebelum diserahkan kepada mitra.
7. **Retrospektif (_Retrospective_)**: Pada akhir setiap iterasi, peneliti dan mitra melakukan evaluasi bersama untuk meninjau ketercapaian fitur serta membandingkan estimasi waktu dengan realisasi pengerjaan. Seluruh masukan mitra didokumentasikan sebagai bahan perbaikan pada inisialisasi iterasi berikutnya.

---

## Referensi yang Disitasi pada Bab 1

- Apriyanti, N., Fitri Ana Wati, S., & Rezha Efrat Najaf, A. (2024). Pemanfaatan Metodologi PXP dan Pengujian User Acceptance Testing (UAT) dalam Pengembangan Website E-Kavling. _JATI (Jurnal Mahasiswa Teknik Informatika)_, 8(3), 3678-3686. https://doi.org/10.36040/jati.v8i3.9766
- Barizi, A., Anshary, N. B., & Sumarni, R. A. (2023). Perancangan Aplikasi Sistem Administrasi Sekolah Musik pada Sekolah Musik ABC Berbasis Java. _Jurnal Riset dan Aplikasi Mahasiswa Informatika (JRAMI)_, 4(2), 332-339.
- Fikri, A. M., & Arthawan, I. P. D. (2020). Rancang Bangun Sistem Informasi Buku Tamu pada Dinas Pemuda, Olahraga dan Pariwisata Kota Balikpapan dengan Metode Personal Extreme Programming. _Multitek Indonesia: Jurnal Ilmiah_, 14(2), 101-110.
- Maliki, I., Jaya, K., Lestari, G. C., Irawan, D., & Wasid, A. (2024). Perancangan Sistem Informasi Berbasis Web pada Bimbingan Belajar (Bimbel) "BNF". _Jurnal Informatika & Komputasi_, 18(2), 72-81.
- Pradana, M. R. A. (2024). Peran Teknologi Informasi dalam Meningkatkan Efektivitas Manajemen Pendidikan di Sekolah. _Jurnal Review Pendidikan dan Pengajaran (JRPP)_, 7(3), 6855-6860. https://doi.org/10.31004/jrpp.v7i3.29286
- Ramadhan, F. (2026). Implementasi Personal Extreme Programming Dalam Perancangan Sistem Informasi Manajemen Keanggotaan Dan Pengaturan Jadwal Untuk Meningkatkan Efisiensi Operasional (Studi Kasus: Sanggar Senam Kurnia). _Journal of Information Systems and Business Technology (JISBET)_, 2(4), 1180-1187.
- Ramadhan, M., & Arifin, N. A. (2021). Sistem Informasi Bimbingan Belajar Indo Prestasi dan English For Communication. _Seminar Nasional Riset dan Inovasi Teknologi (SEMNAS RISTEK)_, 5(1), 1424-1429.
- Safitri, E. C. A., Listyorini, T., & Supriyati, E. (2026). Perancangan Sistem Informasi Manajemen Bimbingan Belajar Berbasis Web untuk Efisiensi Administrasi dan Komunikasi dengan Fitur Notifikasi Otomatis (Studi Kasus: Bimbel Ilman Nafi'). _JATI (Jurnal Mahasiswa Teknik Informatika)_, 10(2), 2345-2352.
- Sidiq, A. L., Marthasari, G. I., & Aminudin. (2025). Implementasi Metode Personal Extreme Programming pada Pengembangan Sistem Informasi Surat Menyurat (Studi Kasus: Dinas Pendidikan Pemuda dan Olahraga Kabupaten Tambrauw). _Jurnal Jaring SainTek_, 7(1), 35-46.
- Thiovanda, V. (2026). Perancangan Sistem Informasi Pencatatan Penjadwalan dan Pembayaran Les Berbasis Web. _Jurnal Ilmu Komputer dan Sistem Informasi_, 14(1).
- Tiana, I., & Gunanto, S. (2026). Perancangan dan Implementasi Sistem Informasi Bimbingan Belajar Berbasis Web Mobile Menggunakan Metode Waterfall. _JUKTISI (Jurnal Ilmiah Komputasi dan Teknologi Informasi)_, 4(3), 1631-1638.
- Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional, Pasal 26.
