import fitz, os

pdf_dir = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF'

tests = [
    ('10_Ahadi', '10_Ahadi_dkk_2025_Djtechno_SINTA4.pdf', 1, 'sudah layak untuk dilanjutkan ke tahap deployment'),
    ('01_Yuanita_Masalah', '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf', 2, 'proses penjadwalan akan memakan waktu lama'),
    ('01_Yuanita_Metode', '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf', 3, 'tahapan yang dilakukan hanya sampai dengan tahap test'),
    ('01_Yuanita_Hasil', '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf', 14, 'mengenerate tigas model jadwal mata kuliah'),
    ('13_Musofa_Masalah', '13_Musofa_dkk_2025_JTIIK_SINTA2.pdf', 2, 'pengunjung dalam buku fisik'),
    ('13_Musofa_Metode', '13_Musofa_dkk_2025_JTIIK_SINTA2.pdf', 3, 'Metode PXP yang terdiri dari beberapa tahapan'),
    ('14_Apriyanti_Metode', '14_Apriyanti_dkk_2024_JATI_SINTA4.pdf', 1, 'menggunakan metode Personal Extreme Programming (PXP)')
]

for label, fname, pno_hint, phrase in tests:
    doc = fitz.open(os.path.join(pdf_dir, fname))
    found = False
    for pno in range(len(doc)):
        res = doc[pno].search_for(phrase)
        if res:
            print(f'[OK] {label} found on P{pno+1}: {len(res)} rects')
            found = True
            break
    if not found:
        print(f'[FAIL] {label} NOT FOUND: {phrase}')

