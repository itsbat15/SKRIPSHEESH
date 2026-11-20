import fitz

# Test on page 4
doc = fitz.open(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\32_Agarwal_Umphress_2008_Single_Person_Extreme_Programming.pdf")
page4 = doc[3] # 0-indexed, page 4

# Remove existing annotations on page 4
for a in list(page4.annots()):
    page4.delete_annot(a)

# Line 65 to 70 data from 150 DPI:
# Line 65: X=110, Y=1166, W=474, H=18
# Line 66: X=110, Y=1187, W=474, H=18
# Line 67: X=109, Y=1208, W=475, H=18
# Line 68: X=110, Y=1229, W=474, H=16
# Line 69: X=110, Y=1250, W=474, H=18
# Line 70: X=110, Y=1271, W=382, H=18

scale = 72.0 / 150.0
lines_p4 = [
    (110, 1166, 474, 18),
    (110, 1187, 474, 18),
    (109, 1208, 475, 18),
    (110, 1229, 474, 16),
    (110, 1250, 474, 18),
    (110, 1271, 382, 18),
]

quads = []
for x, y, w, h in lines_p4:
    x0 = x * scale
    y0 = (y - 1) * scale # slight adjustment to cover ascenders
    x1 = (x + w) * scale
    y1 = (y + h + 1) * scale
    # fitz.Quad(ul, ur, ll, lr)
    quad = fitz.Quad(fitz.Point(x0, y0), fitz.Point(x1, y0), fitz.Point(x0, y1), fitz.Point(x1, y1))
    quads.append(quad)

annot = page4.add_highlight_annot(quads)
annot.set_colors(stroke=[1.0, 0.92, 0.0]) # Standard stabilo yellow
annot.set_info(
    title="Kutipan Skripsi ARTHA (Bab 2 Subbab 2.1.2 PxP Tahap 2 Planning & Tahap 3 Iteration Initialization (Hlm. 34) - Pengelompokan Fitur Berprioritas (FeatureSetPriorityList) ke dalam Rencana Iterasi)",
    content='[Bab 2 Subbab 2.1.2 PxP Tahap 2 Planning & Tahap 3 Iteration Initialization (Hlm. 34) - Pengelompokan Fitur Berprioritas (FeatureSetPriorityList) ke dalam Rencana Iterasi]\n\nKalimat Kutipan/Elaborasi di Skripsi ARTHA:\n"Rangkaian kebutuhan dan fitur dikelompokkan serta diurutkan berdasarkan prioritas implementasi ke dalam beberapa siklus iterasi dengan mempertimbangkan keterkaitan antarfitur dan kecepatan kerja pengembang tunggal (Agarwal & Umphress, 2008)."\n\nKalimat Bukti di Jurnal/Buku (Hlm. 4):\nKalimat Bagian 4 PXP at Work (Hlm. 4 Kolom Kiri): "Iterative development cycle was used as recommended by the PXP process script and the FeatureSet with the highest priority was picked and iteration plan was created for the set. The FeatureSet was then broken down into tasks needed to implement the FeatureSet, and a TaskPriorityList was created (e.g. Figure 4), along with the unit test for each task."',
    subject="Bukti Sitasi Skripsi ARTHA"
)
annot.update()

# Render page 4 to check
pix = page4.get_pixmap(dpi=150)
pix.save(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scratch\test_page_4_highlighted.png")
print("Saved test_page_4_highlighted.png")

