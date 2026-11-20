import subprocess
import os
import shutil

WIDTH = 1820
HEIGHT = 980

svg_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
html_wrapper = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scripts\render_inline_erd.html"
png_artifact = r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_Konseptual_ARTHA_Neat.png"

with open(svg_path, "r", encoding="utf-8") as f:
    svg_code = f.read()

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
{svg_code}
</body>
</html>
""")

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    f"--window-size={WIDTH},{HEIGHT}",
    f"--screenshot={png_artifact}",
    html_wrapper
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

png_final_1 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 Entity Relationship Diagram (ERD) Sistem Informasi ARTHA.png"
png_final_2 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 ERD Sistem Informasi ARTHA.png"
png_final_3 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.png"

if os.path.exists(png_artifact):
    shutil.copyfile(png_artifact, png_final_1)
    shutil.copyfile(png_artifact, png_final_2)
    shutil.copyfile(png_artifact, png_final_3)
    print("Successfully rendered inline SVG to PNG!")

