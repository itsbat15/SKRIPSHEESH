import fitz
from pathlib import Path

pdf_path = Path(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\02_STUDI_KASUS_BIMBEL_DAN_KURSUS\Peran TI Manajemen Pendidikan - JRPP - Pradana - 2024.pdf")
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

keywords = [
    "seperangkat",
    "prosedur",
    "mengumpulkan",
    "menyimpan",
    "mengolah",
    "mendistribusikan",
    "definisi",
    "merupakan seperangkat",
    "sistem informasi adalah",
    "sistem informasi merupakan"
]

for i, page in enumerate(doc):
    text = page.get_text()
    print(f"\n--- Page {i+1} (Print {6855 + i}) ---")
    for kw in keywords:
        if kw.lower() in text.lower():
            print(f"  MATCH: '{kw}'")
            # find surrounding sentence
            lines = text.split("\n")
            for line in lines:
                if kw.lower() in line.lower():
                    print(f"    Line: {line.strip()}")

# Also print all occurrences of "sistem informasi" in Pradana
print("\n" + "="*50)
print("ALL OCCURRENCES OF 'sistem informasi' IN PRADANA:")
for i, page in enumerate(doc):
    text = page.get_text()
    lines = text.split("\n")
    for idx, l in enumerate(lines):
        if "sistem informasi" in l.lower():
            snippet = " ".join([lines[max(0, idx-1)].strip(), l.strip(), lines[min(len(lines)-1, idx+1)].strip()])
            print(f"[Page {i+1}] {snippet}")

doc.close()
