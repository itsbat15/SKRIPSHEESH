# Hasil pemeriksaan ulang Bab 2

Pemeriksaan ini membaca versi terbaru `BAB_2_TINJAUAN_PUSTAKA.md` yang terdiri atas 410 baris, kemudian mencocokkan bagian pentingnya dengan sumber dalam koleksi. Pencocokan difokuskan pada teori PxP dan notasi, sumber gambar baru, serta identitas, teknologi, dan angka hasil penelitian pada Tabel 2.9; pekerjaan ini tidak mengulang verifikasi SINTA seluruh jurnal.

**Penilaian umum: terdapat perbaikan nyata, tetapi naskah belum dapat dinyatakan seluruhnya benar atau siap digunakan tanpa revisi lanjutan.** Sejumlah perbaikan sebelumnya sudah diterapkan, sementara beberapa kesalahan lama masih tersisa dan sumber gambar baru menimbulkan satu kesalahan atribusi yang perlu segera dikoreksi.

## 1. Perbaikan yang sudah tepat

Nama Ahadi, Pariyadi, dan Djauhari serta metode Waterfall pada tabel penelitian terdahulu sudah diperbaiki. Artikel Hendri kini dijelaskan sebagai perancangan prototipe menggunakan Figma, bukan implementasi Laravel dengan angka UAT yang tidak didukung sumber.

Pembahasan BPMN sudah menyatakan bahwa sequence flow dapat melintasi lane dalam satu proses. Kalimat transaksi Laravel dan peran InnoDB juga sudah lebih proporsional, sedangkan penafsiran skor kepuasan mulai membedakan persepsi positif dari kelulusan tugas operasional kritis.

Lima gambar sudah tersedia dalam folder aset dan beberapa lokasi sumbernya dapat dikonfirmasi. Gambar PxP sesuai sumber pada cetak 255; BPMN sesuai Gambar 7.3 pada cetak 23; ringkasan ERD sesuai Elmasri dan Navathe pada cetak 83; sumber diagram bank perlu dikoreksi sebagaimana dijelaskan di bawah.

## 2. Revisi sangat penting

| Lokasi naskah | Temuan | Bukti atau alasan | Perbaikan praktis |
| :--- | :--- | :--- | :--- |
| 2.1.4, baris 113 sampai 119, Gambar 2.2 | Nama penulis dan tahun sumber gambar salah. | Berkas `JURNAL/JURNAL PENDUKUNG/yusrian,+610-1857-1-CE+(1).pdf` berisi artikel Tri A. Kurniawan, 2018, bukan Yusrian dkk. 2024. Gambar 1 memang berada pada cetak 80/PDF 4. | Ganti narasi dan sumber menjadi Kurniawan (2018, hlm. 80, Gambar 1). Nama berkas unduhan tidak dijadikan identitas penulis. |
| 2.1.4, Tabel 2.3, baris 110 | Arah makna extend terbalik. | Naskah menyebut use case target memperluas sumber; OMG UML §18.1 menjelaskan sumber adalah extending use case dan target adalah extended use case. Lihat cetak 641/PDF 683. | Tulis: garis putus-putus berpanah terbuka dari use case perluasan menuju use case dasar yang diperluas. |
| 2.2, Tabel 2.9, baris 391 | Bee Hive masih disebut memakai MySQL. | Artikel Fajriansyah menjelaskan SQLite pada cetak 118/PDF 4 dan cetak 119/PDF 5. | Ganti MySQL menjadi SQLite. Laravel 12, Google Sheets API, dan Brevo memang disebut dalam sumber. |
| 2.2, Tabel 2.9, baris 399 | Waktu Sidiq salah satuan dan pembanding estimasinya belum lengkap. | Kesimpulan cetak 45/PDF 11 menjelaskan estimasi awal 40 hari, diperbarui menjadi 50 hari, dan implementasi aktual 37 hari. | Ganti jam menjadi hari, sertakan perubahan estimasi, dan bandingkan 37 hari dengan estimasi akhir 50 hari jika menyebut selisih 13 hari. |
| 2.2, Tabel 2.9, baris 396; sintesis baris 406 | Java belum didukung teks sumber dan client-server kembali disebut satu pengguna pada sintesis. | Sudirman cetak 127/PDF 2 membahas Visual Basic, MySQL, dan Crystal Report; cetak 128/PDF 3 memuat Prototyping; cetak 129/PDF 4 menyebut client-server dan pembatasan hak akses. | Hapus klaim Java yang belum terverifikasi, jelaskan teknologi sesuai bukti, dan ubah sintesis agar konsisten dengan arsitektur client-server. Jangan menyimpulkan single-user tanpa bukti. |
| 2.2, Tabel 2.9, baris 398 | Angka 100% dilekatkan pada Black Box Testing, padahal sumber mengaitkannya dengan validasi CSP. | Kabisatullah cetak 94/PDF 6 membedakan Black Box, 25 skenario validasi CSP dengan hasil 100%, dan UAT 30 responden dengan skor 4,26/5. | Pisahkan ketiga hasil tersebut. Angka UAT dan jumlah responden sudah sesuai sumber; jangan memindahkan angka antarteknik pengujian. |
| 2.1.14, baris 349 sampai 377 | Klaim instrumen tervalidasi dan atribusi ambang kelayakan kepada Sugiyono masih belum terbukti. | Berkas Sugiyono yang dapat memastikan judul, edisi, dan halaman untuk formula serta interval tersebut belum ditemukan dalam koleksi yang diperiksa. Skala respons bukan bukti validitas butir kuesioner. | Tentukan indikator dan cara pemeriksaan instrumen. Lengkapi sumber yang benar-benar memuat formula/interval atau hapus atribusi yang belum dapat dibuktikan. |

Angka kurang dari dua detik dan benturan jadwal nol persen pada Bee Hive memang ditemukan pada cetak 124 sampai 125/PDF 10 sampai 11. Namun, gunakan rumusan “penulis melaporkan” dalam konteks evaluasi sumber, bukan kesimpulan bahwa risiko benturan jadwal telah dieliminasi secara umum.

Hasil Apriyanti sebesar 91% juga ditemukan pada cetak 3685/PDF 8, tetapi sumber menyebut kategorinya “sangat baik”, bukan “sangat layak”. Sumber tersebut juga tidak konsisten dalam menyebut peserta pada pembahasan dan kesimpulan, sehingga jumlah peserta tidak perlu ditambahkan tanpa menjelaskan perbedaan yang ada.

## 3. Revisi penting pada teori dan metodologi

| Lokasi | Kekurangan yang masih ada | Arah perbaikan |
| :--- | :--- | :--- |
| 2.1.1, Tabel 2.1, baris 23 sampai 32 | Waterfall masih digambarkan memerlukan alokasi antarperan, dan rilis Scrum dipatok pada akhir sprint 2 sampai 4 minggu. | Ukuran tim tidak ditentukan oleh model Waterfall. Scrum Guide menyebut sprint satu bulan atau kurang dan increment dapat disampaikan sebelum sprint berakhir; jangan menyamakan batas sprint dengan kewajiban waktu rilis. |
| 2.1.2, baris 36 dan 40 | Kata “distandarisasi” atau “distandarisasikan” menyiratkan pengesahan formal yang tidak dibuktikan artikel Dzhurov. | Gunakan “diusulkan”, “dirumuskan”, atau “dijelaskan”. Rantai sejarah Agarwal ke Dzhurov dan klaim “pertama kali” perlu bukti khusus jika dipertahankan. |
| 2.1.2, baris 40 sampai 48 | Lima prinsip kini sudah disebut sebagai adaptasi proyek, tetapi masih bercampur dengan klaim tiga instrumen wajib dan Fibonacci dari Cohn (2004). | Pertahankan pembedaan prinsip sumber dan adaptasi peneliti. Periksa halaman sumber Fibonacci; artikel resmi Cohn tentang modified Fibonacci dapat menjadi rujukan yang lebih mudah dilacak, sementara estimasi durasi tugas tetap perlu dijelaskan dalam penerapan PxP. |
| 2.1.3, baris 68 | Cohn disebut merumuskan Three C’s. | Cuplikan Cohn cetak 4/PDF 13 mengatribusikan Card, Conversation, Confirmation kepada Ron Jeffries. Tulis “Cohn (2004) menjelaskan tiga aspek user stories” atau “konsep yang diatribusikan kepada Jeffries sebagaimana dijelaskan Cohn (2004)”. |
| 2.1.5, baris 129 sampai 134 | Pengelompokan BPMN menjadi empat kategori dan penempatan data object serta data store sebagai artifacts tidak mengikuti pembagian pada spesifikasi 2.0.2. | Gunakan kategori Flow Objects, Data, Connecting Objects, Swimlanes, dan Artifacts. Data object dan data store berada pada kategori Data; contoh artifacts adalah group serta text annotation. |
| 2.1.7, baris 200 dan 206 sampai 226 | Derajat relasi disamakan dengan kardinalitas, dan seluruh simbol klasik diatribusikan kepada cuplikan Chen. | Derajat menunjukkan jumlah tipe entitas yang terlibat, sedangkan kardinalitas menyatakan batas keterhubungan. Gunakan Elmasri dan Navathe sebagai sumber tabel notasi yang benar-benar tersedia, kemudian selaraskan pilihan Chen atau Crow’s Foot dengan ERD Bab 3. |
| 2.1.10 dan 2.1.11, baris 272 dan 281 | Sesi Sanctum dan batasan stateless REST disebut tanpa menjelaskan hubungan keduanya pada rancangan. | Nyatakan API HTTP mengadopsi pemodelan sumber daya dan semantik HTTP, sedangkan autentikasi memakai sesi. Jangan menyatakan kepatuhan penuh pada stateless REST untuk rancangan yang menyimpan konteks sesi pengguna di peladen. |
| 2.1.13, Tabel 2.7, baris 333 sampai 334 | Kolom batas menyebut tiga nilai, tetapi kolom nilai uji hanya memuat dua nilai. | Pilih varian BVA secara eksplisit. Untuk contoh dua nilai gunakan 0 dan 1, serta 30 dan 31; jika memilih tiga nilai, jabarkan batas yang diidentifikasi dan tetangganya secara konsisten. |
| 2.1.13 dan 2.1.14, baris 313 dan 342 | Black Box digambarkan seolah penguji tidak boleh mengetahui kode dan hanya dilakukan pengembang, sedangkan UAT diposisikan sebagai kategori yang berlawanan. | Black Box menyatakan dasar perancangan uji tanpa bertumpu pada struktur internal. UAT menyatakan tujuan penerimaan dan dapat menggunakan teknik Black Box, sehingga keduanya tidak saling meniadakan. |
| 2.1.14, baris 353 dan 367 sampai 377 | Pilihan “Cukup Setuju atau Netral” menggabungkan dua arti; interval persentase belum menjelaskan nilai desimal. | Pilih satu label respons yang jelas dan seimbang. Jika kategori persentase dipertahankan, jelaskan aturan nilai batas serta pembulatan; pada pembobotan 1 sampai 5, skor minimum indeks yang ditampilkan adalah 20%, bukan 0%. |
| 2.2, pembukaan dan kolom pembeda | Seluruh artikel disebut terverifikasi, sedangkan edisi Sidiq masih memiliki catatan; ketiadaan uraian fitur dinyatakan sebagai ketiadaan fitur. | Bedakan peringkat jurnal dari cakupan edisi. Gunakan “tidak dibahas dalam artikel” jika tidak ada bukti fitur memang tidak tersedia. |
| 2.2, baris 408 sampai 410 | Kompleksitas penelitian lain dianggap lebih sederhana dan metode PxP disebut sedang diuji ketangguhannya. | Jadikan fokus kontribusi pada pengembangan dan evaluasi prototipe ARTHA. Klaim pengujian keunggulan atau ketangguhan metode memerlukan rancangan evaluasi metode dan indikator tersendiri. |

Sumber resmi pembanding Scrum tersedia pada https://scrumguides.org/scrum-guide.html, terutama bagian The Sprint, Daily Scrum, dan Increment. Untuk Fibonacci, artikel penulis tersedia pada https://www.mountaingoatsoftware.com/agile/why-the-fibonacci-sequence-works-well-for-estimating dan mencantumkan pembaruan 25 Juni 2024; artikel ini bukan bukti bahwa setiap pernyataan serupa pasti terdapat pada buku Cohn tahun 2004.

## 4. Status ringkas setiap baris penelitian terdahulu

| Artikel | Hasil pencocokan ulang isi |
| :--- | :--- |
| Fajriansyah | Identitas jurnal dan Laravel 12 sudah lebih tepat; basis data harus menjadi SQLite. Angka evaluasi ditemukan, tetapi generalisasi risiko dan klaim satu lokasi perlu dibatasi pada yang dijelaskan sumber. |
| Gunawan | Nama penulis sudah tepat. Nama objek pada sumber adalah Rumah Sinau Dhita Course, bukan Rumah Sinau Learning Center; jurnalnya Riau Jurnal Teknik Informatika, bukan Riset Jurnal Teknologi Informasi. Lihat cetak 424 sampai 425/PDF 1 sampai 2. |
| Thiovanda | Peran head admin dan cakupan cabang memang disebut. Hindari menyimpulkan fitur kapasitas atau penjadwalan tentor tidak ada hanya karena tidak dijabarkan dalam artikel. |
| Ahadi | Penulis dan Waterfall sudah diperbaiki. Klaim MySQL belum ditemukan dalam teks PDF yang diperiksa, sehingga tidak boleh diasumsikan hanya berdasarkan pemakaian Laravel; pastikan melalui bagian atau artefak sumber yang eksplisit. |
| Hendri | Waterfall, Figma, UML, dan kedudukan sebagai desain prototipe didukung sumber. Hindari mengubah harapan peningkatan akurasi menjadi hasil peningkatan yang sudah diukur. |
| Sudirman | R&D, Prototyping, MySQL, dan client-server didukung sumber. Java belum terverifikasi dan sintesis satu pengguna perlu dihapus atau dibuktikan. |
| Khafidhoh | Algoritma genetika, PHP, MySQL, dan notifikasi WhatsApp memang disebut. Istilah WhatsApp Gateway belum dipastikan dari uraian implementasi; jangan memakai daftar pustaka artikel sebagai bukti fitur teknologinya. |
| Kabisatullah | Delapan sprint, 30 responden, dan skor 4,26/5 sesuai sumber. Angka 100% perlu dikaitkan dengan 25 skenario validasi CSP. |
| Sidiq | Lima belas user stories sesuai sumber setelah penambahan dari tiga belas. Waktu harus ditulis dalam hari dan menyertakan estimasi awal 40 hari, estimasi akhir 50 hari, serta aktual 37 hari. |
| Apriyanti | Angka 91% sesuai sumber. Pertahankan kategori sumber “sangat baik” dan batasi kesimpulan pada studi E-Kavling, bukan pembuktian umum bahwa PxP lebih unggul. |

## 5. Bahasa, format, dan referensi

Dalam berkas yang diperiksa belum terdapat daftar pustaka, walaupun sejumlah sumber baru sudah dikutip, seperti Humphrey (1995), Elmasri dan Navathe (2016), dan nama yang digunakan pada Gambar 2.2. Jika daftar pustaka memang dikelola pada berkas terpisah, semua sitasi tersebut tetap harus dipasangkan dengan entri yang benar; ketiadaan daftar pada berkas ini tidak otomatis membuktikan daftar pustaka tidak ada di seluruh proposal.

Penamaan penulis lembaga belum konsisten karena “OMG UML 2.5.1” dan “ISTQB CTFL v4.0.1” digunakan seolah nama penulis. Gunakan Object Management Group atau ISTQB sebagai penulis lembaga, sedangkan versi dan judul dokumen dicatat pada daftar pustaka; Beck (2004) juga perlu diselaraskan dengan Beck dan Andres (2004) apabila merujuk buku yang sama.

Beberapa uraian masih menggunakan kata “menjamin”, “paling tepat”, atau menyatakan rancangan sudah divalidasi tanpa bukti pelaksanaan. Contohnya terdapat pada baris 127, 161, 165, dan 192; gunakan “membantu”, “mendukung”, “digunakan untuk”, atau “direncanakan” sesuai kedudukan klaim.

Tidak ditemukan tanda em dash atau en dash pada naskah ini. Namun, paragraf pengantar formula pada baris 357 dan pengantar kategori pada baris 367 masing-masing hanya satu kalimat, sehingga perlu digabungkan dengan paragraf terkait atau dilengkapi penjelasan sesuai aturan penulisan proyek.

## 6. Urutan pengerjaan

Pertama, koreksi sumber Gambar 2.2 dan tabel penelitian terdahulu, khususnya SQLite Bee Hive, satuan waktu Sidiq, teknologi Sudirman, serta pemisahan hasil CSP dan Black Box pada RapaTrack. Kedua, benahi arah extend, atribusi Three C’s, pengelompokan BPMN, serta konsistensi BVA karena perubahan ini langsung memengaruhi pemahaman teori.

Ketiga, lengkapi dasar instrumen UAT dan daftar pustaka sebelum menetapkan formula atau kategori kelayakan. Setelah itu, selaraskan klaim kontribusi dengan tujuan pengembangan prototipe ARTHA dan ringkas kalimat yang berlebihan; naskah utama belum diubah dalam pemeriksaan ini.
