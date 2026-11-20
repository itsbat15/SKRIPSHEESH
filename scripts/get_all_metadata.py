import os
import fitz
import re

folders = [
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\01_FONDASI_DAN_KOMPARASI_METODOLOGI",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\02_STUDI_KASUS_BIMBEL_DAN_KURSUS",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\03_IMPLEMENTASI_PXP_DAN_XP_TERDAHULU",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\04_FITUR_DAN_TEKNOLOGI_PENDUKUNG",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\JURNAL PENDUKUNG",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\BUKU"
]

doi_pattern = re.compile(r'10\.\d{4,9}/[^\s"<>]+')
url_pattern = re.compile(r'https?://[^\s"<>]+')

with open(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scripts\all_extracted_meta.txt", "w", encoding="utf-8") as out:
    for fld in folders:
        fld_name = os.path.basename(fld)
        out.write(f"\n==================== {fld_name} ====================\n")
        files = sorted([f for f in os.listdir(fld) if f.lower().endswith(".pdf")])
        for idx, fname in enumerate(files, 1):
            fpath = os.path.join(fld, fname)
            try:
                doc = fitz.open(fpath)
                full_text = ""
                for pno in range(min(len(doc), 3)):
                    full_text += doc[pno].get_text() + "\n"
                    
                dois = [d.rstrip(".,;()[]") for d in doi_pattern.findall(full_text)]
                dois = list(dict.fromkeys(dois))
                
                urls = [u.rstrip(".,;()[]") for u in url_pattern.findall(full_text)]
                urls = list(dict.fromkeys(urls))
                
                lines = [line.strip() for line in full_text.split("\n") if line.strip()]
                
                out.write(f"\n[{idx}] FILE: {fname}\n")
                out.write(f"  DOIs: {dois[:3]}\n")
                out.write(f"  URLs: {urls[:3]}\n")
                out.write("  HEADER SNIPPET:\n")
                for line in lines[:12]:
                    out.write(f"    {line}\n")
            except Exception as e:
                out.write(f"\n[{idx}] FILE: {fname} ERROR: {e}\n")
print("Extraction complete.")

