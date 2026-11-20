"""
generate_erd_konseptual.py
===========================
Membuat diagram ERD konseptual ARTHA Notasi Peter Chen (Entitas & Kardinalitas)
tanpa atribut, sesuai arahan Pak Arif pada bimbingan tugas akhir.
Sumber referensi: Gambar_3_9_ERD_Chen_ARTHA.drawio
Target output:
1. DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/Gambar_3_9_ERD_Konseptual_ARTHA.drawio
2. DRAFT PROPOSAL MD/DRAW IO/Gambar_3_9_ERD_Konseptual_ARTHA.drawio
"""

import xml.etree.ElementTree as ET
import os

SRC_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.drawio"
BACKUP_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA_Lengkap_Atribut.drawio"
DST_ASET = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.drawio"
DST_DRAWIO = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.drawio"

def main():
    if not os.path.exists(SRC_PATH):
        print(f"Error: file sumber tidak ditemukan: {SRC_PATH}")
        return

    # Backup versi lengkap dengan atribut
    if not os.path.exists(BACKUP_PATH):
        with open(SRC_PATH, "r", encoding="utf-8") as f_src:
            with open(BACKUP_PATH, "w", encoding="utf-8") as f_bak:
                f_bak.write(f_src.read())
        print(f"Backup versi lengkap tersimpan di: {BACKUP_PATH}")

    tree = ET.parse(SRC_PATH)
    root = tree.getroot()

    # 1. Kumpulkan seluruh ID atribut (elemen elips)
    att_ids = set()
    for c in root.findall(".//mxCell"):
        style = c.get("style", "")
        if "ellipse" in style:
            att_ids.add(c.get("id"))

    # 2. Kumpulkan seluruh ID garis yang terhubung ke atribut
    att_edges = set()
    for c in root.findall(".//mxCell"):
        if c.get("edge") == "1":
            src = c.get("source", "")
            tgt = c.get("target", "")
            if src in att_ids or tgt in att_ids:
                att_edges.add(c.get("id"))

    # 3. Hapus sel atribut dan garis atribut dari root
    model = root.find(".//root")
    removed_count = 0
    for c in list(model.findall("mxCell")):
        cid = c.get("id", "")
        if cid in att_ids or cid in att_edges:
            model.remove(c)
            removed_count += 1

    print(f"Total elemen atribut dihapus: {removed_count} (63 elips atribut + 63 garis penghubung).")
    print(f"Sisa elemen utama (Entitas, Relasi, Garis & Kardinalitas): {len(model.findall('mxCell'))}.")

    # 4. Perbarui Title dan Legend agar sesuai dengan diagram konseptual
    for c in model.findall("mxCell"):
        cid = c.get("id", "")
        if cid == "title":
            c.set("value", '&lt;b style="font-size: 17px;"&gt;Entity Relationship Diagram (ERD) - Notasi Peter Chen&lt;/b&gt;&lt;br&gt;&lt;font color="#555555"&gt;Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA (Entitas, Relasi, dan Kardinalitas)&lt;/font&gt;')
        elif cid == "legend":
            c.set("value", '&lt;b&gt;Standar Notasi Peter Chen (1976):&lt;/b&gt;&amp;nbsp;&amp;nbsp; [ Persegi Panjang ] = Entitas &amp;nbsp;|&amp;nbsp; &amp;lt; Belah Ketupat &amp;gt; = Relasi &amp;nbsp;|&amp;nbsp; 1 / N = Rasio Kardinalitas')

    # 5. Perbarui nama diagram
    diag = root.find(".//diagram")
    if diag is not None:
        diag.set("name", "Gambar 3.9 ERD Konseptual Notasi Chen (Entitas & Kardinalitas)")

    # 6. Simpan ke berkas target
    tree.write(DST_ASET, encoding="utf-8", xml_declaration=True)
    tree.write(DST_DRAWIO, encoding="utf-8", xml_declaration=True)
    print(f"Berhasil membuat berkas draw.io konseptual di:\n - {DST_ASET}\n - {DST_DRAWIO}")

if __name__ == "__main__":
    main()

