import fitz, os, re

pdf_dir = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF'

pdf_files = [
    (1, '03_Fajriansyah_dkk_2026_JRIS_SINTA3.pdf', ['Google Forms', 'Waterfall', 'kurang dari 2 detik', 'modul presensi digital', 'Depok dan Tangerang Selatan']),
    (2, '15_Tiana_Gunanto_2026_JUKTISI_SINTA4.pdf', ['Texas Kotabumi', 'Waterfall', 'Black Box', 'kehadiran', 'riwayat pembayaran']),
    (3, '05_Zakaria_dkk_2023_JuTISI_SINTA3.pdf', ['Feng Huang', 'Waterfall', 'MandarinPro', 'Alpha Testing', 'berbasis desktop']),
    (4, '10_Ahadi_dkk_2025_Djtechno_SINTA4.pdf', ['Royal Heritage', 'waterfall-iterative', 'Black Box', 'data cabang', 'tahap deployment']),
    (5, '04_Hendri_dkk_2025_JUSTIAN_SINTA3.pdf', ['Semesta Khatulistiwa', 'Waterfall', 'Figma', 'bukti pembayaran', 'laporan pembayaran']),
    (6, '11_Sudirman_Tristianti_2021_MEANS_SINTA4.pdf', ['Lisa Pratama', 'rekonsiliasi bank', 'Prototyping', 'penerimaan kas', 'hak akses']),
    (7, '12_Khafidhoh_dkk_2026_JTI_SINTA4.pdf', ['Megaluh 7059', 'Algoritma Genetika', 'Waterfall', 'meminimalkan', 'sesuai dengan perancangan']),
    (8, '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf', ['jadwal', 'DevOps', 'Front-End', 'React', 'tiga model jadwal']),
    (9, '13_Musofa_dkk_2025_JTIIK_SINTA2.pdf', ['Lombok Tengah', 'Personal Extreme Programming', '312 ms', '98,7%', 'buku tamu']),
    (10, '14_Apriyanti_dkk_2024_JATI_SINTA4.pdf', ['Mutiara Putri Gemilang', 'Personal Extreme Programming', 'kaveling', '91%', 'validasi berkas'])
]

for row, fname, keywords in pdf_files:
    p = os.path.join(pdf_dir, fname)
    doc = fitz.open(p)
    print(f'=== Baris {row}: {fname} ===')
    for kw in keywords:
        found = False
        for pno in range(len(doc)):
            text = doc[pno].get_text()
            flat = ' '.join(text.split())
            if kw.lower() in flat.lower():
                idx = flat.lower().find(kw.lower())
                snippet = flat[max(0, idx-30):min(len(flat), idx+70)]
                print(f'  [P{pno+1}] kw "{kw}": ...{snippet}...')
                found = True
                break
        if not found:
            print(f'  NOT FOUND: kw "{kw}"')

