import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Data definition
phases = [
    # (Phase name, [(Activity name, active_weeks)])
    ("Fase Proposal", [
        ("Studi literatur dan identifikasi masalah", list(range(1, 9))),
        ("Analisis kebutuhan dan planning (12 User Stories)", list(range(3, 10))),
        ("Perancangan diagram sistem (BPMN, Use Case, ERD, UI)", list(range(5, 11))),
        ("Seminar proposal dan revisi naskah proposal", [11, 12]),
    ]),
    ("Inisialisasi Teknis", [
        ("Setup repositori Git, Next.js, Laravel API, & MySQL", list(range(13, 17))),
    ]),
    ("Iterasi 1", [
        ("Inisialisasi iterasi & perancangan detail (US-01 s.d. US-04)", [17]),
        ("Pembuatan prototipe (Autentikasi RBAC, Cabang, Siswa & Kuota)", [17, 18, 19]),
        ("Pengujian sistem (Black Box) & Retrospective 1", [18, 19]),
    ]),
    ("Iterasi 2", [
        ("Inisialisasi iterasi & perancangan detail (US-05 s.d. US-07)", [20]),
        ("Pembuatan prototipe (Kasir Cabang, Kuitansi PDF & Bukti Bayar)", [20, 21, 22]),
        ("Pengujian sistem (Black Box) & Retrospective 2", [21, 22]),
    ]),
    ("Iterasi 3", [
        ("Inisialisasi iterasi & perancangan detail (US-08 s.d. US-10)", [23]),
        ("Pembuatan prototipe (Validasi Transfer, SPP Otomatis & Tautan WA)", [23, 24, 25]),
        ("Pengujian sistem (Black Box) & Retrospective 3", [24, 25]),
    ]),
    ("Iterasi 4", [
        ("Inisialisasi iterasi & perancangan detail (US-11 s.d. US-12)", [26]),
        ("Pembuatan prototipe (Tutup Kasir Harian & Dasbor 8 Cabang)", [26, 27, 28]),
        ("Pengujian sistem (Black Box) & Retrospective 4 (Final)", [27, 28]),
    ]),
    ("Pasca-Iterasi", [
        ("Uji penerimaan pengguna (UAT) dan deployment", list(range(27, 31))),
        ("Penyusunan laporan akhir skripsi (Bab 4 dan Bab 5)", list(range(21, 31))),
        ("Sidang akhir, revisi naskah, dan penyerahan prototipe", [31, 32]),
    ]),
]

months = [
    ("Okt 2026", 1, 4),
    ("Nov 2026", 5, 8),
    ("Des 2026", 9, 12),
    ("Jan 2027", 13, 16),
    ("Feb 2027", 17, 20),
    ("Mar 2027", 21, 24),
    ("Apr 2027", 25, 28),
    ("Mei 2027", 29, 32),
]

# Total activities
all_rows = []
for phase_name, acts in phases:
    for i, (act_name, weeks) in enumerate(acts):
        all_rows.append({
            "phase": phase_name,
            "is_first_in_phase": (i == 0),
            "phase_len": len(acts),
            "act": act_name,
            "weeks": weeks
        })

n_rows = len(all_rows) # 20 rows
n_cols = 32

# Setup figure
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

fig_width = 16.5
fig_height = 8.5
fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=300)

ax.set_xlim(0, fig_width)
ax.set_ylim(0, fig_height)
ax.axis('off')

# Layout coordinates
margin_left = 0.5
margin_top = 0.7
title_y = fig_height - 0.35

col_phase_w = 1.6
col_act_w = 5.2
week_w = (fig_width - margin_left * 2 - col_phase_w - col_act_w) / 32 # width of each week column
grid_start_x = margin_left + col_phase_w + col_act_w

row_h = 0.28
header_h = 0.32

table_top_y = fig_height - margin_top

# Title
ax.text(margin_left, title_y, 
        "Tabel 3.14 Rencana Jadwal Pembuatan Prototipe Sistem Informasi ARTHA Berdasarkan Siklus Iterasi PxP (Oktober 2026 sampai Mei 2027)",
        fontsize=10.5, fontweight='bold', va='center', ha='left')

# Header Row 1: Months and "Kegiatan"
# Box for "Kegiatan" (spans 2 rows)
kegiatan_box = patches.Rectangle(
    (margin_left, table_top_y - header_h * 2), col_phase_w + col_act_w, header_h * 2,
    linewidth=1.2, edgecolor='black', facecolor='#F2F2F2'
)
ax.add_patch(kegiatan_box)
ax.text(margin_left + (col_phase_w + col_act_w)/2, table_top_y - header_h,
        "Kegiatan", fontsize=9.5, fontweight='bold', ha='center', va='center')

# Month headers
for m_label, w_start, w_end in months:
    m_x = grid_start_x + (w_start - 1) * week_w
    m_w = (w_end - w_start + 1) * week_w
    m_box = patches.Rectangle(
        (m_x, table_top_y - header_h), m_w, header_h,
        linewidth=1.0, edgecolor='black', facecolor='#F2F2F2'
    )
    ax.add_patch(m_box)
    ax.text(m_x + m_w / 2, table_top_y - header_h / 2,
            m_label, fontsize=8.5, fontweight='bold', ha='center', va='center')

# Week headers (Row 2 of header)
for w in range(1, 33):
    w_x = grid_start_x + (w - 1) * week_w
    w_box = patches.Rectangle(
        (w_x, table_top_y - header_h * 2), week_w, header_h,
        linewidth=1.0, edgecolor='black', facecolor='#F2F2F2'
    )
    ax.add_patch(w_box)
    w_num = ((w - 1) % 4) + 1
    ax.text(w_x + week_w / 2, table_top_y - header_h * 1.5,
            str(w_num), fontsize=8.0, fontweight='bold', ha='center', va='center')

# Draw Data Rows
data_start_y = table_top_y - header_h * 2

# Track phase box rendering
current_y = data_start_y
idx = 0
while idx < len(all_rows):
    row_info = all_rows[idx]
    phase_len = row_info["phase_len"]
    phase_box_h = phase_len * row_h
    
    # Phase box in Column 1
    phase_rect = patches.Rectangle(
        (margin_left, current_y - phase_box_h), col_phase_w, phase_box_h,
        linewidth=1.0, edgecolor='black', facecolor='#FAFAFA'
    )
    ax.add_patch(phase_rect)
    ax.text(margin_left + col_phase_w / 2, current_y - phase_box_h / 2,
            row_info["phase"], fontsize=8.5, fontweight='bold', ha='center', va='center', wrap=True)
    
    # Render activities in this phase
    for sub_idx in range(phase_len):
        act_y = current_y - (sub_idx + 1) * row_h
        cur_row_data = all_rows[idx + sub_idx]
        
        # Activity box in Column 2
        act_rect = patches.Rectangle(
            (margin_left + col_phase_w, act_y), col_act_w, row_h,
            linewidth=1.0, edgecolor='black', facecolor='white'
        )
        ax.add_patch(act_rect)
        ax.text(margin_left + col_phase_w + 0.1, act_y + row_h / 2,
                cur_row_data["act"], fontsize=8.0, va='center', ha='left')
        
        # Week grid boxes
        for w in range(1, 33):
            w_x = grid_start_x + (w - 1) * week_w
            is_active = w in cur_row_data["weeks"]
            cell_color = '#777777' if is_active else 'white'
            
            w_cell = patches.Rectangle(
                (w_x, act_y), week_w, row_h,
                linewidth=0.7, edgecolor='black', facecolor=cell_color
            )
            ax.add_patch(w_cell)

    current_y -= phase_box_h
    idx += phase_len

# Note box at bottom
note_y = current_y - 0.28
note_rect = patches.Rectangle(
    (margin_left, note_y), fig_width - margin_left * 2, 0.28,
    linewidth=1.0, edgecolor='black', facecolor='white'
)
ax.add_patch(note_rect)
ax.text(margin_left + 0.1, note_y + 0.14,
        "Keterangan: angka 1 sampai 4 menunjukkan kelompok minggu; arsiran menunjukkan rencana kegiatan.",
        fontsize=8.0, fontstyle='italic', va='center', ha='left')

plt.tight_layout()

# Save image
targets = [
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_Per_Iterasi.png",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_Per_Iterasi.png",
    r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Tabel_3_14_Jadwal_Pembuatan_Prototipe_Per_Iterasi.png"
]

for t in targets:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    plt.savefig(t, dpi=300, bbox_inches='tight')
    print(f"Saved: {t}")

plt.close()

