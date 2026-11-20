import fitz
from pathlib import Path

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
pdf_path = ROOT / "JURNAL" / "01_FONDASI_DAN_KOMPARASI_METODOLOGI" / "Extreme programming for a single person team.pdf"
doc = fitz.open(pdf_path)
page = doc[3] # page 4 (0-indexed 3)
rect = page.rect
print(f"Page rect: {rect}") # e.g. Rect(0.0, 0.0, 612.0, 792.0)

# In agarwal_page4.png, Table 2 "On-site Customer" row
# Let's add a highlight rect:
# In standard US Letter 612 x 792, Table 2 "On-site Customer" is approximately:
# x from ~40 to 570, y from ~265 to ~355.
highlight_rect = fitz.Rect(45, 265, 567, 355)
annot = page.add_highlight_annot(highlight_rect)
annot.set_colors(stroke=[1, 1, 0]) # Yellow
annot.set_info(content="Klaim Bab 1 [A22]: Table 2 - On-site Customer: XP has Customer dedicated to the team full time vs PXP has frequent interaction via email/phone")
annot.update()

pix = page.get_pixmap(dpi=150)
pix.save("scripts/agarwal_page4_highlighted.png")
doc.close()
print("Saved scripts/agarwal_page4_highlighted.png successfully")
