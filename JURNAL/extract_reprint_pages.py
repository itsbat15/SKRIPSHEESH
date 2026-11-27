import pypdf

src_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\PENGAJUAN SEMPRO\Proposal Tugas Akhir_10231018.pdf"
dst_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DOCS SKRIPSI\PENGAJUAN SEMPRO\Halaman_Cetak_Ulang_48-49_58-59_64-65_104-105.pdf"

reader = pypdf.PdfReader(src_path)
writer = pypdf.PdfWriter()

# The target sheets corresponding to printed pages:
# Printed 48 -> PDF Sheet 62 (index 61)
# Printed 49 -> PDF Sheet 63 (index 62)
# Printed 58 -> PDF Sheet 72 (index 71)
# Printed 59 -> PDF Sheet 73 (index 72)
# Printed 64 -> PDF Sheet 78 (index 77)
# Printed 65 -> PDF Sheet 79 (index 78)
# Printed 104 -> PDF Sheet 118 (index 117)
# Printed 105 -> PDF Sheet 119 (index 118)

pages_to_extract = [
    (61, 48),
    (62, 49),
    (71, 58),
    (72, 59),
    (77, 64),
    (78, 65),
    (117, 104),
    (118, 105),
]

for idx, printed_num in pages_to_extract:
    page = reader.pages[idx]
    writer.add_page(page)
    print(f"Added PDF Sheet {idx+1} (Printed Page {printed_num})")

with open(dst_path, "wb") as f_out:
    writer.write(f_out)

print("Successfully written to:", dst_path)

# Verify
verify_reader = pypdf.PdfReader(dst_path)
print("Verified page count:", len(verify_reader.pages))
for i, page in enumerate(verify_reader.pages):
    text = page.extract_text() or ''
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_line = lines[0] if lines else ''
    last_line = lines[-1] if lines else ''
    print(f"Page {i+1} in new PDF | Printed Bottom: {last_line[-15:]} | Top: {first_line[:50]}")
