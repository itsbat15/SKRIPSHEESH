from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'BAB3_PENDUKUNG_2026-10-25/gambar'
OUT.mkdir(parents=True, exist_ok=True)
FONT = 'C:/Windows/Fonts/times.ttf'
BOLD = 'C:/Windows/Fonts/timesbd.ttf'

class Figure:
    def __init__(self, w, h):
        self.w,self.h=w,h
        self.im=Image.new('RGB',(w,h),'white'); self.d=ImageDraw.Draw(self.im)
        self.s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>']
    def line(self, points, arrow=False, color='#222222', width=3):
        self.d.line(points,fill=color,width=width)
        self.s.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
        if arrow:
            x,y=points[-1];a,b=points[-2];t=math.atan2(y-b,x-a)
            tri=[(x,y),(x-15*math.cos(t-.4),y-15*math.sin(t-.4)),(x-15*math.cos(t+.4),y-15*math.sin(t+.4))]
            self.d.polygon(tri,fill=color);self.s.append('<polygon points="'+' '.join(f'{a},{b}' for a,b in tri)+f'" fill="{color}"/>')
    def text(self,x,y,text,size=30,bold=False,center=True):
        font=ImageFont.truetype(BOLD if bold else FONT,size)
        for j,t in enumerate(text.split('\n')):
            yy=y+j*(size+9)
            self.d.text((x,yy),t,font=font,fill='#111111',anchor='mt' if center else 'lt')
            self.s.append(f'<text x="{x}" y="{yy+size*.82}" text-anchor="'+('middle' if center else 'start')+f'" font-family="Times New Roman,serif" font-size="{size}" font-weight="'+('bold' if bold else 'normal')+'">'+escape(t)+'</text>')
    def box(self,x,y,w,h,label,size=29,fill='#f5f5f5',oval=False):
        if oval:
            self.d.ellipse((x,y,x+w,y+h),fill=fill,outline='#222222',width=3)
            self.s.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="#222222" stroke-width="3"/>')
        else:
            self.d.rounded_rectangle((x,y,x+w,y+h),radius=10,fill=fill,outline='#222222',width=3)
            self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="#222222" stroke-width="3"/>')
        n=label.count('\n')+1;self.text(x+w/2,y+(h-n*(size+9))/2+5,label,size)
    def save(self,name):
        self.im.save(OUT/(name+'.png'));(OUT/(name+'.svg')).write_text(''.join(self.s)+'</svg>',encoding='utf-8')

f=Figure(1800,1920)
labels=['Kebutuhan dan studi literatur\n(3.3.1)','Perencanaan proyek\n(3.3.2)','Inisialisasi iterasi\n(3.3.3)','Perancangan modul\n(3.3.4)','Implementasi dan pengujian unit\n(3.3.5)','Pengujian sistem dan perbaikan\n(3.3.6)','Evaluasi iterasi\n(3.3.7)','UAT dan analisis evaluasi\n(3.3.8)','Dokumentasi dan penyiapan luaran']
ys=[80,260,490,670,850,1030,1210,1510,1740]
for i in range(len(ys)-1): f.line([(925,ys[i]+120),(925,ys[i+1])],True)
f.line([(1350,1270),(1640,1270),(1640,550),(1350,550)],True)
f.text(1490,880,'Iterasi\nberikutnya',27)
f.line([(500,1570),(80,1570),(80,315),(500,315)],True)
f.text(280,1010,'Revisi kebutuhan\natau fungsi\nberdasarkan UAT',27)
for y,l in zip(ys,labels): f.box(500,y,850,120,l)
f.text(1170,1400,'Seluruh fungsi siap\ndievaluasi mitra',26)
f.text(1170,1670,'Perbaikan telah\ndiuji ulang',25)
f.save('Gambar_3_1_Alur_Pembuatan_Prototipe')

f=Figure(1800,1640)
f.box(450,80,900,1420,'',fill='#ffffff')
f.text(900,105,'Sistem Informasi Manajemen Operasional ARTHA',30,True)
def actor(x,y,label):
    f.d.ellipse((x-23,y,x+23,y+46),outline='black',width=3)
    f.s.append(f'<circle cx="{x}" cy="{y+23}" r="23" fill="white" stroke="black" stroke-width="3"/>')
    for pts in [[(x,y+46),(x,y+122)],[(x-42,y+75),(x+42,y+75)],[(x,y+122),(x-40,y+180)],[(x,y+122),(x+40,y+180)]]: f.line(pts)
    f.text(x,y+195,label,29,True)
actor(200,560,'Admin Cabang');actor(1600,560,'Super Admin')
ucs=[('UC-01\nMasuk dan keluar sistem',220,'both'),('UC-02\nKelola siswa dan keanggotaan',380,'both'),('UC-03\nKelola kelas dan jadwal',540,'both'),('UC-04\nCatat pembayaran dan bukti',700,'admin'),('UC-05\nBuka tautan penagihan WhatsApp',860,'admin'),('UC-06\nPantau dasbor sesuai kewenangan',1020,'both'),('UC-07\nPeriksa transfer dan pencocokan',1180,'super'),('UC-08\nKelola data induk dan akun',1340,'super')]
for l,y,who in ucs:
    if who in ('admin','both'): f.line([(250,645),(540,y+48)],width=2)
    if who in ('super','both'): f.line([(1550,645),(1260,y+48)],width=2)
for l,y,who in ucs: f.box(540,y,720,96,l,27,oval=True,fill='#ffffff')
f.text(900,1550,'Diagram fungsi inti; rincian kewenangan dan alur alternatif dijabarkan dalam skenario.',26)
f.save('Gambar_3_2_Use_Case_Inti')

f=Figure(2000,1540)
nodes={'Cabang':(70,80),'Pengguna':(760,80),'Pemeriksaan':(1450,80),'Siswa':(70,430),'Tagihan':(760,430),'Pembayaran':(1450,430),'Keanggotaan':(70,780),'Kelas':(760,780),'Pencocokan':(1450,780),'Tentor':(70,1130),'Jadwal':(760,1130),'Setoran Kas':(1450,1130)}
edges=[('Cabang','Pengguna','1 : N'),('Pengguna','Pemeriksaan','1 : N'),('Siswa','Tagihan','1 : N'),('Tagihan','Pembayaran','1 : N'),('Siswa','Keanggotaan','1 : N'),('Keanggotaan','Kelas','N : 1'),('Tentor','Jadwal','1 : N'),('Kelas','Jadwal','1 : N'),('Pembayaran','Pemeriksaan','1 : N'),('Pembayaran','Pencocokan','1 : 0..1'),('Setoran Kas','Pencocokan','1 : 0..1')]
for a,b,l in edges:
    x,y=nodes[a];xx,yy=nodes[b]
    if y==yy:
        left=(x+500,y+95) if xx>x else (x,y+95);right=(xx,yy+95) if xx>x else (xx+500,yy+95)
        f.line([left,right]);f.text((left[0]+right[0])/2,y+60,l,25)
    else:
        if yy>y: p1=(x+250,y+190);p2=(xx+250,yy)
        else:p1=(x+250,y);p2=(xx+250,yy+190)
        f.line([p1,p2]);f.text(p1[0]+70,(p1[1]+p2[1])/2-5,l,25)
fields={'Cabang':'id_cabang (PK)\nnama dan status cabang','Pengguna':'id_pengguna (PK)\nperan dan id_cabang (FK)','Pemeriksaan':'id_pemeriksaan (PK)\npembayaran, pemeriksa, keputusan','Siswa':'id_siswa (PK)\nid_cabang (FK), kontak wali','Tagihan':'id_tagihan (PK)\nsiswa, periode, jatuh tempo','Pembayaran':'id_pembayaran (PK)\ntagihan, nominal, kanal, bukti','Keanggotaan':'id_keanggotaan (PK)\nsiswa, kelas, status, tanggal keluar','Kelas':'id_kelas (PK)\ncabang, ruang, kapasitas','Pencocokan':'id_pencocokan (PK)\nasal transaksi, referensi mutasi','Tentor':'id_tentor (PK)\nnama dan status aktif','Jadwal':'id_jadwal (PK)\nkelas, tentor, ruang, waktu','Setoran Kas':'id_setoran (PK)\ncabang, periode, jumlah, penerima'}
for n,(x,y) in nodes.items():
    f.box(x,y,500,190,'',fill='#ffffff');f.text(x+250,y+15,n,31,True);f.line([(x,y+60),(x+500,y+60)],width=2);f.text(x+250,y+77,fields[n],24)
f.text(1000,1420,'Model konseptual: relasi master lain dan atribut lengkap dijabarkan dalam kamus data.',27)
f.text(1000,1460,'Pencocokan memakai salah satu asal: transfer siswa atau setoran kas ke bank.',27)
f.save('Gambar_3_3_Model_Data_Konseptual')

f=Figure(1500,1300)
boxes=[(360,60,780,150,'Admin Cabang dan Super Admin\nPeramban komputer atau telepon'),(360,310,780,150,'Antarmuka Next.js\nFormulir, daftar, dan dasbor'),(360,560,780,150,'Layanan Laravel\nAutentikasi, otorisasi, aturan bisnis'),(360,810,780,150,'MySQL dan penyimpanan berkas privat\nData terpusat serta bukti pembayaran')]
for i in range(3):f.line([(750,boxes[i][1]+150),(750,boxes[i+1][1])],True)
for x,y,w,h,t in boxes:f.box(x,y,w,h,t,31)
f.box(60,1070,600,130,'WhatsApp melalui tautan\nPesan dikirim oleh admin',29)
f.box(840,1070,600,130,'Mutasi rekening resmi\nDiperiksa oleh petugas berwenang',29)
f.line([(360,385),(160,385),(160,1070)],True)
f.text(1150,1000,'Pencocokan manual, tanpa koneksi API bank',24)
f.text(750,1250,'Notifikasi pengajuan pembayaran ditampilkan di dalam dasbor Super Admin.',27)
f.save('Gambar_3_4_Arsitektur_Prototipe')
print('Created four PNG and four SVG diagrams in '+str(OUT))
