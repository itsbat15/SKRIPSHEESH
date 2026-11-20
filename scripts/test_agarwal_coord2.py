import fitz
from PIL import Image

pdf_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\01_FONDASI_DAN_KOMPARASI_METODOLOGI\Extreme programming for a single person team.pdf"
doc = fitz.open(pdf_path)
page = doc[3]

# Table 2 "On-site Customer" row
# Let's highlight exact row of On-site Customer:
highlight_rect = fitz.Rect(52, 222, 545, 330)
annot = page.add_highlight_annot(highlight_rect)
annot.set_colors(stroke=[1, 1, 0])
annot.set_info(content="Klaim Bab 1 [A22]: Table 2 - On-site Customer: XP vs PXP")
annot.update()

pix = page.get_pixmap(dpi=150)
pix.save("scripts/agarwal_test2.png")
doc.close()

im = Image.open("scripts/agarwal_test2.png")
crop_box = (int(45 * 150 / 72), int(200 * 150 / 72), int(555 * 150 / 72), int(360 * 150 / 72))
im.crop(crop_box).save("scripts/agarwal_crop2.png")
print("Saved agarwal_crop2.png")
