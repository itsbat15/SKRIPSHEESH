# Catatan pembimbing untuk Bab 3 versi copy

Pemeriksaan dilakukan pada 25 Oktober 2026 terhadap seluruh naskah Bab 3 versi copy, dari pembuka sampai jadwal. Hasil ini berupa koreksi dan contoh perbaikan; naskah sumber tidak ditimpa oleh pemeriksa.

Berkas sempat berubah selama pemeriksaan pada beberapa sitasi Fikri, sehingga laporan ini mengacu pada salinan tetap NASKAH YANG DIPERIKSA.md. Lokator baris pada temuan diarahkan ke salinan tersebut agar tetap tepat jika berkas kerja kembali disunting.

Lokator menggunakan subbab, nomor paragraf prosa pada subbab tersebut, dan baris Markdown. Nomor halaman cetak naskah belum tersedia, sedangkan nomor cetak dan nomor halaman PDF panduan dibedakan agar pemeriksaan manual dapat dilakukan.

## G.1 Ringkasan kesiapan naskah

**Nilai pendampingan: 72 dari 100, dengan kategori Perlu Revisi Mayor yang terarah sebelum pengajuan sempro.** Nilai ini menilai draf Bab 3 yang tersedia, bukan nilai resmi ITK, prediksi kelulusan, atau penilaian keseluruhan proposal.

| Aspek penilaian pendampingan | Nilai maksimum | Nilai | Pertimbangan |
| :--- | ---: | ---: | :--- |
| Struktur dan kelengkapan artefak | 20 | 19 | Enam subbab, dua puluh tabel, dan sepuluh gambar tersedia |
| Kejelasan metode dan bukti kebutuhan | 20 | 14 | PxP tersedia; status kegiatan dan prosedur tambahan perlu diperjelas |
| Konsistensi rancangan sistem | 20 | 14 | Ada masalah otorisasi, status pembayaran, kapasitas, dan pencocokan |
| Rencana pengujian dan evaluasi | 20 | 15 | Kasus serta tugas tersedia; EP/BVA, peserta, satuan UAT, dan beban belum lengkap |
| Bahasa dan ketepatan penggunaan sumber | 20 | 10 | Gaya terlalu padat, klaim berlebih, dan beberapa atribusi sumber berubah |
| Jumlah | 100 | 72 | Format fisik Word/PDF belum dinilai |

Kekuatan utama terletak pada struktur yang sesuai template, hubungan kebutuhan dengan pengujian, dan tersedianya artefak rancangan. Kerangka tersebut dapat dipertahankan sehingga revisi tidak memerlukan penyusunan ulang Bab 3 dari awal.

| Kekuatan utama | Bukti pada naskah |
| :--- | :--- |
| Struktur dan artefak lengkap | Enam subbab utama, 20 tabel, 10 gambar, serta penomoran berurutan |
| Proses pengembangan dapat ditelusuri | Tujuh tahap PxP, empat iterasi, log, dan kriteria pemeriksaan |
| Kebutuhan terhubung ke evaluasi | 14 KF, 14 US, 14 kelompok PU, 14 tugas UAT, dan lampiran 33 kasus BB |

| Kelemahan utama | Dampak |
| :--- | :--- |
| Narasi tidak selalu sama dengan model | Token sesi, pembayaran tunai, dan kapasitas dapat dipahami secara keliru |
| Klaim melampaui bukti yang ditunjukkan | Kata menjamin dan terbukti efektif seolah menyatakan hasil sudah teruji |
| Tambahan teknik belum dijabarkan | EP, BVA, pengujian beban, dan kepuasan belum mempunyai prosedur lengkap |
| Pilihan teknologi dan antarbagian belum seluruhnya selaras | Laravel 11 serta peran pemeriksa pada Bab 1 perlu ditinjau |
| Bahasa dan atribusi sumber terlalu berat atau berubah | Contoh penelitian disebut standar dan objek ruang rapat disebut pendidikan |

Pemeriksaan bentuk tidak menemukan paragraf prosa satu kalimat, kata ganti orang pertama, kalimat berawal angka, atau dash panjang. Ditemukan satu kalimat lebih dari empat puluh kata; masalah bahasa yang lebih luas justru terletak pada pemilihan istilah dan penguatan klaim yang tidak diperlukan.

### Dasar penilaian dan batas informasi

Rubrik seminar proposal prototipe berada pada cetak 80 sampai 81/PDF 87 sampai 88 Panduan SI 2026. Rubrik sidang pada cetak 82 sampai 83/PDF 89 sampai 90 digunakan hanya untuk menunjukkan bukti akhir yang kelak diperlukan, sehingga ketiadaan hasil dan kesimpulan pada tahap proposal tidak dinilai sebagai kesalahan.

Ketentuan minimum 70 persen referensi sepuluh tahun terakhir tidak ditemukan sebagai aturan eksplisit pada bagian panduan yang diperiksa. Kriteria tersebut dapat dipakai sebagai permintaan tambahan pengguna, tetapi tidak dikutip seolah merupakan pasal ITK; rubrik prototipe secara eksplisit menyebut dukungan referensi lima tahun terakhir dan minimal sepuluh pustaka pada indikator Sangat Baik.

## G.2 Matriks keselarasan antarbagian

Pembandingan menggunakan tiga rumusan masalah dan tujuan pada Bab 1 SITASI LANGSUNG yang tersedia sebagai acuan antarbab. Status ini perlu diperbarui jika mahasiswa menetapkan berkas Bab 1 lain sebagai versi final.

| Rumusan masalah dan tujuan | Batasan yang berkaitan | Metode dan rancangan Bab 3 | Hasil yang harus dihasilkan | Kesimpulan yang kelak dapat ditarik | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RM/Tujuan 1: integrasi pendaftaran, pembayaran, dan jadwal delapan cabang | Dua peran dan pembatasan cabang | PxP; KF-01 sampai KF-10, KF-14; kelas, tagihan, serta pembayaran | Hasil integrasi dan uji fungsi termasuk tunai, transfer, kapasitas, dan akses | Kesesuaian integrasi berdasarkan fungsi yang benar-benar diuji | Kurang Selaras: peran pemeriksa Bab 1 masih Admin Cabang, sedangkan Bab 3 Super Admin |
| RM/Tujuan 2: dasbor pusat dan pencocokan penerimaan dengan mutasi | Tanpa gateway; pencocokan dibatasi satu sumber penuh | KF-11 sampai KF-13; pemuatan saat permintaan dan pencocokan manual | Rekap yang sesuai sumber dan bukti pencocokan tanpa penghitungan ganda | Kesesuaian pemantauan serta pencocokan pada cakupan yang diuji | Kurang Selaras: istilah real-time dan pencocokan otomatis perlu disamakan |
| RM/Tujuan 3: kesesuaian fungsi melalui Black Box dan UAT | Pengelola dan admin sebagai pengguna | 33 kasus pendamping dan 14 tugas UAT; EP/BVA baru disebut | Hasil aktual, cakupan, kegagalan, uji ulang, dan keputusan peserta | Tingkat kesesuaian berdasarkan satuan evaluasi yang jelas | Kurang Selaras: penerimaan tugas bercampur dengan kepuasan dan implikasi efisiensi |

Hasil pengujian dan kesimpulan belum tersedia pada berkas yang diajukan dan wajar belum tersedia pada proposal. Keselarasan hasil dengan kesimpulan baru dapat dinilai setelah pelaksanaan menghasilkan data; tidak ada hasil yang diasumsikan lulus dalam penilaian ini.

### Ketercakupan seluruh subbab

| Bagian | Penilaian ringkas |
| :--- | :--- |
| Pembuka dan 3.1 | Struktur sesuai; bahasa dan klaim efektivitas perlu disederhanakan |
| 3.1.1 | Objek jelas; konteks empiris lebih baik dijelaskan dengan kegiatan dan sumber |
| 3.1.2 | Dua peran dan WhatsApp manual tersedia; istilah verifikasi dan kapasitas perlu konsisten |
| 3.1.3 | PxP sesuai pengembangan individual; nama Fikri dan atribusi efektivitas perlu diperbaiki |
| 3.1.4 | TKT, produk, artikel, dan HKI ada; pencapaian tetap memerlukan bukti evaluasi |
| 3.2 | Diagram dan tahap tersedia; sumber adaptasi dapat dirapikan |
| 3.3.1 | Sumber dan topik tersedia; bukti observasi serta prosedur triangulasi perlu diperjelas |
| 3.3.2 | Empat iterasi beserta dependensi tersedia; dasar estimasi awal perlu dijelaskan |
| 3.3.3 | Tugas, versi, dan data uji tersedia; kriteria selesai harus sesuai bukti pelaksanaan |
| 3.3.4 | Perancangan proses dan data memadai; hindari jaminan hasil sebelum pengujian |
| 3.3.5 | TDD dan refaktorisasi ada; pengujian unit tidak menjamin seluruh perilaku |
| 3.3.6 | Kasus tersedia; EP/BVA dan syarat penghentian atau pengulangan perlu konkret |
| 3.3.7 | Log dan perbandingan waktu tersedia; selisih durasi bukan bukti keunggulan metode |
| 3.3.8 | UAT cukup terstruktur; peserta, satuan, bantuan, keputusan, dan instrumen persepsi perlu ditetapkan |
| 3.4 | Model relevan; kalimat jaminan penerapan perlu dibatasi |
| 3.4.1 | Alokasi, kas, setoran, serta bank terpisah; manual dan otomatis harus disamakan |
| 3.4.2 | Empat belas KF dan sembilan KNF ada; kapasitas kelompok dan ruang harus dibedakan |
| 3.4.3 | Matriks akses ada; uraian token dan batas Super Admin perlu dikoreksi |
| 3.4.4 | Empat belas cerita dan matriks tersedia; kata standar dan tolok ukur perlu ditinjau |
| 3.4.5 | Diagram dan skenario ada; artikel terapan bukan standar UML |
| 3.4.6 | Dua puluh tiga tabel terpetakan; normalisasi dan pembayaran sah perlu penegasan |
| 3.4.7 | Enam rancangan layar tersedia dan bertanda simulasi; istilah status harus tetap sama |
| 3.5 dan 3.5.1 | Arsitektur tersedia; dukungan versi dan rencana pengujian beban perlu diperjelas |
| 3.5.2 | Perangkat pengembang terinci; perangkat pengguna dan peladen masih rencana |
| 3.5.3 | Versi antarmuka terdata; sumber versi layanan serta pilihan MySQL belum tunggal |
| 3.5.4 | Penyimpanan privat dan zona waktu jelas; cadangan harus memuat isi data |
| 3.6 | Jadwal mingguan diperbolehkan; pemetaan literatur, penyiapan, dan estimasi perlu dilengkapi |

## G.3 Catatan koreksi per kategori dan subbab

Temuan disusun mengikuti urutan naskah agar dapat dikerjakan dari bagian awal sampai akhir. Rujukan panduan menunjukkan tuntutan akademik atau kelengkapan bagian; alasan teknis khusus diperiksa melalui dokumen rancangan, sumber penelitian, dan dokumentasi primer terkait.

### TEMUAN 01

**Kategori:** Bahasa. **Prioritas:** Penting. **Letak:** 3.1.1 Objek dan Konteks Pengembangan, paragraf 1; [baris 13](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:13>).

**Teks semula:** “Temuan lapangan tersebut mengonfirmasi urgensi unifikasi basis data guna menjembatani pengelolaan data siswa, pengaturan jadwal pembelajaran, serta rekonsiliasi kas dalam satu ekosistem digital.”

**Permasalahan:** Kosakata seperti unifikasi, urgensi, dan ekosistem digital bertumpuk tanpa menambah rincian pekerjaan. Kalimat belum menjelaskan informasi lapangan apa yang menghubungkan pencatatan cabang dan kebutuhan pusat.

**Acuan:** Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20.

**Revisi yang disarankan:** “Wawancara pengelola dan staf administrasi digunakan untuk memahami pencatatan siswa, jadwal, dan pembayaran pada cabang. Informasi tersebut menjadi dasar perancangan penyimpanan data terpusat yang dapat digunakan oleh petugas cabang dan pengelola pusat.”

**Langkah perbaikan:** Sebutkan kegiatan, data, dan pelaksana secara langsung. Kurangi ungkapan abstrak pada paragraf pembuka serta bagian lain yang mempunyai pola serupa.

### TEMUAN 02

**Kategori:** Sitasi. **Prioritas:** Penting. **Letak:** 3.1.2 Ruang Lingkup dan Pengguna Prototipe, paragraf 1; [baris 17](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:17>).

**Teks semula:** “Model pembatasan hak akses berbasis lokasi kerja dan peran manajerial semacam ini terbukti efektif”

**Permasalahan:** Keberadaan rancangan akses pada penelitian lain belum dengan sendirinya membuktikan efektivitas ARTHA atau semua organisasi multicabang. Ukuran efektivitas dan batas penerapan penelitian sumber perlu disebutkan bila klaim tersebut dipertahankan.

**Acuan:** Panduan ITK 2025, §3.7(a dan b), cetak 16/PDF 24; Template Prototipe, §3.4, cetak 7/PDF 20.

**Revisi yang disarankan:** “Pemisahan akses cabang dan pemantauan pusat dibahas pada Ahadi dkk. (2025) serta Thiovanda (2026). Pada ARTHA, pembagian ini digunakan untuk merancang kewenangan Admin Cabang dan Super Admin.”

**Langkah perbaikan:** Periksa bagian sumber yang dirujuk, lalu gunakan pernyataan tentang fitur atau hasil yang benar-benar dilaporkan. Hindari mengubah contoh penerapan menjadi kesimpulan umum tentang efektivitas.

### TEMUAN 03

**Kategori:** Sitasi. **Prioritas:** Penting. **Letak:** 3.1.3 Pendekatan Pengembangan Prototipe, paragraf 1; [baris 25](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:25>).

**Teks semula:** “(Fikri & Arthawan, 2020; Sidiq dkk., 2025; Apriyanti dkk., 2024)”

**Permasalahan:** Versi terbaru memakai 2020, sedangkan daftar pustaka pendamping mengikuti metadata penerbit 2021; nama penulis kedua juga tidak konsisten. Penerbit mencatat I Putu Deny Arthawan Sugih Prabowo, publikasi 4 Januari 2021, dan edisi berlabel 2020. Tahun edisi dapat dijelaskan, tetapi pilihan metadata harus konsisten antara sitasi dan daftar pustaka.

**Acuan:** Panduan ITK 2025, §3.7(a dan b), cetak 16/PDF 24.

**Revisi yang disarankan:** “Penerapan PxP pada sistem informasi dibahas oleh Fikri dan Arthawan Sugih Prabowo (2021), Sidiq dkk. (2025), dan Apriyanti dkk. (2024). Penelitian tersebut digunakan sebagai pembanding pelaksanaan, bukan bukti otomatis efektivitas ARTHA.”

**Langkah perbaikan:** Selaraskan nama melalui pengelola referensi dan [metadata penerbit](https://journal.umpo.ac.id/index.php/multitek/article/view/2568). Periksa seluruh kemunculan Fikri pada 3.1.3, 3.3.1, 3.3.4, dan 3.4.4.

### TEMUAN 04

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.1.4 Luaran yang Ditargetkan, paragraf 1; [baris 29](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:29>).

**Teks semula:** “TKT) Level 5, yakni teknologi telah divalidasi dan diuji coba pada lingkungan operasional yang sesungguhnya”

**Permasalahan:** Target TKT 5 telah dicantumkan, tetapi kalimat ini dapat dibaca sebagai kewajiban penerapan produksi penuh. Panduan SI menyebut TKT 5 dan evaluasi mitra atau calon pengguna; cakupan pilot serta bukti pencapaiannya tetap perlu dijelaskan.

**Acuan:** Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88.

**Revisi yang disarankan:** “Prototipe ditargetkan mencapai TKT 5 sesuai ketentuan tugas akhir. Pencapaiannya akan didukung melalui evaluasi bersama mitra atau calon pengguna pada lingkungan pengujian yang relevan dengan proses operasional Artha.”

**Langkah perbaikan:** Tetapkan lokasi atau lingkungan evaluasi, peran mitra, data uji, dan bukti keputusan. Jangan menyamakan target proposal dengan pencapaian yang telah dibuktikan.

### TEMUAN 05

**Kategori:** Tabel-Gambar. **Prioritas:** Penyempurnaan. **Letak:** 3.2 Tahapan Pembuatan Prototipe, keterangan sumber Gambar 3.1; [baris 41](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:41>).

**Teks semula:** “Sumber: Dzhurov dkk. (2009), telah disesuaikan”

**Permasalahan:** Sumber dan status adaptasi sudah ada, tetapi susunannya dapat mengikuti contoh pedoman secara lebih langsung. Label sumber tidak perlu diganti menjadi klaim bahwa seluruh diagram merupakan gambar asli artikel.

**Acuan:** Panduan ITK 2025, §3.5(k dan l), cetak 15/PDF 23.

**Revisi yang disarankan:** “Sumber: (Dzhurov dkk., 2009, telah diolah). Penambahan UAT dan penyiapan luaran dijelaskan pada paragraf pengantar gambar.”

**Langkah perbaikan:** Sesuaikan format keterangan sumber pada Gambar 3.1. Pertahankan penjelasan bahwa diagram telah diadaptasi untuk penelitian ARTHA.

### TEMUAN 06

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.1 Penggalian Kebutuhan (*Requirements*), paragraf 7; [baris 108](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:108>).

**Teks semula:** “Pengamatan langsung terhadap alur kerja kasir dan staf administrasi juga dicatat secara sistematis”

**Permasalahan:** Observasi dan pemeriksaan dokumen fisik belum ditunjukkan bukti pelaksanaannya pada berkas yang diperiksa. Bentuk pasif tanpa kata akan memang lazim untuk prosedur proposal, tetapi status kegiatan yang sudah dan belum dilakukan perlu dibedakan.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88.

**Revisi yang disarankan:** “Contoh dokumen yang diizinkan mitra akan diperiksa untuk melengkapi keterangan wawancara. Apabila dilakukan pengamatan langsung, waktu, kegiatan, dan hasil pengamatan akan dicatat pada lembar observasi.”

**Langkah perbaikan:** Jika kegiatan sudah dilakukan, lampirkan tanggal, objek, dokumen yang diizinkan, serta hasilnya. Jika belum, tuliskan sebagai rencana; jangan menganggap transkrip otomatis membuktikan observasi atau akses mutasi.

### TEMUAN 07

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.1 Penggalian Kebutuhan (*Requirements*), paragraf 8; [baris 110](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:110>).

**Teks semula:** “reduksi data, kategorisasi tematik, dan triangulasi sumber guna mengeliminasi inkonsistensi informasi”

**Permasalahan:** Istilah analisis baru belum dijelaskan cara pelaksanaannya. Triangulasi digunakan untuk memeriksa kesesuaian dan perbedaan informasi, bukan memastikan seluruh perbedaan dapat dieliminasi.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20.

**Revisi yang disarankan:** “Informasi wawancara akan dikelompokkan berdasarkan topik dan dibandingkan antarsumber. Perbedaan keterangan akan dibahas kembali dengan informan terkait, kemudian hasil klarifikasinya digunakan untuk merumuskan kebutuhan sistem.”

**Langkah perbaikan:** Tentukan unit informasi, kategori, sumber pembanding, dan cara menangani perbedaan. Siapkan contoh satu baris kutipan, kode tema, hasil klarifikasi, serta kebutuhan yang diturunkan.

### TEMUAN 08

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.2 Perencanaan (*Planning*), paragraf 1; [baris 118](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:118>).

**Teks semula:** “berlandaskan metrik durasi historis dari pengerjaan fitur serupa”

**Permasalahan:** Data historis pengembang belum diperlihatkan. PxP mengizinkan perkiraan terbaik bila data sebelumnya belum tersedia, sehingga rencana awal tidak perlu mengandaikan adanya metrik historis.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Dzhurov dkk. (2009), cetak 255/PDF 4 pada sumber lokal.

**Revisi yang disarankan:** “Estimasi awal disusun berdasarkan rincian tugas dan perkiraan waktu pengerjaannya. Setelah iterasi pertama, estimasi pekerjaan sejenis diperbarui menggunakan catatan durasi aktual.”

**Langkah perbaikan:** Tambahkan format tugas, estimasi jam, dasar estimasi, dan durasi aktual. Gunakan data proyek sebelumnya hanya jika catatan tersebut memang tersedia.

### TEMUAN 09

**Kategori:** Bahasa. **Prioritas:** Penyempurnaan. **Letak:** 3.3.2 Perencanaan (*Planning*), paragraf 1; [baris 118](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:118>).

**Teks semula:** “Pengembang mengestimasi durasi kerja setiap tugas secara terperinci”

**Permasalahan:** Kalimat aktif ini dapat dipahami, tetapi panduan mengarahkan penyajian materi dengan kalimat pasif. Penyesuaian dapat difokuskan pada uraian prosedur tanpa membuat penjelasan aktor dan tindakan pada skenario menjadi kabur.

**Acuan:** Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20.

**Revisi yang disarankan:** “Durasi setiap tugas diperkirakan berdasarkan rincian pekerjaan yang akan dilakukan. Estimasi kemudian diperbarui menggunakan catatan durasi aktual ketika tersedia.”

**Langkah perbaikan:** Tinjau kalimat dengan subjek pengembang pada uraian metode dan ubah jika lebih sesuai dengan kaidah panduan. Nama aktor tetap diperlukan dalam tabel skenario untuk menjelaskan kewenangan.

### TEMUAN 10

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.5 Implementasi (*Implementation*), paragraf 2; [baris 163](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:163>).

**Teks semula:** “Fokus pengujian unit pada aturan kritis ini menjamin keandalan kalkulasi sistem”

**Permasalahan:** TDD dan pemilihan unit penting tidak menjamin seluruh perhitungan benar. Keberhasilan perlu dinilai dari kasus yang dijalankan, cakupan aturan, serta pengujian integrasi, termasuk permintaan serentak.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Dzhurov dkk. (2009), cetak 255 sampai 256/PDF 4 sampai 5.

**Revisi yang disarankan:** “Pengujian unit diprioritaskan pada sisa tagihan, kapasitas kelas, dan irisan jadwal. Hasilnya dilengkapi pengujian integrasi serta transaksi serentak untuk memeriksa perilaku ketika fungsi saling berhubungan.”

**Langkah perbaikan:** Tentukan kasus unit dan integrasi secara terpisah. Simpan contoh pengujian gagal, lulus, serta hasil setelah refaktorisasi sebelum menyatakan praktik TDD telah dilaksanakan.

### TEMUAN 11

**Kategori:** Metodologi. **Prioritas:** Sangat Penting. **Letak:** 3.3.6 Pengujian Sistem (*System Testing*), paragraf 1; [baris 173](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:173>).

**Teks semula:** “dengan teknik *Equivalence Partitioning* dan *Boundary Value Analysis*”

**Permasalahan:** Teknik disebutkan, tetapi belum ada partisi, batas, pemilihan data, serta cakupan teknik yang dapat diperiksa pada naskah. Daftar kasus normal dan tidak sah tidak otomatis menjadi penerapan EP/BVA yang dijelaskan dengan lengkap.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; ISTQB CTFL v4.0.1, §4.2.1 sampai §4.2.2, halaman 39 sampai 40.

**Revisi yang disarankan:** “Kasus uji disusun dari kelompok masukan sah dan tidak sah serta nilai di sekitar batas yang ditetapkan. Pembagian partisi, batas yang digunakan, data uji, dan keluaran yang diharapkan akan dicantumkan pada lampiran pengujian.”

**Langkah perbaikan:** Buat tabel variabel, aturan, partisi, batas, contoh nilai, kode BB, dan hasil yang diharapkan. Contoh kapasitas dua belas: penambahan dari sebelas menjadi dua belas diterima, sedangkan dari dua belas menjadi tiga belas ditolak. Pilih varian BVA dan lengkapi sumbernya; bila teknik tidak digunakan, hapus nama teknik tersebut.

### TEMUAN 12

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi, paragraf 2; [baris 219](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:219>).

**Teks semula:** “penetapan nama personel, representasi cabang, serta jadwal evaluasi yang dikoordinasikan secara resmi”

**Permasalahan:** Peran peserta sudah tepat, tetapi jumlah sasaran, cabang yang diwakili, alasan kecukupan, serta waktu belum konkret. Rencana ini dapat ditetapkan tanpa mengklaim semua cabang telah terwakili.

**Acuan:** Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88; Template Prototipe, §3.3, cetak 6/PDF 19.

**Revisi yang disarankan:** “Peserta UAT direncanakan mewakili Admin Cabang dan Super Admin yang menjalankan tugas terkait. Jumlah sasaran, cabang, pengalaman, dan jadwal akan ditentukan bersama mitra serta dicantumkan sebelum instrumen digunakan.”

**Langkah perbaikan:** Siapkan daftar sasaran, misalnya satu pemeriksa pusat dan dua admin dari dua cabang jika tersedia, sebagai usulan yang dikonfirmasi. Jelaskan bahwa pemilihan bertujuan memeriksa alur kerja, bukan menghasilkan generalisasi statistik delapan cabang.

### TEMUAN 13

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi, paragraf 9; [baris 252](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:252>).

**Teks semula:** “membagi jumlah skenario tugas yang diterima dengan total skenario tugas yang telah dievaluasi”

**Permasalahan:** Pembuka menyebut pelaksanaan per peserta dan versi, sedangkan rumus menyebut jumlah skenario. Satu tugas dapat dijalankan beberapa peserta dan diulang pada versi berbeda, sehingga unit serta penyebutnya perlu ditegaskan.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88.

**Revisi yang disarankan:** “Satuan analisis UAT adalah satu pelaksanaan tugas oleh satu peserta pada versi aplikasi tertentu. Persentase penerimaan dihitung dari pelaksanaan tugas yang diterima dibandingkan pelaksanaan tugas yang telah dievaluasi pada versi tersebut.”

**Langkah perbaikan:** Tambahkan kolom peserta, tugas, versi, bantuan, keputusan, dan alasan. Pisahkan hasil pertama dan uji ulang, laporkan tugas belum dievaluasi, serta jangan menghitung persetujuan berulang sebagai tugas baru yang meningkatkan persentase.

### TEMUAN 14

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi, paragraf 10; [baris 254](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:254>).

**Teks semula:** “kepuasan pengguna terhadap pemenuhan kebutuhan administrasi”

**Permasalahan:** Tugas diterima atau memerlukan perbaikan menunjukkan penerimaan alur, sedangkan kepuasan memerlukan pertanyaan atau instrumen tersendiri. Instrumen kepuasan belum dijelaskan.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88.

**Revisi yang disarankan:** “Pembahasan evaluasi difokuskan pada kesesuaian fungsi dan penerimaan alur administrasi oleh pengguna. Masukan mengenai kenyamanan dapat dihimpun melalui pertanyaan terbuka yang dicatat sebagai data kualitatif tambahan.”

**Langkah perbaikan:** Pilih antara membatasi simpulan pada penerimaan tugas atau menambah instrumen persepsi beserta pertanyaan, sumber, dan analisisnya. Jangan menyamakan persentase lulus tugas dengan skor kepuasan.

### TEMUAN 15

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.3.8 Pengujian Penerimaan Pengguna dan Analisis Evaluasi, paragraf 10; [baris 254](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:254>).

**Teks semula:** “justifikasi terkait efisiensi waktu kerja dianalisis sebagai implikasi kualitatif dari otomatisasi proses bisnis”

**Permasalahan:** Otomatisasi dapat menjadi alasan memperkirakan manfaat, tetapi tidak membuktikan penghematan waktu. Simpulan kualitatif tetap memerlukan data pendukung seperti wawancara atau pengamatan yang jelas.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; rubrik argumentasi dan penarikan kesimpulan prototipe, Panduan SI 2026, cetak 83/PDF 90.

**Revisi yang disarankan:** “Potensi pengurangan pekerjaan berulang akan dibahas berdasarkan perubahan alur dan masukan pengguna. Besarnya penghematan waktu hanya akan dinyatakan apabila dilakukan pengukuran pembanding dengan tugas yang setara.”

**Langkah perbaikan:** Jika efisiensi bukan tujuan yang diukur, gunakan istilah potensi manfaat. Jika akan diukur, tentukan tugas, kondisi awal, pelaksana, pengulangan, dan cara membandingkan waktunya.

### TEMUAN 16

**Kategori:** Bahasa. **Prioritas:** Penting. **Letak:** 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan, paragraf 3; [baris 280](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:280>).

**Teks semula:** “seluruh alokasi tagihan wajib bernilai ekuivalen dengan total uang yang disetorkan”

**Permasalahan:** Istilah ekuivalen dan fisik kas kurang tepat untuk menerangkan aturan yang juga berlaku pada transfer. Aturan alokasi perlu menyebut nominal pembayaran, terlepas dari kanalnya.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20.

**Revisi yang disarankan:** “Jumlah seluruh alokasi harus sama dengan nominal pembayaran yang dicatat. Setiap alokasi merujuk tagihan siswa dan cabang yang sama dengan transaksi pembayaran.”

**Langkah perbaikan:** Gunakan nominal pembayaran untuk aturan lintas kanal. Gunakan kas tunai hanya pada alur penerimaan dan penyerahan uang tunai.

### TEMUAN 17

**Kategori:** Bahasa. **Prioritas:** Penting. **Letak:** 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan, paragraf 4; [baris 282](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:282>).

**Teks semula:** “Super Admin memverifikasi kesesuaian data transfer terhadap mutasi rekening koran bank; transaksi yang valid akan disetujui”

**Permasalahan:** Kalimat lengkap pada paragraf ini berisi 43 kata setelah penyingkatan dilindungi. Kalimat tersebut menggabungkan pemeriksaan, keputusan, pengembalian, dan pengajuan ulang sehingga sulit diikuti.

**Acuan:** Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20; batas empat puluh kata merupakan ketentuan tambahan pengguna.

**Revisi yang disarankan:** “Kesesuaian transfer diperiksa oleh Super Admin berdasarkan mutasi rekening. Pengajuan yang sesuai disetujui untuk mengurangi sisa tagihan, sedangkan pengajuan yang perlu diperbaiki dikembalikan dengan alasan. Perbaikan diajukan sebagai transaksi baru yang tertaut pada riwayat sebelumnya.”

**Langkah perbaikan:** Pisahkan pemeriksaan, keputusan, dan tindak lanjut. Pertahankan istilah dikembalikan agar tidak berubah menjadi penolakan final yang tidak tersedia dalam model.

### TEMUAN 18

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan, paragraf 6; [baris 286](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:286>).

**Teks semula:** “rekening giro resmi bimbingan belajar”

**Permasalahan:** Jenis rekening giro tidak dibuktikan pada berkas yang diperiksa. Detail ini tidak diperlukan untuk menerangkan pencocokan dan dapat mengubah gambaran proses nyata jika rekening mitra berbeda.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Panduan SI 2026, §1.4.3, cetak 4/PDF 11; rubrik seminar proposal prototipe, cetak 80 sampai 81/PDF 87 sampai 88.

**Revisi yang disarankan:** “Dana yang telah diterima pusat dapat disetorkan ke rekening resmi yang ditetapkan mitra. Rekening tujuan, tanggal, nominal, dan bukti setor dicatat untuk pemeriksaan berikutnya.”

**Langkah perbaikan:** Gunakan istilah rekening resmi sampai jenis rekening dikonfirmasi. Catat jenis rekening hanya jika relevan dan tersedia bukti yang diizinkan.

### TEMUAN 19

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan, paragraf 7; [baris 288](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:288>).

**Teks semula:** “berada di luar lingkup pencocokan otomatis prototipe”

**Permasalahan:** Tabel 3.9 KF-13 dan Tabel 3.14 menyatakan pencocokan manual, sedangkan kalimat ini menyebut pencocokan otomatis. Pembentukan daftar atau validasi nominal dapat otomatis tanpa menjadikan keputusan pencocokan bank otomatis.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Template Prototipe, §3.5, cetak 7/PDF 20.

**Revisi yang disarankan:** “Pencocokan dilakukan secara manual oleh petugas dengan bantuan pemeriksaan nominal dan referensi pada sistem. Dana gabungan, biaya bank, serta selisih nominal dicatat untuk tindak lanjut di luar cakupan pencocokan prototipe.”

**Langkah perbaikan:** Samakan istilah pada 3.1.2, 3.4.1, KF-13, skenario, gambar arsitektur, dan batasan Bab 1. Tegaskan bahwa layanan API Laravel merupakan API internal aplikasi, bukan integrasi otomatis dengan bank.

### TEMUAN 20

**Kategori:** Sitasi. **Prioritas:** Penting. **Letak:** 3.4.1 Gambaran Proses Bisnis Berjalan dan Usulan, paragraf 8; [baris 290](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:290>).

**Teks semula:** “prinsip tata kelola sistem informasi terdistribusi (Ramadhan dan Widodo, 2026)”

**Permasalahan:** Sumber tersebut membahas perlakuan akuntansi pusat dan cabang berdasarkan SAK EP, bukan standar arsitektur sistem terdistribusi. Sumber Sudirman dan Tristianti juga merupakan penelitian penerapan rekonsiliasi, bukan dokumen standar pengendalian kas.

**Acuan:** Panduan ITK 2025, §3.7(a dan b), cetak 16/PDF 24; sumber lokal J08 dan J09.

**Revisi yang disarankan:** “Pemisahan pencatatan cabang dan penghimpunan rekap pusat merujuk Ramadhan dan Widodo (2026). Sudirman dan Tristianti (2021) digunakan sebagai pembanding pencocokan catatan penerimaan dengan catatan bank.”

**Langkah perbaikan:** Periksa kembali bagian pembahasan Ramadhan pada PDF 15 dan 17 serta Sudirman pada cetak 126 sampai 127. Ubah kata standar atau prinsip arsitektur menjadi keterangan isi penelitian yang benar-benar didukung.

### TEMUAN 21

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.4.2 Kebutuhan Fungsional dan Nonfungsional, paragraf 3; [baris 317](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:317>).

**Teks semula:** “terhadap batas maksimum kapasitas ruangan fisik”

**Permasalahan:** Kapasitas kelompok belajar dan kapasitas ruang fisik telah dipisahkan pada model data. Jika keterisian hanya dibandingkan dengan ruang, kelas dengan batas kelompok lebih kecil dapat menerima peserta melampaui kebijakannya.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; kamus data classes dan class_rooms, dokumen basis data pendamping.

**Revisi yang disarankan:** “Keterisian dihitung dari anggota aktif dibandingkan dengan batas peserta pada kelas. Batas kelas juga diperiksa agar tidak melampaui kapasitas ruang yang digunakan pada jadwal aktif.”

**Langkah perbaikan:** Gunakan classes.max_students untuk penambahan peserta dan class_rooms untuk kelayakan ruang. Uji contoh batas kelas sepuluh pada ruang dua belas serta penggantian ruang yang lebih kecil.

### TEMUAN 22

**Kategori:** Sitasi. **Prioritas:** Penting. **Letak:** 3.4.2 Kebutuhan Fungsional dan Nonfungsional, paragraf 3; [baris 317](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:317>).

**Teks semula:** “model kontrol alokasi sumber daya institusi pendidikan (Kabisatullah dan Noprisson, 2026)”

**Permasalahan:** Artikel RapaTrack membahas ruang rapat pada konteks perusahaan, bukan institusi pendidikan. Aturan kapasitas dapat menjadi pembanding lintas domain, tetapi identitas objek sumber tidak boleh diubah.

**Acuan:** Panduan ITK 2025, §3.7(a dan b), cetak 16/PDF 24; artikel RapaTrack, cetak 93 sampai 95/PDF 5 sampai 7.

**Revisi yang disarankan:** “Pemeriksaan kapasitas dan irisan waktu merujuk sebagai pembanding pada sistem manajemen ruang rapat oleh Kabisatullah dan Noprisson (2026). Penerapannya pada kelas Artha disesuaikan dengan batas peserta dan aturan penempatan mitra.”

**Langkah perbaikan:** Ganti deskripsi objek sumber dan jelaskan batas adaptasinya. Lokator pemeriksaan adalah cetak 94/PDF 6; afiliasi penulis universitas tidak menjadikan objek penelitiannya lembaga pendidikan.

### TEMUAN 23

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.4.2 Kebutuhan Fungsional dan Nonfungsional, paragraf 4; [baris 319](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:319>).

**Teks semula:** “Nilai ambang batas ini dikonfigurasi dalam rentang numerik yang fleksibel”

**Permasalahan:** Rentang nilai dan kondisi hampir penuh menjadi kurang jelas dibandingkan kamus data. Kata fleksibel tidak dapat digunakan untuk menentukan keluaran uji.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; kamus data classes.

**Revisi yang disarankan:** “Ambang hampir penuh ditetapkan sebagai jumlah sisa tempat antara satu dan kapasitas kelas. Peringatan ditampilkan ketika sisa tempat positif dan tidak melebihi ambang, sedangkan sisa nol menunjukkan kelas penuh.”

**Langkah perbaikan:** Tuliskan aturan rentang dan bedakan indikator penuh dari status aktif atau ditutup. Isi nilai aktual setelah dikonfirmasi, lalu uji tepat di atas ambang, pada ambang, dan saat penuh.

### TEMUAN 24

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.4.2 Kebutuhan Fungsional dan Nonfungsional, paragraf 5; [baris 321](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:321>).

**Teks semula:** “dua staf administrasi cabang yang berbeda membuka formulir pendaftaran secara simultan”

**Permasalahan:** Contoh tersebut tidak cocok dengan pembatasan akses jika kedua admin menambah peserta pada kelas yang sama dari cabang berbeda. Risiko serentak tetap ada pada dua sesi yang berwenang atas objek yang sama.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Tabel 3.11 dan skenario UC-03.

**Revisi yang disarankan:** “Dua sesi pengguna yang berwenang dapat mengajukan penempatan pada kelas yang sama ketika tersisa satu tempat. Kapasitas diperiksa kembali saat penyimpanan agar hanya satu penambahan tersimpan.”

**Langkah perbaikan:** Gunakan dua sesi pada cabang yang sama atau kombinasi akun yang memang berwenang. Hubungkan contoh dengan BB-07 dan jangan mengubah batas cabang demi membuat skenario serentak.

### TEMUAN 25

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.4.3 Peran Pengguna dan Matriks Hak Akses, paragraf 3; [baris 362](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:362>).

**Teks semula:** “identitas peran yang terenkripsi dalam token sesi”

**Permasalahan:** Ini tidak sesuai dengan rancangan Sanctum SPA berbasis kuki. Dokumentasi Sanctum menjelaskan penggunaan autentikasi sesi Laravel untuk SPA; tidak ada dasar bahwa peran dibawa sebagai token terenkripsi seperti yang diklaim.

**Acuan:** Template Prototipe, §3.5, cetak 7/PDF 20; dokumentasi resmi Laravel Sanctum bagian SPA Authentication.

**Revisi yang disarankan:** “Pengguna diidentifikasi melalui sesi yang sah. Peran dan penugasan cabang diperiksa pada peladen berdasarkan data akun sebelum akses terhadap objek diberikan.”

**Langkah perbaikan:** Samakan 3.4.3 dengan 3.5.1. Bedakan kuki sesi, token API, dan otorisasi; rujuk [dokumentasi Sanctum](https://laravel.com/framework/docs/12.x/sanctum) untuk mode yang dipilih.

### TEMUAN 26

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.4.3 Peran Pengguna dan Matriks Hak Akses, paragraf 3; [baris 362](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:362>).

**Teks semula:** “seluruh tindakan manipulasi data dibatasi secara mutlak pada cabang penugasan yang sah”

**Permasalahan:** Kalimat ini mencakup Super Admin, padahal peran tersebut dapat memantau lintas cabang dan menjalankan koreksi yang diotorisasi. Aturan cabang perlu disebut menurut peran.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Tabel 3.11 dan US-01.

**Revisi yang disarankan:** “Akses Admin Cabang dibatasi pada objek cabang penugasannya. Super Admin dapat menjalankan fungsi lintas cabang sesuai kewenangan yang ditetapkan dan seluruh tindakan penting dicatat.”

**Langkah perbaikan:** Periksa setiap kalimat yang memakai seluruh pengguna atau semua tindakan. Samakan aturan akses dengan Tabel 3.11, US-01, dan kasus pemeriksaan pusat.

### TEMUAN 27

**Kategori:** Bahasa. **Prioritas:** Penyempurnaan. **Letak:** 3.4.4 Cerita Pengguna (*User Story*) dan Kriteria Penerimaan, paragraf 1; [baris 368](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:368>).

**Teks semula:** “tolak ukur kelulusan fitur”

**Permasalahan:** Bentuk yang diperlukan adalah tolok ukur. Penyeragaman ejaan juga diperlukan pada non-tunai menjadi nontunai dan standarisasi menjadi standardisasi.

**Acuan:** Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20; EYD V sesuai rujukan bahasa panduan.

**Revisi yang disarankan:** “Kriteria penerimaan digunakan sebagai tolok ukur pemeriksaan fungsi. Istilah yang sama digunakan secara konsisten pada cerita pengguna dan kasus uji.”

**Langkah perbaikan:** Lakukan pencarian tiga bentuk tersebut di seluruh naskah dan perbaiki sesuai konteks. Periksa pula masukan, nominal, dan pembayaran sebagai pengganti istilah teknis yang tidak diperlukan.

### TEMUAN 28

**Kategori:** Sitasi. **Prioritas:** Penting. **Letak:** 3.4.5 Pemodelan Kasus Penggunaan (*Use Case*) dan Skenario, paragraf 1; [baris 414](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:414>).

**Teks semula:** “standar rekayasa perangkat lunak untuk sistem informasi manajemen (Ahadi dkk., 2025)”

**Permasalahan:** Artikel Ahadi merupakan contoh penerapan use case pada sistem hotel multicabang, bukan dokumen standar UML. Hal serupa terdapat pada penggunaan kata standar untuk bentuk user story dari artikel terapan.

**Acuan:** Panduan ITK 2025, §3.7(a dan b), cetak 16/PDF 24; Template Prototipe, §3.4, cetak 7/PDF 20.

**Revisi yang disarankan:** “Diagram kasus penggunaan digunakan untuk menggambarkan hubungan aktor dan fungsi sistem. Contoh penerapannya pada sistem multicabang dibahas oleh Ahadi dkk. (2025), sedangkan diagram ARTHA disusun sesuai kebutuhan mitra.”

**Langkah perbaikan:** Gunakan artikel terapan untuk contoh atau hasil penerapan. Jika memerlukan definisi standar UML atau teknik pengujian, gunakan sumber primer yang memang menetapkan definisinya.

### TEMUAN 29

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.4.6 Perancangan Basis Data, paragraf 1; [baris 443](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:443>).

**Teks semula:** “dua puluh tiga tabel relasional yang ternormalisasi”

**Permasalahan:** Pemisahan tabel saja tidak membuktikan normalisasi. Normal form, kunci calon, ketergantungan atribut, serta alasan penyimpanan nilai historis belum dijelaskan pada bukti yang diperiksa.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; Template Prototipe, §3.5, cetak 7/PDF 20.

**Revisi yang disarankan:** “Basis data dirancang dalam dua puluh tiga tabel yang memisahkan identitas, keanggotaan, tagihan, pembayaran, dan perpindahan kas. Kesesuaian kunci serta ketergantungan atribut akan diperiksa sebelum skema diimplementasikan.”

**Langkah perbaikan:** Jika mengklaim bentuk normal tertentu, lampirkan penelusuran kunci dan ketergantungan atribut. Jika belum dilakukan, gunakan frasa dirancang secara relasional dan hindari menyatakan normalisasi telah terbukti.

### TEMUAN 30

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.4.6 Perancangan Basis Data, paragraf 5; [baris 484](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:484>).

**Teks semula:** “dikurangi alokasi pembayaran yang telah diverifikasi”

**Permasalahan:** Model membedakan tunai recorded dan transfer verified, keduanya penerimaan sah. Penyebutan hanya yang telah diverifikasi dapat mengeluarkan pembayaran tunai dari penghitungan sisa tagihan.

**Acuan:** Template Prototipe, §3.4, cetak 7/PDF 20; kamus data payments dan dasar penghitungan laporan pada dokumen basis data.

**Revisi yang disarankan:** “Sisa tagihan dihitung dari nilai kewajiban dikurangi alokasi pembayaran tunai berstatus recorded dan transfer berstatus verified. Pengajuan submitted atau returned belum mengurangi sisa tagihan.”

**Langkah perbaikan:** Gunakan istilah pembayaran sah dengan definisi status yang eksplisit. Samakan kueri, dasbor, kuitansi, pencocokan, serta kasus BB-12 dan BB-15.

### TEMUAN 31

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.4.6 Perancangan Basis Data, paragraf 6; [baris 486](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:486>).

**Teks semula:** “diuji secara ketat melalui skrip migrasi terautomasi”

**Permasalahan:** Migrasi membentuk skema, tetapi tidak membuktikan seluruh aturan lintas tabel, konkurensi, dan perilaku di bawah beban riil. Naskah belum memperlihatkan bukti pengujian yang mendukung jaminan pada kalimat berikutnya.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Template Prototipe, §3.5, cetak 7/PDF 20.

**Revisi yang disarankan:** “Kunci, indeks, dan batas nilai akan diperiksa melalui migrasi serta data uji. Aturan lintas tabel dan perubahan serentak akan diperiksa melalui pengujian aplikasi pada lingkungan yang dicatat.”

**Langkah perbaikan:** Pisahkan pemeriksaan migrasi, pengujian integrasi, dan pengujian serentak. Laporkan bukti pelaksanaan saat tersedia dan ubah jaminan menjadi tujuan atau kriteria yang akan diperiksa.

### TEMUAN 32

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.5.1 Arsitektur Sistem, paragraf 6; [baris 575](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:575>).

**Teks semula:** “sebelum sesi pengujian beban dilakukan”

**Permasalahan:** Pengujian beban merupakan tambahan komitmen yang belum mempunyai alat, jumlah pengguna serentak, jumlah data, durasi, fungsi, dan batas penerimaan. Mengukur waktu satu permintaan tidak sama dengan menguji beban.

**Acuan:** Template Prototipe, §3.3, cetak 6/PDF 19; Template Prototipe, §3.5, cetak 7/PDF 20.

**Revisi yang disarankan:** “Waktu tanggapan fungsi utama akan diukur pada perangkat, jaringan, dan jumlah data uji yang dicatat. Pengujian beban akan ditambahkan apabila skenario pengguna serentak serta alat dan kriterianya telah ditetapkan.”

**Langkah perbaikan:** Pilih mengukur tanggapan tugas saja atau melengkapi rancangan pengujian beban. Jika memilih beban, tentukan skenario, tingkat beban, durasi, metrik, dan ambang bersama kebutuhan mitra.

### TEMUAN 33

**Kategori:** Bahasa. **Prioritas:** Penyempurnaan. **Letak:** 3.5.2 Perangkat Keras, paragraf 1; [baris 579](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:579>).

**Teks semula:** “perangkat keras workstation pengembang”

**Permasalahan:** Istilah workstation tidak diberi huruf miring dan mempunyai padanan yang mudah dipahami. Bentuk Diagram Use Case dan beberapa istilah generik lain juga perlu diseragamkan, tanpa memiringkan nama merek atau kode tabel secara sembarang.

**Acuan:** Panduan ITK 2025, §3.2(a sampai d), cetak 12/PDF 20.

**Revisi yang disarankan:** “Tabel 3.18 merangkum perangkat keras komputer pengembangan dan rencana perangkat uji pengguna. Rincian yang belum tersedia dilengkapi sebelum pelaksanaan pengujian.”

**Langkah perbaikan:** Gunakan komputer pengembangan atau stasiun kerja. Pada istilah generik yang tetap dipertahankan, berikan padanan saat pertama muncul dan cetak miring sesuai §3.2(c); nama produk seperti Laravel dan Next.js tetap sebagai nama produk.

### TEMUAN 34

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.5.3 Perangkat Lunak dan Versi Teknologi, paragraf 1; [baris 595](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:595>).

**Teks semula:** “Pemetaan versi perangkat lunak pada Tabel 3.19 diverifikasi secara langsung dari berkas konfigurasi dependensi sistem”

**Permasalahan:** Bukti lockfile antarmuka tidak membuktikan seluruh versi PHP, MySQL, atau layanan Laravel. Tabel juga menyebut dua versi MySQL sekaligus, sehingga lingkungan pengujian yang akan dipakai belum tunggal.

**Acuan:** Template Prototipe, §3.5, cetak 7/PDF 20.

**Revisi yang disarankan:** “Versi antarmuka dicatat dari berkas penguncian dependensi proyek. Versi PHP dan MySQL dicatat dari layanan yang dijalankan, sedangkan versi Laravel dicatat dari proyek layanan dan Composer.”

**Langkah perbaikan:** Bedakan terpasang pada komputer, dipilih untuk rancangan, dan benar-benar dijalankan saat uji. Pilih satu versi MySQL untuk evaluasi dan catat patch serta InnoDB; berkas Composer proyek layanan belum ditemukan pada ruang kerja yang diperiksa.

### TEMUAN 35

**Kategori:** Substansi. **Prioritas:** Sangat Penting. **Letak:** 3.5.3 Perangkat Lunak dan Versi Teknologi, paragraf 2; [baris 610](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:610>).

**Teks semula:** “stabilitas dukungan jangka panjang (Laravel, t.t.-c)”

**Permasalahan:** Tabel menyebut Laravel 11, sedangkan dukungan keamanan resminya telah berakhir pada 12 Maret 2026. Kompatibilitas PHP tidak berarti versi Laravel masih didukung pada tanggal pemeriksaan, 25 Oktober 2026.

**Acuan:** Template Prototipe, §3.5, cetak 7/PDF 20; Laravel, Support Policy, diperiksa 25 Oktober 2026.

**Revisi yang disarankan:** “Versi layanan akan dipilih berdasarkan kompatibilitas PHP dan masa dukungan keamanan yang masih berlaku. Versi yang digunakan pada implementasi dicatat melalui Composer dan berkas penguncian dependensi.”

**Langkah perbaikan:** Periksa [kebijakan rilis resmi Laravel](https://laravel.com/framework/docs/12.x/releases). Pilih versi yang masih didukung untuk lingkungan evaluasi atau jelaskan pembatasan penggunaan versi lama, kemudian perbarui tabel tanpa menyatakan peningkatan telah dilakukan.

### TEMUAN 36

**Kategori:** Substansi. **Prioritas:** Penting. **Letak:** 3.5.4 Lingkungan Implementasi dan Pengujian, paragraf 6; [baris 626](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:626>).

**Teks semula:** “ekspor skema basis data dan direktori penyimpanan berkas bukti bayar”

**Permasalahan:** Ekspor skema saja tidak memulihkan baris siswa, tagihan, pembayaran, dan hubungan bukti. Rencana pencadangan perlu eksplisit mencakup struktur dan isi basis data.

**Acuan:** Template Prototipe, §3.5, cetak 7/PDF 20; KNF-08 dan BB-28.

**Revisi yang disarankan:** “Cadangan mencakup struktur serta isi basis data dan berkas bukti yang berkaitan. Pemulihan dilakukan pada lingkungan uji terpisah, kemudian relasi transaksi dan akses berkas diperiksa kembali.”

**Langkah perbaikan:** Cantumkan cakupan data, frekuensi, lokasi, hak akses, versi, serta langkah pemulihan. Gunakan BB-28 untuk memeriksa data dan berkas setelah dipulihkan.

### TEMUAN 37

**Kategori:** Metodologi. **Prioritas:** Penting. **Letak:** 3.6 Jadwal Pembuatan Prototipe, paragraf 2; [baris 632](<C:/Users/ARIEL/OneDrive - MSFT/Documents/ARTHA/BAB3_PENDUKUNG_2026-10-25/REVIEW_COPY_2026-10-25/NASKAH YANG DIPERIKSA.md:632>).

**Teks semula:** “Penomoran minggu (M1 hingga M12) dihitung secara relatif berdasarkan tanggal sepakatan pelaksanaan di lapangan.”

**Permasalahan:** Tabel mingguan diperbolehkan template, sehingga minggu relatif bukan pelanggaran. Yang perlu dilengkapi adalah dasar alokasi, penegasan kegiatan yang sudah dilakukan, serta studi literatur dan penyiapan penerapan yang belum terlihat sebagai baris tersendiri.

**Acuan:** Template Prototipe, §3.6, cetak 7/PDF 20.

**Revisi yang disarankan:** “Minggu pertama dihitung dari tanggal mulai yang akan disepakati bersama pembimbing dan mitra. Kegiatan yang telah dilaksanakan ditandai, sedangkan studi literatur lanjutan, pengembangan, evaluasi, dan penyiapan prototipe dicantumkan dalam jadwal.”

**Langkah perbaikan:** Perbaiki sepakatan menjadi kesepakatan. Tambahkan atau petakan kegiatan literatur dan penyiapan penerapan, lalu lengkapi estimasi tugas sebelum menetapkan bahwa empat iterasi cukup.

### Catatan lintas bagian yang tetap perlu diperhatikan

Bahasa proposal dapat menjelaskan prosedur menggunakan bentuk pasif tanpa mengulang kata akan pada setiap kalimat. Yang perlu dibatasi ialah pernyataan hasil seperti telah tervalidasi, ternormalisasi, terbukti, atau menjamin ketika bukti pelaksanaan tidak disertakan.

Status pembayaran dan pengajuan perlu diseragamkan antara dikembalikan atau returned, disetujui atau verified, serta tunai recorded. Istilah ditolak pada uraian layar dapat dibaca sebagai penolakan final; gunakan dikembalikan untuk diperbaiki jika tindakan yang dimaksud masih membuka pengajuan ulang.

Tidak perlu menambahkan populasi siswa, hipotesis, uji reliabilitas psikometrik, atau SUS secara otomatis pada penelitian pengembangan ini. Apabila instrumen persepsi ditambahkan, barulah konstruk, sumber instrumen, pemeriksaan kualitas, dan analisisnya dijelaskan sesuai tujuan pengukuran.

### Batas pemeriksaan format fisik

Margin, font, spasi, inden, nomor halaman, watermark, dan pemenggalan tabel belum dapat disimpulkan dari Markdown. Pemeriksaan fisik perlu dilakukan pada Word atau PDF hasil tata letak dengan acuan Panduan 2025 §3.1 sampai §3.5, cetak 11 sampai 15/PDF 19 sampai 23.

Seluruh dua puluh tabel memiliki nomor serta judul di atasnya, dan sepuluh gambar mempunyai judul di bawahnya. Semua telah disebut sebelum kemunculannya dan tautan gambar tersedia; ukuran huruf pada hasil cetak serta kerapian halaman tetap belum dinilai.

### Pemeriksaan sumber, umur rujukan, dan kemiripan redaksi

Tiga belas sumber penelitian yang dicocokkan terdiri atas dua belas artikel jurnal dan satu prosiding asli PxP. Dua belas dari tiga belas sumber tersebut terbit pada 2016 atau setelahnya, yaitu sekitar 92,31 persen, sedangkan Dzhurov dkk. (2009) dipertahankan sebagai sumber asli metode.

Daftar pustaka tidak menyatu dalam berkas Bab 3, tetapi daftar pendamping tersedia dan telah digunakan sebagai pembanding. Keharusan semua sitasi mempunyai entri serta semua entri digunakan perlu diperiksa kembali pada daftar pustaka induk proposal, termasuk metadata Thiovanda yang masih memerlukan kelengkapan volume atau nomor.

Nomor halaman tidak wajib ditambahkan pada seluruh parafrasa hanya karena dihapus dari versi sebelumnya. Nomor halaman perlu dipertahankan untuk kutipan langsung dan dapat ditambahkan pada parafrasa yang spesifik agar mudah diperiksa; identitas objek dan kekuatan klaim harus lebih dahulu benar.

Penilaian ini tidak menggunakan basis data kemiripan seperti Turnitin dan tidak menghasilkan persentase plagiarisme. Pemakaian ungkapan umum atau istilah teknis tidak membuktikan plagiarisme maupun asal penulisannya, sedangkan kemiripan redaksi panjang perlu diperiksa langsung terhadap sumber ketika ditemukan.

### Penilaian terhadap rubrik sidang sebagai sasaran akhir

| Kriteria rubrik | Penilaian pada tahap proposal ini |
| :--- | :--- |
| Struktur dan sistematika | Susunan serta artefak kuat; penggunaan sumber perlu dikoreksi sebelum indikator Sangat Baik dinyatakan |
| Kepatuhan format dan tata tulis | Bentuk dasar Markdown memadai; ejaan, istilah, klaim, dan format fisik belum seluruhnya selesai |
| Eksekusi metode dan relevansi masalah | PxP relevan dengan pengembangan individual; keunikan produk dibahas dengan literatur dan kebutuhan mitra, bukan diasumsikan dari banyaknya fitur |
| Validitas data dan analisis | Rancangan sumber serta analisis tersedia; status bukti dan prosedur teknik baru perlu diperjelas |
| Argumentasi dan kesimpulan | Belum dinilai sebagai hasil karena implementasi serta data evaluasi belum diberikan |
| Luaran, dampak, dan kelayakan | Produk, artikel, HKI, dan evaluasi sudah direncanakan; kinerja serta dampak nyata menunggu hasil pelaksanaan |

## G.4 Daftar periksa wajib sebelum pengajuan

Tanda selesai hanya diberikan pada bagian yang dapat diperiksa dari berkas saat ini. Status terbuka berarti perlu perbaikan atau belum dapat dinilai, bukan otomatis tidak ada pada seluruh proposal.

| No. | Item periksa | Status |
| ---: | :--- | :--- |
| 1 | Anotasi ukuran huruf template telah dihapus | [x] Tidak ditemukan dalam naskah |
| 2 | Nomor bab menggunakan BAB 3 | [x] Terpenuhi |
| 3 | Penomoran desimal maksimal tiga tingkat | [x] Terpenuhi pada berkas |
| 4 | Tidak ada paragraf prosa satu kalimat | [x] Terpenuhi pada pemeriksaan 128 paragraf |
| 5 | Tidak ada kalimat berawal angka numerik | [x] Tidak ditemukan |
| 6 | Tidak ada dash panjang atau dash ganda sebagai penghubung | [x] Tidak ditemukan pada prosa |
| 7 | Istilah asing berpadanan telah disesuaikan | [ ] Perlu penyeragaman |
| 8 | Istilah asing generik yang dipertahankan dicetak miring | [ ] Perlu pemeriksaan akhir |
| 9 | Bentuk terikat ditulis serangkai | [ ] Perbaiki non-tunai |
| 10 | Tidak ada kata ganti orang pertama | [x] Tidak ditemukan |
| 11 | Nomor dan judul tabel di atas tabel | [x] Posisi Markdown sesuai; perataan Word belum dinilai |
| 12 | Nomor dan judul gambar di bawah gambar | [x] Posisi Markdown sesuai; perataan Word belum dinilai |
| 13 | Semua tabel dan gambar disebut dalam paragraf | [x] Dua puluh tabel dan sepuluh gambar diacu |
| 14 | Harvard dan identitas pustaka konsisten | [ ] Perbaiki nama penulis dan atribusi sumber |
| 15 | Target TKT 5 dicantumkan | [x] Ada; bukti pencapaian direncanakan |
| 16 | Rencana HKI disebutkan | [x] Ada pada 3.1.4 |
| 17 | Subbab Bab 1 lengkap 1.1 sampai 1.7 | [ ] Ada pada pembanding; belum diaudit penuh pada pemeriksaan ini |
| 18 | Rumusan masalah berupa pertanyaan bernomor | [x] Tiga pertanyaan ditemukan pada Bab 1 pembanding |
| 19 | Tujuan berhubungan dengan rumusan masalah | [ ] Arah tiga tujuan ada; batas pemeriksa dan istilah waktu nyata perlu diselaraskan |
| 20 | Diagram tahapan tersedia pada 3.2 | [x] Gambar 3.1 tersedia |
| 21 | Font, margin, spasi, inden, dan nomor halaman final | [ ] Memerlukan Word/PDF |
| 22 | Status tunai, transfer, dan saldo tagihan konsisten | [ ] Sangat penting |
| 23 | Autentikasi sesi dan otorisasi sesuai rancangan | [ ] Sangat penting |
| 24 | Partisi dan batas EP/BVA dijabarkan | [ ] Lengkapi atau hapus klaim teknik |
| 25 | Jumlah sasaran peserta, cabang, serta prosedur UAT jelas | [ ] Lengkapi rencana |
| 26 | Versi layanan masih didukung dan dipilih untuk pengujian | [ ] Tinjau Laravel 11 dan pilihan MySQL |
| 27 | Cadangan meliputi struktur, isi data, dan berkas | [ ] Perjelas redaksi dan langkah |
| 28 | Jadwal mencakup literatur serta penyiapan penerapan | [ ] Lengkapi pemetaan kegiatan |

## G.5 Rekomendasi langkah sebelum berkonsultasi

Perbaikan didahulukan pada aturan yang dapat menghasilkan penjelasan atau keluaran sistem berbeda, kemudian metode evaluasi dan bahasa. Kerangka enam subbab, tabel kebutuhan, serta gambar tidak perlu dibuang ketika masalah tersebut diperbaiki.

| Urutan | Pekerjaan | Hasil yang dibawa saat bimbingan |
| ---: | :--- | :--- |
| 1 | Samakan status pembayaran sah, pencocokan manual, batas kelas, serta otorisasi | Satu lembar keputusan aturan dan paragraf yang sudah diselaraskan |
| 2 | Konfirmasikan peran pemeriksa rekening, tunai, setoran, tarif, dan parameter kelas | Ringkasan keputusan mitra atau daftar pertanyaan yang belum terjawab |
| 3 | Pilih versi layanan yang masih didukung dan satu versi MySQL | Tabel versi dengan bukti sumber versi serta status rencana atau digunakan |
| 4 | Jabarkan atau hapus klaim EP/BVA dan pengujian beban | Matriks partisi, batas, data uji, serta rancangan pengukuran yang realistis |
| 5 | Tetapkan rencana peserta dan satuan analisis UAT | Daftar sasaran, tugas menurut peran, formulir, kriteria keputusan, dan prosedur uji ulang |
| 6 | Pisahkan kegiatan telah dilakukan dari rencana | Indeks transkrip, dokumen yang diizinkan, dan lembar observasi bila ada |
| 7 | Koreksi atribusi artikel serta nama penulis | Daftar pustaka dan sitasi dari pengelola referensi yang konsisten |
| 8 | Sederhanakan narasi, ganti klaim jaminan, dan benahi ejaan | Naskah yang menjelaskan pelaksana, tindakan, data, dan keluaran secara langsung |
| 9 | Selaraskan Bab 1 dan daftar pustaka induk, kemudian tata letak | Proposal gabungan dengan batas rancangan serta istilah yang sama dan PDF untuk pemeriksaan format |

Naskah ini layak dibawa untuk konsultasi revisi karena bahan perancangannya sudah cukup lengkap. Namun, versi copy belum disarankan sebagai naskah final pengajuan sempro sebelum masalah penting di atas ditangani; kesiapan semhas atau sidang tidak dapat dinyatakan dari proposal Bab 3 saja.

## Sumber pemeriksaan

Lokator berikut digunakan untuk memisahkan aturan resmi, kriteria tambahan pengguna, bukti rancangan, dan alasan teknis. Pemeriksaan sumber ini tidak merupakan audit akreditasi SINTA baru atau pengesahan seluruh metadata edisi jurnal.

| Sumber | Lokator atau tautan | Kegunaan |
| :--- | :--- | :--- |
| Panduan Kepenulisan ITK 2025 | Cetak 11 sampai 16/PDF 19 sampai 24 | Tata tulis, bahasa, tabel, gambar, persamaan, dan Harvard |
| Panduan TA dan SITASI SI 2026 | Cetak 4/PDF 11; cetak 80 sampai 83/PDF 87 sampai 90 | TKT, mitra, HKI, serta perbedaan rubrik proposal dan sidang |
| Template Prototipe SI | Cetak 6 sampai 7/PDF 19 sampai 20 | Enam subbab dan isi minimum Bab 3 |
| Dokumen use case serta basis data ARTHA | Berkas rancangan yang tersedia di DOKUMEN MD | Peran, status, kapasitas, dan alur pencocokan |
| Daftar pustaka pendamping Bab 3 | BAB3_PENDUKUNG_2026-10-25 | Pembanding identitas sumber dan lokator halaman |
| [Laravel Support Policy](https://laravel.com/framework/docs/12.x/releases) | Baris Laravel 11 dan Laravel 12 | Masa dukungan keamanan, bukan sekadar kompatibilitas PHP |
| [Laravel Sanctum](https://laravel.com/framework/docs/12.x/sanctum) | SPA Authentication | Sesi berbasis kuki untuk mode SPA |
| [ISTQB CTFL v4.0.1](https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) | §4.2.1 dan §4.2.2, halaman 39 sampai 40 | Pengertian partisi dan nilai batas |
| [Metadata penerbit Fikri](https://journal.umpo.ac.id/index.php/multitek/article/view/2568) | Published dan How to Cite | Nama penulis serta publikasi 4 Januari 2021 pada edisi berlabel 2020 |

Foto halaman panduan terpilih, teks per halaman, hasil pemeriksaan struktur, dan daftar temuan terstruktur disimpan pada folder REVIEW_COPY_2026-10-25. Hash naskah diperiksa kembali setelah laporan ditulis untuk memastikan berkas yang ditinjau tetap utuh.
