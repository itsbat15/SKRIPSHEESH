"""Generate editable SVG and matching PNG draft figures; all UI values are fictional."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from html import escape
import math
import shutil
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'BAB3_PENDUKUNG_2026-10-25/gambar'
BACK = ROOT / 'DOKUMEN MD/REVISI_TERPADU_2026-10-25/SEBELUM_REVISI/gambar'
BACK.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)
for original in ['Gambar_3_1_Alur_Pembuatan_Prototipe', 'Gambar_3_2_Use_Case_Inti', 'Gambar_3_3_Model_Data_Konseptual', 'Gambar_3_4_Arsitektur_Prototipe']:
    for ext in ['.png', '.svg']:
        old = OUT / (original + ext)
        target = BACK / old.name
        if old.exists() and not target.exists():
            shutil.copy2(old, target)

class Figure:
    def __init__(self, w, h, ui=False):
        self.w, self.h, self.ui = w, h, ui
        self.im = Image.new('RGB', (w,h), 'white')
        self.d = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>']
        self.labels = []
    def font(self, size, bold=False):
        name = ('arialbd.ttf' if bold else 'arial.ttf') if self.ui else ('timesbd.ttf' if bold else 'times.ttf')
        return ImageFont.truetype('C:/Windows/Fonts/'+name, size)
    def text(self, x,y,text,size=30,bold=False,center=False,color='#202020'):
        family = 'Arial,sans-serif' if self.ui else 'Times New Roman,serif'
        font = self.font(size,bold)
        for n,line in enumerate(text.split('\n')):
            yy=y+n*(size+10)
            self.d.text((x,yy),line,font=font,fill=color,anchor='mt' if center else 'lt')
            self.svg.append(f'<text x="{x}" y="{yy+size*.82}" text-anchor="'+('middle' if center else 'start')+f'" font-family="{family}" font-size="{size}" font-weight="'+('bold' if bold else 'normal')+f'" fill="{color}">'+escape(line)+'</text>')
            self.labels.append({'text':line,'x':x,'y':yy,'size':size})
    def rect(self,x,y,w,h,fill='#ffffff',stroke='#333333',width=2,r=8):
        self.d.rounded_rectangle((x,y,x+w,y+h),radius=r,fill=fill,outline=stroke,width=width)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>')
    def box(self,x,y,w,h,label,size=30,bold=False,fill='#f6f6f6',oval=False):
        if oval:
            self.d.ellipse((x,y,x+w,y+h),fill=fill,outline='#333333',width=2)
            self.svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="#333333" stroke-width="2"/>')
        else:
            self.rect(x,y,w,h,fill)
        self.text(x+w/2,y+(h-(label.count('\n')+1)*(size+10))/2+4,label,size,bold,True)
    def line(self,pts,arrow=False,color='#333333',width=3):
        self.d.line(pts,fill=color,width=width)
        self.svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
        if arrow:
            x,y=pts[-1];a,b=pts[-2];t=math.atan2(y-b,x-a)
            tri=[(x,y),(x-14*math.cos(t-.45),y-14*math.sin(t-.45)),(x-14*math.cos(t+.45),y-14*math.sin(t+.45))]
            self.d.polygon(tri,fill=color)
            self.svg.append('<polygon points="'+' '.join(f'{xx},{yy}' for xx,yy in tri)+f'" fill="{color}"/>')
    def decision(self,x,y,w,h,label,size=29):
        pts=[(x+w/2,y),(x+w,y+h/2),(x+w/2,y+h),(x,y+h/2)]
        self.d.polygon(pts,fill='#ededed',outline='#333333',width=3)
        self.svg.append('<polygon points="'+' '.join(f'{xx},{yy}' for xx,yy in pts)+'" fill="#ededed" stroke="#333333" stroke-width="3"/>')
        self.text(x+w/2,y+(h-(label.count('\n')+1)*(size+10))/2+4,label,size,False,True)
    def save(self,name):
        self.im.save(OUT/(name+'.png'),dpi=(300,300))
        (OUT/(name+'.svg')).write_text(''.join(self.svg)+'</svg>',encoding='utf-8')
        return name

names=[]

# Flowchart: named decisions make loops explicit and distinguish defects from changed needs.
f=Figure(2200,3000)
f.text(1100,35,'Alur pengembangan dan evaluasi prototipe ARTHA',40,True,True)
x=550;w=850;cx=975
stages=[(120,'Penggalian kebutuhan dan studi literatur\n(3.3.1)'),(300,'Perencanaan dan prioritas tugas\n(3.3.2)'),(480,'Inisialisasi iterasi\n(3.3.3)'),(660,'Perancangan modul\n(3.3.4)'),(840,'Implementasi dan pengujian unit\nTes, kode, refaktorisasi (3.3.5)'),(1020,'Pengujian sistem\n(3.3.6)')]
for (y,l),(ny,_) in zip(stages,stages[1:]): f.line([(cx,y+120),(cx,ny)],True)
for y,l in stages: f.box(x,y,w,120,l,33)
f.line([(cx,1140),(cx,1210)],True)
f.decision(680,1210,590,180,'Uji sistem\nlulus?',33)
f.line([(1270,1300),(1510,1300),(1510,900),(1400,900)],True)
f.text(1455,1170,'Tidak:\nperbaiki galat',30,False,True)
f.line([(cx,1390),(cx,1470)],True);f.text(1035,1425,'Ya',30)
f.box(x,1470,w,120,'Evaluasi iterasi: waktu, galat, dan tindak lanjut\n(3.3.7)',33)
f.line([(cx,1590),(cx,1670)],True)
f.decision(650,1670,650,180,'Masih ada tugas\npada rencana?',32)
f.line([(650,1760),(300,1760),(300,540),(550,540)],True)
f.text(315,1680,'Ya: iterasi berikutnya',30)
f.line([(cx,1850),(cx,1930)],True);f.text(1035,1875,'Tidak',30)
f.box(x,1930,w,120,'UAT berbasis tugas bersama mitra\n(3.3.8)',33)
f.line([(cx,2050),(cx,2130)],True)
f.decision(650,2130,650,180,'Tugas penting\nditerima?',32)
f.line([(1300,2220),(1625,2220),(1625,2300)],True);f.text(1435,2170,'Tidak',30)
f.decision(1420,2300,410,200,'Kebutuhan\nberubah?',30)
f.line([(1830,2400),(2050,2400),(2050,180),(1400,180)],True)
f.text(1955,2255,'Ya:\nklarifikasi dan\nrencanakan ulang',29,False,True)
f.line([(1420,2400),(1450,2400),(1450,2670),(100,2670),(100,540),(550,540)],True)
f.text(440,2690,'Tidak: rencanakan perbaikan, uji ulang, lalu ulangi tugas UAT terkait',29)
f.line([(cx,2310),(cx,2440)],True);f.text(1035,2360,'Ya',30)
f.box(x,2440,w,130,'Dokumentasi, penyiapan, dan penyerahan luaran\nVersi prototipe serta bukti evaluasi dicatat',32)
f.line([(cx,2570),(cx,2790)],True)
f.box(760,2790,430,100,'Selesai',35,oval=True)
f.text(1100,2930,'Panah kembali menunjukkan pekerjaan yang harus diperiksa ulang sebelum proses dilanjutkan.',29,False,True)
names.append(f.save('Gambar_3_1_Alur_Pembuatan_Prototipe'))

# UML use-case associations only. Every ellipse is a user goal, not an internal check.
f=Figure(2200,2200)
f.rect(300,80,1600,2010,stroke='#222222')
f.text(1100,110,'Sistem Informasi Manajemen Operasional ARTHA',38,True,True)
def actor(ff,x,y,label):
    ff.d.ellipse((x-25,y,x+25,y+50),outline='#222222',width=3)
    ff.svg.append(f'<circle cx="{x}" cy="{y+25}" r="25" fill="white" stroke="#222222" stroke-width="3"/>')
    for pts in [[(x,y+50),(x,y+135)],[(x-50,y+85),(x+50,y+85)],[(x,y+135),(x-45,y+200)],[(x,y+135),(x+45,y+200)]]:ff.line(pts)
    ff.text(x,y+220,label,30,True,True)
actor(f,145,750,'Admin\nCabang');actor(f,2055,750,'Super\nAdmin')
shared=[('UC-00  Masuk dan keluar sistem',220),('UC-05  Kelola tarif dan tagihan',410),('UC-10  Catat dan periksa setoran kas',600),('UC-12  Dasbor dan laporan',790)]
for lab,y in shared:
    f.line([(145,835),(335,835),(335,y+60),(650,y+60)],width=2,color='#777777')
    f.line([(2055,835),(1865,835),(1865,y+60),(1550,y+60)],width=2,color='#777777')
for lab,y in shared: f.box(650,y,900,120,lab,32,oval=True,fill='white')
left=[('UC-01  Kelola siswa',1010),('UC-02  Kelola kelas dan ruang',1180),('UC-03  Kelola keanggotaan kelas',1350),('UC-04  Kelola jadwal',1520),('UC-06  Catat pembayaran tunai',1690),('UC-07  Ajukan bukti transfer',1860)]
right=[('UC-08  Periksa transfer',1010),('UC-11  Cocokkan penerimaan bank',1230),('UC-13  Kelola data induk dan akun',1450)]
for lab,y in left:
    f.line([(145,835),(340,835),(340,y+55),(430,y+55)],width=2,color='#777777')
for lab,y in right:
    f.line([(2055,835),(1860,835),(1860,y+55),(1770,y+55)],width=2,color='#777777')
f.line([(145,835),(345,835),(345,2025),(1200,2025),(1200,1745)],width=2,color='#777777')
f.line([(2055,835),(1950,835),(1950,1160),(1170,1160),(1170,1235),(1140,1235)],width=2,color='#777777')
for lab,y in left:f.box(430,y,710,110,lab,29,oval=True,fill='white')
for lab,y in right:f.box(1200,y,570,110,lab.replace('  ','\n',1),29,oval=True,fill='white')
f.box(1200,1690,570,110,'UC-09\nBuka tautan WhatsApp',29,oval=True,fill='white')
f.text(1100,2135,'Asosiasi menunjukkan keterlibatan; tindakan rinci dibatasi menurut peran pada skenario.',29,False,True)
names.append(f.save('Gambar_3_2_Use_Case_Inti'))

# Data model highlights allocation, immutable transaction branch, and the two bank sources.
f=Figure(2400,2100)
f.text(1200,35,'Model konseptual inti ARTHA',40,True,True)
def entity(x,y,w,h,title,body):
    f.rect(x,y,w,h)
    f.rect(x,y,w,55,fill='#eeeeee')
    f.text(x+w/2,y+12,title,29,True,True)
    f.text(x+18,y+76,body,26)
def edge(points,label,lx,ly):
    f.line(points,width=3);f.text(lx,ly,label,25)
f.rect(30,110,2340,730,stroke='#888888')
f.text(60,135,'A. Operasional dan nilai tagihan',32,True)
entity(70,240,420,200,'Cabang','PK id\nIdentitas cabang')
entity(680,240,450,200,'Siswa','PK id; FK branch_id\nKontak wali')
entity(1360,240,450,200,'Tagihan','PK id; FK student_id\nFK branch_id historis\nPeriode dan nilai tetap')
entity(1900,240,390,200,'Tarif','PK id; FK branch_id\nSesi, siklus, berlaku')
entity(70,570,420,200,'Kelas','PK id; FK branch_id\nKapasitas dan ambang')
entity(680,570,450,200,'Keanggotaan','PK id; FK student_id\nFK class_id; masuk/keluar')
entity(1360,570,450,200,'Jadwal','PK id; FK class_id\nFK mentor_id; FK room_id\nHari, waktu, masa berlaku')
entity(1900,570,390,200,'Tentor dan ruang','PK id pada tiap entitas\nRuang memiliki cabang\nTentor identitas global')
edge([(490,340),(680,340)],'1 : N',545,300)
edge([(1130,340),(1360,340)],'1 : N',1210,300)
edge([(1810,340),(1900,340)],'N : 1',1815,285)
edge([(280,440),(280,570)],'1 : N',310,485)
edge([(905,440),(905,570)],'1 : N',935,485)
edge([(490,670),(680,670)],'1 : N',545,630)
edge([(280,770),(280,805),(1585,805),(1585,770)],'Kelas 1 : N Jadwal',720,780)
edge([(1810,670),(1900,670)],'N : 1',1815,620)
f.rect(30,880,2340,1030,stroke='#888888')
f.text(60,905,'B. Penerimaan, pemeriksaan, dan pencocokan',32,True)
entity(70,1010,420,210,'Tagihan','PK id\nNilai dan cabang historis')
entity(680,1010,450,210,'Alokasi pembayaran','PK id; FK bill_id\nFK payment_id\nNominal per tagihan')
entity(1360,1010,450,210,'Pembayaran','PK id; FK student_id\nFK branch_id historis\nKanal, nominal, status')
entity(1900,1010,390,210,'Pemeriksaan','PK id; FK payment_id\nPemeriksa, keputusan\nWaktu dan alasan')
entity(70,1380,420,210,'Setoran kas','PK id; FK branch_id\nPenyerah, penerima\nTanggal setor ke bank')
entity(680,1380,450,210,'Rincian setoran','PK id; FK cash_batch_id\nFK payment_id unik\nHanya pembayaran tunai')
entity(1360,1380,450,210,'Pencocokan bank','PK id; FK bank_entry_id\nFK payment_id ATAU\nFK cash_batch_id')
entity(1900,1380,390,210,'Mutasi bank','PK id; FK bank_account_id\nTanggal, referensi\nNominal dana masuk')
edge([(490,1115),(680,1115)],'1 : N',545,1070)
edge([(1130,1115),(1360,1115)],'N : 1',1210,1070)
edge([(1810,1115),(1900,1115)],'1 : 0..1',1815,1060)
edge([(490,1485),(680,1485)],'1 : N',545,1440)
edge([(1130,1485),(1190,1485),(1190,1260),(1585,1260),(1585,1220)],'Rincian 0..1 : 1 pembayaran tunai',1170,1240)
edge([(1585,1220),(1585,1380)],'1 : 0..1',1610,1300)
edge([(1810,1485),(1900,1485)],'0..1 : 1',1815,1430)
edge([(280,1590),(280,1680),(1585,1680),(1585,1590)],'Setoran 1 : 0..1 pencocokan',750,1640)
f.text(80,1750,'Aturan XOR: satu pencocokan memakai transfer siswa atau setoran kas, bukan keduanya.',30,True)
f.text(80,1800,'Satu mutasi dipakai satu sumber dengan nominal cocok penuh pada lingkup prototipe.',29)
f.text(80,1845,'Penerimaan siswa dihitung satu kali; setoran dan pencocokan tidak menambah pendapatan.',29)
f.text(1200,1970,'Diagram menyoroti hubungan berisiko; seluruh 23 tabel serta kunci dijabarkan pada kamus data.',29,False,True)
f.text(1200,2020,'Relasi rekening, pengguna pemeriksa, mata pelajaran, dan jejak aktivitas dirinci pada ERD lengkap.',28,False,True)
names.append(f.save('Gambar_3_3_Model_Data_Konseptual'))

f=Figure(1800,1450)
f.text(900,35,'Arsitektur prototipe ARTHA',40,True,True)
boxes=[(420,140,960,150,'Admin Cabang dan Super Admin\nPeramban komputer atau telepon'),(420,390,960,150,'Antarmuka Next.js\nFormulir, daftar tugas, dan dasbor'),(420,640,960,150,'Layanan Laravel\nAutentikasi, otorisasi cabang, dan aturan bisnis'),(420,890,960,150,'MySQL dan penyimpanan berkas privat\nTransaksi, alokasi, pemeriksaan, serta bukti')]
for i in range(3):f.line([(900,boxes[i][1]+150),(900,boxes[i+1][1])],True)
for x,y,w,h,l in boxes:f.box(x,y,w,h,l,33)
f.box(70,1170,720,140,'WhatsApp melalui tautan\nAdmin memeriksa dan mengirim pesan',30)
f.box(1010,1170,720,140,'Mutasi rekening resmi\nDicatat dan dicocokkan petugas berwenang',30)
f.line([(420,465),(180,465),(180,1170)],True)
f.text(900,1090,'Dasbor menampilkan antrean transfer dari status pengajuan tersimpan.',29,False,True)
f.text(900,1365,'Pencocokan manual tanpa API bank; tidak memerlukan layanan pengiriman WhatsApp otomatis.',28,False,True)
names.append(f.save('Gambar_3_10_Arsitektur_Prototipe'))

# Shared grayscale wireframe components.
def ui(title,role='Admin Cabang',branch='Cabang Contoh A'):
    f=Figure(1800,1160,True)
    f.rect(0,0,1800,1160,fill='#fafafa',stroke='#fafafa',r=0)
    f.rect(0,0,1800,100,fill='#222222',stroke='#222222',r=0)
    f.text(40,29,'ARTHA',36,True,color='#ffffff')
    f.text(270,34,'RANCANGAN ANTARMUKA | DATA SIMULASI',25,color='#ffffff')
    f.text(1470,35,role,25,color='#ffffff')
    f.rect(0,100,270,1060,fill='#eeeeee',stroke='#dddddd',r=0)
    f.text(30,135,'Navigasi',28,True)
    for j,nav in enumerate(['Dasbor','Siswa','Kelas dan ruang','Jadwal','Tagihan','Pembayaran','Setoran','Laporan']):f.text(30,200+j*75,nav,26)
    f.text(315,135,title,38,True)
    f.text(315,195,branch+' | Data buatan untuk menjelaskan alur',25,color='#555555')
    f.line([(315,1080),(1755,1080)],color='#cccccc',width=2)
    f.text(315,1100,'Nilai pada gambar bukan tarif, kapasitas, atau transaksi aktual mitra.',24,color='#555555')
    return f
def button(f,x,y,w,label,disabled=False,primary=False):
    fill='#dddddd' if disabled else ('#333333' if primary else '#ffffff')
    f.rect(x,y,w,52,fill=fill,stroke='#777777')
    f.text(x+w/2,y+13,label,23,True,True,color='#777777' if disabled else ('#ffffff' if primary else '#222222'))
def panel(f,x,y,w,h,title):
    f.rect(x,y,w,h)
    f.text(x+22,y+20,title,28,True)
def kpi(f,x,y,w,label,value,desc):
    f.rect(x,y,w,155)
    f.text(x+20,y+18,label,24)
    f.text(x+20,y+57,value,36,True)
    f.text(x+20,y+112,desc,22,color='#555555')
def table(f,x,y,width,headers,rows,colwidths=None,rowh=70,font=24):
    colwidths=colwidths or [width/len(headers)]*len(headers)
    totalh=62+rowh*len(rows)
    f.rect(x,y,width,totalh,stroke='#b0b0b0',r=0)
    f.rect(x,y,width,62,fill='#eaeaea',stroke='#b0b0b0',r=0)
    xx=x
    for i,h in enumerate(headers):
        f.text(xx+12,y+20,h,font,True)
        if i:f.line([(xx,y),(xx,y+totalh)],color='#d0d0d0',width=1)
        xx+=colwidths[i]
    for ri,row in enumerate(rows):
        yy=y+62+ri*rowh
        if ri:f.line([(x,yy),(x+width,yy)],color='#d0d0d0',width=1)
        xx=x
        for i,item in enumerate(row):
            f.text(xx+12,yy+19,str(item),font)
            xx+=colwidths[i]
def field(f,x,y,w,label,value):
    f.text(x,y,label,24,True)
    f.rect(x,y+34,w,60,stroke='#b0b0b0')
    f.text(x+14,y+53,value,25)

f=ui('Dasbor cabang')
kpi(f,315,260,330,'Siswa aktif','48','Pada cabang penugasan')
kpi(f,680,260,330,'Kelas hampir penuh','2 kelas','Menurut parameter kelas')
kpi(f,1045,260,330,'Tagihan lewat tempo','6 tagihan','Masih memiliki sisa')
kpi(f,1410,260,345,'Transfer diajukan','3 pengajuan','Belum menjadi pelunasan')
panel(f,315,460,1440,310,'Tindak lanjut hari ini')
table(f,340,525,1390,['Prioritas','Objek','Keadaan','Tindakan'],[
    ['Pembayaran','Pengajuan TF-021','Menunggu pemeriksaan','Lihat pengajuan'],
    ['Kapasitas','Kelas Contoh B','8 / 10, hampir penuh','Lihat peserta'],
    ['Tunggakan','Siswa Contoh 03','Sisa Rp300.000','Buka daftar tagihan'],
],[220,400,400,370],rowh=58,font=24)
panel(f,315,810,1440,215,'Batas informasi dasbor')
f.text(340,870,'Data mengikuti cabang penugasan dan status transaksi tersimpan.',27)
f.text(340,920,'Tombol muat ulang digunakan untuk mengambil ringkasan terbaru.',27)
button(f,1480,950,245,'Muat ulang')
names.append(f.save('Gambar_3_4_Dasbor_Cabang'))

f=ui('Keanggotaan dan kapasitas kelas')
field(f,315,255,470,'Kelas terpilih','Kelas Contoh B')
field(f,825,255,425,'Kapasitas / aktif / sisa','10 / 8 / 2 tempat')
field(f,1290,255,465,'Ambang peringatan contoh','Sisa 2 tempat')
f.rect(315,380,1440,85,fill='#eeeeee',stroke='#888888')
f.text(340,405,'HAMPIR PENUH | Nilai ambang pada gambar merupakan contoh parameter.',27,True)
table(f,315,505,1440,['Siswa','Mulai keanggotaan','Status','Tindakan'],[
    ['Siswa Contoh 01','01 Oktober 2026','Aktif','Akhiri keanggotaan'],
    ['Siswa Contoh 02','01 Oktober 2026','Aktif','Akhiri keanggotaan'],
    ['Siswa Contoh 04','15 September 2026','Keluar','Lihat riwayat'],
],[410,370,230,430],rowh=70)
button(f,315,815,410,'Tambah siswa, tersedia 2 tempat',primary=True)
button(f,765,815,460,'Contoh kelas penuh: tambah ditolak',disabled=True)
panel(f,315,910,1440,130,'Perubahan keanggotaan')
f.text(340,965,'Siswa keluar: simpan tanggal dan alasan, pertahankan riwayat, lalu hitung ulang tempat.',26)
names.append(f.save('Gambar_3_5_Keanggotaan_Kelas'))

f=ui('Pengajuan bukti transfer')
field(f,315,255,690,'Siswa / cabang','Siswa Contoh 03 / Cabang Contoh A')
field(f,1045,255,710,'Rekening tujuan resmi','Rekening Simulasi 01')
table(f,315,385,1440,['Tagihan dipilih','Periode','Sisa tagihan','Alokasi transfer'],[
    ['SPP-EX-101','Oktober 2026','Rp300.000','Rp300.000'],
    ['SPP-EX-102','November 2026','Rp300.000','Rp300.000'],
],[430,340,330,340],rowh=66)
field(f,315,630,430,'Total pengajuan','Rp600.000')
field(f,785,630,440,'Tanggal transfer','25 Oktober 2026')
field(f,1265,630,490,'Bukti transfer','bukti_simulasi.pdf')
f.rect(315,765,1440,90,fill='#eeeeee',stroke='#888888')
f.text(340,791,'Setelah diajukan: MENUNGGU VERIFIKASI. Tagihan belum dinyatakan lunas.',27,True)
button(f,315,900,260,'Kembali')
button(f,1325,900,430,'Kirim pengajuan',primary=True)
f.text(315,995,'Pengajuan yang dikembalikan diperbaiki melalui pengajuan baru yang merujuk riwayat lama.',25)
names.append(f.save('Gambar_3_6_Pengajuan_Transfer'))

f=ui('Pemeriksaan transfer','Super Admin','Seluruh cabang sesuai kewenangan')
panel(f,315,255,680,420,'Pengajuan TF-021')
f.text(340,320,'Siswa Contoh 03 | Cabang Contoh A',27)
f.text(340,370,'Diajukan: 25 Oktober 2026',27)
f.text(340,420,'Jumlah alokasi: Rp600.000',29,True)
f.rect(340,480,630,155,fill='#f3f3f3',stroke='#aaaaaa')
f.text(655,525,'Pratinjau bukti simulasi\nBuka berkas privat',26,False,True)
panel(f,1035,255,720,420,'Rujukan dana masuk yang diperiksa')
field(f,1060,320,670,'Rekening resmi','Rekening Simulasi 01')
field(f,1060,440,670,'Mutasi / tanggal / nominal','MUT-EX-101 / 25-10-2026 / Rp600.000')
f.text(1060,580,'Belum dipakai pada pencocokan lain',26,True)
field(f,315,720,1440,'Alasan pengembalian, wajib jika dikembalikan','Contoh: bukti kurang terbaca, mohon unggah ulang.')
button(f,315,870,420,'Kembalikan dengan alasan')
button(f,1250,870,505,'Setujui dan cocokkan dana',primary=True)
f.text(315,970,'Persetujuan, alokasi, riwayat pemeriksaan, dan pencocokan disimpan satu kali.',26)
f.text(315,1010,'Kewenangan pemeriksa merupakan rancangan yang akan divalidasi bersama mitra.',25,color='#555555')
names.append(f.save('Gambar_3_7_Pemeriksaan_Transfer'))

f=ui('Tunggakan dan pesan WhatsApp')
table(f,315,255,1440,['Siswa','Periode','Jatuh tempo','Sisa','Tindakan'],[
    ['Siswa Contoh 03','Oktober 2026','20 Oktober 2026','Rp300.000','Siapkan pesan'],
    ['Siswa Contoh 05','Oktober 2026','21 Oktober 2026','Rp300.000','Siapkan pesan'],
],[330,290,320,240,260],rowh=66)
panel(f,315,515,1440,385,'Pratinjau pesan untuk Siswa Contoh 03')
f.text(340,580,'Penerima: nomor wali terdaftar, ditampilkan tersamar pada gambar ini.',27)
f.rect(340,640,1390,205,fill='#f7f7f7',stroke='#aaaaaa')
f.text(365,665,'Bapak/Ibu wali Siswa Contoh 03, tagihan SPP periode Oktober 2026',28)
f.text(365,715,'sebesar Rp300.000 telah jatuh tempo pada 20 Oktober 2026.',28)
f.text(365,765,'Mohon konfirmasi pembayaran kepada Admin Cabang. Terima kasih.',28)
button(f,315,940,520,'Buka WhatsApp dengan pesan ini',primary=True)
f.text(870,944,'Admin memeriksa dan mengirim di WhatsApp.',25)
f.text(315,1020,'Catatan sistem: tautan dibuka. Status pesan terkirim atau dibaca tidak diketahui sistem.',25)
names.append(f.save('Gambar_3_8_Tunggakan_WhatsApp'))

f=ui('Dasbor pusat dan pencocokan','Super Admin','Seluruh cabang sesuai kewenangan')
field(f,315,255,440,'Cabang','Semua cabang contoh')
field(f,795,255,440,'Periode penerimaan','Oktober 2026')
button(f,1330,290,425,'Terapkan penyaring')
kpi(f,315,390,330,'Penerimaan sah','Rp6.000.000','Tunai + transfer disetujui')
kpi(f,680,390,330,'Pengajuan tertunda','Rp600.000','Tidak masuk penerimaan')
kpi(f,1045,390,330,'Sisa tagihan','Rp900.000','Kewajiban siswa')
kpi(f,1410,390,345,'Sudah cocok bank','Rp4.800.000','Bukan pendapatan tambahan')
panel(f,315,590,1440,315,'Penelusuran sumber pencocokan')
table(f,340,655,1390,['Sumber','Referensi mutasi','Nominal cocok','Status'],[
    ['Transfer TF-020','MUT-EX-099','Rp600.000','Cocok penuh'],
    ['Setoran kas ST-004','MUT-EX-100','Rp4.200.000','Cocok penuh'],
],[420,380,310,280],rowh=70)
f.text(315,955,'Penerimaan belum cocok bank: Rp1.200.000, telusuri kanal dan posisi kasnya.',26)
f.text(315,1005,'Sisa tagihan berbeda dari penerimaan yang belum cocok bank; setoran tidak dihitung ulang.',25)
names.append(f.save('Gambar_3_9_Dasbor_Pusat_Pencocokan'))

# Contact sheet is an inspection aid, not another numbered chapter figure.
names.sort(key=lambda name:int(name.split('_')[2]))
thumbw,thumbh=600,580
montage=Image.new('RGB',(thumbw*2,thumbh*5),'#dddddd')
draw=ImageDraw.Draw(montage)
for i,name in enumerate(names):
    im=Image.open(OUT/(name+'.png')).convert('RGB')
    im.thumbnail((thumbw-30,thumbh-65))
    xx=(i%2)*thumbw+(thumbw-im.width)//2
    yy=(i//2)*thumbh+48
    montage.paste(im,(xx,yy))
    draw.text(((i%2)*thumbw+15,(i//2)*thumbh+12),name.replace('Gambar_','Gambar ').replace('_',' '),font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17),fill='black')
proof=ROOT/'DOKUMEN MD/REVISI_TERPADU_2026-10-25'
montage.save(proof/'KONTAK_GAMBAR_REVISI.png')
(proof/'DAFTAR_GAMBAR_REVISI.json').write_text(json.dumps({'date':'2026-10-25','scope':'Draft diagrams and UI wireframes; all UI values fictional, not implemented application screenshots','figures':names,'formats':['png','svg'],'source_script':str(Path(__file__).resolve())},ensure_ascii=False,indent=2),encoding='utf-8')
# Remove only this script's seven superseded figure names after successful replacement.
for superseded in ['Gambar_3_4_Arsitektur_Prototipe', 'Gambar_3_5_Dasbor_Cabang', 'Gambar_3_6_Keanggotaan_Kelas', 'Gambar_3_7_Pengajuan_Transfer', 'Gambar_3_8_Pemeriksaan_Transfer', 'Gambar_3_9_Tunggakan_WhatsApp', 'Gambar_3_10_Dasbor_Pusat_Pencocokan']:
    for ext in ['.png', '.svg']:
        old = (OUT / (superseded + ext)).resolve()
        assert old.parent == OUT.resolve(), old
        if old.exists():
            old.unlink()
print(json.dumps({'figures':len(names),'png':len(names),'svg':len(names),'backup_files':len(list(BACK.glob('*'))),'montage':str(proof/'KONTAK_GAMBAR_REVISI.png')},ensure_ascii=False))
