 
BAB 1​
PENDAHULUAN 
 
Bab ini memaparkan latar belakang permasalahan, rumusan masalah, tujuan 
yang ingin dicapai, batasan rancangan, manfaat bagi berbagai pihak, potensi 
dampak, serta kerangka tahapan pengembangan prototipe Tugas Akhir 
pengembangan sistem informasi manajemen operasional berbasis web untuk 
Bimbingan Belajar Artha Balikpapan.   
1.1.​
Latar Belakang  
Bimbingan belajar merupakan salah satu bentuk satuan pendidikan 
nonformal yang berfungsi menunjang dan melengkapi proses pembelajaran siswa 
di luar jam sekolah formal. Undang-Undang Republik Indonesia Nomor 20 Tahun 
2003 tentang Sistem Pendidikan Nasional mengakui pendidikan nonformal 
sebagai jalur yang sah dalam mendukung pencapaian kompetensi akademik 
peserta didik. Pelayanan yang dijalankan dalam bimbingan belajar mencakup 
pendampingan materi pelajaran, penguatan pemahaman kurikulum, dan persiapan 
menghadapi ujian. Keberhasilan penyelenggaraan bimbingan belajar didukung 
oleh berbagai faktor, mulai dari peserta didik, tentor pengajar, ketersediaan ruang 
kelas, hingga pengaturan jadwal. Seluruh faktor tersebut saling berkaitan dalam 
menciptakan kegiatan belajar yang efektif dan teratur, sehingga tata kelola 
operasional yang tertata sangat diperlukan agar pelayanan dapat berjalan dan tepat 
sasaran (Tiana & Gunanto, 2026). 
Tuntutan tata kelola operasional tersebut dirasakan secara nyata oleh 
Bimbingan Belajar (Bimbel) Artha Balikpapan, Kalimantan Timur, sebagai salah 
satu lembaga pendidikan nonformal yang terus berupaya mengelola pelayanannya 
secara mandiri. Lembaga ini didirikan pada tanggal 10 Oktober 1997 dan telah 
melayani masyarakat Kota Balikpapan selama hampir tiga dekade. Seiring 
bertambahnya kepercayaan peserta didik dan wali murid, Bimbel Artha 
berkembang hingga memiliki delapan cabang aktif yang tersebar di Kota 
Balikpapan, yang dinamai Artha 1 sampai Artha 8. Enam dari delapan cabang 
1 
 
tersebut melayani peserta didik dari jenjang TK, SD, SMP, sampai SMA; jumlah 
siswa aktif secara kumulatif belum terdokumentasi secara terpusat karena 
pencatatan masih tersimpan terpisah di masing-masing cabang. Berdasarkan 
keterangan pengelola, setiap cabang rata-rata memiliki tujuh hingga delapan 
tentor, sehingga jumlah keseluruhan tentor di delapan cabang mencapai 60 orang 
dan menampung sebanyak 2.400 siswa. Setiap cabang beroperasi dengan struktur 
tim yang terdiri dari satu orang sebagai kepala cabang, satu staf administrasi, dan 
tentor pengajar. 
Aktivitas operasional pada setiap cabang Bimbel Artha bertumpu pada 
empat tahapan layanan utama, yaitu penerimaan peserta didik baru, penempatan 
kelas belajar, pelaksanaan pendampingan belajar, serta pengelolaan pembayaran 
dan pelaporan kas. Pada tahap awal, calon siswa atau wali murid mendatangi 
kantor cabang untuk mendaftar, memilih program bimbingan, mengisi formulir 
data diri, serta menyepakati jadwal sesi belajar. Staf administrasi cabang 
kemudian memproses pendaftaran tersebut dengan memasukkan siswa ke dalam 
kelompok belajar, menetapkan ruang kelas sesuai daya tampung, dan menyusun 
penugasan tentor yang relevan dengan jenjang pendidikan siswa. Pelaksanaan 
kegiatan belajar mengajar selanjutnya berlangsung sesuai jadwal berkala. 
Rangkaian operasional tersebut berlanjut hingga tahap penarikan biaya 
bimbingan, di mana staf administrasi menerima pembayaran, menerbitkan bukti 
setor, membukukan transaksi harian, serta menyiapkan rekapitulasi untuk 
dilaporkan kepada pengelola pusat. Akan tetapi, keseluruhan aktivitas di delapan 
cabang fisik tersebut selama ini dijalankan secara manual dan berdiri sendiri tanpa 
integrasi sistem, sehingga kompleksitas pembagian jadwal dan pengelolaan 
transaksi memicu beban kerja administratif yang tinggi. 
Kerumitan tata kelola operasional tersebut bertambah akibat padatnya 
pembagian waktu belajar dan tingginya variasi penentuan tarif bimbingan di 
setiap cabang. Penyelenggaraan kelas terbagi ke dalam sesi pagi serta empat sesi 
reguler harian dari siang hingga malam hari, dengan dua kelompok pilihan hari 
belajar yaitu hari Senin, Rabu, Jumat serta hari Selasa, Kamis, Sabtu. Setiap sesi 
dibuat untuk mengakomodasi kebutuhan jenjang pendidikan yang berbeda, mulai 
2 
 
dari kelas anak usia dini (Taman Kanak-Kanak), jenjang Sekolah Dasar, Sekolah 
Menengah Pertama, hingga Sekolah Menengah Atas. Variasi jenjang dan waktu 
bimbingan tersebut diikuti oleh skema tarif iuran bulanan yang berbeda, ditambah 
pemberlakuan paket kelulusan khusus bagi siswa tingkat akhir yang dibayarkan 
per semester atau tahunan. Perbedaan kombinasi jadwal dan penentuan tagihan ini 
menimbulkan beban administratif yang berat bagi staf cabang, terlebih staf 
diwajibkan membukukan penutupan kas harian pada pukul 19.20 WITA, 
meskipun aktivitas pembelajaran berlangsung hingga pukul 20.30 WITA. 
Kondisi operasional yang kompleks tersebut semakin rentan terhadap 
kesalahan manusia karena seluruh proses administrasi di delapan cabang masih 
mengandalkan media kertas fisik. Berdasarkan hasil wawancara dengan Ketua 
Artha Balikpapan Ibu Emi Ratnawati, S.E. dan staf administrasi cabang Kak 
Agian Isna, pendaftaran siswa baru hanya dicatat pada buku besar berukuran A4 
yang disimpan terpisah di masing-masing cabang. Format pencatatan pada buku 
besar tersebut sangat terbatas, yakni sekadar mencantumkan nama siswa, nomor 
telepon wali, asal sekolah, dan tabel riwayat SPP dua belas bulan, tanpa 
mencakup identitas lengkap maupun data riwayat belajar peserta didik. Pada saat 
transaksi berlangsung, staf administrasi harus menerbitkan kuitansi fisik rangkap 
dua, menambahkan stempel serta paraf pada kartu SPP siswa, sekaligus 
memperhitungkan penyesuaian biaya khusus secara manual, seperti potongan 
keluarga kurang mampu atau diskon kakak-beradik. Ketiadaan database terpadu 
menyebabkan riwayat administrasi rentan hilang atau rusak, serta menyulitkan 
penelusuran status keaktifan siswa ketika terjadi pergantian staf administrasi 
cabang. 
Kelemahan 
pencatatan 
fisik 
tersebut 
berdampak 
langsung pada 
pengelolaan penerimaan kas dan proses rekonsiliasi keuangan di tingkat 
manajemen pusat. Ketergantungan pada lembaran kuitansi dan buku kas yang 
tersebar di delapan cabang menyulitkan pencocokan antara catatan penerimaan 
kasir dan bukti transaksi yang sebenarnya. Di Bimbel Artha, uang setoran tunai 
dikumpulkan secara berkala oleh kepala cabang untuk diantarkan langsung ke 
kantor pusat, sedangkan buku besar pencatatan tetap ditinggalkan di cabang. 
3 
 
Mekanisme pengantaran fisik uang kas tersebut tidak hanya memuat risiko 
keamanan selama perjalanan, tetapi juga memperlambat proses validasi 
penerimaan oleh pimpinan pusat. Di sisi lain, pembayaran yang dilakukan melalui 
transfer bank harus diverifikasi satu per satu terhadap mutasi rekening secara 
manual tanpa dukungan sistem pemantauan langsung (real-time). Ketiadaan 
rekapitulasi terpusat ini membuka celah terjadinya keterlambatan informasi dan 
selisih pencatatan kas, yang pada akhirnya menghambat pimpinan dalam 
mengambil keputusan strategis keuangan lembaga. 
Persoalan operasional berikutnya berkaitan dengan pengelolaan kapasitas 
ruang kelas dan koordinasi jadwal tentor. Setiap cabang memiliki kapasitas ruang 
kelas yang bervariasi antara delapan hingga lima belas siswa, bergantung pada 
ukuran fisik ruangan dan jenjang bimbingan belajar. Akan tetapi, staf administrasi 
tidak memiliki alat bantu visual untuk memantau apakah ruangan pada jam 
bimbingan tertentu sudah mendekati kapasitas maksimalnya. Ketiadaan indikator 
digital ini menimbulkan kebutuhan sistem yang mampu memetakan ketersediaan 
alokasi ruangan dan waktu mengajar, sehingga bentrokan penempatan sesi 
bimbingan dapat dicegah secara sistematis (Yuanita dkk., 2022). Pada aspek 
koordinasi tenaga pengajar, setiap cabang telah memiliki buku jadwal fisik serta 
lembaran rekapitulasi mingguan yang mencatat nama tentor dan jumlah siswa 
yang dibimbing untuk perhitungan honorarium. Akan tetapi, pencatatan manual di 
masing-masing cabang tersebut menyulitkan pimpinan pusat untuk memantau 
distribusi beban mengajar secara langsung. 
Untuk mengatasi akumulasi permasalahan operasional dan keterisolasian 
data di delapan cabang tersebut, penerapan sistem informasi manajemen 
memegang peranan krusial sebagai fondasi transformasi digital lembaga. Sistem 
informasi merupakan serangkaian komponen yang saling terhubung yang 
dirancang untuk mengumpulkan, mengolah, menyimpan, dan mendistribusikan 
informasi (Laudon & Laudon, 2020). Dalam lingkup lembaga pendidikan 
nonformal, pemanfaatan teknologi informasi terbukti meningkatkan efektivitas 
administrasi manual, mulai dari integrasi database siswa, penataan jadwal terpadu, 
hingga pencatatan pembayaran berkala (Fajriansyah dkk., 2026). Apabila lembaga 
4 
 
beroperasi di beberapa cabang sekaligus, sistem informasi yang dirancang juga 
harus mengakomodasi pemisahan kewenangan antarperan dan penyediaan laporan 
terpusat yang dapat dipantau oleh pimpinan pusat secara langsung (Ahadi dkk., 
2025). 
Sejumlah penelitian terdahulu menunjukkan bahwa pengembangan sistem 
informasi terbukti mampu menangani permasalahan operasional serupa pada 
lembaga pendidikan nonformal maupun unit layanan multicabang. Tiana dan 
Gunanto (2026) membangun sistem informasi bimbingan belajar berbasis web 
mobile yang memuat modul registrasi, penjadwalan, presensi, dan rekapitulasi 
data operasional. Fajriansyah dkk. (2026) mengembangkan sistem informasi 
Bimbel Bee Hive yang mengintegrasikan pengelolaan data siswa, jadwal, dan 
pembayaran dalam satu platform untuk meningkatkan efisiensi operasional. Barizi 
dkk. (2023) merancang sistem administrasi berbasis desktop pada sekolah kursus 
musik yang menyatukan modul pembayaran dan penjadwalan dalam satu 
platform. Zakaria dkk. (2023) merancang sistem administrasi dan pembayaran 
kursus berbasis web yang mengotomatisasi pencatatan iuran kursus, registrasi 
siswa baru, serta penerbitan laporan keuangan untuk meniadakan risiko kesalahan 
manual. Safitri dkk. (2026) mengembangkan sistem informasi manajemen Bimbel 
Ilman Nafi dengan fitur notifikasi otomatis melalui WhatsApp untuk penagihan 
SPP dan komunikasi antara pengelola, tentor, dan wali murid. Khafidhoh dkk. 
(2026) merancang sistem penjadwalan tentor berbasis web pada Bimbel AHE 
yang menunjukkan bahwa pengelolaan jadwal tanpa sistem terpusat berpotensi 
memunculkan konflik penugasan dan ketidakmerataan distribusi beban mengajar. 
Yuanita dkk. (2022) membangun sistem penjadwalan terintegrasi berbasis web 
yang membuktikan perlunya validasi batas kapasitas ruang dan jadwal secara 
digital untuk mencegah terjadinya bentrokan alokasi waktu dan ruangan. 
Sementara itu, Ahadi dkk. (2025) merancang sistem informasi manajemen 
multicabang di perhotelan dengan fitur pemisahan kewenangan Owner dan PIC 
Cabang, sedangkan Ramadhan & Widodo (2026) menunjukkan perlunya 
pemisahan pencatatan keuangan per cabang beserta rekap yang dapat diakses 
pusat. Seluruh penelitian tersebut menjadi acuan fungsional bagi modul-modul 
yang dikembangkan dalam prototipe ini. Meskipun demikian, sebagian besar 
5 
 
penelitian bimbingan belajar tersebut hanya berfokus pada pengelolaan satu 
cabang saja, sehingga belum mempersoalkan sinkronisasi data antarcabang. 
Sementara itu, penelitian multicabang yang ada berasal dari bidang perhotelan 
maupun perdagangan yang proses bisnisnya berbeda dengan lembaga pendidikan 
nonformal. Penelitian pada Bimbel Artha memiliki fokus yang berbeda karena 
dirancang untuk mengintegrasikan operasional delapan cabang sekaligus ke dalam 
satu sistem terpusat. Perbedaan utama terletak pada pembatasan hak akses di 
masing-masing cabang, dashboard pemantauan bagi pimpinan pusat untuk 
memverifikasi bukti transfer dan pemantauan kuota kelas serta jadwal tentor. 
Kebutuhan untuk menghubungkan operasional delapan cabang inilah yang 
menjadi pembeda sekaligus alasan utama dirancangnya sistem informasi untuk 
Bimbel Artha Balikpapan.  
Dari berbagai kendala operasional tersebut, pengembangan prototipe 
sistem informasi manajemen berbasis web menjadi penyelesaian yang tepat bagi 
Bimbel Artha. Sistem berbasis web memungkinkan data operasional dari delapan 
cabang terhubung langsung ke satu database terpusat, sehingga pengelola di 
tingkat pusat dapat memantau kondisi keuangan, jumlah siswa aktif, dan kegiatan 
cabang secara langsung. Penyimpanan data secara digital sekaligus menjaga 
riwayat data tetap terjaga ketika staf administrasi berganti, yang menurut 
pengelola cukup sering terjadi di cabang. Prototipe yang dikembangkan dalam 
Tugas Akhir ini memuat modul pendaftaran yang memantau ketersediaan 
kapasitas kelas secara langsung dan menampilkan peringatan ketika kuota hampir 
penuh, modul kasir yang mencatat pembayaran SPP beserta riwayat kuitansi 
digital dan memicu pengingat jatuh tempo ke WhatsApp wali murid, modul 
penjadwalan tentor yang mendeteksi potensi jadwal ganda serta menampilkan 
distribusi beban jam mengajar, dan dashboard pimpinan untuk mempermudah 
pencocokan penerimaan kas dengan catatan mutasi rekening bank dari delapan 
cabang. 
Dalam pelaksanaan Tugas Akhir ini, metodologi Personal Extreme 
Programming (PXP) dipilih sebagai kerangka kerja pengembangan prototipe 
sistem informasi. Pemilihan metode ini berdasarkan karakteristik PXP terhadap 
6 
 
kriteria evaluasi proses perangkat lunak adaptif untuk pengembang mandiri 
(single developer) (Sommerville, 2011; Dzhurov dkk., 2009). Berdasarkan kajian 
Dzhurov dkk. (2009) serta Agrawal dan Umphress (2008), pengembang mandiri 
menghadapi tantangan besar dalam mengelola estimasi waktu pengerjaan, 
kedisiplinan perencanaan, dan pengendalian kualitas perangkat lunak tanpa harus 
terbebani oleh pengelolaan dokumentasi formal yang rumit seperti pada Personal 
Software Process (PSP) konvensional. Kondisi tersebut sangat selaras dengan apa 
yang terjadi di Bimbel Artha, di mana proses rekayasa perangkat lunak dikerjakan 
oleh satu orang pengembang, proses bisnis lembaga sedang mengalami 
transformasi digital sehingga kebutuhan fungsional berkembang secara bertahap, 
serta pihak pimpinan dan staf administrasi cabang memiliki keterbatasan waktu 
pendampingan harian karena padatnya pengawasan operasional di delapan kantor 
cabang. Oleh karena itu, pendekatan iteratif PxP memungkinkan pengembang 
melakukan eksplorasi kebutuhan dan evaluasi prototipe secara berkala bersama 
mitra pada setiap akhir iterasi tanpa mengganggu operasional harian lembaga 
(Musofa dkk., 2025). 
Beberapa metode pengembangan alternatif dipertimbangkan namun 
memiliki karakteristik yang kurang selaras dengan kondisi penelitian ini. Metode 
Waterfall menerapkan tahapan pengembangan yang bersifat sekuensial linier, 
sehingga perubahan kebutuhan yang teridentifikasi di tengah proses dapat 
menuntut penyesuaian ulang terhadap tahapan analisis dan perancangan 
sebelumnya (Sommerville, 2011). Metode Scrum dirancang untuk pengembangan 
sistem yang melibatkan tim dengan pembagian peran yang formal serta koordinasi 
yang intensif antar anggota tim dalam setiap siklus (Sommerville, 2011; Febrianto 
dkk., 2020). Oleh karena itu, penerapannya kurang sesuai dengan kondisi 
penelitian ini yang hanya melibatkan satu orang pengembang dalam 
melaksanakan seluruh proses pengembangan sistem. Metode Prototyping berfokus 
pada pembuatan tampilan bersama pengguna, namun metode ini belum memiliki 
pedoman kerja personal untuk mengatur alokasi waktu dan pencatatan perbaikan 
sistem secara terukur. Sementara itu, metode Extreme Programming (XP) 
konvensional menuntut dua orang pemrogram bekerja bersama di satu komputer 
(pair programming) serta membutuhkan kehadiran pengguna secara intensif 
7 
 
(Beck & Andres, 2004), yang sulit dipenuhi karena peneliti bekerja sendiri dan 
mitra sibuk mengawasi cabang. Sementara itu, metode Rapid Application 
Development (RAD) menuntut komitmen waktu pengguna yang sangat tinggi 
dalam tahap construction (Hasanah & Untari, 2020), suatu kondisi yang sulit 
dipenuhi oleh pengelola cabang yang operasional hariannya sudah sangat padat. 
Berdasarkan keseluruhan pertimbangan tersebut, Personal Extreme 
Programming 
(PXP) 
dipilih karena merupakan adaptasi dari Extreme 
Programming (XP) yang dipadukan dengan prinsip Personal Software Process 
(PSP) untuk mendukung rekayasa perangkat lunak oleh pengembang individual 
(Agarwal & Umphress, 2008; Dzhurov dkk., 2009; Fikri & Arthawan, 2020). PXP 
menyediakan tujuh tahapan pengembangan yang terstruktur, mulai dari eksplorasi 
kebutuhan (requirements), perencanaan (planning), inisialisasi iterasi (iteration 
initialization), perancangan (design), implementasi (implementation), pengujian 
sistem (system testing), hingga retrospektif (retrospective). Karakteristik tersebut 
memungkinkan pengembang melakukan aktivitas rekayasa perangkat lunak secara 
mandiri, sementara mitra tetap dilibatkan secara terencana dalam memberikan 
kebutuhan dan mengevaluasi hasil fungsional pada setiap akhir iterasi. Masukan 
dari mitra selanjutnya digunakan sebagai bahan pertimbangan dalam menentukan 
prioritas pengembangan pada siklus iterasi berikutnya. Selain itu, PXP 
mengadopsi pengembangan yang lebih ringkas dibandingkan proses Personal 
Software Process (PSP) konvensional dengan meminimalkan beban dokumentasi 
formal, namun tetap menjaga disiplin perencanaan, pengujian berkelanjutan, dan 
evaluasi proses pengembangan (Dzhurov dkk., 2009; Musofa dkk., 2025). Dengan 
demikian, PXP dinilai sebagai metodologi yang paling tepat untuk mendukung 
keberhasilan pengembangan prototipe sistem informasi manajemen operasional 
Bimbel Artha Balikpapan. 
Berdasarkan seluruh permasalahan operasional dan landasan tersebut, 
penelitian Tugas Akhir ini diarahkan pada rancang bangun prototipe sistem 
informasi manajemen operasional terintegrasi berbasis web menggunakan metode 
Personal Extreme Programming (PxP) dengan Bimbingan Belajar Artha 
Balikpapan sebagai mitra studi kasus. Prototipe sistem informasi ini ditujukan 
8 
 
untuk memberikan solusi nyata terhadap kendala pencatatan formulir pendaftaran 
fisik, penempatan kelompok belajar, pencatatan transaksi, serta rekonsiliasi kas 
terpusat bagi delapan kantor cabang secara terpadu. Berlandaskan permasalahan 
yang telah diuraikan, rumusan masalah penelitian ini dirinci secara terstruktur 
pada subbab berikutnya. 
1.2.​
Rumusan Masalah 
Berdasarkan permasalahan yang telah dipaparkan pada latar belakang, 
rumusan masalah dalam Tugas Akhir ini dijabarkan ke dalam beberapa pertanyaan 
sebagai berikut: 
1.​ Bagaimana mengembangkan prototipe sistem informasi manajemen 
operasional bimbingan belajar multicabang berbasis web menggunakan 
metode Personal Extreme Programming (PxP) yang mengintegrasikan 
pengelolaan pendaftaran siswa, penjadwalan tentor dan pencatatan 
pembayaran SPP di tingkat cabang dengan dashboard pemantauan dan 
rekonsiliasi pendapatan di tingkat pusat? 
2.​ Bagaimana hasil evaluasi tingkat kesesuaian fungsional dan penerimaan 
pengguna terhadap prototipe sistem informasi yang dikembangkan, 
berdasarkan pengujian Black Box Testing dan User Acceptance Testing 
(UAT) bersama Pengelola dan Staf Administrasi di Bimbel Artha 
Balikpapan? 
1.3.​
Tujuan 
Tujuan dari penelitian ini adalah merancang dan membangun sistem 
informasi manajemen operasional terintegrasi berbasis web untuk Bimbel Artha 
Balikpapan, dengan capaian spesifik sebagai berikut: 
1.​ Mengembangkan prototipe sistem informasi manajemen operasional 
bimbingan belajar multicabang berbasis web menggunakan metode 
Personal 
Extreme 
Programming 
(PxP) 
yang 
mengintegrasikan 
pengelolaan pendaftaran siswa, penjadwalan tentor, dan pencatatan 
9 
 
pembayaran SPP di tingkat cabang dengan dashboard pemantauan dan 
rekonsiliasi kas di tingkat pusat. 
2.​ Mengevaluasi tingkat kesesuaian fungsional dan penerimaan pengguna 
terhadap prototipe sistem informasi yang dikembangkan melalui pengujian 
Black Box Testing dan User Acceptance Testing (UAT) bersama Pengelola 
dan Staf Administrasi di Bimbel Artha Balikpapan. 
1.4.​
Batasan Rancangan  
Agar prototipe dapat diselesaikan secara optimal dalam batas waktu 
pelaksanaan Tugas Akhir, ruang lingkup rancangan dibatasi sebagai berikut: 
1.​ Prototipe berfokus pada dashboard manajemen operasional internal 
dengan dua peran pengguna, yaitu Admin Cabang dan Super Admin.  
2.​ Fitur pembelajaran daring, bank soal, dan pelaporan perkembangan nilai 
akademik siswa tidak termasuk ke dalam ruang lingkup, karena fokus 
utama prototipe adalah efisiensi administrasi operasional. 
3.​ Prototipe tidak mengintegrasikan payment gateway pihak ketiga. 
Pembayaran SPP melalui transfer bank diverifikasi secara manual oleh 
Admin Cabang berdasarkan bukti transfer yang diunggah ke sistem. 
4.​ Notifikasi kepada wali murid dikirimkan melalui tautan WhatsApp yang 
diakses langsung dari sistem, dan tidak melalui email, karena nomor 
WhatsApp dinilai lebih aktif digunakan dan lebih cepat dibaca oleh wali 
murid. 
 
1.5.​
Manfaat 
Pengembangan prototipe sistem informasi ini diharapkan memberikan 
manfaat nyata bagi berbagai pihak yang terlibat dalam pengelolaan operasional 
bimbingan belajar. Manfaat tersebut terbagi ke dalam tiga pihak, yaitu bagi mitra 
bimbingan belajar, bagi pengguna langsung sistem, serta bagi peneliti dalam 
pengembangan sistem informasi.  
Bagi mitra, yaitu Bimbel Artha Balikpapan, prototipe menyediakan sistem 
pencatatan pendaftaran siswa dan riwayat pembayaran SPP secara digital untuk 
10 
 
menggantikan buku besar kertas di delapan cabang. Sistem ini memungkinkan 
manajemen pusat untuk memantau kondisi keuangan, jumlah siswa aktif, serta 
performa masing-masing cabang secara langsung melalui satu dashboard terpusat. 
Selain itu, prototipe memberikan mitigasi terhadap risiko kehilangan data akibat 
pergantian staf administrasi yang kerap terjadi di cabang, sekaligus memfasilitasi 
koordinasi jadwal tentor agar terhindar dari potensi jadwal ganda antarcabang.  
Bagi pengguna langsung sistem, yaitu Admin Cabang dan Super Admin, 
prototipe mempercepat alur kerja operasional harian yang selama ini dilakukan 
secara manual. Admin Cabang tidak perlu lagi memeriksa buku catatan satu per 
satu untuk memastikan status pembayaran, karena sistem menyajikan informasi 
tersebut secara langsung. Super Admin dapat mencocokkan laporan pendapatan 
dari delapan cabang dengan catatan mutasi rekening bank langsung dari 
dashboard, tanpa harus menunggu berkas laporan fisik dari setiap cabang. 
Bagi peneliti, Tugas Akhir ini memberikan pengalaman langsung dalam 
menerapkan metode Personal Extreme Programming (PxP) pada pengembangan 
sistem berskala menengah dengan mitra yang proses bisnisnya masih berkembang 
dan memperkaya kajian transformasi digital pada sektor pendidikan nonformal di 
Indonesia. 
1.6.​
Potensi Dampak Fungsional/Komersial  
Pada lingkup fungsional, prototipe ini diharapkan menjadi fondasi 
operasional digital bagi Bimbel Artha yang selama ini bergantung sepenuhnya 
pada pencatatan manual. Apabila prototipe diterapkan secara penuh di delapan 
cabang, pengelola dapat memangkas waktu rekapitulasi laporan keuangan bulanan 
yang saat ini dilakukan secara manual dari masing-masing cabang. Pengurangan 
beban kerja administrasi tersebut memungkinkan staf cabang untuk lebih berfokus 
pada pelayanan peserta didik, bukan pada pencatatan yang berulang dan rentan 
kesalahan. Prototipe juga memfasilitasi deteksi dini terhadap tunggakan SPP dan 
bentrok jadwal tentor yang selama ini kerap terlambat diketahui, sehingga 
permasalahan operasional dapat ditangani lebih cepat sebelum berdampak pada 
kualitas layanan. 
11 
 
Pada lingkup komersial, rancangan antarmuka dan arsitektur sistem yang 
dikembangkan dalam prototipe ini dapat dikembangkan lebih lanjut menjadi 
produk perangkat lunak berbasis Software as a Service (SaaS) yang ditawarkan 
kepada lembaga bimbingan belajar lain di Kalimantan Timur maupun nasional. 
Permintaan terhadap sistem manajemen operasional bimbel yang terjangkau dan 
mudah digunakan cukup tinggi, mengingat sebagian besar lembaga sejenis masih 
beroperasi secara manual seperti kondisi Bimbel Artha saat ini.  
1.7.​
Kerangka Tugas Akhir  
Berikut adalah Diagram Alir Kerangka Pengerjaan Tugas Akhir. Diagram 
ini menggambarkan hubungan antara permasalahan yang dihadapi di lapangan, 
landasan teori yang melandasi, proses analisis kebutuhan, tahapan pengembangan 
prototipe dengan metode Personal Extreme Programming (PXP), serta solusi 
yang dihasilkan.  
12 
 
 
Gambar 1.1 Diagram Alir Kerangka Pengerjaan Tugas Akhir 
Gambar 1.1 menyajikan keseluruhan tahapan rekayasa perangkat lunak 
dalam pengembangan prototipe sistem informasi untuk Bimbel Artha Balikpapan. 
Alur kerja terbagi ke dalam empat fase utama, yaitu fase inisiasi penelitian, fase 
rekayasa sistem menggunakan metode Personal Extreme Programming (PxP), 
fase evaluasi pengguna dengan User Acceptance Testing (UAT), serta fase 
deployment. Pembagian fase ini memastikan setiap kebutuhan operasional dari 
delapan cabang Bimbel Artha dapat dipetakan secara akurat, diwujudkan ke 
dalam modul yang teruji, hingga berhasil diterapkan untuk menunjang aktivitas 
operasional.  
Tahap awal penelitian diawali dengan identifikasi masalah melalui 
observasi langsung dan wawancara bersama pengelola serta staf administrasi 
cabang. Identifikasi berfokus pada berbagai kendala operasional di delapan 
cabang, seperti pencatatan pendaftaran dan riwayat SPP pada buku besar kertas, 
penagihan tunggakan manual, pemantauan kapasitas ruang kelas yang belum 
terukur secara digital, serta ketiadaan pemantauan langsung bagi pimpinan pusat. 
Berdasarkan permasalahan tersebut, peneliti melaksanakan studi literatur untuk 
mengkaji konsep tata kelola data terpusat, arsitektur sistem berbasis web, 
mekanisme pemisahan peran antara Admin Cabang dan Super Admin, metodologi 
Personal Extreme Programming (PxP), serta teknik pengujian perangkat lunak. 
Tahap berikutnya adalah fase rekayasa sistem yang dilaksanakan 
menggunakan metode Personal Extreme Programming (PxP). Pemilihan metode 
ini dilandasi oleh kebutuhan pengembangan mandiri yang adaptif terhadap 
dinamika proses bisnis bimbingan belajar (Dzhurov dkk., 2009). PxP diawali 
dengan analisis kebutuhan (requirements) untuk menerjemahkan data lapangan ke 
dalam spesifikasi cerita pengguna (user stories) dan daftar kebutuhan sistem 
(product backlog). Dari daftar kebutuhan tersebut, pengembang menyusun 
rencana kerja (planning) berupa modul ke dalam empat siklus iterasi serta 
penetapan estimasi durasi pengerjaan teknis. 
13 
 
Pelaksanaan setiap iterasi kerja PxP dijalankan secara terstruktur melalui 
siklus yang berulang. Siklus dimulai dari inisialisasi iterasi (iteration 
initialization) untuk menentukan modul yang akan dikerjakan, perancangan 
sistem (design) yang mencakup pemodelan database dan tata letak antarmuka, 
hingga tahap implementasi (implementation). Pada tahap implementasi, 
pengembang menerapkan pendekatan Test-Driven Development (TDD) yang 
terdiri dari penulisan pengujian unit (unit testing), pengodean program (code), dan 
penyempurnaan struktur kode (refactor). Setelah modul selesai dikodekan, 
pengembang melakukan pengujian sistem (system testing) menggunakan metode 
Black Box Testing untuk memastikan seluruh fungsi berjalan tanpa error. Setiap 
iterasi ditutup dengan evaluasi retrospektif (retrospective) untuk menelaah log 
error serta membandingkan estimasi waktu pengerjaan dengan waktu riil. Apabila 
evaluasi menunjukkan masih terdapat modul yang perlu diselesaikan pada iterasi 
lanjutan, alur pengerjaan berputar kembali ke tahap inisialisasi iterasi hingga 
seluruh empat siklus iterasi tuntas diselesaikan. 
Setelah seluruh rangkaian siklus iterasi PxP selesai dan prototipe 
terintegrasi secara menyeluruh, tahap berikutnya adalah pengujian penerimaan 
pengguna melalui User Acceptance Testing (UAT) bersama pihak mitra Bimbel 
Artha. Pengujian ini melibatkan Pengelola dan Staf Administrasi cabang untuk 
menguji kesesuaian alur kerja, mulai dari registrasi siswa baru, pengaturan jadwal 
dan kapasitas kelas, pencatatan pembayaran, hingga pemantauan pendapatan pada 
dashboard pusat. Hasil validasi UAT yang telah disetujui mitra kemudian 
dilanjutkan ke tahap deployment, agar dapat diakses dan digunakan secara 
langsung oleh pengguna di delapan cabang. Rangkaian ditutup dengan selesainya 
seluruh proses rekayasa, sehingga sistem informasi beroperasi dalam menunjang 
tata kelola operasional Bimbingan Belajar Artha Balikpapan.  
 
 
 
 
14 
 
 
15 
