import re

bib_path = 'DRAFT PROPOSAL MD/DAFTAR_PUSTAKA_ARTHA_36_REFERENSI.bib'

with open(bib_path, 'r', encoding='utf-8') as f:
    content = f.read()

dumas_entry = """@book{Dumas2018,
  author = {Dumas, Marlon and La Rosa, Marcello and Mendling, Jan and Reijers, Hajo A.},
  title = {Fundamentals of Business Process Management},
  edition = {2},
  year = {2018},
  publisher = {Springer},
  address = {Berlin, Heidelberg},
  doi = {10.1007/978-3-662-56509-4},
  isbn = {978-3-662-56508-7}
}
"""

yusmar_entry = """@article{Yusmar2023,
  author = {Yusmar, Addini and Nurhadryani, Yani and Hermadi, Irman},
  title = {Analisis Perbaikan dan Pemodelan Proses Bisnis Menggunakan Business Process Improvement Pada Sistem Manajemen Budidaya Buah Agrowing},
  journal = {Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK)},
  volume = {10},
  number = {5},
  pages = {1129--1138},
  year = {2023},
  doi = {10.25126/jtiik.2023107237}
}
"""

# Remove OMG if present
content = re.sub(r'@manual\{OMG2013BPMN,[\s\S]*?\n\}\n*', '', content)

if 'Dumas2018' not in content:
    content += "\n" + dumas_entry
if 'Yusmar2023' not in content:
    content += "\n" + yusmar_entry

with open(bib_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated DAFTAR_PUSTAKA_ARTHA_36_REFERENSI.bib successfully!")

