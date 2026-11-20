import os
import pypdf
import re

# 1. Delete OMG
for p in ['JURNAL/36_REFERENSI_PDF/OMG_BPMN_2.0.2_2013.pdf', 'JURNAL/36_REFERENSI_TXT/OMG_BPMN_2.0.2_2013.txt']:
    if os.path.exists(p):
        os.remove(p)
        print(f"Removed {p}")

# 2. Update BibTeX files
for bib_path in [
    'DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1/REFERENSI DRAF BAB 2.1.bib',
    'DRAFT PROPOSAL MD/DAFTAR_PUSTAKA_ARTHA_36_REFERENSI.bib'
]:
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'@manual\{OMG2013BPMN,[\s\S]*?\n\}\n*', '', content)
    with open(bib_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned OMG from {bib_path}")

# 3. Re-extract Dumas (all 546 pages)
pdf_path = 'JURNAL/36_REFERENSI_PDF/Dumas_dkk_2018_Fundamentals_of_BPM.pdf'
txt_path = 'JURNAL/36_REFERENSI_TXT/Dumas_dkk_2018_Fundamentals_of_BPM.txt'

reader = pypdf.PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f"Extracting all {total_pages} pages from Dumas...")

pages_text = []
for i in range(total_pages):
    txt = reader.pages[i].extract_text() or ''
    pages_text.append(f"=== HALAMAN {i+1} ===\n{txt}")

full_text = "\n\n".join(pages_text)
with open(txt_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Successfully extracted {len(full_text):,} characters to {txt_path}")

