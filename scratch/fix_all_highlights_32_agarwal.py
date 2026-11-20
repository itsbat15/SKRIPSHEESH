import fitz
import shutil
import os

pdf_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.pdf"
backup_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming_backup.pdf"

if not os.path.exists(backup_path):
    shutil.copy2(pdf_path, backup_path)
    print("Backup created at:", backup_path)

# Always start from clean backup
shutil.copy2(backup_path, pdf_path)
doc = fitz.open(pdf_path)

# Keep all pages referenced
pages = [doc[i] for i in range(len(doc))]

# Clear old annotations from all pages
for p in pages:
    for a in list(p.annots()):
        p.delete_annot(a)
print("Cleared old annotations.")

scale = 72.0 / 150.0

def make_quads(line_list):
    quads = []
    for x, y, w, h in line_list:
        x0 = x * scale
        y0 = (y - 1.5) * scale
        x1 = (x + w) * scale
        y1 = (y + h + 1.5) * scale
        quad = fitz.Quad(fitz.Point(x0, y0), fitz.Point(x1, y0), fitz.Point(x0, y1), fitz.Point(x1, y1))
        quads.append(quad)
    return quads

# ==============================================================================
# Citation #1 (Page 1): Abstrak Inisiasi PXP
# ==============================================================================
lines_c1 = [
    (110, 482, 487, 18),
    (110, 504, 487, 18),
    (110, 525, 487, 18),
    (110, 546, 487, 18),
    (109, 567, 161, 18),
    (109, 600, 487, 18),
    (110, 621, 487, 17),
]
annot1 = pages[0].add_highlight_annot(quads=make_quads(lines_c1))
annot1.set_colors(stroke=[1.0, 0.92, 0.0])
annot1.set_info(
    title="Kutipan Skripsi ARTHA (Bab 1 Subbab 1.1 (Hlm. 25), Bab 2 Subbab 2.1.2 (Hlm. 33), & Bab 3 Subbab 3.2 (Hlm. 72) - Abstrak Inisiasi Personal Extreme Programming (PXP))",
    content='[Bab 1 Subbab 1.1 (Hlm. 25), Bab 2 Subbab 2.1.2 (Hlm. 33), & Bab 3 Subbab 3.2 (Hlm. 72) - Abstrak Inisiasi Personal Extreme Programming (PXP)]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Konsep XP untuk pengembang tunggal pertama kali diinisiasi oleh Agarwal dan Umphress (2008) melalui praktik Extreme Programming for a Single Person Team yang memadukan prinsip XP dan Personal Software Process (PSP) menjadi Personal Extreme Programming (PXP)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 1):\nKalimat Abstrak Lengkap (Hlm. 1 Kolom Kiri): "The purpose of this paper is to examine the features of Extreme Programming (XP) and determine how it can be applied to a single person team (i.e. a programmer who works mainly on his/her own as opposed to a programmer who works as a part of a well-integrated team). A software development process for a single person team, Personal Extreme Programming (PXP) is created."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot1.update()

# ==============================================================================
# Citation #2 (Page 1): Adaptasi Praktik XP Tanpa Pair Programming
# ==============================================================================
lines_c2 = [
    (645, 1264, 487, 17),
    (645, 1285, 487, 18),
    (645, 1306, 487, 17),
    (645, 1327, 489, 18),
    (645, 1347, 486, 18),
    (645, 1369, 487, 17),
    (644, 1389, 488, 18),
    (645, 1410, 486, 18),
    (645, 1432, 486, 18),
    (645, 1452, 487, 18),
    (645, 1474, 250, 17),
]
annot2 = pages[0].add_highlight_annot(quads=make_quads(lines_c2))
annot2.set_colors(stroke=[1.0, 0.92, 0.0])
annot2.set_info(
    title="Kutipan Skripsi ARTHA (Bab 1 Subbab 1.1 (Hlm. 24-25) & Bab 2 Subbab 2.1.2 (Hlm. 33) - Adaptasi Praktik XP Tanpa Pair Programming untuk Pengembang Tunggal)",
    content='[Bab 1 Subbab 1.1 (Hlm. 24-25) & Bab 2 Subbab 2.1.2 (Hlm. 33) - Adaptasi Praktik XP Tanpa Pair Programming untuk Pengembang Tunggal]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Karena praktik pair programming pada XP konvensional tidak dapat dilakukan oleh satu pemrogram yang bekerja sendiri, praktik XP dimodifikasi agar sesuai dengan situasi pengembang tunggal melalui metode Personal Extreme Programming (PXP) (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 1):\nKalimat Bagian 2 PXP (Hlm. 1 Kolom Kanan): "There are cases where pair programming is unattainable: where a single programmer is working on a project... The practices of XP are modified so that they can fit in a lone programmer situation and a software development process is created. We call our method PXP (Personal Extreme Programming)."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot2.update()

# ==============================================================================
# Citation #3 (Page 2): Penulisan User Stories pada Kartu beserta Prioritas
# ==============================================================================
lines_c3 = [
    (110, 225, 486, 17),
    (110, 245, 486, 18),
    (110, 267, 486, 17),
    (110, 288, 487, 18),
    (110, 308, 487, 18),
    (645, 225, 486, 17),
    (645, 245, 486, 18),
    (645, 267, 486, 17),
    (645, 288, 486, 18),
]
annot3 = pages[1].add_highlight_annot(quads=make_quads(lines_c3))
annot3.set_colors(stroke=[1.0, 0.92, 0.0])
annot3.set_info(
    title="Kutipan Skripsi ARTHA (Bab 2 Subbab 2.1.2 PxP Tahap 1 Requirements & Tahap 2 Planning (Hlm. 33-34) - Penulisan User Stories pada Kartu beserta Prioritas dan Estimasi Biaya/Waktu)",
    content='[Bab 2 Subbab 2.1.2 PxP Tahap 1 Requirements & Tahap 2 Planning (Hlm. 33-34) - Penulisan User Stories pada Kartu beserta Prioritas dan Estimasi Biaya/Waktu]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Dalam skrip proses PXP, kebutuhan pengguna ditulis dalam bentuk User Stories yang digunakan pada tahap perencanaan (Planning), dilengkapi catatan tingkat prioritas dan estimasi waktu pengerjaan, serta dikelompokkan ke dalam jadwal iterasi (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 2):\nKalimat Penjelasan Tabel 1 (Hlm. 2 Kolom Kiri): "Table 1 shows the process script for the Personal Extreme Programming (PXP). User stories are written on cards. The card does not contain all the information that makes up the requirement. Instead, the card has just enough text to identify the requirement, and to remind everyone what the story is. The card is a token representing the requirement. It\'s used in planning. Notes are written on it, reflecting priority and cost."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot3.update()

# ==============================================================================
# Citation #4 (Page 3): Pengembangan Iteratif melalui 3 Baselines
# ==============================================================================
lines_c4 = [
    (110, 334, 486, 18),
    (110, 355, 487, 18),
    (110, 377, 487, 17),
    (110, 398, 486, 18),
    (110, 418, 487, 18),
    (110, 440, 487, 17),
    (110, 460, 486, 18),
    (110, 481, 486, 18),
]
annot4 = pages[2].add_highlight_annot(quads=make_quads(lines_c4))
annot4.set_colors(stroke=[1.0, 0.92, 0.0])
annot4.set_info(
    title="Kutipan Skripsi ARTHA (Bab 2 Subbab 2.1.2 PxP Tahap 3 Iteration Initialization & Tahap 5 Implementation (Hlm. 34-35) - Pengembangan Iteratif melalui Development, Refactor, dan Production Baseline)",
    content='[Bab 2 Subbab 2.1.2 PxP Tahap 3 Iteration Initialization & Tahap 5 Implementation (Hlm. 34-35) - Pengembangan Iteratif melalui Development, Refactor, dan Production Baseline]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Kode dikembangkan secara bertahap dalam siklus iterasi di mana setiap iterasi diawali dengan perencanaan iterasi dan pembaruan desain, dilanjutkan dengan pengujian unit, refactoring kode, dan pengujian penerimaan sebelum dirilis (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 3):\nKalimat Siklus Iterasi PXP (Hlm. 3 Kolom Kiri): "The code is developed in iterations and is released as versions. Each iteration starts with iteration planning and updating the designs. The developer maintains three baselines, namely development, refactor, and production baselines. After initial code development, the code is maintained by versions in the development baseline. Upon completion of the iteration, the code is integration tested and is moved to refactor baseline to be refactored."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot4.update()

# ==============================================================================
# Citation #5 (Page 3): Praktik Simple Design, Testing, Refactoring
# ==============================================================================
lines_c5 = [
    (668, 901, 444, 17),
    (668, 921, 444, 18),
    (668, 942, 444, 18),
    (668, 963, 346, 18),
    (668, 1006, 444, 18),
    (669, 1027, 443, 18),
    (669, 1048, 443, 17),
    (668, 1069, 444, 18),
    (668, 1090, 443, 18),
    (668, 1133, 444, 18),
    (668, 1154, 444, 17),
]
annot5 = pages[2].add_highlight_annot(quads=make_quads(lines_c5))
annot5.set_colors(stroke=[1.0, 0.92, 0.0])
annot5.set_info(
    title="Kutipan Skripsi ARTHA (Bab 2 Subbab 2.1.2 PxP Tahap 4 Design & Tahap 5 Implementation (Hlm. 34-35) - Praktik Simple Design, Test-First (Unit Test), dan Refactoring pada PXP)",
    content='[Bab 2 Subbab 2.1.2 PxP Tahap 4 Design & Tahap 5 Implementation (Hlm. 34-35) - Praktik Simple Design, Test-First (Unit Test), dan Refactoring pada PXP]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Sebagai pengembang tunggal dalam PXP, pemrogram mempertahankan desain yang sederhana (Simple Design), menulis pengujian unit terlebih dahulu sebelum mengimplementasikan modul, serta melakukan refactoring kode secara disiplin (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 3):\nKalimat Tabel 2 Praktik Inti PXP (Hlm. 3 Kolom Kanan): "Simple Design: As a lone developer it is easy to maintain a simple design... Testing: When writing a new module, programmers should write the interface first, then the unit test, and only then go on to implement the module... Refactoring: As a lone programmer one can and should practice refactoring."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot5.update()

# ==============================================================================
# Citation #6 (Page 4): Bagian 4 PXP at Work (TARGET KOREKSI UTAMA PENGGUNA)
# ==============================================================================
lines_c6 = [
    (110, 1166, 474, 18),
    (110, 1187, 474, 18),
    (109, 1208, 475, 18),
    (110, 1229, 474, 16),
    (110, 1250, 474, 18),
    (110, 1271, 382, 18),
]
annot6 = pages[3].add_highlight_annot(quads=make_quads(lines_c6))
annot6.set_colors(stroke=[1.0, 0.92, 0.0])
annot6.set_info(
    title="Kutipan Skripsi ARTHA (Bab 2 Subbab 2.1.2 PxP Tahap 2 Planning & Tahap 3 Iteration Initialization (Hlm. 34) - Pengelompokan Fitur Berprioritas (FeatureSetPriorityList) ke dalam Rencana Iterasi)",
    content='[Bab 2 Subbab 2.1.2 PxP Tahap 2 Planning & Tahap 3 Iteration Initialization (Hlm. 34) - Pengelompokan Fitur Berprioritas (FeatureSetPriorityList) ke dalam Rencana Iterasi]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Rangkaian kebutuhan dan fitur dikelompokkan serta diurutkan berdasarkan prioritas implementasi ke dalam beberapa siklus iterasi dengan mempertimbangkan keterkaitan antarfitur dan kecepatan kerja pengembang tunggal (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 4):\nKalimat Bagian 4 PXP at Work (Hlm. 4 Kolom Kiri): "Iterative development cycle was used as recommended by the PXP process script and the FeatureSet with the highest priority was picked and iteration plan was created for the set. The FeatureSet was then broken down into tasks needed to implement the FeatureSet, and a TaskPriorityList was created (e.g. Figure 4), along with the unit test for each task."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot6.update()

# ==============================================================================
# Citation #7 (Page 5): Bagian 5 Conclusions (Keseimbangan PXP)
# ==============================================================================
lines_c7 = [
    (657, 883, 475, 18),
    (658, 904, 119, 14),
    (657, 946, 474, 17),
    (657, 967, 475, 18),
    (657, 988, 475, 18),
    (657, 1009, 187, 18),
]
annot7 = pages[4].add_highlight_annot(quads=make_quads(lines_c7))
annot7.set_colors(stroke=[1.0, 0.92, 0.0])
annot7.set_info(
    title="Kutipan Skripsi ARTHA (Bab 1 Subbab 1.1 (Hlm. 25), Bab 2 Subbab 2.1.2 (Hlm. 33), & Bab 3 Subbab 3.2 (Hlm. 72) - Kesimpulan Keseimbangan PXP untuk Pengembang Tunggal)",
    content='[Bab 1 Subbab 1.1 (Hlm. 25), Bab 2 Subbab 2.1.2 (Hlm. 33), & Bab 3 Subbab 3.2 (Hlm. 72) - Kesimpulan Keseimbangan PXP untuk Pengembang Tunggal]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Personal Extreme Programming (PXP) menyelaraskan nilai kesederhanaan, komunikasi, umpan balik, dan ketanggapan XP agar sesuai bagi pengembang tunggal dengan memberikan ketegasan proses yang tepat tanpa membebani pengembang dengan birokrasi dokumentasi yang berlebihan (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 5):\nKalimat Bagian 5 Conclusions (Hlm. 5 Kolom Kanan): "Personal Extreme Programming (PXP) is a software development process for a lone programmer. It preserves the practices of XP, adapting them where necessary to fit a lone programmer situation... The PXP approach tries to balance between the \'too heavy\' and the \'too light\' methodologies. PXP will inject the right amount of rigor for the situation without overburdening the team with unnecessary bureaucracy."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot7.update()

# Save PDF cleanly
temp_save = pdf_path.replace(".pdf", "_temp.pdf")
doc.save(temp_save, incremental=False, deflate=True)
doc.close()

if os.path.exists(pdf_path):
    os.remove(pdf_path)
shutil.move(temp_save, pdf_path)

print("SUCCESS: 32_Agarwal PDF updated with line-by-line highlights for all 7 citations!")
