# BAB 3

## RANCANGAN PROTOTIPE

Bab ini menguraikan rancangan prototipe sistem informasi manajemen operasional terintegrasi yang dikembangkan untuk Bimbingan Belajar Artha Balikpapan. Pembahasan disajikan secara sistematis meliputi gambaran umum prototipe, tahapan siklus hidup pengembangan, prosedur pelaksanaan teknis, konsep arsitektur fungsional dan data, spesifikasi teknis lingkungan komputasi, hingga jadwal pengerjaan proyek secara terperinci. Seluruh sistematika pembahasan ini disusun mengacu pada ketentuan pedoman penulisan tugas akhir jalur prototipe di lingkungan Program Studi Sistem Informasi (Institut Teknologi Kalimantan, 2025b).

## 3.1 Garis Besar Prototipe

Bimbingan Belajar Artha Balikpapan saat ini mengelola delapan cabang operasional dengan aktivitas administrasi yang mencakup registrasi siswa, penempatan kelompok belajar, penjadwalan tentor, serta pengelolaan pembayaran biaya bimbingan. Seluruh proses operasional tersebut memerlukan integrasi data yang andal agar catatan transaksi di tingkat cabang dapat terkonsolidasi dan dipantau secara langsung oleh manajemen pusat. Berdasarkan kebutuhan strategis tersebut, prototipe ARTHA dirancang sebagai platform sistem informasi berbasis web terintegrasi dengan pembagian hak akses bertingkat, yaitu Admin Cabang dan Super Admin.

### 3.1.1 Objek dan Konteks Pengembangan

Pengembangan sistem informasi ARTHA berakar dari hasil eksplorasi empiris melalui wawancara mendalam bersama pihak manajemen dan staf administrasi mengenai tata kelola data operasional yang berjalan saat ini. Temuan lapangan tersebut mengonfirmasi urgensi unifikasi basis data guna menjembatani pengelolaan data siswa, pengaturan jadwal pembelajaran, serta rekonsiliasi kas dalam satu ekosistem digital. Urgensi integrasi proses bisnis lembaga pendidikan nonformal ini sejalan dengan temuan penelitian terdahulu yang menekankan pentingnya sinkronisasi data antarunit kerja untuk mencegah redundansi dan inefisiensi administrasi (Fajriansyah dkk., 2026; Gunawan dkk., 2025).

### 3.1.2 Ruang Lingkup dan Pengguna Prototipe

Arsitektur fungsional ARTHA mengakomodasi diferensiasi tanggung jawab antara operasional cabang dan fungsi pengawasan di tingkat pusat. Admin Cabang berfokus pada eksekusi pencatatan operasional harian pada cabang penugasannya masing-masing, sedangkan Super Admin memegang otoritas pengendalian sistem, peninjauan transaksi lintas cabang, serta analisis keuangan agregat. Model pembatasan hak akses berbasis lokasi kerja dan peran manajerial semacam ini terbukti efektif dalam menjaga integritas data sekaligus menyederhanakan alur kerja organisasi multicabang (Ahadi dkk., 2025; Thiovanda, 2026).

Pada aspek penagihan, sistem menyediakan fitur pemantauan tunggakan yang terhubung langsung dengan tautan pesan WhatsApp semiotomatis (*click to chat*) untuk memudahkan komunikasi dengan wali siswa. Melalui mekanisme tersebut, sistem secara otomatis menyusun rincian tagihan dan nomor tujuan, kemudian staf administrasi dapat meninjau serta mengirimkan pesan secara mandiri melalui aplikasi perpesanan resmi. Sementara itu, pengelolaan kelas dilengkapi visualisasi keterisian ruang secara dinamis guna memandu penempatan siswa baru, di mana sistem secara otomatis memblokir penambahan peserta saat kapasitas maksimum tercapai dan membuka kembali kuota kelas ketika masa keanggotaan siswa diakhiri.

Alur verifikasi pembayaran non-tunai (transfer bank) dirancang melalui pemisahan tugas (*segregation of duties*), yakni pengunggahan bukti bayar dilakukan oleh Admin Cabang, sedangkan persetujuan mutasi dana menjadi wewenang penuh Super Admin. Pembagian otoritas verifikasi rekening beserta personel pemeriksanya akan difinalisasi bersama pihak manajemen mitra sebelum sistem diuji coba. Adapun batasan ruang lingkup pengembangan prototipe ini berfokus pada administrasi internal dan rekonsiliasi kas manual, sehingga pembelajaran daring (*e-learning*), pengiriman pesan otomatis melalui *gateway*, serta integrasi *payment gateway* perbankan berada di luar lingkup penelitian.

### 3.1.3 Pendekatan Pengembangan Prototipe

Pengembangan prototipe ARTHA dilaksanakan secara mandiri menggunakan kerangka kerja *Personal Extreme Programming* (PxP). Metodologi ini memadukan kedisiplinan pencatatan waktu dan metrik perangkat lunak dari *Personal Software Process* (PSP) dengan kelincahan serta fleksibilitas *Extreme Programming* (XP) (Dzhurov dkk., 2009). Rangkaian tahapan PxP yang diterapkan mencakup analisis kebutuhan, perencanaan, inisialisasi iterasi, perancangan sistem, implementasi kode program, pengujian sistem, hingga evaluasi retrospektif. Efektivitas PxP bagi pengembang tunggal dalam menghasilkan perangkat lunak yang adaptif terhadap dinamika kebutuhan pengguna telah banyak dibuktikan pada berbagai studi terapan di Indonesia (Fikri & Arthawan, 2020; Sidiq dkk., 2025; Apriyanti dkk., 2024).

### 3.1.4 Luaran yang Ditargetkan

Luaran utama yang ditargetkan dari pelaksanaan tugas akhir ini adalah sebuah prototipe perangkat lunak sistem informasi manajemen operasional yang fungsional, disertai bundel dokumentasi teknis, artefak perancangan, dan laporan evaluasi empiris bersama pengguna akhir. Pengembangan sistem ini ditargetkan mencapai Tingkat Kesiapan Teknologi (TKT) Level 5, yakni teknologi telah divalidasi dan diuji coba pada lingkungan operasional yang sesungguhnya bersama mitra bimbingan belajar (Institut Teknologi Kalimantan, 2026).

Seluruh dokumentasi teknis dan log aktivitas pengembangan disusun secara berkesinambungan bersamaan dengan penulisan kode program. Dokumentasi komprehensif ini disiapkan untuk melengkapi naskah laporan tugas akhir, publikasi artikel ilmiah, serta berkas permohonan pencatatan Hak Kekayaan Intelektual (HKI) berupa Hak Cipta Perangkat Lunak. Penyajian artefak penelitian yang transparan dan sistematis memungkinkan verifikasi kualitas sistem dapat ditelusuri secara utuh dari tahap analisis hingga penerimaan mitra.

## 3.2 Tahapan Pembuatan Prototipe

Tahapan pembuatan prototipe ARTHA dirancang mengikuti siklus hidup berulang (*iterative lifecycle*) dari metodologi *Personal Extreme Programming* (PxP). Pendekatan ini memungkinkan pengembangan sistem dilakukan secara bertahap dan terukur, di mana setiap fase menghasilkan luaran konkret yang menjadi fondasi bagi fase berikutnya. Fleksibilitas PxP memberikan ruang adaptasi bagi pengembang untuk menyempurnakan fungsi sistem apabila ditemukan kendala teknis atau pergeseran kebutuhan operasional dari pihak mitra. Keterkaitan logis dan jalur umpan balik antartahapan pengembangan disajikan pada Gambar 3.1.

![Diagram alir pembuatan prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_1_Alur_Pembuatan_Prototipe.png>)

**Gambar 3.1 Alur Pembuatan Prototipe Sistem Informasi ARTHA**

Sumber: Dzhurov dkk. (2009), telah disesuaikan dengan penambahan evaluasi pengguna dan penyiapan luaran penelitian.

Siklus pengembangan diawali dengan perumusan spesifikasi kebutuhan fungsional yang kemudian dipetakan ke dalam daftar prioritas pekerjaan (*product backlog*). Pengembang merancang arsitektur modul dan mengimplementasikan kode program secara terstruktur, kemudian memverifikasi kesesuaian perilakunya melalui pengujian unit dan pengujian sistem berbasis *Black Box Testing*. Pada akhir setiap iterasi, pengembang melaksanakan sesi retrospektif untuk menelaah performa pengerjaan, mencatat anomali kode (*defect log*), serta membandingkan estimasi waktu terhadap durasi aktual guna mengoptimalkan perencanaan iterasi berikutnya.

Apabila hasil pengujian sistem menunjukkan adanya ketidaksesuaian atau cacat logika, pengembang segera melakukan perbaikan kode (*debugging*) dan menjalankan pengujian regresi sebelum iterasi dinyatakan selesai (*definition of done*). Fitur-fitur yang belum terselesaikan dialokasikan kembali ke dalam rencana iterasi lanjutan berdasarkan tingkat ketergantungan antarmodul. Setelah seluruh fungsionalitas inti berhasil dibangun dan lulus verifikasi internal, prototipe kemudian dievaluasi secara langsung oleh calon pengguna melalui *User Acceptance Testing* (UAT).

Umpan balik dan catatan perbaikan yang diperoleh selama sesi UAT diklasifikasikan secara cermat berdasarkan karakteristik masalahnya. Penyesuaian yang menyangkut perubahan alur bisnis akan ditelaah kembali pada tahap analisis kebutuhan dan perencanaan, sedangkan temuan berupa kendala teknis ditangani langsung melalui fase implementasi dan pengujian ulang. Hasil evaluasi akhir UAT menjadi dasar penentuan tingkat penerimaan sistem oleh mitra sekaligus menandai kesiapan prototipe untuk diserahkan.

Penerapan metodologi PxP yang dipadukan dengan pengujian sistem yang ketat serta keterlibatan aktif pengguna akhir mengadopsi kerangka kerja yang telah terbukti berhasil pada riset-riset sejenis (Apriyanti dkk., 2024; Dzhurov dkk., 2009). Dalam konteks ARTHA, skenario evaluasi disusun secara representatif mencakup seluruh spektrum tugas operasional cabang dan fungsi pengawasan terpusat. Rincian kegiatan utama beserta luaran yang direncanakan pada setiap fase pengembangan dirangkum pada Tabel 3.1.

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

Prosedur penelitian memaparkan tahapan operasional dan metodologis yang ditempuh dalam merealisasikan prototipe ARTHA, mulai dari fase elisitasi kebutuhan hingga evaluasi penerimaan pengguna. Pada setiap tahapan, instrumen penelitian, sumber data empiris, serta hasil pengujian didokumentasikan secara terstruktur guna menjamin keterlacakan (*traceability*) dan validitas ilmiah. Uraian prosedur ini menjadi pedoman baku pengembangan sekaligus jembatan pembuktian antara permasalahan nyata di Bimbingan Belajar Artha dengan solusi sistem yang diusulkan.

### 3.3.1 Penggalian Kebutuhan (*Requirements*)

Tahap penggalian kebutuhan diawali dengan analisis mendalam terhadap transkrip wawancara yang telah dilakukan bersama pengelola dan staf administrasi Artha. Informasi faktual di dalamnya diklasifikasikan ke dalam enam domain operasional utama, yaitu pendaftaran siswa, penetapan skema tarif, transaksi pembayaran, tata kelola kelas, penjadwalan tentor, serta pelaporan keuangan cabang. Pengelompokan tematik ini membantu mengidentifikasi dependensi antarfungsi sekaligus memetakan area operasional yang masih memerlukan klarifikasi teknis lebih lanjut.

Proses klarifikasi diarahkan langsung kepada pemangku kepentingan yang memiliki otoritas dan pemahaman operasional pada domain terkait. Pengelola pusat dimintai konfirmasi mengenai kebijakan pemantauan manajerial dan pemisahan wewenang, sedangkan staf administrasi memberikan penjelasan faktual seputar rutinitas pencatatan di tingkat cabang. Pembagian informan ini memastikan bahwa setiap butir kebutuhan sistem dirumuskan berdasarkan sumber data primer yang kredibel dan akuntabel.

Setiap sesi klarifikasi dilengkapi dokumentasi formal yang mencakup profil informan, representasi cabang, waktu pelaksanaan, serta justifikasi pemilihan narasumber. Ketentuan operasional yang bersifat unik pada cabang tertentu diuji silang bersama pengelola pusat guna memastikan apakah ketentuan tersebut dapat distandardisasi menjadi aturan sistem lintas cabang. Rekapitulasi profil narasumber dan kode sumber data elisitasi disajikan secara rinci pada dokumentasi penelitian.

Tabel 3.2 merangkum inventaris bahan wawancara yang telah dihimpun beserta status verifikasi bukti pendukungnya. Catatan ini menjadi pedoman dalam membedakan antara kebutuhan yang telah tervalidasi secara faktual dan aspek prosedural yang masih memerlukan penegasan operasional. Verifikasi berkas fisik dan notulensi wawancara dilakukan secara berkala guna menjamin keaslian data yang digunakan sebagai dasar perancangan.

**Tabel 3.2 Sumber Kebutuhan dan Status Bukti**

| Kode | Sumber dan cakupan | Informasi yang digunakan | Tanggal dan status |
| :--- | :--- | :--- | :--- |
| S-01 | Wawancara pertama pengelola | Pendaftaran, paket, dan kebutuhan administrasi | Transkrip tervalidasi (Juli 2026); rekaman dan penanda waktu diarsipkan |
| S-02 | Wawancara kedua, Om Anang | Sistem lama, kebutuhan integrasi, dan akses cabang | Transkrip tervalidasi (Juli 2026); rekaman dan penanda waktu diarsipkan |
| S-03 | Wawancara ketiga, Mama Radit | Tarif, potongan, penerimaan, dan pencocokan bank | Transkrip tervalidasi (Juli 2026); rekaman dan penanda waktu diarsipkan |
| S-04 | Wawancara frontdesk, konteks Cabang 5 | Pelaksanaan pendaftaran, jatuh tempo, ruang, dan pelaporan harian | Transkrip tervalidasi (Oktober 2026); observasi alur Cabang 5 diarsipkan |
| S-05 | Bimbingan Bu Ayu dan Pak Arif | Batas lingkup, keluwesan aturan, metode, dan evaluasi | Notulensi bimbingan dosen pembimbing; arahan diintegrasikan ke rancangan |
| S-06 | Penjelasan pengguna selama penyusunan | WhatsApp manual dan penolakan kelas penuh | Keputusan perancangan dikonfirmasi bersama staf pengguna operasional |
| S-07 | Pengelola keuangan dan admin yang ditunjuk | Pemeriksa rekening, tarif berlaku, setoran, serta parameter kapasitas | Protokol konfirmasi parameter keuangan dan penugasan verifikasi disepakati |

Seluruh berkas transkrip mentah dan rekaman wawancara diarsipkan dalam lampiran penelitian dengan penanda waktu (*timestamp*) yang presisi agar setiap kutipan kebutuhan dapat diverifikasi dengan mudah. Data kuantitatif seperti variasi tarif bimbingan tetap dipetakan sesuai konteks cabang asalnya. Pihak manajemen kemudian meninjau batasan aturan tersebut sebelum diimplementasikan ke dalam modul logika bisnis sistem secara global.

Wawancara lanjutan dirancang menggunakan pendekatan semiterstruktur, di mana pengembang menyiapkan pedoman pertanyaan inti dan mengembangkan eksplorasi lanjutan sesuai dinamika jawaban informan. Pendekatan fleksibel ini terbukti efektif dalam mengurai disparitas persepsi antarstaf dan mengungkap detail proses bisnis yang belum terakomodasi pada sistem manual sebelumnya. Matriks topik wawancara dan instrumen telaah dokumen dirangkum pada Tabel 3.3.

**Tabel 3.3 Rancangan Topik Wawancara dan Pemeriksaan Dokumen**

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

Informasi verbal yang diperoleh dari narasumber dikonfirmasikan dengan bukti dokumen fisik yang diizinkan oleh mitra, meliputi kuitansi manual, buku induk siswa, jadwal pelajaran, rekapitulasi kas harian, dan mutasi transfer bank. Pemeriksaan artefak fisik ini membantu memetakan jalur perpindahan data aktual dari tingkat cabang hingga pelaporan manajemen pusat. Pengamatan langsung terhadap alur kerja kasir dan staf administrasi juga dicatat secara sistematis untuk melengkapi konteks wawancara.

Data empiris yang telah terkumpul kemudian dianalisis melalui reduksi data, kategorisasi tematik, dan triangulasi sumber guna mengeliminasi inkonsistensi informasi. Kebutuhan fungsional yang telah disintesis kemudian diformulasikan ke dalam spesifikasi cerita pengguna (*user story*) yang berorientasi pada nilai bisnis. Format penyusunan spesifikasi kebutuhan berbasis cerita pengguna ini mengacu pada standar rekayasa perangkat lunak terapan (Fikri & Arthawan, 2020; Sidiq dkk., 2025).

Setiap butir kebutuhan yang telah disintesis diberi kode identifikasi unik serta dipetakan hubungannya dengan sumber data primer, cakupan cabang, dan kriteria validasi. Matriks penelusuran ini secara tegas membedakan antara kebutuhan yang lahir dari kendala operasional riil dan fitur preventif yang diusulkan sebagai mitigasi risiko data. Pembedaan yang jelas ini memudahkan manajemen mitra dalam mengevaluasi urgensi dan justifikasi dari setiap fungsionalitas yang dikembangkan.

Draf spesifikasi kebutuhan kemudian ditinjau bersama perwakilan mitra dalam sesi peninjauan formal guna mencapai kesepakatan spesifikasi akhir (*requirements sign-off*). Masukan dan revisi dari mitra langsung diakomodasi untuk menyempurnakan daftar kebutuhan sebelum dialokasikan ke dalam siklus iterasi PxP. Setiap perubahan ruang lingkup dicatat dalam log riwayat versi sehingga alasan penyesuaian fungsionalitas dapat ditelusuri secara transparan.

### 3.3.2 Perencanaan (*Planning*)

Spesifikasi kebutuhan yang telah diformulasikan selanjutnya didekomposisi menjadi paket tugas teknis yang meliputi analisis sistem, perancangan arsitektur, pengodean program, pengujian modul, serta refaktorisasi kode. Pengembang mengestimasi durasi kerja setiap tugas secara terperinci dan memperbarui estimasi tersebut secara adaptif berlandaskan metrik durasi historis dari pengerjaan fitur serupa. Pendekatan estimasi berulang ini selaras dengan disiplin pengelolaan waktu mandiri dalam kerangka kerja PxP (Dzhurov dkk., 2009).

Pengembangan prototipe ARTHA dipetakan ke dalam empat siklus iterasi yang terstruktur dengan mempertimbangkan ketergantungan data dan relasi antarmodul. Modul fondasi yang mencakup manajemen akun pengguna, penetapan cabang, pendataan siswa, konfigurasi ruang kelas, serta struktur tarif diselesaikan pada iterasi awal sebagai prasyarat bagi modul penjadwalan, transaksi pembayaran, dan konsolidasi laporan. Distribusi alokasi modul beserta ketergantungan fungsionalnya disajikan secara sistematis pada Tabel 3.4.

**Tabel 3.4 Rencana Iterasi dan Ketergantungan Kebutuhan**

| Iterasi | Kebutuhan dan cerita pengguna | Lingkup pekerjaan | Prasyarat dan keluaran |
| :--- | :--- | :--- | :--- |
| I-01 | KF-01, KF-02, KF-03, KF-06, KF-14; US dengan nomor yang sama | Akun, cabang, siswa, ruang, kelas, serta dasar tarif dan tagihan | Data dasar dan pembatasan akses dapat diperiksa |
| I-02 | KF-04, KF-05; US-04 dan US-05 | Keanggotaan, kapasitas, jadwal, serta pemeriksaan irisan | Master I-01 tersedia; kelas penuh dan konflik diuji |
| I-03 | KF-07, KF-08, KF-09, KF-10; US dengan nomor yang sama | Tunai, pengajuan transfer, pemeriksaan, serta tautan WhatsApp | Tagihan tersedia; layanan pencocokan transfer dasar dibuat agar verifikasi dapat diuji |
| I-04 | KF-11, KF-12, KF-13; US dengan nomor yang sama | Setoran, rekap pusat, pencocokan, serta integrasi | Penerimaan I-03 tersedia; transaksi sumber dapat ditelusuri |

Pada pelaksanaan Iterasi III (I-03), verifikasi pembayaran transfer mewajibkan ketersediaan data rekening resmi dan nomor referensi mutasi bank agar keputusan persetujuan dapat dieksekusi secara valid. Oleh karena itu, komponen dasar pencocokan transaksi dibangun bersamaan dengan modul verifikasi transfer pada iterasi tersebut. Pengembangan kemudian dilanjutkan pada Iterasi IV (I-04) guna mencakup penyerahan setoran tunai dan rekapitulasi kas terpadu yang mengonsolidasikan seluruh arus penerimaan operasional.

Setiap siklus iterasi dijadwalkan berlangsung selama dua minggu, mengacu pada rentang ideal siklus PxP yakni satu hingga tiga minggu per iterasi (Dzhurov dkk., 2009). Alokasi waktu dua mingguan ini kemudian dijabarkan ke dalam estimasi jam kerja spesifik untuk setiap tugas teknis sebelum iterasi dimulai. Garis waktu dua belas minggu yang tercantum pada Subbab 3.6 diposisikan sebagai target perencanaan dasar yang bersifat dinamis terhadap perkembangan di lapangan.

Permintaan perubahan atau penambahan fitur baru dari pihak mitra dievaluasi dampaknya terhadap ketergantungan modul yang sedang berjalan dan beban pengujian terkait. Keputusan manajerial terkait perubahan ruang lingkup dicatat secara formal beserta sumber usulan dan estimasi penyesuaian jadwalnya. Formulir kendali perubahan dan rincian pembagian jam kerja diarsipkan dalam lampiran untuk menjaga akuntabilitas pelaksanaan proyek.

### 3.3.3 Inisialisasi Iterasi (*Iteration Initialization*)

Fase inisialisasi iterasi menandai dimulainya setiap siklus pengembangan baru melalui pemilihan sejumlah cerita pengguna dari *product backlog* sesuai urutan prioritas yang disepakati. Setiap unit tugas dilengkapi dengan kode kebutuhan, deskripsi teknis, penanggung jawab, alokasi jam estimasi, data uji spesifik, serta kriteria penyelesaian (*definition of done*). Kelengkapan parameter ini memberikan batasan yang tegas mengenai target fungsional yang harus diwujudkan dan mekanisme pengujian yang wajib dipenuhi.

Kumpulan data uji (*test data*) disiapkan sebelum proses penulisan kode dimulai guna merefleksikan variasi kondisi nyata operasional di delapan cabang bimbingan belajar. Selain mencakup skenario masukan normal, data uji secara khusus memuat kasus batas (*boundary cases*) dan masukan anomali untuk memvalidasi ketahanan validasi sistem. Data identitas siswa dan riwayat bukti pembayaran disamarkan (*anonymized*) atau menggunakan data sintetis sesuai protokol kerahasiaan informasi mitra.

Perkembangan implementasi kode program dikelola menggunakan sistem pengendali versi Git dengan konvensi penamaan cabang (*branching*) dan penanda rilis (*tagging*) yang konsisten. Alokasi waktu kerja dicatat secara harian per unit tugas, mencakup aktivitas pemodelan, penulisan kode, perbaikan galat, hingga refaktorisasi. Log waktu aktual ini menjadi data komparatif terhadap estimasi awal saat dilakukan evaluasi retrospektif pada penutupan iterasi.

Penyelesaian suatu tugas diukur secara ketat berdasarkan pemenuhan seluruh kriteria penerimaan fungsional dan ketiadaan cacat kode berstatus kritis. Suatu modul dinyatakan tuntas secara teknis hanya jika seluruh pengujian otomatis berhasil dilewati tanpa menimbulkan regresi pada modul sebelumnya. Hasil verifikasi teknis ini selanjutnya diajukan ke sesi peninjauan bersama mitra, di mana keputusan penerimaan operasional dicatat secara independen.

### 3.3.4 Perancangan (*Design*)

Tahap perancangan mentransformasikan spesifikasi kebutuhan iterasi berjalan ke dalam representasi arsitektur perangkat lunak yang terstruktur dan mudah diimplementasikan. Pengembang menyusun spesifikasi matriks hak akses, pemodelan alur aktivitas pengguna, rancangan konseptual basis data, serta tata letak antarmuka sistem. Artefak rancangan ini berfungsi sebagai cetak biru implementasi kode sekaligus acuan utama dalam penyusunan kasus pengujian sistem.

Pendekatan perancangan dalam penelitian ini mengadopsi prinsip desain sederhana (*simple design*) dari kerangka kerja PxP, di mana struktur sistem dibangun secara tepat guna untuk mengakomodasi kebutuhan iterasi aktif tanpa menambahkan kompleksitas yang berlebihan (Dzhurov dkk., 2009). Model perancangan sistem informasi yang memadukan diagram relasional data dan prototipe antarmuka terbukti efektif dalam memandu pengembang mandiri (Fikri & Arthawan, 2020). Pada ARTHA, model perancangan difokuskan untuk memperjelas batas kewenangan pengguna dan integritas aliran data transaksi multicabang.

Pada domain transaksi keuangan, perancangan memisahkan secara tegas tiga fase pencatatan, yaitu penerimaan pembayaran dari siswa, verifikasi mutasi transfer bank, dan rekonsiliasi setoran kas cabang ke kas pusat. Ketiga peristiwa akuntansi tersebut memiliki aktor penanggung jawab, dokumen bukti, dan waktu pencatatan yang berbeda. Pemisahan logis ini mencegah terjadinya pencatatan ganda (*double counting*), sehingga perpindahan fisik uang kas tidak diakui secara keliru sebagai pendapatan baru lembaga.

Tata kelola kelas dirancang dengan membedakan entitas fisik ruangan bimbingan, kelompok rombongan belajar, dan data keanggotaan siswa aktif. Kuota ketersediaan kelas dihitung secara *real-time* berbasis jumlah siswa berstatus aktif pada rombongan belajar terkait. Apabila seorang siswa memutuskan keluar atau lulus, status keanggotaannya diakhiri dengan tetap melestarikan riwayat pembelajarannya sebagai rekam jejak historis yang tidak boleh terhapus dari basis data.

Setiap dokumen perancangan ditinjau kembali terhadap skenario pengujian yang telah dipersiapkan guna mendeteksi potensi kelemahan logika sebelum kode program ditulis. Peninjauan preventif ini membantu mengidentifikasi ambiguitas aturan bisnis sejak dini, sehingga struktur tabel basis data dan logika *routing* API dapat dirancang secara kokoh. Pertanyaan seputar pengecualian proses bisnis diselesaikan melalui klarifikasi singkat bersama mitra, lalu keputusannya dituangkan ke dalam pembaruan diagram perancangan.

### 3.3.5 Implementasi (*Implementation*)

Fase implementasi mewujudkan seluruh artefak perancangan menjadi kode program yang fungsional melalui penerapan praktik pengujian unit, penulisan kode sumber, dan refaktorisasi berkesinambungan. Pengujian disusun sebelum kode fungsional dilengkapi, kemudian struktur kode disempurnakan setelah seluruh pengujian berhasil dilewati. Rangkaian proses ini mengimplementasikan kaidah teknis dari siklus kerja PxP (Dzhurov dkk., 2009).

Pendekatan *Test-Driven Development* (TDD) difokuskan secara spesifik pada modul logika bisnis inti yang memiliki kompleksitas tinggi dan berdampak langsung pada integritas operasional. Pada sistem ARTHA, aturan bisnis krusial tersebut mencakup kalkulasi akumulasi sisa tagihan, pembatalan otomatis penambahan siswa ke kelas yang telah penuh, serta validasi irisan jadwal mengajar tentor lintas cabang. Fokus pengujian unit pada aturan kritis ini menjamin keandalan kalkulasi sistem tanpa membebani jadwal pengembangan dengan penulisan uji coba yang berlebihan.

Dalam siklus TDD, pengembang terlebih dahulu menuliskan skrip uji coba unit yang mendefinisikan ekspektasi perilaku dan nilai keluaran yang diharapkan. Kode logika bisnis selanjutnya ditulis secara bertahap hingga seluruh unit uji menghasilkan status lolos (*pass*). Riwayat pengujian sebelum dan sesudah kode diselesaikan diarsipkan bersama kode sumber sebagai artefak pembuktian kepatuhan terhadap metodologi TDD.

Setelah fungsionalitas logika bisnis terbukti bekerja dengan benar, pengembang melakukan refaktorisasi kode guna meningkatkan keterbacaan, efisiensi eksekusi, serta mengurangi duplikasi logika (*code smell*). Proses refaktorisasi wajib mempertahankan perilaku eksternal kode, di mana skrip pengujian unit dijalankan kembali untuk memastikan tidak ada fungsionalitas yang terdegradasi. Tahap ini krusial dalam menjaga arsitektur perangkat lunak tetap bersih dan mudah dikembangkan oleh pengembang mandiri.

Lapisan antarmuka pengguna berbasis Next.js dihubungkan secara bertahap dengan layanan API Laravel melalui pertukaran data terstruktur berformat JSON. Setiap permintaan data dari sisi klien melewati lapisan *middleware* autentikasi dan otorisasi pada peladen guna memverifikasi peran pengguna serta cabang penugasannya. Mekanisme keamanan ini memastikan pembatasan akses data tetap kokoh meskipun pengguna mencoba memanipulasi parameter URL atau identitas objek pada permintaan HTTP.

### 3.3.6 Pengujian Sistem (*System Testing*)

Pengujian sistem dilaksanakan untuk memvalidasi bahwa seluruh modul perangkat lunak berfungsi secara harmonis dan menghasilkan luaran yang akurat sesuai spesifikasi kebutuhan pengguna. Pengujian ini menerapkan pendekatan pengujian kotak hitam (*Black Box Testing*) dengan teknik *Equivalence Partitioning* dan *Boundary Value Analysis*. Penerapan pengujian fungsional kotak hitam dalam kerangka PxP telah terbukti efektif dalam memverifikasi keandalan sistem informasi (Apriyanti dkk., 2024). Skenario uji ARTHA dirancang berdasarkan alur kerja pengguna, dengan penekanan khusus pada penegakan batas hak akses cabang, kontrol kapasitas kelas, dan konsistensi pencatatan transaksi keuangan.

Pengujian dijalankan pada lingkungan uji terisolasi dengan menggunakan basis data simulasi yang memuat karakteristik data delapan cabang bimbingan belajar. Sebelum pengujian dieksekusi, pengembang mencatat konfigurasi lingkungan uji yang mencakup nomor versi rilis aplikasi, spesifikasi perangkat keras pengujian, zona waktu komputasi, dan status awal data. Dokumentasi parameter awal ini diperlukan agar setiap skenario pengujian dapat direplikasi secara konsisten ketika proses pengujian ulang pascaperbaikan dilakukan.

Tabel 3.5 menyajikan representasi kasus pengujian sistem yang berfokus pada mitigasi risiko kritis integritas data dan konkurensi transaksi. Daftar lengkap yang mencakup kasus uji BB-01 hingga BB-33 didokumentasikan secara rinci pada lampiran pengujian sistem. Keterkaitan antara kasus uji kotak hitam dengan spesifikasi kebutuhan dipetakan melalui kelompok pengujian PU-01 hingga PU-14 pada Tabel 3.13.

**Tabel 3.5 Contoh Kasus Pengujian Sistem**

| Kode | Kondisi yang diperiksa | Keluaran yang diharapkan | Pelaksanaan |
| :--- | :--- | :--- | :--- |
| BB-01 | Akun cabang meminta objek cabang lain | Akses ditolak dan objek tidak dikirim | Belum diuji |
| BB-07 | Dua permintaan mengisi satu tempat terakhir | Hanya satu keanggotaan aktif baru tersimpan | Belum diuji |
| BB-14 | Pengajuan dikembalikan kemudian diajukan ulang | Pengajuan lama tetap tersimpan dan pengajuan baru tertaut | Belum diuji |
| BB-16 | Persetujuan transfer dikirim berulang | Penerimaan, alokasi, serta pencocokan hanya berlaku sekali | Belum diuji |
| BB-17 | Admin membuka pesan tunggakan | Nomor dan isi sesuai; pembukaan tidak dianggap bukti terkirim | Belum diuji |
| BB-20 | Setoran kas dicocokkan dengan dana bank | Status setoran berubah tanpa menambah penerimaan siswa | Belum diuji |

Setiap eksekusi kasus pengujian dicatat secara rinci meliputi prasyarat pengujian, langkah operasional, data masukan, hasil yang diharapkan, hasil aktual, status kelulusan, serta tangkapan layar bukti eksekusi. Anomali yang teridentifikasi diklasifikasikan berdasarkan tingkat keparahannya terhadap keandalan operasional sistem. Pelanggaran isolasi data cabang, anomali duplikasi pencatatan kas, dan kegagalan penegakan kuota kelas dikategorikan sebagai galat kritis yang wajib diselesaikan sebelum pengujian dilanjutkan.

Modul yang belum memenuhi kriteria kelulusan segera diperbaiki melalui tahapan *debugging*, kemudian diuji kembali menggunakan skenario pengujian yang sama beserta uji regresi pada fungsi-fungsi yang terhubung. Hasil pengujian ulang dicatat secara komparatif dengan merekam nomor versi perbaikan dan tanggal verifikasi. Dokumentasi historis ini mencerminkan lintasan peningkatan kualitas perangkat lunak dari kondisi temuan awal hingga tercapainya status valid.

### 3.3.7 Evaluasi Iterasi (*Retrospective*)

Sesi evaluasi retrospektif diselenggarakan pada akhir setiap siklus iterasi guna meninjau efektivitas kinerja pengembang, menganalisis kendala teknis yang timbul, serta mengevaluasi kualitas modul yang telah diselesaikan. Pengembang membandingkan durasi kerja aktual terhadap estimasi perencanaan, menelaah log galat yang ditemukan, serta mengevaluasi status penyelesaian *backlog*. Kesimpulan yang ditarik dari sesi evaluasi ini menjadi landasan empiris untuk menyempurnakan strategi implementasi pada siklus iterasi berikutnya.

Pencatatan metrik kerja secara disiplin memberikan bukti kuantitatif untuk meningkatkan akurasi estimasi waktu dan kedewasaan proses rekayasa perangkat lunak mandiri (Dzhurov dkk., 2009). Dinamika perubahan kebutuhan dan disparitas waktu pengerjaan modul juga menjadi perhatian utama dalam evaluasi proyek berbasis PxP (Sidiq dkk., 2025). Oleh sebab itu, pencatatan durasi kerja mencakup seluruh fase mulai dari pemodelan, penulisan kode, hingga pengujian guna mengidentifikasi sumber inefisiensi secara komprehensif.

Dimensi dokumentasi yang menjadi instrumen utama dalam evaluasi retrospektif dirangkum pada Tabel 3.6. Seluruh catatan waktu, log galat, perubahan spesifikasi, serta usulan perbaikan diisi secara konsisten sepanjang aktivitas pengembangan berlangsung. Ketersediaan log aktivitas yang faktual ini memastikan proses refleksi retrospektif berlandaskan pada data empiris yang dapat diverifikasi keabsahannya.

**Tabel 3.6 Unsur Dokumentasi Evaluasi Iterasi**

| Dokumen | Unsur yang dicatat | Penggunaan analisis |
| :--- | :--- | :--- |
| Catatan waktu | Kode tugas, kategori, estimasi, waktu mulai, waktu selesai, dan durasi aktual | Selisih estimasi dan aktual beserta penyebabnya |
| Catatan galat | Kode galat, versi, pemicu, tingkat kepentingan, perbaikan, dan uji ulang | Galat terbuka, galat terselesaikan, dan pola kesalahan |
| Catatan perubahan | Asal permintaan, kebutuhan terdampak, keputusan, dan perubahan jadwal | Perubahan ruang lingkup dan tindak lanjut |
| Usulan perbaikan proses | Masalah, bukti, tindakan, dan hasil pemeriksaan berikutnya | Penyesuaian cara kerja pada iterasi selanjutnya |

Analisis varians waktu dihitung secara sistematis pada setiap tugas dengan mengurangkan durasi estimasi dari durasi pengerjaan aktual. Deviasi yang signifikan selanjutnya dianalisis akar penyebabnya melalui penelusuran catatan kendala teknis harian. Pembahasan mendalam ini memungkinkan pemisahan yang jelas antara keterlambatan yang dipicu oleh perubahan kebutuhan pengguna dan waktu ekstra yang dihabiskan untuk menyelesaikan galat logika program.

Rekomendasi perbaikan yang dirumuskan pada sesi retrospektif segera diterapkan untuk memperketat estimasi waktu, menata ulang prioritas tugas tersisa, serta menyempurnakan strategi pengujian pada iterasi berikutnya. Berkas lengkap catatan waktu pengerjaan, log anomali kode, riwayat perubahan kebutuhan, serta notulensi retrospektif diarsipkan secara teratur pada lampiran laporan tugas akhir. Ringkasan hasil evaluasi disajikan pada bab pembahasan guna memperlihatkan kurva pembelajaran dan evolusi kualitas perangkat lunak.

### 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi

Pengujian penerimaan pengguna atau *User Acceptance Testing* (UAT) dilaksanakan untuk mengevaluasi kesesuaian alur kerja prototipe ARTHA terhadap kebutuhan operasional nyata dari sudut pandang pemangku kepentingan langsung. Partisipan evaluasi dipilih menggunakan teknik penarikan sampel bertujuan (*purposive sampling*) dengan mempertimbangkan wewenang manajerial, pengalaman administratif harian, kesediaan waktu, serta keterkaitan peran terhadap fitur yang diuji. Kriteria seleksi ini memastikan bahwa pengujian operasional dijalankan oleh personel yang benar-benar memahami konteks bisnis bimbingan belajar.

Kelompok peserta UAT dirancang mewakili dua peran utama dalam sistem, yaitu Admin Cabang dan Super Admin, dengan penetapan nama personel, representasi cabang, serta jadwal evaluasi yang dikoordinasikan secara resmi bersama manajemen mitra. Setiap peserta menguji serangkaian skenario tugas kerja sesuai hak akses yang dimilikinya. Hasil evaluasi disajikan secara terpilah berdasarkan peran dan cabang yang diwakili guna memberikan gambaran komprehensif mengenai tingkat penerimaan sistem di setiap tingkatan organisasi.

Sebelum sesi pengujian dimulai, pengembang menyiapkan peladen uji mandiri, repositori basis data uji yang telah dinormalisasi, akun pengguna terverifikasi untuk setiap peran, bundel data simulasi transaksi, serta dokumen panduan operasional ringkas. Seluruh fungsionalitas inti dan mekanisme isolasi hak akses diverifikasi kestabilannya terlebih dahulu guna memastikan pengujian berjalan lancar. Lingkungan uji yang telah terstandardisasi ini juga memungkinkan pengulangan skenario tugas pada kondisi awal yang sama apabila terjadi kendala teknis.

Pelaksanaan UAT diawali dengan sesi pembekalan singkat mengenai tujuan pengujian, etika kerahasiaan data, tata cara pengisian instrumen evaluasi, serta persetujuan dokumentasi hasil uji. Peserta selanjutnya menjalankan skenario tugas yang telah disiapkan secara mandiri, sementara pengembang mengamati interaksi pengguna dan mencatat kendala maupun bantuan teknis yang diperlukan. Setiap penyesuaian instruksi yang dilakukan selama pelaksanaan uji dicatat secara kronologis beserta justifikasi rasionalnya.

Tabel 3.7 merangkum empat belas skenario tugas UAT yang merefleksikan proses bisnis operasional bimbingan belajar, di mana kode A merepresentasikan peran Admin Cabang dan kode S merepresentasikan Super Admin. Lembar kerja evaluasi mencakup identitas peserta, nomor versi aplikasi, instruksi langkah kerja, hasil aktual, tingkat intervensi pengembang, status keputusan penerimaan, catatan kualitatif, serta bukti tangkapan layar. Catatan terstruktur ini menjadi bahan telaah kuantitatif dan kualitatif dalam mengukur akseptabilitas sistem.

**Tabel 3.7 Rancangan Tugas Penerimaan Berdasarkan Kebutuhan**

| Kode | Peran | Tugas | Dasar penerimaan |
| :--- | :--- | :--- | :--- |
| UAT-01 | A dan S | Masuk, memeriksa cakupan akses, dan keluar | Akun sesuai peran dan data cabang lain terlindungi |
| UAT-02 | A | Mendaftarkan dan memperbarui siswa | Data wajib benar dan riwayat tetap tersedia |
| UAT-03 | A dan S | Menyiapkan kelas serta ruang | Batas kelas sesuai ruang dan parameter terlihat |
| UAT-04 | A | Menambah peserta, memeriksa penuh, lalu mengakhiri keanggotaan | Penambahan ditolak saat penuh dan tempat kembali tersedia setelah keluar |
| UAT-05 | A | Menyusun serta menyunting jadwal | Irisan relevan ditampilkan tanpa benturan dengan jadwal sendiri |
| UAT-06 | A dan S | Memilih tarif dan menerbitkan tagihan periode | Tarif tepat dan tagihan tidak terbit ganda |
| UAT-07 | A | Mencatat uang tunai dan mencetak kuitansi | Penerimaan sah tercatat satu kali |
| UAT-08 | A | Mengajukan transfer untuk beberapa tagihan siswa yang sama | Alokasi benar dan pengajuan belum melunasi tagihan |
| UAT-09 | S | Memeriksa transfer, mengembalikan, atau menyetujui | Keputusan dan referensi dana masuk dapat ditelusuri |
| UAT-10 | A | Membuka pesan WhatsApp dari tunggakan | Nomor, periode, nominal, dan jatuh tempo sesuai |
| UAT-11 | A dan S | Menyerahkan serta menerima setoran tunai | Daftar pembayaran sumber dan petugas tercatat |
| UAT-12 | A dan S | Menelusuri ringkasan ke transaksi sumber | Total, periode, cabang, dan status sesuai |
| UAT-13 | S | Mencocokkan penerimaan dengan contoh mutasi | Referensi tidak dipakai ganda dan setoran tidak menjadi pendapatan baru |
| UAT-14 | S | Mengelola akun dan data induk | Perubahan hanya dilakukan petugas berwenang |

Sebelum diujikan kepada pengguna, instrumen evaluasi UAT divalidasi terlebih dahulu bersama dosen pembimbing dan perwakilan manajemen mitra guna menjamin kejelasan instruksi serta keselarasan skenario tugas terhadap tujuan penelitian. Partisipasi aktif calon pengguna dalam evaluasi perangkat lunak berbasis PxP merupakan pilar utama dalam memastikan relevansi sistem terhadap kebutuhan operasional nyata (Apriyanti dkk., 2024). Pada prototipe ARTHA, validasi ini diwujudkan melalui pengujian skenario penanganan transaksi nyata yang dapat diobservasi hasilnya secara objektif.

Status pencapaian pada setiap butir skenario tugas diklasifikasikan ke dalam tiga kategori keputusan, yaitu diterima (*accepted*), memerlukan perbaikan (*rework*), atau belum dapat dievaluasi (*blocked*), disertai catatan alasan yang komprehensif. Kendala yang timbul akibat ketidaksiapan data simulasi dipisahkan secara tegas dari kesalahan logika fungsional aplikasi. Setelah perbaikan kode program selesai dilaksanakan, skenario tugas yang bermasalah diuji kembali pada versi rilis perbaikan untuk memverifikasi efektivitas solusi yang diterapkan.

Hasil pelaksanaan pengujian sistem dirangkum secara kuantitatif dengan menyajikan metrik total kasus uji yang direncanakan, kasus yang dieksekusi, jumlah kelulusan, kegagalan uji, serta kasus yang belum dijalankan. Persentase tingkat kelulusan dihitung berdasarkan perbandingan antara jumlah kasus uji yang berstatus lulus terhadap total kasus uji yang telah dieksekusi. Sementara itu, metrik cakupan pengujian dihitung dari rasio kasus uji yang dieksekusi terhadap seluruh populasi kasus uji yang direncanakan, sehingga kedua indikator tersebut memberikan interpretasi mutu yang saling melengkapi.

Analisis hasil evaluasi UAT dikompilasi secara terstruktur berdasarkan capaian pelaksanaan tugas per peserta dan nomor iterasi rilis aplikasi. Tingkat penerimaan pengguna (*acceptance rate*) dihitung menggunakan formula persentase, yakni membagi jumlah skenario tugas yang diterima dengan total skenario tugas yang telah dievaluasi. Tugas yang memerlukan pengujian ulang dilaporkan secara terpisah guna memperlihatkan efektivitas siklus perbaikan sistem hingga disetujui oleh mitra.

Keputusan akhir terkait akseptabilitas prototipe diambil secara komprehensif dengan mempertimbangkan pemenuhan seluruh tugas operasional prioritas tinggi serta tuntasnya penyelesaian seluruh galat kritis. Pembahasan hasil evaluasi difokuskan pada tingkat keterpaduan modul, kemudahan pemantauan transaksi kas, serta kepuasan pengguna terhadap pemenuhan kebutuhan administrasi. Seluruh interpretasi didasarkan secara ketat pada data evaluasi empiris yang terhimpun, sedangkan justifikasi terkait efisiensi waktu kerja dianalisis sebagai implikasi kualitatif dari otomatisasi proses bisnis.

Setelah seluruh masukan evaluasi berhasil diakomodasi, pengembang menyusun paket rilis serah uji yang meliputi kode sumber terverifikasi, panduan instalasi dan penggunaan (*user manual*), daftar batasan sistem, prosedur pencadangan dan pemulihan basis data, serta berita acara pengujian UAT. Dokumen serah terima ini merekam status kesiapan teknologi prototipe pada akhir masa penelitian. Kebijakan mengenai implementasi operasional skala penuh selanjutnya diserahkan kepada kesiapan manajerial mitra bimbingan belajar sesuai hasil validasi yang dicapai.

## 3.4 Konsep Prototipe

Konsep prototipe menguraikan translasi proses bisnis operasional Bimbingan Belajar Artha ke dalam arsitektur fungsional, taksonomi peran pengguna, serta model keterhubungan data digital. Kerangka konseptual ini menjembatani temuan elisitasi empiris dengan keputusan desain antarmuka dan logika pemrosesan yang akan dibangun. Seluruh perumusan proses bisnis dan pemetaan entitas diselaraskan dengan tata kelola manajemen mitra guna menjamin efektivitas penerapan sistem pada lingkungan operasional nyata.

### 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan

Arsitektur usulan sistem ARTHA dirancang untuk mengintegrasikan proses pencatatan di tingkat cabang dengan kebutuhan pengawasan manajerial terpusat secara terpadu. Data operasional yang diinput oleh Admin Cabang secara otomatis mengalir ke basis data terpusat guna mendukung verifikasi transaksi keuangan dan pembentukan laporan manajerial secara *real-time*. Urgensi pembaruan tata kelola kas dan verifikasi berjenjang ini sejalan dengan kajian empiris sistem administrasi SPP yang menekankan pentingnya ketertelusuran dokumen bukti transaksi (Hendri dkk., 2025).

Tabel 3.8 membandingkan alur proses bisnis yang sedang berjalan (*as-is*) dengan rancangan proses usulan (*to-be*) dalam sistem ARTHA. Komparasi ini memperlihatkan transformasi operasional dari pencatatan manual yang terfragmentasi menuju pengelolaan data digital yang terkonsolidasi. Penegasan mengenai otoritas mutasi rekening resmi dan personel pemeriksa bank difinalisasi bersama pihak manajemen sebelum sistem diimplementasikan.

**Tabel 3.8 Proses Berjalan dan Proses Usulan**

| Proses | Dasar yang ditelusuri | Rancangan usulan |
| :--- | :--- | :--- |
| Pendaftaran | Catatan siswa dan pilihan layanan pada cabang | Identitas siswa terpusat dengan pembatasan akses cabang |
| Kelas | Pemeriksaan peserta dan ruang oleh petugas | Hitungan peserta aktif, peringatan hampir penuh, dan penolakan saat penuh |
| Jadwal | Catatan serta komunikasi pengelola | Pemeriksaan irisan tentor dan ruang menurut hari, waktu, serta masa berlaku |
| Penagihan | Jatuh tempo dan pengingat oleh admin | Daftar tunggakan, pratinjau pesan, serta tombol WhatsApp manual |
| Transfer | Bukti disampaikan kepada pihak pengelola | Pengajuan Admin Cabang, pemeriksaan dana masuk, dan keputusan Super Admin |
| Tunai dan setoran | Penerimaan cabang dan penyerahan kepada pusat | Pembayaran siswa, penyerahan kas, serta setoran bank dicatat terpisah |
| Pelaporan | Penghimpunan catatan cabang | Rekap berdasarkan transaksi sah, periode, kanal, dan cabang historis |

Dalam mekanisme transaksi penerimaan pembayaran, staf administrasi memilih satu atau beberapa tagihan aktif milik siswa yang terdaftar pada cabang terkait. Sistem mencatat pembayaran tersebut sebagai satu entitas transaksi induk yang selanjutnya didekomposisi ke dalam rincian alokasi tagihan spesifik. Akumulasi nominal seluruh alokasi tagihan wajib bernilai ekuivalen dengan total uang yang disetorkan guna menjamin keseimbangan antara nilai pelunasan kewajiban dan fisik kas yang diterima.

Pada skema pembayaran transfer, Admin Cabang mengawali proses dengan menginput rincian transaksi serta mengunggah berkas digital bukti transfer ke dalam sistem. Sebelum disetujui oleh Super Admin, status transaksi berada dalam antrean peninjauan dan belum mengurangi sisa tagihan siswa. Super Admin memverifikasi kesesuaian data transfer terhadap mutasi rekening koran bank; transaksi yang valid akan disetujui sehingga memotong piutang siswa, sedangkan pengajuan yang tidak sesuai akan ditolak disertai alasan koreksi untuk kemudian diajukan ulang melalui transaksi baru yang tetap tertaut pada riwayat sebelumnya.

Pada transaksi pembayaran tunai di kasir, Admin Cabang memproses penerimaan kas secara langsung setelah fisik uang dihitung, sehingga status tagihan dapat terpotong secara instan. Rancangan dasar sistem menetapkan skema pelunasan penuh sesuai nilai kewajiban tagihan yang dipilih. Apabila pihak manajemen bimbingan belajar menyepakati adanya skema pembayaran cicilan, fungsionalitas alokasi parsial akan diakomodasi melalui penyesuaian parameter konfigurasi pembayaran.

Fisik uang kas yang dihimpun di tingkat cabang dibundel ke dalam dokumen penyerahan kas (*cash batch*) yang merekam daftar transaksi sumber, petugas penyerah, penerima di kantor pusat, serta waktu serah terima. Tahap berikutnya adalah penyetoran akumulasi uang kas tersebut ke rekening giro resmi bimbingan belajar di bank dengan mencatat rekening tujuan, tanggal setor, dan bukti slip setoran. Kedua tahapan administratif ini merepresentasikan perpindahan fisik kas internal, sehingga pencatatannya tidak diakui sebagai penambahan pendapatan siswa baru dalam pembukuan lembaga.

Mekanisme rekonsiliasi bank pada prototipe ARTHA menerapkan prinsip pencocokan satu-ke-satu (*one-to-one matching*), yakni menghubungkan satu baris mutasi kredit rekening koran dengan satu transaksi transfer siswa atau satu berkas setoran kas cabang yang bernilai nominal identik. Setelah petugas memverifikasi keabsahan data, kode referensi mutasi bank dikunci pada transaksi terkait agar tidak dapat digunakan ulang. Kasus mutasi gabungan (*bulk transfer*), biaya administrasi bank, maupun selisih transfer dicatat dalam log anomali untuk penanganan manajerial lebih lanjut karena berada di luar lingkup pencocokan otomatis prototipe.

Pemisahan tanggung jawab operasional antara kantor cabang dan kantor pusat ini mengadopsi prinsip tata kelola sistem informasi terdistribusi (Ramadhan dan Widodo, 2026), sedangkan mekanisme rekonsiliasi internal dengan rekening koran perbankan merujuk pada standar pengendalian kas (Sudirman dan Tristianti, 2021). Kedua rujukan akademik tersebut mendasari perancangan modul pelaporan dan audit kas ARTHA. Dalam penyajian informasi keuangan, sisa tagihan siswa dipisahkan secara tegas dari status rekonsiliasi bank guna mencegah distorsi pemahaman antara piutang belajar dan posisi likuiditas kas.

### 3.4.2 Kebutuhan Fungsional dan Nonfungsional

Kebutuhan fungsional merepresentasikan seluruh kemampuan operasional dan layanan komputasi yang wajib disediakan oleh sistem ARTHA untuk mendukung pekerjaan pengguna. Setiap butir kebutuhan diformulasikan secara presisi bersama indikator luaran yang diharapkan guna memudahkan verifikasi pada tahap pengujian perangkat lunak. Rincian empat belas kebutuhan fungsional sistem disajikan pada Tabel 3.9.

**Tabel 3.9 Rancangan Kebutuhan Fungsional**

| Kode | Fungsi | Hasil yang diharapkan |
| :--- | :--- | :--- |
| KF-01 | Autentikasi dan kewenangan | Akses berdasarkan peran serta cabang; sesi dapat diakhiri |
| KF-02 | Pengelolaan siswa | Identitas, kontak wali, jenjang termasuk TK, dan status tercatat |
| KF-03 | Pengelolaan kelas dan ruang | Kapasitas kelompok, kapasitas ruang, serta ambang hampir penuh tersedia |
| KF-04 | Keanggotaan dan kapasitas | Peserta aktif dihitung, kelas penuh ditolak, dan keluar membuka tempat |
| KF-05 | Pengelolaan jadwal | Irisan tentor dan ruang diperiksa menurut masa berlaku |
| KF-06 | Tarif dan tagihan | Variasi cabang, sesi, siklus, potongan berwenang, dan periode tersimpan |
| KF-07 | Penerimaan tunai | Penerimaan, alokasi tagihan, dan kuitansi dicatat satu kali |
| KF-08 | Pengajuan transfer | Bukti dan alokasi diajukan tanpa langsung melunasi tagihan |
| KF-09 | Pemeriksaan transfer | Persetujuan atau pengembalian beserta riwayat keputusan tersimpan |
| KF-10 | Tautan WhatsApp | Nomor dan pesan tunggakan disiapkan untuk dikirim oleh admin |
| KF-11 | Setoran tunai | Penyerahan ke pusat dibedakan dari penyetoran ke rekening |
| KF-12 | Dasbor dan laporan | Data cabang serta antrean pemeriksaan ditelusuri ke transaksi sumber |
| KF-13 | Pencocokan penerimaan | Transfer atau setoran dihubungkan ke referensi bank secara manual |
| KF-14 | Data induk dan akun | Tahun ajaran, cabang, akun, tentor, mapel, dan rekening diatur berwenang |

Pada modul penjadwalan pembelajaran, staf administrasi menyusun penugasan mengajar tentor dan alokasi ruangan dengan dukungan fitur deteksi irisan waktu secara otomatis. Jadwal yang terindikasi mengalami benturan waktu atau ruang akan ditandai dengan peringatan visual dan disimpan dalam status nonaktif hingga pengelola menyelesaikan konflik tersebut. Pengaturan deteksi bentrok jadwal pada lembaga bimbingan belajar ini merujuk pada prinsip optimasi jadwal (Khafidhoh dkk., 2026), di mana ARTHA berfokus pada validasi aturan benturan deterministik tanpa menerapkan algoritma genetika yang berlebihan bagi skala operasional mitra.

Penentuan ketersediaan kuota siswa dihitung melalui perbandingan dinamis antara jumlah peserta aktif pada rombongan belajar terhadap batas maksimum kapasitas ruangan fisik. Pendekatan kalkulasi kapasitas dan validasi irisan jadwal ini mengadaptasi model kontrol alokasi sumber daya institusi pendidikan (Kabisatullah dan Noprisson, 2026). Dalam konteks ARTHA, batasan kuota kelas dikonfigurasi secara spesifik berdasarkan kebijakan manajerial cabang masing-masing.

Pengelola sistem menetapkan parameter ambang batas hampir penuh (*near-full threshold*) untuk memberikan sinyal peringatan dini apabila sisa kuota ruang mulai menipis. Nilai ambang batas ini dikonfigurasi dalam rentang numerik yang fleksibel, sementara status penuh (*full*) secara otomatis aktif ketika jumlah siswa terdaftar telah menyamai kapasitas maksimum. Indikator keterisian kelas ini ditampilkan secara independen dari status operasional kelas, sehingga staf dapat dengan mudah membedakan antara kelas yang aktif penuh dan kelas yang sengaja ditutup.

Validasi kapasitas kelas dieksekusi kembali pada sisi peladen (*backend*) sesaat sebelum perintah penyimpanan data keanggotaan dijalankan. Pemeriksaan ganda ini krusial untuk mencegah anomali *race condition*, di mana dua staf administrasi cabang yang berbeda membuka formulir pendaftaran secara simultan saat kuota hanya tersisa satu kursi. Mekanisme transaksi terisolasi pada basis data menjamin hanya satu permintaan pendaftaran yang berhasil diproses, sedangkan permintaan lainnya akan ditolak secara anggun dengan pesan informatif.

Fitur penagihan tunggakan mengompilasi data nama siswa, rincian periode belajar, sisa nominal tagihan, dan batas waktu jatuh tempo menjadi draf pesan teks terstruktur. Nomor kontak wali murid distandardisasi ke dalam format internasional, kemudian seluruh draf pesan dienkode ke dalam format URL protokol WhatsApp resmi. Pembentukan tautan perpesanan ini mengacu pada dokumentasi teknis antarmuka *click to chat* resmi (WhatsApp, t.t.).

Ketika staf administrasi menekan tombol WhatsApp, sistem merekam log aktivitas interaksi tersebut guna mencatat riwayat upaya penagihan yang telah dilakukan lembaga. Staf kemudian diarahkan ke aplikasi WhatsApp Web atau WhatsApp Desktop untuk meninjau redaksi pesan sebelum dikirimkan secara manual kepada wali siswa. Karena pengiriman pesan berlangsung di luar domain aplikasi ARTHA, log sistem mencatat status pembuatan tautan dan tidak mengklaim status keterbacaan pesan di perangkat penerima.

Selain fungsi operasional inti, perancangan prototipe menetapkan kriteria kualitas teknis yang mencakup aspek keamanan akses data, keandalan konkurensi, integritas audit, serta pengalaman pengguna. Kebutuhan nonfungsional yang menjadi standar penerimaan teknis dirangkum pada Tabel 3.10. Seluruh indikator kinerja kuantitatif akan diukur secara empiris pada lingkungan pengujian yang representatif.

**Tabel 3.10 Rancangan Kebutuhan Nonfungsional**

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

Struktur hak akses pengguna dalam sistem ARTHA dirancang menggunakan model *Role-Based Access Control* (RBAC) yang memadukan wewenang jabatan dengan batasan cabang penugasan. Pemisahan domain data operasional antarcabang disertai akses pemantauan terpusat untuk pimpinan merupakan praktik terbaik dalam tata kelola sistem informasi terdistribusi (Ahadi dkk., 2025; Thiovanda, 2026). Dalam implementasinya, ARTHA menetapkan dua peran utama, yaitu Admin Cabang dan Super Admin.

Tabel 3.11 mendefinisikan pembagian kewenangan fungsional dan jangkauan akses data untuk masing-masing peran pengguna. Matriks otorisasi ini diterapkan secara ketat baik pada lapisan antarmuka pengguna maupun pada logika validasi API di sisi peladen. Pembagian tanggung jawab keuangan yang memerlukan keputusan kebijakan dibahas dan disepakati bersama manajemen sebelum modul diterapkan.

**Tabel 3.11 Matriks Hak Akses Pengguna**

| Fungsi | Admin Cabang | Super Admin |
| :--- | :--- | :--- |
| Siswa dan keanggotaan | Mengelola sesuai cabang penugasan | Memantau seluruh cabang dan melakukan koreksi berwenang |
| Kelas dan jadwal | Mengelola pada cabangnya sesuai aturan | Memantau lintas cabang dan menangani penyesuaian berwenang |
| Tarif dan parameter kelas | Menggunakan tarif; mengelola kelas sesuai penugasan | Menetapkan tarif, kapasitas, dan ambang sesuai kewenangan |
| Penerimaan tunai | Mencatat penerimaan dan menyiapkan setoran | Memeriksa rekap serta penerimaan setoran |
| Transfer siswa | Mengajukan bukti dan membuat pengajuan ulang yang tertaut | Memeriksa dana masuk serta menyetujui atau mengembalikan |
| Tautan WhatsApp | Mengakses tagihan serta nomor wali pada cabangnya | Memantau tindak lanjut tanpa perlu mengirim pesan berulang |
| Dasbor | Melihat data cabangnya | Melihat agregat dan rincian seluruh cabang |
| Akun pengguna | Menggunakan akun yang diberikan | Membuat, menonaktifkan, dan mengatur penugasan akun |

Pada setiap permintaan data, peladen secara konsisten memeriksa identitas peran yang terenkripsi dalam token sesi serta memvalidasi relasi pengguna terhadap data cabang yang diminta. Nilai cabang yang kosong (*null*) pada profil pengguna ditangani secara ketat dan tidak secara otomatis mewarisi hak akses Super Admin. Melalui mekanisme pertahanan berlapis ini, seluruh tindakan manipulasi data dibatasi secara mutlak pada cabang penugasan yang sah.

Pihak tentor dan orang tua atau wali siswa diposisikan sebagai entitas eksternal yang menjadi subjek operasional dan target komunikasi bimbingan belajar. Dalam batasan arsitektur prototipe ini, kedua pihak tersebut tidak diberikan akun interaktif untuk mengakses dasbor sistem. Staf administrasi bertindak sebagai operator yang mengelola data penugasan tentor serta menyalurkan informasi tagihan kepada wali siswa melalui kanal komunikasi resmi.

### 3.4.4 Cerita Pengguna (*User Story*) dan Kriteria Penerimaan

Spesifikasi kebutuhan operasional sistem dirumuskan ke dalam bentuk cerita pengguna (*user story*) guna menggambarkan interaksi fungsional dari perspektif persona pengguna akhir. Setiap butir cerita pengguna dilengkapi dengan kriteria penerimaan objektif yang menjadi tolak ukur kelulusan fitur pada saat pengujian. Struktur perumusan cerita pengguna ini mengadopsi standar rekayasa perangkat lunak tangkas (Fikri & Arthawan, 2020; Sidiq dkk., 2025), dengan substansi yang disesuaikan pada konteks kebutuhan ARTHA sebagaimana disajikan pada Tabel 3.12.

**Tabel 3.12 Cerita Pengguna dan Kriteria Penerimaan**

| Kode | Peran dan tindakan | Manfaat | Kriteria penerimaan |
| :--- | :--- | :--- | :--- |
| US-01 | Pengguna masuk dan keluar sesuai peran | Akses data sesuai tugas | Akses Admin Cabang ke cabang lain ditolak; Super Admin sesuai kewenangan; sesi keluar tidak dapat dipakai |
| US-02 | Admin mendaftarkan serta memperbarui siswa | Data siswa dapat ditelusuri | Data wajib lengkap; penonaktifan tidak menghapus transaksi |
| US-03 | Admin menyiapkan kelas; Super Admin menetapkan ruang dan kapasitas | Batas peserta terlihat sebelum penempatan | Kapasitas kelas sesuai ruang dan ambang sisa tempat tersimpan |
| US-04 | Admin mengelola masuk dan keluar kelas | Tempat tersedia serta riwayat benar | Penuh menolak penambahan; keluar membuka satu tempat |
| US-05 | Admin menyusun jadwal | Potensi irisan diketahui | Konflik tentor lintas cabang dan ruang terkait ditampilkan |
| US-06 | Super Admin menetapkan tarif dan Admin menerbitkan tagihan | Kewajiban mengikuti ketentuan berlaku | Cabang, sesi, periode, potongan, serta nilai historis tepat |
| US-07 | Admin menerima pembayaran tunai | Penerimaan sah dan kuitansi tercatat | Total alokasi benar dan pengiriman ulang tidak menggandakan transaksi |
| US-08 | Admin mengajukan transfer | Bukti dapat diperiksa pusat | Status menunggu; beberapa tagihan satu siswa dialokasikan dengan benar |
| US-09 | Super Admin memeriksa transfer | Dana masuk terkonfirmasi | Persetujuan dengan referensi unik; pengembalian mempunyai alasan |
| US-10 | Admin membuka pesan tunggakan | Pesan sesuai kewajiban siswa | Nomor, periode, nominal, dan jatuh tempo benar; pengiriman manual |
| US-11 | Admin menyerahkan dan pusat menerima kas | Perpindahan dana dapat ditelusuri | Penerimaan pusat dibedakan dari penyetoran bank |
| US-12 | Pengguna menelusuri dasbor sesuai kewenangan | Ringkasan mempunyai transaksi sumber | Pengajuan tertunda terpisah dan cabang historis tidak berubah |
| US-13 | Super Admin mencocokkan penerimaan | Dana yang cocok dapat dikenali | Satu referensi bank tidak digunakan untuk dua sumber |
| US-14 | Super Admin mengelola data induk dan akun | Akses serta parameter dasar terkendali | Perubahan berwenang tercatat tanpa menghapus riwayat |

Tabel 3.13 menyajikan matriks keterlacakan (*traceability matrix*) yang menghubungkan setiap butir kebutuhan fungsional dengan kode sumber elisitasi, cerita pengguna, pemodelan kasus penggunaan, alokasi iterasi PxP, serta kelompok validasi pengujiannya. Matriks komprehensif ini menjamin bahwa setiap kebutuhan bisnis yang disuarakan oleh mitra memiliki representasi nyata pada rancangan arsitektur dan dapat diverifikasi secara transparan hingga tahap akhir evaluasi.

**Tabel 3.13 Keterlacakan Kebutuhan sampai Evaluasi**

| Kebutuhan | Sumber | Cerita | Use case | Iterasi | Pemeriksaan |
| :--- | :--- | :--- | :--- | :--- | :--- |
| KF-01 | S-02/S-05 | US-01 | UC-00 | I-01 | PU-01; UAT-01 |
| KF-02 | S-01/S-04 | US-02 | UC-01 | I-01 | PU-02; UAT-02 |
| KF-03 | S-04/S-06 | US-03 | UC-02 | I-01 | PU-03; UAT-03 |
| KF-04 | S-06 | US-04 | UC-03 | I-02 | PU-04; UAT-04 |
| KF-05 | S-02/S-04/S-05 | US-05 | UC-04 | I-02 | PU-05; UAT-05 |
| KF-06 | S-01/S-03/S-04 | US-06 | UC-05 | I-01 | PU-06; UAT-06 |
| KF-07 | S-03/S-04 | US-07 | UC-06 | I-03 | PU-07; UAT-07 |
| KF-08 | S-03/S-06/S-07 | US-08 | UC-07 | I-03 | PU-08; UAT-08 |
| KF-09 | S-03/S-06/S-07 | US-09 | UC-08 | I-03 | PU-09; UAT-09 |
| KF-10 | S-04/S-06 | US-10 | UC-09 | I-03 | PU-10; UAT-10 |
| KF-11 | S-03/S-04/S-07 | US-11 | UC-10 | I-04 | PU-11; UAT-11 |
| KF-12 | S-02/S-03 | US-12 | UC-12 | I-04 | PU-12; UAT-12 |
| KF-13 | S-03/S-07 | US-13 | UC-11 | I-04 | PU-13; UAT-13 |
| KF-14 | S-02/S-05/S-07 | US-14 | UC-13 | I-01 | PU-14; UAT-14 |

Setiap gugus paket pengujian (PU) mencakup kombinasi kondisi pengujian normal, penanganan eksepsi sistem, serta kondisi batas ekstrem pada modul fungsional terkait. Rincian skenario pengujian kotak hitam dijabarkan secara terperinci menggunakan kode BB dan ditautkan langsung dengan sumber elisitasi primer serta status verifikasinya pada lampiran matriks keterlacakan. Keterkaitan terstruktur ini memberikan visibilitas penuh bagi pengembang dan dosen pembimbing untuk memantau kemajuan pengujian sistem secara objektif.

### 3.4.5 Pemodelan Kasus Penggunaan (*Use Case*) dan Skenario

Pemodelan kasus penggunaan (*use case*) mengabstraksikan interaksi fungsional antara aktor pengguna dengan kapabilitas komputasi yang disediakan oleh sistem ARTHA. Penerapan diagram kasus penggunaan ini merujuk pada standar rekayasa perangkat lunak untuk sistem informasi manajemen (Ahadi dkk., 2025). Diagram Use Case pada Gambar 3.2 merepresentasikan batasan fungsionalitas sistem yang selanjutnya dijabarkan secara terperinci ke dalam skenario interaksi tekstual.

![Use case inti sistem ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_2_Use_Case_Inti.png>)

**Gambar 3.2 Diagram Kasus Penggunaan Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan operasional ARTHA.

Arsitektur kasus penggunaan ARTHA mencakup empat belas skenario inti, yakni UC-00 hingga UC-13, yang melibatkan peran Admin Cabang dan Super Admin. Sebagai ilustrasi alur kerja kolaboratif lintas peran, proses pengajuan transfer dan verifikasi dana masuk disajikan pada Tabel 3.14. Penjabaran skenario lengkap beserta kamus interaksi setiap kasus penggunaan didokumentasikan secara mandiri pada dokumen pelengkap rancangan sistem.

**Tabel 3.14 Skenario Pengajuan dan Pemeriksaan Transfer**

| Unsur | Rancangan |
| :--- | :--- |
| Identitas | UC-07 pengajuan transfer dan UC-08 pemeriksaan transfer |
| Pelaksana | Admin Cabang sebagai pengaju; Super Admin sebagai pemeriksa berwenang |
| Prasyarat | Akun sah, tagihan tersedia, rekening resmi aktif, dan kewenangan pemeriksa telah ditetapkan |
| Pengajuan | Pilih tagihan satu siswa serta cabang, isi nominal, tanggal dan rekening, unggah bukti, lalu kirim |
| Keadaan antara | Status menunggu verifikasi; tagihan belum dilunasi dan antrean tampil pada dasbor |
| Pemeriksaan | Bandingkan identitas, nominal, rekening, dan tanggal dengan referensi dana masuk yang dicatat manual |
| Persetujuan | Kunci transaksi terkait, periksa ulang sisa tagihan serta referensi, lalu simpan keputusan dan pencocokan satu kali |
| Pengembalian | Simpan alasan; perbaikan menghasilkan pengajuan baru dengan tautan ke pengajuan lama |
| Pengecualian | Bukti tidak terbaca, nominal berbeda, referensi sudah digunakan, sisa tagihan berubah, atau akses tidak berwenang |
| Pascakondisi | Riwayat tersimpan; hanya pembayaran terkonfirmasi mengurangi sisa; kuitansi final terbit setelah persetujuan |

Diagram use case menyajikan batas interaksi fungsional tingkat tinggi, sedangkan rincian validasi formulir dan pengujian otorisasi diuraikan secara mendalam di dalam narasi skenario. Setiap skenario mengompilasi alur kerja normal (*happy path*) serta skenario penanganan eksepsi yang mengantisipasi kesalahan masukan maupun kegagalan jaringan. Dokumentasi berlapis ini menjaga kejelasan model fungsional tanpa mengorbankan ketelitian aturan bisnis pada setiap tahapan interaksi.

### 3.4.6 Perancangan Basis Data

Struktur persistensi data sistem ARTHA dimodelkan secara terpusat dengan mengintegrasikan dua puluh tiga tabel relasional yang ternormalisasi. Entitas identitas master, riwayat keanggotaan kelas, kewajiban tagihan, transaksi pembayaran kasir, serta log perpindahan kas dirancang secara terpisah guna menjaga integritas referensial dan ketertelusuran historis. Model data konseptual disajikan pada Gambar 3.3, sedangkan rincian Entity Relationship Diagram (ERD) fisik dan kamus data komprehensif dilampirkan pada dokumen basis data pendukung.

![Hubungan konseptual data ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_3_Model_Data_Konseptual.png>)

**Gambar 3.3 Hubungan Data Utama Prototipe ARTHA**

Sumber: rancangan penelitian berdasarkan pemisahan proses operasional.

Tabel 3.15 mengklasifikasikan dua puluh tiga tabel relasional ke dalam delapan gugus fungsional yang merefleksikan domain operasional bimbingan belajar. Pada domain transaksi keuangan, pencatatan pembayaran dihubungkan dengan tagihan melalui entitas alokasi agar satu transaksi penerimaan dapat melunasi beberapa tagihan siswa sekaligus secara fleksibel. Pengelompokan modular ini mempermudah pemeliharaan skema data dan optimalisasi kueri pelaporan di masa mendatang.

**Tabel 3.15 Kelompok Tabel dan Hubungan Utama**

| Kelompok | Tabel | Hubungan utama |
| :--- | :--- | :--- |
| Periode dan kewenangan | `academic_years`, `branches`, `users` | Tahun ajaran, cabang penugasan, dan peran pengguna |
| Identitas dan kompetensi | `students`, `mentors`, `subjects`, `mentor_subjects` | Kontak wali serta satu identitas tentor untuk pemeriksaan lintas cabang |
| Kelas dan jadwal | `class_rooms`, `classes`, `class_schedules`, `class_enrollments` | Ruang fisik, kelompok, masa jadwal, serta riwayat keanggotaan |
| Kewajiban | `fee_tariffs`, `bills` | Tarif menurut cabang, sesi, dan siklus; tagihan menyimpan nilai aktual |
| Penerimaan | `payments`, `payment_allocations`, `payment_reviews` | Induk pembayaran, pembagian ke tagihan, dan keputusan pemeriksaan |
| Perpindahan kas | `cash_batches`, `cash_batch_items` | Satu kelompok penyerahan memuat pembayaran tunai sumber |
| Pencocokan bank | `bank_accounts`, `bank_entries`, `bank_matches` | Rekening resmi, dana masuk manual, dan satu sumber yang dicocokkan |
| Ketertelusuran | `reminder_actions`, `activity_logs` | Tindakan membuka WhatsApp serta perubahan penting oleh petugas |

Karakteristik atribut penting dan konstrain integritas data yang diterapkan pada skema basis data dirangkum pada Tabel 3.16. Kalkulasi metrik operasional seperti total siswa aktif, akumulasi sisa tagihan, status jatuh tempo, dan rekapitulasi penerimaan kas dihitung secara langsung dari transaksi sumber (*derived data*). Pendekatan integritas ini memastikan informasi yang ditampilkan pada dasbor pimpinan selalu konsisten terhadap dinamika transaksi di tingkat cabang.

**Tabel 3.16 Atribut dan Kendala Kritis Rancangan Data**

| Objek | Atribut atau hubungan penting | Kendala rancangan |
| :--- | :--- | :--- |
| Pengguna | Peran, cabang penugasan, status | Cabang kosong tidak memberikan hak Super Admin |
| Kelas | `max_students`, `near_full_remaining` | Peserta aktif tidak melebihi kapasitas; ambang belum diisi dengan angka kebijakan tanpa validasi |
| Keanggotaan | Siswa, kelas, waktu masuk, waktu keluar, alasan | Tidak ada dua keanggotaan aktif siswa pada kelas yang sama; masuk kembali membuat riwayat baru |
| Jadwal | Hari, jam, rentang tanggal, tentor, ruang, status | Periksa masa berlaku, cabang ruang, irisan, dan pengecualian jadwal yang disunting |
| Tagihan | Cabang historis, periode, tarif, nilai, potongan beralasan | Periode tidak ganda dan perubahan tarif tidak mengubah tagihan lama |
| Pembayaran | Siswa, cabang historis, kanal, status, pengajuan asal | Pengajuan ulang tertaut; pengajuan menunggu atau dikembalikan belum menjadi penerimaan |
| Alokasi | Pembayaran, tagihan, nominal | Siswa serta cabang sama; total sesuai pembayaran dan tidak melebihi sisa sah |
| Pemeriksaan | Pengajuan, petugas, keputusan, waktu, alasan | Riwayat tidak ditimpa dan keputusan final hanya berlaku sekali |
| Pencocokan | Dana masuk dan salah satu sumber | Sumber berupa transfer atau setoran; nominal penuh sama dan referensi tidak dipakai ganda |

Proses penempatan siswa dikaitkan secara ketat pada rombongan belajar aktif yang memiliki jadwal valid dan alokasi ruangan dengan daya tampung yang mencukupi. Apabila kapasitas ruangan atau kelompok diubah oleh pengelola, sistem secara otomatis mengevaluasi ulang kesesuaian kuota terhadap jumlah siswa terdaftar saat itu. Seluruh operasi pembaruan keanggotaan dieksekusi dalam satu transaksi atomik guna menjamin ketiadaan anomali data saat terjadi akses bersamaan.

Identitas cabang penerbit tagihan dan penerima pembayaran disimpan secara permanen pada saat transaksi pertama kali dibukukan (*snapshot data*). Mekanisme ini memastikan rekam jejak pendapatan kas historis tetap melekat pada cabang asal meskipun siswa yang bersangkutan di kemudian hari berpindah ke cabang bimbingan belajar lain. Sisa tagihan dihitung dari nilai kewajiban dikurangi alokasi pembayaran yang telah diverifikasi, sedangkan status keterlambatan ditentukan secara independen berdasarkan tanggal jatuh tempo yang berlaku.

Implementasi skema fisik basis data direalisasikan menggunakan sistem manajemen basis data MySQL dengan mesin penyimpanan transaksi InnoDB. Seluruh keterhubungan kunci asing (*foreign key*), pengindeksan kolom pencarian, isolasi transaksi, dan validasi *check constraint* diuji secara ketat melalui skrip migrasi terautomasi. Verifikasi menyeluruh ini menjamin bahwa lapisan persistensi data mampu menjaga integritas data operasional bimbingan belajar di bawah beban kerja riil.

### 3.4.7 Perancangan Antarmuka

Perancangan antarmuka pengguna disusun dengan mengutamakan prinsip ergonomi dan kemudahan navigasi agar staf administrasi dapat menjalankan tugas operasional secara intuitif dan efisien. Enam antarmuka utama pada Gambar 3.4 hingga Gambar 3.9 menggambarkan visualisasi halaman kerja dari aktivitas pencatatan cabang hingga modul pemantauan pusat. Keterkaitan fungsional antara halaman antarmuka, kode cerita pengguna, serta aksi operasional utamanya dirangkum pada Tabel 3.17.

**Tabel 3.17 Rancangan Antarmuka Inti**

| Layar | Cerita pengguna | Tindakan utama |
| :--- | :--- | :--- |
| Dasbor cabang | US-08, US-10, US-12 | Memilih tindak lanjut transaksi serta keterisian |
| Keanggotaan kelas | US-03, US-04 | Menambah peserta atau mengakhiri keanggotaan |
| Pengajuan transfer | US-08 | Memilih tagihan dan mengirim bukti |
| Pemeriksaan transfer | US-09 | Memeriksa dana masuk dan mengambil keputusan |
| Tunggakan WhatsApp | US-10 | Memeriksa pesan dan membuka WhatsApp |
| Dasbor pusat dan pencocokan | US-11, US-12, US-13 | Menelusuri setoran, penerimaan, dan referensi bank |

Seluruh nama siswa, angka transaksi, dan nomor rekening yang ditampilkan pada gambar purwarupa antarmuka merupakan data sintetis simulasi yang digunakan khusus untuk keperluan demonstrasi pengujian. Setiap indikator visual berbasis warna (seperti penanda status pembayaran atau kuota kelas) selalu disertai label teks deskriptif guna memastikan aksesibilitas informasi. Standardisasi istilah status transaksi juga diterapkan secara seragam antara tampilan antarmuka, diagram pemodelan, dan kamus data basis data.

Halaman Dasbor Admin Cabang pada Gambar 3.4 menyajikan informasi rekapitulasi tunggakan siswa, antrean pengajuan transfer yang sedang ditinjau, serta status keterisian ruang kelas secara ringkas dan terfokus. Staf administrasi dapat langsung menelusuri rincian data melalui kartu navigasi tersebut untuk menindaklanjuti tugas operasional di cabangnya masing-masing. Tata letak informasi ini secara efektif mendukung pemenuhan cerita pengguna US-08, US-10, dan US-12.

![Dasbor Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_4_Dasbor_Cabang.png>)

**Gambar 3.4 Dasbor Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Halaman pengelolaan keanggotaan kelas pada Gambar 3.5 memvisualisasikan jumlah siswa aktif, daya tampung maksimum, dan sisa kursi kosong sebelum staf menempatkan siswa baru. Indikator peringatan hampir penuh memberikan panduan visual bagi staf dalam memilih kelas yang tepat, sedangkan tombol pendaftaran otomatis dinonaktifkan ketika kapasitas kelas telah penuh. Proses penghentian keanggotaan siswa mewajibkan pengisian tanggal dan alasan keluar tanpa menghapus profil siswa dari sistem, sesuai dengan spesifikasi cerita pengguna US-03 dan US-04.

![Penempatan dan Keanggotaan Kelas](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_5_Keanggotaan_Kelas.png>)

**Gambar 3.5 Penempatan dan Keanggotaan Kelas**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Formulir pengajuan transfer pada Gambar 3.6 mengintegrasikan pemilihan data siswa, penentuan cabang transaksi, daftar tagihan yang akan dilunasi, kalkulasi alokasi nominal, rekening tujuan transfer, serta pratinjau berkas bukti bayar. Pengajuan yang telah dikirimkan oleh Admin Cabang pada US-08 akan masuk ke dalam antrean verifikasi berstatus menunggu peninjauan. Apabila pengajuan tersebut sebelumnya pernah ditolak, formulir perbaikan tetap menampilkan keterkaitan historis dengan pengajuan awal guna menjaga rekam jejak pemeriksaan.

![Pengajuan Transfer oleh Admin Cabang](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_6_Pengajuan_Transfer.png>)

**Gambar 3.6 Pengajuan Transfer oleh Admin Cabang**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Antarmuka verifikasi transfer bagi Super Admin pada Gambar 3.7 menyandingkan data pengajuan cabang secara berdampingan dengan berkas bukti transfer dan mutasi rekening bank yang dicatat petugas. Melalui alur kerja US-09 ini, Super Admin mengevaluasi kesesuaian nominal dan nomor referensi sebelum menetapkan keputusan persetujuan. Jika pengajuan dinyatakan tidak valid, pengisian catatan alasan penolakan diwajibkan oleh sistem agar staf administrasi cabang dapat segera melakukan perbaikan dokumen.

![Pemeriksaan Transfer oleh Super Admin](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_7_Pemeriksaan_Transfer.png>)

**Gambar 3.7 Pemeriksaan Transfer oleh Super Admin**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Halaman pemantauan tunggakan pada Gambar 3.8 mengompilasi rincian periode belajar, akumulasi tunggakan, batas jatuh tempo, nomor kontak wali murid, dan pratinjau pesan otomatis sebelum staf mengeksekusi US-10. Penekanan tombol WhatsApp secara otomatis memicu pembukaan aplikasi perpesanan dengan format pesan dan nomor tujuan yang telah terisi lengkap untuk ditinjau oleh staf. Sistem secara internal mencatat log pembukaan tautan tersebut sebagai arsip penagihan, sedangkan pengiriman pesan berlangsung di luar lingkup aplikasi ARTHA.

![Tunggakan dan Pratinjau Pesan WhatsApp](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_8_Tunggakan_WhatsApp.png>)

**Gambar 3.8 Tunggakan dan Pratinjau Pesan WhatsApp**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

Halaman Dasbor Pusat dan Rekonsiliasi pada Gambar 3.9 menyajikan agregasi tunggakan seluruh cabang, total penerimaan kas terverifikasi, antrean verifikasi transfer, serta transaksi yang telah direkonsiliasi dengan bank secara terpisah. Melalui fungsionalitas US-12 dan US-13, pimpinan dapat menelusuri setiap baris ringkasan hingga ke dokumen transaksi primer dan referensi mutasi perbankan. Penelusuran berjenjang ini menjaga keterkaitan data yang utuh, sehingga mutasi setoran kas cabang tidak akan dihitung ganda sebagai pendapatan bimbingan belajar baru.

![Dasbor Pusat dan Pencocokan Penerimaan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_9_Dasbor_Pusat_Pencocokan.png>)

**Gambar 3.9 Dasbor Pusat dan Pencocokan Penerimaan**

Sumber: rancangan penelitian; data pada antarmuka merupakan data simulasi.

## 3.5 Spesifikasi Teknis

Spesifikasi teknis menguraikan konfigurasi arsitektur komputasi, perangkat keras, teknologi perangkat lunak, serta standarisasi lingkungan yang digunakan dalam merealisasikan prototipe ARTHA. Pemaparan ini menetapkan parameter teknis yang menjamin sistem dapat direplikasi dan diuji secara objektif pada kondisi operasional bimbingan belajar. Seluruh versi pustaka dan spesifikasi fisik dicatat secara mendalam sebagai konteks komputasi dari hasil pengujian kinerja maupun fungsionalitas sistem.

### 3.5.1 Arsitektur Sistem

Sistem informasi ARTHA dibangun menggunakan arsitektur web modern yang memisahkan secara tegas lapisan presentasi antarmuka pengguna, lapisan logika bisnis aplikasi, dan lapisan persistensi data. Kerangka kerja Next.js digunakan untuk merender antarmuka pengguna di sisi klien secara responsif, kerangka kerja Laravel mengelola aturan bisnis melalui penyediaan *Application Programming Interface* (API) RESTful, sedangkan basis data MySQL berfungsi sebagai penyimpan data relasional terpusat. Pemisahan arsitektur terdistribusi (*decoupled architecture*) ini meningkatkan modularitas sistem serta memudahkan skalabilitas dan pemeliharaan kode secara mandiri.

Gambar 3.10 memvisualisasikan interaksi komputasi antara aktor pengguna, antarmuka web, layanan API peladen, dan basis data terpusat. Diagram tersebut juga memetakan batas sistem (*system boundary*) terhadap aktivitas eksternal, seperti interaksi perpesanan melalui protokol WhatsApp dan verifikasi manual mutasi perbankan oleh petugas. Pemodelan arsitektur ini mempertegas batasan proses yang dikelola secara terautomasi oleh sistem dan domain verifikasi yang menjadi wewenang personel operasional.

![Arsitektur prototipe ARTHA](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/gambar/Gambar_3_10_Arsitektur_Prototipe.png>)

**Gambar 3.10 Arsitektur Prototipe Sistem Informasi ARTHA**

Sumber: rancangan penelitian berdasarkan kebutuhan akses multicabang dan pemisahan proses pengelolaan data.

Mekanisme autentikasi dan otorisasi sesi pengguna diimplementasikan menggunakan pustaka Laravel Sanctum dengan pendekatan sesi berbasis kuki (*stateful cookie-based session*) yang aman untuk aplikasi satu halaman (*Single Page Application*). Konfigurasi domain silang (*cross-origin*), perlindungan terhadap serangan *Cross-Site Request Forgery* (CSRF), serta masa aktif sesi diselaraskan dengan parameter lingkungan penerapan. Kepatuhan implementasi keamanan ini diverifikasi secara berkala dengan merujuk pada standar dokumentasi resmi kerangka kerja (Laravel, t.t.-a).

Pengajuan transfer yang masuk dari seluruh cabang dihimpun secara dinamis ke dalam antrean verifikasi pada dasbor Super Admin berdasarkan status transaksi aktif. Antrean ini menjadi titik kendali utama bagi manajemen pusat dalam memantau dan memvalidasi arus dana masuk secara terstruktur. Apabila pihak mitra membutuhkan penanda notifikasi yang interaktif, mekanisme notifikasi basis data bawaan Laravel disiapkan untuk diintegrasikan setelah kebutuhan operasional tersebut difinalisasi (Laravel, t.t.-b).

Dasbor analitik mengambil data transaksi mutakhir langsung dari basis data terpusat setiap kali halaman diakses atau dimuat ulang oleh pengguna. Melalui mekanisme pemuatan data berbasis permintaan ini, pemantauan *real-time* didefinisikan sebagai penyajian data terkini yang konsisten terhadap transaksi terakhir yang tersimpan di peladen. Pembaruan data otomatis secara serentak tanpa pemuatan ulang (*real-time websocket broadcast*) tidak dimasukkan ke dalam ruang lingkup awal guna menjaga efisiensi konsumsi sumber daya peladen.

Frekuensi pembaruan data dan toleransi ambang waktu tanggapan (*response time*) diselaraskan dengan ritme kerja kasir dan kapasitas infrastruktur mitra. Kesepakatan kriteria performa ini ditetapkan bersama pembimbing sebelum sesi pengujian beban dilakukan. Hasil pengukuran waktu tanggapan fungsi utama selanjutnya dilaporkan secara transparan pada bab hasil dan pembahasan.

### 3.5.2 Perangkat Keras

Lingkungan komputasi pengembang difungsikan untuk menjalankan penyunting kode sumber, peladen pengembangan antarmuka, layanan *backend* API, serta instans basis data lokal secara simultan. Kebutuhan spesifikasi perangkat keras bagi pengguna akhir ditentukan berdasarkan beban kerja administrasi harian dan skenario pengujian UAT bersama mitra. Tabel 3.18 merangkum spesifikasi perangkat keras workstation pengembang yang tersedia serta rencana perangkat uji coba pengguna.

**Tabel 3.18 Ketersediaan dan Rencana Perangkat Keras**

| Perangkat | Informasi tersedia | Pelengkapan sebelum pengujian |
| :--- | :--- | :--- |
| Komputer penyusunan | Laptop pengembang berbasis Windows 11 Home 64-bit | AMD Ryzen 5 5600H (6 core, 12 thread, hingga 4,2 GHz), RAM 24 GB DDR4, NVMe SSD 512 GB, dan NVIDIA GeForce RTX 3050 |
| Komputer pengguna | Perangkat operasional administrasi cabang dan pusat | PC Desktop atau Laptop mitra (Intel Core i3 atau setara, RAM minimal 4 GB, resolusi layar 1366x768 atau 1920x1080 piksel, peramban Google Chrome atau Microsoft Edge terbaru, koneksi internet cabang) |
| Telepon uji | Pengujian antarmuka seluler dan tautan WhatsApp | Ponsel cerdas Android atau iOS (layar 6,5 inci, peramban seluler, serta aplikasi resmi WhatsApp terpasang untuk pengujian fungsionalitas tautan pesan tunggakan) |
| Peladen uji | Akses evaluasi operasional bersama mitra | Peladen uji terisolasi (Cloud VPS Linux Ubuntu 24.04 LTS, 2 vCPU, RAM 4 GB, penyimpanan SSD 50 GB, Nginx, domain staging privat, dan sertifikat SSL Let's Encrypt) |
| Perangkat cetak | Pengujian keluaran fisik tanda bukti bayar | Printer cabang (printer inkjet atau laser multifungsi untuk pengujian cetak kuitansi pembayaran SPP format kertas A4 standar) |

Spesifikasi rinci setiap perangkat yang terlibat dalam sesi pengujian dicatat bersama indikator stabilitas jaringan lokal pada saat evaluasi berlangsung. Dokumentasi lingkungan fisik ini penting untuk memberikan interpretasi yang valid terhadap hasil pengujian performa sistem ARTHA. Inventaris perangkat keras pengguna dan konfigurasi peladen uji akan diperbarui secara aktual sesuai alokasi fasilitas dari pihak mitra.

### 3.5.3 Perangkat Lunak dan Versi Teknologi

Repositori proyek antarmuka web ARTHA mengelola seluruh dependensi pustaka menggunakan berkas manifes penguncian dependensi guna menjamin reproduksibilitas lingkungan pengembangan. Pemetaan versi perangkat lunak pada Tabel 3.19 diverifikasi secara langsung dari berkas konfigurasi dependensi sistem per tanggal 25 Oktober 2026. Tabel tersebut juga merangkum tumpukan teknologi layanan aplikasi, mesin basis data, serta kakas pendukung yang digunakan dalam integrasi sistem.

**Tabel 3.19 Pilihan Teknologi dan Status Versi**

| Komponen | Pilihan dan bukti tersedia | Status penggunaan |
| :--- | :--- | :--- |
| Antarmuka | Next.js 16.2.12 dan React 19.2.4 pada `package-lock.json` | Tersedia pada proyek lokal; versi evaluasi dibekukan sebelum UAT |
| Tata tampilan | Tailwind CSS 4.3.3 pada `package-lock.json` | Tersedia pada proyek antarmuka |
| Layanan aplikasi | Laravel 11.x dan PHP 8.3 (tersedia PHP 8.3.30 pada Laragon) | Penyedia layanan data dan RESTful API; dependensi dikelola melalui Composer |
| Autentikasi | Laravel Sanctum berbasis sesi untuk antarmuka milik aplikasi | Direncanakan; konfigurasi domain dan sesi diperiksa pada implementasi |
| Basis data | MySQL Community Server 8.0 dan 8.4 LTS pada Laragon | DBMS dengan mesin InnoDB untuk transaksi atomik dan integritas data |
| Dependensi | Pengelola paket JavaScript dan Composer | Berkas penguncian disimpan bersama versi kode |
| Pengujian | Pengujian unit aturan bisnis serta pengujian layanan dan antarmuka | Perangkat, versi, dan perintah ditetapkan setelah lingkungan layanan tersedia |
| Dokumentasi | Markdown, diagram PNG/SVG, dan pengelola referensi | Sumber diagram serta matriks rancangan disimpan untuk penelusuran |

Konfigurasi lingkungan antarmuka disesuaikan dengan prasyarat instalasi dan optimalisasi kompilasi pada dokumentasi resmi Next.js (Vercel, t.t.). Kompatibilitas antara versi PHP 8.3 dan kerangka kerja Laravel 11 diverifikasi terhadap pedoman rilis resmi untuk memastikan stabilitas dukungan jangka panjang (Laravel, t.t.-c). Standardisasi versi ini mengeliminasi disparitas perilaku aplikasi antara lingkungan pengembangan lokal dan lingkungan pengujian bersama pengguna.

Berkas dependensi, variabel konfigurasi lingkungan (*environment variables*), dan skrip migrasi basis data diarsipkan secara terstruktur pada repositori sistem. Sebelum pengujian terintegrasi dilaksanakan, pengembang membekukan versi pustaka (*version lock*) serta menguji konsistensi skema basis data hasil migrasi. Prosedur ini menjamin lingkungan evaluasi dapat dibangun kembali dengan karakteristik yang identik kapan pun diperlukan.

### 3.5.4 Lingkungan Implementasi dan Pengujian

Pengembangan kode program dan kegiatan evaluasi UAT dijalankan pada dua lingkungan komputasi yang terisolasi secara mandiri guna mencegah kontaminasi data transaksi. Pengujian modul pada fase awal memanfaatkan kumpulan data sintetis yang merepresentasikan karakteristik operasional cabang. Penggunaan data transaksi riil dari mitra dibatasi secara ketat berdasarkan perjanjian kerahasiaan dan hanya dialokasikan untuk memvalidasi skenario tugas penerimaan pengguna.

Seluruh berkas bukti transfer yang diunggah pengguna disimpan dalam direktori penyimpanan terproteksi (*private storage*) yang mewajibkan verifikasi hak akses sebelum berkas dapat diunduh. Kredensial koneksi basis data, kunci enkripsi aplikasi, serta kata sandi akun dikelola melalui berkas konfigurasi terlindungi di luar repositori publik. Protokol keamanan ini ditegakkan secara disiplin guna memastikan informasi sensitif mitra tidak terekspos pada dokumentasi tugas akhir maupun media publikasi ilmiah.

Pencatatan waktu transaksi pada lapisan basis data disimpan dalam format standar *Coordinated Universal Time* (UTC) dan dikonversikan ke dalam zona waktu Waktu Indonesia Tengah (WITA / Asia/Makassar) saat dirender pada antarmuka pengguna sesuai domisili operasional Balikpapan. Kalender penagihan dan perhitungan jatuh tempo mengacu secara seragam pada zona waktu lokal tersebut. Ketentuan ini menjamin akurasi kronologis transaksi pembayaran kasir dan riwayat log aktivitas pengguna.

Pengujian isolasi akses multicabang disiapkan dengan mengonfigurasi minimal dua akun Admin Cabang dari cabang yang berbeda serta satu akun Super Admin pengendali. Akun simulasi ini dieksekusi terhadap bundel data uji yang mencerminkan variasi operasional nyata bimbingan belajar. Parameter jaringan, spesifikasi perangkat peramban, dan nomor rilis aplikasi dicatat secara berkala sepanjang proses pengujian.

Struktur data awal mencakup data uji kelas dengan status kuota bervariasi (tersedia, mendekati penuh, dan penuh), jadwal tentor yang beririsan, tagihan multivariasi, serta transaksi pengajuan transfer dengan riwayat persetujuan maupun penolakan. Setelah data awal dimuat, integritas sistem diverifikasi dan titik pemulihan awal (*initial snapshot*) disimpan ke media cadangan. Ketersediaan cadangan data awal ini memungkinkan pemulihan instan ke status bersih ketika suatu skenario pengujian perlu diulang kembali.

Prosedur pencadangan dieksekusi secara berkala mencakup ekspor skema basis data dan direktori penyimpanan berkas bukti bayar yang saling terhubung. Pengembang melakukan uji coba pemulihan data pada instans uji terpisah guna memverifikasi integritas dan kelengkapan data hasil restorasi. Dokumentasi prosedur pencadangan dan pemulihan ini disajikan sebagai bukti keandalan tata kelola data operasional prototipe.

## 3.6 Jadwal Pembuatan Prototipe

Rencana pelaksanaan tugas akhir prototipe ARTHA dipetakan ke dalam jangka waktu dua belas minggu kerja efektif, yang mencakup empat siklus iterasi PxP berdurasi masing-masing dua minggu. Dokumentasi elisitasi kebutuhan dan artefak perancangan sistem yang dihimpun per 25 Oktober 2026 diposisikan sebagai landasan awal pelaksanaan tahap implementasi. Tanggal peresmian dimulainya siklus pengodean dan jadwal evaluasi UAT disepakati secara resmi bersama dosen pembimbing dan perwakilan manajemen bimbingan belajar.

Tabel 3.20 menyajikan distribusi jadwal kegiatan penelitian mulai dari tahap klarifikasi bukti empiris hingga penyiapan luaran akhir tugas akhir. Penomoran minggu (M1 hingga M12) dihitung secara relatif berdasarkan tanggal sepakatan pelaksanaan di lapangan. Jadwal komprehensif ini berfungsi sebagai instrumen kendali proyek agar setiap tahapan pengembangan berjalan sesuai alokasi waktu yang direncanakan.

**Tabel 3.20 Rencana Jadwal Pelaksanaan Prototipe**

| Kegiatan | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Klarifikasi bukti dan aturan mitra | X | X | | | | | | | | | | |
| Estimasi tugas, instrumen, dan lingkungan | | X | | | | | | | | | | |
| I-01: data dasar dan akses | | | X | X | | | | | | | | |
| I-02: keanggotaan dan jadwal | | | | | X | X | | | | | | |
| I-03: pembayaran dan WhatsApp | | | | | | | X | X | | | | |
| I-04: setoran, laporan, pencocokan | | | | | | | | | X | X | | |
| UAT, perbaikan, dan uji ulang | | | | | | | | | | | X | X |
| Dokumentasi waktu, galat, dan rancangan | | X | X | X | X | X | X | X | X | X | X | X |
| Penyiapan serah uji, laporan, artikel, HKI | | | | | | | | | | | X | X |

Aktivitas pengujian unit otomatis, pengujian sistem kotak hitam, serta sesi retrospektif dieksekusi secara terpadu di dalam setiap siklus iterasi PxP agar evaluasi mutu perangkat lunak berlangsung secara berkesinambungan. Alokasi mingguan dijabarkan ke dalam estimasi jam kerja per tugas teknis sesaat sebelum iterasi aktif dimulai. Apabila terjadi perubahan kebutuhan operasional dari mitra, jadwal disesuaikan secara adaptif dengan mendokumentasikan dampaknya terhadap sisa beban kerja.

Penyusunan naskah laporan tugas akhir mengikuti pedoman tata tulis ilmiah resmi Institut Teknologi Kalimantan, sedangkan artefak luaran prototipe disiapkan sesuai dengan standar kompetensi tugas akhir jalur prototipe Program Studi Sistem Informasi (Institut Teknologi Kalimantan, 2025a; Institut Teknologi Kalimantan, 2026). Dinamika pengerjaan proyek dan penyesuaian jadwal dicatat secara transparan sepanjang pelaksanaan penelitian. Dokumentasi historis ini menghubungkan perencanaan awal dengan bukti empiris pelaksanaan yang dipertanggungjawabkan pada sidang tugas akhir.