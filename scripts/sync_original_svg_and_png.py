"""
sync_original_svg_and_png.py
============================
Creates SVG and PNG from the exact original layout of Gambar_3_9_ERD_Chen_ARTHA.svg,
removing ONLY attributes while keeping all lines, positions, and routings identical to the user's image.
"""

import os
import subprocess
import shutil

SRC_SVG = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.svg"
BACKUP_SVG = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA_Lengkap_Atribut.svg"

# Backup original full SVG if not backed up
if not os.path.exists(BACKUP_SVG):
    shutil.copyfile(SRC_SVG, BACKUP_SVG)
    print("Backed up full SVG to:", BACKUP_SVG)

with open(BACKUP_SVG, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'class="line-att"' in line or 'class="box-att"' in line or 'class="att-pk"' in line or 'class="att-label"' in line:
        continue
    if '&nbsp;' in line:
        line = line.replace('&nbsp;', '&#160;')
    new_lines.append(line)

out_svg_1 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
out_svg_2 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.svg"
out_svg_3 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
out_svg_4 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Chen_ARTHA.svg"

for p in [out_svg_1, out_svg_2, out_svg_3, out_svg_4]:
    with open(p, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("Wrote SVG:", p)

# Render PNG via Edge headless
WIDTH = 2240
HEIGHT = 1580

html_wrapper = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scripts\render_original_erd.html"
with open(html_wrapper, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #ffffff; overflow: hidden; width: {WIDTH}px; height: {HEIGHT}px; }}
  svg {{ display: block; width: {WIDTH}px; height: {HEIGHT}px; }}
</style>
</head>
<body>
{''.join(new_lines)}
</body>
</html>
""")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
png_artifact = r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_Konseptual_ARTHA_Original_Lines.png"
url = "file:///" + html_wrapper.replace(os.sep, "/")

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    f"--window-size={WIDTH},{HEIGHT}",
    f"--screenshot={png_artifact}",
    url
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge screenshot return code:", res.returncode)

png_final_1 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 Entity Relationship Diagram (ERD) Sistem Informasi ARTHA.png"
png_final_2 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 ERD Sistem Informasi ARTHA.png"
png_final_3 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.png"
png_final_4 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.png"

for p in [png_final_1, png_final_2, png_final_3, png_final_4]:
    shutil.copyfile(png_artifact, p)
    print("Copied PNG:", p)

