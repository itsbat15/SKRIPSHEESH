import os
import shutil
import pypdf

pdf_dir = 'JURNAL/36_REFERENSI_PDF'
txt_dir = 'JURNAL/36_REFERENSI_TXT'

# 1. Rename BPMN.pdf -> Yusmar_dkk_2023_JTIIK_SINTA2_BPMN_Agrowing.pdf
old_bpmn = os.path.join(pdf_dir, 'BPMN.pdf')
new_bpmn = os.path.join(pdf_dir, 'Yusmar_dkk_2023_JTIIK_SINTA2_BPMN_Agrowing.pdf')

if os.path.exists(old_bpmn):
    os.rename(old_bpmn, new_bpmn)
    print(f"Renamed {old_bpmn} -> {new_bpmn}")
elif os.path.exists(new_bpmn):
    print(f"{new_bpmn} already exists")

# 2. Rename 10713-Article Text-47433-2-10-20250814.pdf -> Tan_2025_JuTISI_SINTA3_Middleware_Laravel.pdf
old_10713 = os.path.join(pdf_dir, '10713-Article Text-47433-2-10-20250814.pdf')
new_10713 = os.path.join(pdf_dir, 'Tan_2025_JuTISI_SINTA3_Middleware_Laravel.pdf')

if os.path.exists(old_10713):
    os.rename(old_10713, new_10713)
    print(f"Renamed {old_10713} -> {new_10713}")
elif os.path.exists(new_10713):
    print(f"{new_10713} already exists")

# Function to extract text
def extract_pdf_to_txt(pdf_path, txt_path):
    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    pages_text = []
    for i in range(total_pages):
        t = reader.pages[i].extract_text() or ''
        pages_text.append(f"=== HALAMAN {i+1} ===\n{t}")
    content = "\n\n".join(pages_text)
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Extracted {pdf_path} ({total_pages} pages) -> {txt_path} ({len(content)} chars)")

# Extract Yusmar
yusmar_txt = os.path.join(txt_dir, 'Yusmar_dkk_2023_JTIIK_SINTA2_BPMN_Agrowing.txt')
extract_pdf_to_txt(new_bpmn, yusmar_txt)

# Extract Tan
tan_txt = os.path.join(txt_dir, 'Tan_2025_JuTISI_SINTA3_Middleware_Laravel.txt')
extract_pdf_to_txt(new_10713, tan_txt)

print("\n--- ALL COMPLETED SUCCESSFULLY ---")

