import pypdf

p = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\PENGAJUAN SEMPRO\Proposal Tugas Akhir_10231018.pdf"
reader = pypdf.PdfReader(p)

with open(r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\pdf_structure_audit.txt", "w", encoding="utf-8") as out:
    for i in range(len(reader.pages)):
        txt = reader.pages[i].extract_text()
        lines = [l.strip() for l in txt.split("\n") if l.strip()]
        f = lines[0] if lines else ""
        l = lines[-1] if lines else ""
        header = ""
        for line in lines[:4]:
            if any(k in line.upper() for k in ["BAB ", "DAFTAR ", "ABSTRAK", "ABSTRACT", "LEMBAR", "KATA PENGANTAR", "PROPOSAL", "TABEL 3.6", "LAMPIRAN"]):
                header = line
                break
        if not header and lines:
            header = lines[0][:35]
        out.write(f"PDF_Sheet_{i+1:03d} | Printed_Page: {l:6s} | Header: {header}\n")

print("Saved to pdf_structure_audit.txt")
