import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
svg_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
png_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 Entity Relationship Diagram (ERD) Sistem Informasi ARTHA.png"
png_path_alt = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 ERD Sistem Informasi ARTHA.png"
png_path_drawio = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.png"
png_artifact = r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_Konseptual_ARTHA.png"

# Create a clean HTML wrapper to ensure perfect rendering without scrollbars/margins
html_wrapper = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scripts\render_erd.html"
with open(html_wrapper, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<head>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #ffffff; overflow: hidden; }}
  img {{ width: 2240px; height: 1580px; display: block; }}
</style>
</head>
<body>
  <img src="file:///{svg_path.replace(os.sep, '/')}" />
</body>
</html>
""")

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2240,1580",
    f"--screenshot={png_artifact}",
    f"file:///{html_wrapper.replace(os.sep, '/')}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)

if os.path.exists(png_artifact):
    import shutil
    shutil.copyfile(png_artifact, png_path)
    shutil.copyfile(png_artifact, png_path_alt)
    shutil.copyfile(png_artifact, png_path_drawio)
    print("Successfully rendered and copied PNG to:")
    print(" -", png_artifact)
    print(" -", png_path)
    print(" -", png_path_alt)
    print(" -", png_path_drawio)
else:
    print("Failed to render screenshot")

