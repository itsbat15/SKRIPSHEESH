import shutil
import os
import pypdf

src = 'C:/Users/ARIEL/Downloads/Dumas et al (2018).pdf'
dst_pdf = 'JURNAL/36_REFERENSI_PDF/Dumas_dkk_2018_Fundamentals_of_BPM.pdf'
dst_txt = 'JURNAL/36_REFERENSI_TXT/Dumas_dkk_2018_Fundamentals_of_BPM.txt'

shutil.copy2(src, dst_pdf)
print(f"Copied {src} to {dst_pdf} ({os.path.getsize(dst_pdf)} bytes)")

# Extract text
reader = pypdf.PdfReader(dst_pdf)
print(f"Total pages: {len(reader.pages)}")

all_text = []
for idx, page in enumerate(reader.pages):
    txt = page.extract_text() or ''
    all_text.append(f"=== HALAMAN {idx+1} ===\n" + txt)

full_extracted = "\n\n".join(all_text)
with open(dst_txt, 'w', encoding='utf-8') as f:
    f.write(full_extracted)

print(f"Saved extracted text to {dst_txt} ({len(full_extracted)} chars)")

