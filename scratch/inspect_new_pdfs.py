import pypdf

files_to_check = [
    'JURNAL/36_REFERENSI_PDF/BPMN.pdf',
    'JURNAL/36_REFERENSI_PDF/10713-Article Text-47433-2-10-20250814.pdf',
    'JURNAL/36_REFERENSI_PDF/TailwindCSS_JTEKSIS_Santoso_2025.pdf'
]

for p in files_to_check:
    print(f"=== CHECKING: {p} ===")
    try:
        reader = pypdf.PdfReader(p)
        print("Total pages:", len(reader.pages))
        first_page = reader.pages[0].extract_text() or ''
        print("--- FIRST 800 CHARACTERS ---")
        print(first_page[:800])
        print("\n" + "="*50 + "\n")
    except Exception as e:
        print("Error reading:", e)

