import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Define paths
excel_paths = [
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_ARTHA.xlsx",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_ARTHA.xlsx",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_dan_3_15_Jadwal_Pelaksanaan_TA_ARTHA.xlsx",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_dan_3_15_Jadwal_Pelaksanaan_TA_ARTHA.xlsx",
    r"C:\Users\ARIEL\.gemini\antigravity\brain\b4f2bb35-f783-4d11-88ed-819fbfb3f0fb\Tabel_3_14_Jadwal_Pembuatan_Prototipe_ARTHA.xlsx",
]

# Months and weeks: 32 weeks total
# Col A (1): Fase / Iterasi
# Col B (2): Rincian Kegiatan
# Col C..AH (3..34): Weeks 1..32
months_data = [
    ("Okt 2026", 3, 6),
    ("Nov 2026", 7, 10),
    ("Des 2026", 11, 14),
    ("Jan 2027", 15, 18),
    ("Feb 2027", 19, 22),
    ("Mar 2027", 23, 26),
    ("Apr 2027", 27, 30),
    ("Mei 2027", 31, 34),
]

# Rows data: (Phase, Activity, [active week numbers 1..32], is_phase_start, phase_span)
# Week numbers 1..32 correspond to cols 3..34 (col = week + 2)
rows_data = [
    # Fase Proposal (Weeks 1 to 12)
    ("Fase Proposal", "Studi literatur dan identifikasi masalah", list(range(1, 9)), True, 4),
    ("Fase Proposal", "Analisis kebutuhan dan planning (12 User Stories)", list(range(3, 10)), False, 0),
    ("Fase Proposal", "Perancangan diagram sistem (BPMN, Use Case, ERD, UI)", list(range(5, 11)), False, 0),
    ("Fase Proposal", "Seminar proposal dan revisi naskah proposal", [11, 12], False, 0),

    # Inisialisasi Teknis
    ("Inisialisasi Teknis", "Setup repositori Git, framework Next.js, Laravel API, & basis data MySQL", list(range(13, 17)), True, 1),

    # Iterasi 1
    ("Iterasi 1", "Inisialisasi iterasi & perancangan detail (US-01 s.d. US-04)", [17], True, 3),
    ("Iterasi 1", "Pembuatan prototipe (Autentikasi RBAC, Cabang, Siswa & Kuota)", [17, 18, 19], False, 0),
    ("Iterasi 1", "Pengujian sistem (Black Box) & Retrospective 1", [18, 19], False, 0),

    # Iterasi 2
    ("Iterasi 2", "Inisialisasi iterasi & perancangan detail (US-05 s.d. US-07)", [20], True, 3),
    ("Iterasi 2", "Pembuatan prototipe (Kasir Cabang, Kuitansi PDF & Bukti Bayar)", [20, 21, 22], False, 0),
    ("Iterasi 2", "Pengujian sistem (Black Box) & Retrospective 2", [21, 22], False, 0),

    # Iterasi 3
    ("Iterasi 3", "Inisialisasi iterasi & perancangan detail (US-08 s.d. US-10)", [23], True, 3),
    ("Iterasi 3", "Pembuatan prototipe (Validasi Transfer, SPP Otomatis & Tautan WA)", [23, 24, 25], False, 0),
    ("Iterasi 3", "Pengujian sistem (Black Box) & Retrospective 3", [24, 25], False, 0),

    # Iterasi 4
    ("Iterasi 4", "Inisialisasi iterasi & perancangan detail (US-11 s.d. US-12)", [26], True, 3),
    ("Iterasi 4", "Pembuatan prototipe (Tutup Kasir Harian & Dasbor 8 Cabang)", [26, 27, 28], False, 0),
    ("Iterasi 4", "Pengujian sistem (Black Box) & Retrospective 4 (Final)", [27, 28], False, 0),

    # Pasca-Iterasi
    ("Pasca-Iterasi", "Uji penerimaan pengguna (UAT) dan deployment", list(range(27, 31)), True, 3),
    ("Pasca-Iterasi", "Penyusunan laporan akhir skripsi (Bab 4 dan Bab 5)", list(range(21, 31)), False, 0),
    ("Pasca-Iterasi", "Sidang akhir, revisi naskah, dan penyerahan prototipe", [31, 32], False, 0),
]

def build_iterative_sheet(wb, sheet_name, active_fill_hex, header_bg_hex=None):
    if sheet_name in wb.sheetnames:
        del wb[sheet_name]
    ws = wb.create_sheet(title=sheet_name)

    # Styles
    font_title = Font(name="Times New Roman", size=11, bold=True)
    font_header = Font(name="Times New Roman", size=9.5, bold=True)
    font_week = Font(name="Times New Roman", size=9, bold=True)
    font_cell = Font(name="Times New Roman", size=9, bold=False)
    font_phase = Font(name="Times New Roman", size=9, bold=True)
    font_note = Font(name="Times New Roman", size=8.5, italic=True)

    thin_border_side = Side(border_style="thin", color="00000000")
    border_all = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    fill_active = PatternFill(start_color=active_fill_hex, end_color=active_fill_hex, fill_type="solid")
    fill_white = PatternFill(start_color="00FFFFFF", end_color="00FFFFFF", fill_type="solid")
    
    if header_bg_hex:
        fill_header = PatternFill(start_color=header_bg_hex, end_color=header_bg_hex, fill_type="solid")
    else:
        fill_header = None

    # Row 1: Title
    ws.merge_cells("A1:AH1")
    title_cell = ws["A1"]
    title_cell.value = "Tabel 3.14 Rencana Jadwal Pembuatan Prototipe Sistem Informasi ARTHA Berdasarkan Siklus Iterasi PxP (Oktober 2026 sampai Mei 2027)"
    title_cell.font = font_title
    title_cell.alignment = Alignment(horizontal="left", vertical="center")
    ws.row_dimensions[1].height = 24

    # Row 2 & 3: Headers
    # Merge A2:B2 for "Kegiatan"
    ws.merge_cells("A2:B2")
    ws["A2"].value = "Kegiatan"
    ws["A2"].font = font_header
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    ws["A3"].value = "Fase / Iterasi"
    ws["A3"].font = font_week
    ws["A3"].alignment = Alignment(horizontal="center", vertical="center")

    ws["B3"].value = "Rincian Kegiatan"
    ws["B3"].font = font_week
    ws["B3"].alignment = Alignment(horizontal="center", vertical="center")

    # Months header in Row 2
    for m_label, start_c, end_c in months_data:
        ws.merge_cells(start_row=2, start_column=start_c, end_row=2, end_column=end_c)
        c = ws.cell(row=2, column=start_c)
        c.value = m_label
        c.font = font_header
        c.alignment = Alignment(horizontal="center", vertical="center")

    # Weeks header in Row 3
    for w_idx in range(1, 33):
        col = w_idx + 2
        c = ws.cell(row=3, column=col)
        c.value = ((w_idx - 1) % 4) + 1
        c.font = font_week
        c.alignment = Alignment(horizontal="center", vertical="center")

    # Format header borders
    for r in [2, 3]:
        ws.row_dimensions[r].height = 20
        for c in range(1, 35):
            cell = ws.cell(row=r, column=c)
            cell.border = border_all
            if fill_header:
                cell.fill = fill_header

    # Data Rows (Row 4 to Row 23)
    curr_row = 4
    phase_start_row = 4

    for item in rows_data:
        phase_name, activity_name, active_weeks, is_start, span = item
        ws.row_dimensions[curr_row].height = 19

        # Column A (Phase)
        cell_phase = ws.cell(row=curr_row, column=1)
        if is_start:
            phase_start_row = curr_row
            cell_phase.value = phase_name
            cell_phase.font = font_phase
            cell_phase.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            if span > 1:
                ws.merge_cells(start_row=curr_row, start_column=1, end_row=curr_row + span - 1, end_column=1)
        
        # Column B (Activity)
        cell_act = ws.cell(row=curr_row, column=2)
        cell_act.value = activity_name
        cell_act.font = font_cell
        cell_act.alignment = Alignment(horizontal="left", vertical="center")
        cell_act.border = border_all

        # Columns C to AH (Weeks 1 to 32)
        for w_idx in range(1, 33):
            col = w_idx + 2
            cell_w = ws.cell(row=curr_row, column=col)
            cell_w.border = border_all
            if w_idx in active_weeks:
                cell_w.fill = fill_active

        curr_row += 1

    # Border for Column A across merged rows
    for r in range(4, curr_row):
        ws.cell(row=r, column=1).border = border_all

    # Row 24: Keterangan
    ws.row_dimensions[curr_row].height = 20
    ws.merge_cells(start_row=curr_row, start_column=1, end_row=curr_row, end_column=34)
    cell_note = ws.cell(row=curr_row, column=1)
    cell_note.value = "Keterangan: angka 1 sampai 4 menunjukkan kelompok minggu; arsiran menunjukkan rencana kegiatan."
    cell_note.font = font_note
    cell_note.alignment = Alignment(horizontal="left", vertical="center")

    # Column dimensions
    ws.column_dimensions["A"].width = 15.0
    ws.column_dimensions["B"].width = 46.0
    for w_idx in range(1, 33):
        col_letter = get_column_letter(w_idx + 2)
        ws.column_dimensions[col_letter].width = 3.8

    # Gridlines
    ws.views.sheetView[0].showGridLines = True

def main():
    for path in excel_paths:
        if os.path.exists(path):
            print(f"Updating: {path}")
            wb = openpyxl.load_workbook(path)
            
            # Add sheet 1: Jadwal per Iterasi (Abu-abu)
            build_iterative_sheet(wb, "Jadwal per Iterasi (Dua Kolom)", active_fill_hex="00999999")
            
            # Add sheet 2: Jadwal per Iterasi (Biru ITK)
            build_iterative_sheet(wb, "Jadwal per Iterasi (Biru ITK)", active_fill_hex="001E3A8A")

            wb.save(path)
            print(f"Successfully saved: {path}")

if __name__ == "__main__":
    main()

