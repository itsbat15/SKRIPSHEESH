import fitz, os

pdf_dir = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF'

# Targets with updated notes (no city/region locations)
targets = [
    # -------------------------------------------------------------
    # 1. Fajriansyah dkk. (2026)
    # -------------------------------------------------------------
    {
        'file': '03_Fajriansyah_dkk_2026_JRIS_SINTA3.pdf',
        'row': 1,
        'author': 'Fajriansyah dkk., 2026',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'manually through Google Forms, spreadsheets, and WhatsApp communications',
                'note': 'Pengelolaan operasional bimbingan belajar Bee Hive Tutoring masih mengandalkan Google Forms, spreadsheets, dan grup WhatsApp. Kondisi konvensional tersebut memicu penjadwalan kelas tutor tidak terstruktur, data peserta didik dan tutor tercecer, pelaporan hasil evaluasi belajar terhambat, serta minimnya proteksi keamanan data akademik lembaga.'
            },
            {
                'cat': 'Metode',
                'search': 'mengacu pada model Waterfall yang dikemukakan oleh',
                'note': 'Penelitian ini menerapkan model Waterfall konvensional dengan tahapan terstruktur mulai dari analisis kebutuhan hingga pengujian sistem.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'otomatis dalam waktu kurang dari 2 detik setelah tombol submit ditekan',
                'note': 'Penelitian ini menghasilkan Sistem Informasi Bimbingan Belajar (SIMB) berbasis web menggunakan kerangka kerja Laravel dan basis data SQLite yang menyediakan layanan pendaftaran daring mandiri, pencatatan log belajar tutor, sinkronisasi rekapitulasi data melalui Google Sheets API, serta pengiriman email konfirmasi akun melalui Brevo SMTP. Pengujian fungsional direncanakan menggunakan metode Black Box Testing. Penerapan sistem ini berhasil memangkas durasi pemrosesan verifikasi pendaftaran oleh sistem menjadi di bawah dua detik dibandingkan pemrosesan manual sebelumnya yang memakan waktu sepuluh hingga lima belas menit, serta meniadakan potensi benturan jadwal mengajar tutor hingga nol persen.'
            },
            {
                'cat': 'Keterkaitan (Bukti Presensi Saran Masa Depan)',
                'search': 'disarankan untuk menambahkan modul presensi digital guna melacak kehadiran',
                'note': 'Keterkaitan terletak pada kesamaan domain digitalisasi administrasi operasional bimbingan belajar nonformal. Perbedaannya, sistem Bee Hive belum dilengkapi modul manajemen multicabang terpusat dan modul presensi kehadiran terintegrasi (presensi masih berupa saran penelitian masa depan), sedangkan sistem Bimbel ARTHA mengelola delapan kantor cabang terpadu dengan pembatasan hak akses berbasis peran, pencatatan presensi siswa, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 2. Tiana dan Gunanto (2026)
    # -------------------------------------------------------------
    {
        'file': '15_Tiana_Gunanto_2026_JUKTISI_SINTA4.pdf',
        'row': 2,
        'author': 'Tiana dan Gunanto, 2026',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'Bimbingan Belajar Texas Kotabumi di Kabupaten Lampung Utara',
                'note': 'Tata kelola administrasi pendaftaran siswa, pengelolaan level paket belajar, dan pencatatan riwayat pembayaran pada bimbingan belajar Texas masih dilaksanakan secara konvensional. Kondisi ini mengakibatkan inefisiensi waktu operasional staf, memperbesar kerentanan kesalahan pencatatan data bimbingan, serta menyulitkan penelusuran riwayat iuran kursus siswa.'
            },
            {
                'cat': 'Metode',
                'search': 'Pengujian dilakukan menggunakan pengujian black-box',
                'note': 'Pengujian sistem menggunakan metode Black Box Testing pada enam skenario fungsi utama guna memvalidasi fungsionalitas sistem informasi bimbingan belajar berbasis web mobile.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'texas_kelas yang mendefinisikan kursus dengan level yang terhubung ke tabel',
                'note': 'Penelitian ini menghasilkan sistem informasi bimbingan belajar berbasis web mobile yang memfasilitasi modul manajemen akun pengguna, pengelolaan master data siswa, pengaturan level kursus, pengalokasian peserta kursus ke dalam kelas, serta pencatatan riwayat pembayaran iuran bimbingan. Pengujian sistem menggunakan metode Black Box Testing pada enam skenario fungsi utama membuktikan bahwa seluruh fungsionalitas sistem berjalan sesuai dengan spesifikasi rancangan.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'suksesnya penciptaan sistem informasi web-mobile yang interaktif',
                'note': 'Keterkaitan terletak pada kesamaan domain digitalisasi tata kelola administrasi dan pembayaran iuran bimbingan belajar nonformal. Perbedaannya, sistem pada penelitian Tiana dan Gunanto dirancang untuk satu unit lembaga mandiri tanpa pengelolaan multicabang terpadu, tidak mengintegrasikan modul rekonsiliasi mutasi kas bank, serta tidak menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 3. Zakaria dkk. (2023)
    # -------------------------------------------------------------
    {
        'file': '05_Zakaria_dkk_2023_JuTISI_SINTA3.pdf',
        'row': 3,
        'author': 'Zakaria dkk., 2023',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'Feng Huang Mandarin Course Bali untuk menunjang pendaftaran siswa',
                'note': 'Tata kelola administrasi pembayaran pada lembaga kursus bahasa Mandarin Feng Huang masih dijalankan secara semi-manual menggunakan pembukuan spreadsheet dan kuitansi fisik. Prosedur tersebut memakan waktu lama, membuka celah potensi penyalahgunaan keuangan, serta menyulitkan penelusuran status keaktifan murid dan penyusunan laporan penerimaan kas berkala.'
            },
            {
                'cat': 'Metode',
                'search': 'telah diuji menggunakan Alpha Testing dan Beta Testing',
                'note': 'Pengujian sistem melalui Alpha Testing terhadap tujuh skenario fungsionalitas dan Beta Testing kepada pengguna akhir membuktikan bahwa seluruh fungsi transaksi berjalan sesuai dengan kebutuhan operasional lembaga.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'Sistem Pembayaran Kursus MandarinPro sudah diujicoba',
                'note': 'Penelitian ini menghasilkan sistem informasi pembayaran kursus berbasis Desktop Windows (MandarinPro) yang mengotomatisasi registrasi siswa baru, pemrosesan pembayaran uang les, pelacakan riwayat pembayaran murid, serta penerbitan laporan penerimaan kas harian dan bulanan.'
            },
            {
                'cat': 'Keterkaitan (Bukti Platform Desktop Windows)',
                'search': 'Aplikasi ini masih berbasis desktop, sehingga hanya digunakan di sistem operasi Windows',
                'note': 'Keterkaitan terletak pada digitalisasi administrasi pembayaran iuran pendidikan kursus dan pelaporan transaksi kas masuk. Perbedaannya, sistem MandarinPro dibangun berbasis aplikasi desktop Windows untuk satu lembaga kursus mandiri, sedangkan sistem Bimbel ARTHA dirancang berbasis aplikasi web terpadu untuk delapan kantor cabang, menerapkan rekonsiliasi mutasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 4. Ahadi, Pariyadi, Djauhari (2025)
    # -------------------------------------------------------------
    {
        'file': '10_Ahadi_dkk_2025_Djtechno_SINTA4.pdf',
        'row': 4,
        'author': 'Ahadi dkk., 2025',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'Hotel Royal Heritage Jambi sudah menggunakan sistem informasi manajemen hotel',
                'note': 'Manajemen Hotel Royal Heritage merencanakan ekspansi penambahan unit cabang perhotelan di berbagai wilayah kabupaten dan kota lain. Sistem informasi manajemen eksisting belum mendukung pengelolaan multicabang, sehingga menyulitkan manajemen pusat dalam mengelola data cabang baru, reservasi kamar, dan pemantauan transaksi reservasi secara terpadu.'
            },
            {
                'cat': 'Metode',
                'search': 'menerapkan pendekatan waterfall-iterative',
                'note': 'Metode pengembangan menggunakan pendekatan waterfall-iterative, di mana fase analisis, perancangan, dan implementasi dieksekusi secara iteratif sebelum sistem dideploy.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'sudah layak untuk dilanjutkan ke tahap deployment',
                'note': 'Penelitian ini menghasilkan sistem informasi manajemen multicabang berbasis web yang memfasilitasi pendaftaran unit cabang baru, pengelolaan kamar, pencatatan reservasi tamu, pembayaran reservasi, serta pemrosesan check in pada masing-masing cabang. Pengujian fungsional menggunakan Black Box Testing pada lima skenario utama membuktikan sistem berjalan sesuai rancangan dan layak untuk dilanjutkan ke tahap penerapan.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'Master data cabang hotel. Modul ini diperlukan untuk menentukan cabang hotel',
                'note': 'Keterkaitan terletak pada penerapan arsitektur sistem informasi multicabang terintegrasi untuk mendukung ekspansi unit operasional. Perbedaannya, sistem Ahadi dkk. diterapkan pada sektor industri perhotelan dengan metode waterfall-iterative, sedangkan sistem Bimbel ARTHA diterapkan pada domain operasional bimbingan belajar delapan cabang dengan validasi kuota kelas, rekonsiliasi kas bank, serta dikembangkan menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 5. Hendri dkk. (2025)
    # -------------------------------------------------------------
    {
        'file': '04_Hendri_dkk_2025_JUSTIAN_SINTA3.pdf',
        'row': 5,
        'author': 'Hendri dkk., 2025',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'seperti kesalahan pencatatan dan keterlambatan laporan',
                'note': 'Tata kelola penerimaan kas pembayaran Sumbangan Pembinaan Pendidikan (SPP) pada Yayasan Semesta Khatulistiwa masih menggunakan pencatatan buku kas manual. Kondisi tersebut memicu ketidakefisienan pembukuan, keterlambatan penyusunan rekapitulasi pembayaran siswa, serta memperbesar risiko selisih catatan penerimaan kas bendahara.'
            },
            {
                'cat': 'Metode',
                'search': 'designing a prototype system using Figma, supported by UML',
                'note': 'Metode Waterfall diterapkan pada tahapan analisis kebutuhan dan perancangan prototipe antarmuka sistem menggunakan Figma serta pemodelan UML.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'untuk membayar atau mencetak bukti pembayaran',
                'note': 'Penelitian ini menghasilkan rancangan prototipe antarmuka sistem informasi akuntansi penerimaan kas SPP berbasis Figma beserta pemodelan diagram UML. Rancangan sistem memodelkan menu pencatatan pembayaran SPP, visualisasi opsi kanal pembayaran nontunai, pencetakan bukti pembayaran, serta ekspor rekapitulasi pembayaran siswa ke format PDF dan Excel.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'bisa mencetak laporan setiap tahunnya dalam format PDF atau Excel',
                'note': 'Keterkaitan terletak pada fokus tata kelola penerimaan kas pembayaran SPP pendidikan dan pencatatan riwayat transaksi siswa. Perbedaannya, penelitian Hendri dkk. terbatas pada perancangan prototipe antarmuka Figma pada satu yayasan tanpa tahap pengkodean dan pengujian sistem, sedangkan sistem Bimbel ARTHA membangun aplikasi web operasional terintegrasi pada delapan cabang dengan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 6. Sudirman dan Tristianti (2021)
    # -------------------------------------------------------------
    {
        'file': '11_Sudirman_Tristianti_2021_MEANS_SINTA4.pdf',
        'row': 6,
        'author': 'Sudirman dan Tristianti, 2021',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'Rekonsiliasi bank sangatlah penting sebagai pengendalian intern perusahaan',
                'note': 'Pengendalian transaksi kas pada CV. Lisa Pratama belum menerapkan proses rekonsiliasi kas bank secara berkala dan terkomputerisasi. Kondisi tersebut menyebabkan perusahaan tidak dapat memastikan kesesuaian saldo antara catatan kas internal dengan rekening koran bank, sehingga menyulitkan evaluasi arus kas dan pengendalian internal.'
            },
            {
                'cat': 'Metode',
                'search': 'pengembangan sistem dengan metode Prototyping untuk menghasilkan',
                'note': 'Metode penelitian menggunakan Research and Development (R&D) dengan pendekatan siklus hidup pengembangan sistem Prototyping.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'rekening Bank BRI perusahaan. Penerimaan kas maupun pengeluaran kas',
                'note': 'Penelitian ini menghasilkan sistem informasi pengendalian kas bank yang menyediakan antarmuka pencatatan penerimaan kas, formulir pengeluaran kas, serta fasilitas pencatatan data rekening koran bank guna mempermudah pembuatan laporan rekonsiliasi kas bank. Sistem ini dilengkapi dengan pemisahan hak akses antara staf kasir dan pimpinan untuk menjaga tertib administrasi keuangan.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'bisa mengakses informasi sesuai hak akses yang ditentukan',
                'note': 'Keterkaitan terletak pada penerapan konsep rekonsiliasi mutasi rekening bank guna mencocokkan pencatatan kas internal dengan rekening bank. Perbedaannya, penelitian Sudirman dan Tristianti berfokus pada pengendalian kas entitas bisnis tunggal menggunakan pendekatan prototyping, sedangkan sistem Bimbel ARTHA mengintegrasikan verifikasi mutasi bank ke dalam arsitektur web multicabang bimbingan belajar dengan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 7. Khafidhoh, Febrianti, Sujono (2026)
    # -------------------------------------------------------------
    {
        'file': '12_Khafidhoh_dkk_2026_JTI_SINTA4.pdf',
        'row': 7,
        'author': 'Khafidhoh dkk., 2026',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'Megaluh 7059 was previously conducted manually, which led to potential',
                'note': 'Pengelolaan jadwal kegiatan belajar mengajar pada Bimbingan Belajar Anak Hebat (AHE) masih dilakukan secara manual. Mekanisme konvensional tersebut berpotensi memicu bentrokan jam mengajar tutor, alokasi beban mengajar guru yang tidak merata, serta menyulitkan penyesuaian jadwal belajar siswa.'
            },
            {
                'cat': 'Metode',
                'search': 'development method uses the Waterfall model',
                'note': 'Metode pengembangan perangkat lunak menggunakan model Waterfall yang dipadukan dengan optimasi Algoritma Genetika.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'lebih terstruktur dan meminimalkan bentrok dibandingkan metode konvensional',
                'note': 'Penelitian ini menghasilkan sistem informasi penjadwalan bimbingan belajar berbasis web yang menerapkan optimasi Algoritma Genetika dengan mempertimbangkan ketersediaan jam mengajar guru, preferensi waktu belajar siswa, dan pemerataan alokasi mengajar. Pengujian sistem membuktikan bahwa fungsionalitas utama sistem berjalan sesuai perancangan dan mampu meminimalkan potensi konflik jadwal mengajar guru secara terkomputerisasi.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'seluruh fungsi utama sistem berjalan sesuai dengan perancangan',
                'note': 'Keterkaitan terletak pada pengelolaan otomasi penjadwalan bimbingan belajar guna mencegah konflik waktu mengajar tentor. Perbedaannya, sistem bimbingan belajar AHE berfokus pada penjadwalan satu lokasi dengan optimasi algoritma genetika tanpa validasi batas kuota fisik ruangan, sedangkan sistem Bimbel ARTHA menggabungkan validasi kuota kapasitas ruang kelas dan ketersediaan tentor pada delapan cabang menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 8. Yuanita, Wijayanto, Cahyono (2022)
    # -------------------------------------------------------------
    {
        'file': '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf',
        'row': 8,
        'author': 'Yuanita dkk., 2022',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'membuat sulitnya menyusun jadwal mata kuliah',
                'note': 'Penyusunan jadwal perkuliahan terintegrasi di lingkungan perguruan tinggi yang melibatkan banyak kelas dan ruangan menghadapi kendala lamanya durasi kompilasi data manual serta rentannya jadwal ganda perkuliahan. Proses manual tersebut memerlukan waktu berminggu-minggu serta menyulitkan penyesuaian alokasi jadwal mengajar dosen.'
            },
            {
                'cat': 'Metode',
                'search': 'tahapan yang dilakukan hanya sampai dengan tahap test',
                'note': 'Metode pengembangan menerapkan pendekatan DevOps yang difokuskan pada tahapan perencanaan, pengkodean, build, dan pengujian front-end.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'mengenerate tigas model jadwal mata kuliah',
                'note': 'Penelitian ini menghasilkan sistem informasi penjadwalan perkuliahan terintegrasi pada sisi front-end berbasis React.js yang menyediakan antarmuka pengelolaan data master jadwal serta penyajian visual tiga model rekomendasi jadwal hasil generate backend. Pengujian fungsionalitas front-end melalui Black Box Testing membuktikan bahwa antarmuka pengguna berhasil terhubung dengan antarmuka pemrograman aplikasi (API) dan seluruh komponen fungsi berjalan valid sesuai kebutuhan pengguna.'
            },
            {
                'cat': 'Keterkaitan (Bukti Front-End Saja)',
                'search': 'PERANCANGAN FRONT-END SISTEM PENJADWALAN MATA KULIAH',
                'note': 'Keterkaitan terletak pada digitalisasi perancangan jadwal kegiatan belajar guna mempermudah pengelolaan alokasi waktu dan ruangan. Perbedaannya, penelitian Yuanita dkk. berfokus pada pengembangan antarmuka front-end perkuliahan dalam tim proyek MBKM dengan pendekatan DevOps, sedangkan sistem Bimbel ARTHA membangun sistem penuh (full-stack) mandiri untuk delapan cabang bimbingan belajar dengan validasi kapasitas fisik kelas menggunakan metode Personal Extreme Programming (PxP).'
            }
        ]
    },
    # -------------------------------------------------------------
    # 9. Musofa, Fadli, Murniati, Fahmi (2025)
    # -------------------------------------------------------------
    {
        'file': '13_Musofa_dkk_2025_JTIIK_SINTA2.pdf',
        'row': 9,
        'author': 'Musofa dkk., 2025',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'pengunjung dalam buku fisik',
                'note': 'Pencatatan data tamu pada Dinas Komunikasi dan Informatika masih menggunakan buku register fisik. Mekanisme manual tersebut menyulitkan pencarian arsip riwayat kunjungan, rentan terhadap kerusakan atau kehilangan data, serta memperbesar risiko kesalahan pencatatan data identitas tamu dinas.'
            },
            {
                'cat': 'Metode',
                'search': 'Metode PXP yang terdiri dari beberapa tahapan',
                'note': 'Metode yang digunakan adalah Personal Extreme Programming (PxP) dengan tujuh tahapan terstruktur mulai dari requirement hingga retrospective.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'pemindaian QR mencapai 312 ms dan tingkat akurasi verifikasi identitas tamu sebesar 98.7%',
                'note': 'Penelitian ini menghasilkan Aplikasi Buku Tamu Digital berbasis web yang memfasilitasi pengisian data kunjungan oleh tamu melalui pemindaian tautan QR Code serta penyediaan dashboard statistik kunjungan dan ekspor laporan PDF bagi staf dinas. Pengujian fungsionalitas menggunakan Black Box Testing membuktikan delapan puluh skenario uji berhasil dijalankan dengan persentase seratus persen. Hasil pengujian performa menunjukkan waktu tanggap sistem sebesar 312 ms serta akurasi verifikasi identitas tamu sebesar 98,7%.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'verifikasi identitas tamu mencapai 98,7% dengan standar deviasi',
                'note': 'Keterkaitan terletak pada penerapan metodologi Personal Extreme Programming (PxP) secara komprehensif mulai dari analisis kebutuhan hingga retrospective guna membangun aplikasi web yang teruji fungsionalitas dan performanya. Perbedaannya, penelitian Musofa dkk. diterapkan pada sistem pelayanan tamu instansi pemerintah daerah satu lokasi, sedangkan sistem Bimbel ARTHA menerapkan PxP pada sistem operasional bisnis delapan cabang bimbingan belajar dengan transaksi kas dan validasi kuota ruang kelas.'
            }
        ]
    },
    # -------------------------------------------------------------
    # 10. Apriyanti, Wati, Najaf (2024)
    # -------------------------------------------------------------
    {
        'file': '14_Apriyanti_dkk_2024_JATI_SINTA4.pdf',
        'row': 10,
        'author': 'Apriyanti dkk., 2024',
        'items': [
            {
                'cat': 'Permasalahan',
                'search': 'PT. Mutiara Putri Gemilang merupakan sebuah perusahaan properti yang berlokasi',
                'note': 'Pengelolaan dan pemasaran penjualan tanah kavling pada PT Mutiara Putri Gemilang masih mengandalkan pencatatan pembukuan manual dan penyebaran brosur fisik. Kondisi tersebut membatasi jangkauan promosi properti, memperbesar risiko catatan transaksi penjualan tercecer, serta memperlambat proses validasi data pembelian konsumen.'
            },
            {
                'cat': 'Metode',
                'search': 'menggunakan metode Personal Extreme Programming (PXP)',
                'note': 'Metode pengembangan menggunakan Personal Extreme Programming (PxP) yang dirancang untuk pengembang mandiri dengan perulangan iterasi adaptif.'
            },
            {
                'cat': 'Hasil Penelitian',
                'search': 'mencapai keberhasilan 91% yang menandakan sistem termasuk dalam kategori sangat baik',
                'note': 'Penelitian ini menghasilkan situs web pemasaran dan penjualan properti (E-Kavling) yang memfasilitasi penelusuran daftar kavling, formulir pembelian tanah, pengunggahan berkas administrasi pembeli, serta validasi bukti pembayaran oleh direktur. Pengujian fungsionalitas menggunakan Black Box Testing pada fitur validasi berkas berjalan sesuai rancangan, serta evaluasi penerimaan pengguna (UAT) yang melibatkan lima belas responden memperoleh skor persentase sebesar 91% dengan kategori Sangat Baik.'
            },
            {
                'cat': 'Keterkaitan',
                'search': 'penjualan properti disertai validasi berkas pembelian dan unggah bukti pembayaran',
                'note': 'Keterkaitan terletak pada penerapan metodologi Personal Extreme Programming (PxP) dalam merancang alur transaksi penjualan daring dan validasi berkas bukti pembayaran. Perbedaannya, sistem E-Kavling menangani objek penjualan tanah kavling tunggal tanpa modul rekonsiliasi mutasi rekening kas bank, sedangkan sistem Bimbel ARTHA mengintegrasikan rekonsiliasi mutasi bank, manajemen kuota kelas, dan administrasi operasional pada delapan kantor cabang bimbingan belajar.'
            }
        ]
    }
]

def make_rc_string(content):
    c_xml = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    lines = c_xml.split('\n')
    formatted_lines = []
    for idx, l in enumerate(lines):
        if idx == 0:
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:10pt;">{l}</span>')
        elif l.startswith('Kategori:'):
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:9.5pt;">{l}</span>')
        elif l.startswith('Kalimat Skripsi ARTHA:'):
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:9.5pt;">{l}</span>')
        else:
            formatted_lines.append(f'<span style="color:#000000;font-weight:normal;font-size:9.5pt;">{l}</span>')
    
    body_inner = '<br/>'.join(formatted_lines)
    rc = (
        '<?xml version="1.0"?>'
        '<body xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/" '
        'xfa:APIVersion="Acrobat:8.0.0" xfa:spec="2.0.2" '
        'style="font-size:9.5pt;text-align:left;color:#000000;font-weight:normal;font-style:normal;font-family:Helvetica,sans-serif">'
        f'<p dir="ltr">{body_inner}</p>'
        '</body>'
    )
    rc_pdf = rc.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    return rc_pdf

print('=== Re-synchronizing 10 PDFs with Clean Text (No Locations) and Solid Black Hover Text ===')

total_synced = 0

for t in targets:
    p = os.path.join(pdf_dir, t['file'])
    doc = fitz.open(p)
    doc_synced = 0
    
    for item in t['items']:
        found = False
        for pno in range(len(doc)):
            page = doc[pno]
            rects = page.search_for(item['search'])
            if rects:
                # Find existing green annot on this rect or update it
                matched_annot = None
                for a in page.annots():
                    s = a.colors.get('stroke')
                    if s and abs(s[0] - 0.1) < 0.05 and abs(s[1] - 0.75) < 0.05:
                        # Check distance between rects
                        if abs(a.rect.x0 - rects[0].x0) < 50 and abs(a.rect.y0 - rects[0].y0) < 50:
                            matched_annot = a
                            break
                
                popup_text = f"[ARTHA BAB 2 - TABEL 2.6: PENELITIAN TERDAHULU]\nKategori: {item['cat']} (Baris {t['row']} - {t['author']})\nKalimat Skripsi ARTHA:\n\"{item['note']}\""
                
                if matched_annot:
                    matched_annot.set_info(
                        title=f"ARTHA BAB 2 - Baris {t['row']}",
                        content=popup_text
                    )
                    matched_annot.update()
                    xref = matched_annot.xref
                else:
                    new_a = page.add_highlight_annot(rects)
                    new_a.set_colors(stroke=(0.1, 0.75, 0.2))
                    new_a.set_info(
                        title=f"ARTHA BAB 2 - Baris {t['row']}",
                        content=popup_text
                    )
                    new_a.update()
                    xref = new_a.xref
                
                # Invert styling to solid black
                doc.xref_set_key(xref, 'DS', '(font: Helvetica,sans-serif 9.5pt; text-align:left; color:#000000)')
                doc.xref_set_key(xref, 'DA', '(/Helv 10 Tf 0 g)')
                rc_str = make_rc_string(popup_text)
                doc.xref_set_key(xref, 'RC', f'({rc_str})')
                
                doc_synced += 1
                total_synced += 1
                found = True
                break
        if not found:
            print(f"  WARNING: Search failed for '{item['search']}' in {t['file']}")
            
    temp_p = p + '.temp.pdf'
    doc.save(temp_p, deflate=True)
    doc.close()
    os.replace(temp_p, p)
    print(f"SUCCESS: Synchronized {doc_synced} items in {t['file']}")

print(f"\nALL 10 PDFs Synchronized! Total annotations updated: {total_synced}/40")

