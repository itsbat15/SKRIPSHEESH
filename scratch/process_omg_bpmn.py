import shutil
import os
import pypdf

src = 'ARSIP JURNAL LAMA/06_SUMBER_PRIMER_BAB2_1_2026-10-27/OMG_BPMN_2.0.2_2013.pdf'
dst = 'JURNAL/36_REFERENSI_PDF/OMG_BPMN_2.0.2_2013.pdf'
txt_dst = 'JURNAL/36_REFERENSI_TXT/OMG_BPMN_2.0.2_2013.txt'

if not os.path.exists(dst):
    shutil.copy2(src, dst)
    print("Copied OMG BPMN PDF to JURNAL/36_REFERENSI_PDF/")
else:
    print("OMG BPMN PDF already in JURNAL/36_REFERENSI_PDF/")

if not os.path.exists(txt_dst):
    reader = pypdf.PdfReader(dst)
    print(f"OMG BPMN total pages: {len(reader.pages)}")
    # extract first 60 pages (covers core concepts, elements, diagram types)
    extracted = []
    for i in range(min(60, len(reader.pages))):
        extracted.append(f"=== HALAMAN {i+1} ===\n" + (reader.pages[i].extract_text() or ''))
    with open(txt_dst, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(extracted))
    print("Extracted core pages of OMG BPMN to", txt_dst)
else:
    print("OMG BPMN TXT already exists.")

