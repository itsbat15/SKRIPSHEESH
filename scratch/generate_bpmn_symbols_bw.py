import os
from PIL import Image, ImageDraw, ImageFont

out_dir = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 2\ASET BAB 2.1\simbol_bpmn_artha"
os.makedirs(out_dir, exist_ok=True)

# Helper function to draw at 4x resolution and downscale for ultra-crisp anti-aliasing
def create_canvas(w, h, scale=4):
    img = Image.new('RGBA', (w * scale, h * scale), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    return img, draw, scale

def save_scaled(img, scale, filename):
    w, h = img.size
    final_img = img.resize((w // scale, h // scale), Image.Resampling.LANCZOS)
    final_img.save(os.path.join(out_dir, filename), format='PNG')
    print(f"Saved {filename} ({w // scale}x{h // scale}) [Pure B&W]")

# 1. Start Event (Lingkaran Tunggal Tipis - Dumas p. 76)
img, d, s = create_canvas(100, 80)
d.ellipse([ (50-26)*s, (40-26)*s, (50+26)*s, (40+26)*s ], fill='#FFFFFF', outline='#000000', width=2*s)
save_scaled(img, s, 'simbol_start_event.png')

# 2. Intermediate Event (Lingkaran Ganda Tipis - Dumas p. 123)
img, d, s = create_canvas(100, 80)
d.ellipse([ (50-26)*s, (40-26)*s, (50+26)*s, (40+26)*s ], fill='#FFFFFF', outline='#000000', width=2*s)
d.ellipse([ (50-20)*s, (40-20)*s, (50+20)*s, (40+20)*s ], fill='#FFFFFF', outline='#000000', width=2*s)
save_scaled(img, s, 'simbol_intermediate_event.png')

# 3. End Event (Lingkaran Tunggal Tebal - Dumas p. 76)
img, d, s = create_canvas(100, 80)
d.ellipse([ (50-26)*s, (40-26)*s, (50+26)*s, (40+26)*s ], fill='#FFFFFF', outline='#000000', width=5*s)
save_scaled(img, s, 'simbol_end_event.png')

# 4. Task / Activity (Persegi Panjang Sudut Tumpul - Dumas p. 76)
img, d, s = create_canvas(160, 80)
d.rounded_rectangle([ 15*s, 15*s, 145*s, 65*s ], radius=10*s, fill='#FFFFFF', outline='#000000', width=2*s)
try:
    font = ImageFont.truetype("arial.ttf", 11*s)
    d.text((80*s, 40*s), "Task / Activity", fill='#000000', font=font, anchor="mm")
except Exception:
    d.line([ 40*s, 35*s, 120*s, 35*s ], fill='#000000', width=2*s)
    d.line([ 50*s, 45*s, 110*s, 45*s ], fill='#000000', width=2*s)
save_scaled(img, s, 'simbol_task.png')

# 5. Exclusive Gateway (XOR) (Belah Ketupat Bersilang X - Dumas p. 80)
img, d, s = create_canvas(100, 80)
pts = [ (50*s, 12*s), (82*s, 40*s), (50*s, 68*s), (18*s, 40*s) ]
d.polygon(pts, fill='#FFFFFF', outline='#000000')
d.line(pts + [pts[0]], fill='#000000', width=2*s)
# Draw X inside
d.line([ (50-10)*s, (40-10)*s, (50+10)*s, (40+10)*s ], fill='#000000', width=3*s)
d.line([ (50-10)*s, (40+10)*s, (50+10)*s, (40-10)*s ], fill='#000000', width=3*s)
save_scaled(img, s, 'simbol_exclusive_gateway.png')

# 6. Parallel Gateway (AND) (Belah Ketupat Bertanda Tambah + - Dumas p. 82)
img, d, s = create_canvas(100, 80)
pts = [ (50*s, 12*s), (82*s, 40*s), (50*s, 68*s), (18*s, 40*s) ]
d.polygon(pts, fill='#FFFFFF', outline='#000000')
d.line(pts + [pts[0]], fill='#000000', width=2*s)
# Draw + inside
d.line([ 50*s, (40-12)*s, 50*s, (40+12)*s ], fill='#000000', width=3*s)
d.line([ (50-12)*s, 40*s, (50+12)*s, 40*s ], fill='#000000', width=3*s)
save_scaled(img, s, 'simbol_parallel_gateway.png')

# 7. Sequence Flow (Garis Lurus Panah Padat - Dumas p. 77)
img, d, s = create_canvas(180, 50)
d.line([ 20*s, 25*s, 145*s, 25*s ], fill='#000000', width=2*s)
arrow_pts = [ (160*s, 25*s), (145*s, 18*s), (145*s, 32*s) ]
d.polygon(arrow_pts, fill='#000000')
save_scaled(img, s, 'simbol_sequence_flow.png')

# 8. Message Flow (Garis Putus-Putus Panah Terbuka & Lingkaran Awal - Dumas p. 100)
img, d, s = create_canvas(180, 50)
# Start circle (open)
d.ellipse([ 15*s, 21*s, 23*s, 29*s ], fill='#FFFFFF', outline='#000000', width=2*s)
# Dashed line
x = 25
while x < 145:
    d.line([ x*s, 25*s, min(x+6, 145)*s, 25*s ], fill='#000000', width=2*s)
    x += 10
# Open arrowhead
d.line([ 145*s, 17*s, 160*s, 25*s ], fill='#000000', width=2*s)
d.line([ 145*s, 33*s, 160*s, 25*s ], fill='#000000', width=2*s)
save_scaled(img, s, 'simbol_message_flow.png')

# 9. Pool (Wadah Organisasi Mandiri - Dumas p. 96)
img, d, s = create_canvas(180, 80)
d.rectangle([ 15*s, 15*s, 165*s, 65*s ], fill='#FFFFFF', outline='#000000', width=2*s)
d.line([ 45*s, 15*s, 45*s, 65*s ], fill='#000000', width=2*s)
try:
    font_v = ImageFont.truetype("arial.ttf", 9*s)
    d.text((30*s, 40*s), "Pool", fill='#000000', font=font_v, anchor="mm")
except Exception:
    pass
save_scaled(img, s, 'simbol_pool.png')

# 10. Lane (Partisi Horizontal di Dalam Pool - Dumas p. 96)
img, d, s = create_canvas(180, 80)
d.rectangle([ 15*s, 15*s, 165*s, 65*s ], fill='#FFFFFF', outline='#000000', width=2*s)
d.line([ 45*s, 15*s, 45*s, 65*s ], fill='#000000', width=2*s)
# Horizontal lane partition
d.line([ 45*s, 40*s, 165*s, 40*s ], fill='#000000', width=1*s)
try:
    font_v = ImageFont.truetype("arial.ttf", 8*s)
    d.text((30*s, 27*s), "Lane 1", fill='#000000', font=font_v, anchor="mm")
    d.text((30*s, 52*s), "Lane 2", fill='#000000', font=font_v, anchor="mm")
except Exception:
    pass
save_scaled(img, s, 'simbol_lane.png')

# 11. Data Object (Dokumen Sudut Terlipat - Dumas p. 89)
img, d, s = create_canvas(120, 80)
pts = [ (40*s, 15*s), (70*s, 15*s), (80*s, 25*s), (80*s, 65*s), (40*s, 65*s) ]
d.polygon(pts, fill='#FFFFFF', outline='#000000')
d.line(pts + [pts[0]], fill='#000000', width=2*s)
d.line([ 70*s, 15*s, 70*s, 25*s, 80*s, 25*s ], fill='#000000', width=2*s)
try:
    font_do = ImageFont.truetype("arial.ttf", 8*s)
    d.text((60*s, 45*s), "Data\nObject", fill='#000000', font=font_do, anchor="mm", align="center")
except Exception:
    pass
save_scaled(img, s, 'simbol_data_object.png')

# 12. Data Store (Silinder Basis Data - Dumas p. 93)
img, d, s = create_canvas(120, 80)
d.ellipse([ 40*s, 18*s, 80*s, 30*s ], fill='#FFFFFF', outline='#000000', width=2*s)
d.rectangle([ 40*s, 24*s, 80*s, 56*s ], fill='#FFFFFF', outline=None)
d.line([ 40*s, 24*s, 40*s, 56*s ], fill='#000000', width=2*s)
d.line([ 80*s, 24*s, 80*s, 56*s ], fill='#000000', width=2*s)
d.arc([ 40*s, 48*s, 80*s, 62*s ], 0, 180, fill='#000000', width=2*s)
d.arc([ 40*s, 34*s, 80*s, 48*s ], 0, 180, fill='#000000', width=1*s)
try:
    font_ds = ImageFont.truetype("arial.ttf", 8*s)
    d.text((60*s, 44*s), "Data\nStore", fill='#000000', font=font_ds, anchor="mm", align="center")
except Exception:
    pass
save_scaled(img, s, 'simbol_data_store.png')

print("All pure B&W BPMN symbols generated successfully!")

