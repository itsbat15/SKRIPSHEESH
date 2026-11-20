import fitz  # PyMuPDF
import os

width = 1780
height = 920

# Setup SVG
svg_parts = []
svg_parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 23px; font-weight: 700; fill: #0F172A; text-anchor: middle; }}
      .subtitle {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #64748B; text-anchor: middle; }}
      .col-header {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: 700; fill: #FFFFFF; text-anchor: middle; letter-spacing: 0.5px; }}
      .col-sub {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #E2E8F0; text-anchor: middle; }}
      .card-title {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #1E293B; }}
      .card-desc {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; fill: #64748B; }}
      .arrow-lbl {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 9.5px; font-weight: 700; text-anchor: middle; }}
      .arrow-sub {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 8.5px; fill: #64748B; text-anchor: middle; }}
      .badge-txt {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; font-weight: 700; text-anchor: middle; }}
    </style>

    <!-- Filters -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0F172A" flood-opacity="0.06" />
    </filter>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.07" />
    </filter>

    <!-- Markers -->
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#2563EB" />
    </marker>
    <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#D97706" />
    </marker>
    <marker id="arrow-indigo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#4F46E5" />
    </marker>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#7C3AED" />
    </marker>
    <marker id="arrow-slate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#64748B" />
    </marker>
  </defs>

  <!-- Clean Background -->
  <rect width="100%" height="100%" fill="#F8FAFC" />
''')

# Header text
svg_parts.append(f'''
  <text x="{width//2}" y="42" class="title">KONSEP ARSITEKTUR SISTEM INFORMASI OPERASIONAL MULTICABANG ARTHA</text>
  <text x="{width//2}" y="65" class="subtitle">Arsitektur Berlapis Berorientasi Layanan (5-Tier Architecture Model) dengan Alur Permintaan &amp; Respons Terarah</text>
''')

col_w = 264
col_gap = 76
start_x = 52
start_y = 95
col_h = 790

cols = [
    {
        'num': '1', 'name': 'LAPISAN PENGGUNA', 'en': 'User Tier', 'color': '#0F766E', 'bg': '#F0FDFA', 'border': '#99F6E4',
        'badge': 'Aktor & Titik Akses',
        'cards': [
            {'title': 'Super Admin', 'icon': 'shield', 'desc': 'Pusat (Pimpinan & Keuangan)', 'y': 220, 'h': 130},
            {'title': 'Staf Administrasi', 'icon': 'branch', 'desc': 'Cabang (Pelayanan & Kasir)', 'y': 510, 'h': 130}
        ]
    },
    {
        'num': '2', 'name': 'LAPISAN ANTARMUKA', 'en': 'Presentation Tier', 'color': '#1D4ED8', 'bg': '#EFF6FF', 'border': '#BFDBFE',
        'badge': 'Next.js 14 & Tailwind CSS',
        'cards': [
            {'title': 'Next.js App Router', 'icon': 'globe', 'desc': 'Server-Side Rendering (SSR)', 'y': 175, 'h': 85},
            {'title': 'Responsive Multi-Device UI', 'icon': 'layout', 'desc': 'Tailwind CSS Modern Styling', 'y': 310, 'h': 85},
            {'title': 'Client State Management', 'icon': 'sliders', 'desc': 'Validasi & Reaktivitas Form', 'y': 445, 'h': 85},
            {'title': 'Route Guards & Middleware', 'icon': 'lock', 'desc': 'Proteksi Halaman Berbasis Role', 'y': 580, 'h': 85}
        ]
    },
    {
        'num': '3', 'name': 'GERBANG KOMUNIKASI', 'en': 'API Gateway Tier', 'color': '#B45309', 'bg': '#FFFBEB', 'border': '#FDE68A',
        'badge': 'RESTful API & Security',
        'cards': [
            {'title': 'RESTful API Endpoints', 'icon': 'network', 'desc': 'Format Pertukaran JSON', 'y': 210, 'h': 115},
            {'title': 'Laravel Sanctum Auth', 'icon': 'key', 'desc': 'Bearer Token Authentication', 'y': 380, 'h': 115},
            {'title': 'HTTP Standard Methods', 'icon': 'arrows', 'desc': 'GET | POST | PUT | DELETE', 'y': 550, 'h': 115}
        ]
    },
    {
        'num': '4', 'name': 'LOGIKA BISNIS', 'en': 'Business Logic Tier', 'color': '#4338CA', 'bg': '#EEF2FF', 'border': '#C7D2FE',
        'badge': 'Laravel 11 Backend MVC',
        'cards': [
            {'title': 'RBAC & Filter Cabang', 'icon': 'filter', 'desc': 'Validasi Hak Akses & branch_id', 'y': 165, 'h': 75},
            {'title': 'Master Data Cabang', 'icon': 'building', 'desc': 'Manajemen 8 Kantor Cabang', 'y': 275, 'h': 75},
            {'title': 'Pendaftaran Siswa', 'icon': 'userplus', 'desc': 'Formulir Siswa & Rombel Belajar', 'y': 385, 'h': 75},
            {'title': 'Jatuh Tempo SPP', 'icon': 'clock', 'desc': 'Kunci Tanggal & Pengingat Tagihan', 'y': 495, 'h': 75},
            {'title': 'Kasir & Invoicing', 'icon': 'cash', 'desc': 'Kasir Tunai, Transfer & QRIS', 'y': 605, 'h': 75},
            {'title': 'Rekonsiliasi Kas Cabang', 'icon': 'chart', 'desc': 'Laporan Terpusat Real-Time', 'y': 715, 'h': 75}
        ]
    },
    {
        'num': '5', 'name': 'PENYIMPANAN DATA', 'en': 'Data Storage Tier', 'color': '#6D28D9', 'bg': '#FAF5FF', 'border': '#DDD6FE',
        'badge': 'MySQL & File Storage',
        'cards': [
            {'title': 'Basis Data MySQL', 'icon': 'database', 'desc': 'Tabel users, students, payments, etc.', 'y': 240, 'h': 190},
            {'title': 'Penyimpanan Berkas Digital', 'icon': 'folder', 'desc': 'Kuitansi PDF & Bukti Bayar', 'y': 520, 'h': 190}
        ]
    }
]

def get_icon(icon_type, x, y, color):
    if icon_type == 'shield':
        return f'<g transform="translate({x},{y})"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="{color}" opacity="0.15"/><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 8v5M12 16h.01" stroke="{color}" stroke-width="2" stroke-linecap="round"/></g>'
    elif icon_type == 'branch':
        return f'<g transform="translate({x},{y})"><rect x="2" y="4" width="20" height="16" rx="2" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M6 8h12M6 12h8M6 16h4" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'globe':
        return f'<g transform="translate({x},{y})"><circle cx="12" cy="12" r="9" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M3 12h18M12 3c3 4 3 14 0 18M12 3c-3 4-3 14 0 18" stroke="{color}" stroke-width="1.5" stroke-linecap="round"/></g>'
    elif icon_type == 'layout':
        return f'<g transform="translate({x},{y})"><rect x="3" y="3" width="18" height="18" rx="2" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M3 9h18M9 21V9" stroke="{color}" stroke-width="1.8"/></g>'
    elif icon_type == 'sliders':
        return f'<g transform="translate({x},{y})"><path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'lock':
        return f'<g transform="translate({x},{y})"><rect x="4" y="10" width="16" height="11" rx="2" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M8 10V7a4 4 0 0 1 8 0v3" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'network':
        return f'<g transform="translate({x},{y})"><circle cx="6" cy="6" r="3" fill="{color}"/><circle cx="18" cy="6" r="3" fill="{color}"/><circle cx="12" cy="18" r="3" fill="{color}"/><path d="M8.5 7.5l4 7M15.5 7.5l-4 7M9 6h6" stroke="{color}" stroke-width="1.8"/></g>'
    elif icon_type == 'key':
        return f'<g transform="translate({x},{y})"><circle cx="8" cy="15" r="5" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M12 11l8-8M17 3l3 3M14 6l2 2" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'arrows':
        return f'<g transform="translate({x},{y})"><path d="M7 16V4M7 4L3 8M7 4l4 4M17 8v12M17 20l4-4M17 20l-4-4" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g>'
    elif icon_type == 'filter':
        return f'<g transform="translate({x},{y})"><path d="M4 4h16l-6 7v6l-4 3v-9L4 4z" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></g>'
    elif icon_type == 'building':
        return f'<g transform="translate({x},{y})"><rect x="4" y="3" width="16" height="18" rx="1" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M8 7h2M14 7h2M8 11h2M14 11h2M8 15h2M14 15h2M10 21v-3h4v3" stroke="{color}" stroke-width="1.6"/></g>'
    elif icon_type == 'userplus':
        return f'<g transform="translate({x},{y})"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/><circle cx="9" cy="7" r="4" stroke="{color}" stroke-width="1.8"/><path d="M19 8v6M16 11h6" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'clock':
        return f'<g transform="translate({x},{y})"><circle cx="12" cy="12" r="9" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M12 7v5l3 3" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    elif icon_type == 'cash':
        return f'<g transform="translate({x},{y})"><rect x="2" y="5" width="20" height="14" rx="2" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><circle cx="12" cy="12" r="3" stroke="{color}" stroke-width="1.8"/><path d="M6 9h.01M18 15h.01" stroke="{color}" stroke-width="2"/></g>'
    elif icon_type == 'chart':
        return f'<g transform="translate({x},{y})"><path d="M3 21h18M5 17v-4M9 17v-8M13 17v-5M17 17v-10" stroke="{color}" stroke-width="2" stroke-linecap="round"/></g>'
    elif icon_type == 'database':
        return f'<g transform="translate({x},{y})"><ellipse cx="12" cy="5" rx="9" ry="3" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6" stroke="{color}" stroke-width="1.8"/></g>'
    elif icon_type == 'folder':
        return f'<g transform="translate({x},{y})"><path d="M4 4h5l2 3h9a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="{color}" opacity="0.15" stroke="{color}" stroke-width="1.8"/><path d="M8 13h8M8 17h5" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/></g>'
    return ''

# Draw Columns and Cards
for i, col in enumerate(cols):
    cx = start_x + i * (col_w + col_gap)
    # Column Outer Container (Microsoft style)
    svg_parts.append(f'''
    <!-- Column {col["num"]}: {col["name"]} -->
    <rect x="{cx}" y="{start_y}" width="{col_w}" height="{col_h}" rx="12" fill="{col["bg"]}" stroke="{col["border"]}" stroke-width="1.5" filter="url(#shadow)" />
    
    <!-- Column Header -->
    <path d="M {cx} {start_y+12} Q {cx} {start_y} {cx+12} {start_y} L {cx+col_w-12} {start_y} Q {cx+col_w} {start_y} {cx+col_w} {start_y+12} L {cx+col_w} {start_y+54} L {cx} {start_y+54} Z" fill="{col["color"]}" />
    <text x="{cx+col_w//2}" y="{start_y+24}" class="col-header">TIER {col["num"]}: {col["name"]}</text>
    <text x="{cx+col_w//2}" y="{start_y+42}" class="col-sub">{col["en"]}</text>

    <!-- Sub-badge -->
    <rect x="{cx+15}" y="{start_y+66}" width="{col_w-30}" height="24" rx="6" fill="#FFFFFF" stroke="{col["border"]}" stroke-width="1" />
    <text x="{cx+col_w//2}" y="{start_y+82}" class="badge-txt" fill="{col["color"]}">{col["badge"]}</text>
    ''')

    # Cards inside column
    for card in col['cards']:
        card_x = cx + 15
        card_w = col_w - 30
        card_y = card['y']
        card_h = card['h']

        svg_parts.append(f'''
        <g filter="url(#card-shadow)">
          <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1" />
          <rect x="{card_x}" y="{card_y}" width="5" height="{card_h}" rx="2" fill="{col["color"]}" />
          {get_icon(card["icon"], card_x + 14, card_y + (card_h//2 - 12), col["color"])}
          <text x="{card_x + 46}" y="{card_y + card_h//2 - 4}" class="card-title">{card["title"]}</text>
          <text x="{card_x + 46}" y="{card_y + card_h//2 + 13}" class="card-desc">{card["desc"]}</text>
        </g>
        ''')

# ==================== SPECIFIC BIDIRECTIONAL & BRANCHING ARROWS ====================

def draw_arrow(x1, y1, x2, y2, color, marker, label_top='', label_sub=''):
    res = f'<path d="M {x1} {y1} L {x2} {y2}" stroke="{color}" stroke-width="1.8" marker-end="url(#{marker})" />'
    if label_top:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2
        res += f'''
        <rect x="{mx-34}" y="{my-13}" width="68" height="24" rx="4" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="0.8" opacity="0.96" />
        <text x="{mx}" y="{my-1}" class="arrow-lbl" fill="{color}">{label_top}</text>
        <text x="{mx}" y="{my+9}" class="arrow-sub">{label_sub}</text>
        '''
    return res

# 1. BETWEEN TIER 1 & TIER 2
# Forward: Super Admin -> App Router
c1_r = start_x + col_w - 15
c2_l = start_x + col_w + col_gap + 15
svg_parts.append(draw_arrow(c1_r, 260, c2_l, 215, '#2563EB', 'arrow-blue', 'HTTPS Req', 'Action / View'))
# Return: Responsive UI -> Super Admin
svg_parts.append(draw_arrow(c2_l, 290, c1_r, 310, '#64748B', 'arrow-slate', 'Rendered', 'HTML / State'))

# Forward: Staf Cabang -> State Manager
svg_parts.append(draw_arrow(c1_r, 550, c2_l, 490, '#2563EB', 'arrow-blue', 'Input Form', 'Kasir / Daftar'))
# Return: Route Guard -> Staf Cabang
svg_parts.append(draw_arrow(c2_l, 620, c1_r, 600, '#64748B', 'arrow-slate', 'UI Feedback', 'Kuitansi PDF'))


# 2. BETWEEN TIER 2 & TIER 3
c2_r = start_x + 2*col_w + col_gap - 15
c3_l = start_x + 2*col_w + 2*col_gap - col_w + 15  # wait, start_x + 2*(col_w+col_gap) + 15
c3_l = start_x + 2*(col_w + col_gap) + 15

# Upper: Next.js -> REST API
svg_parts.append(draw_arrow(c2_r, 215, c3_l, 255, '#D97706', 'arrow-amber', 'REST Call', 'JSON Payload'))
# Middle: Guards -> Sanctum Auth
svg_parts.append(draw_arrow(c2_r, 620, c3_l, 440, '#D97706', 'arrow-amber', 'Auth Header', 'Bearer Token'))
# Return: REST API -> State Manager
svg_parts.append(draw_arrow(c3_l, 290, c2_r, 475, '#64748B', 'arrow-slate', 'JSON Resp', 'Status 200 OK'))


# 3. BETWEEN TIER 3 & TIER 4 (BRANCHING ROUTING)
c3_r = start_x + 3*col_w + 2*col_gap - col_w - 15 # wait: cx for col 3 is start_x + 2*(col_w+col_gap)
c3_r = start_x + 2*(col_w + col_gap) + col_w - 15
c4_l = start_x + 3*(col_w + col_gap) + 15

# Branch 1: Sanctum Auth -> RBAC & Branch Filter
svg_parts.append(f'''
<path d="M {c3_r} 420 C {c3_r+25} 420, {c4_l-25} 202, {c4_l} 202" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arrow-indigo)" />
<rect x="{(c3_r+c4_l)//2 - 32}" y="295" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="0.8" />
<text x="{(c3_r+c4_l)//2}" y="306" class="arrow-lbl" fill="#4F46E5">RBAC Check</text>
<text x="{(c3_r+c4_l)//2}" y="315" class="arrow-sub">branch_id</text>
''')

# Branch 2: REST Endpoints -> Operasional (Master Data & Pendaftaran)
svg_parts.append(f'''
<path d="M {c3_r} 265 C {c3_r+25} 265, {c4_l-25} 312, {c4_l} 312" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arrow-indigo)" />
<path d="M {c3_r} 265 C {c3_r+25} 265, {c4_l-25} 422, {c4_l} 422" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arrow-indigo)" />
<rect x="{(c3_r+c4_l)//2 - 32}" y="348" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="0.8" />
<text x="{(c3_r+c4_l)//2}" y="359" class="arrow-lbl" fill="#4F46E5">Route Dispatch</text>
<text x="{(c3_r+c4_l)//2}" y="368" class="arrow-sub">Controllers</text>
''')

# Branch 3: HTTP Methods -> Finansial (Kasir & Rekonsiliasi)
svg_parts.append(f'''
<path d="M {c3_r} 605 C {c3_r+25} 605, {c4_l-25} 642, {c4_l} 642" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arrow-indigo)" />
<path d="M {c3_r} 605 C {c3_r+25} 605, {c4_l-25} 752, {c4_l} 752" stroke="#4F46E5" stroke-width="1.8" fill="none" marker-end="url(#arrow-indigo)" />
<rect x="{(c3_r+c4_l)//2 - 32}" y="655" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#C7D2FE" stroke-width="0.8" />
<text x="{(c3_r+c4_l)//2}" y="666" class="arrow-lbl" fill="#4F46E5">Transactions</text>
<text x="{(c3_r+c4_l)//2}" y="675" class="arrow-sub">Kas / Invoicing</text>
''')

# Return from Logic Tier to API Gateway
svg_parts.append(f'''
<path d="M {c4_l} 532 C {c4_l-25} 532, {c3_r+25} 580, {c3_r} 580" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arrow-slate)" />
<rect x="{(c3_r+c4_l)//2 - 32}" y="545" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
<text x="{(c3_r+c4_l)//2}" y="556" class="arrow-lbl" fill="#64748B">Data Objects</text>
<text x="{(c3_r+c4_l)//2}" y="565" class="arrow-sub">Service Response</text>
''')


# 4. BETWEEN TIER 4 & TIER 5 (DATABASE & STORAGE)
c4_r = start_x + 3*(col_w + col_gap) + col_w - 15
c5_l = start_x + 4*(col_w + col_gap) + 15

# Upper Branch: Data Cabang & Pendaftaran -> MySQL (Query SQL)
svg_parts.append(f'''
<path d="M {c4_r} 312 C {c4_r+25} 312, {c5_l-25} 315, {c5_l} 315" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arrow-purple)" />
<rect x="{(c4_r+c5_l)//2 - 32}" y="295" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="0.8" />
<text x="{(c4_r+c5_l)//2}" y="306" class="arrow-lbl" fill="#7C3AED">SQL Queries</text>
<text x="{(c4_r+c5_l)//2}" y="315" class="arrow-sub">INSERT / UPDATE</text>
''')

# Return from MySQL -> Logic
svg_parts.append(f'''
<path d="M {c5_l} 370 C {c5_l-25} 370, {c4_r+25} 422, {c4_r} 422" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arrow-slate)" />
<rect x="{(c4_r+c5_l)//2 - 32}" y="380" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
<text x="{(c4_r+c5_l)//2}" y="391" class="arrow-lbl" fill="#64748B">Result Sets</text>
<text x="{(c4_r+c5_l)//2}" y="400" class="arrow-sub">Eloquent Models</text>
''')

# Lower Branch: Kasir & Invoicing -> File Storage (Upload Proof / Generate PDF)
svg_parts.append(f'''
<path d="M {c4_r} 642 C {c4_r+25} 642, {c5_l-25} 595, {c5_l} 595" stroke="#7C3AED" stroke-width="1.8" fill="none" marker-end="url(#arrow-purple)" />
<rect x="{(c4_r+c5_l)//2 - 32}" y="600" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="0.8" />
<text x="{(c4_r+c5_l)//2}" y="611" class="arrow-lbl" fill="#7C3AED">Upload Bukti</text>
<text x="{(c4_r+c5_l)//2}" y="620" class="arrow-sub">Storage Write</text>
''')

# Lower Return: File Storage -> Logic (Fetch PDF / Stream)
svg_parts.append(f'''
<path d="M {c5_l} 665 C {c5_l-25} 665, {c4_r+25} 752, {c4_r} 752" stroke="#64748B" stroke-width="1.8" fill="none" marker-end="url(#arrow-slate)" />
<rect x="{(c4_r+c5_l)//2 - 32}" y="690" width="64" height="23" rx="4" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="0.8" />
<text x="{(c4_r+c5_l)//2}" y="701" class="arrow-lbl" fill="#64748B">Fetch PDF</text>
<text x="{(c4_r+c5_l)//2}" y="710" class="arrow-sub">Kuitansi Stream</text>
''')

svg_parts.append('</svg>')

final_svg = ''.join(svg_parts)

dest_dir = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb'
svg_path = os.path.join(dest_dir, 'visualisasi_arsitektur_landscape.svg')
png_path = os.path.join(dest_dir, 'visualisasi_arsitektur_landscape.png')

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(final_svg)
print('SVG saved successfully:', os.path.getsize(svg_path))

# Render to 180 DPI PNG for high clarity
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=180)
pix.save(png_path)
print('PNG rendered successfully:', os.path.getsize(png_path))

