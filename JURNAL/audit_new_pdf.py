import pypdf
import os
import datetime

pdf_path = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\PENGAJUAN SEMPRO\Proposal Tugas Akhir_10231018.pdf'
stat = os.stat(pdf_path)
print("File size:", stat.st_size)
print("Last modified:", datetime.datetime.fromtimestamp(stat.st_mtime))

reader = pypdf.PdfReader(pdf_path)
print("Total pages:", len(reader.pages))

with open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\new_pdf_audit.txt', 'w', encoding='utf-8') as f:
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ''
        first_lines = [line.strip() for line in text.split('\n') if line.strip()][:3]
        header = ' | '.join(first_lines)
        last_line = [line.strip() for line in text.split('\n') if line.strip()][-1:] if text.strip() else ['']
        f.write(f"PDF_Sheet_{i+1:03d} | Header: {header[:100]} | Last: {last_line[0][:50]}\n")
        for kw in ['LEMBAR PERSETUJUAN', 'KATA PENGANTAR', 'ABSTRAK', 'ABSTRACT', 'DAFTAR ISI', 'DAFTAR GAMBAR', 'DAFTAR TABEL', 'BAB 1', 'BAB 2', 'BAB 3', 'DAFTAR PUSTAKA', 'LAMPIRAN']:
            if kw in header.upper() or kw in text[:400].upper():
                print(f"Sheet {i+1:03d}: {kw} -> {header[:80]}")
