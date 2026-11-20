import fitz  # PyMuPDF
import os

# Exact 2:1 aspect ratio matching user's Canva diagram (1640 x 820)
W = 1640
H = 820

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <style>
      .tier-hdr {{ font-family: 'Segoe UI', Inter, -apple-system, sans-serif; font-size: 14.5px; font-weight: 800; fill: #FFFFFF; text-anchor: middle; letter-spacing: 0.3px; }}
      .card-txt {{ font-family: 'Segoe UI', Inter, -apple-system, sans-serif; font-size: 12.5px; font-weight: 700; fill: #0F172A; }}
      .pill-txt {{ font-family: 'Segoe UI', Inter, -apple-system, sans-serif; font-size: 8.5px; font-weight: 700; fill: #334155; text-anchor: middle; }}
    </style>

    <filter id="box-sh" x="-2%" y="-1%" width="104%" height="104%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#0F172A" flood-opacity="0.04" />
    </filter>
    <filter id="card-sh" x="-4%" y="-2%" width="108%" height="108%">
      <feDropShadow dx="0" dy="1.5" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.06" />
    </filter>

    <!-- Markers -->
    <marker id="arr-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#1E88E5" />
    </marker>
    <marker id="arr-indigo" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#3949AB" />
    </marker>
    <marker id="arr-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#7B1FA2" />
    </marker>
    <marker id="arr-gray" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 7 5 L 0 8.5 z" fill="#94A3B8" />
    </marker>
  </defs>

  <!-- Pure White Canvas Background -->
  <rect width="100%" height="100%" fill="#FFFFFF" />
'''

# 5 Tier Columns configuration
start_x = 25
start_y = 20
col_w = 205
col_gap = 135
col_h = 770

cols = [
    {
        'title': 'User Tier', 'color': '#1E88E5',
        'cards': [
            {'title': ['Super Admin', '(Pusat)'], 'icon': 'shield-user', 'y': 80, 'h': 295},
            {'title': ['Staf', 'Administrasi'], 'icon': 'store', 'y': 440, 'h': 295}
        ]
    },
    {
        'title': 'Presentation Tier', 'color': '#0288D1',
        'cards': [
            {'title': ['Next.js', 'App Router'], 'icon': 'globe', 'y': 80, 'h': 130},
            {'title': ['Responsive', 'Multi-Device UI'], 'icon': 'devices', 'y': 245, 'h': 130},
            {'title': ['Client State', 'Management'], 'icon': 'sliders', 'y': 410, 'h': 130},
            {'title': ['Route Guards &', 'Middleware'], 'icon': 'lock', 'y': 575, 'h': 130}
        ]
    },
    {
        'title': 'API Gateway Tier', 'color': '#FB8C00',
        'cards': [
            {'title': ['RESTful API', 'Endpoints'], 'icon': 'network', 'y': 80, 'h': 190},
            {'title': ['Laravel Sanctum', 'Auth'], 'icon': 'key', 'y': 310, 'h': 190},
            {'title': ['HTTP Standard', 'Methods'], 'icon': 'arrows', 'y': 540, 'h': 190}
        ]
    },
    {
        'title': 'Business Logic Tier', 'color': '#3949AB',
        'cards': [
            {'title': ['RBAC &', 'Filter Cabang'], 'icon': 'funnel', 'y': 80, 'h': 90},
            {'title': ['Master Data', 'Cabang'], 'icon': 'building', 'y': 190, 'h': 90},
            {'title': ['Pendaftaran', 'Siswa'], 'icon': 'userplus', 'y': 300, 'h': 90},
            {'title': ['Jatuh Tempo', 'SPP'], 'icon': 'clock', 'y': 410, 'h': 90},
            {'title': ['Kasir &', 'Invoicing'], 'icon': 'card', 'y': 520, 'h': 90},
            {'title': ['Rekonsiliasi Kas', 'Multicabang'], 'icon': 'chart', 'y': 630, 'h': 90}
        ]
    },
    {
        'title': 'Data Storage Tier', 'color': '#7B1FA2',
        'cards': [
            {'title': ['Basis Data', 'Relasional', 'MySQL'], 'icon': 'database', 'y': 80, 'h': 320},
            {'title': ['Penyimpanan', 'Berkas Digital'], 'icon': 'folder-cloud', 'y': 440, 'h': 320}
        ]
    }
]

def get_icon(name, cx, cy, col):
    if name == 'shield-user':
        return f'''
        <g transform="translate({cx-20},{cy-26}) scale(1.7)">
          <path d="M12 2L4 5.5v5.8c0 5 3.4 9.6 8 10.7 4.6-1.1 8-5.7 8-10.7V5.5L12 2z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="12" cy="10" r="3" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M7.5 16.5c1.2-1.8 2.8-2.5 4.5-2.5s3.3.7 4.5 2.5" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'store':
        return f'''
        <g transform="translate({cx-22},{cy-24}) scale(1.85)">
          <path d="M3 9l1-5h16l1 5M3 9a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0M4 9v11h16V9M9 20v-7h6v7" fill="none" stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif name == 'globe':
        return f'''
        <g transform="translate({cx-16},{cy-16}) scale(1.35)">
          <circle cx="12" cy="12" r="9" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M3 12h18M12 3c3 4 3 14 0 18M12 3c-3 4-3 14 0 18" fill="none" stroke="{col}" stroke-width="1.5" stroke-linecap="round"/>
        </g>'''
    elif name == 'devices':
        return f'''
        <g transform="translate({cx-18},{cy-16}) scale(1.35)">
          <rect x="2" y="4" width="14" height="12" rx="1.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M6 19h6M9 16v3" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <rect x="15" y="8" width="6" height="11" rx="1" fill="none" stroke="{col}" stroke-width="1.6"/>
          <circle cx="18" cy="16.5" r="0.5" fill="{col}"/>
        </g>'''
    elif name == 'sliders':
        return f'''
        <g transform="translate({cx-16},{cy-16}) scale(1.35)">
          <path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'lock':
        return f'''
        <g transform="translate({cx-16},{cy-16}) scale(1.35)">
          <rect x="4" y="10" width="16" height="11" rx="2" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="12" cy="15.5" r="1.5" fill="{col}"/>
        </g>'''
    elif name == 'network':
        return f'''
        <g transform="translate({cx-18},{cy-18}) scale(1.5)">
          <circle cx="12" cy="5" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <circle cx="5" cy="17" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <circle cx="19" cy="17" r="2.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M10.5 7.5L6.5 14.5M13.5 7.5L17.5 14.5M7.5 17h9" stroke="{col}" stroke-width="1.6"/>
        </g>'''
    elif name == 'key':
        return f'''
        <g transform="translate({cx-18},{cy-18}) scale(1.5)">
          <circle cx="8" cy="15" r="4.5" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M11.5 11.5L20 3M16 3l4 4M13.5 5.5l2.5 2.5" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'arrows':
        return f'''
        <g transform="translate({cx-18},{cy-18}) scale(1.5)">
          <path d="M4 8h16M16 4l4 4-4 4M20 16H4M8 12l-4 4 4 4" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif name == 'funnel':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <path d="M3 4h18l-7 8.5V19l-4 2v-8.5L3 4z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </g>'''
    elif name == 'building':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <path d="M3 21h18M5 21V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16M9 8h2M13 8h2M9 12h2M13 12h2M9 16h2M13 16h2" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'userplus':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <path d="M15 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" fill="none" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
          <circle cx="8.5" cy="7" r="4" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M19 8v6M16 11h6" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'clock':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <circle cx="12" cy="12" r="9" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M12 7v5l3 2.5" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'card':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <rect x="2" y="5" width="20" height="14" rx="2" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M2 10h20M6 15h4" stroke="{col}" stroke-width="1.8" stroke-linecap="round"/>
        </g>'''
    elif name == 'chart':
        return f'''
        <g transform="translate({cx-15},{cy-15}) scale(1.3)">
          <path d="M3 21h18M5 17v-4M10 17v-8M15 17v-5M19 17v-11" stroke="{col}" stroke-width="2" stroke-linecap="round"/>
        </g>'''
    elif name == 'database':
        return f'''
        <g transform="translate({cx-22},{cy-30}) scale(2.0)">
          <ellipse cx="12" cy="5" rx="8" ry="3" fill="none" stroke="{col}" stroke-width="1.8"/>
          <path d="M4 5v5c0 1.66 3.58 3 8 3s8-1.34 8-3V5M4 10v5c0 1.66 3.58 3 8 3s8-1.34 8-3v-5M4 15v5c0 1.66 3.58 3 8 3s8-1.34 8-3v-5" fill="none" stroke="{col}" stroke-width="1.8"/>
        </g>'''
    elif name == 'folder-cloud':
        return f'''
        <g transform="translate({cx-22},{cy-30}) scale(2.0)">
          <path d="M4 4h5l2 2h9a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" fill="none" stroke="{col}" stroke-width="1.6"/>
          <path d="M12 16a2.5 2.5 0 0 1 2.4-2 3 3 0 0 1 3 3h-6a2 2 0 0 1 .6-1z" fill="none" stroke="{col}" stroke-width="1.6"/>
        </g>'''
    return ''

# Render Columns and Cards
for i, col in enumerate(cols):
    cx = start_x + i * (col_w + col_gap)

    # Column Outer Container
    svg += f'''
    <rect x="{cx}" y="{start_y}" width="{col_w}" height="{col_h}" rx="14" fill="#FAFCFF" stroke="#E2E8F0" stroke-width="1.5" filter="url(#box-sh)" />

    <!-- Column Pill Header -->
    <path d="M {cx} {start_y+14} Q {cx} {start_y} {cx+14} {start_y} L {cx+col_w-14} {start_y} Q {cx+col_w} {start_y} {cx+col_w} {start_y+14} L {cx+col_w} {start_y+44} L {cx} {start_y+44} Z" fill="{col["color"]}" />
    <text x="{cx+col_w//2}" y="{start_y+27}" class="tier-hdr">{col["title"]}</text>
    '''

    for card in col['cards']:
        card_x = cx + 12
        card_w = col_w - 24
        card_y = card['y']
        card_h = card['h']

        svg += f'''
        <g filter="url(#card-sh)">
          <rect x="{card_x}" y="{card_y}" width="{card_w}" height="{card_h}" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.5" />
        '''

        lines = card['title']
        if len(cols[i]['cards']) <= 2:
            # Tall cards (Col 1 & 5)
            icon_cx = card_x + card_w // 2
            icon_cy = card_y + card_h // 2 - 32
            svg += get_icon(card['icon'], icon_cx, icon_cy, col['color'])
            
            text_y = card_y + card_h // 2 + 35
            for l_idx, l_txt in enumerate(lines):
                svg += f'<text x="{card_x + card_w//2}" y="{text_y + l_idx*18}" class="card-txt" text-anchor="middle">{l_txt}</text>'
        else:
            # Horizontal cards (Col 2, 3, 4)
            icon_cx = card_x + 28
            icon_cy = card_y + card_h // 2
            svg += get_icon(card['icon'], icon_cx, icon_cy, col['color'])

            text_y = card_y + card_h // 2 - (len(lines) - 1) * 9 + 4
            for l_idx, l_txt in enumerate(lines):
                svg += f'<text x="{card_x + 56}" y="{text_y + l_idx*18}" class="card-txt">{l_txt}</text>'

        svg += '</g>'

# ==================== SEGMENTED ARROWS (ABSOLUTELY ZERO LINE OVERLAP) ====================

def draw_pill(mx, my, w, txt):
    h = 24
    return f'''
    <rect x="{mx - w//2}" y="{my - h//2}" width="{w}" height="{h}" rx="5" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1" />
    <text x="{mx}" y="{my + 3.5}" class="pill-txt">{txt}</text>'''

def draw_arrow_pair(x1, x2, y_fwd, y_ret, color_fwd, marker_fwd, lbl_fwd, lbl_ret, w_fwd=80, w_ret=80):
    mid_x = (x1 + x2) // 2

    # Forward Arrow (Left to Right, split into two segments so line NEVER crosses pill!)
    gap_half_fwd = w_fwd // 2 + 3
    res = f'<path d="M {x1} {y_fwd} L {mid_x - gap_half_fwd} {y_fwd}" stroke="{color_fwd}" stroke-width="1.8" />'
    res += f'<path d="M {mid_x + gap_half_fwd} {y_fwd} L {x2} {y_fwd}" stroke="{color_fwd}" stroke-width="1.8" marker-end="url(#{marker_fwd})" />'
    res += draw_pill(mid_x, y_fwd, w_fwd, lbl_fwd)

    # Return Arrow (Right to Left, split into two segments!)
    gap_half_ret = w_ret // 2 + 3
    res += f'<path d="M {x2} {y_ret} L {mid_x + gap_half_ret} {y_ret}" stroke="#94A3B8" stroke-width="1.8" />'
    res += f'<path d="M {mid_x - gap_half_ret} {y_ret} L {x1} {y_ret}" stroke="#94A3B8" stroke-width="1.8" marker-end="url(#arr-gray)" />'
    res += draw_pill(mid_x, y_ret, w_ret, lbl_ret)

    return res

# 1. TIER 1 TO TIER 2
t1_r = start_x + col_w
t2_l = start_x + col_w + col_gap
svg += draw_arrow_pair(t1_r, t2_l, 200, 240, '#1E88E5', 'arr-blue', 'HTTPS Request', 'Render UI', 92, 75)
svg += draw_arrow_pair(t1_r, t2_l, 560, 600, '#1E88E5', 'arr-blue', 'Input Kasir &amp; Siswa', 'Cetak Kuitansi PDF', 115, 105)

# 2. TIER 2 TO TIER 3 (3 PARALLEL PAIRS)
t2_r = start_x + col_w + col_gap + col_w
t3_l = start_x + 2*(col_w + col_gap)
svg += draw_arrow_pair(t2_r, t3_l, 150, 190, '#1E88E5', 'arr-blue', 'REST Calls', 'JSON Response', 75, 88)
svg += draw_arrow_pair(t2_r, t3_l, 380, 420, '#1E88E5', 'arr-blue', 'REST Calls', 'JSON Response', 75, 88)
svg += draw_arrow_pair(t2_r, t3_l, 610, 650, '#1E88E5', 'arr-blue', 'Token Bearer', 'Auth Status', 85, 80)

# 3. TIER 3 TO TIER 4 (3 PARALLEL PAIRS WITH LOGICAL LABELS)
t3_r = start_x + 2*(col_w + col_gap) + col_w
t4_l = start_x + 3*(col_w + col_gap)
svg += draw_arrow_pair(t3_r, t4_l, 150, 190, '#3949AB', 'arr-indigo', 'Modul Siswa &amp; Data', 'JSON Response', 112, 88)
svg += draw_arrow_pair(t3_r, t4_l, 380, 420, '#3949AB', 'arr-indigo', 'Validasi Token &amp; Role', 'JSON Response', 120, 88)
svg += draw_arrow_pair(t3_r, t4_l, 610, 650, '#3949AB', 'arr-indigo', 'Transaksi Keuangan', 'JSON Response', 108, 88)

# 4. TIER 4 TO TIER 5 (6 CLEAN STRAIGHT PAIRS WITH FULL STORAGE CONNECTIVITY)
t4_r = start_x + 3*(col_w + col_gap) + col_w
t5_l = start_x + 4*(col_w + col_gap)

# Rows 1-4: Connects to MySQL Database
svg += draw_arrow_pair(t4_r, t5_l, 110, 140, '#7B1FA2', 'arr-purple', 'Query SQL', 'Result Sets', 70, 70)
svg += draw_arrow_pair(t4_r, t5_l, 220, 250, '#7B1FA2', 'arr-purple', 'Query SQL', 'Result Sets', 70, 70)
svg += draw_arrow_pair(t4_r, t5_l, 330, 360, '#7B1FA2', 'arr-purple', 'Query SQL', 'Result Sets', 70, 70)
svg += draw_arrow_pair(t4_r, t5_l, 440, 470, '#7B1FA2', 'arr-purple', 'Query SQL', 'Result Sets', 70, 70)

# Rows 5-6: Connects to File Storage (Upload Bukti Transfer & Unduh Kuitansi PDF)
svg += draw_arrow_pair(t4_r, t5_l, 550, 580, '#7B1FA2', 'arr-purple', 'Upload Bukti Transfer', 'Result Sets', 120, 70)
svg += draw_arrow_pair(t4_r, t5_l, 660, 690, '#7B1FA2', 'arr-purple', 'Query SQL', 'Unduh Kuitansi PDF', 70, 115)

svg += '</svg>'

dest_dir = r'C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb'
svg_path = os.path.join(dest_dir, 'arsitektur_canva_1to1.svg')
png_path = os.path.join(dest_dir, 'arsitektur_canva_1to1.png')

with open(svg_path, 'w', encoding='utf-8') as f:
    f.write(svg)
print('SVG generated:', os.path.getsize(svg_path))

# Render to 200 DPI PNG
doc = fitz.open(svg_path)
page = doc[0]
pix = page.get_pixmap(dpi=200)
pix.save(png_path)
print('PNG rendered:', os.path.getsize(png_path))

# Update thesis asset
asset_path = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_3_Konsep_Arsitektur_Sistem_ARTHA.png'
pix.save(asset_path)
print('Saved to thesis assets:', asset_path)
