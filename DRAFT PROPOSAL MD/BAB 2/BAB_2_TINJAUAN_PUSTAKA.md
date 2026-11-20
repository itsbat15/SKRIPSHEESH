 
BAB 2​
TINJAUAN PUSTAKA 
 
Bab ini berisi tinjauan pustaka yang mencakup dasar teori yang selaras 
dengan penelitian tugas akhir ini. Uraian di dalamnya bertujuan untuk 
menjelaskan konsep rekayasa perangkat lunak, teknologi yang digunakan, serta 
telaah penelitian terdahulu yang relevan.  
2.1.​
Kajian Teknologi atau Metode Terkait 
Kajian teknologi atau metode terkait dalam subbab ini untuk menguraikan 
konsep, prinsip kerja, dan standar rekayasa perangkat lunak dalam membangun 
prototipe sistem ARTHA. Rangkaian teori yang dikaji tidak sekadar disajikan 
sebagai definisi, melainkan dihubungkan secara kontekstual dengan alasan 
pemilihannya serta relevansinya terhadap pemecahan masalah operasional 
bimbingan belajar multicabang.  
Seluruh kajian pada bagian ini dikelompokkan ke dalam empat aspek 
utama. Aspek pertama membahas metode pengembangan perangkat lunak yang 
mencakup 
konsep 
sistem 
informasi 
manajemen 
beserta 
siklus 
hidup 
pengembangannya dan metodologi Personal Extreme Programming (PxP). Aspek 
kedua membahas teknik pemodelan kebutuhan dan perancangan sistem yang 
meliputi User Stories, Use Case Diagram, Business Process Model and Notation 
(BPMN), serta Entity Relationship Diagram (ERD). Aspek ketiga membedah 
arsitektur teknologi yang terdiri dari Next.js, Tailwind CSS, Laravel, REST API, 
dan database MySQL. Aspek keempat menguraikan metodologi pengujian 
perangkat lunak yang mencakup Black Box Testing dan User Acceptance Testing 
(UAT). 
2.1.1.​
Sistem Informasi Manajemen  
Sistem informasi merupakan serangkaian komponen yang saling 
terhubung 
untuk 
mengumpulkan, 
memproses, 
menyimpan, 
dan 
mendistribusikan informasi untuk mendukung pengambilan keputusan, 
koordinasi, analisis masalah, serta visualisasi dalam suatu organisasi 
16 
 
(Laudon & Laudon, 2020). Sistem informasi bekerja melalui siklus 
pengolahan data yang melibatkan komponen input, process, output, dan 
storage, yang disertai feedback. Penerapan sistem informasi yang tepat 
dapat 
membantu 
organisasi 
mengurangi 
redundansi 
pencatatan, 
meminimalkan potensi kesalahan yang dilakukan oleh manusia, serta 
mempercepat pertukaran data (Sommerville, 2011). 
Management Information System (SIM) merupakan kategori sistem 
informasi 
yang melayani middle management untuk memantau, 
mengendalikan kinerja operasional, dan mendukung pengambilan 
keputusan dengan penyajian laporan secara berkala (Laudon & Laudon, 
2020). SIM bekerja dengan cara mengirimkan data transaksi harian, 
kemudian mentransformasikannya menjadi laporan manajerial, seperti 
laporan berkala, laporan ringkasan, serta laporan penyimpangan 
operasional. Ketersediaan informasi tersebut agar pengelola organisasi 
dapat memantau efektivitas kinerja yang sedang berjalan, mengendalikan 
aktivitas rutin, dan mengambil keputusan berlandaskan data yang 
konsisten dan terintegrasi.  
2.1.2.​
Personal Extreme Programming 
Personal Extreme Programming (PxP) merupakan metodologi 
rekayasa perangkat lunak yang diadaptasi dari prinsip-prinsip Extreme 
Programming (XP) untuk diterapkan oleh pengembang tunggal. Konsep 
XP untuk pengembang tunggal pertama kali diinisiasi oleh Agarwal dan 
Umphress (2008) melalui praktik Extreme Programming for a Single 
Person Team, yang kemudian distandarisasi oleh Dzhurov, Krasteva, dan 
Ilieva (2009) menjadi kerangka kerja PxP.  
17 
 
Gambar 2.1 Tahapan Personal Extreme Programming 
(Dzhurov, Krasteva, dan Ilieva, 2009) 
Pelaksanaan metodologi Personal Extreme Programming (PxP) 
terbagi ke dalam tujuh tahapan proses yang berjalan secara sistematis dan 
berulang dalam setiap iterasi pengembangan. Rangkaian tahapan tersebut 
dirinci sebagai berikut: 
1.​ Kebutuhan (Requirements) 
Pada 
tahap 
ini, 
pengembang 
mengidentifikasi 
kebutuhan 
fungsional dan nonfungsional sistem melalui diskusi langsung 
bersama pemangku kepentingan (Dzhurov dkk., 2009). Hasil 
identifikasi kebutuhan tersebut kemudian didefinisikan ke dalam 
bentuk dokumen spesifikasi kebutuhan yang memuat kumpulan 
User Stories sebagai representasi fitur operasional yang akan 
dibangun (Fikri & Arthawan, 2020; Marthasari dkk., 2018). 
18 
 
2.​ Perencanaan (Planning) 
Pada tahap perencanaan, pengembang menyusun daftar User 
Stories yang telah disepakati untuk memetakan keseluruhan beban 
kerja sistem (Dzhurov dkk., 2009). Setiap User Story dianalisis 
untuk menetapkan skala prioritas pengembangan serta diberikan 
bobot Story Points untuk memperkirakan tingkat kompleksitas 
pengerjaan (Marthasari dkk., 2018). Rangkaian kebutuhan tersebut 
dilanjutkan 
ke 
dalam 
beberapa 
siklus 
iterasi 
dengan 
mempertimbangkan keterkaitan antarfitur dan waktu pengembang 
tunggal (Agarwal & Umphress, 2008).  
3.​ Inisialisasi Iterasi (Iteration Initialization) 
Tahap ini menandai dimulainya setiap siklus iterasi pengembangan 
perangkat lunak, setiap siklus diawali dengan pemilihan prioritas 
dengan durasi pengerjaan yang berlangsung antara satu hingga tiga 
minggu sesuai lingkup pengerjaan (Dzhurov dkk., 2009; 
Praseptiawan dkk., 2025).  
4.​ Perancangan (Design)​
Tahap ini menerapkan prinsip Simple Design untuk menghasilkan 
struktur perangkat lunak yang ringkas dan hanya berfokus pada 
kebutuhan iterasi yang sedang berjalan (Dzhurov dkk., 2009). 
Pengembang 
merancang 
antarmuka 
sistem 
dalam 
bentuk 
wireframe, menyusun pemodelan alur kerja interaksi pengguna 
menggunakan Use Case Diagram, serta memetakan struktur data 
relasional menggunakan Entity Relationship Diagram (ERD) untuk 
mempermudah penulisan kode program (Fikri & Arthawan, 2020; 
Musofa dkk., 2025).    
5.​ Implementasi (Implementation)​
Pada tahap ini berlangsung proses penulisan kode program untuk 
mengimplementasikan seluruh objek dan fungsi yang telah 
19 
 
ditetapkan pada tahap desain (Dzhurov dkk., 2009). Pengembang 
menerapkan alur kerja terstruktur yang terdiri atas tiga tahapan 
berurutan, yaitu pembuatan pengujian unit (Unit Testing), 
penulisan kode fitur (code generation), dan refactoring (Marthasari 
dkk., 2018). Tahap ini dinyatakan selesai apabila seluruh kode 
program berjalan dengan benar dan pengujian unit berhasil lolos 
tanpa error.   
6.​ Pengujian Sistem (System Testing)​
Pada tahap ini, seluruh modul yang telah selesai dibangun diuji 
untuk memverifikasi pemenuhan persyaratan awal sistem (Dzhurov 
dkk., 2009). Pengembang melakukan verifikasi fungsi operasional 
menggunakan teknik Black Box Testing untuk memastikan bahwa 
seluruh data yang masuk dan antarmuka berjalan valid sesuai 
skenario bisnis (Musofa dkk., 2025).  
7.​ Retrospektif (Retrospective)​
Tahap ini menjadi fase evaluasi akhir dari setiap siklus iterasi yang 
telah dijalankan pada tahap ini dilakukan analisis perbandingan 
antara estimasi waktu pengerjaan tugas dengan durasi kerja 
(Dzhurov dkk., 2009), serta memastikan tidak ada kesalahan fungsi 
yang tersisa sebelum sistem beralih ke iterasi berikutnya (Musofa 
dkk., 2025).  
 
20 
 
2.1.3.​
Business Process Model and Notation (BPMN) 
Business Process Model and Notation (BPMN) merupakan standar 
pemodelan yang dirancang untuk menggambarkan rangkaian aktivitas dan 
logika proses bisnis organisasi ke dalam diagram alur kerja (Dumas dkk., 
2018). 
Visualisasi 
diagram 
ini 
berfungsi 
mengatasi 
kelemahan 
dokumentasi teks naratif yang ambigu, rentan multitafsir, serta sulit 
disinkronkan dengan kebutuhan teknis perangkat lunak yang terus 
berkembang. Melalui standarisasi notasi grafis, BPMN menjembatani 
komunikasi teknis antara pemangku kepentingan bisnis nonteknis, analis 
sistem, dan pengembang perangkat lunak, sehingga seluruh alur kerja 
operasional dapat dipetakan menjadi blueprint perancangan arsitektur 
sistem informasi. 
Dalam metodologi rekayasa proses bisnis, pemodelan alur kerja 
terikat pada siklus hidup perbaikan proses yang menuntut dua pemetaan 
utama, yaitu analisis proses bisnis As-Is pada tahap penemuan proses 
Process Discovery dan perancangan proses bisnis To-Be pada tahap 
perancangan ulang (Process Redesign). Penyusunan diagram BPMN 
mengorganisasikan elemen visual ke dalam empat kelompok notasi pokok, 
yaitu objek aliran (flow objects), objek penghubung (connecting objects), 
jalur pembagi tanggung jawab (swimlanes), dan artefak data (data 
objects). Objek aliran mencakup peristiwa (event) untuk menandai status 
awal atau akhir proses, aktivitas (task) untuk merepresentasikan unit 
tindakan kerja yang dieksekusi, serta gerbang logika (gateway) berbentuk 
belah ketupat untuk percabangan keputusan maupun aliran paralel. 
Pembagian wewenang dan batasan interaksi diatur menggunakan pool 
yang merepresentasikan batasan entitas, serta lane yang menunjukkan alur 
berdasarkan peran tanggung jawab dari masing-masing aktor kerja. 
Penerapan 
pemodelan 
visual 
proses 
bisnis 
As-Is 
dan 
To-Be 
diimplementasikan menggunakan perangkat lunak Bizagi Modeler, yang 
terbukti efektif menghasilkan model alur kerja terstruktur yang adaptif 
sebagai landasan spesifikasi kebutuhan perangkat lunak (Yusmar dkk., 
21 
 
2023). Rangkuman unsur dan notasi dasar BPMN disajikan pada Tabel 
2.1. 
Tabel 2.1 Unsur dan Notasi Business Process Model and Notation 
Kategori 
Elemen 
Simbol 
Notasi 
Nama Notasi 
Deskripsi Operasional 
Flow Objects 
 
Start Event 
Menandai titik pemicu awal 
dimulainya 
suatu 
aliran 
proses bisnis operasional. 
Flow Objects 
 
Intermediate 
Event 
Menandai peristiwa transisi 
yang terjadi di antara awal 
dan 
akhir 
alur 
proses, 
seperti penerimaan pesan 
atau jeda waktu tertentu. 
Flow Objects 
 
End Event 
Menandai titik penyelesaian 
akhir dari seluruh rangkaian 
hasil eksekusi proses bisnis. 
Flow Objects 
 
Task / Activity 
Unit 
pekerjaan 
atau 
tindakan 
operasional 
spesifik 
yang 
dieksekusi 
oleh pengguna manusia atau 
modul sistem informasi. 
Flow Objects 
 
Exclusive 
Gateway (XOR) 
Gerbang 
percabangan 
keputusan kondisional yang 
membatasi 
alur 
proses 
untuk hanya memilih tepat 
satu 
lintasan 
keluar 
berdasarkan syarat tertentu. 
Flow Objects 
 
Parallel Gateway 
(AND) 
Gerbang 
yang 
memecah 
satu 
aliran 
menjadi 
beberapa alur aktivitas yang 
berjalan 
serentak, 
atau 
menggabungkan 
kembali 
alur paralel menjadi satu. 
22 
 
Kategori 
Elemen 
Simbol 
Notasi 
Nama Notasi 
Deskripsi Operasional 
Connecting 
Objects 
 
Sequence Flow 
Garis 
penunjuk 
urutan 
eksekusi 
aktivitas 
kerja 
yang 
menghubungkan 
antarelemen aliran di dalam 
satu pool atau lane yang 
sama. 
Connecting 
Objects 
 
Message Flow 
Garis 
pengiriman 
sinyal 
atau 
pesan 
pertukaran 
informasi yang melintasi 
batasan 
antardua 
pool 
organisasi yang berbeda. 
Swimlanes 
 
Pool 
Wadah 
visual 
yang 
merepresentasikan batasan 
suatu 
entitas 
bisnis, 
partisipan 
organisasi 
mandiri, 
atau 
sistem 
informasi eksternal. 
Swimlanes 
 
Lane 
Subdivisi di dalam pool 
yang 
membagi 
aktivitas 
kerja 
berdasarkan 
peran 
fungsional 
spesifik 
dari 
aktor 
penanggung jawab 
tugas. 
Data Objects 
 
Data Object 
Artefak dokumen informasi 
yang 
menjadi 
masukan 
(input) atau luaran (output) 
dari aktivitas proses bisnis. 
Data Objects 
 
Data Store 
Wadah penyimpanan data 
terstruktur atau pangkalan 
data yang persisten dan 
melampaui masa hidup satu 
instans proses bisnis. 
  
 
23 
 
2.1.4.​
User Stories 
User Stories merupakan kebutuhan perangkat lunak yang berfokus 
pada nilai fungsional dari sudut pandang pengguna akhir. Dalam 
metodologi agile, user stories menggantikan dokumen spesifikasi 
kebutuhan formal dengan deskripsi kebutuhan yang ringkas dan mudah 
dipahami oleh pihak pengembang maupun pemangku kepentingan 
nonteknis. Penggunaan user stories agar komunikasi antara pengembang 
dan pengguna dapat memahami alur bisnis operasional serta diselaraskan 
secara cepat (Cohn, 2004). 
Pembuatan user story mengikuti struktur format baku yang telah 
terstandarisasi dalam rekayasa perangkat lunak modern (Cohn, 2004). 
Format tersebut dirumuskan dalam kalimat: "Sebagai [peran pengguna], 
saya ingin [tindakan atau kemampuan sistem], agar [tujuan atau manfaat 
bisnis yang diharapkan]." Pola kalimat ini menegaskan tiga aspek, yaitu 
subjek yang membutuhkan fungsi, kapabilitas teknis yang harus 
disediakan perangkat lunak, serta nilai manfaat bisnis yang ingin dicapai. 
Kriteria penerimaan (acceptance criteria) berfungsi sebagai 
batasan operasional dan tolok ukur dari suatu user story. Kriteria ini 
dirumuskan dalam bentuk skenario pengujian yang dapat diverifikasi, 
misalnya keberhasilan validasi masukan data, perubahan status transaksi, 
atau label peringatan error (Febrianto dkk., 2020). Dalam metodologi PxP, 
user stories dan kriteria penerimaan menjadi fondasi utama dalam 
perancangan kasus uji Black Box Testing dan skenario User Acceptance 
Testing (UAT). Format penulisan user story beserta kriteria penerimaannya 
disajikan pada Tabel 2.2.  
 
24 
 
Tabel 2.2 Contoh Format Penulisan User Story  
Kode  
Peran 
I Want To 
So That 
Acceptance 
Criteria 
US-01 
Staf 
Administrasi 
Cabang 
Mencatat data 
formulir 
pendaftaran 
siswa baru ke 
sistem 
Data riwayat 
akademik dan 
rombongan 
belajar siswa 
tersimpan 
terpusat pada 
database 
1. Sistem 
berhasil 
menyimpan 
rekaman jika 
seluruh kolom 
wajib terisi 
secara valid. 
2. Sistem 
menampilkan 
pesan peringatan 
spesifik jika 
nomor telepon 
atau identitas 
telah terdaftar. 
3. Status 
pendaftaran 
awal disetel 
otomatis 
menjadi 
'Menunggu 
Pembayaran'. 
 
2.1.5.​
Use Case Diagram 
Use Case Diagram merupakan salah satu diagram pemodelan 
perilaku dalam kerangka kerja Unified Modeling Language (UML) yang 
merepresentasikan interaksi antara sistem perangkat lunak dengan entitas 
eksternal di lingkungannya (Hasanah & Untari, 2020). Model ini berfungsi 
memetakan batasan sistem serta mengidentifikasi layanan fungsional yang 
disediakan perangkat lunak untuk memenuhi tujuan kerja pengguna, 
sehingga perancangannya berfokus pada apa yang dilakukan oleh sistem 
untuk aktor, bukan bagaimana mekanisme prosedural di dalam kode 
dijalankan (Sommerville, 2011). 
25 
 
Komponen utama dalam use case diagram terdiri dari aktor, use 
case, dan relasi keterhubungan (Hasanah & Untari, 2020; Kurniawan, 
2018). Aktor merepresentasikan peran pengguna manusia, perangkat 
keras, atau hal lain di luar sistem yang berinteraksi langsung dengan fungsi 
perangkat lunak. Sementara itu, use case merepresentasikan sekumpulan 
runtutan aksi yang dieksekusi sistem untuk menghasilkan luaran bagi aktor 
tersebut. 
Keterhubungan 
fungsional 
antarelemen 
dalam 
diagram 
dinyatakan melalui relasi asosiasi, <<include>>, <<extend>>, serta relasi 
pewarisan (generalization). Format penulisan simbol use case diagram 
disajikan pada Tabel 2.3. 
 
 
26 
 
Tabel 2.3 Simbol Use Case Diagram 
Nama Simbol 
Simbol 
Deskripsi 
Actor 
 
Peran 
pihak 
di luar 
sistem yang berinteraksi 
dengan fungsi sistem 
informasi, baik berupa 
pengguna 
manusia 
maupun sistem eksternal 
lain. 
Use Case 
 
Fungsionalitas 
atau 
perilaku yang disediakan 
sistem sebagai unit yang 
menghasilkan 
nilai 
terukur 
bagi 
aktor, 
dinyatakan dengan kata 
kerja aktif. 
Association 
 
Garis lurus penghubung 
langsung antara aktor 
dengan use case yang 
menunjukkan 
keterlibatan komunikasi 
dua 
arah 
tanpa 
menyatakan 
urutan 
proses. 
Include 
 
Relasi di mana sebuah 
use case utama secara 
wajib 
menyertakan 
perilaku dari use case 
yang 
disertakan 
ke 
dalam 
alur utamanya 
agar use case utama 
tersebut dapat selesai 
Extend 
 
Relasi perluasan fungsi 
secara kondisional pada 
titik perluasan tertentu 
(extension point) yang 
27 
 
hanya dieksekusi dalam 
alur alternatif jika syarat 
terpenuhi. 
Generalization 
 
Hubungan 
hierarki 
umum 
dan 
khusus 
antaraktor atau antar-use 
case, di mana unsur 
turunan mewarisi akses 
spesifik 
dari 
unsur 
utama. 
  
2.1.6.​
Activity Diagram 
Activity Diagram digunakan untuk memvisualisasikan alur kerja , 
urutan aktivitas operasional, serta logika prosedural sistem dari awal 
hingga akhir (Hasanah & Untari, 2020). Berbeda dengan diagram alir 
konvensional (flowchart), activity diagram menggambarkan aktivitas 
komputasi yang berlangsung secara paralel (fork dan join). Untuk 
membantu 
pengembang 
dan 
pemangku 
kepentingan 
memahami 
bagaimana proses bisnis ditransformasikan ke dalam tahapan yang saling 
terhubung. 
Kelebihan utama dalam pemodelan activity diagram terletak pada 
pemanfaatan jalur tanggung jawab atau swimlane (Hasanah & Untari, 
2020). Melalui swimlane, diagram dibagi menjadi beberapa kolom vertikal 
atau horizontal yang merepresentasikan aktor atau entitas penanggung 
jawab dari setiap aksi. Format penulisan simbol activity diagram disajikan 
pada Tabel 2.4. 
 
28 
 
Tabel 2.4 Simbol Activity Diagram  
Nama Simbol 
Simbol 
Deskripsi 
Initial State 
 
Lingkaran 
hitam 
pekat 
yang menandai titik mula 
dimulainya 
suatu 
aliran 
proses bisnis atau alur kerja 
sistem. 
Action 
 
Persegi panjang bersudut 
tumpul 
yang 
merepresentasikan eksekusi 
aksi atau tugas operasional 
tertentu 
yang 
dilakukan 
oleh aktor atau sistem. 
Decision Node 
 
Simbol belah ketupat yang 
menunjukkan kondisi untuk 
menentukan satu jalur alur 
kerja berikutnya. 
Fork 
 
Simbol 
untuk 
memecah 
satu aliran kontrol tunggal 
menjadi dua atau lebih alur 
aktivitas 
yang 
berjalan 
serentak. 
Join 
 
Simbol 
yang 
berfungsi 
untuk 
menyinkronkan 
kembali 
beberapa 
alur 
paralel menjadi satu aliran 
tunggal setelah seluruh aksi 
terpenuhi. 
Final State 
 
Lingkaran 
berbingkai 
dengan 
titik 
hitam 
di 
tengah yang menandakan 
penyelesaian 
akhir 
dari 
seluruh 
siklus 
aktivitas 
sistem. 
29 
 
Swimlane 
 
Kolom pembatas vertikal 
atau 
horizontal 
yang 
mengelompokkan aktivitas 
berdasarkan 
pembagian 
wewenang peran aktor atau 
subsistem. 
 
2.1.7.​
Entity Relationship Diagram 
Entity 
Relationship 
Diagram 
(ERD) 
merupakan 
diagram 
pemodelan data yang digunakan untuk memvisualisasikan struktur 
penyimpanan data, entitas bisnis, atribut penyusun, serta hubungan 
relasional antarentitas dalam sistem database (Chen, 1976; Hasanah & 
Untari, 2020). Dalam siklus perancangan database, pemodelan data 
diawali dari identifikasi kebutuhan informasi pengguna (user view) yang 
kemudian dibuatkan ke dalam bentuk entitas dan keterkaitan logis 
antarentitas untuk mencegah terjadinya redundansi data serta anomali 
penyimpanan (Wibagso & Lia, 2020). Diagram ini sebagai dasar dalam 
pembentukan skema konseptual sebelum pengembang mengubahnya ke 
dalam skema relasional pada Database Management System (DBMS). 
Konsep pemodelan data ini pertama kali dirumuskan oleh Peter 
Chen melalui notasi grafis yang membedakan antara objek data, 
karakteristik objek, dan keterhubungan antarentitas (Chen, 1976). 
Komponen utama notasi Chen terdiri atas entitas (entity), entitas lemah 
(weak entity), relasi (relationship), dan atribut (attribute) yang disertai 
batasan derajat kardinalitas pemetaan (Hasanah & Untari, 2020). Entitas 
menyatakan objek nyata atau konseptual yang informasinya disimpan, 
relasi menggambarkan bentuk asosiasi antarobjek dengan simbol belah 
ketupat, 
sedangkan 
atribut 
menyatakan 
karakteristik 
data 
yang 
digambarkan dalam bentuk elips dan melekat pada entitas maupun relasi 
(Hasanah & Untari, 2020). Tabel 2.5 menyajikan simbol dan notasi 
pemodelan data. 
30 
 
Tabel 2.5 Unsur dan Notasi Entity Relationship Diagram  
Notasi 
Simbol 
Deskripsi  
Entity 
 
Persegi panjang tunggal 
yang merepresentasikan 
objek 
nyata 
atau 
konseptual 
yang 
memiliki 
keberadaan 
mandiri 
dan 
informasinya 
disimpan 
dalam sistem database. 
Weak Entity 
 
Persegi 
panjang yang 
merepresentasikan 
entitas 
yang 
keberadaannya 
bergantung mutlak pada 
entitas pemilik dan tidak 
memiliki kunci utama 
mandiri. 
Relationship 
 
Belah 
ketupat 
yang 
merepresentasikan 
asosiasi 
atau 
keterhubungan 
fungsional antara dua 
entitas atau lebih dalam 
sistem. 
Attribute 
 
Elips 
yang 
merepresentasikan 
karakteristik 
atau 
properti 
data 
spesifik 
yang 
mendeskripsikan 
suatu 
entitas 
maupun 
relasi. 
Key Attribute 
 
Elips dengan teks nama 
atribut bergaris bawah 
(underlined) 
yang 
menandakan 
atribut 
31 
 
pengidentifikasi 
unik 
(primary 
key) 
untuk 
membedakan setiap baris 
instansiasi entitas. 
Multivalued Attribute 
 
Elips 
yang 
merepresentasikan 
atribut 
yang 
dapat 
memiliki lebih dari satu 
nilai 
untuk 
sebuah 
kemunculan 
instansiasi 
entitas 
tunggal 
yang 
sama. 
Garis Kardinalitas (Link 
& Cardinality) 
 
Garis lurus penghubung 
antarkomponen 
yang 
dilengkapi notasi rasio 
kardinalitas 
pemetaan 
relasi, yaitu satu ke satu 
(1:1), satu ke banyak 
(1:N), atau banyak ke 
banyak (M:N). 
 
 
32 
 
2.1.8.​
Arsitektur Tiga Lapis (Three-Tier Architecture) 
Arsitektur tiga lapis (three-tier architecture) merupakan pola 
perancangan perangkat lunak terdistribusi yang membagi seluruh 
fungsionalitas sistem ke dalam tiga lapisan terpisah secara logis maupun 
fisik (Sommerville, 2011). Tiga lapisan utama dalam arsitektur ini 
mencakup lapisan presentasi antarmuka pengguna (Presentation Tier), 
lapisan logika pemrosesan bisnis aplikasi (Application Tier), dan lapisan 
penyimpanan data (Data Storage Tier) (Sommerville, 2011; Yusup dkk., 
2010). Lapisan presentasi beroperasi pada sisi perangkat pengguna, yang 
berfungsi menerima input serta menyajikan informasi visual tanpa 
melakukan manipulasi data secara langsung. Lapisan aplikasi bertindak 
sebagai pusat pengendali logika yang mengeksekusi aturan bisnis 
(business rules), memvalidasi hak akses otorisasi pengguna, serta 
mengelola alur kerja transaksi. Sementara itu, lapisan penyimpanan data 
bertugas menjamin persistensi, konsistensi, serta keutuhan data relasional 
melalui sistem manajemen basis data (Database Management System) 
(Yusup dkk., 2010). 
2.1.9.​
Next.js 
Next.js merupakan framework berbasis React yang digunakan 
untuk membangun antarmuka secara terstruktur dan efisien. Framework 
ini memiliki keunggulan utama berupa dukungan Server-Side Rendering 
(SSR) dan sistem perutean direktori halaman (Widarti & Akbar, 2026). 
Melalui konsep SSR, proses pengolahan data dan perenderan antarmuka 
diselesaikan terlebih dahulu di sisi server sebelum dokumen HTML 
dikirimkan ke browser pengguna (Widarti & Akbar, 2026). Pendekatan ini 
membuat waktu pemuatan halaman awal (initial page load) menjadi jauh 
lebih cepat, mengurangi beban komputasi pada perangkat, serta 
menghasilkan tampilan halaman yang lebih responsif saat menyajikan data 
dinamis. 
Selain meningkatkan performa kecepatan akses, arsitektur Next.js 
juga memberikan perlindungan tambahan pada aspek keamanan 
33 
 
komunikasi data. Menurut Widarti dan Akbar (2026), Next.js mampu 
menyembunyikan endpoint API backend dari inspect element pada 
browser 
pengguna 
melalui 
mekanisme 
internal 
route 
handlers. 
Framework ini juga menyediakan fitur middleware di sisi server yang 
bertindak sebagai penyaring awal untuk memeriksa status autentikasi 
cookies dan hak akses pengguna sebelum halaman ditampilkan (Widarti & 
Akbar, 2026). Melalui mekanisme tersebut, sistem dapat membatasi akses 
ke berbagai halaman administratif secara terstruktur dan memastikan 
bahwa fitur sensitif hanya dapat dibuka oleh pengguna yang memiliki 
kewenangan. 
2.1.10.​
Tailwind CSS 
Tailwind CSS merupakan framework CSS dengan pendekatan 
utility-first yang digunakan untuk membangun antarmuka web secara 
fleksibel dan efisien. Berbeda dari framework CSS konvensional yang 
menyediakan komponen siap pakai, Tailwind CSS menyediakan kumpulan 
utility yang dapat digunakan pada elemen HTML untuk mengatur tata 
letak, warna, jarak, dan tipografi (Santoso, 2025). Melalui pendekatan 
utilitas ini, proses perancangan desain antarmuka menjadi lebih leluasa 
karena pengembang tidak terikat pada gaya tampilan baku serta dapat 
menghemat penulisan baris kode CSS tambahan (Santoso, 2025).  
Selain memberikan keleluasaan dalam kustomisasi tampilan, 
Tailwind CSS memiliki keunggulan pada pengelolaan desain antarmuka 
yang responsif di berbagai perangkat. Menurut Santoso (2025), Tailwind 
CSS memanfaatkan varian penanda ukuran layar (breakpoint) seperti sm, 
md, dan lg untuk menyesuaikan susunan tata letak secara dinamis dari 
tampilan perangkat seluler hingga layar desktop. Penerapan utilitas ini juga 
mempermudah pemeliharaan kode program dalam jangka panjang karena 
fungsi dari setiap kelas visual terlihat secara jelas pada struktur dokumen 
antarmuka (Santoso, 2025).  
34 
 
2.1.11.​
Laravel 
Laravel merupakan framework dengan menggunakan bahasa 
pemrograman PHP yang dirancang untuk mempercepat perancangan dan 
implementasi perangkat lunak melalui penerapan pola arsitektur 
Model-View-Controller (MVC) (Tan, 2025). Menurut Tan (2025), 
keselarasan antara kerangka kerja Laravel dan desain sistem berbasis 
MVC membantu pengembang dalam menyusun struktur kode program 
secara teratur agar proses perancangan perangkat lunak berjalan dengan 
baik. Pemisahan tanggung jawab antarkomponen arsitektur tersebut 
membuat pemeliharaan kode program menjadi lebih terstruktur dan 
efisien. 
Pengelolaan data relasional dan keamanan hak akses pada 
framework Laravel didukung oleh dua fitur utama, yaitu Object-Relational 
Mapping (ORM) Eloquent dan lapisan middleware. Tan (2025) 
menjelaskan bahwa kelas model pada Laravel bertindak sebagai super 
class bagi seluruh entitas data yang memanfaatkan Eloquent ORM, 
sehingga interaksi basis data dapat dipetakan secara terstruktur ke dalam 
objek program. Selain itu, Laravel menyediakan lapisan middleware yang 
diimplementasikan pada tingkat kelas controller untuk memproses 
permintaan HTTP (HTTP request), memvalidasi autentikasi token, serta 
mengatur pembagian hak akses pengguna (multi-user access) berdasarkan 
relasi tabel peran (role) yang terhubung dalam database (Tan, 2025). 
2.1.12.​
REST API 
Representational 
State 
Transfer 
Application 
Programming 
Interface (REST API) merupakan arsitektur web yang digunakan untuk 
memfasilitasi pertukaran data antarsistem secara terstruktur melalui 
protokol standar Hypertext Transfer Protocol (HTTP). Arsitektur ini 
menerapkan prinsip pemisahan tugas (separation of concerns) antara sisi 
klien dan server, di mana setiap data atau entitas diakses sebagai sumber 
daya (resource) melalui alamat endpoint yang seragam (Haryono dkk., 
2025). Dalam pola komunikasi ini, interaksi bersifat stateless, artinya 
35 
 
server tidak menyimpan riwayat sesi antarpermintaan sehingga setiap 
permintaan dari klien wajib memuat seluruh informasi dan parameter yang 
dibutuhkan secara lengkap (Tanaem dkk., 2016). Format data yang umum 
digunakan dalam pengiriman muatan data (payload) adalah JavaScript 
Object Notation (JSON), yang memiliki struktur ringan sehingga 
mempercepat proses serialisasi serta transmisi data antarkomponen 
aplikasi. 
Selain menyederhanakan integrasi antarsistem, REST API 
memanfaatkan metode standar HTTP untuk mendefinisikan tindakan 
operasional terhadap sumber daya data. Keempat metode HTTP yang 
umum digunakan dalam REST API, yaitu GET untuk membaca data, 
POST untuk membuat data baru, PUT untuk memperbarui data, dan 
DELETE untuk menghapus data. Tanaem dkk. (2016) menambahkan 
bahwa aspek keamanan komunikasi data pada REST API diperkuat 
melalui mekanisme autentikasi token yang disematkan pada bagian header 
permintaan HTTP untuk memvalidasi hak akses klien sebelum permintaan 
diproses oleh server.  
2.1.13.​
MySQL 
MySQL adalah salah satu sistem manajemen basis data relasional 
Relational Database Management System (RDBMS) yang mengorganisasi 
data ke dalam bentuk tabel-tabel berelasi. Menurut Ilham dkk. (2026), 
struktur 
tabel 
pada 
MySQL 
menghubungkan 
baris 
antarentitas 
menggunakan atribut primary key dan foreign key untuk mencegah 
anomali serta redundansi data. Dengan menerapkan mekanisme validasi 
skema saat penulisan (schema-on-write), di mana setiap atribut data yang 
masuk diverifikasi tipe, panjang, dan batasannya agar selalu mematuhi 
aturan relasional yang telah ditetapkan (Ilham dkk., 2026).  
Keunggulan dari MySQL terletak pada kemampuannya menjaga 
konsistensi data melalui penegakan prinsip ACID (Atomicity, Consistency, 
Isolation, Durability). Ilham dkk. (2026) menjelaskan bahwa prinsip 
ACID menjamin setiap rangkaian operasi manipulasi data diselesaikan 
36 
 
secara menyeluruh atau dibatalkan sepenuhnya jika terjadi kesalahan 
sistem, sehingga risiko data tersimpan secara parsial dapat dihindari. 
Sehingga, MySQL sangat efektif digunakan untuk menangani data 
transaksional yang bersifat kritikal, seperti pencatatan transaksi keuangan, 
mutasi pembayaran, dan pemrosesan data antarentitas yang menuntut 
akurasi tinggi (Ilham dkk., 2026).  
2.1.14.​
Black Box Testing 
Black Box Testing merupakan metode pengujian perangkat lunak 
untuk evaluasi fungsionalitas sistem berdasarkan spesifikasi kebutuhan 
tanpa memeriksa struktur kode internal maupun logika algoritma di 
dalamnya. Pengujian ini mengevaluasi kesesuaian antara data masukan 
dengan luaran yang dihasilkan untuk mendeteksi potensi anomali pada 
antarmuka, fungsionalitas sistem, dan pemrosesan data (Fadhilasari dkk., 
2024). Menurut Fadhilasari dkk. (2024), efisiensi black box testing dapat 
dioptimalkan melalui teknik Equivalence Partitioning yang membagi 
domain masukan ke dalam data valid dan tidak valid. Melalui pembagian 
tersebut, penguji cukup memilih sampel representatif dari setiap kelompok 
nilai untuk memverifikasi perilaku sistem tanpa harus menguji seluruh 
kemungkinan kombinasi data secara berulang. 
Selain membagi kelompok data, black box testing diperkuat 
dengan penerapan teknik Boundary Value Analysis (BVA) untuk 
memeriksa area batas masukan. Fadhilasari dkk. (2024) menjelaskan 
bahwa teknik BVA berfokus pada pengujian nilai ekstrem di sekitar batas 
atas dan batas bawah masukan. Penggabungan antara Equivalence 
Partitioning dan Boundary Value Analysis menghasilkan skenario kasus 
uji yang lebih terarah dan mampu menemukan cacat validasi data yang 
berpotensi terlewatkan (Fadhilasari dkk., 2024).  
2.1.15.​
User Acceptance Testing 
User Acceptance Testing (UAT) yaitu tahapan pengujian perangkat 
lunak yang dilakukan langsung oleh pengguna akhir (end-user) untuk 
memverifikasi apakah sistem yang dikembangkan telah memenuhi 
37 
 
kebutuhan operasional. Berbeda dari pengujian yang dilakukan oleh 
pengembang, UAT berfokus pada pengalaman interaksi pengguna dalam 
menjalankan tugas fungsional sesuai peran dan alur kerja masing-masing 
(Apriyanti dkk., 2024). Menurut Apriyanti dkk. (2024), User Acceptance 
Testing dilakukan dengan menguji skenario operasional untuk menilai 
kemudahan penggunaan, kejelasan antarmuka, serta proses bisnis yang 
sesuai. 
Selain 
mengevaluasi alur operasional, UAT menggunakan 
instrumen kuesioner untuk mengukur persepsi kepuasan dan tingkat 
penerimaan 
pengguna 
secara 
kuantitatif. 
Apriyanti 
dkk. 
(2024) 
menjelaskan bahwa pengukuran kepuasan pengguna dapat menerapkan 
kuesioner berskala Likert lima poin yang memuat kriteria penilaian dari 
Sangat Tidak Setuju hingga Sangat Setuju. Hasil jawaban kuesioner 
tersebut kemudian dihitung nilai persentasenya dan dikelompokkan ke 
dalam rentang bobot evaluasi untuk menentukan kategori kelayakan sistem 
secara objektif (Apriyanti dkk., 2024).  
38 
 
2.2.​
Penelitian Terdahulu 
Kajian terhadap penelitian terdahulu dilakukan untuk memahami konteks permasalahan serta membangun landasan 
perancangan bagi sistem yang dikembangkan. Berikut adalah rangkuman hasil penelitian terdahulu yang memiliki keterkaitan dengan 
penelitian yang dilakukan, sebagaimana disajikan pada Tabel 2.6. 
Tabel 2.6 Penelitian Terdahulu 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
1 
Satria 
Nur 
Fajriansyah, 
Muhammad 
Subaktiar 
Wijaya, Daffa Arifta Eryana, 
Alaudin Safa, Harsya Rafif 
Pramadhan, 
Arya 
Wicaksono, 
Muhammad 
Ilham 
Baehaqi, 
Filius 
Deivivi, 
Dandy 
Nurfajriansyah, dan Sopiyan 
Apandi (2026). 
Pengelolaan 
operasional bimbingan 
belajar 
masih 
mengandalkan Google 
Forms, 
spreadsheet, 
dan grup pesan instan, 
sehingga 
memicu 
jadwal 
kelas 
tidak 
terstruktur, 
data 
peserta didik tersebar, 
dan minim proteksi 
keamanan 
data 
akademik. 
Waterfall 
Menghasilkan Sistem Informasi 
Bimbingan 
Belajar 
(SIMB) 
berbasis web dengan Laravel 
dan SQLite yang memfasilitasi 
modul pendaftaran online, log 
belajar, dan konfirmasi akun. 
Pengujian Black Box Testing 
membuktikan 
fungsionalitas 
berjalan 
valid, 
memangkas 
durasi verifikasi pendaftaran di 
bawah 
dua 
detik, 
serta 
meniadakan potensi benturan 
jadwal mengajar hingga nol 
persen. 
Persamaan: Digitalisasi tata 
kelola 
administrasi 
operasional 
bimbingan 
belajar nonformal. 
Perbedaan: Sistem rujukan 
berfokus pada operasional 
satu unit cabang dengan 
registrasi 
mandiri 
siswa, 
sedangkan sistem ARTHA 
mengelola delapan kantor 
cabang 
terpadu 
dengan 
pembatasan 2 hak akses, 
pendaftaran siswa di cabang, 
kendali 
kuota 
kelompok 
belajar, 
rekonsiliasi 
kas, 
serta menggunakan metode 
39 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
Personal 
Extreme 
Programming (PxP). 
2 
Teddy 
Marcus 
Zakaria, 
Julianti 
Kasih, 
Natanael 
Halim, 
dan 
Michael 
Sebastian Gunadi (2023). 
Tata 
kelola 
administrasi 
pembayaran 
iuran 
kursus 
masih 
menggunakan kuitansi 
fisik dan pembukuan 
manual, 
sehingga 
rawan kehilangan data, 
memperlambat 
rekapitulasi 
kas 
masuk, 
serta 
menyulitkan pencarian 
status keaktifan murid. 
Waterfall 
Menghasilkan sistem informasi 
pembayaran kursus berbasis 
Desktop 
Windows 
(MandarinPro) 
yang 
memfasilitasi registrasi siswa 
baru, pemrosesan pembayaran 
uang 
les, 
serta 
penerbitan 
laporan kas harian dan bulanan. 
Pengujian 
Alpha dan Beta 
Testing membuktikan seluruh 
fungsi transaksi berjalan valid 
sesuai kebutuhan operasional 
lembaga. 
Persamaan: 
Digitalisasi 
administrasi pencatatan kas 
masuk 
pembayaran 
iuran 
pendidikan kursus. 
Perbedaan: 
Dibangun 
berbasis 
aplikasi 
desktop 
Windows 
untuk 
satu 
lembaga 
kursus 
mandiri, 
sedangkan sistem ARTHA 
dirancang berbasis aplikasi 
web terpadu untuk delapan 
kantor 
cabang 
dengan 
rekonsiliasi mutasi kas dan 
menggunakan 
metode 
Personal 
Extreme 
Programming (PxP). 
40 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
3 
Ahmad 
Husna 
Ahadi, 
Pariyadi, 
dan 
Teuku 
Djauhari (2025). 
Rencana 
ekspansi 
penambahan 
unit 
cabang 
operasional 
terhambat 
karena 
sistem eksisting belum 
mendukung 
integrasi 
multicabang, sehingga 
menyulitkan 
manajemen 
pusat 
dalam memantau data 
cabang, 
reservasi 
kamar, dan konsolidasi 
laporan pendapatan. 
Waterfall 
Menghasilkan sistem informasi 
manajemen 
multicabang 
berbasis 
web 
yang 
memfasilitasi 
pendaftaran 
cabang baru, reservasi kamar, 
pencatatan 
transaksi 
pembayaran, dan konsolidasi 
laporan pendapatan. Pengujian 
Black 
Box 
Testing 
membuktikan seluruh skenario 
modul antarcabang berfungsi 
dengan benar. 
Persamaan: 
Penerapan 
arsitektur sistem informasi 
manajemen 
multicabang 
terintegrasi berbasis web. 
Perbedaan: Sistem rujukan 
diterapkan 
pada 
sektor 
industri perhotelan dengan 
metode Waterfall, sedangkan 
sistem ARTHA diterapkan 
pada operasional bimbingan 
belajar 
delapan 
cabang 
dengan 
validasi 
kuota 
kelompok 
belajar, 
rekonsiliasi 
kas, 
serta 
menggunakan 
metode 
Personal 
Extreme 
Programming (PxP). 
41 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
4 
Bagus 
Sudirman 
dan 
Mawada Tristianti (2021). 
Pengendalian transaksi 
kas 
internal 
belum 
menerapkan 
proses 
rekonsiliasi 
bank 
berkala 
secara 
terkomputerisasi, 
sehingga 
memicu 
risiko 
selisih 
pencatatan antara buku 
kas perusahaan dan 
rekening koran bank. 
Research and 
Development 
(R&D)  
Menghasilkan sistem informasi 
pengendalian kas bank berbasis 
web 
yang 
menyediakan 
antarmuka 
pencatatan 
penerimaan 
kas, 
formulir 
pengeluaran, serta pembuatan 
laporan rekonsiliasi kas bank 
otomatis dengan pemisahan hak 
akses antara staf kasir dan 
pimpinan. 
Persamaan: 
Penerapan 
konsep rekonsiliasi mutasi 
rekening koran perbankan 
guna 
mencocokkan 
pencatatan 
kas 
internal 
dengan rekening bank. 
Perbedaan: Berfokus pada 
pengendalian 
kas 
entitas 
bisnis perdagangan dengan 
pendekatan 
prototyping, 
sedangkan sistem ARTHA 
mengintegrasikan verifikasi 
mutasi ke dalam arsitektur 
web multicabang bimbingan 
belajar 
menggunakan 
metode Personal Extreme 
Programming (PxP). 
42 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
5 
Nur Khafidhoh, Arfia Rahmi 
Febrianti, 
dan 
Sujono 
(2026). 
Pengelolaan 
jadwal 
kegiatan 
bimbingan 
belajar 
masih 
dilakukan 
secara 
manual, 
sehingga 
berpotensi 
memicu 
benturan alokasi jam 
mengajar 
guru, 
ketidakmerataan beban 
tugas, 
serta 
menyulitkan 
penyesuaian 
jadwal 
belajar siswa. 
Waterfall 
Menghasilkan sistem informasi 
penjadwalan bimbingan belajar 
berbasis web yang menerapkan 
optimasi Algoritma Genetika 
dengan 
mempertimbangkan 
ketersediaan jam mengajar guru 
dan preferensi siswa. Pengujian 
sistem membuktikan otomasi 
jadwal mampu meminimalkan 
potensi 
konflik 
jadwal 
mengajar. 
Persamaan: 
Pengelolaan 
alokasi waktu dan kelompok 
belajar 
pada 
domain 
bimbingan 
belajar 
nonformal. 
Perbedaan: Berfokus pada 
optimasi 
penugasan 
mengajar guru di satu lokasi 
menggunakan 
algoritma 
genetika, sedangkan sistem 
ARTHA 
berfokus 
pada 
validasi 
batas 
kuota 
kapasitas fisik ruang kelas 
per kelompok belajar pada 
delapan 
kantor 
cabang 
menggunakan 
metode 
Personal 
Extreme 
Programming (PxP). 
43 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
6 
Herfina 
Intan 
Yuanita, 
Bangun 
Wijayanto, 
dan 
Teguh Cahyono (2022). 
Penyusunan 
jadwal 
perkuliahan 
tanpa 
validasi kapasitas fisik 
ruangan 
mengakibatkan 
kelebihan kuota kelas 
dan 
ketidakefisienan 
alokasi ruang, disertai 
proses kompilasi data 
manual 
yang 
memakan 
waktu 
berminggu-minggu. 
DevOps 
Menghasilkan 
antarmuka 
sistem 
penjadwalan 
perkuliahan 
terintegrasi 
berbasis 
React.js 
yang 
memvalidasi 
kapasitas 
daya 
tampung 
ruangan 
dan 
menyajikan visualisasi model 
rekomendasi jadwal. Pengujian 
Black 
Box 
Testing 
membuktikan 
seluruh 
komponen 
antarmuka 
pengguna berhasil terhubung 
valid dengan backend API. 
Persamaan: 
Penerapan 
mekanisme 
batas 
daya 
tampung kuota ruangan kelas 
untuk mencegah kelebihan 
kapasitas belajar. 
Perbedaan: 
Penelitian 
berfokus 
pada 
pengembangan 
antarmuka 
perkuliahan 
oleh 
tim 
pengembang 
dengan 
pendekatan 
DevOps, 
sedangkan sistem ARTHA 
membangun sistem penuh 
secara mandiri untuk delapan 
cabang bimbingan belajar 
dengan 
metode 
Personal 
Extreme 
Programming 
(PxP). 
44 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
7 
Aolia Musofa, Sofiansyah 
Fadli, Wafiah Murniati, dan 
Hairul Fahmi (2025). 
Pencatatan data tamu 
pada 
instansi 
kedinasan 
masih 
menggunakan 
buku 
register fisik, sehingga 
pencarian 
arsip 
riwayat 
kunjungan 
lambat, 
data rentan 
tersebar, 
serta 
penyusunan 
laporan 
berkala 
belum 
terintegrasi otomatis. 
Personal 
Extreme 
Programming 
(PxP) 
Menghasilkan Aplikasi Buku 
Tamu Digital berbasis web 
melalui tujuh tahapan PxP oleh 
pengembang tunggal dengan 
integrasi pemindaian QR Code. 
Pengujian fungsionalitas Black 
Box Testing berjalan valid 
seratus persen pada delapan 
puluh skenario uji, didukung 
waktu tanggap sistem sebesar 
312 ms dan akurasi verifikasi 
data sebesar 98,7%. 
Persamaan: 
Penerapan 
tujuh tahapan siklus metode 
Personal 
Extreme 
Programming (PxP) secara 
komprehensif 
oleh 
pengembang mandiri. 
Perbedaan: Sistem rujukan 
diterapkan pada pelayanan 
buku 
tamu satu instansi 
pemerintah 
daerah, 
sedangkan sistem ARTHA 
menerapkan 
PxP 
pada 
operasional bisnis delapan 
cabang bimbingan belajar 
yang 
mengintegrasikan 
transaksi kas masuk dan 
validasi 
kuota 
kelompok 
belajar. 
45 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
8 
Narti Apriyanti, Seftin Fitri 
Ana Wati, dan Abdul Rezha 
Efrat Najaf (2024). 
Pengelolaan 
dan 
pemasaran 
penjualan 
tanah kavling masih 
manual menggunakan 
pembukuan fisik dan 
brosur, 
sehingga 
membatasi 
promosi 
properti, 
memperlambat 
verifikasi 
berkas 
pembeli, 
serta 
memperbesar 
risiko 
data transaksi tercecer. 
Personal 
Extreme 
Programming 
(PxP) 
Menghasilkan 
situs 
web 
pemasaran 
dan 
penjualan 
properti 
(E-Kavling) 
yang 
memfasilitasi 
penelusuran 
kavling, 
pemesanan 
unit, 
pengunggahan 
berkas 
administrasi, dan validasi bukti pembayaran. Pengujian 
Black 
Box 
Testing 
membuktikan 
seluruh 
alur 
transaksi valid seratus persen, 
didukung 
evaluasi 
User 
Acceptance 
Testing 
(UAT) 
dengan persentase keberhasilan 
91% (kategori Sangat Baik). 
Persamaan: 
Efektivitas 
penerapan metode PxP oleh 
pengembang 
tunggal 
dan 
perancangan modul validasi bukti pembayaran. 
Perbedaan: Sistem rujukan 
menangani 
penjualan 
properti 
kavling 
tunggal 
tanpa modul rekonsiliasi kas, 
sedangkan sistem ARTHA 
mengintegrasikan 
rekonsiliasi mutasi rekening 
dan kendali kuota kelas pada 
delapan 
kantor 
cabang 
bimbingan belajar. 
46 
 
No 
Penulis dan Tahun 
Permasalahan 
Metode 
Hasil Penelitian 
Keterkaitan 
9
Mugi Praseptiawan, Meida Cahyo Utoro, Ilham Firman Ashari, Muhammad Habib Algifari, dan Aidil Afriansyah (2025).
Sistem perbankan mini di SMK Negeri 7 Bandar Lampung belum berjalan optimal akibat pengelolaan data pengguna yang masih manual, pencatatan transaksi yang belum terotomatisasi, serta sistem keamanan login yang minim sehingga rentan terhadap akses tidak sah. Selain itu, ketiadaan integrasi pembayaran secara daring memperlambat pemrosesan iuran SPP dan tabungan siswa sehingga menimbulkan inefisiensi operasional serta risiko kesalahan pencatatan transaksi.
Personal Extreme Programming (PXP)
Menghasilkan situs web perbankan mini sekolah (m-EduPayment) melalui tahapan PXP yang terintegrasi dengan Application Programming Interface (API) gerbang pembayaran iPaymu untuk melayani transaksi pembayaran SPP, tabungan, dan bank sampah secara daring. Pengujian fungsionalitas sistem menggunakan Postman dan Selenium IDE mencapai tingkat keberhasilan 99%, didukung evaluasi System Usability Scale (SUS) pada tiga puluh satu responden yang memperoleh skor rata-rata 91 dengan kategori Excellent (Grade A).
Persamaan: Penerapan tahapan metodologi Personal Extreme Programming (PXP) oleh pengembang tunggal dalam merancang sistem transaksi pembayaran iuran pendidikan berbasis web. Keduanya sama-sama memfasilitasi digitalisasi pencatatan administrasi keuangan lembaga pendidikan.

Perbedaan: Sistem rujukan mengintegrasikan Application Programming Interface (API) gerbang pembayaran pihak ketiga (iPaymu) untuk transaksi SPP, tabungan, dan bank sampah pada satu sekolah kejuruan. Sementara itu, sistem ARTHA berfokus pada sistem informasi operasional dan keuangan tanpa gerbang pembayaran pihak ketiga yang mengintegrasikan validasi kuota kelompok belajar dan pencatatan kas internal pada delapan kantor cabang bimbingan belajar.
47

No
Penulis dan Tahun
Permasalahan
Metode
Hasil Penelitian
Keterkaitan
10
Gita Indah Marthasari, Wildan Suharso, dan Frendy Ardiansyah (2018).
Layanan perpustakaan di Kejaksaan Negeri Kota Batu menghadapi kendala pencarian buku yang lambat akibat penggunaan katalog kertas fisik yang rentan rusak atau hilang, ketiadaan media pengingat otomatis batas waktu peminjaman yang memicu keterlambatan pengembalian buku, serta pustakawan yang harus menulis ulang data transaksi secara manual dari awal. Selain itu, pemahaman kebutuhan fungsional perangkat lunak oleh pengguna yang belum terinci berpotensi memunculkan perubahan kebutuhan yang dinamis selama proses pengembangan dan memperpanjang durasi proyek apabila menggunakan metodologi konvensional.
Personal Extreme Programming (PXP) dengan Skala Prioritas MoSCoW
Menghasilkan sistem informasi perpustakaan Kejaksaan Negeri Kota Batu berbasis web melalui metode PXP yang dipadukan dengan teknik prioritas MoSCoW untuk menetapkan kebutuhan berdasarkan nilai bisnis dan risiko teknis. Perencanaan rilis berhasil memetakan enam belas cerita pengguna (user stories) dengan estimasi satu story point per kebutuhan (setara tiga hari kerja) ke dalam empat siklus iterasi dengan nilai velocity sebesar empat poin per iterasi. Penerapan Test Driven Development (TDD) melalui tahapan unit testing, code generation, dan refactoring menghasilkan kelolosan unit testing seratus persen serta memenuhi seluruh kriteria User Acceptance Test (UAT) secara valid.
Persamaan: Penerapan metodologi Personal Extreme Programming (PXP) oleh pengembang tunggal dengan pemodelan User Stories, pembobotan tingkat kesulitan (story points), serta penyelesaian sistem dalam empat siklus iterasi pengembangan. Keduanya sama-sama memfasilitasi keterlibatan intensif pengguna dan menerapkan verifikasi fungsionalitas melalui pengujian unit dan pengujian penerimaan pengguna.

Perbedaan: Sistem rujukan berfokus pada otomasi perpustakaan satu lokasi dengan pengujian penerimaan pengguna sebatas ceklis biner kualitatif (tabel kriteria terpenuhi atau tidak). Sementara itu, sistem ARTHA berfokus pada operasional dan keuangan delapan cabang bimbingan belajar dengan evaluasi User Acceptance Testing (UAT) menggunakan kuesioner berskala Likert lima poin guna mengukur persentase kepuasan pengguna secara kuantitatif.
48

(Halaman Sengaja Dikosongkan)
49
