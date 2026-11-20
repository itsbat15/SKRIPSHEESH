from PIL import Image
import numpy as np

im = Image.open(r'C:/Users/ARIEL/.gemini/antigravity/brain/b4f2bb35-f783-4d11-88ed-819fbfb3f0fb/.user_uploaded/media_1793874497647_02e1b81b.png').convert('RGB')
arr = np.array(im)

cols2 = [49, 231, 249, 264, 279, 296, 316, 333, 348, 365, 382, 399, 415, 432, 451, 470, 488, 507, 526, 547, 565, 582, 601, 617, 634, 654, 686]
col_mid2 = [(cols2[i] + cols2[i+1]) // 2 for i in range(1, len(cols2)-1)]

col_names = [
    "Sep 1", "Sep 2", "Sep 3", "Sep 4",
    "Okt 1", "Okt 2", "Okt 3", "Okt 4",
    "Nov 1", "Nov 2", "Nov 3", "Nov 4",
    "Des 1", "Des 2", "Des 3", "Des 4",
    "Apr 1", "Apr 2", "Apr 3", "Apr 4",
    "Mei 1", "Mei 2", "Mei 3", "Mei 4",
    "Jun 1"
]

rows2 = [
    ("Planning", 465),
    ("Iteration Initialization", 490),
    ("Design", 520),
    ("Implementation", 545),
    ("System Testing", 575),
    ("Retrospective", 600),
    ("Deployment", 630),
    ("User Training", 655),
    ("Kesimpulan dan Saran", 685),
]

for rname, y in rows2:
    shaded = []
    for c_idx, x in enumerate(col_mid2):
        r, g, b = [int(v) for v in arr[y, x]]
        if abs(r - 0x5f) < 40 and abs(g - 0x49) < 40 and abs(b - 0x7a) < 40:
            shaded.append((col_names[c_idx], "PURPLE"))
        elif abs(r - 0x21) < 40 and abs(g - 0x58) < 40 and abs(b - 0x68) < 40:
            shaded.append((col_names[c_idx], "TEAL"))
    print(f"\n{rname}:")
    for c, col_type in shaded:
        print(f"  {c} ({col_type})", end=", ")
    print()

