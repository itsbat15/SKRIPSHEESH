from PIL import Image
import numpy as np

im = Image.open(r'C:/Users/ARIEL/.gemini/antigravity/brain/b4f2bb35-f783-4d11-88ed-819fbfb3f0fb/.user_uploaded/media_1793874497647_02e1b81b.png').convert('RGB')
arr = np.array(im)

cols = [11, 192, 211, 225, 241, 258, 278, 294, 310, 326, 344, 360, 377, 394, 413, 427, 450, 469, 488, 508, 527, 544, 563, 579, 596, 616, 648]

col_mid = [(cols[i] + cols[i+1]) // 2 for i in range(1, len(cols)-1)]
print(f"Number of week columns: {len(col_mid)}")

# Row Y coordinates:
# Table 1:
# Row 1: Mengidentifikasi Masalah ~ y=140
# Row 2: Studi Literatur ~ y=170
# Row 3: Requirements ~ y=195
# Table 2:
# Row 4: Planning ~ y=465
# Row 5: Iteration Initialization ~ y=490
# Row 6: Design ~ y=520
# Row 7: Implementation ~ y=545
# Row 8: System Testing ~ y=575
# Row 9: Retrospective ~ y=600
# Row 10: Deployment ~ y=630
# Row 11: User Training ~ y=655
# Row 12: Kesimpulan dan Saran ~ y=685

rows = [
    ("Mengidentifikasi Masalah", 140),
    ("Studi Literatur", 170),
    ("Requirements", 195),
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

col_names = [
    "Sep 1", "Sep 2", "Sep 3", "Sep 4",
    "Okt 1", "Okt 2", "Okt 3", "Okt 4",
    "Nov 1", "Nov 2", "Nov 3", "Nov 4",
    "Des 1", "Des 2", "Des 3", "Des 4",
    "Apr 1", "Apr 2", "Apr 3", "Apr 4",
    "Mei 1", "Mei 2", "Mei 3", "Mei 4",
    "Jun 1"
]

for rname, y in rows:
    shaded = []
    for c_idx, x in enumerate(col_mid):
        pix = arr[y, x]
        # check purple
        if np.abs(pix[0] - 0x5f) < 30 and np.abs(pix[1] - 0x49) < 30 and np.abs(pix[2] - 0x7a) < 30:
            shaded.append((col_names[c_idx], "PURPLE"))
        elif np.abs(pix[0] - 0x21) < 30 and np.abs(pix[1] - 0x58) < 30 and np.abs(pix[2] - 0x68) < 30:
            shaded.append((col_names[c_idx], "TEAL"))
    print(f"\n{rname}:")
    for c, col_type in shaded:
        print(f"  {c} ({col_type})", end=", ")
    print()

