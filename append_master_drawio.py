import os
import re

dirs = [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3'),
    os.path.abspath('ASET BAB 3'),
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/ASET BAB 3')
]

master_path = os.path.join(dirs[0], 'ARTHA_Semua_Diagram_UML_Bab3.drawio')
with open(master_path, 'r', encoding='utf-8') as f:
    master_content = f.read()

erd_path = os.path.join(dirs[0], 'Gambar_3_9_ERD_MySQL_ARTHA.drawio')
with open(erd_path, 'r', encoding='utf-8') as f:
    erd_content = f.read()

m = re.search(r'<diagram\s+[^>]*>(.*?)</diagram>', erd_content, re.DOTALL)
if m:
    inner = m.group(1).strip()
    erd_page = f'  <diagram id="diag_3_9" name="Gambar 3.9 ERD MySQL ARTHA">\n    {inner}\n  </diagram>'
    if 'diag_3_9' not in master_content:
        master_content = master_content.replace('</mxfile>', f'{erd_page}\n</mxfile>')
        for d in dirs:
            p = os.path.join(d, 'ARTHA_Semua_Diagram_UML_Bab3.drawio')
            with open(p, 'w', encoding='utf-8') as f_out:
                f_out.write(master_content)
            print(f'Updated master drawio at: {p}')
    else:
        print('diag_3_9 already exists in master')

