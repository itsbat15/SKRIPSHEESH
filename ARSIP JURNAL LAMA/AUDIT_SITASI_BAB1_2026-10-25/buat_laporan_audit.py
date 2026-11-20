from pathlib import Path
from collections import Counter
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DRAFT = ROOT / 'BAB 1 - PENDAHULUAN (VERSI 11 PARAGRAF).md'
snapshot = (HERE / 'SALINAN_BAB1_YANG_DIAUDIT.md').read_text(encoding='utf-8')
extracted = json.loads((HERE / 'SUMBER_DAN_TEKS_HALAMAN.json').read_text(encoding='utf-8'))

source_specs = [
    ('S01', 'Tiana', 'Tiana dan Gunanto (2026)', 'Perancangan dan Implementasi Sistem Informasi Bimbingan Belajar Berbasis Web Mobile Menggunakan Metode Waterfall', 'Artikel JUKTISI; konteks Texas Kotabumi, bukan ARTHA.'),
    ('S02', 'Pradana', 'Pradana (2024)', 'Peran Teknologi Informasi dalam Meningkatkan Efektivitas Manajemen Pendidikan di Sekolah', 'Kajian literatur manajemen pendidikan sekolah; bukan sumber definisi SI yang ditulis pada Bab 1.'),
    ('S03', 'Fajriansyah', 'Fajriansyah dkk. (2026)', 'Pengembangan Sistem Informasi Bimbingan Belajar Berbasis Web untuk Efisiensi Operasional Bee Hive', 'Artikel memuat laporan dampak pada hlm. 124 dan simpulan pada hlm. 125; batasi kesimpulan pada kasus Bee Hive.'),
    ('S04', 'Ahadi', 'Ahadi dkk. (2025)', 'Pengembangan Sistem Informasi Manajemen Hotel Multi-Cabang Berbasis Web dengan Framework Laravel', 'Tabel kebutuhan pengguna mencakup empat aktor; jangan menyederhanakannya menjadi sistem yang hanya memiliki Owner dan PIC.'),
    ('S05', '05_Penerimaan', 'Hendri dkk. (2025)', 'Analisis Sistem Informasi Akuntansi Penerimaan Kas (SPP) pada Yayasan Semesta Khatulistiwa', 'Hasil berupa analisis dan rancangan antarmuka Figma; masalah pencocokan catatan siswa dan bendahara disebut pada hlm. 124.'),
    ('S06', 'Rams_Dimsum', 'Ramadhan dan Widodo (2026)', 'Accounting Treatment Of Head Office And Branches Based On SAK EP: A Study on UMKM Rams Dimsum', 'PDF lokal 19 halaman, tetapi footer memakai penyebut 15. Gunakan urutan PDF; footer 17/15 bukan nomor halaman jurnal yang stabil.'),
    ('S07', 'Sudirman', 'Sudirman dan Tristianti (2021)', 'Sistem Informasi Pengendalian Kas Bank dengan Metode Rekonsiliasi pada CV. Lisa Pratama Berbasis Client-Server', 'Edisi Desember 2021; sumber rekonsiliasi bank, bukan studi bimbel atau pusat-cabang.'),
    ('S08', 'Kabisatullah', 'Kabisatullah dan Noprisson (2026)', 'Pengembangan Aplikasi RapaTrack untuk Manajemen Ruang Rapat Menggunakan Constraint Satisfaction Problem Berbasis Android', 'Konteks reservasi ruang rapat. PDF menulis Noprison, sedangkan metadata penerbit menggunakan Noprisson.'),
    ('S09', 'Khafidhoh', 'Khafidhoh dkk. (2026)', 'Sistem Penjadwalan Menggunakan Algoritma Genetika Berbasis Web', 'Konteks AHE Megaluh 7059 dengan penyusunan jadwal otomatis, bukan hanya peringatan konflik.'),
    ('S10', 'Gunawan', 'Gunawan dkk. (2025)', 'Sistem Informasi Bimbingan Belajar RSDC Berbasis Website dengan Menggunakan Metode Waterfall untuk Meningkatkan Efisiensi Administrasi', 'Modul yang disebut Bab 1 terdapat pada abstrak hlm. 424.'),
    ('S11', 'Barizi', 'Barizi dkk. (2023)', 'Perancangan Aplikasi Sistem Administrasi Sekolah Musik pada Sekolah Musik ABC Berbasis Java', 'Identitas eksplisit menyebut Java. Antarmuka aplikasi pada hlm. 336-337 menjadi dasar pengenalan bentuk aplikasi desktop.'),
    ('S12', 'Thiovanda', 'Thiovanda (2026)', 'Perancangan Sistem Informasi Pencatatan Penjadwalan dan Pembayaran Les Berbasis Web', 'Tahun 2026 dan DOI 10.24912/yctfww47 dikonfirmasi dari laman penerbit; tahun tidak tercantum jelas pada header PDF lokal. Halaman 4 memuat pengelolaan cabang dan pembatasan akses.'),
    ('S13', 'Safitri', 'Safitri dkk. (2026)', 'Perancangan Sistem Informasi Manajemen Bimbingan Belajar Berbasis Web untuk Efisiensi Administrasi dan Komunikasi dengan Fitur Notifikasi Otomatis', 'Tabel 1 baris 14 pada hlm. 2350 tidak konsisten: label notifikasi WhatsApp, tetapi hasilnya menjelaskan logout.'),
    ('S14', 'Scrum Guide', 'Schwaber dan Sutherland (2020)', 'The Scrum Guide', 'Hlm. cetak 5 sama dengan PDF 6; hlm. cetak 9 sama dengan PDF 10 karena sampul ikut dihitung.'),
    ('S15', 'Sommerville', 'Sommerville (2011)', 'Software Engineering, Ninth Edition', 'Pada halaman rujukan yang diperiksa, urutan PDF = nomor cetak + 17. Gunakan nomor yang tertulis, bukan asumsi offset untuk seluruh buku.'),
    ('S16', 'Kent-Beck', 'Beck dan Andres (2004)', 'Extreme Programming Explained: Embrace Change, Second Edition', 'Salinan digital mengalir ulang menjadi 294 halaman PDF. Nomor cetak asli tidak tampil pada halaman yang dirujuk; gunakan PDF 104 dan nama subbagian, jangan mengarang nomor cetak.'),
    ('S17', 'single person', 'Agarwal dan Umphress (2008)', 'Extreme Programming for a Single Person Team', 'PDF pindai enam halaman, cetak 82-87. Teks OCR hanya alat bantu; halaman 82, 85 dan 86 diperiksa visual. DOI 10.1145/1593105.1593127.'),
    ('S18', 'Mishra', 'Mishra dan Alzoubi (2023)', 'Structured Software Development versus Agile Software Development: A Comparative Analysis', 'Artikel cetak 1504-1522. Pembahasan kohesivitas tim berada dalam kajian Agile umum, bukan bukti kewajiban mentor pada XP individual.'),
    ('S19', 'pressman', 'Pressman (2010)', 'Software Engineering: A Practitioner\'s Approach, Seventh Edition', 'Bagian model proses dan pengembangan berbasis komponen diperiksa pada cetak 39-51. Tidak ditemukan dukungan bagi larangan RAD untuk diskon atau rekap multicabang pada salinan ini.'),
    ('S20', 'Buku Tamu', 'Fikri dan Arthawan (2020)', 'Rancang Bangun Sistem Informasi Buku Tamu pada Dinas Pemuda, Olahraga dan Pariwisata Kota Balikpapan dengan Metode Personal Extreme Programming', 'Nama Prabowo pada nama file keliru; PDF menyebut I Putu Deny Arthawan S. P. Nomor halaman 103-104 terlihat jelas meskipun rentang pada header awal artikel salah ketik.'),
    ('S21', 'Sidiq', 'Sidiq dkk. (2025)', 'Implementasi Metode Personal Extreme Programming pada Pengembangan Sistem Informasi Surat Menyurat', 'Hlm. 45 membedakan total pengembangan 50 hari dan implementasi 37 hari. Jangan menafsirkan angka implementasi sebagai keseluruhan proyek lebih cepat.'),
]
sources = {}
for sid, key, author, title, note in source_specs:
    match = [x for x in extracted if key.lower() in x['file'].lower()]
    assert len(match) == 1, (sid, key)
    sources[sid] = dict(match[0], id=sid, author=author, title=title, note=note)

# Locations below explicitly distinguish evidence from nearby material that does
# not support the claim. No page is invented for an unsupported assertion.
rows = []

def add(aid, paragraph, sid, status, claim, locations, anchor, finding, correction):
    rows.append(dict(id=aid, paragraph=paragraph, source=sid, status=status,
                     claim=claim, locations=locations, anchor=anchor,
                     finding=finding, correction=correction))

add('A01', 1, 'S01', 'SEBAGIAN',
    'Seluruh faktor tersebut saling berkaitan dalam menciptakan kegiatan belajar yang efektif dan teratur',
    [(1, '1631', 'Pendahuluan dan abstrak'), (2, '1632', 'Lanjutan pendahuluan')],
    'alternatif pendidikan non-formal',
    'Artikel mendukung peran bimbel serta kebutuhan administrasi pendaftaran, jadwal, kehadiran dan pembayaran. Uraian khusus seluruh faktor siswa, tentor, ruang dan efektivitas pembelajaran merupakan sintesis yang lebih luas; artikel ini juga tidak menjadi sumber hukum UU 20/2003.',
    'Tulis lebih dekat ke sumber: Tiana dan Gunanto (2026, hlm. 1631-1632) membahas pengelolaan pendaftaran, jadwal, kehadiran dan pembayaran pada bimbel. Beri sumber hukum tersendiri untuk Pasal 26 dan hindari satu sitasi di ujung paragraf seolah mendukung seluruh kalimat.')

add('A02', 2, 'S02', 'TIDAK DIDUKUNG',
    'Sistem informasi merupakan seperangkat prosedur yang dirancang untuk mengumpulkan, mengolah, menyimpan, dan mendistribusikan informasi',
    [(2, '6856', 'Pendahuluan; bagian terkait, bukan definisi tersebut'), (4, '6858', 'Pembahasan administrasi; bagian terkait')],
    'sistem informasi yang terintegrasi',
    'Penelusuran seluruh enam halaman tidak menemukan definisi SI dengan susunan konsep yang ditulis pada Bab 1. Halaman 6856 dan 6858 membahas integrasi informasi serta otomatisasi administrasi sekolah, bukan definisi tersebut.',
    'Ganti menjadi klaim fungsi yang benar-benar dibahas, misalnya Pradana (2024, hlm. 6858) membahas penggunaan sistem informasi untuk pengelolaan data siswa dan keuangan sekolah. Jika ingin mempertahankan definisi, cari sumber teori yang memang menyatakan definisi itu.')

add('A03', 2, 'S03', 'SEBAGIAN',
    'penerapan teknologi informasi terbukti meningkatkan efektivitas administrasi',
    [(2, '116', 'Abstrak Indonesia'), (10, '124', 'Analisis Efektivitas dan Dampak Operasional'), (11, '125', 'Kesimpulan dan evaluasi')],
    'Analisis Efektivitas dan Dampak Operasional',
    'Artikel memang melaporkan dampak pada Bee Hive, termasuk waktu pendaftaran dari sekitar 10-15 menit menjadi kurang dari dua detik dan evaluasi bersama owner serta dua tutor senior. Klaim itu merupakan laporan studi kasus tersebut; kalimat Bab 1 menggeneralisasikannya ke pendidikan nonformal secara keseluruhan.',
    'Gunakan atribusi terbatas: Pada Bee Hive, Fajriansyah dkk. (2026, hlm. 124-125) melaporkan perbaikan proses administrasi setelah pengembangan sistem. Jangan memindahkan hasil waktunya menjadi hasil atau jaminan untuk ARTHA.')

add('A04', 2, 'S04', 'DIDUKUNG',
    'pemisahan kewenangan antar-peran dan penyediaan laporan terpusat',
    [(7, '764', 'Tabel 1 lanjutan, Tabel 2 dan Tabel 3'), (8, '765', 'Tabel 3 lanjutan')],
    'Owner; PIC Cabang',
    'Kebutuhan laporan per cabang, batasan akses dan hak Owner melihat semua laporan tercantum pada halaman 764. Halaman 765 membedakan kewenangan PIC cabang, front office dan housekeeping; ini mendukung prinsip pembagian akses yang dipakai sebagai acuan rancangan.',
    'Pertahankan dengan batas konteks: Ahadi dkk. (2025, hlm. 764-765) menjadi contoh pembagian hak akses dan laporan pada hotel multicabang. Kata harus pada seluruh lembaga merupakan keputusan rancangan yang perlu dijustifikasi, bukan hukum universal yang diuji artikel.')

add('A05', 6, 'S05', 'SEBAGIAN',
    'menyulitkan pencocokan antara catatan kasir dan bukti transaksi yang sebenarnya',
    [(1, '124', 'Pendahuluan, paragraf terakhir'), (2, '125', 'Landasan penerimaan kas dan metode')],
    'catatan siswa dan catatan bendahara',
    'Masalah yang disebut eksplisit ialah kesulitan pencocokan catatan siswa dengan catatan bendahara pada Yayasan Semesta Khatulistiwa. Penyimpanan di setiap cabang, keadaan kasir ARTHA dan proses bukti transaksi ARTHA tidak diteliti artikel ini; hasilnya juga berupa rancangan antarmuka.',
    'Pisahkan bukti: Hendri dkk. (2025, hlm. 124) menemukan kesulitan pencocokan catatan siswa dan bendahara pada penerimaan SPP. Letakkan uraian ARTHA pada kalimat tersendiri dengan rujukan wawancara atau dokumen mitra.')

add('A06', 6, 'S06', 'SEBAGIAN',
    'pimpinan pusat memerlukan laporan setoran dari seluruh cabang untuk dicocokkan dengan mutasi rekening bank',
    [(13, 'footer 13/15', 'Temuan pencatatan gabungan dan operasional'), (15, 'footer 15/15', 'Rekomendasi pencatatan per cabang'), (17, 'footer 17/15', 'Tabel 8 Rekap Penjualan Harian dan simpulan')],
    'Rekap Penjualan Harian',
    'Artikel mendukung pemisahan catatan cabang, rekap pusat, dokumen pendukung dan rekonsiliasi penerimaan harian. Bagian tersebut bukan pembuktian pencocokan mutasi bank pada ARTHA; yang dibahas adalah UMKM Rams Dimsum dan tata kelola akuntansinya.',
    'Gunakan Ramadhan dan Widodo (2026, halaman PDF 15 dan 17) untuk pemisahan catatan dan rekap harian pusat-cabang. Gunakan sumber rekonsiliasi bank secara terpisah, serta wawancara ARTHA untuk siapa yang memeriksa penerimaan di ARTHA.')

add('A07', 6, 'S07', 'SEBAGIAN',
    'pimpinan pusat memerlukan laporan setoran dari seluruh cabang untuk dicocokkan dengan mutasi rekening bank',
    [(1, '126', 'Abstrak dan akhir pendahuluan'), (2, '127', 'Definisi dan tujuan rekonsiliasi')],
    'rekening koran bank',
    'Sumber ini memang menjelaskan pencocokan catatan perusahaan dengan rekening koran bank dan manfaat pengendalian kas bank. Artikel tidak meneliti delapan cabang ARTHA atau membuktikan keterlambatan informasi pusat ARTHA; kedua sumber dalam kurung ini saling melengkapi konsep, tetapi tidak menggantikan data kasus.',
    'Pertahankan sebagai konsep: Sudirman dan Tristianti (2021, hlm. 126-127) membahas rekonsiliasi catatan kas perusahaan dengan rekening koran. Pisahkan konsep tersebut dari temuan proses setoran dan keterlambatan ARTHA.')

add('A08', 7, 'S08', 'SEBAGIAN',
    'status ketersediaan ruang secara langsung kepada staf',
    [(5, '93', 'Perancangan antarmuka reservasi'), (6, '94', 'Lima constraint dan pengujian CSP')],
    'Capacity',
    'RapaTrack menunjukkan reservasi ruang, batas jumlah peserta terhadap kapasitas dan validasi waktu. Ketiadaan alat bantu visual pada ARTHA atau perbaikan pengarahan siswa tidak dibuktikan oleh studi ruang rapat ini; penolakan reservasi juga berbeda dari peringatan yang mengikuti kebijakan pengelola.',
    'Tulis hubungan adaptasinya: Aturan kapasitas pada Kabisatullah dan Noprisson (2026, hlm. 94) menjadi acuan validasi penempatan kelas. Sumber kebutuhan keterisian dan penempatan siswa ARTHA tetap berasal dari wawancara atau observasi.')

add('A09', 7, 'S09', 'SEBAGIAN',
    'berpotensi memunculkan konflik penugasan dan ketidakmerataan alokasi pengajar',
    [(1, '15', 'Abstrak dan pendahuluan'), (2, '16', 'Tujuan dan rancangan penelitian')],
    'uneven distribution of teaching assignments',
    'Konflik jadwal dan pemerataan penugasan memang menjadi masalah pada AHE Megaluh 7059. Artikel tidak mengamati grup percakapan, pergantian tentor atau ketidakmerataan penugasan di ARTHA, sehingga sitasi tidak boleh membuat kesan bahwa temuan AHE adalah temuan mitra.',
    'Pisahkan pembanding: Khafidhoh dkk. (2026, hlm. 15-16) membahas risiko jadwal manual pada AHE. Setelah itu jelaskan pencatatan dan komunikasi ARTHA berdasarkan wawancara, serta posisikan peringatan sebagai rancangan pencegahan.')

add('A10', 8, 'S10', 'DIDUKUNG',
    'mencakup modul registrasi, penjadwalan, presensi, dan verifikasi pembayaran',
    [(1, '424', 'Abstract dan abstrak'), (9, '432', 'Antarmuka verifikasi pembayaran')],
    'payment verification',
    'Keempat fungsi disebut langsung pada abstrak artikel RSDC. Uraian antarmuka memperlihatkan pengelolaan verifikasi pembayaran; kalimat Bab 1 sudah menyebut objek penelitian dengan jelas dan tidak memindahkan hasilnya ke ARTHA.',
    'Dapat dipertahankan: Gunawan dkk. (2025, hlm. 424) mengembangkan sistem RSDC yang mencakup registrasi, penjadwalan, presensi dan verifikasi pembayaran. Tambahkan hlm. 432 jika pembahasan difokuskan pada antarmuka pembayaran.')

add('A11', 8, 'S03', 'DIDUKUNG',
    'mengintegrasikan pengelolaan data siswa, jadwal, dan pembayaran dalam satu platform',
    [(2, '116', 'Abstrak Indonesia'), (10, '124', 'Dampak operasional dan tampilan sistem'), (11, '125', 'Kesimpulan')],
    'pendaftaran siswa',
    'Integrasi fungsi tersebut dinyatakan pada abstrak Indonesia dan pembahasan sistem Bee Hive. Uraian Bab 1 sudah dibatasi pada studi tersebut; bila menyebut efisiensi, gunakan bahasa melaporkan sesuai bentuk evaluasinya.',
    'Dapat dipertahankan dengan halaman: Fajriansyah dkk. (2026, hlm. 116, 124-125) mengembangkan platform administrasi Bee Hive dan melaporkan dampak operasionalnya. Hindari menyebut peningkatan yang sama sebagai hasil ARTHA.')

add('A12', 8, 'S11', 'DIDUKUNG',
    'menyatukan modul pembayaran dan penjadwalan dalam satu platform',
    [(1, '332', 'Abstrak dan judul Java'), (5, '336', 'Tampilan aplikasi'), (6, '337', 'Tampilan data jadwal dan pembayaran'), (7, '338', 'Simpulan')],
    'penjadwalan kursus; pembayaran kursus',
    'Abstrak menyebut pengelolaan siswa, guru, kursus, penjadwalan dan pembayaran, dan simpulan mengulang fungsi tersebut. Bentuk desktop dikenali dari implementasi dan tampilan Java; judul eksplisitnya menyebut berbasis Java, sehingga istilah itu lebih langsung dibandingkan istilah desktop.',
    'Dapat dipertahankan atau diperjelas: Barizi dkk. (2023, hlm. 332, 337-338) merancang aplikasi administrasi berbasis Java yang mencakup penjadwalan dan pembayaran kursus. Jangan menjadikan aplikasi ini pembuktian sistem multicabang.')

add('A13', 8, 'S12', 'DIDUKUNG',
    'guna mengurangi benturan jadwal dan mempercepat pengelolaan transaksi',
    [(1, '1', 'Abstrak'), (4, '4', 'Gambar 9-13: cabang, siswa dan penjadwalan'), (5, '5', 'Verifikasi pembayaran dan kesimpulan')],
    'Cabang Management',
    'Abstrak dan pembahasan mendukung sistem penjadwalan serta pembayaran les dengan tujuan penanganan benturan dan administrasi transaksi. Temuan penting yang tidak disebut dalam Bab 1 ialah head admin dapat mengelola semua cabang dan admin dibatasi pada cabangnya di hlm. 4; ini melemahkan klaim kebaruan umum setelah daftar penelitian.',
    'Pertahankan deskripsi fungsi, tetapi tambahkan perbandingan multicabang: Thiovanda (2026, hlm. 4-5) sudah mencakup cabang, akses siswa berdasarkan cabang dan verifikasi pembayaran. Bedakan ARTHA berdasarkan aturan kapasitas, mekanisme penerimaan dan evaluasi yang benar-benar akan dikerjakan.')

add('A14', 8, 'S13', 'SEBAGIAN',
    'fitur notifikasi otomatis melalui WhatsApp untuk penagihan SPP',
    [(1, '2345', 'Abstrak'), (5, '2349', 'Broadcast jadwal dan modul pembayaran'), (6, '2350', 'Tabel 1, baris 11-14')],
    'Notifikasi WhatsApp',
    'WhatsApp, broadcast jadwal, tagihan otomatis dan verifikasi pembayaran memang dijelaskan. Namun, baris pengujian notifikasi pembayaran pada tabel menampilkan hasil logout, sehingga bukti uji spesifik pengiriman penagihan SPP tidak konsisten; pembuatan tagihan juga tidak sama dengan pengiriman pesan penagihan.',
    'Persempit menjadi Safitri dkk. (2026, hlm. 2349) mengembangkan broadcast jadwal WhatsApp dan modul pembayaran. Jika tetap menyebut penagihan SPP otomatis, jelaskan bahwa artikel mengklaim fitur itu, sedangkan bukti pengujian pada hlm. 2350 perlu dikonfirmasi.')

add('A15', 8, 'S09', 'DIDUKUNG',
    'pengelolaan jadwal tanpa sistem terpusat berpotensi memunculkan konflik penugasan',
    [(1, '15', 'Abstrak dan masalah penjadwalan manual'), (2, '16', 'Tujuan'), (5, '19', 'Hasil dan kesimpulan')],
    'Sistem Penjadwalan',
    'Artikel mendukung masalah jadwal manual pada AHE, pemerataan tugas dan pengembangan sistem web. Frasa paling dekat dengan sumber adalah penjadwalan manual atau tidak terorganisasi; algoritma genetika merupakan komponen utama yang sebaiknya disebut dalam perbandingan.',
    'Gunakan Khafidhoh dkk. (2026, hlm. 15-16, 19) untuk contoh penjadwalan otomatis dengan algoritma genetika pada AHE. Jangan menambahkan angka penurunan konflik karena artikel tidak memberi perbandingan kuantitatif sebelum-sesudah yang rinci.')

add('A16', 8, 'S08', 'SEBAGIAN',
    'membuktikan perlunya validasi kapasitas secara digital',
    [(6, '94', 'Constraint kapasitas dan pengujian'), (7, '95', 'Lanjutan kesimpulan')],
    'Constraint Satisfaction Problem',
    'Artikel melaporkan penerapan CSP dan 25 skenario validasi pada ruang rapat, termasuk batas kapasitas. Hasil itu mendukung contoh penerapan validasi, bukan pembuktian universal bahwa setiap lembaga harus memakai validasi digital atau bahwa aturan ruang rapat identik dengan kelas ARTHA.',
    'Ganti membuktikan perlunya menjadi menerapkan: Kabisatullah dan Noprisson (2026, hlm. 94) menerapkan batas kapasitas peserta dan validasi waktu pada reservasi ruang rapat berbasis Android. Jelaskan adaptasinya untuk kelas bimbel.')

add('A17', 8, 'S04', 'DIDUKUNG',
    'fitur pemisahan kewenangan Owner dan PIC Cabang',
    [(7, '764', 'Tabel kebutuhan sistem dan pengguna'), (8, '765', 'Tabel pengguna lanjutan')],
    'Owner; PIC Cabang',
    'Owner dan PIC Cabang serta kewenangannya dinyatakan langsung pada tabel pengguna. Artikel memang memakai Laravel dan objek hotel; kedua detail itu sudah sesuai dengan uraian Bab 1.',
    'Dapat dipertahankan dengan hlm. 764-765. Bila menjelaskan jumlah peran, sebutkan bahwa artikel juga mempunyai front office dan housekeeping, sehingga dua peran ARTHA adalah adaptasi rancangan, bukan salinan seluruh struktur artikel.')

add('A18', 8, 'S06', 'DIDUKUNG',
    'pemisahan pencatatan keuangan per cabang beserta rekap yang dapat diakses pusat',
    [(15, 'footer 15/15', 'Rekomendasi tata kelola; laporan per cabang'), (17, 'footer 17/15', 'Tabel 8 dan simpulan')],
    'pencatatan transaksi secara mandiri',
    'Rekomendasi secara eksplisit mengusulkan catatan transaksi cabang sebelum direkap pusat dan informasi pendapatan per outlet. Ini mendukung kebutuhan pelaporan pusat-cabang, tetapi belum membuktikan bahwa artikel membangun dasbor web yang telah diimplementasikan.',
    'Tulis Ramadhan dan Widodo (2026, halaman PDF 15 dan 17) merekomendasikan pemisahan pencatatan cabang serta rekap pusat. Gunakan kata rekomendasi atau kajian akuntansi agar tidak menimbulkan kesan hasilnya aplikasi operasional.')

add('A19', 10, 'S14', 'BERTENTANGAN',
    'yang dilarang dirangkap oleh satu orang',
    [(6, '5', 'Scrum Team dan tiga accountabilities'), (10, '9', 'Daily Scrum')],
    'Daily Scrum',
    'Panduan menyebut tiga akuntabilitas, bukan larangan mutlak setiap bentuk perangkapan. Pada hlm. 9, Product Owner atau Scrum Master yang aktif mengerjakan Sprint Backlog dapat berpartisipasi sebagai Developers; karena itu larangan mutlak seluruh perangkapan yang diatribusikan kepada panduan tidak benar.',
    'Hapus larangan mutlak dan penilaian tidak dapat dipertanggungjawabkan secara akademis. Gunakan pembahasan struktur akuntabilitas dan kebutuhan koordinasi sebagai pertimbangan kecocokan, tanpa menganggap perangkapan yang dimungkinkan berarti proyek solo otomatis memenuhi seluruh Scrum.')

add('A20', 10, 'S15', 'TIDAK DIDUKUNG',
    'tidak menghasilkan bukti metrik yang memadai untuk dipertanggungjawabkan dalam sidang Tugas Akhir',
    [(62, '45', '2.3.1 Prototyping dan Figure 2.9'), (63, '46', 'Evaluasi dan keterbatasan throwaway prototype')],
    'Evaluation Report',
    'Buku membahas tujuan, fungsi, evaluasi serta keterbatasan prototipe, termasuk dokumentasi dan kualitas pada throwaway prototype. Tidak ada kesimpulan bahwa Prototyping tidak dapat menghasilkan metrik memadai untuk sidang; Figure 2.9 bahkan menyebut rencana dan laporan evaluasi.',
    'Hapus alasan ketidaklayakan sidang. Jika dibandingkan dengan PxP, sebutkan fokus prototyping untuk eksplorasi kebutuhan menurut Sommerville (2011, hlm. 45-46), lalu dukung pencatatan waktu dan cacat PxP dengan sumber yang memang menjelaskannya.')

add('A21', 10, 'S16', 'DIDUKUNG',
    'dua pemrogram wajib bekerja berpasangan secara fisik di satu stasiun kerja',
    [(104, 'tidak tampil pada salinan digital ini', 'Chapter 7, Primary Practices, Pair Programming')],
    'Write all production programs',
    'Bagian tersebut secara langsung menganjurkan kode produksi ditulis oleh dua orang yang duduk pada satu mesin dan menjelaskan praktik pasangan. Buku juga mengizinkan eksplorasi ide sendiri sebelum membawanya kembali ke tim; kutipan mendukung praktik pair programming, bukan larangan semua bentuk kerja individual.',
    'Pertahankan secara terbatas: Beck dan Andres (2004, Chapter 7, Pair Programming; halaman PDF 104 pada salinan ini) menempatkan pair programming sebagai praktik kode produksi XP. Jangan menulis hlm. 104 sebagai halaman cetak buku jika nomor cetaknya tidak terlihat.')

add('A22', 10, 'S17', 'SEBAGIAN',
    'mengharuskan perwakilan pengguna hadir mendampingi pengembang setiap hari',
    [(4, '85', 'Table 2 lanjutan, baris On-site Customer')],
    'On-site Customer',
    'Tabel membandingkan pelanggan yang dialokasikan ke tim pada XP dengan komunikasi email atau telepon pada PXP. Artikel mendukung pentingnya kedekatan komunikasi, tetapi tidak membuktikan bahwa mitra ARTHA tidak mampu hadir setiap hari; kesimpulan tentang ketersediaan ARTHA harus berasal dari mitra.',
    'Gunakan Agarwal dan Umphress (2008, hlm. 85) untuk membandingkan keterlibatan pelanggan dalam XP dan PXP. Tuliskan mekanisme komunikasi serta jadwal mitra ARTHA sebagai rencana atau kesepakatan tersendiri, bukan temuan artikel.')

add('A23', 10, 'S18', 'TIDAK DIDUKUNG',
    'sulit diterapkan secara mandiri tanpa bimbingan orang yang berpengalaman',
    [(3, '1506', 'Kajian kohesivitas tim Agile umum'), (4, '1507', 'Tabel 1 kajian terdahulu'), (9, '1512', '3.1.1 Agile development frameworks'), (12, '1515', 'Tabel perbandingan expertise dan pengorganisasian')],
    'team cohesiveness',
    'Artikel membahas kohesivitas tim dalam kajian Agile umum dan mengenalkan XP terutama melalui test-driven development. Penelusuran isi tidak menemukan kesimpulan spesifik bahwa penerapan XP individual memerlukan mentor berpengalaman; klaim Bab 1 memperluas konteks tim umum menjadi syarat XP.',
    'Hapus syarat bimbingan orang berpengalaman kecuali ada sumber langsung yang mendukung. Gunakan Mishra dan Alzoubi (2023) untuk perbandingan karakteristik pendekatan secara proporsional, dengan membedakan temuan kajian terdahulu yang mereka rangkum dari kesimpulan tentang ARTHA.')

add('A24', 10, 'S15', 'TIDAK DIDUKUNG',
    'RAD tidak hanya menuntut beberapa tim kecil yang bekerja paralel pada modul berbeda',
    [(760, '743', 'Glossary, rapid application development (RAD)'), (77, '60', 'Keterbatasan customer involvement pada Agile umum')],
    'rapid application development (RAD)',
    'Glosarium mendefinisikan RAD sebagai pendekatan untuk penyampaian cepat dengan dukungan perangkat pengembangan. Pembahasan keterlibatan pelanggan pada hlm. 60 adalah tentang Agile umum, bukan bukti syarat mutlak tim paralel RAD atau ketidakmungkinan keterlibatan mitra ARTHA.',
    'Jangan gunakan halaman-halaman ini sebagai dukungan kalimat sekarang. Jika RAD akan ditolak atas dasar organisasi tim dan workshop, diperlukan sumber langsung tentang model RAD yang dimaksud serta data sumber daya dan jadwal mitra.')

add('A25', 10, 'S19', 'TIDAK DIDUKUNG',
    'tidak cocok untuk sistem dengan logika bisnis yang bersifat unik dan tidak tersedia',
    [(79, '50', '2.4.1 Component-Based Development; pembanding terdekat'), (80, '51', 'Lanjutan pengembangan berbasis komponen')],
    'Component-Based Development',
    'Bagian terdekat dalam edisi ketujuh membahas pengembangan berbasis komponen dan penggunaan kembali, bukan larangan RAD terhadap aturan diskon atau rekap cabang. Penelusuran teks seluruh salinan, daftar isi dan bagian model proses tidak menghasilkan halaman yang mendukung klaim spesifik tersebut; halaman 50-51 bukan pengganti bukti yang hilang.',
    'Hapus kesimpulan bahwa diskon saudara dan rekap cabang membuat RAD tidak cocok. Evaluasi ketersediaan komponen, modularitas, waktu dan partisipasi pengguna secara nyata, lalu rujuk edisi serta halaman sumber yang memang membahas RAD jika digunakan.')

add('A26', 11, 'S20', 'DIDUKUNG',
    'seluruh proses mulai dari eksplorasi kebutuhan hingga pengujian sistem secara mandiri',
    [(3, '103', 'Metode penelitian dan Requirements'), (4, '104', 'Planning sampai Retrospective'), (5, '105', 'Umpan balik pada akhir iterasi')],
    'Requirements; System Testing',
    'Artikel menjelaskan PxP untuk pengembang individual dan tahapan dari kebutuhan hingga pengujian serta retrospektif. Mandiri perlu dibaca sebagai pengerjaan pengembangan individual, bukan tanpa komunikasi klien; artikel justru menjelaskan pengujian bersama klien dan timbal balik iterasi.',
    'Dapat dipertahankan dengan batas arti: Fikri dan Arthawan (2020, hlm. 103-105) menerapkan PxP untuk pengembangan individual dengan keterlibatan klien. Gunakan sumber ini untuk rancangan evaluasi, tetapi bukan bukti bahwa mitra ARTHA sudah menyepakati jadwal evaluasi.')

add('A27', 11, 'S21', 'SEBAGIAN',
    'PxP juga mengedepankan prinsip kesederhanaan dan desain yang berkembang seiring iterasi tanpa mengorbankan kualitas sistem secara keseluruhan',
    [(3, '37', 'Alasan pemilihan dan metode'), (4, '38', 'Design, Implementation, System Testing dan Retrospective'), (11, '45', 'Kesimpulan waktu dan pengujian')],
    'Retrospective; refactoring',
    'Artikel mendukung komunikasi, perubahan kebutuhan, estimasi, iterasi, refactoring serta pengujian. Pernyataan tanpa mengorbankan kualitas keseluruhan dan kesesuaian dengan keterbatasan waktu mitra ARTHA lebih kuat daripada bukti studi surat-menyurat; total proyek pada simpulan justru bertambah dari 40 menjadi 50 hari.',
    'Persempit: Sidiq dkk. (2025, hlm. 37-38, 45) menerapkan komunikasi klien, iterasi dan pengujian untuk menangani perubahan kebutuhan. Jangan menjadikannya jaminan kualitas atau ketepatan waktu ARTHA; bedakan implementasi 37 hari dari total pengembangan 50 hari.')

paragraph_texts = [p.strip() for p in snapshot.split('## 1.1 Latar Belakang', 1)[1].split('## 1.2', 1)[0].split('\n\n') if p.strip() and p.strip() != '---']
assert len(rows) == 27 and len(sources) == 21 and len(paragraph_texts) == 12
for row in rows:
    para = paragraph_texts[row['paragraph'] - 1]
    assert row['claim'] in para, (row['id'], row['claim'])
    row['draft_line'] = snapshot[:snapshot.index(para)].count('\n') + 1
    for pdf_page, printed, section in row['locations']:
        assert 1 <= pdf_page <= len(sources[row['source']]['pages'])
    row['claim_supported_as_written'] = row['status'] == 'DIDUKUNG'

def link(label, file):
    return f'[{label}](<{Path(file).as_posix()}>)'

def locations(row):
    return '; '.join(f'cetak {printed}, PDF {page}' for page, printed, section in row['locations'])

counts = Counter(x['status'] for x in rows)
report = [
    '# Audit isi sitasi Bab 1 dan peta halaman sumber', '',
    'Tanggal pemeriksaan: 25 Oktober 2026. Audit mengikuti isi berkas VERSI 11 PARAGRAF yang dibaca pada tanggal ini, bukan draf revisi terpadu atau versi yang diperiksa sebelumnya.', '',
    f'Berkas yang diaudit: {link(DRAFT.name, DRAFT)}. Salinan tetap untuk pengecekan tersedia pada {link("salinan Bab 1 yang diaudit", HERE / "SALINAN_BAB1_YANG_DIAUDIT.md")}.', '',
    f'SHA-256 salinan: `{hashlib.sha256(snapshot.encode("utf-8")).hexdigest()}`. Nama berkas menyebut sebelas paragraf, tetapi bagian latar belakang pada salinan ini berisi dua belas paragraf.', '',
    '## Kesimpulan', '',
    'Ditemukan 27 penggunaan rujukan dari 21 sumber yang seluruh PDF-nya tersedia di JURNAL. Penilaian dilakukan per penggunaan, sebab satu artikel dapat mendukung suatu klaim dan tidak mendukung klaim lain dalam paragraf yang berbeda.', '',
    f'Hasilnya: {counts["DIDUKUNG"]} penggunaan DIDUKUNG, {counts["SEBAGIAN"]} SEBAGIAN, {counts["TIDAK DIDUKUNG"]} TIDAK DIDUKUNG, dan {counts["BERTENTANGAN"]} BERTENTANGAN. Kategori tersebut menilai kecocokan isi dengan kalimat yang ditulis, bukan penilaian peringkat atau mutu keseluruhan jurnal.', '',
    'Koreksi utama terdapat pada definisi SI yang diatribusikan kepada Pradana, larangan mutlak perangkapan peran Scrum, alasan menolak Prototyping/RAD, dan syarat mentor yang diatribusikan kepada Mishra dan Alzoubi. Temuan lain yang penting adalah artikel Thiovanda telah memuat cabang dan pembatasan akses, sehingga klaim kebaruan umum pada akhir paragraf penelitian terdahulu perlu diperbaiki.', '',
    '## Cara membaca nomor halaman', '',
    '- **Cetak** ialah nomor yang benar-benar tertulis pada lembar artikel atau buku. Contohnya, halaman 764 pada Ahadi adalah urutan PDF 7.',
    '- **PDF** ialah urutan halaman berkas lokal, dihitung mulai satu termasuk sampul dan halaman awal. Masukkan nomor ini pada kotak nomor halaman pembaca PDF apabila label halaman aplikasi membingungkan.',
    '- **Rams Dimsum:** salinan lokal memuat 19 halaman, tetapi footer memakai penyebut 15. Gunakan PDF 15 atau PDF 17 dan nama tabel; jangan mengubah footer tersebut menjadi rentang halaman jurnal yang dianggap normal.',
    '- **Beck dan Andres:** nomor cetak tidak tampil pada bagian yang dirujuk dalam salinan yang mengalir ulang. Lokator yang pasti adalah Chapter 7, Pair Programming, PDF 104, bukan klaim bahwa halaman cetaknya 104.',
    '- **Tidak didukung:** halaman yang dicantumkan adalah bagian terdekat yang diperiksa, bukan halaman yang dapat dipakai untuk mempertahankan klaim salah. Tidak ada nomor halaman pendukung yang dibuat-buat.', '',
    'Nomor cetak diprioritaskan untuk sitasi akhir jika tersedia, sedangkan nomor PDF disediakan untuk penelusuran manual. Untuk salinan tanpa nomor cetak, gunakan nama bagian atau bab sesuai pengaturan referensi yang disetujui pembimbing dan simpan nomor PDF sebagai catatan kerja.', '',
    '## Matriks seluruh penggunaan sitasi', '',
    '| ID | Paragraf latar belakang | Sumber | Klaim yang diperiksa | Halaman yang diperiksa | Status |',
    '| --- | ---: | --- | --- | --- | --- |',
]
for row in rows:
    claim = row['claim'][:105] + ('...' if len(row['claim']) > 105 else '')
    report.append(f'| {row["id"]} | {row["paragraph"]} | {sources[row["source"]]["author"]} | {claim} | {locations(row)} | {row["status"]} |')

report += ['', '## Bukti dan perbaikan per penggunaan', '',
           'Kata kunci di bawah ini membantu pencarian manual pada sumber, sedangkan uraian temuan merupakan parafrase hasil pembacaan. Pada PDF pindai Agarwal dan Umphress, gunakan halaman gambar karena pencarian teks langsung tidak tersedia.', '']
for row in rows:
    source = sources[row['source']]
    report += [f'### {row["id"]}. {source["author"]}, paragraf {row["paragraph"]}', '',
               f'**Status: {row["status"]}.** Lokasi klaim pada {link("salinan Bab 1", str(HERE / "SALINAN_BAB1_YANG_DIAUDIT.md") + ":" + str(row["draft_line"]))}.', '',
               f'> {row["claim"]}', '',
               f'Sumber primer: {link(source["title"], source["file"])}.', '',
               '| Halaman PDF | Nomor pada lembar | Bagian yang diperiksa |',
               '| ---: | --- | --- |']
    for page, printed, section in row['locations']:
        report.append(f'| {page} | {printed} | {section} |')
    report += ['', f'Kata kunci pencarian: **{row["anchor"]}**.', '',
               row['finding'], '', '**Tindakan yang disarankan:** ' + row['correction'], '']

report += [
    '## Temuan tambahan yang tidak dihitung sebagai 27 penggunaan sitasi', '',
    '### Klaim kebaruan multicabang perlu diperbaiki', '',
    'Kalimat setelah daftar penelitian menyatakan penelitian bimbel umumnya satu cabang dan penelitian multicabang belum menggabungkan kebutuhan sejenis. Klaim luas itu tidak dapat dipertahankan hanya dari daftar sumber ini, sebab Thiovanda sudah menunjukkan pengelolaan cabang, siswa lintas cabang, admin cabang dan head admin, serta penjadwalan dan verifikasi pembayaran.', '',
    'Periksa Thiovanda halaman cetak/PDF 4, khususnya Gambar 9 dan 11 beserta paragraf penjelasnya, lalu PDF 5 untuk pembayaran. Ubah kontribusi ARTHA menjadi perbedaan aturan proses bisnis, kapasitas, alur setoran/penerimaan, hak akses dan evaluasi yang memang belum sama dengan pembanding; jangan mengklaim studi pertama tanpa pencarian yang terdokumentasi.', '',
    '### Waterfall disebut tanpa rujukan tepat pada klaimnya', '',
    'Kalimat tentang Waterfall pada paragraf 10 tidak memiliki sitasi sendiri sebelum kalimat Scrum. Jika perbandingan dipertahankan, Pressman cetak 39-40, PDF 68-69 dapat diperiksa; catatan kaki pada cetak 39 bahkan menyebut adanya feedback loops dalam usulan asli Royce, sehingga ungkapan mutlak tidak dapat berubah perlu dihindari.', '',
    '### Fakta ARTHA tetap memerlukan data kasus', '',
    'Artikel lain tidak membuktikan jumlah tentor, tarif, batas tutup kas, kendala alamat, keterlambatan rekap, atau kesediaan evaluator ARTHA. Gunakan wawancara, observasi dan dokumen mitra untuk fakta-fakta tersebut, sementara jurnal digunakan untuk teori dan pembanding yang jelas atribusinya.', '',
    '### Undang-Undang dan daftar pustaka', '',
    'UU 20/2003 disebut pada paragraf pertama, tetapi bukan salah satu dari 21 PDF yang dipakai dalam 27 sitasi author-year pada audit ini. Untuk klaim hukum pendidikan nonformal, Pasal 26 merupakan lokator yang tepat dan perlu diberi sumber resmi tersendiri; artikel Tiana tidak menggantikan rujukan hukum itu.', '',
    'Pada berkas yang diaudit tidak ditemukan bagian daftar pustaka tersendiri. Karena itu, penilaian cocok isi pada laporan ini belum sama dengan pemeriksaan tuntas seluruh entri bibliografi; semua 21 sumber perlu dicocokkan dengan daftar pustaka proposal, termasuk buku dan prosiding yang tidak berstatus artikel jurnal.', '',
    '## Identitas sumber dan catatan penomoran', '',
]
for sid, source in sources.items():
    report += [f'### {sid}. {source["author"]}', '',
               link(source['title'], source['file']) + '.', '',
               source['note'] + f' Berkas lokal memiliki {len(source["pages"])} halaman PDF.', '']

report += [
    '## Langkah pengecekan manual', '',
    '1. Buka PDF dari tautan sumber pada kartu audit yang dipilih.',
    '2. Pergi ke urutan PDF yang tercantum, kemudian cocokkan nomor yang tercetak pada lembar.',
    '3. Cari nama bagian, tabel, gambar atau kata kunci yang disediakan. Baca paragraf sebelum dan sesudahnya agar konteks objek dan metodenya tidak terlepas.',
    '4. Bandingkan dengan klaim Bab 1 pada salinan audit. Pisahkan isi yang dinyatakan penulis sumber dari penyesuaian rancangan untuk ARTHA.',
    '5. Pertahankan, persempit atau ganti sitasi sesuai status per penggunaan. Gunakan nomor cetak yang sah pada kutipan akhir dan catat nomor PDF untuk penelusuran pribadi.', '',
    '## Batas pemeriksaan dan bukti yang disimpan', '',
    'Isi PDF yang dapat dibaca ditelusuri per halaman, disertai pemeriksaan visual pada sumber dan halaman penting yang bermasalah penomorannya. PDF pindai Agarwal dibaca menggunakan gambar asli dengan OCR sebagai alat bantu, sedangkan nomor cetak Beck tidak disimpulkan dari jumlah halaman edisi cetaknya.', '',
    'Halaman yang disebut tidak mendukung dicatat sebagai hasil penelusuran pada salinan yang tersedia, bukan pernyataan bahwa topik itu tidak mungkin dibahas pada seluruh edisi atau publikasi lain. Audit tidak menyunting Bab 1 dan tidak mengubah PDF sumber; salinan, hash, matriks JSON dan hasil ekstraksi halaman disimpan untuk menjaga keterlacakan pemeriksaan.', '',
    'Metadata tahun Thiovanda dicocokkan dengan [laman penerbit](https://journal.untar.ac.id/index.php/jiksi/article/view/36675). Nomor halaman dan isi pengelolaan cabangnya ditetapkan dari PDF lokal yang dirujuk pada laporan ini.', '',
]
(HERE / 'LAPORAN_AUDIT_SITASI_BAB1.md').write_text('\n'.join(report), encoding='utf-8')

matrix = dict(date='2026-10-25', draft=str(DRAFT), snapshot_sha256=hashlib.sha256(snapshot.encode('utf-8')).hexdigest(),
              scope='Kecocokan isi per penggunaan rujukan; bukan penilaian peringkat jurnal',
              counts=dict(counts), rows=rows,
              sources=[{k: v for k, v in x.items() if k != 'pages'} | {'pdf_pages': len(x['pages'])} for x in sources.values()])
(HERE / 'MATRIKS_KLAIM_DAN_HALAMAN.json').write_text(json.dumps(matrix, ensure_ascii=False, indent=2), encoding='utf-8')

quick = ['# Peta cepat halaman rujukan Bab 1', '',
         'Daftar ini merangkum halaman yang perlu dibuka untuk pengecekan manual. Untuk memutuskan apakah kalimat boleh dipertahankan, gunakan status dan penjelasan pada laporan audit lengkap, sebab halaman terdekat pada klaim tidak didukung bukan halaman pembenaran klaim tersebut.', '',
         '| Sumber | Nomor pada lembar dan urutan PDF | ID penggunaan |',
         '| --- | --- | --- |']
for sid, source in sources.items():
    uses = [r for r in rows if r['source'] == sid]
    locs = []
    for r in uses:
        for page, printed, section in r['locations']:
            label = f'{printed} (PDF {page})'
            if label not in locs:
                locs.append(label)
    quick.append(f'| {link(source["author"], source["file"])} | {"; ".join(locs)} | {", ".join(r["id"] for r in uses)} |')
quick += ['', 'PDF dihitung mulai satu termasuk sampul dan halaman awal. Pada Rams Dimsum, footer tidak konsisten; pada Beck, gunakan nama bab/subbagian dan urutan PDF karena nomor cetak tidak tampil.', '',
          'Temuan paling penting untuk diperiksa lebih dahulu adalah A19 (Scrum), A20 (Prototyping), A24-A25 (RAD), A13 (cabang Jia Jia Education), dan A14 (tabel uji notifikasi WhatsApp). Rincian status semua penggunaan tersedia pada ' + link('laporan audit lengkap', HERE / 'LAPORAN_AUDIT_SITASI_BAB1.md') + '.', '']
(HERE / 'PETA_CEPAT_HALAMAN_RUJUKAN.md').write_text('\n'.join(quick), encoding='utf-8')

print(json.dumps({'rows': len(rows), 'sources': len(sources), 'counts': dict(counts),
                  'snapshot_matches_current': DRAFT.read_bytes() == (HERE / 'SALINAN_BAB1_YANG_DIAUDIT.md').read_bytes()}, ensure_ascii=False))
