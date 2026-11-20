import pypdf

p = 'JURNAL/36_REFERENSI_PDF/10713-Article Text-47433-2-10-20250814.pdf'
reader = pypdf.PdfReader(p)
print("Total pages:", len(reader.pages))
text = reader.pages[0].extract_text() or ''
cleaned = text.encode('ascii', errors='replace').decode('ascii')
print(cleaned[:1200])

