# DOKUMEN INSTRUMEN PERTANYAAN VALIDASI LAPANGAN DAN WAWANCARA MITRA
**Rancang Bangun Prototipe Sistem Informasi Manajemen Operasional Bimbel Artha Balikpapan**

* **Mitra Penelitian**: Bimbingan Belajar (Bimbel) Artha Balikpapan (Delapan Cabang Operasional)
* **Penyusun**: Ariel (Mahasiswa Tugas Akhir Program Studi Sistem Informasi ITK)
* **Dosen Pembimbing**: Bu Ayu dan Pak Arif
* **Tujuan Dokumen**: Memvalidasi seluruh asumsi proses bisnis berjalan (*As-Is*), mengonfirmasi anomali operasional lapangan, memitigasi risiko finansial, serta memetakan batasan aturan sistem (*To-Be*) sesuai arahan akademik pembimbing.

---

## 📌 PETUNJUK PENGGUNAAN INSTRUMEN

Dokumen ini disusun sebagai panduan wawancara mendalam (*in-depth interview*) dan observasi langsung bersama tiga pihak utama, yaitu Pemilik Bimbel Artha (Om Tok), Perwakilan Staf Frontdesk Cabang, dan Staf Keuangan/Administrasi Manajemen Pusat. 

Setiap butir pertanyaan telah dilengkapi dengan kolom catatan lapangan (*field notes*) serta indikator luaran (*output indicator*) yang akan langsung digunakan sebagai data primer penyusunan BAB 1 (Latar Belakang dan Rumusan Masalah) serta BAB 3 (Analisis Kebutuhan dan Pemodelan Sistem).

---

## 🔹 MODUL 1: PROSES PENDAFTARAN SISWA, BUKU BESAR A4, DAN ATURAN DISKON
*Fokus: Menggali detail langkah administratif saat pendaftar datang, format kolom buku besar A4, penentuan potongan harga, serta dokumen fisik yang diserahkan.*

### 1.1 Observasi dan Pernyataan Kondisi Berjalan (*As-Is*)
Calon siswa atau wali murid datang langsung ke meja frontdesk cabang untuk mendaftar. Staf frontdesk mencatat data identitas siswa, nomor telepon, dan asal sekolah. Pada lembar dokumen yang terdokumentasi, pencatatan dimulai dari bulan Juli (semester satu). Pihak frontdesk juga menilai kemampuan ekonomi calon siswa secara visual atau subjektif guna memberikan potongan biaya, serta mengecek status kepesertaan saudara kandung (kakak atau adik).

### 1.2 Daftar Pertanyaan Validasi Lapangan
1. **Siklus Pembukuan Pendaftaran**:
   * *Pertanyaan*: Apakah setiap buku besar pendaftaran A4 di cabang selalu dimulai pada bulan Juli mengikuti kalender tahun ajaran baru sekolah, ataukah ada buku pendaftaran baru yang dibuka pada bulan lain (misalnya Januari untuk semester genap)?
   * *Catatan Lapangan*: `[ ............................................................ ]`
2. **Kriteria Pemberian Diskon Ekonomi**:
   * *Pertanyaan*: Bagaimana parameter atau kriteria konkret yang digunakan staf frontdesk saat memutuskan seorang calon siswa berhak mendapatkan potongan biaya atas dasar pertimbangan ekonomi? Apakah frontdesk harus meminta izin atau persetujuan terlebih dahulu kepada pemilik (Om Tok) sebelum menetapkan harga diskon tersebut, ataukah frontdesk memiliki batas kewenangan mandiri?
   * *Catatan Lapangan*: `[ ............................................................ ]`
3. **Mekanisme Pengecekan Diskon Kakak Beradik**:
   * *Pertanyaan*: Bagaimana cara staf frontdesk memvalidasi apakah seorang calon pendaftar benar-benar memiliki kakak atau adik yang saat ini aktif les atau pernah les di Bimbel Artha? Apakah staf memeriksa lembar buku tahun-tahun sebelumnya satu per satu, menanyakan ke cabang lain melalui grup WhatsApp, atau hanya mengandalkan kejujuran lisan wali murid?
   * *Catatan Lapangan*: `[ ............................................................ ]`
4. **Struktur Kolom dan Format Buku Besar A4**:
   * *Pertanyaan*: Apa saja judul kolom resmi yang wajib diisi pada buku besar A4 pendaftaran dan iuran di cabang? Dari seluruh kolom tersebut, kolom mana saja yang paling sering kosong atau tidak lengkap diisi?
   * *Catatan Lapangan*: `[ ............................................................ ]`
5. **Paket Penyerahan Dokumen Pendaftar**:
   * *Pertanyaan*: Setelah data dicatat di buku besar, dokumen atau barang fisik apa saja yang langsung diserahkan kepada siswa di tempat (misalkan buku modul materi, kuitansi pendaftaran, kartu anggota siswa, atau seragam bimbel)?
   * *Catatan Lapangan*: `[ ............................................................ ]`
6. **Waktu Mulai Masuk Kelas Pasca-Pendaftaran**:
   * *Pertanyaan*: Berdasarkan pola yang berjalan selama ini, apakah siswa baru mayoritas langsung masuk kelas pada jam sesi saat itu juga, mulai keesokan harinya, atau harus menunggu jadwal awal pekan berikutnya?
   * *Catatan Lapangan*: `[ ............................................................ ]`

---

## 🔹 MODUL 2: PEMBAGIAN SESI BELAJAR, MANAJEMEN PENJADWALAN TENTOR, DAN INTEGRASI BUDAYA KERJA
*Fokus: Mengonfirmasi anomali jam sesi pagi, mekanisme distribusi beban kerja tentor, pembatasan bentrok jadwal, serta mitigasi risiko keterlambatan pengajar.*

### 2.1 Observasi dan Pernyataan Kondisi Berjalan (*As-Is*)
Jadwal bimbingan belajar dibagi menjadi sesi pagi dan sesi siang hingga malam:
* **Jadwal Pagi**:
  * Sesi 1: Pukul 07.30 hingga 09.30
  * Sesi 2: Pukul 09.00 hingga 10.30 (Terdapat tumpang tindih waktu 30 menit antara pukul 09.00 dan 09.30)
* **Jadwal Siang dan Malam**:
  * Sesi 1: Pukul 14.00 hingga 15.30
  * Sesi 2: Pukul 15.30 hingga 17.00
  * Sesi 3: Pukul 17.00 hingga 18.30
  * Sesi 4: Pukul 19.00 hingga 20.30

Pembagian jadwal selama ini dipengaruhi oleh budaya kekeluargaan dan senioritas tentor yang telah mengabdi bertahun-tahun. Tentor senior kerap meminta jam mengajar lebih padat guna meningkatkan pendapatan, yang berpotensi memicu jadwal bentrok, mobilitas terburu-buru antarcabang, atau keterlambatan masuk kelas.

### 2.2 Daftar Pertanyaan Validasi Lapangan
1. **Klarifikasi Tumpang Tindih (*Overlap*) Jam Sesi Pagi**:
   * *Pertanyaan*: Mengapa pada jadwal pagi Sesi 1 selesai pada pukul 09.30 sementara Sesi 2 sudah dimulai sejak pukul 09.00? Apakah kedua sesi tersebut menggunakan ruangan dan tentor yang berbeda, ataukah ada kekeliruan penulisan jam operasional di lapangan? Mengapa polanya berbeda dengan sesi siang yang bersambung secara runtut tanpa jeda?
   * *Catatan Lapangan*: `[ ............................................................ ]`
2. **Penanggung Jawab dan Prosedur Penetapan Jadwal**:
   * *Pertanyaan*: Siapa pejabat atau staf yang bertanggung jawab penuh dalam menyusun dan menetapkan pembagian jadwal tentor di awal semester? Bagaimana alur koordinasi antara manajemen pusat dengan frontdesk masing-masing cabang dalam mencocokkan ketersediaan waktu tentor?
   * *Catatan Lapangan*: `[ ............................................................ ]`
3. **Struktur Penggajian dan Honorarium Tentor**:
   * *Pertanyaan*: Bagaimana formula perhitungan gaji tentor di Bimbel Artha? Apakah bersifat honor flat bulanan, honor per jam mengajar, honor per sesi kelas, atau memperhitungkan jumlah siswa yang hadir di dalam kelas?
   * *Catatan Lapangan*: `[ ............................................................ ]`
4. **Mobilitas Tentor Lintas Cabang**:
   * *Pertanyaan*: Apakah seorang tentor diperbolehkan mengajar di dua cabang yang berbeda pada hari yang sama? Berapa estimasi jeda waktu perjalanan minimal yang diwajibkan oleh manajemen agar tentor tidak terlambat tiba di cabang berikutnya?
   * *Catatan Lapangan*: `[ ............................................................ ]`
5. **Dampak Keterlambatan dan Kompensasi Hak Siswa**:
   * *Pertanyaan*: Seberapa sering tentor terlambat tiba di kelas akibat macet atau cuaca hujan lebat di jalan saat berpindah cabang? Jika tentor terlambat selama 15 hingga 30 menit, bagaimana bentuk kompensasi jam belajar bagi siswa: apakah waktu kelas dimundurkan, diadakan sesi pengganti di hari lain, atau waktu belajar siswa hangus?
   * *Catatan Lapangan*: `[ ............................................................ ]`
6. **Batasan Sistem Penjadwalan: *Hard Constraint* versus *Warning Alert***:
   * *Pertanyaan*: Sesuai arahan Bu Ayu untuk meredam resistensi tentor senior, jika sistem baru mendeteksi jadwal tentor yang bentrok atau terlalu padat antarcabang, apakah manajemen menginginkan sistem langsung melarang jadwal tersebut (*hard lock*), ataukah sistem cukup memberikan peringatan (*warning alert*) namun manajemen tetap memiliki hak izin khusus (*manual override*) untuk menyetujuinya?
   * *Catatan Lapangan*: `[ ............................................................ ]`
7. **Pencatatan Kehadiran (*Presensi*) Tentor**:
   * *Pertanyaan*: Bagaimana cara frontdesk memastikan bahwa tentor benar-benar hadir dan mengajar sesuai durasi waktu yang ditetapkan? Apakah ada buku tanda tangan kehadiran fisik khusus tentor di meja frontdesk?
   * *Catatan Lapangan*: `[ ............................................................ ]`

---

## 🔹 MODUL 3: CAKUPAN JENJANG PENDIDIKAN CABANG DAN OPERASIONAL BIMBEL PRIVAT
*Fokus: Mengidentifikasi fasilitas tingkatan kelas di delapan cabang, kapasitas fisik ruangan, dan alur bimbingan privat guru datang ke rumah.*

### 3.1 Observasi dan Pernyataan Kondisi Berjalan (*As-Is*)
Bimbel Artha melayani jenjang Taman Kanak-Kanak (Calistung), SD, SMP, hingga SMA. Namun, ketersediaan fasilitas jenjang tersebut tidak seragam di seluruh cabang. Selain kelas reguler di kantor cabang, terdapat pula layanan les privat di mana tentor mendatangi langsung rumah murid.

### 3.2 Daftar Pertanyaan Validasi Lapangan
1. **Pemetaan Layanan TK pada Delapan Cabang**:
   * *Pertanyaan*: Dari delapan cabang Artha yang aktif saat ini, cabang mana saja yang menyediakan program kelas TK / Calistung? Untuk cabang yang tidak menyediakan kelas TK, apakah seluruhnya serentak melayani jenjang SD, SMP, dan SMA?
   * *Catatan Lapangan*: `[ ............................................................ ]`
2. **Kapasitas Fisik Ruang Kelas per Cabang**:
   * *Pertanyaan*: Berapa jumlah ruang kelas fisik yang tersedia di masing-masing cabang? Berapa batas kuota maksimal siswa per ruangan (misalkan maksimal 10 atau 12 anak)? Apakah pernah terjadi penumpukan siswa melebihi kapasitas kursi yang tersedia?
   * *Catatan Lapangan*: `[ ............................................................ ]`
3. **Prosedur dan Tarif Layanan Bimbel Privat**:
   * *Pertanyaan*: Apakah layanan bimbingan privat (tentor datang ke rumah siswa) masih aktif beroperasi saat ini? Bagaimana prosedur pendaftarannya, bagaimana pembagian honor tentor privat, dan berapa skema tarif biaya yang dibebankan kepada wali murid?
   * *Catatan Lapangan*: `[ ............................................................ ]`

---

## 🔹 MODUL 4: TRANSAKSI KEUANGAN, PENUTUPAN KAS HARIAN (*CUT-OFF*), REKONSILIASI, DAN RISIKO PEMBAYARAN
*Fokus: Membedah tata kelola kas fisik cabang, penagihan SPP, pencocokan mutasi bank manual, mitigasi manipulasi bukti transfer, serta wewenang kepala cabang.*

### 4.1 Observasi dan Pernyataan Kondisi Berjalan (*As-Is*)
Pembayaran pendaftaran dan SPP dilakukan melalui tunai di frontdesk cabang atau transfer bank/QRIS ke rekening yayasan. Kas tunai di cabang diambil setiap hari oleh orang kepercayaan pemilik yang berkeliling ke delapan cabang. Di sisi lain, data transaksi dicatat ganda, yaitu di buku besar kertas dan sebagian disalin ke lembar kerja Excel. Pihak manajemen harus memvalidasi data rekapan tersebut dengan mencocokkan mutasi rekening bank secara manual untuk ribuan siswa.

### 4.2 Daftar Pertanyaan Validasi Lapangan
1. **Mekanisme dan Jadwal Pengambilan Uang Kas Fisik**:
   * *Pertanyaan*: Pada pukul berapa orang kepercayaan pemilik biasanya datang mengambil setoran uang tunai di cabang? Apakah bentuk rekapan yang diserahkan bersama uang fisik tersebut berupa sobekan kertas kasir harian, lembaran rekap khusus, atau buku besar A4 yang ikut dibawa keliling?
   * *Catatan Lapangan*: `[ ............................................................ ]`
2. **Batas Waktu Penutupan Transaksi (*Cut-Off Time*) dan Penyimpanan Kas Malam**:
   * *Pertanyaan*: Sesuai penekanan Bu Ayu mengenai jam penutupan kas, jika kurir mengambil uang pada sore hari (misalkan pukul 16.00) dan pada Sesi 4 malam (pukul 19.00–20.30) ada pembayaran SPP tunai dari siswa, di mana uang kas fisik tersebut disimpan semalaman di cabang? Siapa yang bertanggung jawab atas keamanan uang tersebut sebelum diserahkan pada hari berikutnya?
   * *Catatan Lapangan*: `[ ............................................................ ]`
3. **Formulir dan Tanda Terima Serah Terima Kas**:
   * *Pertanyaan*: Apakah ada tanda tangan bukti serah terima kas resmi antara staf frontdesk dengan kurir pengambil uang tunai guna mencegah saling lempar tanggung jawab jika terjadi selisih nominal?
   * *Catatan Lapangan*: `[ ............................................................ ]`
4. **Alur Validasi Mutasi Bank versus Rekapan Cabang**:
   * *Pertanyaan*: Bagaimana prosedur teknis manajemen dalam memvalidasi pembayaran nontunai? Apakah manajemen benar-benar memelototi mutasi rekening koran atau aplikasi mobile banking satu per satu untuk mencocokkan setiap nama pengirim dengan catatan rekapan cabang? Berapa lama waktu yang dihabiskan untuk proses ini setiap pekannya?
   * *Catatan Lapangan*: `[ ............................................................ ]`
5. **Frekuensi Ketidaksesuaian (*Miss*) dan Selisih Pembayaran**:
   * *Pertanyaan*: Seberapa sering terjadi ketidaksesuaian dalam sebulan, seperti di rekapan cabang tercatat sudah membayar tetapi di mutasi rekening bank dana tidak ditemukan (atau sebaliknya)? Apakah pernah terjadi insiden kerugian finansial yang signifikan akibat selisih pencatatan tersebut?
   * *Catatan Lapangan*: `[ ............................................................ ]`
6. **Risiko Pemalsuan Bukti Transfer Digital**:
   * *Pertanyaan*: Sebagaimana disoroti oleh Bu Ayu mengenai potensi kecurangan digital (*AI photo manipulation*), apakah Bimbel Artha pernah mengalami kasus bukti transfer palsu atau struk pembayaran editan yang diserahkan oleh wali murid? Bagaimana staf frontdesk memastikan keaslian bukti transfer yang ditunjukkan melalui layar ponsel?
   * *Catatan Lapangan*: `[ ............................................................ ]`
7. **Peran Administratif Figur Senior / Kepala Cabang Nonformal**:
   * *Pertanyaan*: Apa peran nyata figur yang dituakan di cabang dalam urusan keuangan? Apakah beliau ikut memeriksa dan memvalidasi uang kas fisik sebelum diserahkan ke kurir manajemen, ataukah urusan kas sepenuhnya langsung antara staf frontdesk dengan kurir?
   * *Catatan Lapangan*: `[ ............................................................ ]`
8. **Prosedur Penagihan Tunggakan SPP**:
   * *Pertanyaan*: Kapan tanggal jatuh tempo pembayaran SPP setiap bulannya? Bagaimana alur penagihan tunggakan saat ini: apakah murid ditegur langsung saat masuk kelas, atau staf frontdesk mencari nomor telepon di buku A4 lalu mengirim pesan WhatsApp satu per satu?
   * *Catatan Lapangan*: `[ ............................................................ ]`

---

## 🔹 MODUL 5: KESIAPAN PERANGKAT KOMPUTASI DAN KOMITMEN PENGUJIAN LAPANGAN (*PROTOTIPE VS PROYEK*)
*Fokus: Mengukur kesiapan perangkat keras di cabang, jaringan internet, serta kesediaan mitra untuk terlibat dalam pengujian prototipe operasional.*

### 5.1 Observasi dan Pernyataan Kondisi Berjalan (*As-Is*)
Ariel awalnya mengusulkan Tugas Akhir berbentuk Proyek, namun Bu Ayu menyarankan untuk menaikkan level penelitian menjadi Prototipe jika mitra bersedia melakukan pengujian dengan pengguna riil (*real user*). Kesiapan ini bergantung pada fasilitas komputer di meja frontdesk cabang serta komitmen waktu manajemen dalam mendampingi uji coba.

### 5.2 Daftar Pertanyaan Validasi Lapangan
1. **Ketersediaan Perangkat Keras di Meja Frontdesk**:
   * *Pertanyaan*: Perangkat komputasi apa saja yang saat ini tersedia dan beroperasi di meja frontdesk masing-masing cabang? Apakah seluruh delapan cabang sudah memiliki komputer desktop atau laptop kerja, ataukah operasional selama ini bertumpu pada telepon genggam pribadi staf?
   * *Catatan Lapangan*: `[ ............................................................ ]`
2. **Kondisi dan Kestabilan Koneksi Internet Cabang**:
   * *Pertanyaan*: Apakah seluruh delapan cabang telah terpasang jaringan internet Wi-Fi tetap yang stabil untuk mengakses aplikasi sistem informasi berbasis web secara bersamaan (*real-time*)?
   * *Catatan Lapangan*: `[ ............................................................ ]`
3. **Kesiapan Alokasi Infrastruktur Server Yayasan**:
   * *Pertanyaan*: Apakah pihak yayasan atau pimpinan bersedia menyediakan anggaran sewa komputasi awan (*cloud server hosting*) dan nama domain resmi agar sistem prototipe ini dapat diakses secara daring oleh delapan cabang?
   * *Catatan Lapangan*: `[ ............................................................ ]`
4. **Komitmen Waktu Pengujian Pengguna Riil (*User Acceptance Testing*)**:
   * *Pertanyaan*: Apakah staf frontdesk dari perwakilan cabang dan staf manajemen bersedia meluangkan waktu untuk mengikuti sesi pelatihan penggunaan serta simulasi pengujian sistem (*UAT*) bersama peneliti sebelum naskah skripsi diujikan pada sidang sarjana?
   * *Catatan Lapangan*: `[ ............................................................ ]`

---

## 📋 DAFTAR BUKTI FISIK DAN DOKUMEN YANG WAJIB DIAMBIL / DIFOTO
Sebelum mengakhiri sesi wawancara dan observasi, pastikan Anda meminta izin untuk memotret atau mengumpulkan berkas pendukung berikut sebagai lampiran bukti empiris naskah Tugas Akhir:

1. [ ] **Halaman Buku Besar Pendaftaran A4**: Foto sampel halaman pendaftaran siswa baru (nama dan identitas sensitif disamarkan).
2. [ ] **Halaman Buku Catatan Iuran / SPP A4**: Foto sampel kolom rekapan pembayaran SPP bulanan di cabang.
3. [ ] **Lembar Kuitansi Fisik**: Foto blanko kuitansi pembayaran manual yang selama ini diserahkan kepada wali murid.
4. [ ] **Buku Absensi Kehadiran Tentor**: Foto buku presensi tentor di cabang yang memuat jam masuk dan tanda tangan mengajar.
5. [ ] **Brosur / Lembaran Daftar Tarif Resmi**: Dokumen cetak tarif pendaftaran, SPP per jenjang, dan paket khusus.
6. [ ] **Sampel Berkas Rekapan Excel Manajemen**: Salinan berkas file Excel rekapitulasi keuangan mingguan yang selama ini digunakan oleh manajemen pusat (cukup format kolom dan baris dummy).
7. [ ] **Foto Tata Letak Meja Frontdesk**: Foto fisik meja operasional frontdesk cabang untuk memperlihatkan ada atau tidaknya komputer kerja.
