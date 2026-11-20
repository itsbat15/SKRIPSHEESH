from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'DRAFT PROPOSAL MD/BAB 2/ASET BAB 2.1'
OUT.mkdir(exist_ok=True)
W,H=1500,1590
im=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(im)
fontpath='C:/Windows/Fonts/arial.ttf'
boldpath='C:/Windows/Fonts/arialbd.ttf'
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><rect width="100%" height="100%" fill="white"/>']
def line(points,dash=False,arrow=False):
 if dash:
  import math
  for (x,y),(xx,yy) in zip(points,points[1:]):
   length=math.hypot(xx-x,yy-y)
   for s in range(0,int(length),18):
    a=s/length;b=min(s+10,length)/length
    d.line([(x+(xx-x)*a,y+(yy-y)*a),(x+(xx-x)*b,y+(yy-y)*b)],fill='#444444',width=3)
 else:d.line(points,fill='#222222',width=4)
 svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+'" fill="none" stroke="#222" stroke-width="3"'+(' stroke-dasharray="10 8"' if dash else '')+'/>')
 if arrow:
  import math
  x,y=points[-1];a,b=points[-2];angle=math.atan2(y-b,x-a)
  pts=[(x,y),(x-18*math.cos(angle-.5),y-18*math.sin(angle-.5)),(x-18*math.cos(angle+.5),y-18*math.sin(angle+.5))]
  d.polygon(pts,fill='#222222');svg.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in pts)+'" fill="#222"/>')
def text(x,y,s,size=32,bold=False):
 f=ImageFont.truetype(boldpath if bold else fontpath,size)
 d.text((x,y),s,font=f,fill='#111111',anchor='mm')
 svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}">{escape(s)}</text>')
def box(x,y,w,h,labels,fill='#f4f4f4',size=32,bold=False):
 d.rectangle((x,y,x+w,y+h),outline='#222222',fill=fill,width=3)
 svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#222" stroke-width="3"/>')
 for j,s in enumerate(labels):text(x+w/2,y+h/2+(j-(len(labels)-1)/2)*(size+10),s,size,bold)
box(110,320,830,1050,[],fill='white')
text(300,354,'SIKLUS ITERASI',28,True)
phases=[(70,['Requirements','Penggalian kebutuhan']),(200,['Planning','Perencanaan']),(410,['Iteration initialization','Inisialisasi iterasi']),(550,['Design','Perancangan']),(970,['System testing','Pengujian sistem']),(1110,['Retrospective','Evaluasi iterasi'])]
for y,labels in phases:box(220,y,610,95,labels)
for y,y2 in [(165,200),(295,410),(505,550),(645,700),(920,970),(1065,1110)]:line([(525,y),(525,y2)],arrow=True)
box(170,700,710,220,[],fill='#f8f8f8')
text(525,737,'Implementation / Implementasi',31,True)
box(192,790,203,92,['Unit testing','Pengujian unit'],size=23,fill='white')
box(424,790,203,92,['Code','Pengodean'],size=23,fill='white')
box(656,790,203,92,['Refactoring','Perapian kode'],size=23,fill='white')
line([(395,836),(424,836)],arrow=True);line([(627,836),(656,836)],arrow=True)
line([(830,1157),(904,1157),(904,388),(525,388),(525,410)],arrow=True)
box(1010,645,380,310,['LOG PENGEMBANGAN','Estimasi dan waktu aktual','Cacat dan perbaikannya','Usulan perbaikan proses'],size=25,fill='white')
for x,y in [(830,247),(880,810),(830,1017),(830,1157)]:line([(x,y),(970,y),(1010,800)],dash=True)
text(525,1265,'Iterasi dilanjutkan sesuai kebutuhan.',25)
text(750,1450,'Garis utuh: urutan tahap dan pengulangan iterasi.',27)
text(750,1500,'Garis putus-putus: hubungan tahap dengan catatan pengembangan.',27)
svg.append('</svg>')
(OUT/'Gambar 2.1 Tahapan PxP.svg').write_text('\n'.join(svg),encoding='utf-8')
im.save(OUT/'Gambar 2.1 Tahapan PxP.png')
print(OUT/'Gambar 2.1 Tahapan PxP.png')
