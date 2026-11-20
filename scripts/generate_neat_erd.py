"""
generate_neat_erd.py
====================
Creates both the SVG and draw.io files for the neat, perfectly aligned ARTHA ERD (Peter Chen Notation).
No attributes, pure entities + relationships + cardinalities.
"""

import xml.etree.ElementTree as ET
import subprocess
import os
import shutil

# Coordinates
COL_A = 240   # users, daily_reconciliations
COL_B = 620   # branches, students
COL_C = 1060  # study_groups, enrollments, tuition_bills
COL_D = 1520  # course_packages, payments, payment_proofs

MID_AB = 430  # rel_memiliki
MID_BC = 840  # rel_mengelola, rel_mengambil
MID_CD = 1290 # rel_ditawarkan, rel_diselesaikan

ROW_1 = 180   # branches, study_groups, course_packages
ROW_R1 = 300  # rel_memiliki, rel_menaungi, rel_ditempati, rel_ditawarkan
ROW_2 = 420   # users, students, enrollments
ROW_R2 = 540  # rel_melakukan, rel_menerbitkan, rel_melayani
ROW_3 = 660   # daily_rec, tuition_bills, payments
ROW_R3 = 780  # rel_melampirkan
ROW_4 = 900   # payment_proofs, rel_memvalidasi

X_PERIM_L = 80   # rel_mengadakan
X_PERIM_R = 1720 # rel_menerima

WIDTH = 1820
HEIGHT = 980

# ----------------- 1. BUILD SVG -----------------
svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">',
    '  <defs>',
    '    <style>',
    "      .title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; font-weight: bold; fill: #000000; }",
    "      .sub-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #555555; }",
    "      .legend-box { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; fill: #000000; text-anchor: middle; }",
    "      .ent-label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #000000; text-anchor: middle; dominant-baseline: central; }",
    "      .rel-label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #000000; text-anchor: middle; dominant-baseline: central; }",
    "      .card-label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; fill: #000000; text-anchor: middle; dominant-baseline: central; }",
    '      .line-solid { stroke: #000000; stroke-width: 1.6; fill: none; }',
    '      .box-ent { fill: #ffffff; stroke: #000000; stroke-width: 1.8; }',
    '      .box-rel { fill: #ffffff; stroke: #000000; stroke-width: 1.6; }',
    '    </style>',
    '  </defs>',
    '',
    f'  <rect width="{WIDTH}" height="{HEIGHT}" fill="#ffffff" />',
    '',
    '  <!-- Header: Title & Legend -->',
    '  <text x="50" y="40" class="title">Entity Relationship Diagram (ERD) - Notasi Peter Chen</text>',
    '  <text x="50" y="60" class="sub-title">Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA (Entitas, Relasi, dan Kardinalitas)</text>',
    '  <g transform="translate(1000, 24)">',
    '    <rect width="770" height="40" rx="4" ry="4" fill="#FAFAFA" stroke="#000000" stroke-width="1.2" />',
    '    <text x="385" y="24" class="legend-box">Standar Notasi Peter Chen (1976): &#160; [ Persegi Panjang ] = Entitas &#160;|&#160; &lt; Belah Ketupat &gt; = Relasi &#160;|&#160; 1 / N = Rasio Kardinalitas</text>',
    '  </g>',
    '',
    '  <!-- ================= 14 RELATIONSHIP LINES & PATHS ================= -->'
]

# Helper for SVG diamond
def svg_diamond(cx, cy, w, h, name):
    hw, hh = w / 2, h / 2
    pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
    return f'  <polygon points="{pts}" class="box-rel" />\n  <text x="{cx}" y="{cy}" class="rel-label">{name}</text>'

# Helper for SVG entity box
def svg_rect(cx, cy, w, h, name):
    x, y = cx - w / 2, cy - h / 2
    return f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" class="box-ent" />\n  <text x="{cx}" y="{cy}" class="ent-label">{name}</text>'

# Helper for Cardinality text with white background badge for legibility
def svg_card(x, y, txt):
    return f'  <rect x="{x-10}" y="{y-10}" width="20" height="20" fill="#ffffff" />\n  <text x="{x}" y="{y}" class="card-label">{txt}</text>'

# 1. Mengelola (branches -> study_groups) HORIZONTAL
svg_lines.append('  <!-- 1. branches -[1]- <Mengelola> -[N]- study_groups -->')
svg_lines.append(f'  <line x1="{620+70}" y1="{ROW_1}" x2="{1060-70}" y2="{ROW_1}" class="line-solid" />')
svg_lines.append(svg_card(715, ROW_1 - 14, "1"))
svg_lines.append(svg_card(965, ROW_1 - 14, "N"))

# 2. Menaungi (branches -> students) VERTICAL
svg_lines.append('  <!-- 2. branches -[1]- <Menaungi> -[N]- students -->')
svg_lines.append(f'  <line x1="{COL_B}" y1="{ROW_1+22.5}" x2="{COL_B}" y2="{ROW_2-22.5}" class="line-solid" />')
svg_lines.append(svg_card(COL_B + 16, ROW_1 + 45, "1"))
svg_lines.append(svg_card(COL_B + 16, ROW_2 - 45, "N"))

# 3. Ditempati (study_groups -> enrollments) VERTICAL
svg_lines.append('  <!-- 3. study_groups -[1]- <Ditempati> -[N]- enrollments -->')
svg_lines.append(f'  <line x1="{COL_C}" y1="{ROW_1+22.5}" x2="{COL_C}" y2="{ROW_2-22.5}" class="line-solid" />')
svg_lines.append(svg_card(COL_C + 16, ROW_1 + 45, "1"))
svg_lines.append(svg_card(COL_C + 16, ROW_2 - 45, "N"))

# 4. Mengambil (students -> enrollments) HORIZONTAL
svg_lines.append('  <!-- 4. students -[1]- <Mengambil> -[N]- enrollments -->')
svg_lines.append(f'  <line x1="{620+70}" y1="{ROW_2}" x2="{1060-70}" y2="{ROW_2}" class="line-solid" />')
svg_lines.append(svg_card(715, ROW_2 - 14, "1"))
svg_lines.append(svg_card(965, ROW_2 - 14, "N"))

# 5. Menerbitkan (enrollments -> tuition_bills) VERTICAL
svg_lines.append('  <!-- 5. enrollments -[1]- <Menerbitkan> -[N]- tuition_bills -->')
svg_lines.append(f'  <line x1="{COL_C}" y1="{ROW_2+22.5}" x2="{COL_C}" y2="{ROW_3-22.5}" class="line-solid" />')
svg_lines.append(svg_card(COL_C + 16, ROW_2 + 45, "1"))
svg_lines.append(svg_card(COL_C + 16, ROW_3 - 45, "N"))

# 6. Diselesaikan (tuition_bills -> payments) HORIZONTAL
svg_lines.append('  <!-- 6. tuition_bills -[1]- <Diselesaikan> -[N]- payments -->')
svg_lines.append(f'  <line x1="{1060+70}" y1="{ROW_3}" x2="{1520-70}" y2="{ROW_3}" class="line-solid" />')
svg_lines.append(svg_card(1155, ROW_3 - 14, "1"))
svg_lines.append(svg_card(1425, ROW_3 - 14, "N"))

# 7. Melampirkan (payments -> payment_proofs) VERTICAL
svg_lines.append('  <!-- 7. payments -[1]- <Melampirkan> -[1]- payment_proofs -->')
svg_lines.append(f'  <line x1="{COL_D}" y1="{ROW_3+22.5}" x2="{COL_D}" y2="{ROW_4-22.5}" class="line-solid" />')
svg_lines.append(svg_card(COL_D + 16, ROW_3 + 45, "1"))
svg_lines.append(svg_card(COL_D + 16, ROW_4 - 45, "1"))

# 8. Melakukan (users -> daily_reconciliations) VERTICAL
svg_lines.append('  <!-- 8. users -[1]- <Melakukan> -[N]- daily_reconciliations -->')
svg_lines.append(f'  <line x1="{COL_A}" y1="{ROW_2+22.5}" x2="{COL_A}" y2="{ROW_3-22.5}" class="line-solid" />')
svg_lines.append(svg_card(COL_A + 16, ROW_2 + 45, "1"))
svg_lines.append(svg_card(COL_A + 16, ROW_3 - 45, "N"))

# 9. Memiliki (branches -> users) DIAGONAL SYMMETRIC
svg_lines.append('  <!-- 9. branches -[1]- <Memiliki> -[N]- users -->')
svg_lines.append(f'  <line x1="{COL_B-70}" y1="{ROW_1+15}" x2="{COL_A+70}" y2="{ROW_2-15}" class="line-solid" />')
svg_lines.append(svg_card(535, 215, "1"))
svg_lines.append(svg_card(325, 385, "N"))

# 10. Ditawarkan (course_packages -> enrollments) DIAGONAL SYMMETRIC
svg_lines.append('  <!-- 10. course_packages -[1]- <Ditawarkan> -[N]- enrollments -->')
svg_lines.append(f'  <line x1="{COL_D-75}" y1="{ROW_1+15}" x2="{COL_C+70}" y2="{ROW_2-15}" class="line-solid" />')
svg_lines.append(svg_card(1425, 215, "1"))
svg_lines.append(svg_card(1150, 385, "N"))

# 11. Mengadakan (branches -> daily_reconciliations) PERIMETER LEFT
svg_lines.append('  <!-- 11. branches -[1]- <Mengadakan> -[N]- daily_reconciliations -->')
svg_lines.append(f'  <path d="M {COL_B} {ROW_1-22.5} L {COL_B} {95} L {X_PERIM_L} {95} L {X_PERIM_L} {ROW_3} L {COL_A-85} {ROW_3}" class="line-solid" />')
svg_lines.append(svg_card(580, 85, "1"))
svg_lines.append(svg_card(COL_A - 105, ROW_3 - 14, "N"))

# 12. Menerima (branches -> payments) PERIMETER RIGHT
svg_lines.append('  <!-- 12. branches -[1]- <Menerima> -[N]- payments -->')
svg_lines.append(f'  <path d="M {COL_B} {ROW_1-22.5} L {COL_B} {95} L {X_PERIM_R} {95} L {X_PERIM_R} {ROW_3} L {COL_D+70} {ROW_3}" class="line-solid" />')
svg_lines.append(svg_card(660, 85, "1"))
svg_lines.append(svg_card(COL_D + 95, ROW_3 - 14, "N"))

# 13. Melayani (users -> payments) ORTHOGONAL
svg_lines.append('  <!-- 13. users -[1]- <Melayani> -[N]- payments -->')
svg_lines.append(f'  <path d="M {COL_A+70} {ROW_2+15} L 360 {ROW_2+15} L 360 {ROW_R2} L {1440} {ROW_R2} L {1440} {ROW_3-22.5}" class="line-solid" />')
svg_lines.append(svg_card(380, ROW_2 + 25, "1"))
svg_lines.append(svg_card(1455, ROW_3 - 35, "N"))

# 14. Memvalidasi (users -> payment_proofs) BOTTOM ORTHOGONAL
svg_lines.append('  <!-- 14. users -[1]- <Memvalidasi> -[N]- payment_proofs -->')
svg_lines.append(f'  <path d="M {COL_A} {ROW_3+22.5} L {COL_A} {ROW_4} L {COL_D-75} {ROW_4}" class="line-solid" />')
svg_lines.append(svg_card(COL_A + 16, ROW_3 + 45, "1"))
svg_lines.append(svg_card(COL_D - 95, ROW_4 - 14, "N"))

svg_lines.append('\n  <!-- ================= 14 RELATIONSHIP DIAMONDS ================= -->')
# Render diamonds
svg_lines.append(svg_diamond(MID_BC,    ROW_1,  110, 50, 'Mengelola'))
svg_lines.append(svg_diamond(MID_AB,    ROW_R1, 110, 50, 'Memiliki'))
svg_lines.append(svg_diamond(COL_B,     ROW_R1, 110, 50, 'Menaungi'))
svg_lines.append(svg_diamond(COL_C,     ROW_R1, 110, 50, 'Ditempati'))
svg_lines.append(svg_diamond(MID_CD,    ROW_R1, 110, 50, 'Ditawarkan'))
svg_lines.append(svg_diamond(MID_BC,    ROW_2,  110, 50, 'Mengambil'))
svg_lines.append(svg_diamond(COL_A,     ROW_R2, 110, 50, 'Melakukan'))
svg_lines.append(svg_diamond(COL_C,     ROW_R2, 115, 50, 'Menerbitkan'))
svg_lines.append(svg_diamond(1360,      ROW_R2, 110, 50, 'Melayani'))
svg_lines.append(svg_diamond(MID_CD,    ROW_3,  115, 50, 'Diselesaikan'))
svg_lines.append(svg_diamond(COL_D,     ROW_R3, 115, 50, 'Melampirkan'))
svg_lines.append(svg_diamond(1220,      ROW_4,  110, 50, 'Memvalidasi'))
svg_lines.append(svg_diamond(X_PERIM_L, 420,    110, 50, 'Mengadakan'))
svg_lines.append(svg_diamond(X_PERIM_R, 420,    110, 50, 'Menerima'))

svg_lines.append('\n  <!-- ================= 10 ENTITY RECTANGLES ================= -->')
# Render rectangles
svg_lines.append(svg_rect(COL_B, ROW_1, 140, 45, 'branches'))
svg_lines.append(svg_rect(COL_C, ROW_1, 140, 45, 'study_groups'))
svg_lines.append(svg_rect(COL_D, ROW_1, 150, 45, 'course_packages'))
svg_lines.append(svg_rect(COL_A, ROW_2, 140, 45, 'users'))
svg_lines.append(svg_rect(COL_B, ROW_2, 140, 45, 'students'))
svg_lines.append(svg_rect(COL_C, ROW_2, 140, 45, 'enrollments'))
svg_lines.append(svg_rect(COL_A, ROW_3, 170, 45, 'daily_reconciliations'))
svg_lines.append(svg_rect(COL_C, ROW_3, 140, 45, 'tuition_bills'))
svg_lines.append(svg_rect(COL_D, ROW_3, 140, 45, 'payments'))
svg_lines.append(svg_rect(COL_D, ROW_4, 150, 45, 'payment_proofs'))

svg_lines.append('</svg>\n')

svg_content = '\n'.join(svg_lines)

svg_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.svg"
svg_path_drawio = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.svg"

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg_content)
with open(svg_path_drawio, 'w', encoding='utf-8') as f:
    f.write(svg_content)

print(f"Generated clean SVG ({WIDTH}x{HEIGHT}) at {svg_path}")

# ----------------- 2. RENDER PNG VIA HEADLESS EDGE -----------------
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
png_artifact = r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Gambar_3_9_ERD_Konseptual_ARTHA_Neat.png"
html_wrapper = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\scripts\render_erd_neat.html"

with open(html_wrapper, "w", encoding="utf-8") as f:
    f.write(f"""<!DOCTYPE html>
<html>
<head>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #ffffff; overflow: hidden; }}
  img {{ width: {WIDTH}px; height: {HEIGHT}px; display: block; }}
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
    f"--window-size={WIDTH},{HEIGHT}",
    f"--screenshot={png_artifact}",
    f"file:///{html_wrapper.replace(os.sep, '/')}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge screenshot code:", res.returncode)

png_final_1 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 Entity Relationship Diagram (ERD) Sistem Informasi ARTHA.png"
png_final_2 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar 3.9 ERD Sistem Informasi ARTHA.png"
png_final_3 = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.png"

if os.path.exists(png_artifact):
    shutil.copyfile(png_artifact, png_final_1)
    shutil.copyfile(png_artifact, png_final_2)
    shutil.copyfile(png_artifact, png_final_3)
    print("Copied PNG to all assets directories!")
