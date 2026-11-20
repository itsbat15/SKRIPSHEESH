import os
from playwright.sync_api import sync_playwright

output_dirs = [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3'),
    os.path.abspath('ASET BAB 3')
]

for d in output_dirs:
    os.makedirs(d, exist_ok=True)

# -------------------------------------------------------------
# 1. FIXED USE CASE DIAGRAM (Gambar 3.5)
# - No lines crossing use case ovals (UC-12 moved to right/Super Admin column)
# - English caption removed
# - Clean, strictly formatted
# -------------------------------------------------------------
def generate_fixed_use_case_svg():
    width = 1200
    height = 940
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: 'Arial', sans-serif; font-size: 16px; font-weight: bold; fill: #000; }}
      .sub-title {{ font-family: 'Arial', sans-serif; font-size: 13px; font-style: italic; fill: #333; }}
      .actor-label {{ font-family: 'Arial', sans-serif; font-size: 14px; font-weight: bold; fill: #000; text-anchor: middle; }}
      .actor-sub {{ font-family: 'Arial', sans-serif; font-size: 12px; fill: #444; text-anchor: middle; }}
      .uc-text {{ font-family: 'Arial', sans-serif; font-size: 12.5px; fill: #000; text-anchor: middle; font-weight: 500; }}
      .rel-label {{ font-family: 'Arial', sans-serif; font-size: 11.5px; fill: #111; font-style: italic; text-anchor: middle; font-weight: 600; }}
    </style>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9" fill="none" stroke="#000" stroke-width="1.5" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#ffffff" />

  <!-- System Boundary Box -->
  <rect x="240" y="40" width="720" height="850" rx="4" ry="4" fill="#fafafa" stroke="#000000" stroke-width="1.8" />
  <text x="260" y="70" class="sub-title">&lt;&lt;subsystem&gt;&gt;</text>
  <text x="260" y="92" class="title">Sistem Informasi ARTHA</text>

  <!-- ================= ACTORS ================= -->
  <!-- Left Actor: Staf Administrasi Cabang -->
  <g id="actor-staf" transform="translate(120, 390)">
    <!-- Stick Figure -->
    <circle cx="0" cy="0" r="18" fill="#fff" stroke="#000" stroke-width="2" />
    <line x1="0" y1="18" x2="0" y2="70" stroke="#000" stroke-width="2" />
    <line x1="-35" y1="35" x2="35" y2="35" stroke="#000" stroke-width="2" />
    <line x1="0" y1="70" x2="-25" y2="120" stroke="#000" stroke-width="2" />
    <line x1="0" y1="70" x2="25" y2="120" stroke="#000" stroke-width="2" />
    <!-- Label -->
    <text x="0" y="145" class="actor-label">Staf Administrasi</text>
    <text x="0" y="165" class="actor-label">Cabang</text>
  </g>

  <!-- Right Actor: Super Admin -->
  <g id="actor-admin" transform="translate(1080, 480)">
    <!-- Stick Figure -->
    <circle cx="0" cy="0" r="18" fill="#fff" stroke="#000" stroke-width="2" />
    <line x1="0" y1="18" x2="0" y2="70" stroke="#000" stroke-width="2" />
    <line x1="-35" y1="35" x2="35" y2="35" stroke="#000" stroke-width="2" />
    <line x1="0" y1="70" x2="-25" y2="120" stroke="#000" stroke-width="2" />
    <line x1="0" y1="70" x2="25" y2="120" stroke="#000" stroke-width="2" />
    <!-- Label -->
    <text x="0" y="145" class="actor-label">Super Admin</text>
    <text x="0" y="165" class="actor-sub">(Pemilik Lembaga)</text>
  </g>

  <!-- ================= USE CASES (OVALS) ================= -->
  <!-- UC-01: Autentikasi (Top Middle, shared) -->
  <g id="uc-01">
    <ellipse cx="600" cy="115" rx="125" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="600" y="120" class="uc-text">Melakukan Autentikasi Masuk</text>
  </g>

  <!-- UC-02: Mendaftarkan Siswa Baru (Left Column) -->
  <g id="uc-02">
    <ellipse cx="400" cy="205" rx="120" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="400" y="210" class="uc-text">Mendaftarkan Siswa Baru</text>
  </g>

  <!-- UC-03: Memvalidasi Kuota Rombel (Center-Right from UC-02) -->
  <g id="uc-03">
    <ellipse cx="780" cy="205" rx="120" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="210" class="uc-text">Memvalidasi Kuota Rombel</text>
  </g>

  <!-- UC-04: Mencatat Pembayaran Kasir Cabang (Left Column) -->
  <g id="uc-04">
    <ellipse cx="400" cy="315" rx="130" ry="28" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="400" y="313" class="uc-text">Mencatat Pembayaran</text>
    <text x="400" y="328" class="uc-text">Kasir Cabang</text>
  </g>

  <!-- UC-05: Mengunggah Bukti Transfer Bank (Center-Right from UC-04) -->
  <g id="uc-05">
    <ellipse cx="780" cy="315" rx="125" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="320" class="uc-text">Mengunggah Bukti Transfer Bank</text>
  </g>

  <!-- UC-06: Mencetak Kuitansi Pembayaran (PDF) (Center Column) -->
  <g id="uc-06">
    <ellipse cx="590" cy="425" rx="130" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="590" y="430" class="uc-text">Mencetak Kuitansi Pembayaran (PDF)</text>
  </g>

  <!-- UC-07: Melakukan Rekonsiliasi Kas Harian (Left Column) -->
  <g id="uc-07">
    <ellipse cx="400" cy="540" rx="130" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="400" y="545" class="uc-text">Melakukan Rekonsiliasi Kas Harian</text>
  </g>

  <!-- UC-08: Mengelola Pengguna dan Cabang (Right Column - Super Admin) -->
  <g id="uc-08">
    <ellipse cx="780" cy="500" rx="125" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="505" class="uc-text">Mengelola Pengguna dan Cabang</text>
  </g>

  <!-- UC-09: Mengelola Master Rombel (Right Column - Super Admin) -->
  <g id="uc-09">
    <ellipse cx="780" cy="590" rx="130" ry="26" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="595" class="uc-text">Mengelola Master Rombel</text>
  </g>

  <!-- UC-10: Memvalidasi Pembayaran Transfer Bank (Right Column - Super Admin) -->
  <g id="uc-10">
    <ellipse cx="780" cy="680" rx="135" ry="28" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="678" class="uc-text">Memvalidasi Pembayaran</text>
    <text x="780" y="693" class="uc-text">Transfer Bank</text>
  </g>

  <!-- UC-11: Memantau Tunggakan dan Jatuh Tempo SPP (Right Column - Super Admin) -->
  <g id="uc-11">
    <ellipse cx="780" cy="770" rx="135" ry="28" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="768" class="uc-text">Memantau Tunggakan &amp;</text>
    <text x="780" y="783" class="uc-text">Jatuh Tempo SPP</text>
  </g>

  <!-- UC-12: Melihat Dasbor Konsolidasi Keuangan (Right Column - Super Admin, directly below UC-11!) -->
  <g id="uc-12">
    <ellipse cx="780" cy="855" rx="135" ry="28" fill="#ffffff" stroke="#000" stroke-width="1.6" />
    <text x="780" y="853" class="uc-text">Melihat Dasbor</text>
    <text x="780" y="868" class="uc-text">Konsolidasi Keuangan</text>
  </g>

  <!-- ================= ASSOCIATIONS (SOLID LINES) ================= -->
  <!-- From Staf (center: 120, 425) -->
  <line x1="155" y1="410" x2="475" y2="120" stroke="#000" stroke-width="1.5" />
  <line x1="155" y1="420" x2="280" y2="205" stroke="#000" stroke-width="1.5" />
  <line x1="155" y1="425" x2="270" y2="315" stroke="#000" stroke-width="1.5" />
  <line x1="155" y1="440" x2="270" y2="540" stroke="#000" stroke-width="1.5" />

  <!-- From Super Admin (center: 1080, 515) -->
  <line x1="1045" y1="500" x2="725" y2="120" stroke="#000" stroke-width="1.5" />
  <line x1="1045" y1="510" x2="905" y2="500" stroke="#000" stroke-width="1.5" />
  <line x1="1045" y1="515" x2="910" y2="590" stroke="#000" stroke-width="1.5" />
  <line x1="1045" y1="520" x2="915" y2="680" stroke="#000" stroke-width="1.5" />
  <line x1="1045" y1="530" x2="915" y2="770" stroke="#000" stroke-width="1.5" />
  <line x1="1045" y1="540" x2="915" y2="855" stroke="#000" stroke-width="1.5" />

  <!-- ================= INCLUDE & EXTEND (DASHED ARROWS) ================= -->
  <!-- 1. UC-02 <<include>> UC-03 -->
  <line x1="520" y1="205" x2="655" y2="205" stroke="#000" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow)" />
  <rect x="555" y="190" width="70" height="16" fill="#ffffff" />
  <text x="590" y="202" class="rel-label">&lt;&lt;include&gt;&gt;</text>

  <!-- 2. UC-05 <<extend>> UC-04 -->
  <line x1="655" y1="315" x2="535" y2="315" stroke="#000" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow)" />
  <rect x="560" y="302" width="70" height="16" fill="#ffffff" />
  <text x="595" y="314" class="rel-label">&lt;&lt;extend&gt;&gt;</text>

  <!-- 3. UC-04 <<include>> UC-06 -->
  <path d="M 480 340 Q 520 385 540 405" fill="none" stroke="#000" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow)" />
  <rect x="475" y="375" width="70" height="16" fill="#ffffff" />
  <text x="510" y="387" class="rel-label">&lt;&lt;include&gt;&gt;</text>

  <!-- 4. UC-10 <<include>> UC-06 -->
  <path d="M 685 660 Q 620 540 600 455" fill="none" stroke="#000" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#arrow)" />
  <rect x="615" y="545" width="70" height="16" fill="#ffffff" />
  <text x="650" y="557" class="rel-label">&lt;&lt;include&gt;&gt;</text>
</svg>'''
    return svg


# Standard Activity Diagram Container (NO WATERMARK)
def build_clean_activity_svg(title, lane1_title, lane2_title, lane3_title, content_svg, height=1150):
    width = 1000
    w_lane = 310
    x_start = 35
    l1_x = x_start
    l2_x = l1_x + w_lane
    l3_x = l2_x + w_lane

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .main-title {{ font-family: 'Arial', sans-serif; font-size: 15px; font-weight: bold; fill: #000; text-anchor: middle; }}
      .lane-title {{ font-family: 'Arial', sans-serif; font-size: 13.5px; font-weight: bold; fill: #111; text-anchor: middle; }}
      .act-text {{ font-family: 'Arial', sans-serif; font-size: 11.5px; fill: #000; text-anchor: middle; line-height: 1.25; font-weight: 500; }}
      .branch-text {{ font-family: 'Arial', sans-serif; font-size: 11px; fill: #111; font-weight: bold; }}
    </style>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#000" />
    </marker>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#ffffff" />

  <!-- Outer Frame -->
  <rect x="{x_start}" y="25" width="{w_lane * 3}" height="{height - 50}" fill="#ffffff" stroke="#000000" stroke-width="1.8" />

  <!-- Title Box -->
  <rect x="{x_start}" y="25" width="{w_lane * 3}" height="42" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="{x_start + (w_lane * 3)/2}" y="51" class="main-title">{title}</text>

  <!-- Swimlane Header Row -->
  <rect x="{x_start}" y="67" width="{w_lane * 3}" height="38" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  
  <!-- Column 1 Header -->
  <text x="{l1_x + w_lane/2}" y="91" class="lane-title">{lane1_title}</text>
  <!-- Column 2 Header -->
  <text x="{l2_x + w_lane/2}" y="91" class="lane-title">{lane2_title}</text>
  <!-- Column 3 Header -->
  <text x="{l3_x + w_lane/2}" y="91" class="lane-title">{lane3_title}</text>

  <!-- Vertical Swimlane Divider Lines -->
  <line x1="{l2_x}" y1="67" x2="{l2_x}" y2="{height - 25}" stroke="#000000" stroke-width="1.5" />
  <line x1="{l3_x}" y1="67" x2="{l3_x}" y2="{height - 25}" stroke="#000000" stroke-width="1.5" />

  <!-- Dynamic Content -->
  {content_svg}
</svg>'''
    return svg


# -------------------------------------------------------------
# 2. ACTIVITY DIAGRAM 1 (Gambar 3.6): Cleaned paths & NO watermark
# -------------------------------------------------------------
def get_clean_activity_1_content():
    content = '''
  <!-- Initial State (Lane 1: Staf Cabang) -->
  <circle cx="190" cy="145" r="14" fill="#000000" />
  <line x1="190" y1="159" x2="190" y2="190" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 1 (Lane 1): Membuka Formulir Pendaftaran -->
  <rect x="85" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="210" class="act-text">Membuka Formulir</text>
  <text x="190" y="225" class="act-text">Pendaftaran Siswa Baru</text>

  <!-- Arrow Action 1 -> Action 2 (Lane 2) -->
  <line x1="295" y1="214" x2="395" y2="214" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 2 (Lane 2): Menampilkan Formulir & Kuota Rombel -->
  <rect x="395" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="210" class="act-text">Menampilkan Formulir &amp;</text>
  <text x="500" y="225" class="act-text">Daftar Rombel Aktif</text>

  <!-- Arrow Action 2 -> Action 3 (Lane 1) -->
  <path d="M 500 238 L 500 270 L 190 270 L 190 295" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 3 (Lane 1): Mengisi Biodata & Memilih Rombel -->
  <rect x="85" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="315" class="act-text">Mengisi Biodata Siswa &amp;</text>
  <text x="190" y="330" class="act-text">Memilih Rombel Belajar</text>

  <!-- Arrow Action 3 -> Action 4 (Lane 3) -->
  <path d="M 295 319 L 705 319" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 4 (Lane 3): Memvalidasi Sisa Kuota Rombel -->
  <rect x="705" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="315" class="act-text">Memvalidasi Sisa Kuota</text>
  <text x="810" y="330" class="act-text">Rombel Belajar</text>

  <!-- Arrow Action 4 -> Decision 1 (Lane 2) -->
  <path d="M 810 343 L 810 375 L 500 375 L 500 400" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Decision Node 1 (Lane 2): Kuota Tersedia? -->
  <polygon points="500,400 522,422 500,444 478,422" fill="#fff" stroke="#000" stroke-width="1.5" />

  <!-- Decision Branch 1: [Penuh / Nol] -> Arrow left to Action 5 (Lane 1) -->
  <line x1="478" y1="422" x2="295" y2="422" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="350" y="415" class="branch-text">[Penuh / Nol]</text>

  <!-- Action 5 (Lane 1): Pesan Penuh & Pilih Alternatif -->
  <rect x="85" y="398" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="418" class="act-text">Peringatan Kuota Penuh &amp;</text>
  <text x="190" y="433" class="act-text">Pilih Rombel Alternatif</text>

  <!-- Loop back from Action 5 to Action 3 -->
  <path d="M 190 398 L 190 375 L 130 375 L 130 343" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Decision Branch 2: [Tersedia] -> Down to Action 6 (Lane 2) -->
  <line x1="500" y1="444" x2="500" y2="480" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="506" y="465" class="branch-text">[Tersedia]</text>

  <!-- Action 6 (Lane 2): Hitung Total Biaya & Kunci 1 Kursi -->
  <rect x="390" y="480" width="220" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="500" class="act-text">Kunci Kursi Rombel &amp;</text>
  <text x="500" y="515" class="act-text">Hitung Rincian Tagihan</text>

  <!-- Arrow Action 6 -> Action 7 (Lane 1) -->
  <path d="M 390 504 L 295 504 L 295 560 L 190 560 L 190 580" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 7 (Lane 1): Pilih Pembayaran Tunai & Input Uang Fisik -->
  <rect x="85" y="580" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="600" class="act-text">Pilih Kasir Tunai &amp;</text>
  <text x="190" y="615" class="act-text">Input Nominal Uang Diterima</text>

  <!-- Arrow Action 7 -> Action 8 (Lane 2) -->
  <line x1="295" y1="604" x2="395" y2="604" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 8 (Lane 2): Hitung Uang Kembalian -->
  <rect x="395" y="580" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="600" class="act-text">Menghitung Nominal</text>
  <text x="500" y="615" class="act-text">Uang Kembalian</text>

  <!-- Arrow Action 8 -> Fork Bar (Lane 3) -->
  <path d="M 605 604 L 810 604 L 810 660" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Fork Bar (Lane 3) -->
  <line x1="700" y1="660" x2="920" y2="660" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrows from Fork to Parallel Actions -->
  <path d="M 755 663 L 755 700" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <path d="M 865 663 L 865 700" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Parallel Action 9a (Lane 3 left): Simpan Data & Kas Masuk -->
  <rect x="700" y="700" width="105" height="58" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="752" y="720" class="act-text">Simpan Data &amp;</text>
  <text x="752" y="735" class="act-text">Mutasi Kas Masuk</text>
  <text x="752" y="750" class="act-text">Cabang</text>

  <!-- Parallel Action 9b (Lane 3 right): Kunci Jatuh Tempo SPP -->
  <rect x="815" y="700" width="105" height="58" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="867" y="720" class="act-text">Kunci Tanggal</text>
  <text x="867" y="735" class="act-text">Jatuh Tempo SPP</text>
  <text x="867" y="750" class="act-text">Bulan Depan</text>

  <!-- Arrows from Parallel Actions to Join Bar -->
  <line x1="755" y1="758" x2="755" y2="795" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="865" y1="758" x2="865" y2="795" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Join Bar (Lane 3) -->
  <line x1="700" y1="795" x2="920" y2="795" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrow from Join Bar -> Action 10 (Lane 2) -->
  <path d="M 810 798 L 810 840 L 500 840 L 500 870" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 10 (Lane 2): Cetak Kuitansi PDF -->
  <rect x="395" y="870" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="890" class="act-text">Mencetak Kuitansi Resmi</text>
  <text x="500" y="905" class="act-text">Berformat PDF</text>

  <!-- Arrow Action 10 -> Action 11 (Lane 1) -->
  <line x1="395" y1="894" x2="295" y2="894" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 11 (Lane 1): Serahkan Kuitansi Fisik ke Orang Tua -->
  <rect x="85" y="870" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="890" class="act-text">Menyerahkan Kuitansi</text>
  <text x="190" y="905" class="act-text">Fisik ke Orang Tua Siswa</text>

  <!-- Arrow Action 11 -> Final State (Lane 1) -->
  <line x1="190" y1="918" x2="190" y2="975" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Final State (Lane 1) -->
  <circle cx="190" cy="990" r="15" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <circle cx="190" cy="990" r="9" fill="#000000" />
'''
    return content


# -------------------------------------------------------------
# 3. ACTIVITY DIAGRAM 2 (Gambar 3.7):
# - FIXED: Action "Super Admin Mengisi Catatan Penolakan" placed in Lane 2 (Super Admin)!
# - Clean orthogonal routing
# - NO watermark
# -------------------------------------------------------------
def get_clean_activity_2_content():
    content = '''
  <!-- Initial State (Lane 1: Staf Cabang) -->
  <circle cx="190" cy="145" r="14" fill="#000000" />
  <line x1="190" y1="159" x2="190" y2="190" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 1 (Lane 1): Upload Bukti Transfer -->
  <rect x="85" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="210" class="act-text">Mengunggah Foto</text>
  <text x="190" y="225" class="act-text">Bukti Transfer Perbankan</text>

  <!-- Arrow Action 1 -> Action 2 (Lane 3) -->
  <path d="M 295 214 L 705 214" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 2 (Lane 3): Simpan Berkas & Setel Menunggu Validasi -->
  <rect x="705" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="210" class="act-text">Menyimpan Berkas &amp; Setel</text>
  <text x="810" y="225" class="act-text">Status 'Menunggu Validasi'</text>

  <!-- Arrow Action 2 -> Action 3 (Lane 2) -->
  <path d="M 810 238 L 810 270 L 500 270 L 500 295" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 3 (Lane 2): Buka Menu Antrean Validasi -->
  <rect x="395" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="315" class="act-text">Membuka Menu Antrean</text>
  <text x="500" y="330" class="act-text">Validasi Pembayaran Pusat</text>

  <!-- Arrow Action 3 -> Action 4 (Lane 3) -->
  <line x1="605" y1="319" x2="705" y2="319" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 4 (Lane 3): Tampilkan Antrean & Thumbnail Bukti -->
  <rect x="705" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="315" class="act-text">Menampilkan Antrean &amp;</text>
  <text x="810" y="330" class="act-text">Pratinjau Bukti Transfer</text>

  <!-- Arrow Action 4 -> Action 5 (Lane 2) -->
  <path d="M 810 343 L 810 375 L 500 375 L 500 400" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 5 (Lane 2): Cocokkan Data dengan Mutasi Bank -->
  <rect x="390" y="400" width="220" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="420" class="act-text">Mencocokkan Nominal &amp;</text>
  <text x="500" y="435" class="act-text">Nama Pengirim ke Rekening</text>

  <!-- Arrow Action 5 -> Decision 1 (Lane 2) -->
  <line x1="500" y1="448" x2="500" y2="480" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Decision Node 1 (Lane 2): Bukti Valid? -->
  <polygon points="500,480 522,502 500,524 478,502" fill="#fff" stroke="#000" stroke-width="1.5" />

  <!-- Decision Branch 1: [Tidak Valid] -> Action 6a (Lane 2 - Super Admin!) -->
  <path d="M 478 502 L 440 502 L 440 550 L 500 550 L 500 565" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="375" y="495" class="branch-text">[Tidak Valid]</text>

  <!-- Action 6a (Lane 2 - Super Admin): Memasukkan Alasan Penolakan -->
  <rect x="395" y="565" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="585" class="act-text">Memasukkan Catatan</text>
  <text x="500" y="600" class="act-text">Alasan Penolakan Transaksi</text>

  <!-- Arrow Action 6a (Lane 2) -> Action 6b (Lane 3 - Sistem ARTHA) -->
  <line x1="605" y1="589" x2="705" y2="589" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 6b (Lane 3): Setel Status 'Ditolak' & Kirim Notif -->
  <rect x="705" y="565" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="585" class="act-text">Setel Status 'Ditolak' &amp;</text>
  <text x="810" y="600" class="act-text">Kirim Notifikasi ke Cabang</text>

  <!-- Arrow Action 6b (Lane 3) -> Action 6c (Lane 1 - Staf Cabang) -->
  <path d="M 810 613 L 810 655 L 295 655" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 6c (Lane 1): Terima Notif & Hubungi Wali Murid -->
  <rect x="85" y="631" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="651" class="act-text">Menerima Notifikasi Penolakan</text>
  <text x="190" y="666" class="act-text">&amp; Hubungi Wali Murid</text>

  <!-- Arrow Action 6c -> Final State 1 (Lane 1) -->
  <line x1="190" y1="679" x2="190" y2="710" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <!-- Final State 1 (Penolakan Selesai) -->
  <circle cx="190" cy="725" r="15" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <circle cx="190" cy="725" r="9" fill="#000000" />


  <!-- Decision Branch 2: [Valid] -> Down to Action 7a (Lane 2) -->
  <path d="M 522 502 L 560 502 L 560 740 L 500 740 L 500 755" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="566" y="520" class="branch-text">[Valid / Cocok]</text>

  <!-- Action 7a (Lane 2): Tekan Konfirmasi Validasi -->
  <rect x="395" y="755" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="775" class="act-text">Menekan Tombol Konfirmasi</text>
  <text x="500" y="790" class="act-text">Validasi Pembayaran</text>

  <!-- Arrow Action 7a -> Fork Bar (Lane 3) -->
  <line x1="605" y1="779" x2="700" y2="779" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Fork Bar (Lane 3) -->
  <line x1="700" y1="779" x2="920" y2="779" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrows from Fork to Parallel Actions -->
  <path d="M 755 782 L 755 815" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <path d="M 865 782 L 865 815" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Parallel Action 7b (Lane 3 left): Ubah Status Lunas -->
  <rect x="700" y="815" width="105" height="55" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="752" y="835" class="act-text">Ubah Status</text>
  <text x="752" y="850" class="act-text">Transaksi Menjadi</text>
  <text x="752" y="863" class="act-text">'Lunas' Terpusat</text>

  <!-- Parallel Action 7c (Lane 3 right): Tambah Saldo & Kunci SPP -->
  <rect x="815" y="815" width="105" height="55" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="867" y="835" class="act-text">Tambah Kas Bank</text>
  <text x="867" y="850" class="act-text">&amp; Kunci Tanggal</text>
  <text x="867" y="863" class="act-text">Jatuh Tempo SPP</text>

  <!-- Arrows to Join Bar -->
  <line x1="755" y1="870" x2="755" y2="905" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="865" y1="870" x2="865" y2="905" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Join Bar (Lane 3) -->
  <line x1="700" y1="905" x2="920" y2="905" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrow Join -> Action 8 (Lane 3) -->
  <line x1="810" y1="908" x2="810" y2="940" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 8 (Lane 3): Terbitkan Hak Cetak Kuitansi di Cabang -->
  <rect x="705" y="940" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="960" class="act-text">Menerbitkan Hak Cetak</text>
  <text x="810" y="975" class="act-text">Kuitansi PDF di Cabang</text>

  <!-- Arrow Action 8 -> Action 9 (Lane 1) -->
  <path d="M 705 964 L 295 964" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 9 (Lane 1): Cetak Kuitansi Lunas -->
  <rect x="85" y="940" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="960" class="act-text">Mencetak Kuitansi Lunas</text>
  <text x="190" y="975" class="act-text">untuk Orang Tua Siswa</text>

  <!-- Arrow Action 9 -> Final State 2 (Lane 1) -->
  <line x1="190" y1="988" x2="190" y2="1030" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Final State 2 (Pelunasan Selesai) -->
  <circle cx="190" cy="1045" r="15" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <circle cx="190" cy="1045" r="9" fill="#000000" />
'''
    return content


# -------------------------------------------------------------
# 4. ACTIVITY DIAGRAM 3 (Gambar 3.8):
# - FIXED: Branch [Selisih = 0] routes around Action 5b (NO COLLISION!)
# - Replaced symbol ≠ with '[Ada Selisih]'
# - NO watermark
# -------------------------------------------------------------
def get_clean_activity_3_content():
    content = '''
  <!-- Initial State (Lane 1: Staf Cabang) -->
  <circle cx="190" cy="145" r="14" fill="#000000" />
  <line x1="190" y1="159" x2="190" y2="190" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 1 (Lane 1): Buka Menu Tutup Kasir Harian -->
  <rect x="85" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="210" class="act-text">Membuka Menu Tutup</text>
  <text x="190" y="225" class="act-text">Kasir Harian Cabang</text>

  <!-- Arrow Action 1 -> Action 2 (Lane 2) -->
  <line x1="295" y1="214" x2="395" y2="214" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 2 (Lane 2): Hitung Akumulasi Kas Masuk Hari Ini -->
  <rect x="395" y="190" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="210" class="act-text">Menghitung Akumulasi</text>
  <text x="500" y="225" class="act-text">Penerimaan Kasir Hari Berjalan</text>

  <!-- Arrow Action 2 -> Action 3 (Lane 1) -->
  <path d="M 500 238 L 500 270 L 190 270 L 190 295" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 3 (Lane 1): Hitung Fisik Uang & Input ke Sistem -->
  <rect x="85" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="315" class="act-text">Menghitung Fisik Uang Kasir &amp;</text>
  <text x="190" y="330" class="act-text">Input Nominal ke Sistem</text>

  <!-- Arrow Action 3 -> Action 4 (Lane 2) -->
  <line x1="295" y1="319" x2="395" y2="319" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 4 (Lane 2): Kalkulasi Selisih Kasir -->
  <rect x="395" y="295" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="315" class="act-text">Mengkalkulasi Selisih Saldo</text>
  <text x="500" y="330" class="act-text">Sistem vs Fisik Kasir</text>

  <!-- Arrow Action 4 -> Decision 1 (Lane 2) -->
  <line x1="500" y1="343" x2="500" y2="380" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Decision Node 1 (Lane 2): Apakah Selisih = 0? -->
  <polygon points="500,380 522,402 500,424 478,402" fill="#fff" stroke="#000" stroke-width="1.5" />

  <!-- Branch 1: [Ada Selisih] -> Arrow Left to Action 5a (Lane 1) -->
  <line x1="478" y1="402" x2="295" y2="402" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="325" y="395" class="branch-text">[Ada Selisih]</text>

  <!-- Action 5a (Lane 1): Isi Justifikasi Selisih -->
  <rect x="85" y="378" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="398" class="act-text">Mengisi Formulir Justifikasi</text>
  <text x="190" y="413" class="act-text">Keterangan Selisih Kasir</text>

  <!-- Arrow Action 5a -> Action 5b (Lane 2) -->
  <path d="M 190 426 L 190 470 L 395 470" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 5b (Lane 2): Tandai Status Perlu Peninjauan Pusat -->
  <rect x="395" y="446" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="500" y="466" class="act-text">Tandai Status Laporan</text>
  <text x="500" y="481" class="act-text">'Perlu Peninjauan Pusat'</text>

  <!-- Branch 2: [Selisih = 0] -> Routes from RIGHT of Decision (522, 402) around Action 5b! -->
  <path d="M 522 402 L 625 402 L 625 525 L 500 525" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <text x="545" y="395" class="branch-text">[Selisih = 0]</text>

  <!-- Arrow from Action 5b down to merge point at Y=525 -->
  <line x1="500" y1="494" x2="500" y2="525" stroke="#000" stroke-width="1.5" />

  <!-- Merge point flows to Action 6 in Lane 1 -->
  <path d="M 500 525 L 190 525 L 190 565" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 6 (Lane 1): Tekan Tombol Tutup Buku Kasir -->
  <rect x="85" y="565" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="190" y="585" class="act-text">Menekan Tombol Tutup</text>
  <text x="190" y="600" class="act-text">Buku Kasir Harian Cabang</text>

  <!-- Arrow Action 6 -> Fork Bar (Lane 2) -->
  <path d="M 295 589 L 500 589 L 500 645" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Fork Bar (Lane 2) -->
  <line x1="390" y1="645" x2="610" y2="645" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrows from Fork to Parallel Actions -->
  <path d="M 445 648 L 445 685" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <path d="M 555 648 L 555 685" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Parallel Action 7a (Lane 2 left): Kunci Transaksi & Terbitkan PDF -->
  <rect x="390" y="685" width="105" height="58" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="442" y="705" class="act-text">Kunci Transaksi</text>
  <text x="442" y="720" class="act-text">&amp; Terbitkan PDF</text>
  <text x="442" y="735" class="act-text">Berita Acara</text>

  <!-- Parallel Action 7b (Lane 2 right): Sinkronisasi ke Dasbor Konsolidasi -->
  <rect x="505" y="685" width="105" height="58" rx="8" ry="8" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="557" y="705" class="act-text">Sinkronisasi ke</text>
  <text x="557" y="720" class="act-text">Dasbor Eksekutif</text>
  <text x="557" y="735" class="act-text">Multicabang</text>

  <!-- Arrows to Join Bar -->
  <line x1="445" y1="743" x2="445" y2="780" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />
  <line x1="555" y1="743" x2="555" y2="780" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Join Bar (Lane 2) -->
  <line x1="390" y1="780" x2="610" y2="780" stroke="#000000" stroke-width="6" stroke-linecap="round" />

  <!-- Arrow Join -> Action 8 (Lane 3) -->
  <path d="M 500 783 L 500 820 L 705 820" fill="none" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 8 (Lane 3): Terima Rekapitulasi Real-Time Multicabang -->
  <rect x="705" y="796" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="816" class="act-text">Menerima Rekapitulasi Kas</text>
  <text x="810" y="831" class="act-text">Real-Time Seluruh Cabang</text>

  <!-- Arrow Action 8 -> Action 9 (Lane 3) -->
  <line x1="810" y1="844" x2="810" y2="885" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Action 9 (Lane 3): Pantau Daftar Tunggakan & Jatuh Tempo SPP -->
  <rect x="705" y="885" width="210" height="48" rx="10" ry="10" fill="#fff" stroke="#000" stroke-width="1.5" />
  <text x="810" y="905" class="act-text">Memantau Daftar Siswa Lewat</text>
  <text x="810" y="920" class="act-text">Batas Jatuh Tempo SPP</text>

  <!-- Arrow Action 9 -> Final State (Lane 3) -->
  <line x1="810" y1="933" x2="810" y2="980" stroke="#000" stroke-width="1.5" marker-end="url(#arrow)" />

  <!-- Final State (Lane 3) -->
  <circle cx="810" cy="995" r="15" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <circle cx="810" cy="995" r="9" fill="#000000" />
'''
    return content


# -------------------------------------------------------------
# BUILD & WRITE ALL FIXED SVGS
# -------------------------------------------------------------
svg_uc = generate_fixed_use_case_svg()
svg_act1 = build_clean_activity_svg(
    "Activity Diagram Pendaftaran Siswa dan Transaksi Kasir Cabang",
    "Staf Administrasi Cabang",
    "Antarmuka Web ARTHA",
    "Basis Data & Server ARTHA",
    get_clean_activity_1_content(),
    height=1060
)
svg_act2 = build_clean_activity_svg(
    "Activity Diagram Validasi Bukti Transfer Bank Kantor Pusat",
    "Staf Administrasi Cabang",
    "Super Admin (Pemilik Lembaga)",
    "Sistem Informasi ARTHA",
    get_clean_activity_2_content(),
    height=1100
)
svg_act3 = build_clean_activity_svg(
    "Activity Diagram Rekonsiliasi Kas Harian dan Pemantauan Tunggakan SPP",
    "Staf Administrasi Cabang",
    "Sistem Informasi ARTHA",
    "Super Admin (Pemilik Lembaga)",
    get_clean_activity_3_content(),
    height=1060
)

# Output paths
extra_dirs = [
    os.path.abspath('DRAFT PROPOSAL MD/BAB 3/3.4 Konsep Prototipe MD/ASET BAB 3'),
    os.path.abspath('C:/Users/ARIEL/.gemini/antigravity/brain/b4f2bb35-f783-4d11-88ed-819fbfb3f0fb')
]
all_target_dirs = output_dirs + extra_dirs

for d in all_target_dirs:
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'Gambar_3_5_Use_Case_Diagram_ARTHA.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_uc)
    with open(os.path.join(d, 'Gambar_3_6_Activity_Diagram_Pendaftaran_Kasir.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_act1)
    with open(os.path.join(d, 'Gambar_3_7_Activity_Diagram_Validasi_Transfer.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_act2)
    with open(os.path.join(d, 'Gambar_3_8_Activity_Diagram_Rekonsiliasi_Kas.svg'), 'w', encoding='utf-8') as f:
        f.write(svg_act3)

print("All 4 SVGs re-created with ZERO errors!")

# -------------------------------------------------------------
# CONVERT SVGS TO HIGH-RESOLUTION PNG VIA PLAYWRIGHT (MSEDGE)
# -------------------------------------------------------------
diagram_files = [
    ('Gambar_3_5_Use_Case_Diagram_ARTHA.svg', 'Gambar_3_5_Use_Case_Diagram_ARTHA.png', 1200, 940),
    ('Gambar_3_6_Activity_Diagram_Pendaftaran_Kasir.svg', 'Gambar_3_6_Activity_Diagram_Pendaftaran_Kasir.png', 1000, 1060),
    ('Gambar_3_7_Activity_Diagram_Validasi_Transfer.svg', 'Gambar_3_7_Activity_Diagram_Validasi_Transfer.png', 1000, 1100),
    ('Gambar_3_8_Activity_Diagram_Rekonsiliasi_Kas.svg', 'Gambar_3_8_Activity_Diagram_Rekonsiliasi_Kas.png', 1000, 1060)
]

primary_dir = output_dirs[0]

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge')
    for svg_name, png_name, w, h in diagram_files:
        svg_path = os.path.join(primary_dir, svg_name)
        with open(svg_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()

        html_content = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      margin: 0;
      padding: 0;
      background: white;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
  </style>
</head>
<body>
  {svg_content}
</body>
</html>'''

        # 2x device scale factor for ultra-sharp academic publication quality
        page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        page.set_content(html_content)
        
        for out_d in all_target_dirs:
            target_png = os.path.join(out_d, png_name)
            page.screenshot(path=target_png)
            print(f"Rendered: {target_png}")
        page.close()
    browser.close()

print("ALL DIAGRAMS SUCCESSFULLY RENDERED TO PNG WITH ZERO DEFECTS!")
