from PIL import Image

im = Image.open("scripts/agarwal_page4_highlighted.png")
w, h = im.size
print(f"Image size: {w}x{h}")
# dpi = 150. A4 is 594.96 x 841.92 pt -> w = 594.96 * 150/72 = 1240, h = 841.92 * 150/72 = 1754
# Let's crop y from 200*150/72 to 450*150/72
crop_box = (int(40 * 150 / 72), int(240 * 150 / 72), int(570 * 150 / 72), int(420 * 150 / 72))
cropped = im.crop(crop_box)
cropped.save("scripts/agarwal_crop.png")
print("Saved scripts/agarwal_crop.png")
