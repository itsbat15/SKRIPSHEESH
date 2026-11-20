import os

svg_src = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.svg"
svg_dst = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
svg_drawio_dir = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.svg"

with open(svg_src, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'class="line-att"' in line or 'class="box-att"' in line or 'class="att-pk"' in line or 'class="att-label"' in line:
        continue
    if 'class="legend-box"' in line:
        line = '    <text x="470" y="26" class="legend-box"><b>Standar Notasi Peter Chen (1976):</b> &nbsp; [ Persegi Panjang ] = Entitas &nbsp;|&nbsp; &lt; Belah Ketupat &gt; = Relasi &nbsp;|&nbsp; 1 / N = Rasio Kardinalitas</text>\n'
    if '<text x="50" y="62"' in line:
        line = '  <text x="50" y="62" class="sub-title">Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA (Entitas, Relasi, dan Kardinalitas)</text>\n'
    new_lines.append(line)

with open(svg_dst, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

with open(svg_drawio_dir, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Generated {svg_dst} and {svg_drawio_dir} (lines: {len(new_lines)})")

