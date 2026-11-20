from PIL import Image, ImageDraw, ImageFont
import os

# Create visual guide for the user
w, h = 900, 480
img = Image.new('RGB', (w, h), (255, 255, 255))
d = ImageDraw.Draw(img)

# Title
d.rectangle([0, 0, w, 45], fill='#1E293B')
d.text((w//2, 22), "PANDUAN PERBAIKAN GERBANG BIZAGI: 3 BELAH KETUPAT vs 4 BELAH KETUPAT", fill='#FFFFFF', anchor="mm")

# Left Column: KONDISI SEKARANG (3 BELAH KETUPAT - SALAH / DEADLOCK)
d.rectangle([20, 60, 430, 450], fill='#FFF5F5', outline='#FF8787', width=2)
d.rectangle([20, 60, 430, 95], fill='#FFC9C9')
d.text((225, 77), "Kondisi di Bizagi Anda Sekarang (SALAH - DEADLOCK)", fill='#C92A2A', anchor="mm")

# Text explanation left
d.text((35, 110), "- Ada 3 belah ketupat di seluruh diagram.", fill='#495057')
d.text((35, 130), "- Dua panah (Tunai & Valid) masuk ke gerbang (+) yang sama.", fill='#C92A2A')
d.text((35, 150), "- AKIBAT: Gerbang (+) akan macet total (deadlock)", fill='#C92A2A')
d.text((35, 170), "  karena menunggu uang Tunai dan Transfer bersamaan!", fill='#C92A2A')

# Draw diagram left
# Box Tunai
d.rectangle([40, 205, 180, 245], fill='#FFFFFF', outline='#1C7ED6', width=2)
d.text((110, 225), "Terima Uang Tunai", fill='#1864AB', anchor="mm")

# Box Validasi
d.rectangle([40, 290, 180, 330], fill='#FFFFFF', outline='#1C7ED6', width=2)
d.text((110, 310), "Validasi Transfer", fill='#1864AB', anchor="mm")

# Diamond Bukti Valid?
d.polygon([(230, 310), (250, 290), (270, 310), (250, 330)], fill='#FFF9DB', outline='#E67700')
d.text((250, 310), "X", fill='#D9480F', anchor="mm")
d.line([(180, 310), (230, 310)], fill='#000000', width=2)

# Diamond Plus (+)
d.polygon([(340, 310), (360, 290), (380, 310), (360, 330)], fill='#FFF9DB', outline='#E67700')
d.text((360, 310), "+", fill='#D9480F', anchor="mm")

# Arrow from Bukti Valid to Plus
d.line([(270, 310), (340, 310)], fill='#000000', width=2)
d.text((305, 300), "Valid", fill='#2B8A3E', anchor="mm")

# Arrow from Tunai entering bottom of Plus
d.line([(180, 225), (360, 225), (360, 350), (360, 330)], fill='#C92A2A', width=2)

# Two arrows out of Plus
d.line([(360, 290), (360, 260), (410, 260)], fill='#000000', width=2)
d.text((415, 260), "> Kuitansi", fill='#495057', anchor="lm")
d.line([(380, 310), (410, 310)], fill='#000000', width=2)
d.text((415, 310), "> Rekap Kas", fill='#495057', anchor="lm")

d.text((225, 415), "Dua panah masuk ke (+) = DEADLOCK!", fill='#C92A2A', anchor="mm")

# Right Column: KONDISI BENAR (4 BELAH KETUPAT)
d.rectangle([470, 60, 880, 450], fill='#EBFBEE', outline='#69DB7C', width=2)
d.rectangle([470, 60, 880, 95], fill='#B2F2BB')
d.text((675, 77), "Kondisi yang Benar (4 BELAH KETUPAT - SEMPURNA)", fill='#2B8A3E', anchor="mm")

# Text explanation right
d.text((485, 110), "- Ada 4 belah ketupat di seluruh diagram.", fill='#495057')
d.text((485, 130), "- Selipkan belah ketupat (X) baru sebelum gerbang (+).", fill='#2B8A3E')
d.text((485, 150), "- Tunai dan Transfer bersatu di belah ketupat (X).", fill='#2B8A3E')
d.text((485, 170), "- Hanya 1 panah masuk ke gerbang (+) = BEBAS MACET!", fill='#2B8A3E')

# Draw diagram right
# Box Tunai
d.rectangle([490, 205, 620, 245], fill='#FFFFFF', outline='#1C7ED6', width=2)
d.text((555, 225), "Terima Uang Tunai", fill='#1864AB', anchor="mm")

# Box Validasi
d.rectangle([490, 290, 620, 330], fill='#FFFFFF', outline='#1C7ED6', width=2)
d.text((555, 310), "Validasi Transfer", fill='#1864AB', anchor="mm")

# Diamond 2: Bukti Valid?
d.polygon([(645, 310), (665, 290), (685, 310), (665, 330)], fill='#FFF9DB', outline='#E67700')
d.text((665, 310), "X", fill='#D9480F', anchor="mm")
d.line([(620, 310), (645, 310)], fill='#000000', width=2)

# Diamond 3: XOR-Join BARU (X)
d.polygon([(720, 310), (740, 290), (760, 310), (740, 330)], fill='#D0EBFF', outline='#1971C2', width=2)
d.text((740, 310), "X", fill='#1971C2', anchor="mm")

# Diamond 4: Plus (+)
d.polygon([(795, 310), (815, 290), (835, 310), (815, 330)], fill='#FFF9DB', outline='#E67700')
d.text((815, 310), "+", fill='#D9480F', anchor="mm")

# Arrow from Bukti Valid to XOR-Join BARU
d.line([(685, 310), (720, 310)], fill='#000000', width=2)
d.text((702, 300), "Valid", fill='#2B8A3E', anchor="mm")

# Arrow from Tunai into TOP of XOR-Join BARU
d.line([(620, 225), (740, 225), (740, 290)], fill='#1971C2', width=2)

# One arrow from XOR-Join BARU into Plus (+)
d.line([(760, 310), (795, 310)], fill='#000000', width=2)

# Two arrows out of Plus
d.line([(815, 290), (815, 260), (850, 260)], fill='#000000', width=2)
d.text((855, 260), "> Kuitansi", fill='#495057', anchor="lm")
d.line([(835, 310), (850, 310)], fill='#000000', width=2)
d.text((855, 310), "> Rekap Kas", fill='#495057', anchor="lm")

d.text((675, 415), "Belah ketupat (X) baru menyatukan Tunai & Transfer!", fill='#2B8A3E', anchor="mm")

out_path = r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\panduan_koreksi_gateway.png"
img.save(out_path)
print("Saved guide image to", out_path)

