import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def build_schedule_workbook():
    wb = openpyxl.Workbook()
    
    # Setup data
    data_rows = [
        # FASE I
        (True, "I", "Fase Identifikasi Kebutuhan (Requirements)", [], ""),
        (False, "1", "Wawancara mendalam bersama Pemilik Lembaga dan observasi delapan kantor cabang", [1, 2], "Transkrip wawancara dan catatan lapangan"),
        (False, "2", "Analisis dokumen manual (Buku Besar, formulir pendaftaran, dan kartu kuitansi)", [2, 3], "Matriks perbandingan proses bisnis As-Is"),
        (False, "3", "Pemodelan proses bisnis BPMN (As-Is dan To-Be) serta spesifikasi User Stories", [3, 4], "Diagram BPMN 2.0 dan 12 butir User Stories"),
        
        # FASE II
        (True, "II", "Fase Perencanaan Rilis (Planning)", [], ""),
        (False, "4", "Estimasi bobot tugas dengan Fibonacci Story Points dan penetapan rencana rilis", [4], "Dokumen matriks prioritas backlog rilis"),
        (False, "5", "Perancangan arsitektur sistem, pemodelan use case, dan skema basis data relasional ERD", [4], "Diagram Arsitektur, Use Case, dan ERD MySQL"),
        
        # FASE III
        (True, "III", "Fase Siklus Iterasi PxP (Iterations)", [], ""),
        (False, "6", "Iterasi 1: Inisialisasi proyek, modul login cabang RBAC, dan form pendaftaran siswa", [5, 6], "Modul Registrasi Siswa dan Unit Test 1"),
        (False, "7", "Iterasi 2: Modul kasir tunai cabang, kalkulasi saldo, dan penerbitan kuitansi PDF", [7, 8], "Modul Kasir Pembayaran dan Kuitansi PDF"),
        (False, "8", "Iterasi 3: Modul unggah bukti transfer, validasi mutasi bank, dan penagihan WhatsApp", [9, 10], "Modul Validasi Transfer dan Pengawasan SPP"),
        (False, "9", "Iterasi 4: Modul rekonsiliasi kas harian, berita acara PDF, dan dasbor konsolidasi", [11, 12], "Dasbor Monitoring Multicabang Terintegrasi"),
        
        # FASE IV
        (True, "IV", "Fase Evaluasi, Penyebaran, dan Finalisasi", [], ""),
        (False, "10", "Pengujian kelayakan operasional sistem (User Acceptance Testing) bersama mitra", [13], "Dokumen lembar uji dan berita acara UAT"),
        (False, "11", "Penyebaran prototipe ke peladen awan (VPS Cloud Deployment & domain HTTPS)", [14], "Aplikasi web aktif daring (live production)"),
        (False, "12", "Retrospeksi akhir pengembang mandiri dan evaluasi pencapaian Story Points", [15], "Dokumen log retrospektif dan evaluasi defect"),
        (False, "13", "Penyusunan draf lengkap laporan Tugas Akhir dan persiapan sidang seminar proposal", [15, 16], "Naskah final Tugas Akhir dan kelengkapan uji"),
    ]

    sheet_configs = [
        ("Jadwal PxP (Standar X)", "X"),
        ("Jadwal PxP (Simbol Centang)", "✓")
    ]

    for idx, (title, marker) in enumerate(sheet_configs):
        if idx == 0:
            ws = wb.active
            ws.title = title
        else:
            ws = wb.create_sheet(title=title)

        ws.views.sheetView[0].showGridLines = True

        # Styles (Standar Akademik ITK - Times New Roman)
        font_title = Font(name="Times New Roman", size=12, bold=True, color="000000")
        font_header_main = Font(name="Times New Roman", size=10, bold=True, color="FFFFFF")
        font_header_sub = Font(name="Times New Roman", size=9, bold=True, color="FFFFFF")
        font_phase = Font(name="Times New Roman", size=10, bold=True, color="1E3A8A")
        font_body = Font(name="Times New Roman", size=10, color="000000")
        font_gantt_active = Font(name="Times New Roman", size=10, bold=True, color="FFFFFF")

        fill_header_main = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
        fill_header_sub = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
        fill_phase = PatternFill(start_color="EEF2FF", end_color="EEF2FF", fill_type="solid")
        fill_gantt_active = PatternFill(start_color="1D4ED8", end_color="1D4ED8", fill_type="solid")
        fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

        thin_side = Side(border_style="thin", color="CBD5E1")
        med_side = Side(border_style="medium", color="1E3A8A")

        border_cell = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
        border_header = Border(left=thin_side, right=thin_side, top=med_side, bottom=med_side)

        # 1. Judul Tabel
        ws.merge_cells("A1:S1")
        ws["A1"] = "Tabel 3.14 Rencana Jadwal dan Matriks Pelaksanaan Pembuatan Prototipe PxP"
        ws["A1"].font = font_title
        ws["A1"].alignment = Alignment(horizontal="left", vertical="center")
        ws.row_dimensions[1].height = 24

        # 2. Header Baris 1 (Row 3)
        headers_r1 = [
            ("A3:A4", "No.", Alignment(horizontal="center", vertical="center", wrap_text=True)),
            ("B3:B4", "Fase dan Rincian Aktivitas Pengembangan", Alignment(horizontal="center", vertical="center", wrap_text=True)),
            ("C3:F3", "Minggu 1-4 (Bulan I)", Alignment(horizontal="center", vertical="center")),
            ("G3:J3", "Minggu 5-8 (Bulan II)", Alignment(horizontal="center", vertical="center")),
            ("K3:N3", "Minggu 9-12 (Bulan III)", Alignment(horizontal="center", vertical="center")),
            ("O3:R3", "Minggu 13-16 (Bulan IV)", Alignment(horizontal="center", vertical="center")),
            ("S3:S4", "Artefak Keluaran Tahapan", Alignment(horizontal="center", vertical="center", wrap_text=True)),
        ]

        for cell_range, text, align in headers_r1:
            ws.merge_cells(cell_range)
            top_left = ws[cell_range.split(":")[0]]
            top_left.value = text
            top_left.font = font_header_main
            top_left.fill = fill_header_main
            top_left.alignment = align

        for col in range(1, 20):
            c = ws.cell(row=3, column=col)
            c.fill = fill_header_main
            c.border = border_header
            if not c.font.bold:
                c.font = font_header_main

        # 3. Header Baris 2 (Row 4) Angka Minggu
        for w in range(1, 17):
            col = w + 2
            c = ws.cell(row=4, column=col)
            c.value = w
            c.font = font_header_sub
            c.fill = fill_header_sub
            c.alignment = Alignment(horizontal="center", vertical="center")
            c.border = border_header

        for col_idx in [1, 2, 19]:
            c = ws.cell(row=4, column=col_idx)
            c.fill = fill_header_main
            c.border = border_header

        ws.row_dimensions[3].height = 24
        ws.row_dimensions[4].height = 20

        # 4. Data Rows
        curr_row = 5
        for item in data_rows:
            is_phase, no_val, act_val, active_w, art_val = item
            
            if is_phase:
                ws.cell(row=curr_row, column=1, value=no_val).alignment = Alignment(horizontal="center", vertical="center")
                ws.cell(row=curr_row, column=2, value=act_val).alignment = Alignment(horizontal="left", vertical="center")
                
                for col in range(1, 20):
                    c = ws.cell(row=curr_row, column=col)
                    c.font = font_phase
                    c.fill = fill_phase
                    c.border = border_cell
                ws.row_dimensions[curr_row].height = 22
            else:
                is_even = (curr_row % 2 == 0)
                row_fill = fill_zebra if is_even else PatternFill(fill_type=None)
                
                c1 = ws.cell(row=curr_row, column=1, value=no_val)
                c1.alignment = Alignment(horizontal="center", vertical="center")
                c1.font = font_body
                c1.border = border_cell
                if row_fill.fill_type: c1.fill = row_fill
                
                c2 = ws.cell(row=curr_row, column=2, value=act_val)
                c2.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                c2.font = font_body
                c2.border = border_cell
                if row_fill.fill_type: c2.fill = row_fill
                
                for w in range(1, 17):
                    col = w + 2
                    cw = ws.cell(row=curr_row, column=col)
                    cw.border = border_cell
                    if w in active_w:
                        cw.value = marker
                        cw.font = font_gantt_active
                        cw.fill = fill_gantt_active
                        cw.alignment = Alignment(horizontal="center", vertical="center")
                    else:
                        cw.value = ""
                        cw.font = font_body
                        if row_fill.fill_type: cw.fill = row_fill
                        cw.alignment = Alignment(horizontal="center", vertical="center")
                
                c19 = ws.cell(row=curr_row, column=19, value=art_val)
                c19.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
                c19.font = font_body
                c19.border = border_cell
                if row_fill.fill_type: c19.fill = row_fill
                
                ws.row_dimensions[curr_row].height = 24
                
            curr_row += 1

        # Optimal Column Widths
        ws.column_dimensions["A"].width = 6
        ws.column_dimensions["B"].width = 46
        for w in range(1, 17):
            col_letter = get_column_letter(w + 2)
            ws.column_dimensions[col_letter].width = 4.2
        ws.column_dimensions["S"].width = 40

    out1 = r"DRAFT PROPOSAL MD\BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx"
    out2 = r"DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Tabel_3_14_Jadwal_Pembuatan_Prototipe_PxP.xlsx"
    
    wb.save(out1)
    wb.save(out2)
    print("Multi-sheet Excel file generated successfully.")

build_schedule_workbook()
