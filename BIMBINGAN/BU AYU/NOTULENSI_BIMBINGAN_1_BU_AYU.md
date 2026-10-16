# NOTULENSI BIMBINGAN TUGAS AKHIR KE-1
**Dosen Pembimbing 2: Ibu Sri Rahayu Natasia, S.Kom., M.Si., M.Sc.**

---

### Informasi Pelaksanaan Bimbingan
* **Hari, Tanggal**: Kamis, 15 Oktober 2026
* **Waktu**: Pukul 14.30 – 15.45 WITA (Durasi Audio: 72 Menit 48 Detik)
* **Tempat**: Ruang Dosen Sistem Informasi, Institut Teknologi Kalimantan (ITK)
* **Dosen Pembimbing 2**: Ibu Sri Rahayu Natasia, S.Kom., M.Si., M.Sc. (Bu Ayu)
* **Mahasiswa**: Ariel (NIM. 10221074)
* **Topik Tugas Akhir**: Rancang Bangun Sistem Informasi Manajemen Operasional Bimbingan Belajar Artha Balikpapan
* **File Sumber Audio**: [`BIMBINGAN KE-1 (Bu Ayu).m4a`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/BIMBINGAN/BU%20AYU/BIMBINGAN%20KE-1%20(Bu%20Ayu).m4a)
* **File Transkrip Lengkap**: [`BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt`](file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/BIMBINGAN/BU%20AYU/BIMBINGAN%20KE-1%20(Bu%20Ayu)_WITH_TIMESTAMPS.txt)

---

## 📌 RINGKASAN EKSEKUTIF HASIL BIMBINGAN

Pertemuan bimbingan perdana bersama Bu Ayu berfokus pada pendalaman logika latar belakang, ketajaman rumusan masalah dan tujuan, justifikasi ilmiah pemilihan metodologi pengembangan perangkat lunak, evaluasi beban kerja operasional validasi pembayaran, serta penentuan klasifikasi naskah Tugas Akhir antara format Proyek atau Prototipe.

Bu Ayu memberikan arahan mendasar agar penulisan naskah tidak sekadar memindahkan alur manual ke sistem digital, melainkan harus mempertimbangkan budaya kerja mitra, risiko operasional baru yang mungkin timbul, serta kejelasan tolok ukur ketercapaian tujuan tugas akhir pada saat seminar dan sidang.

---

## 📋 NOTULENSI RINCI PER TEMA PEMBAHASAN

### 1. Pembahasan Latar Belakang dan Urgensi Masalah (Menit 00:00 – 15:00)
* **Pemaparan Mahasiswa**:
  Mahasiswa memaparkan kondisi empiris Bimbel Artha yang memiliki delapan cabang aktif di Kota Balikpapan. Seluruh proses pendaftaran dan SPP masih dicatat pada buku besar kertas dan direkap ulang ke Excel. Setiap pekan manajemen mengadakan rapat evaluasi keuangan, di mana pimpinan harus memvalidasi data rekapitulasi buku dan Excel dengan catatan mutasi bank di ponsel secara manual. Akibatnya, pernah terjadi selisih pencatatan (*miss* pembayaran) dan penerimaan yang terlewat.
* **Tanggapan dan Arahan Bu Ayu**:
  1. *Eksplorasi Nilai Kerugian atau Frekuensi Miss*:
     Bu Ayu menyarankan agar urgensi masalah diperkuat dengan data frekuensi terjadinya kesalahan atau estimasi kerugian finansial yang dialami mitra akibat sistem manual. Jika terdapat angka nominal selisih atau frekuensi kejadian rutin per bulan, hal tersebut akan menjadi dasar pembenaran yang sangat kuat (*urgent*) mengapa sistem informasi mutlak dibutuhkan.
  2. *Fokus pada Akar Masalah Utama*:
     Mahasiswa diingatkan agar tidak terlalu berambisi mencakup semua pihak (seperti membuat modul portal khusus siswa atau wali murid) di awal pengerjaan. Fokus utama penelitian harus diarahkan untuk menyelesaikan permasalahan inti operasional di tingkat staf administrasi cabang dan manajemen pusat.
  3. *Validasi Alur Pendaftaran Fisik*:
     Bu Ayu mengonfirmasi alasan mengapa pendaftaran tidak dilakukan mandiri secara daring oleh wali murid. Mahasiswa menjelaskan bahwa pendaftaran di Artha mensyaratkan kehadiran fisik karena ada pembayaran biaya pendaftaran awal, penyerahan buku modul cetak, serta verifikasi kelas. Bu Ayu menilai batasan peran ini sudah tepat dan dapat diterima.

---

### 2. Budaya Kerja Mitra dan Mitigasi Risiko Sistem (Menit 15:00 – 33:00)
* **Analisis Budaya Kerja Lembaga**:
  Bimbel Artha telah beroperasi hampir tiga puluh tahun dengan budaya kerja kekeluargaan. Hubungan antara pimpinan, staf cabang, dan tentor didasari oleh rasa saling percaya yang tinggi.
* **Arahan Kritis Bu Ayu terkait Otomasi dan Fleksibilitas**:
  1. *Bahaya Sistem yang Terlalu Kaku (Saklek)*:
     Bu Ayu mengingatkan bahwa sistem yang terlalu banyak aturan penguncian otomatis (*strict locking*) justru berisiko ditolak oleh pengguna jika bertentangan dengan budaya kerja mitra. Contohnya pada modul penjadwalan tentor, jika sistem otomatis mengunci nama tentor yang memiliki jam mengajar berdekatan antar-cabang, hal tersebut dapat memicu keluhan tentor yang merasa jam mengajarnya dipotong sepihak.
  2. *Aturan Kontrol Sistem yang Seimbang*:
     Aturan pembatasan di sistem harus didiskusikan secara mendalam dengan manajemen lembaga. Sistem sebaiknya memberikan peringatan dini (*warning*) atau rekomendasi, bukan langsung mengunci secara mutlak, sehingga pimpinan tetap memiliki ruang diskresi manajerial.
  3. *Standarisasi Tutup Buku Harian (Cut-Off Time)*:
     Bu Ayu menyarankan agar sistem memiliki mekanisme kontrol waktu transaksi, seperti penutupan transaksi harian pada jam tertentu layaknya sistem perbankan. Mekanisme ini memastikan data penerimaan harian selesai direkonsiliasi dan diaudit sebelum operasional hari berikutnya dimulai.
  4. *Pencatatan Kondisi Khusus dan Diskon*:
     Skema potongan harga (diskon kakak-beradik, diskon tahunan, atau keringanan bagi keluarga kurang mampu) harus memiliki modul pencatatan tersendiri di sistem. Hal ini penting agar saat dilakukan audit keuangan, selisih antara tarif normal dan uang yang masuk ke kas tidak dianggap sebagai kebocoran dana.

---

### 3. Evaluasi Rumusan Masalah dan Tujuan Penelitian (Menit 47:30 – 52:00)
* **Kritik Bu Ayu terhadap Draf BAB 1**:
  Bu Ayu menyoroti bagian Rumusan Masalah dan Tujuan yang saat ini dipecah menjadi lima butir pertanyaan yang sangat detail per modul teknis (modul pendaftaran, modul kasir/SPP, modul jadwal tentor, dasbor monitoring, dan notifikasi).
* **Catatan Koreksi Fundamental**:
  1. *Keterikatan Kaku pada Pengujian Akhir*:
     Rumusan masalah akan dijawab secara langsung oleh tujuan penelitian. Jika tujuan penelitian dipatok ke dalam lima poin teknis yang sangat spesifik, maka pada saat sidang Tugas Akhir kelima poin tersebut harus dibuktikan tercapai secara mutlak.
  2. *Potensi Perubahan Kebutuhan di Lapangan*:
     Pada pengembangan perangkat lunak berbasis kebutuhan dinamis, fitur sistem berpotensi mengalami penyesuaian seiring intensitas komunikasi bersama mitra. Jika narasi tujuan ditulis terlalu kaku sejak awal, perubahan fitur di tengah jalan akan menimbulkan ketidaksesuaian laporan.
  3. *Rekomendasi Perbaikan Narasi*:
     Bu Ayu menyarankan agar rumusan masalah dan tujuan ditulis secara lebih utuh, terintegrasi, dan berorientasi pada pencapaian kapabilitas tata kelola multicabang, bukan sekadar memecah daftar modul fitur.
  4. *Kesesuaian Kata Kerja dengan Paradigma Pengembangan*:
     Penggunaan kata kerja seperti "merancang" dan "membangun" harus diselaraskan dengan metode yang dipilih. Pada paradigma *agile*, porsi perancangan formal tidak dibuat terpisah secara masif di awal, melainkan berjalan secara terpadu (*iterative*) bersamaan dengan implementasi dan pengujian modul.

---

### 4. Justifikasi Ilmiah Pemilihan Metodologi (Menit 40:00 – 47:15 & 55:00 – 57:00)
* **Kritik terhadap Argumen "Solo Developer"**:
  Bu Ayu menegaskan bahwa alasan *"saya memilih Personal Extreme Programming (PxP) karena Tugas Akhir ini dikerjakan secara individu"* merupakan jawaban yang kurang tepat dan sangat klise. Dosen penguji di ruang sidang pasti akan mendebat argumen tersebut.
* **Poin Justifikasi Ilmiah yang Harus Dibangun Mahasiswa**:
  1. *Perbandingan Multi-Aspek*:
     Pemilihan metode harus didasarkan pada perbandingan objektif dari beberapa aspek utama, meliputi karakteristik kebutuhan sistem (dinamis vs terdefinisi pasti), tingkat keterlibatan *stakeholder*, ketersediaan waktu pengerjaan, serta kebutuhan dokumentasi formal.
  2. *Peran dan Keterlibatan Mitra*:
     Jelaskan posisi perwakilan mitra (misalnya peran Mas Radit atau pimpinan Artha). Apakah mitra bertindak sebagai *on-site customer* yang bersedia memberikan evaluasi rutin di setiap iterasi, atau hanya diwawancarai di awal dan akhir proyek. Tingkat keaktifan mitra ini menjadi penentu utama kelayakan metode *agile*.
  3. *Komparasi terhadap Metode Lain*:
     Mahasiswa harus mampu membedah mengapa tidak menggunakan metode lain:
     * Mengapa bukan *Waterfall*? Karena proses bisnis Artha sedang bertransformasi dan membutuhkan adaptasi berkala, sehingga pendekatan linier satu arah sangat berisiko gagal.
     * Mengapa bukan *Scrum*? Karena seremoni formal Scrum (Scrum Master, Product Owner, Sprint Review tim) membutuhkan struktur tim multi-orang.
     * Mengapa bukan *Prototyping* murni? Karena *prototyping* sering kali hanya menghasilkan maket evaluasi visual sementara (*throwaway prototype*), sedangkan PxP menghasilkan modul fungsional yang siap dioperasikan.

---

### 5. Beban Kerja Validasi Pembayaran dan Risiko Pemalsuan Bukti (Menit 18:25 – 21:50)
* **Sorotan terhadap Pembayaran Transfer Manual Tanpa Payment Gateway**:
  Mahasiswa merencanakan sistem pembayaran transfer bank diverifikasi secara manual oleh admin/pimpinan berdasarkan foto bukti transfer yang diunggah.
* **Peringatan Penting dari Bu Ayu**:
  1. *Beban Kerja Operasional (Workload Effort)*:
     Delapan cabang dengan rata-rata ratusan siswa per cabang menghasilkan ribuan transaksi SPP setiap bulan. Jika pimpinan pusat atau admin harus memvalidasi foto bukti transfer dan mencocokkan mutasi rekening satu per satu secara manual, hal ini akan menciptakan beban kerja baru yang sangat melelahkan dan tetap berpotensi menimbulkan kesalahan manusia (*human error*).
  2. *Risiko Rekayasa Bukti Transfer Berbasis AI / Grafis*:
     Saat ini teknologi kecerdasan buatan dan manipulasi gambar sangat mudah digunakan untuk memalsukan bukti transfer (mengubah nama pengirim, nominal, atau tanggal transfer bulan sebelumnya). Mengandalkan verifikasi visual bukti transfer sangat berisiko bagi keamanan kas mitra.
  3. *Saran Tindak Lanjut Teknis*:
     Bu Ayu menyarankan agar mahasiswa meneliti lebih lanjut mengenai skema *payment gateway* (termasuk biaya langganan dan integrasinya) sebagai alternatif solusi yang dapat ditawarkan ke mitra. Jika tetap menggunakan mekanisme verifikasi transfer manual, alur rekonsiliasi dan pembagian tugas verifikasi antara staf cabang dan pusat harus dirancang secara sangat matang dan realistis.

---

### 6. Pertimbangan Naskah Tugas Akhir: Proyek vs Prototipe (Menit 22:00 – 23:40 & 54:00 – 57:40)
* **Perbedaan Kategori Proyek vs Prototipe**:
  * *Proyek*: Sistem dibangun berdasarkan spesifikasi kebutuhan internal mitra, dengan pengujian fungsionalitas internal.
  * *Prototipe*: Sistem diwajibkan untuk diuji coba langsung oleh pengguna akhir di lingkungan kerja nyata (*real user testing*) dan siap untuk dioperasikan secara langsung oleh mitra.
* **Pandangan dan Keputusan Pembimbing**:
  * Bu Ayu secara pribadi lebih mendukung jika naskah Tugas Akhir ini dapat diangkat ke kategori **Prototipe**, karena dampaknya nyata dan sistem langsung digunakan oleh Bimbel Artha.
  * Namun, untuk saat ini mahasiswa disarankan tetap **mengikuti arahan Pak Arif (Dosen Pembimbing 1)** dengan menggunakan format naskah Proyek terlebih dahulu.
  * Keputusan final mengenai kenaikan status menjadi Prototipe akan dimusyawarahkan bersama oleh Dosen Pembimbing dan Dosen Penguji pada saat Seminar Proposal (Sempro), dengan melihat kesiapan perangkat lunak dan komitmen mitra.

---

## 🎯 DAFTAR TINDAK LANJUT (*ACTION ITEMS*) MAHASISWA

| No | Rencana Tindak Lanjut | Bagian Naskah Terkait | Prioritas |
| :---: | :--- | :--- | :---: |
| 1 | Menyederhanakan dan mengintegrasikan 5 poin Rumusan Masalah dan Tujuan agar tidak terlalu kaku per modul teknis. | BAB 1 (Subbab 1.2 & 1.3) | **Tinggi** |
| 2 | Menambahkan data empiris mengenai frekuensi kesalahan rekap manual atau potensi kerugian finansial pada latar belakang. | BAB 1 (Subbab 1.1) | **Sedang** |
| 3 | Memperkuat argumen pemilihan PxP dengan analisis komparasi multi-aspek (Waterfall, Scrum, Prototyping) dan peran mitra. | BAB 1 (Subbab 1.6) & BAB 2 | **Tinggi** |
| 4 | Merancang alur pembagian kerja rekonsiliasi mutasi bank yang realistis agar tidak membebani manajemen secara manual. | Desain Sistem (BAB 3) | **Tinggi** |
| 5 | Mengonfirmasi ulang aturan penjadwalan tentor dan batas kapasitas kelas ke pihak manajemen Artha agar sistem tidak terlalu saklek. | Kebutuhan Pengguna (BAB 3) | **Sedang** |
| 6 | Memulai penyusunan kajian teori dan penelitian terdahulu (*state of the art*) pada BAB 2 sesuai arahan pembimbing. | BAB 2 (Tinjauan Pustaka) | **Tinggi** |

---

> [!NOTE]
> Notulensi ini disusun secara komprehensif berdasarkan rekaman percakapan aktual dan berkas transkrip bimbingan untuk digunakan sebagai pedoman revisi berkas proposal skripsi serta bahan diskusi pada sesi bimbingan berikutnya.
