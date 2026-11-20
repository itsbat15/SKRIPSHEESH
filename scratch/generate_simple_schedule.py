import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def generate_simple_itk_schedule():
    wb = openpyxl.Workbook()
    
    # Bulan and week distribution:
    # Sep (4), Okt (4), Nov (4), Des (4), April (4), Mei (4), Juni (1)
    months = [
        ("Sep", 4),
        ("Okt", 4),
        ("Nov", 4),
        ("Des", 4),
        ("April", 4),
        ("Mei", 4),
        ("Juni", 1)
    ]
    
    # 25 total weeks
    total_weeks = sum(m[1] for m in months)
    
    # Activities definition: (name, is_italic, active_dict: {week_index (1-25): color_type})
    # Colors: 'P' = Purple (#5F497A), 'T' = Teal (#215868)
    activities = [
        ("Mengidentifikasi Masalah", False, {1: 'P', 2: 'P', 3: 'P', 4: 'P'}),
        ("Studi Literatur", False, {w: 'P' for w in range(3, 17)}),
        ("Requirements", True, {w: 'P' for w in range(5, 17)}),
        ("Planning", True, {w: 'P' for w in range(9, 17)}),
        ("Iteration Initialization", True, {**{w: 'P' for w in range(17, 24)}, 24: 'T'}),
        ("Design", True, {**{w: 'P' for w in range(17, 22)}, 22: 'T', 23: 'T', 24: 'T'}),
        ("Implementation", True, {**{w: 'P' for w in range(17, 24)}, 24: 'T'}),
        ("System Testing", True, {**{w: 'P' for w in range(17, 24)}, 24: 'T'}),
        ("Retrospective", True, {**{w: 'P' for w in range(17, 24)}, 24: 'T'}),
        ("Deployment", True, {24: 'T', 25: 'T'}),
        ("User Training", True, {24: 'T', 25: 'T'}),
        ("Kesimpulan dan Saran", False, {25: 'T'}),
    ]

    # Palettes
    # Sheet 1: Exact Reference Style (Purple #5F497A & Teal #215868)
    # Sheet 2: ITK Primary Blue Style (Dark Navy #1E3A8A & Royal Blue #2563EB)
    palettes = [
        ("Jadwal Simple (Sesuai Contoh)", "5F497A", "215868"),
        ("Jadwal Simple (Biru ITK)", "1E3A8A", "2563EB")
    ]

    for s_idx, (sheet_title, col1_hex, col2_hex) in enumerate(palettes):
        if s_idx == 0:
            ws = wb.active
            ws.title = sheet_title
        else:
            ws = wb.create_sheet(title=sheet_title)
            
        ws.views.sheetView[0].showGridLines = True
        
        font_header = Font(name="Times New Roman", size=11, bold=True, color="000000")
        font_week_num = Font(name="Times New Roman", size=10, bold=False, color="000000")
        font_act_regular = Font(name="Times New Roman", size=11, bold=False, color="000000")
        font_act_italic = Font(name="Times New Roman", size=11, italic=True, bold=False, color="000000")
        
        fill_color1 = PatternFill(start_color=col1_hex, end_color=col1_hex, fill_type="solid")
        fill_color2 = PatternFill(start_color=col2_hex, end_color=col2_hex, fill_type="solid")
        fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
        
        black_thin = Side(border_style="thin", color="000000")
        border_all = Border(left=black_thin, right=black_thin, top=black_thin, bottom=black_thin)

        # Row 1-3: "Kegiatan" merged A1:A3
        ws.merge_cells("A1:A3")
        cell_kegiatan = ws["A1"]
        cell_kegiatan.value = "Kegiatan"
        cell_kegiatan.font = font_header
        cell_kegiatan.alignment = Alignment(horizontal="center", vertical="center")
        
        # Row 1: "Bulan" merged B1:Z1 (cols 2 to 26)
        last_col_letter = get_column_letter(1 + total_weeks)
        ws.merge_cells(f"B1:{last_col_letter}1")
        cell_bulan = ws["B1"]
        cell_bulan.value = "Bulan"
        cell_bulan.font = font_header
        cell_bulan.alignment = Alignment(horizontal="center", vertical="center")
        
        # Apply borders to Row 1
        for c in range(1, 2 + total_weeks):
            ws.cell(row=1, column=c).border = border_all
            ws.cell(row=2, column=c).border = border_all
            ws.cell(row=3, column=c).border = border_all
            
        # Row 2: Month headers
        # Row 3: Week numbers (1, 2, 3, 4...)
        curr_col = 2
        for m_name, w_count in months:
            start_col = curr_col
            end_col = curr_col + w_count - 1
            start_ltr = get_column_letter(start_col)
            end_ltr = get_column_letter(end_col)
            
            if w_count > 1:
                ws.merge_cells(f"{start_ltr}2:{end_ltr}2")
            c_month = ws[f"{start_ltr}2"]
            c_month.value = m_name
            c_month.font = font_header
            c_month.alignment = Alignment(horizontal="center", vertical="center")
            
            for w_idx in range(1, w_count + 1):
                c_week = ws.cell(row=3, column=curr_col)
                c_week.value = w_idx
                c_week.font = font_week_num
                c_week.alignment = Alignment(horizontal="center", vertical="center")
                curr_col += 1
                
        ws.row_dimensions[1].height = 24
        ws.row_dimensions[2].height = 20
        ws.row_dimensions[3].height = 20
        
        # Data Rows (Row 4 to 15)
        for r_idx, (act_name, is_it, active_map) in enumerate(activities, start=4):
            # Activity cell
            c_act = ws.cell(row=r_idx, column=1)
            c_act.value = act_name
            c_act.font = font_act_italic if is_it else font_act_regular
            c_act.alignment = Alignment(horizontal="center", vertical="center")
            c_act.border = border_all
            ws.row_dimensions[r_idx].height = 22
            
            # Week cells
            for w_num in range(1, total_weeks + 1):
                col_num = 1 + w_num
                cw = ws.cell(row=r_idx, column=col_num)
                cw.border = border_all
                if w_num in active_map:
                    ctype = active_map[w_num]
                    cw.fill = fill_color1 if ctype == 'P' else fill_color2
                else:
                    cw.fill = fill_white
                    
        # Set Widths
        ws.column_dimensions["A"].width = 28 # Kegiatan column
        for w in range(1, total_weeks + 1):
            col_ltr = get_column_letter(1 + w)
            ws.column_dimensions[col_ltr].width = 3.2 # Compact Gantt cells

    # Save to both paths
    out1 = r"DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx"
    out2 = r"DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx"
    
    wb.save(out1)
    wb.save(out2)
    print("Simple ITK schedule table generated successfully!")

generate_simple_itk_schedule()

