"""
generate_lampiran_wawancara.py
==============================
Menyusun naskah Lampiran Wawancara Pemangku Kepentingan Mitra ARTHA
sesuai format tabel lembar kendali wawancara akademik ITK (persis seperti contoh gambar).
Output:
1. Markdown: WAWANCARA/NOTULENSI/LAMPIRAN_NOTULENSI_WAWANCARA_MITRA.md
2. Word DOCX: WAWANCARA/NOTULENSI/LAMPIRAN_WAWANCARA_MITRA_ARTHA.docx
3. Word DOCX: DRAFT PROPOSAL MD/DOCS SKRIPSI/LAMPIRAN_WAWANCARA_MITRA_ARTHA.docx
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml

DATA_WAWANCARA = [
    {
        "ke": "1",
        "tanggal": "28 Juli 2026",
        "pukul": "19.10 WITA - Selesai",
        "narasumber": "Ibu Radit (Mama Radit)",
        "posisi": "Pimpinan Bagian Manajemen dan Keuangan",
        "lokasi": "Kantor Bimbel ARTHA Cabang 5, Balikpapan",
        "agenda": "Inisiasi Penelitian, Penjajakan Awal Kebutuhan Sistem, dan Kesepakatan Kemitraan Tugas Akhir",
        "catatan": [
            "Pihak manajemen Bimbingan Belajar ARTHA secara resmi menyetujui dan menyambut baik pelaksanaan penelitian tugas akhir mahasiswa Program Studi Sistem Informasi ITK untuk digitalisasi proses operasional lembaga.",
            "Pengelolaan operasional pada delapan kantor cabang di wilayah Balikpapan selama puluhan tahun masih bertumpu penuh pada buku besar kertas fisik dan kuitansi manual tanpa adanya integrasi data terpusat.",
            "Mekanisme pendaftaran konvensional mengharuskan calon siswa atau orang tua datang langsung ke kantor cabang, sehingga sering menimbulkan penumpukan antrean fisik dan risiko berkas pendaftaran terselip pada periode tahun ajaran baru.",
            "Manajemen membutuhkan portal web pendaftaran mandiri yang memungkinkan calon siswa memilih cabang bimbingan, tingkatan kelas, dan jadwal belajar secara daring dari rumah.",
            "Pihak mitra berkomitmen mengalokasikan anggaran belanja modal guna menyediakan perangkat komputer tablet Android di meja kasir (frontdesk) setiap cabang untuk pencatatan transaksi pendaftaran dan presensi.",
            "Manajemen menyepakati strategi penerapan bertahap (pilot project) dimulai dari Cabang ARTHA 7 di kawasan Perusda yang memiliki populasi siswa terpadat, yakni mencapai lebih dari empat puluh hingga lima puluh siswa per angkatan.",
            "Ruang lingkup pengembangan sistem informasi difokuskan pada dua modul prioritas paling mendesak, yaitu modul pendaftaran siswa baru dan modul pencatatan transaksi serta pengingat tagihan SPP bulanan.",
            "Sistem baru diwajibkan tetap menyediakan opsi cetak formulir fisik cadangan (hardcopy) guna mengantisipasi gangguan teknis seperti pemadaman listrik atau kendala koneksi internet di lokasi cabang.",
            "Budaya kerja lembaga yang berlandaskan asas kekeluargaan menuntut perancangan antarmuka sistem yang sederhana, ramah pengguna, dan mudah diadaptasi oleh staf administrasi cabang tanpa resistensi operasional."
        ]
    },
    {
        "ke": "2",
        "tanggal": "29 Juli 2026",
        "pukul": "15.30 WITA - Selesai",
        "narasumber": "Bapak Anang (Om Anang)",
        "posisi": "Pimpinan Operasional Teknis Lembaga",
        "lokasi": "Kantor Pusat Bimbel ARTHA, Balikpapan",
        "agenda": "Evaluasi Sistem Informasi Lama, Infrastruktur Server, dan Perancangan Arsitektur Sistem Informasi Multicabang",
        "catatan": [
            "Situs web profil lembaga berbasis WordPress yang sebelumnya dikembangkan oleh pihak ketiga asal Yogyakarta ditinggalkan karena antarmuka yang rumit, kendala keterbatasan memori alokasi server shared hosting, serta ketiadaan modul transaksi keuangan operasional.",
            "Manajemen operasional memutuskan untuk membangun sistem informasi baru secara mandiri dari awal (from scratch) guna memutus ketergantungan terhadap vendor luar kota dan menyesuaikan fitur dengan alur kerja nyata di delapan cabang.",
            "Arsitektur sistem informasi dirancang dengan memisahkan antarmuka menjadi dua zona utama, yaitu halaman publik (landing page) untuk promosi program dan portal internal terproteksi khusus staf kasir serta pimpinan.",
            "Sistem informasi wajib menerapkan kontrol hak akses berbasis peran (Role-Based Access Control) dan isolasi data cabang yang ketat, di mana staf administrasi cabang hanya dapat mengakses data cabangnya sendiri sedangkan Super Admin dapat memantau seluruh cabang secara terpusat.",
            "Kebutuhan mendesak mencakup sentralisasi basis data transaksi cabang untuk memantau volume pendaftaran siswa baru secara waktu nyata (real-time) tanpa menunggu pengiriman buku rekapitulasi fisik.",
            "Sistem dituntut mampu merekam data demografi asal sekolah siswa guna memetakan sebaran pendaftar per jenjang (SD, SMP, SMA) sebagai dasar penentuan strategi promosi dan distribusi brosur pemasaran lembaga.",
            "Pengaturan jadwal mengajar tenaga pendidik (tentor) memerlukan standarisasi tiga sesi harian (15.30, 17.00, dan 19.00 WITA) yang dapat diakses langsung oleh tentor melalui peramban ponsel pintar guna mencegah benturan jam mengajar antarcabang.",
            "Evaluasi logistik kas mengonfirmasi bahwa alur perpindahan dana tunai dan buku rekapan fisik antarcabang selama ini sangat mengandalkan sistem titipan antarguru yang melintas, sehingga memiliki risiko keamanan tinggi dan keterlambatan pelaporan bulanan."
        ]
    },
    {
        "ke": "3",
        "tanggal": "30 Juli 2026",
        "pukul": "14.15 WITA - Selesai",
        "narasumber": "Ibu Radit (Mama Radit)",
        "posisi": "Pimpinan Bagian Keuangan dan Administrasi Operasional",
        "lokasi": "Kantor Administrasi Pusat Bimbel ARTHA, Balikpapan",
        "agenda": "Tata Kelola Keuangan, Struktur Paket Belajar, Kendala Buku Besar A4, dan Rekonsiliasi Pembayaran Bank",
        "catatan": [
            "Bimbingan Belajar ARTHA didirikan secara resmi pada tanggal 10 Oktober 1997 dan saat ini telah menaungi delapan cabang di Balikpapan, namun seluruh pencatatan transaksi pendaftaran dan kas harian masih bertumpu pada lembaran Buku Besar fisik A4.",
            "Struktur tarif SPP bulanan diklasifikasikan berdasarkan jenjang pendidikan (SD, SMP, SMA), frekuensi pertemuan mingguan (dua atau tiga kali seminggu), paket intensif ujian kelulusan, serta biaya cetak buku modul pelajaran tambahan.",
            "Alur transaksi pembayaran terbagi menjadi dua metode, yaitu setoran uang tunai di meja kasir cabang dan pembayaran non-tunai melalui transfer rekening bank atas nama yayasan lembaga (BCA dan Bank Mandiri).",
            "Terjadi kendala rekonsiliasi yang fatal (miss reconciliation) akibat bukti transfer WhatsApp dari orang tua siswa yang sering tidak memuat nama lengkap siswa dan asal cabang, sehingga memicu kesalahan penagihan dan salah catat tunggakan SPP.",
            "Rekapitulasi keuangan di akhir bulan menyita waktu kerja berhari-hari karena pimpinan harus memeriksa lembar demi lembar buku besar dari delapan cabang, menghitung manual dengan kalkulator, dan mencocokkannya dengan buku rekening koran.",
            "Media pencatatan kertas fisik berukuran A4 sangat rentan mengalami kerusakan fisik, basah, sobek, serta tercecer dalam proses pengiriman logistik bulanan antarcabang.",
            "Pimpinan keuangan sangat membutuhkan modul rekonsiliasi kas bank terkomputerisasi yang dilengkapi pencatatan petugas (audit trail) dan dasbor penerimaan harian terpusat untuk memvalidasi dana masuk secara akurat."
        ]
    },
    {
        "ke": "4",
        "tanggal": "20 Oktober 2026",
        "pukul": "15.30 WITA - Selesai",
        "narasumber": "Mbak Agian (Gian)",
        "posisi": "Staf Administrasi dan Kasir Meja Depan (Frontdesk)",
        "lokasi": "Ruang Administrasi Frontdesk Bimbel ARTHA Cabang 5, Balikpapan",
        "agenda": "Operasional Harian Frontdesk, Tata Kelola Pendaftaran Siswa, Kuitansi Fisik, Kartu SPP, Tarif Riil, dan Penjadwalan Tentor",
        "catatan": [
            "Staf meja depan menjalankan peran ganda yang mencakup pelayanan pendaftaran siswa baru, penerimaan pembayaran SPP tunai, pengarsipan kuitansi, pencatatan absensi siswa, komunikasi dengan wali murid, serta penataan jadwal ruangan belajar.",
            "Beban kerja kasir cabang memuncak pada jam-jam sibuk (peak hours) di sore hari menjelang dimulainya sesi kelas bimbingan, sehingga rawan memicu kekeliruan penulisan nomor kuitansi manual.",
            "Setiap pendaftaran siswa baru menghasilkan tiga berkas fisik wajib, yaitu lembar formulir pendaftaran di buku besar A4, kuitansi bukti pembayaran manual rangkap dua, serta kartu kontrol SPP fisik dua belas bulan yang disimpan dalam kotak arsip cabang.",
            "Staf administrasi mengalami kesulitan memvalidasi keabsahan diskon saudara kandung (kakak-adik) karena arsip data saudara yang pernah belajar pada tahun ajaran sebelumnya tersimpan di gudang atau kantor pusat, sehingga verifikasi hanya berdasar pada pengakuan lisan wali murid.",
            "Pembagian ruangan kelas di cabang menerapkan batas kapasitas maksimal sepuluh hingga lima belas siswa per sesi, namun staf meja depan belum memiliki alat bantu visual otomatis untuk memantau keterisian kuota kelas secara real-time.",
            "Mekanisme penyetoran uang kas fisik dan buku besar A4 bulanan ke kantor pusat dilakukan melalui titipan kepada guru senior atau kepala cabang yang melintas, yang memiliki risiko keamanan tinggi terhadap kehilangan dana tunai di perjalanan.",
            "Pengaturan jadwal mengajar tentor disusun secara manual bersama Kepala Cabang berdasarkan jam luang pengajar, dengan agenda rapat koordinasi guru setiap seminggu sekali dan rapat evaluasi staf cabang sebulan sekali bersama manajemen pusat.",
            "Staf meja depan menyatakan dukungan penuh terhadap pengembangan sistem informasi berbasis web karena akan mempermudah pencarian riwayat siswa, mengesahkan pelunasan SPP secara instan, dan mengontrol kapasitas ruangan kelas tanpa perlu membuka buku besar fisik secara berulang."
        ]
    }
]

def build_markdown():
    lines = [
        "# LAMPIRAN: LEMBAR KENDALI DAN NOTULENSI WAWANCARA PEMANGKU KEPENTINGAN MITRA",
        "## Mitra Penelitian: Bimbingan Belajar Artha Balikpapan (Bimbel ARTHA)",
        "",
        "Berikut merupakan dokumentasi lembar kendali pelaksanaan wawancara mendalam bersama pemangku kepentingan (*stakeholders*) Bimbingan Belajar Artha Balikpapan guna menggali permasalahan operasional, analisis kebutuhan sistem, serta justifikasi perancangan sistem informasi manajemen multicabang.",
        ""
    ]

    for item in DATA_WAWANCARA:
        lines.append(f"### Lembar Wawancara Ke-{item['ke']}")
        lines.append("")
        
        # HTML Table for perfect visual matching and copy-paste compatibility
        lines.append('<table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%; font-family: \'Times New Roman\', serif; font-size: 11pt;">')
        lines.append("  <tr>")
        lines.append('    <td style="width: 18%; font-weight: bold;">Wawancara ke</td>')
        lines.append(f'    <td style="width: 27%;">{item["ke"]}</td>')
        lines.append('    <td style="width: 13%; font-weight: bold;">Tanggal</td>')
        lines.append(f'    <td style="width: 27%;">{item["tanggal"]}</td>')
        lines.append('    <td rowspan="3" style="width: 15%; text-align: center; vertical-align: top; font-weight: bold;">Tanda Tangan<br><br><br><br></td>')
        lines.append("  </tr>")
        lines.append("  <tr>")
        lines.append('    <td style="font-weight: bold;">Nama Narasumber</td>')
        lines.append(f'    <td>{item["narasumber"]}</td>')
        lines.append('    <td style="font-weight: bold;">Pukul</td>')
        lines.append(f'    <td>{item["pukul"]}</td>')
        lines.append("  </tr>")
        lines.append("  <tr>")
        lines.append('    <td style="font-weight: bold;">Posisi</td>')
        lines.append(f'    <td>{item["posisi"]}</td>')
        lines.append('    <td style="font-weight: bold;">Lokasi</td>')
        lines.append(f'    <td>{item["lokasi"]}</td>')
        lines.append("  </tr>")
        lines.append("  <tr>")
        lines.append('    <td style="font-weight: bold;">Agenda</td>')
        lines.append(f'    <td colspan="4">{item["agenda"]}</td>')
        lines.append("  </tr>")
        lines.append("  <tr>")
        lines.append('    <td colspan="5" style="font-weight: bold; background-color: #f2f2f2;">Catatan Wawancara</td>')
        lines.append("  </tr>")
        lines.append("  <tr>")
        lines.append('    <td colspan="5" style="vertical-align: top;">')
        lines.append('      <ul style="margin-top: 6px; margin-bottom: 6px; padding-left: 20px; line-height: 1.4;">')
        for b in item["catatan"]:
            lines.append(f"        <li>{b}</li>")
        lines.append("      </ul>")
        lines.append("    </td>")
        lines.append("  </tr>")
        lines.append("</table>")
        lines.append("")
        lines.append("<hr>")
        lines.append("")

    md_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\NOTULENSI\LAMPIRAN_NOTULENSI_WAWANCARA_MITRA.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Berhasil membuat berkas Markdown di: {md_path}")

def set_cell_border(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(r'''
        <w:tcBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
            <w:top w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:left w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="000000"/>
            <w:right w:val="single" w:sz="6" w:space="0" w:color="000000"/>
        </w:tcBorders>
    ''')
    tcPr.append(tcBorders)

def build_docx(target_path):
    doc = docx.Document()
    
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.18)    # 3 cm
        section.bottom_margin = Inches(1.18) # 3 cm
        section.left_margin = Inches(1.57)   # 4 cm
        section.right_margin = Inches(1.18)  # 3 cm

    # Document Header Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("LAMPIRAN\nLEMBAR KENDALI DAN NOTULENSI WAWANCARA MITRA")
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(12)
    run_title.font.bold = True
    p_title.paragraph_format.space_after = Pt(18)

    for item in DATA_WAWANCARA:
        table = doc.add_table(rows=6, cols=5)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False

        col_widths = [Inches(1.2), Inches(1.8), Inches(0.9), Inches(1.8), Inches(1.1)]
        for row in table.rows:
            for i, w in enumerate(col_widths):
                row.cells[i].width = w

        # Row 0: Wawancara ke | <num> | Tanggal | <date> | Tanda Tangan
        table.cell(0, 0).text = "Wawancara ke"
        table.cell(0, 1).text = item["ke"]
        table.cell(0, 2).text = "Tanggal"
        table.cell(0, 3).text = item["tanggal"]
        table.cell(0, 4).text = "Tanda Tangan"

        # Row 1: Nama Narasumber | <name> | Pukul | <time>
        table.cell(1, 0).text = "Nama Narasumber"
        table.cell(1, 1).text = item["narasumber"]
        table.cell(1, 2).text = "Pukul"
        table.cell(1, 3).text = item["pukul"]

        # Row 2: Posisi | <pos> | Lokasi | <loc>
        table.cell(2, 0).text = "Posisi"
        table.cell(2, 1).text = item["posisi"]
        table.cell(2, 2).text = "Lokasi"
        table.cell(2, 3).text = item["lokasi"]

        # Merge signature column (Col 4, Rows 0, 1, 2)
        c_sig = table.cell(0, 4)
        c_sig.merge(table.cell(1, 4)).merge(table.cell(2, 4))
        p_sig = c_sig.paragraphs[0]
        p_sig.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_sig.runs[0].font.bold = True
        p_sig.runs[0].font.name = "Times New Roman"
        p_sig.runs[0].font.size = Pt(10)
        c_sig.add_paragraph("\n\n\n")

        # Row 3: Agenda
        table.cell(3, 0).text = "Agenda"
        c_agenda = table.cell(3, 1)
        c_agenda.merge(table.cell(3, 2)).merge(table.cell(3, 3)).merge(table.cell(3, 4))
        c_agenda.text = item["agenda"]

        # Row 4: Catatan Wawancara
        c_cat_header = table.cell(4, 0)
        c_cat_header.merge(table.cell(4, 1)).merge(table.cell(4, 2)).merge(table.cell(4, 3)).merge(table.cell(4, 4))
        c_cat_header.text = "Catatan Wawancara"
        p_ch = c_cat_header.paragraphs[0]
        p_ch.runs[0].font.bold = True
        p_ch.runs[0].font.name = "Times New Roman"
        p_ch.runs[0].font.size = Pt(11)

        # Row 5: Bullet list content
        c_content = table.cell(5, 0)
        c_content.merge(table.cell(5, 1)).merge(table.cell(5, 2)).merge(table.cell(5, 3)).merge(table.cell(5, 4))
        
        p_first = c_content.paragraphs[0]
        p_first.text = f"•   {item['catatan'][0]}"
        p_first.paragraph_format.space_after = Pt(4)
        p_first.paragraph_format.line_spacing = 1.15
        p_first.runs[0].font.name = "Times New Roman"
        p_first.runs[0].font.size = Pt(10)

        for b in item["catatan"][1:]:
            p = c_content.add_paragraph(f"•   {b}")
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.line_spacing = 1.15
            p.runs[0].font.name = "Times New Roman"
            p.runs[0].font.size = Pt(10)

        # Style all cells in table
        for r_idx, row in enumerate(table.rows):
            for c_idx, cell in enumerate(row.cells):
                set_cell_border(cell)
                for p in cell.paragraphs:
                    for r in p.runs:
                        r.font.name = "Times New Roman"
                        if r_idx < 4 and c_idx in [0, 2]:
                            r.font.bold = True
                        if r.font.size is None:
                            r.font.size = Pt(10)

        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_after = Pt(24)

    doc.save(target_path)
    print(f"Berhasil membuat berkas Word DOCX di: {target_path}")

if __name__ == "__main__":
    build_markdown()
    out_docx_1 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\WAWANCARA\NOTULENSI\LAMPIRAN_WAWANCARA_MITRA_ARTHA.docx"
    out_docx_2 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\LAMPIRAN_WAWANCARA_MITRA_ARTHA.docx"
    build_docx(out_docx_1)
    build_docx(out_docx_2)
