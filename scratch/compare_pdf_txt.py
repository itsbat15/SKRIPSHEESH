import os

pdf_dir = 'JURNAL/36_REFERENSI_PDF'
txt_dir = 'JURNAL/36_REFERENSI_TXT'

pdfs = sorted(os.listdir(pdf_dir))
txts = sorted(os.listdir(txt_dir))

print(f"Total PDFs: {len(pdfs)}")
print(f"Total TXTs: {len(txts)}")

print("\n--- PDFs in directory ---")
for p in pdfs:
    base = os.path.splitext(p)[0]
    has_txt = (base + '.txt') in txts
    print(f"{'[TXT OK]' if has_txt else '[NO TXT]'} {p}")

