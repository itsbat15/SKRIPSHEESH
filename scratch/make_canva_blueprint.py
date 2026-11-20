import fitz  # PyMuPDF
import os

width = 2050
height = 1080

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .main-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 26px; font-weight: 800; fill: #0F172A; text-anchor: middle; }}
      .main-subtitle {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13.5px; fill: #475569; text-anchor: middle; }}
      .col-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13.5px; font-weight: 800; fill: #FFFFFF; text-anchor: middle; letter-spacing: 0.5px; }}
      .col-sub {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #E0F2FE; text-anchor: middle; }}
      .badge-txt {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; font-weight: 700; text-anchor: middle; }}
      .card-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #0F172A; }}
      .card-desc {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; fill: #64748B; }}
      .arrow-lbl {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 9.5px; font-weight: 700; text-anchor: middle; }}
      .arrow-sub {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 8px; fill: #64748B; text-anchor: middle; }}
    </style>

    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.06" />
    </filter>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08" />
    </filter>

    <!-- Arrow Markers -->
    <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#0078D4" />
    </marker>
    <marker id="arr-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#D97706" />
    </marker>
    <marker id="arr-indigo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#4F46E5" />
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#7C3AED" />
    </marker>
    <marker id="arr-slate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#64748B" />
    </marker>
  </defs>

  <!-- Clean Canvas Background -->
  <rect width="100%" height="100%" fill="#F8FAFC" />

  <!-- Title Header -->
  <text x="{width//2}" y="44" class="main-title">CETAK BIRU ARSITEKTUR SISTEM INFORMASI OPERASIONAL MULTICABANG ARTHA</text>
  <text x="{width//2}" y="70" class="main-subtitle">Format Microsoft Azure N-Tier Architecture (5 Kolom Horizontal dengan Pemetaan Panah Logis Presisi)</text>
'''

# Layout measurements
start_x = 55
start_y = 100
col_w = 280
col_gap = 135
col_h = 920

cols = [
    {
        'num': '1', 'name': 'LAPISAN PENGGUNA', 'en': 'User Tier', 'color': '#0078D4', 'bg': '#F0F9FF', 'border': '#BAE6FD',
        'badge': 'Akses & Titik Masuk',
        'cards': [
            {'title': 'Super Admin (Pusat)', 'icon': 'shield', 'desc': 'Pimpinan Lembaga & Kas Pusat', 'y': 240, 'h': 140},
            {'title': 'Staf Administrasi', 'icon': 'branch', 'desc': 'Petugas Kasir 8 Kantor Cabang', 'y': 580, 'h': 140}
        ]
    },
    {
        'num': '2', 'name': 'LAPISAN ANTARMUKA', 'en': 'Presentation Tier', 'color': '#0284C7', 'bg': '#F8FAFC', 'border': '#CBD5E1',
        'badge': 'Next.js 14 & Tailwind CSS',
        'cards': [
            {'title': 'Next.js App Router', 'icon': 'globe', 'desc': 'Navigasi & Server-Side Rendering', 'y': 190, 'h': 92},
            {'title': 'Responsive Multi-Device UI', 'icon': 'layout', 'desc': 'Tata Letak Tailwind CSS', 'y': 335, 'h': 92},
            {'title': 'Client State Management', 'icon': 'sliders', 'desc': 'Validasi & Reaktivitas Form', 'y': 480, 'h': 92},
            {'title': 'Route Guards & Middleware', 'icon': 'lock', 'desc': 'Proteksi Halaman Berbasis Role', 'y': 625, 'h': 92}
        ]
    },
    {
        'num': '3', 'name': 'GERBANG KOMUNIKASI', 'en': 'API Gateway Tier', 'color': '#D97706', 'bg': '#FFFBEB', 'border': '#FDE68A',
        'badge': 'RESTful API & Security',
        'cards': [
            {'title': 'RESTful API Endpoints', 'icon': 'network', 'desc': 'Format Pertukaran JSON Terenkripsi', 'y': 230, 'h': 125},
            {'title': 'Laravel Sanctum Auth', 'icon': 'key', 'desc': 'Validasi Bearer Token Sesi', 'y': 420, 'h': 125},
            {'title': 'HTTP Standard Methods', 'icon': 'arrows', 'desc': 'Protokol GET | POST | PUT | DELETE', 'y': 610, 'h': 125}
        ]
    },
    {
        'num': '4', 'name': 'LOGIKA BISNIS', 'en': 'Business Logic Tier', 'color': '#4F46E5', 'bg': '#EEF2FF', 'border': '#C7D2FE',
        'badge': 'Laravel 11 Backend MVC',
        'cards': [
            {'title': 'RBAC & Filter Cabang', 'icon': 'filter', 'desc': 'Validasi Hak Akses & branch_id', 'y': 175, 'h': 82},
            {'title': 'Master Data Cabang', 'icon': 'building', 'desc': 'Profil & Alokasi 8 Cabang', 'y': 300, 'h': 82},
            {'title': 'Pendaftaran Siswa', 'icon': 'userplus', 'desc': 'Data Siswa & Rombel Belajar', 'y': 425, 'h': 82},
            {'title': 'Jatuh Tempo SPP', 'icon': 'clock', 'desc': 'Kunci Tanggal & Pengingat Tagihan', 'y': 550, 'h': 82},
            {'title': 'Kasir & Invoicing', 'icon': 'cash', 'desc': 'Transaksi Tunai, Transfer & QRIS', 'y': 675, 'h': 82},
            {'title': 'Rekonsiliasi Kas Multicabang', 'icon': 'chart', 'desc': 'Laporan Terpusat Real-Time', 'y': 800, 'h': 82}
        ]
    },
    {
        'num': '5', 'name': 'PENYIMPANAN DATA', 'en': 'Data Storage Tier', 'color': '#7C3AED', 'bg': '#FAF5FF', 'border': '#DDD6FE',
        'badge': 'MySQL & File System',
        'cards': [
            {'title': 'Basis Data Relasional MySQL', 'icon': 'database', 'desc': 'Tabel users, students, payments, etc.', 'y': 260, 'h': 220},
            {'title': 'Penyimpanan Berkas Digital', 'icon': 'folder', 'desc': 'Kuitansi PDF & Bukti Transfer Bank', 'y': 590, 'h': 220}
        ]
    }
]

def render_icon(icon_name, x, y, col):
    if icon_name == 'shield':
        return f'<g transform="translate({x},{y})"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 8v5M12 16h.01" stroke="{col}" stroke-width="2" stroke-linecap="round"/></g>'
    elif icon_name == 'branch':
        return f'<g transform="translate({x},{y})"><rect x="2" y="4" width="20" height="16" rx="2" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M6 8h12M6 12h8M6 16h4" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'globe':
        return f'<g transform="translate({x},{y})"><circle cx="12" cy="12" r="9" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M3 12h18M12 3c3 4 3 14 0 18M12 3c-3 4-3 14 0 18" stroke="{col}" stroke-width="1.5" stroke-linecap="round"/></g>'
    elif icon_name == 'layout':
        return f'<g transform="translate({x},{y})"><rect x="3" y="3" width="18" height="18" rx="2" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M3 9h18M9 21V9" stroke="{col}" stroke-width="1.8"/></g>'
    elif icon_name == 'sliders':
        return f'<g transform="translate({x},{y})"><path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'lock':
        return f'<g transform="translate({x},{y})"><rect x="4" y="10" width="16" height="11" rx="2" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M8 10V7a4 4 0 0 1 8 0v3" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'network':
        return f'<g transform="translate({x},{y})"><circle cx="6" cy="6" r="3" fill="{col}"/><circle cx="18" cy="6" r="3" fill="{col}"/><circle cx="12" cy="18" r="3" fill="{col}"/><path d="M8.5 7.5l4 7M15.5 7.5l-4 7M9 6h6" stroke="{col}" stroke-width="1.8"/></g>'
    elif icon_name == 'key':
        return f'<g transform="translate({x},{y})"><circle cx="8" cy="15" r="5" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M12 11l8-8M17 3l3 3M14 6l2 2" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'arrows':
        return f'<g transform="translate({x},{y})"><path d="M7 16V4M7 4L3 8M7 4l4 4M17 8v12M17 20l4-4M17 20l-4-4" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g>'
    elif icon_name == 'filter':
        return f'<g transform="translate({x},{y})"><path d="M4 4h16l-6 7v6l-4 3v-9L4 4z" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g>'
    elif icon_name == 'building':
        return f'<g transform="translate({x},{y})"><rect x="4" y="3" width="16" height="18" rx="1" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2M10 21v-3h4v3" stroke="{col}" stroke-width="1.6"/></g>'
    elif icon_name == 'userplus':
        return f'<g transform="translate({x},{y})"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/><circle cx="9" cy="7" r="4" stroke="{col}" stroke-width="1.8"/><path d="M19 8v6M16 11h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'clock':
        return f'<g transform="translate({x},{y})"><circle cx="12" cy="12" r="9" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M12 7v5l3 3" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_name == 'cash':
        return f'<g transform="translate({x},{y})"><rect x="2" y="5" width="20" height="14" rx="2" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><circle cx="12" cy="12" r="3" stroke="{col}" stroke-width="1.8"/><path d="M6 9h.01M18 15h.01" stroke="{col}" stroke-width="2"/></g>'
    elif icon_name == 'chart':
        return f'<g transform="translate({x},{y})"><path d="M3 21h18M5 17v-4M9 17v-8M13 17v-5M17 17v-10" stroke="{col}" stroke-width="2" stroke-linecap="round"/></g>'
    elif icon_name == 'database':
        return f'<g transform="translate({x},{y})"><ellipse cx="12" cy="5" rx="9" ry="3" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6" stroke="{col}" stroke-width="1.8"/></g>'
    elif icon_name == 'folder':
        return f'<g transform="translate({x},{y})"><path d="M4 4h5l2 3h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="{col}" opacity="0.15" stroke="{col}" stroke-width="1.8"/><path d="M8 13h8M8 17h5" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/></g>'
    return ''

# Render Columns
for i, col in enumerate(cols):
    cx = start_x + i * (col_w + col_gap)
    # Container box
    svg += f'''
    <rect x="{cx}" y="{start_y}" width="{col_w}" height="{col_h}" rx="12" fill="{col["bg"]}" stroke="{col["border"]}" stroke-width="1.5" filter="url(#shadow)" />
    
    <!-- Header -->
    <path d="M {cx} {start_y+12} Q {cx} {start_y} {cx+12} {start_y} L {cx+col_w-12} {start_y} Q {cx+col_w} {start_y} {cx+col_w} {start_y+12} L {cx+col_w} {start_y+54} L {cx} {start_y+54} Z" fill="{col["color"]}" />
    <text x="{cx+col_w//2}" y="{start_y+25}" class="col-title">TIER {col["num"]}: {col["name"]}</text>
    <text x="{cx+col_w//2}" y="{start_y+43}" class="col-sub">{col["en"]}</text>

    <!-- Sub-badge -->
    <rect x="{cx+15}" y="{start_y+66}" width="{col_w-30}" height="24" rx="6" fill="#FFFFFF" stroke="{col["border"]}" stroke-width="1" />
    <text x="{cx+col_w//2}" y="{start_y+82}" class="badge-txt" fill="{col["color"]}">{col["badge"]}</text>
    '''

    for card in col['cards']:
        card_x = cx + 15
        card_w = col_w - 30
        card_y = card['y']
        card_h = card['h']
        svg += f'''
        <g filter="url(#card-shadow)">
          <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1" />
          <rect x="{card_x}" y="{card_y}" width="5" height="{card_h}" rx="2" fill="{col["color"]}" />
          {render_icon(card["icon"], card_x + 14, card_y + (card_h//2 - 12), col["color"])}
          <text x="{card_x + 46}" y="{card_y + card_h//2 - 4}" class="card-title">{card["title"]}</text>
          <text x="{card_x + 46}" y="{card_y + card_h//2 + 13}" class="card-desc">{card["desc"]}</text>
        </g>
        '''

# ==================== 100% PRECISE LOGICAL ARROWS (SPACED OUT) ====================

def draw_pill_label(mx, my, lbl_top, lbl_sub, color):
    return f'''
    <rect x="{mx-44}" y="{my-14}" width="88" height="27" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.9" opacity="0.98" filter="url(#card-shadow)" />
    <text x="{mx}" y="{my-1}" class="arrow-lbl" fill="{color}">{lbl_top}</text>
    <text x="{mx}" y="{my+10}" class="arrow-sub">{lbl_sub}</text>
    '''

# 1. TIER 1 -> TIER 2
c1_r = start_x + col_w - 15
c2_l = start_x + col_w + col_gap + 15
gap12_mid = (c1_r + c2_l) // 2

# Super Admin -> Next.js App Router (Forward)
svg += f'<path d="M {c1_r} 280 L {c2_l} 235" stroke="#0078D4" stroke-width="1.8" marker-end="url(#arr-blue)" />'
svg += draw_pill_label(gap12_mid, 240, 'Akses Dasbor', 'HTTPS Request', '#0078D4')

# App Router -> Super Admin (Return)
svg += f'<path d="M {c2_l} 255 L {c1_r} 340" stroke="#64748B" stroke-width="1.8" marker-end="url(#arr-slate)" />'
svg += draw_pill_label(gap12_mid, 315, 'Render UI', 'HTML / State', '#64748B')

# Staf Cabang -> Responsive UI (Forward)
svg += f'<path d="M {c1_r} 620 L {c2_l} 385" stroke="#0078D4" stroke-width="1.8" marker-end="url(#arr-blue)" />'
svg += draw_pill_label(gap12_mid, 520, 'Input Kasir', 'Pendaftaran Siswa', '#0078D4')

# Responsive UI -> Staf Cabang (Return: Kuitansi PDF)
svg += f'<path d="M {c2_l} 415 L {c1_r} 670" stroke="#64748B" stroke-width="1.8" marker-end="url(#arr-slate)" />'
svg += draw_pill_label(gap12_mid, 620, 'Cetak Kuitansi', 'PDF Stream', '#64748B')


# 2. TIER 2 -> TIER 3
c2_r = start_x + col_w + col_gap + col_w - 15
c3_l = start_x + 2 * (col_w + col_gap) + 15
gap23_mid = (c2_r + c3_l) // 2

# App Router & State -> RESTful API Endpoints (Forward)
svg += f'<path d="M {c2_r} 245 L {c3_l} 275" stroke="#D97706" stroke-width="1.8" marker-end="url(#arr-amber)" />'
svg += draw_pill_label(gap23_mid, 245, 'REST Calls', 'Payload JSON', '#D97706')

# RESTful API -> State Management (Return)
svg += f'<path d="M {c3_l} 310 L {c2_r} 515" stroke="#64748B" stroke-width="1.8" marker-end="url(#arr-slate)" />'
svg += draw_pill_label(gap23_mid, 400, 'JSON Response', 'Status 200 OK', '#64748B')

# Route Guards -> Sanctum Auth (Forward: Bearer Token)
svg += f'<path d="M {c2_r} 670 L {c3_l} 485" stroke="#D97706" stroke-width="1.8" marker-end="url(#arr-amber)" />'
svg += draw_pill_label(gap23_mid, 590, 'Token Bearer', 'Header Auth', '#D97706')


# 3. TIER 3 -> TIER 4
c3_r = start_x + 2 * (col_w + col_gap) + col_w - 15
c4_l = start_x + 3 * (col_w + col_gap) + 15
gap34_mid = (c3_r + c4_l) // 2

# Sanctum Auth -> RBAC & Branch Filter
svg += f'''
<path d="M {c3_r} 460 C {c3_r+40} 460, {c4_l-40} 215, {c4_l} 215" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arr-indigo)" />
'''
svg += draw_pill_label(gap34_mid, 250, 'Validasi Role', 'RBAC &amp; branch_id', '#4F46E5')

# RESTful API -> Operasional (Master Cabang & Pendaftaran)
svg += f'''
<path d="M {c3_r} 280 C {c3_r+40} 280, {c4_l-40} 340, {c4_l} 340" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arr-indigo)" />
<path d="M {c3_r} 280 C {c3_r+40} 280, {c4_l-40} 465, {c4_l} 465" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arr-indigo)" />
'''
svg += draw_pill_label(gap34_mid, 360, 'Modul Siswa', 'Daftar &amp; Rombel', '#4F46E5')

# HTTP Methods -> Finansial (Kasir & Rekonsiliasi)
svg += f'''
<path d="M {c3_r} 670 C {c3_r+40} 670, {c4_l-40} 715, {c4_l} 715" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arr-indigo)" />
<path d="M {c3_r} 670 C {c3_r+40} 670, {c4_l-40} 840, {c4_l} 840" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arr-indigo)" />
'''
svg += draw_pill_label(gap34_mid, 760, 'Transaksi Kas', 'Invoicing &amp; Rekap', '#4F46E5')

# Return from Business Logic to API Gateway
svg += f'''
<path d="M {c4_l} 590 C {c4_l-40} 590, {c3_r+40} 330, {c3_r} 330" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arr-slate)" />
'''
svg += draw_pill_label(gap34_mid, 480, 'Data Return', 'Objek Transaksi', '#64748B')


# 4. TIER 4 -> TIER 5
c4_r = start_x + 3 * (col_w + col_gap) + col_w - 15
c5_l = start_x + 4 * (col_w + col_gap) + 15
gap45_mid = (c4_r + c5_l) // 2

# SQL Write (All Data Modules -> MySQL)
svg += f'''
<path d="M {c4_r} 340 C {c4_r+40} 340, {c5_l-40} 330, {c5_l} 330" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)" />
<path d="M {c4_r} 465 C {c4_r+40} 465, {c5_l-40} 355, {c5_l} 355" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)" />
<path d="M {c4_r} 715 C {c4_r+40} 715, {c5_l-40} 395, {c5_l} 395" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)" />
'''
svg += draw_pill_label(gap45_mid, 340, 'Query SQL', 'INSERT / UPDATE', '#7C3AED')

# SQL Result Sets (MySQL -> Business Logic)
svg += f'''
<path d="M {c5_l} 435 C {c5_l-40} 435, {c4_r+40} 590, {c4_r} 590" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arr-slate)" />
'''
svg += draw_pill_label(gap45_mid, 490, 'Result Sets', 'Eloquent Models', '#64748B')

# File Upload (Kasir & Pendaftaran -> File Storage)
svg += f'''
<path d="M {c4_r} 735 C {c4_r+40} 735, {c5_l-40} 660, {c5_l} 660" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arr-purple)" />
'''
svg += draw_pill_label(gap45_mid, 675, 'Upload Bukti', 'Simpan Gambar', '#7C3AED')

# File Fetch (File Storage -> Kasir / Stream)
svg += f'''
<path d="M {c5_l} 730 C {c5_l-40} 730, {c4_r+40} 840, {c4_r} 840" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arr-slate)" />
'''
svg += draw_pill_label(gap45_mid, 785, 'Unduh PDF', 'Kuitansi Stream', '#64748B')

svg += '</svg>'

dest_dir = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb'
svg_path = os.path.join(dest_dir, 'cetak_biru_arsitektur_canva.svg')
png_path = os.path.join(dest_dir, 'cetak_biru_arsitektur_canva.png')

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg)
print('SVG generated successfully:', os.path.getsize(svg_path))

# Render to 200 DPI PNG
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=200)
pix.save(png_path)
print('PNG rendered successfully:', os.path.getsize(png_path))
