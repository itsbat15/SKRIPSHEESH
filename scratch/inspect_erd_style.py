import os
from PIL import Image

for folder in ['simbol_erd_chen', 'simbol_erd_artha', 'simbol_activity_artha', 'simbol_usecase_artha']:
    p = os.path.join('DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1', folder)
    print('=== Folder:', folder)
    if os.path.exists(p):
        for f in os.listdir(p)[:3]:
            im = Image.open(os.path.join(p, f))
            # get unique RGB values (excluding transparent alpha=0)
            rgbs = set()
            for pix in im.getdata():
                if len(pix) == 4 and pix[3] > 10:
                    rgbs.add((pix[0], pix[1], pix[2]))
            print(f"  {f}: size={im.size}, sample non-transparent RGBs: {list(rgbs)[:5]}")

