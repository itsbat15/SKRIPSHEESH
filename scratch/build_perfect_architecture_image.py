import fitz  # PyMuPDF
import os

width = 2200
height = 1180

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .tier-header-txt {{ font-family: 'Segoe UI', Inter, Arial, sans-serif; font-size: 18px; font-weight: 800; fill: #FFFFFF; text-anchor: middle; letter-spacing: 0.5px; }}
      .card-title-txt {{ font-family: 'Segoe UI', Inter, Arial, sans-serif; font-size: 15px; font-weight: 800; fill: #0F172A; }}
      .arrow-lbl-txt {{ font-family: 'Segoe UI', Inter, Arial, sans-serif; font-size: 11px; font-weight: 800; text-anchor: middle; }}
    </style>

    <filter id="box-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0F172A" flood-opacity="0.04" />
    </filter>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2.5" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.07" />
    </filter>
    <filter id="pill-shadow" x="-5%" y="-5%" width="110%" height="120%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.09" />
    </filter>

    <!-- Arrow Markers -->
    <marker id="m-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#1E88E5" />
    </marker>
    <marker id="m-indigo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#3949AB" />
    </marker>
    <marker id="m-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#7B1FA2" />
    </marker>
    <marker id="m-slate" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#94A3B8" />
    </marker>
  </defs>

  <!-- Pure White Background identical to Canva canvas -->
  <rect width="100%" height="100%" fill="#FFFFFF" />
'''

# Layout calculations
start_x = 45
start_y = 45
col_w = 285
col_gap = 130
col_h = 1070

cols = [
    {
        'title': 'User Tier', 'color': '#1E88E5',
        'cards': [
            {'title': 'Super Admin\\n(Pusat)', 'icon': 'shield-user', 'y': 150, 'h': 260},
            {'title': 'Staf\\nAdministrasi', 'icon': 'store', 'y': 560, 'h': 260}
        ]
    },
    {
        'title': 'Presentation Tier', 'color': '#0288D1',
        'cards': [
            {'title': 'Next.js\\nApp Router', 'icon': 'globe', 'y': 130, 'h': 140},
            {'title': 'Responsive\\nMulti-Device UI', 'icon': 'devices', 'y': 360, 'h': 140},
            {'title': 'Client State\\nManagement', 'icon': 'sliders', 'y': 590, 'h': 140},
            {'title': 'Route Guards &\\nMiddleware', 'icon': 'lock', 'y': 820, 'h': 140}
        ]
    },
    {
        'title': 'API Gateway Tier', 'color': '#FB8C00',
        'cards': [
            {'title': 'RESTful API\\nEndpoints', 'icon': 'network', 'y': 160, 'h': 210},
            {'title': 'Laravel Sanctum\\nAuth', 'icon': 'key', 'y': 470, 'h': 210},
            {'title': 'HTTP Standard\\nMethods', 'icon': 'arrows', 'y': 780, 'h': 210}
        ]
    },
    {
        'title': 'Business Logic Tier', 'color': '#3949AB',
        'cards': [
            {'title': 'RBAC &\\nFilter Cabang', 'icon': 'funnel', 'y': 120, 'h': 110},
            {'title': 'Master Data\\nCabang', 'icon': 'building', 'y': 275, 'h': 110},
            {'title': 'Pendaftaran\\nSiswa', 'icon': 'userplus', 'y': 430, 'h': 110},
            {'title': 'Jatuh Tempo\\nSPP', 'icon': 'clock', 'y': 585, 'h': 110},
            {'title': 'Kasir &\\nInvoicing', 'icon': 'card', 'y': 740, 'h': 110},
            {'title': 'Rekonsiliasi Kas\\nMulticabang', 'icon': 'chart', 'y': 895, 'h': 110}
        ]
    },
    {
        'title': 'Data Storage Tier', 'color': '#7B1FA2',
        'cards': [
            {'title': 'Basis Data\\nRelasional\\nMySQL', 'icon': 'database', 'y': 180, 'h': 360},
            {'title': 'Penyimpanan\\nBerkas Digital', 'icon': 'folder-cloud', 'y': 620, 'h': 360}
        ]
    }
]

def get_canva_icon(icon_name, cx, cy, col):
    if icon_name == 'shield-user':
        return f'''
        <g transform="translate({cx-26},{cy-34}) scale(2.2)">
          <path d="M12 2L4 5.5v5.8c0 5 3.4 9.6 8 10.7 4.6-1.1 8-5.7 8-10.7V5.5L12 2z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="12" cy="10" r="3" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M7.5 16.5c1.2-1.8 2.8-2.5 4.5-2.5s3.3.7 4.5 2.5" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'store':
        return f'''
        <g transform="translate({cx-28},{cy-30}) scale(2.4)">
          <path d="M3 9l1-5h16l1 5M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0M4 9v11h16V9M9 20v-7h6v7" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif icon_name == 'globe':
        return f'''
        <g transform="translate({cx-22},{cy-22}) scale(1.8)">
          <circle cx="12" cy="12" r="9" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M3 12h18M12 3c3 4 3 14 0 18M12 3c-3 4-3 14 0 18" fill="none" stroke="{col}" stroke-width="1.5" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'devices':
        return f'''
        <g transform="translate({cx-24},{cy-22}) scale(1.8)">
          <rect x="2" y="4" width="14" height="12" rx="1.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M6 19h6M9 16v3" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <rect x="15" y="8" width="6" height="11" rx="1" fill="none" stroke="{col}" stroke-width="1.6"/>
          <circle cx="18" cy="16.5" r="0.5" fill="{col}"/>
        </g>'''
    elif icon_name == 'sliders':
        return f'''
        <g transform="translate({cx-22},{cy-22}) scale(1.8)">
          <path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'lock':
        return f'''
        <g transform="translate({cx-22},{cy-22}) scale(1.8)">
          <rect x="4" y="10" width="16" height="11" rx="2" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="12" cy="15.5" r="1.5" fill="{col}"/>
        </g>'''
    elif icon_name == 'network':
        return f'''
        <g transform="translate({cx-24},{cy-24}) scale(2.0)">
          <circle cx="12" cy="5" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <circle cx="5" cy="17" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <circle cx="19" cy="17" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M10.5 7.5L6.5 14.5M13.5 7.5L17.5 14.5M7.5 17h9" stroke="{col}" stroke-width="1.6"/>
        </g>'''
    elif icon_name == 'key':
        return f'''
        <g transform="translate({cx-24},{cy-24}) scale(2.0)">
          <circle cx="8" cy="15" r="4.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M11.5 11.5L20 3M16 3l4 4M13.5 5.5l2.5 2.5" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'arrows':
        return f'''
        <g transform="translate({cx-24},{cy-24}) scale(2.0)">
          <path d="M4 8h16M16 4l4 4-4 4M20 16H4M8 12l-4 4 4 4" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif icon_name == 'funnel':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <path d="M3 4h18l-7 8.5V19l-4 2v-8.5L3 4z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif icon_name == 'building':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 8h2M13 8h2M9 12h2M13 12h2M9 16h2M13 16h2" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'userplus':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <path d="M15 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="8.5" cy="7" r="4" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M19 8v6M16 11h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'clock':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <circle cx="12" cy="12" r="9" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M12 7v5l3 2.5" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'card':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <rect x="2" y="5" width="20" height="14" rx="2" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M2 10h20M6 15h4" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'chart':
        return f'''
        <g transform="translate({cx-20},{cy-20}) scale(1.6)">
          <path d="M3 21h18M5 17v-4M10 17v-8M15 17v-5M19 17v-11" stroke="{col}" stroke-width="2" stroke-linecap="round"/>
        </g>'''
    elif icon_name == 'database':
        return f'''
        <g transform="translate({cx-32},{cy-40}) scale(2.8)">
          <ellipse cx="12" cy="5" rx="8" ry="3" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M4 5v5c0 1.66 3.58 3 8 3s8-1.34 8-3V5M4 10v5c0 1.66 3.58 3 8 3s8-1.34 8-3v-5M4 15v5c0 1.66 3.58 3 8 3s8-1.34 8-3v-5" fill="none" stroke="{col}" stroke-width="1.8"/>
        </g>'''
    elif icon_name == 'folder-cloud':
        return f'''
        <g transform="translate({cx-32},{cy-40}) scale(2.8)">
          <path d="M4 4h5l2 2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="none" stroke="{col}" stroke-width="1.6"/>
          <path d="M12 16a2.5 2.5 0 0 1 2.4-2 3 3 0 0 1 3 3h-6a2 2 0 0 1 .6-1z" fill="none" stroke="{col}" stroke-width="1.6"/>
        </g>'''
    return ''

# Render 5 Columns and inner cards
for i, col in enumerate(cols):
    cx = start_x + i * (col_w + col_gap)

    # Tall Container
    svg += f'''
    <!-- Column {col["title"]} -->
    <rect x="{cx}" y="{start_y}" width="{col_w}" height="{col_h}" rx="16" fill="#FAFCFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#box-shadow)" />

    <!-- Column Header Pill (Exact Canva Style) -->
    <path d="M {cx} {start_y+16} Q {cx} {start_y} {cx+16} {start_y} L {cx+col_w-16} {start_y} Q {cx+col_w} {start_y} {cx+col_w} {start_y+16} L {cx+col_w} {start_y+58} L {cx} {start_y+58} Z" fill="{col["color"]}" />
    <text x="{cx+col_w//2}" y="{start_y+36}" class="tier-header-txt">{col["title"]}</text>
    '''

    for card in col['cards']:
        card_x = cx + 18
        card_w = col_w - 36
        card_y = card['y']
        card_h = card['h']

        # Render White Card
        svg += f'''
        <g filter="url(#card-shadow)">
          <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="14" fill="#FFFFFF" stroke="#E8EDF5" stroke-width="1.5" />
        '''

        # Layout icon and text inside card
        lines = card['title'].split('\\n')
        if len(cols[i]['cards']) <= 2:
            # Tall cards (Col 1 & Col 5): icon on top, text below
            icon_cx = card_x + card_w // 2
            icon_cy = card_y + card_h // 2 - 38
            svg += get_canva_icon(card['icon'], icon_cx, icon_cy, col['color'])
            
            # Text lines
            text_start_y = card_y + card_h // 2 + 40
            for line_idx, line_txt in enumerate(lines):
                svg += f'<text x="{card_x + card_w//2}" y="{text_start_y + line_idx * 22}" class="card-title-txt" text-anchor="middle">{line_txt}</text>'
        else:
            # Horizontal cards (Col 2, 3, 4): icon on left, text on right
            icon_cx = card_x + 36
            icon_cy = card_y + card_h // 2
            svg += get_canva_icon(card['icon'], icon_cx, icon_cy, col['color'])

            text_start_y = card_y + card_h // 2 - (len(lines) - 1) * 11 + 6
            for line_idx, line_txt in enumerate(lines):
                svg += f'<text x="{card_x + 72}" y="{text_start_y + line_idx * 22}" class="card-title-txt">{line_txt}</text>'

        svg += '</g>'

# ==================== 100% CORRECT & CLEAN ARROWS ====================

def draw_pill(mx, my, w, txt, col_txt='#334155'):
    h = 26
    return f'''
    <g filter="url(#pill-shadow)">
      <rect x="{mx - w//2}" y="{my - h//2}" width="{w}" height="{h}" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1" />
      <text x="{mx}" y="{my + 4.5}" class="arrow-lbl-txt" fill="{col_txt}">{txt}</text>
    </g>'''

# 1. TIER 1 -> TIER 2
c1_r = start_x + col_w
c2_l = start_x + col_w + col_gap
mid12 = (c1_r + c2_l) // 2

# Super Admin -> Next.js App Router (Forward)
svg += f'<path d="M {c1_r} 260 L {c2_l} 190" stroke="#1E88E5" stroke-width="2.2" marker-end="url(#m-blue)" />'
svg += draw_pill(mid12, 215, 105, 'HTTPS Request', '#1E88E5')

# Next.js App Router -> Super Admin (Return)
svg += f'<path d="M {c2_l} 210 L {c1_r} 290" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid12, 260, 95, 'Render UI', '#64748B')

# Staf Administrasi -> Responsive UI (CORRECTED FORWARD REQUEST!)
svg += f'<path d="M {c1_r} 670 L {c2_l} 440" stroke="#1E88E5" stroke-width="2.2" marker-end="url(#m-blue)" />'
svg += draw_pill(mid12, 545, 135, 'Input Kasir &amp; Siswa', '#1E88E5')

# Responsive UI -> Staf Administrasi (CORRECTED RETURN: CETAK KUITANSI PDF)
svg += f'<path d="M {c2_l} 460 L {c1_r} 710" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid12, 600, 125, 'Cetak Kuitansi PDF', '#64748B')


# 2. TIER 2 -> TIER 3
c2_r = start_x + col_w + col_gap + col_w
c3_l = start_x + 2*(col_w + col_gap)
mid23 = (c2_r + c3_l) // 2

# Next.js App Router -> RESTful API Endpoints
svg += f'<path d="M {c2_r} 200 L {c3_l} 240" stroke="#1E88E5" stroke-width="2.2" marker-end="url(#m-blue)" />'
svg += draw_pill(mid23, 210, 88, 'REST Calls', '#1E88E5')

# RESTful API Endpoints -> Next.js App Router
svg += f'<path d="M {c3_l} 265 L {c2_r} 225" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid23, 255, 105, 'JSON Response', '#64748B')

# Client State Management -> RESTful API Endpoints (Data Submit)
svg += f'<path d="M {c2_r} 650 L {c3_l} 300" stroke="#1E88E5" stroke-width="2.2" marker-end="url(#m-blue)" />'
svg += draw_pill(mid23, 460, 88, 'REST Calls', '#1E88E5')

# RESTful API Endpoints -> Client State Management (State Update)
svg += f'<path d="M {c3_l} 320 L {c2_r} 675" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid23, 510, 105, 'JSON Response', '#64748B')

# Route Guards -> Laravel Sanctum Auth (Auth check)
svg += f'<path d="M {c2_r} 890 L {c3_l} 575" stroke="#1E88E5" stroke-width="2.2" marker-end="url(#m-blue)" />'
svg += draw_pill(mid23, 720, 105, 'Token Bearer', '#1E88E5')

# Sanctum Auth -> Route Guards (Token status)
svg += f'<path d="M {c3_l} 600 L {c2_r} 915" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid23, 770, 105, 'Auth Status', '#64748B')


# 3. TIER 3 -> TIER 4 (ROUTING DISPATCH TO BUSINESS MODULES)
c3_r = start_x + 2*(col_w + col_gap) + col_w
c4_l = start_x + 3*(col_w + col_gap)
mid34 = (c3_r + c4_l) // 2

# Sanctum Auth -> RBAC & Filter Cabang (CORRECTED ROLE & BRANCH VALIDATION)
svg += f'<path d="M {c3_r} 530 C {c3_r+40} 530, {c4_l-40} 175, {c4_l} 175" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />'
svg += draw_pill(mid34, 250, 135, 'Validasi Token &amp; Role', '#3949AB')

# RESTful API Endpoints -> Master Data Cabang & Pendaftaran Siswa (OPERATIONAL BRANCHING)
svg += f'''
<path d="M {c3_r} 250 C {c3_r+40} 250, {c4_l-40} 330, {c4_l} 330" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />
<path d="M {c3_r} 250 C {c3_r+40} 250, {c4_l-40} 485, {c4_l} 485" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />
'''
svg += draw_pill(mid34, 370, 130, 'Modul Siswa &amp; Data', '#3949AB')

# HTTP Standard Methods -> Kasir & Rekonsiliasi (FINANCIAL BRANCHING)
svg += f'''
<path d="M {c3_r} 885 C {c3_r+40} 885, {c4_l-40} 640, {c4_l} 640" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />
<path d="M {c3_r} 885 C {c3_r+40} 885, {c4_l-40} 795, {c4_l} 795" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />
<path d="M {c3_r} 885 C {c3_r+40} 885, {c4_l-40} 950, {c4_l} 950" stroke="#3949AB" stroke-width="2.2" fill="none" marker-end="url(#m-indigo)" />
'''
svg += draw_pill(mid34, 860, 130, 'Transaksi Keuangan', '#3949AB')

# Business Logic Return -> RESTful API Endpoints (Return Objects)
svg += f'<path d="M {c4_l} 550 C {c4_l-40} 550, {c3_r+40} 290, {c3_r} 290" stroke="#94A3B8" stroke-width="2.2" fill="none" marker-end="url(#m-slate)" />'
svg += draw_pill(mid34, 460, 105, 'JSON Response', '#64748B')


# 4. TIER 4 -> TIER 5 (DATA & FILE STORAGE - COMPLETELY CORRECTED!)
c4_r = start_x + 3*(col_w + col_gap) + col_w
c5_l = start_x + 4*(col_w + col_gap)
mid45 = (c4_r + c5_l) // 2

# 1. SQL Query lines to MySQL
svg += f'''
<path d="M {c4_r} 175 L {c5_l} 250" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
<path d="M {c4_r} 330 L {c5_l} 290" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
<path d="M {c4_r} 485 L {c5_l} 330" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
<path d="M {c4_r} 640 L {c5_l} 370" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
<path d="M {c4_r} 795 L {c5_l} 410" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
<path d="M {c4_r} 950 L {c5_l} 450" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />
'''
svg += draw_pill(mid45, 270, 85, 'Query SQL', '#7B1FA2')

# Return Result Sets from MySQL
svg += f'''
<path d="M {c5_l} 490 C {c5_l-30} 490, {c4_r+30} 585, {c4_r} 585" stroke="#94A3B8" stroke-width="2.2" fill="none" marker-end="url(#m-slate)" />
'''
svg += draw_pill(mid45, 530, 90, 'Result Sets', '#64748B')

# 2. FILE STORAGE CONNECTIONS (FULLY CONNECTED AS REQUESTED!)
# Upload Bukti Bayar: From Kasir & Invoicing to Penyimpanan Berkas Digital
svg += f'<path d="M {c4_r} 810 L {c5_l} 760" stroke="#7B1FA2" stroke-width="2.2" marker-end="url(#m-purple)" />'
svg += draw_pill(mid45, 770, 135, 'Upload Bukti Transfer', '#7B1FA2')

# Unduh PDF Kuitansi: From Penyimpanan Berkas Digital back to Kasir & Rekonsiliasi
svg += f'<path d="M {c5_l} 840 L {c4_r} 965" stroke="#94A3B8" stroke-width="2.2" marker-end="url(#m-slate)" />'
svg += draw_pill(mid45, 915, 130, 'Unduh Kuitansi PDF', '#64748B')

svg += '</svg>'

dest_dir = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb'
svg_path = os.path.join(dest_dir, 'arsitektur_final_terkoreksi.svg')
png_path = os.path.join(dest_dir, 'arsitektur_final_terkoreksi.png')

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg)
print('SVG generated:', os.path.getsize(svg_path))

# Render to 200 DPI PNG
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=200)
pix.save(png_path)
print('PNG rendered:', os.path.getsize(png_path))

# Also copy to thesis asset folder
asset_path = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_3_Konsep_Arsitektur_Sistem_ARTHA.png'
pix.save(asset_path)
print('Saved to thesis assets:', asset_path)
