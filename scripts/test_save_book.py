import time
from pathlib import Path
import fitz

ROOT = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA")
out_dir = ROOT / "JURNAL" / "PDF_TERSTABILO_BAB1"
out_dir.mkdir(parents=True, exist_ok=True)

# Test Sommerville
sommerville_path = ROOT / "JURNAL" / "BUKU" / "Software-Engineering-9th-Edition-by-Ian-Sommerville.pdf"
t0 = time.time()
doc = fitz.open(sommerville_path)
page62 = doc[61]
matches = page62.search_for("Evaluation report")
for m in matches:
    annot = page62.add_highlight_annot(m)
    annot.update()
out_file = out_dir / "TEST_Sommerville.pdf"
doc.save(out_file, garbage=1, deflate=True)
doc.close()
t1 = time.time()
print(f"Sommerville highlighted and saved in {t1 - t0:.2f}s, size: {out_file.stat().st_size / 1024 / 1024:.2f} MB")
if out_file.exists():
    out_file.unlink()
