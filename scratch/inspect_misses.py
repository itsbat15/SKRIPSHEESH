import fitz

# 1. PDF 4
doc4 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\10_Ahadi_dkk_2025_Djtechno_SINTA4.pdf')
p1_4 = doc4[0].get_text()
for line in p1_4.splitlines():
    if 'deployment' in line.lower() or 'layak' in line.lower():
        print('Doc4 P1:', line)

# 2. PDF 8
doc8 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf')
print('Doc8 P2 lines:')
for line in doc8[1].get_text().splitlines():
    if 'tujuan' in line.lower() or 'jadwal' in line.lower() or 'mengatasi' in line.lower():
        print('  ', line)
print('Doc8 P3 lines:')
for line in doc8[2].get_text().splitlines():
    if 'devops' in line.lower() or 'tahap' in line.lower():
        print('  ', line)
print('Doc8 P14 lines:')
for line in doc8[13].get_text().splitlines():
    if 'generate' in line.lower() or 'model' in line.lower() or 'jadwal' in line.lower():
        print('  ', line)

# 3. PDF 9
doc9 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\13_Musofa_dkk_2025_JTIIK_SINTA2.pdf')
print('Doc9 P2 lines:')
for line in doc9[1].get_text().splitlines():
    if 'buku tamu' in line.lower() or 'manual' in line.lower() or 'pengunjung' in line.lower():
        print('  ', line)
print('Doc9 P3 lines:')
for line in doc9[2].get_text().splitlines():
    if 'pxp' in line.lower() or 'tahapan' in line.lower() or 'metode' in line.lower():
        print('  ', line)

# 4. PDF 10
doc10 = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\14_Apriyanti_dkk_2024_JATI_SINTA4.pdf')
print('Doc10 P2 lines:')
for line in doc10[1].get_text().splitlines():
    if 'pxp' in line.lower() or 'programming' in line.lower() or 'metode' in line.lower():
        print('  ', line)

