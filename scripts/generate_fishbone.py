import matplotlib.pyplot as plt
import matplotlib.patches as patches
import textwrap
import os

def create_fishbone_diagram_4m(output_path):
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    ax.axis('off')
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9.6)

    font_family = 'Segoe UI'
    line_color = '#111111'
    line_width = 1.8

    # 1. Main Central Spine
    spine_y = 4.8
    spine_start_x = 0.6
    spine_end_x = 11.8
    ax.plot([spine_start_x, spine_end_x], [spine_y, spine_y], color=line_color, lw=2.4, zorder=2)

    # 2. Effect Box (Head of Fish)
    head_box_x = 11.8
    head_box_y = 3.2
    head_box_w = 3.8
    head_box_h = 3.2

    rect_head = patches.FancyBboxPatch(
        (head_box_x, head_box_y), head_box_w, head_box_h,
        boxstyle="square,pad=0",
        linewidth=line_width, edgecolor=line_color, facecolor='white', zorder=3
    )
    ax.add_patch(rect_head)

    effect_text = (
        "Rendahnya Efisiensi dan Akurasi\n"
        "pada Pengelolaan Operasional Bimbel\n"
        "Multicabang yang Berdampak pada\n"
        "Risiko Kehilangan Data, Overcapacity\n"
        "Kelas, Bentrok Jadwal Tentor, dan\n"
        "Keterlambatan Penagihan SPP"
    )
    ax.text(
        head_box_x + head_box_w / 2.0, head_box_y + head_box_h / 2.0,
        effect_text,
        ha='center', va='center',
        fontsize=10.5, fontfamily=font_family, fontweight='bold',
        color=line_color, linespacing=1.35, zorder=4
    )

    # Category Box Function
    def draw_cat_box(cx, cy, text, bw=2.4, bh=0.7):
        bx, by = cx - bw/2.0, cy - bh/2.0
        rect = patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="square,pad=0",
            linewidth=line_width, edgecolor=line_color, facecolor='white', zorder=5
        )
        ax.add_patch(rect)
        ax.text(
            cx, cy, text,
            ha='center', va='center',
            fontsize=12, fontfamily=font_family, fontweight='bold',
            color=line_color, zorder=6
        )

    # Category coordinates
    man_cx, man_cy = 3.6, 8.9
    man_bot_y = man_cy - 0.35
    man_spine_x, man_spine_y = 5.2, spine_y
    draw_cat_box(man_cx, man_cy, "Man")
    ax.plot([man_cx, man_spine_x], [man_bot_y, man_spine_y], color=line_color, lw=line_width, zorder=2)

    mach_cx, mach_cy = 9.2, 8.9
    mach_bot_y = mach_cy - 0.35
    mach_spine_x, mach_spine_y = 10.8, spine_y
    draw_cat_box(mach_cx, mach_cy, "Machine")
    ax.plot([mach_cx, mach_spine_x], [mach_bot_y, mach_spine_y], color=line_color, lw=line_width, zorder=2)

    mat_cx, mat_cy = 3.6, 0.7
    mat_top_y = mat_cy + 0.35
    mat_spine_x, mat_spine_y = 5.2, spine_y
    draw_cat_box(mat_cx, mat_cy, "Material")
    ax.plot([mat_cx, mat_spine_x], [mat_top_y, mat_spine_y], color=line_color, lw=line_width, zorder=2)

    met_cx, met_cy = 9.2, 0.7
    met_top_y = met_cy + 0.35
    met_spine_x, met_spine_y = 10.8, spine_y
    draw_cat_box(met_cx, met_cy, "Metode")
    ax.plot([met_cx, met_spine_x], [met_top_y, met_spine_y], color=line_color, lw=line_width, zorder=2)

    def add_sub_branch_top(start_cx, bot_y, sp_x, sp_y, branch_y, text, text_len=3.7):
        intersect_x = start_cx + (branch_y - bot_y) * (sp_x - start_cx) / (sp_y - bot_y)
        left_x = intersect_x - text_len
        ax.plot([left_x, intersect_x], [branch_y, branch_y], color=line_color, lw=1.3, zorder=2)
        wrapped = "\n".join(textwrap.wrap(text, width=38))
        ax.text(
            left_x + 0.05, branch_y + 0.12, wrapped,
            ha='left', va='bottom',
            fontsize=8.5, fontfamily=font_family,
            color=line_color, linespacing=1.2, zorder=4
        )

    def add_sub_branch_bottom(start_cx, top_y, sp_x, sp_y, branch_y, text, text_len=3.7):
        intersect_x = start_cx + (branch_y - top_y) * (sp_x - start_cx) / (sp_y - top_y)
        left_x = intersect_x - text_len
        ax.plot([left_x, intersect_x], [branch_y, branch_y], color=line_color, lw=1.3, zorder=2)
        wrapped = "\n".join(textwrap.wrap(text, width=38))
        ax.text(
            left_x + 0.05, branch_y + 0.12, wrapped,
            ha='left', va='bottom',
            fontsize=8.5, fontfamily=font_family,
            color=line_color, linespacing=1.2, zorder=4
        )

    # SUB-BRANCHES: MAN
    man_items = [
        "Pergantian staf administrasi cabang yang sering terjadi menyulitkan pemahaman alur kerja dan pembukuan manual",
        "Pimpinan pusat kesulitan mengawasi aktivitas operasional harian di delapan cabang secara serentak"
    ]
    add_sub_branch_top(man_cx, man_bot_y, man_spine_x, man_spine_y, 7.4, man_items[0], text_len=3.7)
    add_sub_branch_top(man_cx, man_bot_y, man_spine_x, man_spine_y, 6.0, man_items[1], text_len=3.7)

    # SUB-BRANCHES: MACHINE
    mach_items = [
        "Belum tersedianya sistem informasi manajemen terpusat berbasis web yang menghubungkan delapan cabang secara real-time",
        "Belum tersedia modul penjadwalan yang dapat mendeteksi bentrok jadwal mengajar tentor antarcabang secara otomatis",
        "Belum adanya modul notifikasi pengingat jatuh tempo pembayaran SPP ke WhatsApp wali murid"
    ]
    add_sub_branch_top(mach_cx, mach_bot_y, mach_spine_x, mach_spine_y, 7.6, mach_items[0], text_len=3.7)
    add_sub_branch_top(mach_cx, mach_bot_y, mach_spine_x, mach_spine_y, 6.6, mach_items[1], text_len=3.7)
    add_sub_branch_top(mach_cx, mach_bot_y, mach_spine_x, mach_spine_y, 5.6, mach_items[2], text_len=3.7)

    # SUB-BRANCHES: MATERIAL
    mat_items = [
        "Pencatatan pendaftaran siswa dan riwayat pembayaran SPP masih mengandalkan buku besar kertas A4 di cabang",
        "Data operasional tersimpan terisolasi di setiap cabang tanpa basis data terpusat",
        "Berkas fisik kuitansi dan buku pendaftaran rentan risiko kerusakan fisik, lapuk, basah, atau terselip",
        "Data profil tempat tinggal siswa belum tercatat lengkap sehingga menyulitkan analisis sebaran geografis"
    ]
    add_sub_branch_bottom(mat_cx, mat_top_y, mat_spine_x, mat_spine_y, 4.0, mat_items[0], text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_top_y, mat_spine_x, mat_spine_y, 3.1, mat_items[1], text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_top_y, mat_spine_x, mat_spine_y, 2.2, mat_items[2], text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_top_y, mat_spine_x, mat_spine_y, 1.3, mat_items[3], text_len=3.7)

    # SUB-BRANCHES: METODE
    met_items = [
        "Pengendalian batas kapasitas kelas manual dengan menghitung buku kertas rawan memicu overcapacity",
        "Penagihan SPP manual satu per satu melalui pesan teks WhatsApp pribadi oleh staf berisiko terlewat",
        "Pencocokan laporan penerimaan kas cabang dan mutasi rekening bank dilakukan manual satu per satu"
    ]
    add_sub_branch_bottom(met_cx, met_top_y, met_spine_x, met_spine_y, 3.8, met_items[0], text_len=3.7)
    add_sub_branch_bottom(met_cx, met_top_y, met_spine_x, met_spine_y, 2.8, met_items[1], text_len=3.7)
    add_sub_branch_bottom(met_cx, met_top_y, met_spine_x, met_spine_y, 1.8, met_items[2], text_len=3.7)

    plt.tight_layout()
    plt.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
    plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()
    print("4M Fishbone generated successfully at:", output_path)

def create_fishbone_diagram_5m(output_path):
    fig, ax = plt.subplots(figsize=(17, 10), dpi=300)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    ax.axis('off')
    ax.set_xlim(0, 17)
    ax.set_ylim(0, 10)

    font_family = 'Segoe UI'
    line_color = '#111111'
    line_width = 1.8

    # Main Spine
    spine_y = 5.0
    spine_start_x = 0.5
    spine_end_x = 12.8
    ax.plot([spine_start_x, spine_end_x], [spine_y, spine_y], color=line_color, lw=2.4, zorder=2)

    # Effect Box
    head_box_x = 12.8
    head_box_y = 3.3
    head_box_w = 4.0
    head_box_h = 3.4

    rect_head = patches.FancyBboxPatch(
        (head_box_x, head_box_y), head_box_w, head_box_h,
        boxstyle="square,pad=0",
        linewidth=line_width, edgecolor=line_color, facecolor='white', zorder=3
    )
    ax.add_patch(rect_head)

    effect_text = (
        "Rendahnya Efisiensi dan Akurasi\n"
        "pada Pengelolaan Operasional Bimbel\n"
        "Multicabang yang Berdampak pada\n"
        "Risiko Kehilangan Data, Overcapacity\n"
        "Kelas, Bentrok Jadwal Tentor, dan\n"
        "Keterlambatan Penagihan SPP"
    )
    ax.text(
        head_box_x + head_box_w / 2.0, head_box_y + head_box_h / 2.0,
        effect_text,
        ha='center', va='center',
        fontsize=10.5, fontfamily=font_family, fontweight='bold',
        color=line_color, linespacing=1.35, zorder=4
    )

    def draw_cat_box(cx, cy, text, bw=2.6, bh=0.7):
        bx, by = cx - bw/2.0, cy - bh/2.0
        rect = patches.FancyBboxPatch(
            (bx, by), bw, bh,
            boxstyle="square,pad=0",
            linewidth=line_width, edgecolor=line_color, facecolor='white', zorder=5
        )
        ax.add_patch(rect)
        ax.text(
            cx, cy, text,
            ha='center', va='center',
            fontsize=11.5, fontfamily=font_family, fontweight='bold',
            color=line_color, zorder=6
        )

    # 3 Top Bones: Man, Machine, Measurement
    man_cx, man_cy = 2.4, 9.3
    man_spine_x, man_spine_y = 3.8, spine_y
    draw_cat_box(man_cx, man_cy, "Man")
    ax.plot([man_cx, man_spine_x], [man_cy - 0.35, man_spine_y], color=line_color, lw=line_width, zorder=2)

    mach_cx, mach_cy = 6.4, 9.3
    mach_spine_x, mach_spine_y = 7.8, spine_y
    draw_cat_box(mach_cx, mach_cy, "Machine")
    ax.plot([mach_cx, mach_spine_x], [mach_cy - 0.35, mach_spine_y], color=line_color, lw=line_width, zorder=2)

    meas_cx, meas_cy = 10.4, 9.3
    meas_spine_x, meas_spine_y = 11.8, spine_y
    draw_cat_box(meas_cx, meas_cy, "Measurement", bw=2.9)
    ax.plot([meas_cx, meas_spine_x], [meas_cy - 0.35, meas_spine_y], color=line_color, lw=line_width, zorder=2)

    # 2 Bottom Bones: Material, Metode
    mat_cx, mat_cy = 3.6, 0.7
    mat_spine_x, mat_spine_y = 5.2, spine_y
    draw_cat_box(mat_cx, mat_cy, "Material")
    ax.plot([mat_cx, mat_spine_x], [mat_cy + 0.35, mat_spine_y], color=line_color, lw=line_width, zorder=2)

    met_cx, met_cy = 9.2, 0.7
    met_spine_x, met_spine_y = 10.8, spine_y
    draw_cat_box(met_cx, met_cy, "Metode")
    ax.plot([met_cx, met_spine_x], [met_cy + 0.35, met_spine_y], color=line_color, lw=line_width, zorder=2)

    def add_sub_branch_top(start_cx, bot_y, sp_x, sp_y, branch_y, text, text_len=3.4):
        intersect_x = start_cx + (branch_y - bot_y) * (sp_x - start_cx) / (sp_y - bot_y)
        left_x = intersect_x - text_len
        ax.plot([left_x, intersect_x], [branch_y, branch_y], color=line_color, lw=1.3, zorder=2)
        wrapped = "\n".join(textwrap.wrap(text, width=34))
        ax.text(
            left_x + 0.05, branch_y + 0.12, wrapped,
            ha='left', va='bottom',
            fontsize=8.0, fontfamily=font_family,
            color=line_color, linespacing=1.2, zorder=4
        )

    def add_sub_branch_bottom(start_cx, top_y, sp_x, sp_y, branch_y, text, text_len=3.7):
        intersect_x = start_cx + (branch_y - top_y) * (sp_x - start_cx) / (sp_y - top_y)
        left_x = intersect_x - text_len
        ax.plot([left_x, intersect_x], [branch_y, branch_y], color=line_color, lw=1.3, zorder=2)
        wrapped = "\n".join(textwrap.wrap(text, width=38))
        ax.text(
            left_x + 0.05, branch_y + 0.12, wrapped,
            ha='left', va='bottom',
            fontsize=8.5, fontfamily=font_family,
            color=line_color, linespacing=1.2, zorder=4
        )

    # Sub-branches
    add_sub_branch_top(man_cx, man_cy - 0.35, man_spine_x, man_spine_y, 7.8, "Pergantian staf administrasi cabang yang sering terjadi menyulitkan pemahaman alur kerja dan pembukuan", text_len=2.8)
    add_sub_branch_top(man_cx, man_cy - 0.35, man_spine_x, man_spine_y, 6.2, "Pimpinan pusat kesulitan mengawasi aktivitas operasional harian di delapan cabang secara serentak", text_len=2.8)

    add_sub_branch_top(mach_cx, mach_cy - 0.35, mach_spine_x, mach_spine_y, 8.0, "Belum adanya sistem informasi manajemen terpusat berbasis web untuk delapan cabang", text_len=3.2)
    add_sub_branch_top(mach_cx, mach_cy - 0.35, mach_spine_x, mach_spine_y, 6.9, "Belum ada modul penjadwalan pendeteksi bentrok jadwal mengajar tentor otomatis", text_len=3.2)
    add_sub_branch_top(mach_cx, mach_cy - 0.35, mach_spine_x, mach_spine_y, 5.8, "Belum ada modul notifikasi pengingat jatuh tempo pembayaran SPP ke WhatsApp", text_len=3.2)

    add_sub_branch_top(meas_cx, meas_cy - 0.35, meas_spine_x, meas_spine_y, 7.6, "Tidak tersedianya dasbor untuk memantau performa pendapatan dan tren siswa aktif antarcabang", text_len=3.2)
    add_sub_branch_top(meas_cx, meas_cy - 0.35, meas_spine_x, meas_spine_y, 6.2, "Ketiadaan indikator visual untuk mengukur distribusi beban jam mengajar tentor lintas cabang", text_len=3.2)

    # Bottom
    add_sub_branch_bottom(mat_cx, mat_cy + 0.35, mat_spine_x, mat_spine_y, 4.2, "Pencatatan pendaftaran siswa dan riwayat pembayaran SPP masih mengandalkan buku kertas A4", text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_cy + 0.35, mat_spine_x, mat_spine_y, 3.3, "Data operasional tersimpan terisolasi di setiap cabang tanpa basis data terpusat (data silo)", text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_cy + 0.35, mat_spine_x, mat_spine_y, 2.4, "Berkas fisik kuitansi dan buku pendaftaran rentan risiko kerusakan, lapuk, basah, atau hilang", text_len=3.7)
    add_sub_branch_bottom(mat_cx, mat_cy + 0.35, mat_spine_x, mat_spine_y, 1.4, "Data profil tempat tinggal siswa belum tercatat lengkap untuk analisis sebaran geografis", text_len=3.7)

    add_sub_branch_bottom(met_cx, met_cy + 0.35, met_spine_x, met_spine_y, 4.0, "Pengendalian kuota kapasitas kelas manual dengan menghitung buku kertas rawan overcapacity", text_len=3.7)
    add_sub_branch_bottom(met_cx, met_cy + 0.35, met_spine_x, met_spine_y, 2.9, "Penagihan SPP manual satu per satu melalui pesan teks WhatsApp pribadi berisiko terlewat", text_len=3.7)
    add_sub_branch_bottom(met_cx, met_cy + 0.35, met_spine_x, met_spine_y, 1.8, "Pencocokan laporan penerimaan kas cabang dan mutasi rekening bank dilakukan manual", text_len=3.7)

    plt.tight_layout()
    plt.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
    plt.savefig(output_path, dpi=300, facecolor='white', bbox_inches='tight')
    plt.close()
    print("5M Fishbone generated successfully at:", output_path)

if __name__ == '__main__':
    out_dir = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA'
    create_fishbone_diagram_4m(os.path.join(out_dir, 'Gambar 1.1 Diagram Fishbone Bimbel Artha.png'))
    create_fishbone_diagram_4m(os.path.join(out_dir, 'Gambar 1.1 Diagram Fishbone Bimbel Artha (4M).png'))
    create_fishbone_diagram_5m(os.path.join(out_dir, 'Gambar 1.1 Diagram Fishbone Bimbel Artha (5M).png'))
