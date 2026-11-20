# Audit kesesuaian use case dan basis data ARTHA

Pemeriksaan dilakukan pada 25 Oktober 2026 terhadap seluruh isi dokumen use case dan skema basis data, dengan membandingkannya terhadap Bab 1, bukti wawancara yang relevan, dan penjelasan terbaru pengguna. Penilaian ini merupakan pemeriksaan rancangan, bukan hasil eksekusi aplikasi atau pengesahan skema sebagai basis data produksi.

## 1. Kesimpulan utama

Kedua dokumen mempunyai dasar yang relevan dan dapat digunakan sebagai bahan revisi Bab 3. Namun, belum seluruh isinya konsisten atau cukup lengkap untuk dijadikan rancangan final, terutama pada WhatsApp, alur pembayaran, pencocokan penerimaan, aturan tarif, dan kesinambungan antara use case serta tabel.

Kerangka yang dapat dipertahankan meliputi dua peran pengguna, pembatasan cabang, pengelolaan siswa, pemisahan ruang dan kelas, keanggotaan kelas, jadwal tentor, tagihan, serta pembayaran. Jumlah tabel atau jumlah use case tidak ditetapkan sebagai sasaran yang harus dipertahankan apabila kebutuhan akhirnya memerlukan penyesuaian.

### 1.1 Dasar keputusan yang dibedakan

| Kedudukan | Isi | Perlakuan dalam revisi |
| :--- | :--- | :--- |
| Keputusan terbaru pengguna | WhatsApp dibuka melalui tombol, nomor dan pesan disiapkan, admin mengirim pesan | Menjadi acuan revisi skenario dan rancangan pencatatan komunikasi |
| Keputusan terbaru pengguna | Kelas hampir penuh diberi peringatan; kelas penuh menolak penambahan; tempat tersedia setelah siswa keluar | Menjadi acuan revisi kapasitas serta keanggotaan |
| Isi Bab 1 yang masih tertulis | Transfer diverifikasi manual oleh Admin Cabang | Tidak disebut salah hanya karena berbeda dengan usulan baru |
| Usulan pembayaran yang dibahas | Admin mengajukan bukti; Super Admin memeriksa dana masuk dan mengambil keputusan | Ditetapkan sebagai usulan sampai kewenangan serta akses rekening dikonfirmasi; Bab 1 perlu diubah bila usulan dipilih |
| Fitur tambahan dalam dokumen lama | Antrean otomatis, WhatsApp terjadwal, kartu anggota, serta integrasi landing page | Dipisahkan dari kebutuhan inti dan ditetapkan statusnya sebelum dimasukkan ke Bab 3 |

Tidak semua perbedaan berarti dokumen lama salah pada saat dibuat. Sebagian merupakan perubahan kebutuhan, sedangkan sebagian lainnya merupakan ketidaksinkronan atau kelemahan desain yang dapat ditunjukkan langsung dari berkas.

## 2. Kesesuaian dengan rumusan masalah Bab 1

| Rumusan masalah | Use case yang relevan | Kelompok data yang relevan | Penilaian |
| :--- | :--- | :--- | :--- |
| RM 1: integrasi pendaftaran, SPP, dan jadwal | UC-02 sampai UC-06 serta dukungan UC-00/UC-11/UC-12 | Siswa, kelas, keanggotaan, jadwal, tarif, tagihan, dan pembayaran | Relevan; rincian tarif, kapasitas, dan verifikasi perlu diperbaiki |
| RM 2: dasbor pusat dan dukungan pencocokan dengan mutasi bank | UC-07, UC-08, dan pemantauan jadwal UC-09 | Transaksi, data cabang, serta rancangan pencocokan penerimaan | Belum cukup; perbandingan tagihan dengan pembayaran tidak sama dengan pencocokan bank |
| RM 3: kesesuaian prototipe melalui pengujian dan UAT | Seluruh kebutuhan yang diuji, bukan satu fitur operasional baru | Bukti kebutuhan, kasus uji, tugas UAT, serta hasil evaluasi | Perlu matriks keterlacakan; tidak harus dibuat tabel operasional bernama UAT |

Dokumen basis data masih menyebut Rumusan Masalah 4 dan memakai penomoran masalah dari rancangan lama. Bab 1 saat ini mempunyai tiga rumusan masalah, sehingga pemetaan tersebut harus diperbarui.

## 3. Temuan yang sangat penting

### F01. WhatsApp otomatis tidak sesuai dengan keputusan terbaru

**Lokasi:** use case UC-04 langkah kesepuluh, baris 389; basis data `wa_logs`, baris 757 sampai 771. **Prioritas:** sangat penting.

Dokumen lama menjelaskan pengiriman otomatis H-7, H-1, dan H+3 menggunakan penjadwal. Keputusan terbaru pengguna adalah tombol yang membuka WhatsApp dengan pesan terisi setelah admin melihat tagihan lewat jatuh tempo.

**Perbaikan:** ubah skenario menjadi memilih tagihan, memeriksa pratinjau pesan dan nomor, membuka tautan, lalu mengirim melalui WhatsApp. Jika aktivitas dicatat, gunakan nama seperti `reminder_actions` atau makna pencatatan lain yang sesuai, dengan pengaju tindakan serta waktu pembukaan tautan; jangan menyatakan sistem mengetahui status terkirim atau diterima.

### F02. Alur transfer perlu memilih satu pembagian kewenangan

**Lokasi:** use case UC-04, baris 365 sampai 395; Bab 1 batasan ketiga; basis data `payments`, baris 733 sampai 749. **Prioritas:** sangat penting.

Skenario saat ini menempatkan Admin Cabang sebagai pengunggah sekaligus pemeriksa transfer, lalu langsung melunasi tagihan. Hal tersebut sesuai redaksi batasan Bab 1 lama, tetapi belum mewakili usulan pengajuan oleh admin dan keputusan Super Admin yang dibahas kemudian.

**Perbaikan:** bila usulan pemeriksaan pusat dipilih, pisahkan pengajuan bukti, antrean pemeriksaan, pencocokan dana masuk, dan keputusan. Samakan pihak berwenang pada Bab 1, use case, matriks hak akses, rancangan layar, kolom pemeriksa, dan pengujian; jangan hanya mengubah diagram Bab 3.

### F03. Data pembayaran belum cukup untuk pengembalian dan pengajuan ulang

**Lokasi:** ERD `payments`, baris 196 sampai 209; kamus data baris 733 sampai 749. **Prioritas:** sangat penting.

Kolom `verified_by_user_id` dan `verified_at` yang boleh kosong sudah memberi penanda dasar belum/sudah diperiksa. Namun, skema belum menjelaskan siapa yang mengajukan, status dikembalikan, alasan, versi bukti yang diperbaiki, serta riwayat keputusan.

**Perbaikan:** tambahkan pencatatan pengaju, waktu pengajuan, status pemeriksaan, dan alasan yang dapat ditelusuri. Riwayat keputusan dapat diletakkan pada tabel pemeriksaan terpisah atau mekanisme audit yang setara; jangan menimpa bukti dan keputusan lama tanpa riwayat.

### F04. Pengajuan bukti belum otomatis merupakan pelunasan

**Lokasi:** use case UC-04 pascakondisi serta langkah kedelapan, baris 374 dan 387. **Prioritas:** sangat penting.

Pascakondisi selalu menyatakan tagihan menjadi `paid`, meskipun nominal, kecocokan dana, dan kemungkinan pembayaran sebagian belum dibedakan. Unggah bukti transfer merupakan pengajuan pemeriksaan dan tidak sendirinya membuktikan dana diterima.

**Perbaikan:** hitung sisa tagihan dari pembayaran yang diterima atau disetujui menurut prosedur kanalnya. Bukti pengajuan sementara dibedakan dari kuitansi pembayaran terkonfirmasi; tentukan pula kapan nomor kuitansi resmi diterbitkan dan bagaimana transaksi yang dikoreksi ditelusuri.

### F05. Satu pembayaran untuk beberapa periode belum didukung model yang sama

**Lokasi:** UC-04 langkah ketiga, baris 380; `payments.bill_id`, baris 740. **Prioritas:** sangat penting.

Use case memperbolehkan pemilihan satu atau lebih bulan dalam satu proses, sedangkan satu baris `payments` hanya merujuk satu `bill_id`. Skema belum menjelaskan pembagian nominal, bukti yang sama, dan hubungan satu kuitansi dengan beberapa tagihan.

**Perbaikan:** pilih salah satu kebijakan yang konsisten. Jika satu penerimaan boleh melunasi beberapa tagihan, gunakan penerimaan sebagai induk dan rincian alokasi per tagihan; jika satu transaksi dibatasi satu tagihan, ubah skenario serta aturan kuitansi dan jelaskan batasnya.

### F06. Rekap tagihan dan pembayaran belum merupakan rekonsiliasi bank

**Lokasi:** UC-08 baris 466 sampai 490; `revenue_validations`, baris 775 sampai 790. **Prioritas:** sangat penting.

`expected_revenue` adalah jumlah tagihan, sedangkan `actual_revenue` adalah pembayaran. Selisih keduanya dapat menunjukkan tunggakan, tetapi bukan otomatis selisih antara catatan penerimaan dan mutasi bank; nominal saldo bank yang cocok serta transaksi sumber belum dimodelkan secara jelas.

**Perbaikan:** pisahkan tagihan belum lunas, penerimaan terkonfirmasi, kas tunai yang diserahkan, dan dana yang sudah dicocokkan dengan referensi bank. Tambahkan rujukan transaksi, tanggal dan nominal dana masuk, status pencocokan, serta pemeriksanya sesuai lingkup yang dipilih; tidak perlu membangun seluruh sistem akuntansi jika tujuan hanya pencocokan penerimaan.

### F07. Setoran tunai belum mempunyai hubungan data yang memadai

**Lokasi:** UC-06 dan UC-08; kamus data yang hanya memuat `payments` serta `revenue_validations` untuk proses penerimaan. **Prioritas:** sangat penting.

Penerimaan uang dari wali, penyerahan uang cabang kepada pusat, dan penyetoran ke bank merupakan kejadian berbeda. Dokumen belum menunjukkan daftar pembayaran yang termasuk dalam satu setoran, penyerah, penerima, serta bukti penyerahannya.

**Perbaikan:** bila pelacakan setoran termasuk lingkup penelitian, sediakan objek setoran dan rincian pembayaran asal atau mekanisme setara. Setoran tidak dihitung sebagai pendapatan siswa yang baru, dan uang tunai yang belum masuk bank tidak otomatis dinyatakan sebagai selisih yang salah.

### F08. Tarif belum dapat membedakan variasi cabang dan sesi

**Lokasi:** `fee_tariffs`, baris 525 sampai 552; Bab 1 latar belakang paragraf keempat. **Prioritas:** sangat penting.

Tarif saat ini dipilih menurut tahun ajaran, program, jenjang, dan tingkat kelas. Padahal, Bab 1 serta wawancara menjelaskan variasi terkait cabang atau waktu belajar; belum ada cara yang jelas untuk memilih dua tarif berbeda bagi kombinasi jenjang yang sama.

**Perbaikan:** petakan faktor tarif yang benar-benar berlaku, kemudian tambahkan pembeda cabang, sesi, atau paket yang diperlukan beserta aturan prioritas tarif. Simpan nilai yang dikenakan pada tagihan agar perubahan tarif tidak mengubah transaksi historis.

### F09. Diskon Rp200.000 tidak boleh dipatok sebagai potongan setiap SPP

**Lokasi:** UC-02 langkah kelima, baris 309; basis data baris 326 dan `students.discount_amount`. **Prioritas:** sangat penting.

Transkrip wawancara ketiga memang menyebut potongan Rp200.000 pada 48:18 sampai 48:24, tetapi konteks dan penerapannya perlu dipastikan. Transkrip frontdesk pada 19:28 sampai 19:30 menyebut potongan Rp10.000 per anak, sehingga sumber yang tersedia belum membenarkan satu nominal tetap untuk semua tagihan di seluruh cabang.

**Perbaikan:** tetapkan jenis potongan, dasar nominal, pihak yang berhak, cakupan cabang, periode berlaku, dan apakah potongan sekali atau berulang. Simpan potongan aktual serta alasan pada tagihan; jangan menjadikan satu angka dalam transkrip sebagai aturan global di kode.

### F10. Biaya paket diperlakukan sebagai SPP bulanan pada contoh data

**Lokasi:** contoh `fee_tariffs`, baris 551; `bills.bill_type`, baris 721. **Prioritas:** sangat penting.

Contoh data menyimpan paket SMA kelas dua belas Rp2.250.000 sebagai `spp_monthly`. Bab 1 menjelaskan pembayaran paket semester atau tahunan untuk jenjang tertentu, sehingga penandaan bulanan berisiko menimbulkan pengulangan tagihan yang tidak sesuai.

**Perbaikan:** bedakan program belajar dari jenis dan periode pembayarannya. Tentukan kategori serta periode paket berdasarkan kebijakan nyata, kemudian uji bahwa tagihan paket tidak diterbitkan ulang setiap bulan jika kewajibannya memang sekali per semester atau tahun.

### F11. Empat tabel yang dihapus masih digunakan use case

**Lokasi:** UC-02, UC-03, UC-04, UC-11, dan matriks baris 586 sampai 606; peta migrasi basis data baris 811 sampai 820. **Prioritas:** sangat penting.

Matriks use case merujuk dua puluh nama tabel, sedangkan ERD memuat enam belas. Empat nama yang tidak lagi ada adalah `learning_programs`, `capacity_rules`, `discount_rules`, dan `wa_templates`.

**Perbaikan:** pilih apakah aturan tetap berada di kode, dikembalikan ke penyimpanan pengaturan, atau diwakili kolom yang sudah ada. Perbarui seluruh referensi tabel dan matriks bersamaan; klaim integritas seratus persen tidak dipertahankan sebelum pemeriksaan ulang.

### F12. Pengaturan oleh Super Admin bertentangan dengan konfigurasi di kode

**Lokasi:** UC-11 baris 539 sampai 560; alasan penghapusan empat tabel, baris 302 sampai 334; checklist fitur baris 838 sampai 839. **Prioritas:** sangat penting.

UC-11 menjanjikan perubahan diskon, kapasitas, dan templat melalui dasbor tanpa perubahan kode. Dokumen basis data justru menempatkan beberapa pengaturan tersebut di kelas layanan atau berkas konfigurasi yang diubah melalui deployment.

**Perbaikan:** tetapkan siapa yang benar-benar boleh mengubah setiap parameter dan melalui sarana apa. Jika Super Admin perlu mengubahnya melalui aplikasi, sediakan penyimpanan dan mekanisme pengaturan yang sesuai; menghapus tabel bukan otomatis penyederhanaan yang tetap mempertahankan semua fungsi.

## 4. Temuan penting pada kelas, jadwal, dan data

### F13. Kelas penuh sudah sesuai, tetapi proses siswa keluar belum lengkap

**Lokasi:** UC-03; `classes`, baris 638 sampai 660; `class_enrollments`, baris 687 sampai 704. **Prioritas:** sangat penting.

Penolakan penambahan saat kelas penuh sudah sesuai keputusan terbaru pengguna. Namun, perubahan peserta menjadi keluar atau selesai belum dijelaskan sebagai alur yang memperbarui jumlah aktif, status keterisian, dan waktu keanggotaan berakhir.

**Perbaikan:** tambahkan alur mengakhiri keanggotaan kelas, menyimpan tanggal serta alasan, lalu menghitung ulang kapasitas. `current_students` dapat dipertahankan sebagai penghitung tersimpan jika pembaruannya konsisten, atau dihitung dari keanggotaan aktif; jangan menghapus siswa beserta riwayatnya hanya untuk membuka tempat.

### F14. Daftar tunggu dan promosi otomatis masih merupakan fitur tambahan

**Lokasi:** UC-03C; basis data baris 409 sampai 411 serta 704. **Prioritas:** penting.

Keputusan pengguna menetapkan tempat terbuka setelah siswa keluar, tetapi belum menetapkan antrean otomatis atau pengiriman WhatsApp ketika slot tersedia. Fitur tersebut dapat berguna, tetapi tidak otomatis menjadi kebutuhan yang telah disepakati.

**Perbaikan:** tandai daftar tunggu sebagai pilihan pengembangan atau kebutuhan yang memerlukan dasar mitra. Jika digunakan, jelaskan urutan, konfirmasi kesediaan siswa, kapan `enrolled_at` diisi, dan larangan mengaktifkan peserta sebelum penempatan disetujui.

### F15. Angka hampir penuh dan beban tentor belum mempunyai dasar yang jelas

**Lokasi:** UC-03 baris 337 sampai 339; UC-09 baris 509 sampai 512. **Prioritas:** penting.

Dokumen menggunakan delapan puluh persen sebagai ambang hampir penuh dan lebih dari delapan kelas per minggu sebagai beban berlebih. Angka tersebut belum ditunjukkan sebagai kebijakan mitra, sedangkan jumlah kelas juga tidak selalu sama dengan jumlah jam mengajar.

**Perbaikan:** tetapkan ambang kapasitas sebagai parameter yang disepakati dan tampilkan jumlah peserta beserta sisa tempat. Beban tentor dihitung dari durasi penugasan dan disajikan tanpa label normal atau berlebih sebelum kriteria penilaiannya ditetapkan.

### F16. Kapasitas perlu diperiksa saat penyimpanan dan terhadap ruang aktual

**Lokasi:** `classes.max_students`, `current_students`, `status`, serta `class_rooms.physical_capacity`. **Prioritas:** sangat penting.

Validasi saat pembuatan kelas belum cukup untuk mencegah dua permintaan mengisi satu tempat terakhir secara bersamaan. Kapasitas kelompok juga perlu diperiksa terhadap ruangan yang dipakai pada jadwal, termasuk ketika ruangan atau batas kapasitas diubah.

**Perbaikan:** tetapkan satu sumber hitungan peserta aktif dan gunakan transaksi dengan pemeriksaan yang tetap berlaku saat penyimpanan. Jika memakai MySQL InnoDB, penguncian baris kelas yang sesuai dapat menjadi bagian solusi; penguncian harus berada dalam transaksi dan diikuti seluruh jalur penambahan peserta, bukan sekadar menambahkan kata `FOR UPDATE` pada satu kueri.

### F17. Kueri benturan jadwal memerlukan batas konteks tambahan

**Lokasi:** basis data baris 681 sampai 683. **Prioritas:** penting.

Perbandingan `start_time < akhir_baru` dan `end_time > awal_baru` sudah merupakan dasar irisan waktu yang tepat. Namun, contoh kueri belum mengecualikan jadwal nonaktif, jadwal yang sedang diedit, serta periode atau tahun ajaran yang tidak berlaku.

**Perbaikan:** tambahkan pemeriksaan rentang berlakunya jadwal, status aktif, identitas yang diedit, dan urutan jam selesai sesudah jam mulai. Pemeriksaan tentor dilakukan lintas cabang tanpa membuka seluruh data cabang lain kepada Admin Cabang; kebutuhan jeda perjalanan hanya ditambahkan bila memang ditetapkan mitra.

### F18. Penugasan kelas, ruang, dan siswa perlu menjaga konsistensi cabang

**Lokasi:** relasi `students`, `classes`, `class_schedules`, dan `class_rooms`. **Prioritas:** penting.

Kunci asing ke masing-masing tabel belum dengan sendirinya memastikan sebuah kelas memakai ruangan dari cabang yang benar. Kebijakan siswa belajar lintas cabang juga belum dijelaskan, sehingga tidak boleh diasumsikan semua kombinasi yang mempunyai kunci asing sah selalu diperbolehkan.

**Perbaikan:** tulis aturan kecocokan cabang pada penempatan dan penjadwalan, kemudian terapkan pemeriksaan objek di peladen. Apabila lintas cabang diperbolehkan, modelkan kewenangan serta riwayatnya secara eksplisit, bukan membiarkan hubungan berubah tanpa aturan.

### F19. Riwayat penerimaan dapat berubah jika hanya mengikuti cabang siswa saat ini

**Lokasi:** `students.branch_id`, `bills.student_id`, dan `payments.bill_id`. **Prioritas:** penting.

Tagihan dan pembayaran belum mempunyai rujukan kepemilikan cabang pada waktu transaksi yang dijelaskan sebagai tetap. Jika cabang siswa diperbarui, laporan historis yang menghubungkan pembayaran melalui data siswa saat ini berisiko berpindah cabang.

**Perbaikan:** tentukan rujukan cabang transaksi yang tidak berubah, misalnya pada tagihan atau pendaftaran periode yang menjadi sumbernya. Hindari menambahkan kolom cabang ke semua tabel tanpa aturan; yang diperlukan adalah satu hubungan historis yang jelas serta dipakai konsisten pada laporan.

### F20. Status pembayaran dan keterlambatan perlu dibedakan

**Lokasi:** `bills.payment_status`, baris 726. **Prioritas:** penting.

Pilihan `unpaid`, `partial`, `paid`, dan `overdue` menggabungkan pelunasan dengan kondisi lewat waktu. Tagihan dapat sekaligus dibayar sebagian dan lewat jatuh tempo, sehingga satu nilai tersebut belum menjelaskan kedua kondisi secara utuh.

**Perbaikan:** simpan atau turunkan tingkat pelunasan dari jumlah pembayaran yang sah, lalu tentukan keterlambatan dari sisa tagihan serta tanggal jatuh tempo. Dasbor dapat menampilkan status belum lunas atau sebagian beserta penanda lewat jatuh tempo, tanpa kehilangan salah satunya.

### F21. Periode, duplikasi, dan nilai transaksi belum seluruhnya dibatasi

**Lokasi:** `academic_years`, `fee_tariffs`, `bills`, `payments`, dan `revenue_validations`. **Prioritas:** penting.

Kamus data belum menjelaskan seluruh aturan untuk mencegah tagihan periode yang sama terbit ganda, rentang tarif bertumpang tindih, nominal tidak sah, atau validasi periode cabang yang berulang. Pada `revenue_validations`, pemeriksa dan waktu pemeriksaan wajib terisi meskipun status awalnya `pending`.

**Perbaikan:** tetapkan kunci bisnis dan aturan nilai untuk setiap objek, kemudian pilih kombinasi kendala basis data serta validasi aplikasi yang sesuai. Pemeriksa dan waktu final dapat kosong sebelum keputusan, sementara pengaju atau pembuat data dicatat pada atribut yang berbeda.

### F22. Data TK dan jenis paket perlu definisi yang konsisten

**Lokasi:** formulir UC-02 baris 306; `grade_level` mencakup TK, tetapi `class_grade` dijelaskan sebagai satu sampai dua belas. **Prioritas:** penting.

Bab 1 mencakup layanan TK, sedangkan uraian formulir pendaftaran hanya menyebut SD, SMP, dan SMA. Model belum menjelaskan nilai tingkat kelas untuk TK dan hubungan program reguler, intensif, serta paket dengan periode pembayaran.

**Perbaikan:** samakan pilihan jenjang pada formulir dan kamus data, lalu definisikan tingkat kelas yang sesuai atau nilai kosong yang diizinkan untuk TK. Jangan menganggap paket pembayaran pasti merupakan program belajar yang berbeda apabila proses nyata tidak membedakannya demikian.

## 5. Temuan pemodelan dan konsistensi dokumen

### F23. Arah extend pada Mermaid berbeda dari PlantUML

**Lokasi:** blok Mermaid baris 107 sampai 124 dan PlantUML baris 209 sampai 226. **Prioritas:** penting.

Contoh Mermaid mengarahkan `UC02` ke `UC02B` dengan label extend. PlantUML mengarahkan hubungan dari `UC02B` ke `UC02`, sehingga dua diagram pada dokumen yang sama tidak mempunyai makna arah yang konsisten.

**Perbaikan:** arah extend dibuat dari kasus tambahan menuju kasus dasar yang diperluas. Include dibuat dari kasus utama menuju perilaku yang disertakan; penggunaan include tetap diperiksa apakah perilaku tersebut selalu dibutuhkan untuk tujuan kasus utama.

### F24. Beberapa tujuan pengguna dan langkah internal tercampur

**Lokasi:** UC-03, UC-04, serta UC-08 dan subkasusnya. **Prioritas:** penting.

Penempatan siswa dan penyusunan jadwal digabung dalam UC-03, sehingga pemeriksaan benturan seolah selalu dilakukan ketika menambah keanggotaan. Pembayaran yang bersifat menunggu pemeriksaan juga diperlakukan sebagai satu alur sinkron bersama penerbitan kuitansi final.

**Perbaikan:** bedakan tujuan penempatan siswa, pengelolaan jadwal, pengajuan transfer, dan pengambilan keputusan pemeriksaan. Tidak semua pemeriksaan formulir wajib menjadi use case tersendiri; pemeriksaan yang hanya langkah internal dapat dijelaskan pada skenario tanpa memperbanyak elips.

### F25. Autentikasi dan kebolehan akses harus konsisten dengan peran

**Lokasi:** deskripsi aktor baris 22 sampai 25; kamus `users`, baris 492 sampai 509; ERD relasi cabang dengan pengguna dan tentor. **Prioritas:** sangat penting.

Peran sudah tersedia pada kolom `role`, tetapi uraian juga menjadikan `branch_id = NULL` sebagai penanda pemberi hak Super Admin. Relasi ERD menyatakan satu cabang wajib untuk setiap pengguna atau tentor, sedangkan kolomnya justru dapat kosong.

**Perbaikan:** hak akses ditetapkan melalui peran yang sah dan kebijakan objek cabang, bukan hanya nilai kosong. Sesuaikan kardinalitas opsional, periksa kewenangan pada setiap permintaan, dan lengkapi alur keluar sistem yang belum dijelaskan meskipun UC-00 diberi nama login dan logout.

### F26. Jumlah dan klaim validasi belum konsisten dengan isi

**Lokasi:** header serta matriks akhir use case; ringkasan statistik basis data. **Prioritas:** penting.

Blok diagram use case memuat tiga belas subkasus berbeda, bukan sebelas seperti pada header. ERD memuat enam belas tabel dan dua puluh empat garis relasi, sedangkan matriks use case tetap merujuk dua puluh nama tabel; semua enam belas tabel ada dalam matriks, tetapi terdapat empat rujukan yang sudah dihapus dari skema.

**Perbaikan:** hitung ulang setelah fungsi disepakati dan samakan ERD, kamus data, serta matriks. Tanda centang 27 dari 27 fitur menunjukkan klaim cakupan dokumen, bukan bukti fitur sudah disetujui mitra, benar secara semantik, atau telah lulus pengujian.

### F27. Klaim fakta dan angka tidak boleh diambil dari asumsi rancangan

**Lokasi:** uraian tabel `mentors`, `class_schedules`, `revenue_validations`, serta UC-09. **Prioritas:** sangat penting.

Dokumen menyatakan lebih dari enam puluh tentor, pernah terjadi insiden tentor di dua cabang sekaligus, serta laporan mingguan sebagai fakta yang sudah pasti. Bukti yang diperiksa menunjukkan jumlah tentor berbeda antar cabang, jadwal dibedakan pada cabang yang diwawancarai, dan penerimaan harian dilaporkan setiap malam.

**Perbaikan:** kaitkan setiap fakta dengan informan, cabang, tanggal, dan penanda waktu. Informasi yang belum terkonfirmasi ditulis sebagai risiko atau kebutuhan pencegahan, sedangkan frasa “dampak fatal” diganti dengan fungsi serta konsekuensi yang proporsional dan dapat dijelaskan.

### F28. Fitur tambahan perlu dipisahkan dari kebutuhan inti

**Lokasi:** UC-03C, UC-05B, UC-07, UC-09, UC-10, serta dukungan QRIS. **Prioritas:** penting.

Antrean otomatis, kartu anggota, peta landing page, grafik yang sangat rinci, dan QRIS tidak otomatis salah. Namun, masing-masing perlu ditetapkan apakah merupakan kebutuhan mitra, fungsi pendukung, atau pengembangan lanjutan agar ruang lingkup administrasi internal tetap dapat diselesaikan.

**Perbaikan:** pertahankan fungsi inti dan beri prioritas pada tambahan yang mempunyai manfaat serta dasar kebutuhan yang jelas. Kartu SPP pada proses lama tidak otomatis sama dengan kartu anggota PDF, sedangkan QRIS statis juga tidak otomatis berarti integrasi payment gateway.

### F29. Mengurangi tabel bukan bukti optimasi yang cukup

**Lokasi:** bagian justifikasi penghapusan empat tabel, baris 302 sampai 334, serta target MySQL/PostgreSQL. **Prioritas:** penting.

ENUM untuk pilihan tetap dan berkas konfigurasi untuk templat sederhana dapat menjadi keputusan yang sah. Akan tetapi, alasan harus mengikuti kebutuhan perubahan, kewenangan pengguna, keterlacakan, dan DBMS yang akhirnya dipilih, bukan sekadar mengurangi jumlah JOIN atau mempertahankan enam belas tabel.

**Perbaikan:** pilih kebutuhan lebih dahulu, lalu bentuk penyimpanan yang paling sederhana tetapi memenuhinya. Tentukan satu DBMS untuk skema fisik atau sediakan perbedaan implementasinya; dokumen kamus data saat ini belum merupakan DDL yang sudah dieksekusi dan diuji pada keduanya.

## 6. Penilaian per tabel yang sudah dirancang

| Tabel | Bagian yang dapat dipertahankan | Perbaikan utama sebelum dipakai pada Bab 3 |
| :--- | :--- | :--- |
| `academic_years` | Periode dan pengarsipan tahun ajaran | Definisikan satu tahun aktif, rentang tanggal, dan arti tahun pendaftaran siswa |
| `branches` | Identitas cabang dan relasi data operasional | Peta publik dipisahkan dari ruang lingkup inti; jumlah ruang dijaga konsistensinya |
| `users` | Dua peran, akun nonaktif, dan riwayat login | Peran menjadi dasar otorisasi; nilai cabang kosong bukan pemberi hak otomatis |
| `subjects` | Penamaan mata pelajaran yang konsisten | Periksa kebutuhan kelas atau sesi yang mencakup beberapa mata pelajaran |
| `fee_tariffs` | Tarif terpisah dan nominal desimal | Variasi cabang/sesi, masa berlaku, serta paket bulanan/semester/tahunan |
| `students` | Identitas, kontak wali, dan status | Data wajib, cakupan cabang, TK, diskon, serta hubungan saudara yang belum dijelaskan untuk lebih dari dua anak |
| `mentors` | Satu identitas tentor untuk pemeriksaan lintas cabang | Jangan menggandakan tentor per cabang atau mematok jumlah yang belum dikonfirmasi |
| `mentor_subjects` | Relasi banyak ke banyak dengan pasangan unik | Pertahankan jika kompetensi mapel memang digunakan pada penjadwalan |
| `class_rooms` | Pemisahan ruang fisik dari kelompok belajar | Hubungkan kapasitas ruang dengan keputusan penempatan kelas |
| `classes` | Batas kapasitas dan identitas kelompok | Sumber hitungan aktif, ambang hampir penuh, serta status ditutup berbeda dari kondisi penuh |
| `class_schedules` | Kelas, tentor, ruang, hari, dan jam | Masa berlaku, jadwal nonaktif, suntingan, serta konsistensi cabang |
| `class_enrollments` | Hubungan siswa dengan kelas dan status | Tanggal berakhir, riwayat perubahan, dan daftar tunggu yang masih opsional |
| `bills` | Nominal tagihan, diskon aktual, periode, dan jatuh tempo | Anti-duplikasi, kategori paket, riwayat cabang, serta status terlambat terpisah |
| `payments` | Tagihan, kanal, bukti, nominal, dan penanda pemeriksaan dasar | Pengaju, status pengajuan, riwayat pemeriksaan, alokasi beberapa tagihan, dan kuitansi |
| `wa_logs` | Gagasan pencatatan tindakan pengingat | Ubah makna menjadi tindakan admin pada tautan; jangan mengklaim transmisi otomatis |
| `revenue_validations` | Ringkasan pemeriksaan pusat | Pisahkan tunggakan, penerimaan, setoran, dan pencocokan bank yang tertelusur |

Tidak semua perbaikan membutuhkan tabel baru. Sebagian dapat berupa perubahan skenario, atribut, hubungan, batasan nilai, atau penghapusan janji fungsi yang tidak dipakai pada prototipe.

## 7. Contoh rancangan koreksi yang dapat diturunkan ke Bab 3

### 7.1 Alur transfer yang diusulkan

| Tahap | Pelaksana | Data dan perubahan |
| :--- | :--- | :--- |
| Pengajuan | Admin Cabang | Memilih tagihan, mencatat nominal/tanggal, mengunggah bukti, lalu mengirim pengajuan |
| Pemeriksaan | Super Admin yang berwenang | Membandingkan pengajuan dengan rujukan dana masuk pada rekening resmi |
| Persetujuan | Super Admin | Menyimpan keputusan, pemeriksa, waktu, dan alokasi nominal; sisa tagihan dihitung ulang |
| Pengembalian | Super Admin | Menyimpan alasan; pengajuan dapat diperbaiki dan diajukan kembali tanpa menghilangkan jejak |
| Pelaporan | Sistem | Menampilkan penerimaan terkonfirmasi dan pengajuan menunggu pemeriksaan secara terpisah |

Alur tersebut merupakan usulan yang telah dibahas, bukan pengganti persetujuan pihak yang menguasai rekening. Bila dipilih, butir ketiga batasan Bab 1 yang masih menyatakan verifikasi oleh Admin Cabang juga harus disesuaikan.

### 7.2 Aturan kapasitas berdasarkan keputusan pengguna

Jumlah peserta aktif menjadi dasar keterisian kelas. Peringatan hampir penuh muncul menurut ambang yang ditetapkan, sedangkan penambahan ditolak apabila peserta aktif telah mencapai kapasitas.

Ketika siswa keluar dari kelas, status keanggotaannya diakhiri dan waktunya dicatat. Riwayat siswa tetap tersimpan, jumlah aktif diperbarui, dan tempat kembali tersedia; pemindahan otomatis dari daftar tunggu tidak dilakukan sebelum kebutuhannya ditetapkan.

### 7.3 Arah hubungan UML yang perlu disamakan

Jika perilaku cetak bukti pendaftaran benar-benar dipilih sebagai perluasan opsional, arah panah extend berasal dari cetak bukti menuju pendaftaran. Jika pemeriksaan kapasitas menjadi perilaku wajib pada penempatan siswa, arah include berasal dari penempatan menuju pemeriksaan kapasitas.

Pemeriksaan kelayakan diskon dapat tetap menjadi langkah wajib untuk semua pendaftar, sedangkan penerapan diskonnya bersyarat. Nama kasus dan skenario perlu membedakan kedua hal tersebut agar pemakaian include tidak dinilai salah hanya karena tidak semua siswa menerima potongan.

## 8. Urutan kerja terkait sembilan revisi Bab 3

Sembilan poin revisi Bab 3 tetap digunakan sebagai arah pekerjaan. Pemeriksaan model ini menambahkan urutan ketergantungan agar rancangan layar, data, dan pengujian memakai aturan yang sama.

1. Catat keputusan yang sudah jelas dan pisahkan usulan yang masih perlu ditetapkan, terutama kewenangan pembayaran, tarif, diskon, dan fitur tambahan.
2. Selaraskan dokumen use case serta model data dengan keputusan WhatsApp manual dan kapasitas kelas.
3. Perbaiki hubungan transaksi, pengajuan, pemeriksaan, setoran, serta pencocokan penerimaan sebelum menggambar layar keuangan.
4. Perbarui matriks kebutuhan, cerita pengguna, use case, tabel, iterasi, dan pengujian.
5. Gunakan rincian rancangan yang sudah ada sebagai bahan Bab 3, lalu buat gambar antarmuka inti sesuai alur yang telah diselaraskan.
6. Perbaiki diagram alir, prosedur UAT, penyiapan lingkungan uji, spesifikasi, dan jadwal berdasarkan data yang tersedia.
7. Simpan rincian teknis lengkap pada lampiran atau dokumen pendamping agar Bab 3 tetap terbaca.
8. Selaraskan Bab 1 dan Bab 2 setelah aturan rancangan stabil, termasuk rumusan masalah, batasan pembayaran, istilah rekonsiliasi, dan metode evaluasi.

Dokumen lama mempunyai rincian yang lebih kaya daripada model konseptual awal pada draf Bab 3. Rincian tersebut layak dimanfaatkan setelah diperiksa, bukan digantikan seluruhnya dengan diagram generik atau dimasukkan tanpa koreksi.

## 9. Kasus pemeriksaan yang perlu disiapkan

| Kasus | Hasil yang perlu dibuktikan |
| :--- | :--- |
| Admin membuka WhatsApp untuk satu tagihan | Nomor, periode, nominal, dan tanggal benar; pembukaan tautan tidak dianggap terkirim |
| Dua admin mengisi satu tempat terakhir | Hanya satu peserta baru aktif dan kapasitas tidak terlampaui |
| Siswa keluar lalu kembali ke kelas yang sama | Tempat serta riwayat masuk/keluar konsisten dengan kebijakan yang dipilih |
| Kelas dipindah ke ruang lebih kecil | Sistem memeriksa kapasitas dan menolak atau meminta penyesuaian sesuai aturan |
| Jadwal lama nonaktif pada tahun berbeda | Tidak menjadi benturan palsu dengan jadwal yang berlaku |
| Jadwal disunting tanpa mengubah waktunya | Tidak berbenturan dengan dirinya sendiri |
| Satu transfer melunasi dua periode | Alokasi dan total tagihan sesuai, bukti serta kuitansi tidak menghasilkan penerimaan ganda |
| Pengajuan transfer dikembalikan lalu diperbaiki | Riwayat pengajuan dan alasan tetap dapat ditelusuri |
| Persetujuan dikirim dua kali | Sisa tagihan serta total penerimaan hanya berubah satu kali |
| Siswa pindah cabang | Riwayat penerimaan lama tetap dimiliki cabang asal transaksi |
| Paket semester diterbitkan | Tidak berubah menjadi tagihan bulanan berulang tanpa dasar |
| Setoran tunai dicatat | Tidak menambah pendapatan siswa untuk kedua kalinya |
| Akun cabang kosong atau permintaan menyebut cabang lain | Tidak memperoleh hak Super Admin atau akses lintas cabang |

## 10. Penunjuk bukti dan acuan teknis

### 10.1 Berkas utama

- [Use case dan skenario](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/PERANCANGAN USE CASE & SKENARIO.md>).
- [Skema dan ERD](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/DOKUMEN MD/PERANCANGAN BASIS DATA (SKEMA & ERD).md>).
- [Bab 1 yang dibandingkan](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md>).
- [Draf Bab 3](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 3 - RANCANGAN PROTOTIPE (DRAF 2026-10-25).md>).

### 10.2 Bukti lapangan terpilih

| Topik | Lokator transkrip | Batas penafsiran |
| :--- | :--- | :--- |
| Tarif terkait sesi | [Frontdesk, baris 292](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:292>), 14:17 sampai 14:36 | Tidak otomatis menetapkan tarif seluruh cabang |
| Potongan saudara | [Frontdesk, baris 384](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:384>), 19:18 sampai 20:51 | Menyebut Rp10.000 per anak pada konteks cabang yang diwawancarai |
| Potongan Rp200.000 dan penyesuaian lain | [Wawancara ketiga, baris 617](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt:617>), 48:06 dan bagian berikutnya | Tidak cukup untuk mematok pengurangan Rp200.000 pada setiap SPP semua siswa |
| Jumlah pengajar berbeda | [Frontdesk, baris 593](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:593>), 30:31 sampai 31:10 | Jumlah satu cabang tidak dikalikan sebagai jumlah pasti seluruh tentor |
| Kapasitas ruang | [Frontdesk, baris 881](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:881>), 45:19 sampai 46:30 | Kapasitas bervariasi; pengendalian kelas merupakan kebutuhan yang tetap relevan |
| Laporan dan setoran harian | [Frontdesk, baris 981](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:981>), 50:38 sampai 51:48 | Bedakan dari rekap bulanan jumlah siswa per tentor |
| Pengiriman bukti transfer | [Frontdesk, baris 1017](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1017>), 52:24 sampai 52:42 | Belum menentukan seluruh pembagian kewenangan sistem usulan |
| Jatuh tempo per siswa | [Frontdesk, baris 1136](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1136>), 58:19 sampai 59:25 | Mengikuti tanggal awal masuk menurut informan; bukan satu tanggal global |

Transkrip otomatis dapat mengandung salah dengar dan perlu diperiksa terhadap rekaman pada bagian yang ambigu. Perbedaan keterangan tidak diselesaikan dengan memilih satu angka tanpa memastikan konteks, cabang, periode, dan kewenangan narasumber.

### 10.3 Acuan teknis primer yang diperiksa

- [OMG, spesifikasi UML, bagian Extend dan Include](https://www.omg.org/spec/UML/ISO/19505-2/PDF), cetak 609 sampai 611: arah hubungan serta perbedaan perluasan dan penyertaan perilaku.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html): pemeriksaan hak akses pada setiap permintaan dan penolakan akses yang tidak mempunyai dasar izin.
- [MySQL 8.4, Locking Reads](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html): pembacaan biasa belum cukup melindungi rangkaian pemeriksaan dan pembaruan terhadap transaksi serentak.

Acuan tersebut dipakai untuk memeriksa ketepatan rancangan teknis. Kebijakan bisnis ARTHA, nominal, kewenangan, serta prioritas fitur tetap ditetapkan berdasarkan kebutuhan mitra dan keputusan penelitian yang terdokumentasi.
