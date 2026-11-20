import fitz
from pathlib import Path

OUT_DIR = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\PDF_TERSTABILO_BAB1")
pdf_files = sorted(OUT_DIR.glob("*.pdf"))

print(f"Total PDFs found: {len(pdf_files)}")
total_annots_all = 0

for pf in pdf_files:
    doc = fitz.open(pf)
    annots_in_doc = 0
    pages_with_annots = []
    for i, page in enumerate(doc):
        annots = list(page.annots())
        if annots:
            annots_in_doc += len(annots)
            pages_with_annots.append(i + 1)
    print(f"{pf.name:<55} | Pages: {len(doc):<4} | Annots: {annots_in_doc:<3} | Marked Pages: {pages_with_annots}")
    total_annots_all += annots_in_doc
    doc.close()

print(f"\nTotal highlight annotations across all files: {total_annots_all}")
