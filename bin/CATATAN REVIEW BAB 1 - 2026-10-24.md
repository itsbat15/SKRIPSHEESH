# Catatan penelaahan Bab 1 ARTHA

Penelaahan ini menggunakan teks terbaru yang dikirim pada 24 Oktober 2026 melalui [lampiran teks pengguna](<C:/Users/ARIEL/.codex/attachments/ed7e7c03-6d2f-4d60-87c6-315af1d4787d/Pasted text.txt>). Kesimpulannya, struktur Bab 1 sudah dapat digunakan sebagai dasar bimbingan, tetapi isi belum siap dinyatakan final karena masih terdapat kesalahan pembacaan metode, generalisasi fakta kasus, dan rincian rancangan yang belum konsisten.

Teks terbaru lebih baik daripada draf awal dalam beberapa hal: angka 2.000 siswa telah dikeluarkan, buku dijelaskan tetap di cabang, dan referensi tambahan sudah digunakan. Kelebihan tersebut perlu dipertahankan sambil memperbaiki hal-hal di bawah ini; penambahan jumlah sitasi tidak menggantikan pemeriksaan hubungan setiap klaim dengan sumbernya.

## Ringkasan penilaian

| Aspek | Penilaian | Implikasi |
| --- | --- | --- |
| Susunan subbab | Sesuai arah template prototipe | Pertahankan bagian 1.1 sampai 1.7; pastikan penomoran tampil pada berkas Word. |
| Alur latar belakang | Sudah terbaca, tetapi beberapa paragraf terlalu padat | Ringkas rincian operasional dan uraian penelitian; pertegas kebutuhan yang diturunkan dari bukti. |
| Fakta wawancara | Sebagian didukung, sebagian digeneralisasi | Batasi keterangan staf cabang pada cakupan yang benar-benar disampaikan. |
| Justifikasi PxP | Memerlukan revisi utama | Pertahankan alasan positif PxP, koreksi larangan mutlak terhadap metode lain. |
| Sitasi | Relevansi meningkat, dukungan klaim belum selalu tepat | Pisahkan fakta ARTHA, hasil studi lain, teori metode, dan usulan rancangan. |
| Rumusan dan tujuan | Sejalan, tetapi sebagian berulang | Bedakan pembangunan fungsi, pemantauan pusat, dan evaluasi; jelaskan ukuran keberhasilan. |
| Batasan rancangan | Belum cukup untuk alur pembayaran dan pengujian | Tentukan kewenangan, status pemeriksaan, data awal, serta cakupan uji. |
| Manfaat dan dampak | Relevan, tetapi beberapa manfaat ditulis sebagai hasil | Gunakan bentuk harapan atau potensi sampai terdapat pengukuran. |
| Kerangka TA | Masih lebih berupa analisis masalah | Tambahkan alur pelaksanaan, iterasi, pengujian, dan evaluasi yang diminta template. |
| Bahasa dan teknis penulisan | Masih memerlukan penyuntingan | Perbaiki kalimat tidak lengkap, salah ketik, paragraf satu kalimat, dan petunjuk template. |

## Revisi utama yang memengaruhi ketepatan ilmiah

### A. Klaim tentang Scrum harus dikoreksi

Teks menyatakan bahwa peran Scrum dilarang dirangkap dan bahwa penerapan oleh pengembang tunggal tidak dapat dipertanggungjawabkan secara akademis. Larangan mutlak tersebut tidak didukung [Scrum Guide 2020, hlm. 9](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf), yang justru membahas Product Owner atau Scrum Master yang turut mengerjakan Sprint Backlog sebagai Developers.

Keterangan itu juga perlu diselaraskan dengan [bimbingan Bu Ayu, 46:43 sampai 47:01](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:1102>), yang menjelaskan kemungkinan perangkapan peran dan konsekuensinya. Hal ini bukan bukti bahwa proyek satu orang otomatis memenuhi seluruh Scrum, melainkan alasan untuk mengganti penolakan mutlak dengan pembahasan kecocokan dan beban penerapan pada proyek ARTHA.

### B. Perbandingan metode lain terlalu mutlak dan tidak seluruhnya sesuai sumber

| Klaim dalam teks | Masalah | Perbaikan |
| --- | --- | --- |
| Waterfall tidak menampung perubahan dan berisiko menghasilkan sistem tidak relevan | Kesimpulan terlalu luas; perlu dibedakan model berurutan dan biaya/konsekuensi perubahan. | Jelaskan kebutuhan umpan balik dan perubahan ARTHA, lalu bandingkan pengelolaan perubahan antarmetode dengan sumber dan halaman tertentu. |
| Prototyping tidak menghasilkan metrik yang memadai untuk sidang, dengan sitasi Dzhurov dkk. (2009) | Makalah itu menjelaskan PxP, PSP, praktik XP, dan perbandingan dengan pengembangan ad hoc; bukan bukti bahwa Prototyping tidak dapat dipertanggungjawabkan. | Hapus kesimpulan tersebut dan tempatkan pembahasan pencatatan waktu/cacat sebagai alasan positif menggunakan PxP. |
| XP mensyaratkan kehadiran mitra setiap hari dan kondisi itu tidak mungkin dipenuhi ARTHA | Praktik kolaborasi pelanggan perlu dibahas sesuai sumber; ketidakmungkinan pada ARTHA memerlukan bukti jadwal/kesediaan mitra. | Pisahkan karakteristik praktik XP dari fakta ketersediaan mitra. Cantumkan lokator buku atau makalah sebelum menarik kesimpulan yang kuat. |
| RAD harus menggunakan tim paralel dan tidak cocok untuk logika bisnis unik ARTHA | Klaim kategoris membutuhkan dukungan halaman yang tepat; keberadaan diskon atau rekap cabang saja belum membuktikan ketidakcocokan RAD. | Bahas sumber daya, modularisasi, keterlibatan pengguna dan kebutuhan komponen secara terbatas. Jangan menganggap fitur diskon otomatis menutup pilihan RAD. |

Alasan yang lebih kuat untuk PxP adalah adanya proses pengembangan individual, pembagian tugas, pencatatan estimasi dan realisasi, pengujian berkelanjutan, serta retrospektif yang akan benar-benar dilaksanakan. Landasan aslinya dapat menggunakan [Dzhurov, Krasteva dan Ilieva (2009)](https://research.uni-sofia.bg/handle/10506/647), sedangkan Apriyanti dkk. (2024) mendukung contoh penerapan dan pengujian; hasil studi lain tidak menjadi jaminan keberhasilan ARTHA.

### C. Komitmen mitra setiap iterasi belum boleh ditulis sebagai fakta pasti

Dua paragraf metode menyatakan bahwa mitra telah bersedia mengevaluasi setiap akhir iterasi. Pada transkrip yang diperiksa, kesediaan dihubungi kembali dan pertanyaan pembimbing tentang keterlibatan pemangku kepentingan belum setara dengan persetujuan jadwal evaluasi rutin.

Gunakan rumusan rencana, misalnya: “Evaluasi modul direncanakan bersama perwakilan mitra pada akhir iterasi sesuai jadwal yang disepakati.” Tentukan nama/peran evaluator, frekuensi, bentuk evaluasi dan dokumentasinya sebelum komitmen itu dijadikan alasan utama metode; lihat [bimbingan Bu Ayu, 45:09 sampai 45:45](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:1045>).

### D. Kapasitas sepuluh sampai lima belas siswa tidak berlaku universal

Angka tersebut masih muncul sebagai batas setiap cabang, padahal [frontdesk, 45:19 sampai 46:19](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:881>) menyebut beberapa kapasitas berbeda, yaitu delapan, sepuluh, dua belas, dan tiga belas siswa pada ruang yang dibahas. [Pengelola, 35:25 sampai 38:37](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA KETIGA SKRIPSI (MAMA RADIT)_WITH_TIMESTAMPS.txt:468>) juga membedakan kapasitas menurut jenjang, termasuk kelompok awal SD yang lebih kecil.

Rumusan yang dapat dipertahankan adalah bahwa kapasitas ditetapkan menurut ruang, jenjang, dan sesi berdasarkan kebijakan mitra. Fitur keterisian dan peringatan tetap dapat diajukan, tetapi batasnya perlu menjadi data yang dapat diatur, bukan satu angka untuk seluruh cabang.

### E. Bedakan fakta lapangan, risiko, dan usulan

Peringatan jadwal ganda dan kapasitas dapat dibenarkan sebagai dukungan koordinasi serta pencegahan. Namun, kalimat pada bagian dampak masih menyatakan benturan “selama ini kerap terlambat diketahui”, sedangkan [frontdesk, 31:10 sampai 33:06](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:607>) menjelaskan pembagian jadwal dan tidak membenarkan kejadian berulang tersebut.

Kalimat “pencocokan mutasi rekening baru dapat dimulai setelah berkas pendukung tiba” juga belum didukung sebagai aturan operasional yang pasti. [Frontdesk, 52:24 sampai 52:42](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:1017>) justru menyebut pengiriman bukti transfer melalui pesan, sehingga bukti digital dan penitipan kas fisik perlu dibahas sebagai alur berbeda.

## Ketepatan profil dan rincian proses bisnis

- **Riwayat pendirian:** tanggal 10 Oktober 1997 muncul sebagai informasi dari website yang disebut pewawancara. Jika dipertahankan, gunakan profil resmi atau konfirmasi pengelola sebagai bukti; pada 24 Oktober 2026, ungkapan “hampir 29 tahun” juga sudah tidak tepat, sehingga menuliskan tahun pendirian lebih tahan terhadap perubahan tanggal.
- **Jumlah tentor:** angka rata-rata tujuh sampai delapan orang per cabang belum memiliki dukungan yang jelas dari transkrip. Penggantian “60” menjadi “puluhan” belum menyelesaikan persoalan jika dasar rata-ratanya tetap tidak terverifikasi; gunakan rekap bertanggal atau hilangkan estimasi.
- **Enam cabang melayani TK:** terdapat dukungan keterangan bahwa layanan kalistung/TK tidak ada pada Artha 3 dan Artha 6. Ini dapat dipakai dengan atribusi narasumber, tetapi tidak membuktikan seluruh jam dan tarif seragam pada enam cabang lainnya.
- **Jadwal dan tarif:** banyak rincian memang terdapat pada wawancara frontdesk, tetapi konteksnya mencakup cabang yang ditangani narasumber. Pada [14:18 sampai 14:36](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/WAWANCARA/TRANSKRIP TEKS (TXT)/WAWANCARA MITRA (FRONTDESK)_WITH_TIMESTAMPS.txt:292>), narasumber membedakan tarif/jam TK di cabang tersebut dan cabang lain, sehingga jangan menjadikannya satu matriks universal delapan cabang.
- **Penutupan kas pukul 19.20:** keterangan ini muncul pada wawancara frontdesk mengenai cabangnya. Jangan langsung menulis bahwa seluruh cabang menerapkan batas yang sama tanpa SOP atau konfirmasi pusat.
- **Identitas narasumber:** transkrip frontdesk menyebut nama Agian. Ejaan nama lengkap dan jabatan formal perlu mengikuti surat, lembar persetujuan, atau konfirmasi narasumber, bukan perkiraan hasil transkripsi; gelar akademik juga tidak diperlukan pada setiap penyebutan dalam uraian.
- **Kelengkapan alamat siswa:** bedakan kolom buku yang diperlihatkan dari formulir pendaftaran dan media pencatatan lain. Frasa “tanpa mencakup alamat maupun data identitas lengkap lainnya” terlalu luas sebelum seluruh dokumen terkait diperiksa.
- **Manual:** sebagian pencatatan masih berbasis buku, tetapi komunikasi memakai WhatsApp. “Pencatatan siswa dan pembayaran masih menggunakan buku” lebih tepat daripada menyebut seluruh administrasi sepenuhnya manual tanpa batas proses.

Paragraf rincian jam, harga dan paket pada teks terbaru berisi sekitar 349 kata, sedangkan paragraf perbandingan metode sekitar 371 kata. Masalahnya adalah terlalu banyak pokok yang digabungkan, bukan pelanggaran batas jumlah kata tertentu; ringkas latar belakang menjadi variasi layanan, jadwal dan biaya, lalu pindahkan matriks rinci ke profil mitra, analisis kebutuhan atau lampiran.

## Sitasi dan hubungan klaim dengan sumber

Sitasi penelitian perlu ditempatkan segera setelah klaim yang benar-benar didukung penelitian tersebut. Contohnya, fakta tentang penyerahan kas ARTHA harus dirujuk ke wawancara atau dokumen ARTHA, sedangkan Hendri dkk., Ramadhan dan Widodo, atau Sudirman dan Tristianti digunakan untuk pembanding serta dasar rancangan.

| Bagian | Hal yang perlu diperbaiki |
| --- | --- |
| Definisi sistem informasi | Pradana (2024) merupakan kajian pendidikan, sehingga definisi fundamental sebaiknya diperiksa ke sumber teori primer yang dirujuknya atau ditulis sebagai uraian fungsi tanpa mengklaim definisi baku. |
| Undang-Undang | Jika dipertahankan, kaitkan langsung dengan Pasal 26 dan masukkan sumber resmi pada daftar pustaka; pasal itu membahas pendidikan nonformal, bukan uraian khusus sistem administrasi bimbel. |
| Penelitian terdahulu | Ringkas menurut kelompok fungsi dan jelaskan persamaan, perbedaan, serta fungsi yang diadaptasi. Daftar panjang judul dan fitur belum dengan sendirinya menghasilkan analisis perbandingan. |
| Kebaruan | Batasi pada penelitian yang benar-benar ditelaah. Kalimat “umumnya satu cabang” atau “penelitian multicabang belum membahas bimbel” memerlukan cakupan pencarian yang jelas jika akan dijadikan klaim tentang seluruh literatur. |
| RapaTrack | Artikel menerapkan validasi kapasitas dan waktu pada reservasi ruang rapat. Ubah “membuktikan perlunya” menjadi “memberikan contoh penerapan”, lalu jelaskan perbedaan dengan peringatan yang mengikuti kebijakan ARTHA. |
| PxP | Sitasi Dzhurov dkk. mendukung proses PxP dan pelacakan pekerjaan, bukan penolakan semua alternatif. Penjelasan PxP juga perlu memuat hubungan PSP dan praktik XP, bukan hanya menyebut turunan XP. |
| Gaya penulis | Gunakan satu konvensi author-year yang konsisten. Dalam uraian berbahasa Indonesia, bentuk “dan” untuk dua penulis dan “dkk.” untuk lebih dari dua penulis dapat diseragamkan sesuai gaya Harvard yang dipilih pada pengelola referensi. |
| Daftar pustaka | Daftar pustaka tidak ikut disertakan dalam teks terbaru. Karena itu, kesesuaian seluruh sitasi dengan entri, tahun, DOI dan urutan abjad belum dapat dinyatakan selesai untuk versi tersebut. |

[UU Nomor 20 Tahun 2003, Pasal 26](https://jdih.kemendikdasmen.go.id/sjdih/siperpu/dokumen/salinan/UU_tahun2003_nomor020.pdf) dapat digunakan sebagai sumber primer apabila pembuka hukum dipertahankan. Peringkat dan cakupan enam artikel tambahan telah dijelaskan pada [laporan validasi referensi](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/JURNAL/VALIDASI_KESIAPAN_BAB1_2026-10-24.md>), tetapi status akreditasi tidak membuktikan bahwa setiap parafrase dalam draf sudah tepat.

## Konsistensi rumusan, tujuan, batasan dan pengujian

Rumusan masalah pertama dan kedua masih tumpang tindih pada pembangunan sistem dan dasbornya. Keduanya dapat dipertahankan jika rumusan pertama menekankan integrasi fungsi operasional, sementara rumusan kedua menekankan kewenangan cabang, pemantauan pusat dan alur pemeriksaan penerimaan.

Tujuan juga perlu memuat hasil yang dapat diperiksa, yaitu prototipe fungsional, dasbor dan kontrol akses, serta hasil pengujian/penerimaan. Karena bentuk TA adalah prototipe perangkat lunak, kata “merancang dan membangun” lebih konsisten dengan rencana implementasi dibandingkan seluruh tujuan hanya menggunakan “merancang”.

| Isu rancangan | Keputusan yang perlu diperjelas |
| --- | --- |
| Transfer diverifikasi Admin Cabang | Apakah admin mempunyai kewenangan memeriksa rekening? Jika hanya mengumpulkan tangkapan layar, bedakan unggahan bukti dari konfirmasi penerimaan dana. |
| Rekonsiliasi kas dan bank | Pisahkan pembayaran tunai dengan pencocokan catatan/setoran, serta pembayaran transfer dengan pemeriksaan mutasi. Tentukan transaksi yang belum cocok, petugas penanggung jawab dan cara koreksinya. |
| Tanpa payment gateway | Dapat menjadi batasan rancangan, tetapi bukan bukti persetujuan final pembimbing. Bu Ayu meminta evaluasi beban verifikasi, keaslian bukti, akses mutasi dan biaya alternatif. |
| WhatsApp | Tautan yang dipicu petugas berbeda dari notifikasi otomatis. Samakan istilah di latar belakang, batasan, manfaat, kerangka dan skenario uji. |
| Pemantauan real-time | Jelaskan apakah yang dimaksud data terbaru setelah penyimpanan/pemuatan halaman atau pembaruan seketika. Jangan mengesankan ada koneksi langsung ke bank jika rancangan tidak mencakupnya. |
| Kapasitas dan peringatan jadwal | Tentukan dasar hitung, ambang, hak penyesuaian, serta pencatatan keputusan pengguna. Hindari otomatis mengunci proses jika kebijakan yang direncanakan memberi ruang keputusan pengelola. |
| Data lama tidak dimigrasi | Tetap perlukan data induk siswa lama, status awal pembayaran dan periode mulai agar tunggakan serta siswa aktif dapat diuji. Bedakan tidak memigrasikan seluruh transaksi historis dengan tidak menyediakan data awal sama sekali. |
| Delapan cabang | Bedakan cakupan struktur/data delapan cabang dan lokasi uji nyata. Jangan menyatakan penerapan serentak sudah pasti sebelum rencana dan dukungan mitra tersedia. |
| Pengujian | Bedakan kesesuaian fungsi melalui black box dan penerimaan melalui UAT. Rincian instrumen, responden, skenario, kriteria penerimaan dan penanganan temuan dijabarkan pada Bab 3. |

Arahan verifikasi transfer dapat ditelusuri pada [bimbingan Bu Ayu, 01:05:41 sampai 01:08:11](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BIMBINGAN/BU AYU/TRANSKRIP TEKS (TXT)/BIMBINGAN KE-1 (Bu Ayu)_WITH_TIMESTAMPS.txt:1387>). Rancangan pemeriksaan yang hanya mengandalkan gambar bukti belum menjawab kekhawatiran yang dibahas pada bagian tersebut.

## Bahasa dan penulisan

| Teks sekarang | Contoh perbaikan |
| --- | --- |
| “Penggunaan sistem berbasis web agar data dihimpun ...” | “Penggunaan sistem berbasis web memungkinkan data dihimpun secara terpusat.” |
| “Pada sisi pimpinan pusat memerlukan laporan ...” | “Pimpinan pusat memerlukan laporan penerimaan dari setiap cabang.” |
| “Dan koordinasi tenaga pengajar ...” | “Pada koordinasi tenaga pengajar, pencatatan jadwal masih ...” |
| “Lalu, koordinasi pergantian jadwal ...” | “Koordinasi pergantian jadwal ...” |
| “Dadri berbagai kendala ...” | “Berdasarkan kebutuhan operasional tersebut, ...” |
| “Beberapa metode alternatif seperti,.” | Hapus fragmen dan tulis perbandingan dalam kalimat lengkap. |
| “menimbulkan metodologis ...” | Hapus bersama kesimpulan mutlak tentang Scrum; persoalannya bukan hanya pilihan kata. |
| “Manajemen pusat untuk memantau ...” | “Manajemen pusat diharapkan dapat memantau ...” |
| “Pada Gambar 1.1 merupakan ...” | “Gambar 1.1 menunjukkan ...” |
| “riwayat data tetap terjaga” setelah “menjaga” | “Pencatatan digital diharapkan mendukung penelusuran riwayat data.” |
| “dashboard”, “multi-cabang”, “antar-peran” | Seragamkan menjadi “dasbor”, “multicabang”, dan “antarperan” dalam uraian berbahasa Indonesia. |
| “(12 pt, 1.5 spasi, bold)” dan “(optional)” | Terapkan pengaturannya pada dokumen dan keluarkan petunjuk template dari teks akhir. |

Paragraf pembuka bab, pengantar manfaat, manfaat peneliti, serta beberapa uraian fishbone masih hanya satu kalimat. Sesuai aturan akademik proyek, gabungkan dengan paragraf yang terkait atau tambahkan kalimat penjelas yang relevan; jangan menambah kalimat kosong untuk memenuhi jumlah.

Teks terbaru memuat dua belas paragraf latar belakang, bukan sebelas seperti nama draf terdahulu. Tidak terdapat kewajiban jumlah paragraf tertentu pada bagian template dan arahan pembimbing yang diperiksa, sehingga jumlah paragraf bukan ukuran kelayakan; yang perlu dinilai adalah alur dan kecukupan bukti.

## Manfaat, dampak dan kerangka

Manfaat masih menggunakan bentuk seolah hasilnya sudah tercapai, seperti “mempercepat alur kerja” dan “menggantikan buku besar”. Untuk proposal, gunakan “diharapkan membantu” atau “berpotensi”, lalu nyatakan pengukuran apabila akan menyimpulkan efisiensi setelah pengujian.

Pernyataan permintaan pasar cukup tinggi dan sebagian besar lembaga masih manual memerlukan data pasar yang tidak disertakan. Peluang pengembangan SaaS tetap dapat dibahas sebagai potensi yang memerlukan kajian lanjutan, sedangkan manfaat terhadap kualitas layanan atau kinerja keuangan tidak perlu dijanjikan melampaui evaluasi yang direncanakan.

Fishbone dapat dipertahankan sebagai alat identifikasi masalah, dengan penyebab yang didukung bukti dan risiko yang diberi status jelas. Namun, bagian 1.7 pada template prototipe meminta alur identifikasi, pengumpulan data, analisis, perancangan, implementasi, pengujian dan evaluasi; teks terbaru belum menjelaskan alur tersebut atau pelaksanaan tujuh tahap PxP.

Gambar aktual tidak ikut terbawa pada teks lampiran, sehingga tata letak dan isi visualnya belum dinilai pada pemeriksaan ini. Uraian “menghitung baris di buku”, kehilangan data karena pergantian staf, serta waktu rekonsiliasi yang lama perlu didukung bukti sebelum dijadikan penyebab pasti dalam diagram.

## Acuan panduan dan hasil penyempurnaan

[Panduan kepenulisan ITK 2025](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/PANDUAN TA/[2025] B PANDUAN KEPENULISAN TUGAS AKHIR ITK.pdf>) menetapkan bahasa baku dan penggunaan kalimat pasif pada hlm. 12, serta Harvard dan konsistensi daftar pustaka pada hlm. 16. Ketentuan minimal sepuluh referensi dan 70% terbitan sepuluh tahun terakhir berada pada hlm. 4; pemenuhannya dihitung untuk proposal, bukan dari jumlah PDF yang disimpan.

[Panduan TA dan SITASI SI ITK 2026](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/PANDUAN TA/Panduan TA dan SITASI - Sistem Informasi ITK 2026.pdf>) menjelaskan prototipe dan TKT 5 pada hlm. 4, serta rubrik proposal prototipe yang memuat minimal sepuluh pustaka lima tahun terakhir pada hlm. 80, yaitu halaman PDF 87. “SITASI” pada panduan ini merupakan aplikasi administrasi TA, sehingga ketentuan gaya kutipan tidak disimpulkan dari namanya.

[Template prototipe](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/TEMPLATE TA/Copy of Template Laporan TA 2025 PROTOTIPE SI.docx.pdf>) meminta kerangka tahapan pelaksanaan, bukan mewajibkan fishbone sebagai satu-satunya kerangka. Pengaturan huruf, margin, spasi, penomoran dan posisi gambar perlu diperiksa kembali setelah naskah dipindahkan ke Word, karena teks tempelan tidak menyimpan seluruh informasi tersebut.

Sebagai pemenuhan permintaan sebelumnya, tersedia [draf penyempurnaan Bab 1](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB 1 - PENDAHULUAN (PENYEMPURNAAN 2026-10-24).md>) yang mempertahankan susunan template dan sebelas paragraf latar belakang. Draf pembanding itu membatasi fakta pada bukti yang dapat ditelusuri, menyertakan dua belas referensi termasuk sepuluh terbitan 2024 sampai 2026, dan menandai rincian rancangan sebagai usulan yang perlu divalidasi; draf tersebut tidak mengesahkan angka, SOP, atau komitmen mitra yang belum terkonfirmasi.

Prioritas revisi adalah meluruskan pembenaran metode, mengonfirmasi alur penerimaan dan kewenangan bank, lalu menyeragamkan fakta kasus serta istilah fitur. Setelah itu, rapikan bahasa, daftar pustaka, lampiran wawancara dan format Word agar naskah siap dibawa ke bimbingan berikutnya.
