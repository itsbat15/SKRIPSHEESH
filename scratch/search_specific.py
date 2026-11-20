import fitz

# 1. Baris 2
doc2 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\15_Tiana_Gunanto_2026_JUKTISI_SINTA4.pdf')
for pno, page in enumerate(doc2):
    t = page.get_text()
    if 'tabel' in t.lower() or 'pengujian' in t.lower():
        lines = [line.strip() for line in t.splitlines() if 'tabel' in line.lower() or 'pengujian' in line.lower() or 'sesuai' in line.lower()]
        if lines:
            print(f'Doc2 P{pno+1}:', lines[:4])

# 2. Baris 5
doc5 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\04_Hendri_dkk_2025_JUSTIAN_SINTA3.pdf')
for pno, page in enumerate(doc5):
    t = page.get_text()
    if 'laporan' in t.lower():
        lines = [line.strip() for line in t.splitlines() if 'laporan' in line.lower() or 'excel' in line.lower()]
        if lines:
            print(f'Doc5 P{pno+1}:', lines[:4])

# 3. Baris 8
doc8 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf')
for pno, page in enumerate(doc8):
    t = page.get_text()
    if 'generate' in t.lower() or 'model' in t.lower():
        lines = [line.strip() for line in t.splitlines() if 'tiga' in line.lower() or 'generate' in line.lower()]
        if lines:
            print(f'Doc8 P{pno+1}:', lines[:4])

