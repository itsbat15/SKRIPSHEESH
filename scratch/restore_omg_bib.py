import re

for bib_path in [
    'DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1/REFERENSI DRAF BAB 2.1.bib',
    'DRAFT PROPOSAL MD/DAFTAR_PUSTAKA_ARTHA_36_REFERENSI.bib'
]:
    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    omg_entry = """@manual{OMG2013BPMN,
  author = {{Object Management Group}},
  title = {Business Process Model and Notation, Version 2.0.2},
  year = {2013},
  url = {https://www.omg.org/spec/BPMN/2.0.2},
  urldate = {2026-10-27}
}
"""
    if 'OMG2013BPMN' not in content:
        content += "\n" + omg_entry

    with open(bib_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {bib_path}")

