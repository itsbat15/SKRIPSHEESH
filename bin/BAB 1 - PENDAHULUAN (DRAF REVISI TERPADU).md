# BAB 1

## PENDAHULUAN

Bab ini menguraikan dasar pengembangan prototipe sistem informasi manajemen operasional multicabang berbasis web pada Bimbingan Belajar Artha Balikpapan. Pembahasan mencakup latar belakang, rumusan masalah, tujuan, batasan rancangan, manfaat, potensi dampak fungsional dan komersial, serta kerangka pelaksanaan Tugas Akhir.

## 1.1 Latar Belakang

Bimbingan belajar diselenggarakan untuk mendukung kegiatan belajar siswa di luar pembelajaran sekolah. Dalam konteks pendidikan nonformal, layanan pendidikan dapat berfungsi sebagai penambah dan pelengkap pendidikan formal sebagaimana diatur dalam Undang-Undang Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional, Pasal 26 (Republik Indonesia, 2003). Penyelenggaraan layanan tersebut memerlukan pengelolaan administrasi yang mencakup data siswa, jadwal tentor, penempatan kelas, dan pembayaran biaya bimbingan. Keterkaitan kegiatan tersebut menjadi dasar perlunya pencatatan yang dapat digunakan untuk mendukung pelayanan harian serta penyusunan laporan lembaga.

Pengembangan sistem informasi berbasis web telah diterapkan untuk mendukung administrasi lembaga pendidikan nonformal. Gunawan dkk. (2025) mengembangkan sistem pada Bimbingan Belajar RSDC yang mencakup registrasi, jadwal, presensi, dan verifikasi pembayaran, sedangkan Fajriansyah dkk. (2026) mengintegrasikan pengelolaan siswa, tentor, jadwal, pembayaran, dan laporan pada Bimbingan Belajar Bee Hive. Pada administrasi keuangan, Abadi dkk. (2025) mengembangkan aplikasi pembayaran SPP dan penggajian guru, sementara Karpina dkk. (2025) mengembangkan pencatatan pembayaran kursus beserta rekap keuangannya. Penelitian tersebut memberikan contoh pengelolaan data operasional dalam sistem digital yang dapat dijadikan acuan sesuai kebutuhan lembaga.

Bimbingan Belajar (Bimbel) Artha Balikpapan merupakan mitra pengembangan dalam Tugas Akhir ini. Berdasarkan wawancara dengan pengelola, kegiatan layanan Bimbel Artha mencakup delapan cabang yang memerlukan pencatatan kegiatan serta pelaporan kepada pengelola pusat.[^W2][^W3] Jenjang layanan mencakup TK, SD, SMP, dan SMA, dengan ketersediaan layanan yang berbeda antarcabang, termasuk layanan TK atau kalistung yang menurut staf administrasi tidak diselenggarakan di Artha 3 dan Artha 6.[^W4F] Kegiatan operasionalnya melibatkan penerimaan siswa, penempatan pada sesi dan ruang, pengaturan tentor, serta pencatatan pembayaran. Cakupan tersebut menimbulkan kebutuhan untuk mengelola informasi berdasarkan cabang sekaligus menyediakan ringkasan bagi pengelola pusat.

Pada pencatatan administrasi, staf cabang menjelaskan bahwa data siswa dan pembayaran masih disimpan dalam buku. Pendaftaran dapat disampaikan secara langsung maupun melalui WhatsApp, kemudian dicatat oleh petugas sesuai informasi yang diperlukan.[^W4A] Ketentuan biaya berkaitan dengan jenjang dan sesi bimbingan, sedangkan potongan biaya bagi siswa yang bersaudara melibatkan keterangan dari wali murid.[^W4G][^W4A] Jatuh tempo pembayaran SPP mengikuti tanggal mulai bimbingan masing-masing siswa, dan keterlambatan ditindaklanjuti dengan menghubungi wali murid atau mengingatkan siswa.[^W4B] Berdasarkan alur tersebut, pencatatan digital diperlukan untuk menghubungkan identitas siswa, ketentuan biaya, hubungan saudara, dan riwayat pembayaran dalam informasi yang dapat ditelusuri oleh petugas berwenang.

Pada pelaporan penerimaan, staf administrasi menerangkan bahwa catatan pembayaran dan penerimaan harian dikumpulkan ke pusat, sedangkan buku pencatatan tetap disimpan di cabang. Rekap bulanan disusun terpisah dari pengumpulan penerimaan harian, sementara bukti pembayaran melalui transfer diteruskan kepada pengelola yang menangani penerimaan pusat.[^W4C] Dengan alur tersebut, pemeriksaan memerlukan keterkaitan antara transaksi siswa, catatan cabang, dan penerimaan di pusat. Kebutuhan sistem diarahkan pada penelusuran transaksi beserta status pemeriksaannya, sehingga catatan pembayaran dapat ditinjau berdasarkan cabang, siswa, dan periode. Pembayaran tunai dan transfer juga perlu dibedakan dalam pencatatan karena bukti penerimaan yang diperiksa mengikuti mekanisme pembayaran masing-masing.

Pengelolaan kelas memerlukan informasi mengenai ruang, sesi, dan jumlah siswa yang ditempatkan. Wawancara dengan pengelola serta staf administrasi menunjukkan bahwa kapasitas berbeda menurut ruang dan jenjang, dan penempatan siswa dapat disesuaikan ke ruang atau sesi lain.[^W3K][^W4D] Pembagian jadwal tentor juga telah dilakukan oleh petugas di cabang sesuai pengaturan kegiatan bimbingan.[^W4E] Informasi tersebut menjadi dasar rancangan pencatatan keterisian kelas serta jadwal tentor lintas cabang. Peringatan kapasitas dan waktu yang tumpang tindih direncanakan untuk mendukung pemeriksaan penempatan dan penugasan sebelum keputusan operasional ditetapkan.

Penelitian tentang pengelolaan pusat dan cabang menyediakan acuan untuk pembagian kewenangan serta penyajian laporan. Ahadi dkk. (2025) mengembangkan sistem manajemen hotel dengan fungsi pengguna pemilik dan penanggung jawab cabang serta laporan berdasarkan cabang. Ramadhan dan Widodo (2026), melalui studi akuntansi pada UMKM Rams Dimsum, membahas pemisahan pencatatan pusat dan cabang serta kebutuhan pelaporan transaksi yang terdokumentasi. Pada administrasi pendidikan, Hendri dkk. (2025) menyusun rancangan antarmuka pencatatan penerimaan SPP untuk mendukung penelusuran catatan pembayaran. Hasil penelitian tersebut digunakan sebagai acuan yang saling melengkapi dengan memperhatikan perbedaan objek, proses bisnis, dan bentuk hasil yang dihasilkan.

Pada pengaturan kegiatan, Khafidhoh dkk. (2026) mengembangkan sistem penjadwalan bimbingan belajar menggunakan algoritma genetika, sedangkan Kabisatullah dan Noprisson (2026) menerapkan batasan kapasitas serta waktu yang tidak tumpang tindih dalam aplikasi manajemen ruang rapat. Pada aspek penerimaan, Sudirman dan Tristianti (2021) mengembangkan sistem pengendalian kas bank dengan metode rekonsiliasi. Penelitian tersebut memberikan pertimbangan mengenai aturan penjadwalan, kapasitas, dan pencocokan catatan transaksi. Penerapannya pada Bimbel Artha disesuaikan menjadi pencatatan jadwal dengan peringatan, informasi keterisian kelas, serta dukungan pemeriksaan penerimaan pembayaran sesuai kewenangan pengguna.

Berdasarkan kebutuhan mitra dan penelitian yang ditelaah, prototipe diarahkan pada integrasi pencatatan operasional cabang dengan pemantauan pusat. Fungsi yang direncanakan meliputi pencatatan siswa, pengaturan kelas dan kapasitas, pembayaran SPP, jadwal tentor, serta dasbor rekap penerimaan menurut cabang dan periode. Admin Cabang mengelola data sesuai kewenangan cabangnya, sedangkan Super Admin meninjau informasi seluruh cabang dan menangani pemeriksaan yang menjadi kewenangan pusat. Dukungan pengingat pembayaran disediakan melalui tautan WhatsApp yang dibuka oleh petugas. Kontribusi pengembangan terletak pada penyesuaian fungsi-fungsi tersebut dengan keterkaitan proses pendaftaran, penempatan kelas, pembayaran, dan pelaporan pada operasional Bimbel Artha.

Metode *Personal Extreme Programming* (PxP) dipilih sebagai kerangka pengembangan prototipe. Dzhurov dkk. (2009) menjelaskan PxP sebagai proses pengembangan individual yang mempertahankan prinsip *Personal Software Process* dan mengadopsi praktik *Extreme Programming*, termasuk pengujian berkelanjutan, pencatatan pekerjaan, dan retrospektif. Proses tersebut menyediakan dasar untuk membagi pekerjaan, memantau pelaksanaan tugas, serta mengevaluasi hasil pengembangan. Contoh penerapan PxP pada website transaksi ditunjukkan oleh Apriyanti dkk. (2024), yang melengkapinya dengan pengujian fungsional dan penerimaan pengguna. Sumber tersebut digunakan untuk mendukung penyusunan proses pengembangan dan evaluasi yang akan diterapkan pada Bimbel Artha.

Pemilihan PxP dipertimbangkan berdasarkan pengembangan oleh satu orang, pembagian fungsi ke dalam modul, batas waktu Tugas Akhir, serta kebutuhan untuk meninjau rincian proses bisnis secara bertahap. Pencatatan estimasi dan realisasi waktu, hasil pengujian, serta cacat perangkat lunak direncanakan agar kemajuan setiap iterasi dapat dievaluasi. Peninjauan modul bersama perwakilan mitra direncanakan untuk memperoleh masukan terhadap alur yang telah diimplementasikan, dengan pihak dan jadwal evaluasi ditetapkan pada tahap perencanaan. Dengan demikian, kesesuaian PxP ditinjau dari proses kerja yang akan dijalankan dan bukti pelaksanaannya. Perbandingan tahapan, keterlibatan pengguna, dan kebutuhan sumber daya dengan metode alternatif dijabarkan pada Bab 2 untuk melengkapi dasar pemilihan metode.

Melalui Tugas Akhir ini, akan dikembangkan prototipe perangkat lunak untuk mendukung pencatatan serta pemantauan operasional multicabang Bimbel Artha Balikpapan. Kesesuaian fungsi direncanakan diuji menggunakan *black box testing*, sedangkan penerimaan pengguna dievaluasi melalui *User Acceptance Testing* (UAT) bersama perwakilan mitra. Hasil pengujian dan evaluasi digunakan untuk mengidentifikasi fungsi yang telah memenuhi kebutuhan serta bagian yang masih memerlukan perbaikan. Prototipe diharapkan menjadi dasar penerapan pencatatan digital yang sesuai dengan proses operasional dan kewenangan pengguna pada Bimbel Artha.

## 1.2 Rumusan Masalah

Rumusan masalah disusun berdasarkan kebutuhan integrasi pencatatan cabang dan pemantauan pusat. Pertanyaan berikut menjadi dasar pembangunan serta evaluasi prototipe.

1. Bagaimana merancang dan membangun prototipe sistem informasi manajemen operasional multicabang berbasis web menggunakan PxP untuk mengintegrasikan pencatatan siswa, kapasitas kelas, pembayaran SPP, dan jadwal tentor pada Bimbel Artha Balikpapan?
2. Bagaimana menyediakan pemantauan terpusat dengan pembatasan akses berdasarkan cabang dan penelusuran transaksi untuk mendukung pemeriksaan penerimaan pembayaran?
3. Bagaimana kesesuaian fungsi dan penerimaan pengguna terhadap prototipe berdasarkan hasil *black box testing* dan UAT bersama perwakilan mitra?

## 1.3 Tujuan

Tujuan Tugas Akhir diturunkan dari rumusan masalah yang telah ditetapkan. Ketercapaiannya ditinjau melalui fungsi yang dihasilkan, hasil pengujian, dan evaluasi pengguna.

1. Merancang dan membangun prototipe sistem informasi manajemen operasional multicabang berbasis web menggunakan PxP yang mengintegrasikan pencatatan siswa, kapasitas kelas, pembayaran SPP, dan jadwal tentor pada Bimbel Artha Balikpapan.
2. Menghasilkan dasbor pemantauan pusat, pembatasan akses berdasarkan cabang, dan penelusuran transaksi yang mendukung pemeriksaan penerimaan pembayaran.
3. Mengevaluasi kesesuaian fungsi dan penerimaan pengguna terhadap prototipe melalui *black box testing* dan UAT bersama perwakilan mitra.

## 1.4 Batasan Rancangan

Rancangan difokuskan pada administrasi operasional internal dan dukungan pemantauan pusat. Pembatasan berikut digunakan untuk menjaga kesesuaian antara fungsi yang dikembangkan, waktu pengerjaan, dan evaluasi yang direncanakan.

1. Prototipe dirancang untuk struktur delapan cabang Bimbel Artha dengan dua peran pengguna, yaitu Admin Cabang dan Super Admin. Admin Cabang mengelola data sesuai kewenangan cabangnya, sedangkan Super Admin meninjau data seluruh cabang dan mengelola pengaturan pusat.
2. Fungsi utama mencakup pencatatan siswa dan kontak wali, data tentor, kelas dan kapasitas, jadwal, pembayaran SPP, serta laporan penerimaan. Ketentuan biaya, hubungan saudara, dan penyesuaian biaya dicatat sebagai dasar penelusuran administrasi pembayaran.
3. Kapasitas ditetapkan berdasarkan ruang, kelas, dan sesi sesuai kebijakan mitra. Informasi keterisian dan peringatan diberikan ketika penempatan mendekati atau melampaui ambang yang ditetapkan, kemudian keputusan penanganannya dicatat oleh pengguna yang berwenang.
4. Jadwal tentor dimasukkan oleh petugas dan diperiksa terhadap waktu penugasan tentor yang sama di seluruh cabang. Ringkasan jam penugasan disajikan berdasarkan jadwal yang tercatat untuk membantu peninjauan distribusi tugas. Penanganan peringatan mengikuti kewenangan pengelola, sedangkan penyusunan jadwal otomatis menggunakan algoritma optimasi berada di luar ruang lingkup.
5. Pembayaran mencakup pencatatan tunai dan transfer bank tanpa integrasi *payment gateway* pada rancangan ini. Admin Cabang menghimpun data transaksi dan dokumen pendukung, sedangkan konfirmasi penerimaan transfer direncanakan dilakukan oleh Super Admin yang memiliki kewenangan memeriksa mutasi rekening.
6. Dukungan rekonsiliasi dibatasi pada penelusuran transaksi SPP, rekap penerimaan dan setoran tunai cabang, serta pencocokan transfer dengan catatan mutasi yang diperiksa petugas berwenang. Hasil pemeriksaan dibedakan antara transaksi yang menunggu konfirmasi dan transaksi yang telah dikonfirmasi, dengan koreksi yang dapat ditelusuri.
7. Prototipe tidak melakukan koneksi otomatis ke rekening bank atau menyusun laporan keuangan lengkap beserta jurnal penyesuaian. Pemeriksaan penerimaan tetap dilakukan berdasarkan dokumen dan akses rekening yang menjadi kewenangan mitra.
8. Pengingat pembayaran disiapkan berdasarkan tanggal jatuh tempo masing-masing siswa dan disampaikan melalui tautan WhatsApp yang dibuka oleh petugas. Pengiriman pesan memerlukan tindakan petugas dan tidak mencakup pengiriman otomatis terjadwal melalui WhatsApp API.
9. Tentor, siswa, dan wali murid tidak diberikan akun pada prototipe ini. Pembelajaran daring, bank soal, pelaporan nilai akademik, pengelolaan layanan privat, dan penggajian tentor berada di luar ruang lingkup pengembangan.
10. Prototipe berupa aplikasi web responsif dengan Laravel pada sisi layanan, MySQL sebagai basis data, dan Next.js pada sisi antarmuka. Pertukaran data direncanakan menggunakan RESTful API, sedangkan aplikasi seluler khusus tidak dikembangkan.
11. Pemantauan pusat menampilkan data yang telah tersimpan dan dimuat dari sistem melalui jaringan yang tersedia. Ringkasan disajikan berdasarkan cabang dan periode, dengan pembaruan mengikuti pencatatan serta pemeriksaan transaksi oleh petugas.
12. Migrasi menyeluruh atas transaksi historis tidak termasuk ruang lingkup. Data induk, status awal pembayaran, dan data transaksi yang diperlukan untuk pengujian disiapkan bersama mitra agar skenario siswa lama dan siswa baru dapat dievaluasi.
13. Pengujian mencakup fungsi utama, kewenangan akses cabang dan pusat, aturan kapasitas, peringatan jadwal, serta alur pemeriksaan pembayaran. Data uji mewakili struktur delapan cabang, sedangkan lokasi, pengguna, dan periode pengujian bersama mitra ditetapkan dalam rencana pengujian.

## 1.5 Manfaat

Bagi Bimbel Artha Balikpapan, prototipe diharapkan menyediakan pencatatan siswa, kelas, jadwal, dan pembayaran yang dapat ditelusuri berdasarkan cabang. Pengelola pusat diharapkan memperoleh ringkasan operasional untuk mendukung pemeriksaan laporan dan koordinasi dengan cabang.

Bagi Admin Cabang, prototipe diharapkan membantu pencarian riwayat siswa dan pembayaran serta pemeriksaan keterisian kelas. Informasi tersebut dapat digunakan sebagai dukungan pelayanan pendaftaran, penempatan siswa, dan tindak lanjut pembayaran sesuai kewenangan petugas.

Bagi Super Admin, prototipe diharapkan menyediakan rekap lintas cabang dan status pemeriksaan penerimaan dalam satu sistem. Penelusuran transaksi diharapkan mendukung pemeriksaan catatan cabang, konfirmasi penerimaan, dan penanganan transaksi yang memerlukan koreksi.

Bagi pengembangan keilmuan, Tugas Akhir ini diharapkan menyediakan dokumentasi penerapan PxP pada administrasi bimbingan belajar multicabang. Dokumentasi kebutuhan, pelaksanaan iterasi, pengujian, dan evaluasi dapat digunakan sebagai bahan pembelajaran mengenai kesesuaian proses pengembangan individual dengan kebutuhan pengguna pada kasus tersebut.

## 1.6 Potensi Dampak Fungsional/Komersial

Pada aspek fungsional, prototipe berpotensi mendukung keterlacakan pembayaran, penyusunan rekap cabang, dan koordinasi penempatan kelas. Penerapannya diharapkan membantu petugas meninjau informasi operasional dari data yang tersimpan, dengan hasil yang bergantung pada kelengkapan input serta ketepatan prosedur pemeriksaan. Potensi perubahan waktu kerja dan kesalahan pencatatan dapat menjadi bahan evaluasi lanjutan setelah prototipe digunakan dalam periode yang memadai.

Pada aspek komersial, rancangan sistem berpotensi dikembangkan lebih lanjut untuk lembaga bimbingan belajar yang memiliki kebutuhan operasional serupa. Pengembangan menjadi layanan berlangganan memerlukan kajian kebutuhan pengguna, biaya operasional, keamanan data, dan dukungan pemeliharaan. Kajian kelayakan usaha tersebut berada di luar lingkup Tugas Akhir ini dan dapat dilakukan setelah kesesuaian fungsi prototipe dievaluasi bersama mitra.

## 1.7 Kerangka Tugas Akhir

Kerangka Tugas Akhir menghubungkan identifikasi kebutuhan, pengembangan prototipe, dan evaluasi bersama mitra. Pengumpulan data dilakukan sebagai langkah awal sebelum tujuh tahap PxP menurut Dzhurov dkk. (2009). Dokumentasi pekerjaan dan hasil pengujian digunakan untuk mendukung evaluasi iterasi serta penyusunan laporan.

1. Identifikasi masalah dan pengumpulan data dilakukan melalui penelaahan wawancara, dokumen operasional, dan klarifikasi kepada pihak mitra. Hasilnya digunakan untuk memetakan proses pendaftaran, penempatan kelas, pembayaran, penjadwalan, dan pelaporan yang akan didukung prototipe.
2. Pada tahap kebutuhan (*requirements*), hasil pengumpulan data dirumuskan menjadi kebutuhan fungsional dan nonfungsional. Kriteria penerimaan ditetapkan untuk setiap fungsi agar hasil pengembangan dapat diuji dan ditelusuri ke kebutuhan awal.
3. Pada tahap perencanaan (*planning*), kebutuhan diuraikan menjadi tugas yang diprioritaskan dan diberi estimasi waktu. Perwakilan evaluator, jadwal peninjauan modul, data awal, dan sarana pengujian direncanakan bersama mitra.
4. Pada tahap inisialisasi iterasi (*iteration initialization*), tugas dipilih sesuai prioritas serta kapasitas waktu pengembangan. Target hasil iterasi dicatat untuk dibandingkan dengan realisasi pekerjaan pada akhir siklus.
5. Pada tahap perancangan (*design*), model data, kewenangan pengguna, aturan pembayaran, kapasitas, jadwal, dan antarmuka dirancang sesuai tugas iterasi. Pemodelan sistem serta rancangan antarmuka digunakan untuk memeriksa keterkaitan alur sebelum implementasi.
6. Pada tahap implementasi (*implementation*), pengujian unit disiapkan berdasarkan perilaku yang diharapkan, kemudian kode dikembangkan dan diperbaiki melalui *refactoring*. Estimasi, realisasi waktu, cacat, dan hasil pengujian dicatat untuk mendukung evaluasi pekerjaan.
7. Pada tahap pengujian sistem (*system testing*), fungsi dan hubungan antarmodul diuji menggunakan skenario *black box testing*. Skenario mencakup penggunaan normal, input tidak valid, pembatasan akses lintas cabang, kapasitas, konflik waktu, serta pemeriksaan pembayaran.
8. Pada tahap retrospektif (*retrospective*), estimasi dan realisasi pekerjaan, temuan cacat, serta usulan perbaikan proses dianalisis oleh pengembang. Umpan balik dari peninjauan modul bersama mitra digunakan untuk memperbarui kebutuhan atau prioritas tugas sesuai jadwal evaluasi yang disepakati.

Iterasi berikutnya dimulai apabila masih terdapat kebutuhan atau perbaikan yang belum diselesaikan. Setelah fungsi pada versi rilis memenuhi kriteria pengujian, UAT dilakukan bersama perwakilan pengguna cabang dan pusat untuk menilai penerimaan terhadap skenario operasional.

Hasil pengujian dan UAT didokumentasikan beserta keterbatasan serta tindak lanjut temuannya. Dokumentasi mencakup kondisi lingkungan uji, pengguna yang terlibat, dan bukti evaluasi mitra untuk mendukung penilaian terhadap target Tingkat Kesiapan Teknologi (TKT) 5 yang dipersyaratkan pada bentuk Tugas Akhir prototipe.

Luaran yang direncanakan meliputi prototipe perangkat lunak, laporan Tugas Akhir, dokumentasi pengujian, dan panduan penggunaan. Penyiapan artikel ilmiah dan pendaftaran Hak Kekayaan Intelektual (HKI) dilaksanakan mengikuti ketentuan program studi serta arahan pembimbing.

## Daftar Pustaka

Abadi, R., Wasino dan Lina (2025) 'Perancangan aplikasi pembayaran SPP dan penggajian guru berbasis web pada bimbingan belajar', *Jurnal Teknologi dan Sistem Informasi Bisnis*, 7(1), hlm. 216-225. https://doi.org/10.47233/jteksis.v7i1.1666.

Ahadi, A.H., Pariyadi dan Djauhari, T. (2025) 'Pengembangan sistem informasi manajemen hotel multi-cabang berbasis web dengan framework Laravel', *Djtechno: Jurnal Teknologi Informasi*, 6(2), hlm. 758-773. https://doi.org/10.46576/djtechno.v6i2.7139.

Apriyanti, N., Wati, S.F.A. dan Najaf, A.R.E. (2024) 'Pemanfaatan metodologi PXP dan pengujian User Acceptance Testing (UAT) dalam pengembangan website e-kavling', *JATI (Jurnal Mahasiswa Teknik Informatika)*, 8(3), hlm. 3678-3686. https://doi.org/10.36040/jati.v8i3.9766.

Dzhurov, Y., Krasteva, I. dan Ilieva, S. (2009) 'Personal Extreme Programming - An Agile Process for Autonomous Developers', dalam *Proceedings of the International Conference on Software, Services and Semantic Technologies (S3T 2009)*. Sofia: Demetra EOOD, hlm. 252-259. Tersedia pada: https://research.uni-sofia.bg/handle/10506/647 (Diakses: 24 Oktober 2026).

Fajriansyah, S.N., Wijaya, M.S., Eryana, D.A., Safa, A., Pramadhan, H.R., Wicaksono, A., Baehaqi, M.I., Deivivi, F., Nurfajriansyah, D. dan Apandi, S. (2026) 'Pengembangan sistem informasi bimbingan belajar berbasis web untuk efisiensi operasional Bee Hive', *JRIS: Jurnal Rekayasa Informasi Swadharma*, 6(2), hlm. 115-126. https://doi.org/10.56486/jris.vol6no2.1346.

Gunawan, S.C., Nurwegiono, M. dan Setiawan, R. (2025) 'Sistem informasi bimbingan belajar RSDC berbasis website dengan menggunakan metode Waterfall untuk meningkatkan efisiensi administrasi', *RJTI Riau Jurnal Teknik Informatika*, 4(3), hlm. 424-435. https://doi.org/10.52158/rjti.v4i3.3655.

Hendri, Alghifari, M., Putri, H.Y., Rahayu, M. dan Nurmalasari (2025) 'Analisis sistem informasi akuntansi penerimaan kas (SPP) pada Yayasan Semesta Khatulistiwa', *JUSTIAN: Jurnal Sistem Informasi Akuntansi*, 6(2), hlm. 124-135. https://doi.org/10.31294/justian.v6i2.9114.

Kabisatullah, F. dan Noprisson, H. (2026) 'Pengembangan aplikasi RapaTrack untuk manajemen ruang rapat menggunakan Constraint Satisfaction Problem berbasis Android', *JUSIBI (Jurnal Sistem Informasi dan E-Bisnis)*, 8(2), hlm. 89-96. https://doi.org/10.54650/jusibi.v8i2.678.

Karpina, A., Akbar, Y., Lestari, W.A. dan Jamilah, F.N. (2025) 'Pengembangan sistem pembayaran pada website bimbingan belajar non-formal berbasis PHP MySQL di LOOP Coding BSD, Tangerang, Banten', *Jurnal JTIK (Jurnal Teknologi Informasi dan Komunikasi)*, 9(4), hlm. 1217-1223. https://doi.org/10.35870/jtik.v9i4.3846.

Khafidhoh, N., Febrianti, A.R. dan Sujono (2026) 'Sistem penjadwalan menggunakan algoritma genetika berbasis web', *Jurnal Teknologi Informasi: Jurnal Keilmuan dan Aplikasi Bidang Teknik Informatika*, 20(2), hlm. 15-20. https://doi.org/10.47111/jti.v20i2.24540.

Ramadhan, F. dan Widodo, H. (2026) 'Accounting Treatment Of Head Office And Branches Based On SAK EP: A Study on UMKM Rams Dimsum', *Indonesian Journal of Law and Economics Review*, 21(2). https://doi.org/10.21070/ijler.v21i2.1706.

Republik Indonesia (2003) *Undang-Undang Republik Indonesia Nomor 20 Tahun 2003 tentang Sistem Pendidikan Nasional*. Lembaran Negara Republik Indonesia Tahun 2003 Nomor 78. Tersedia pada: https://jdih.kemendikdasmen.go.id/sjdih/siperpu/dokumen/salinan/UU_tahun2003_nomor020.pdf (Diakses: 24 Oktober 2026).

Sudirman, B. dan Tristianti, M. (2021) 'Sistem informasi pengendalian kas bank dengan metode rekonsiliasi pada CV. Lisa Pratama berbasis client-server', *MEANS (Media Informasi Analisa dan Sistem)*, 6(2), hlm. 126-129. https://doi.org/10.54367/means.v6i2.1450.

## Penunjuk Bukti Wawancara untuk Draf Kerja

Penunjuk ini disediakan untuk membantu penelusuran fakta selama revisi dan tidak menggantikan lampiran wawancara pada proposal resmi. Sebelum pengajuan, identitas narasumber dan tanggal wawancara perlu dilengkapi berdasarkan bukti asli serta diselaraskan dengan penamaan lampiran pada laporan.

[^W2]: Wawancara kedua dengan Om Anang, bagian 24:15 sampai 25:04 tentang pencatatan dan 43:35 sampai 43:53 tentang konteks cabang. Lihat [transkrip wawancara kedua](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KEDUA SKRIPSI (OM ANANG)_WITH_TIMESTAMPS.txt:378>).

[^W3]: Wawancara ketiga dengan Mama Radit, bagian 19:01 sampai 21:11 mengenai pembahasan delapan cabang. Lihat [transkrip wawancara ketiga](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt:248>).

[^W3K]: Wawancara ketiga, bagian 35:25 sampai 38:37 mengenai jumlah siswa dan pengaturan kelas. Lihat [pembahasan kapasitas](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt:468>).

[^W4A]: Wawancara staf frontdesk, bagian 20:06 sampai 20:51 mengenai potongan saudara, 21:21 sampai 22:09 mengenai buku, dan 22:48 sampai 23:18 mengenai pendaftaran. Lihat [transkrip frontdesk](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:395>).

[^W4B]: Wawancara staf frontdesk, bagian 58:19 sampai 59:25 mengenai jatuh tempo dan pengingat pembayaran. Lihat [alur pengingat SPP](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1136>).

[^W4C]: Wawancara staf frontdesk, bagian 49:40 sampai 55:03 mengenai penyimpanan buku, laporan harian, pengiriman bukti transfer, dan rekap bulanan. Lihat [alur laporan dan penerimaan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:960>).

[^W4D]: Wawancara staf frontdesk, bagian 44:08 sampai 46:30 mengenai penempatan siswa dan kapasitas beberapa ruang. Lihat [pengaturan ruang dan sesi](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:853>).

[^W4E]: Wawancara staf frontdesk, bagian 31:10 sampai 33:06 mengenai pembagian jadwal tentor. Lihat [pengaturan jadwal tentor](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:607>).


[^W4F]: Wawancara staf frontdesk, bagian 04:29 sampai 05:03 mengenai layanan kalistung atau TK pada cabang yang dibahas. Lihat [keterangan layanan cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:68>).

[^W4G]: Wawancara staf frontdesk, bagian 07:07 sampai 08:01 dan 14:18 sampai 14:36 mengenai perbedaan biaya menurut jenjang, sesi, dan cabang. Lihat [pembahasan ketentuan biaya](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:135>).
