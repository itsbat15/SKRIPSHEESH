"""
build_neat_drawio.py
====================
Builds the clean, aligned, orthogonal Draw.io XML for Gambar 3.9 ERD Konseptual ARTHA.
"""

import xml.etree.ElementTree as ET
import os

def generate_drawio():
    mxfile = ET.Element("mxfile", {
        "host": "Electron",
        "modified": "2026-11-11T11:40:00.000Z",
        "agent": "Antigravity/2.0 (Windows NT 10.0; Win64; x64)",
        "version": "21.6.8",
        "type": "device"
    })
    
    diagram = ET.SubElement(mxfile, "diagram", {
        "id": "diag_chen_konseptual",
        "name": "Gambar 3.9 ERD Konseptual Notasi Chen (Entitas & Kardinalitas)"
    })
    
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", {
        "dx": "1422",
        "dy": "794",
        "grid": "1",
        "gridSize": "10",
        "guides": "1",
        "tooltips": "1",
        "connect": "1",
        "arrows": "1",
        "fold": "1",
        "page": "1",
        "pageScale": "1",
        "pageWidth": "1920",
        "pageHeight": "1080",
        "math": "0",
        "shadow": "0"
    })
    
    root = ET.SubElement(mxGraphModel, "root")
    
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})
    
    # Styles
    style_title = "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;"
    style_legend = "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=0;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#FAFAFA;strokeColor=#000000;strokeWidth=1;"
    style_ent = "rounded=0;whiteSpace=wrap;html=1;fontStyle=1;strokeWidth=1.5;fillColor=#ffffff;strokeColor=#000000;fontSize=13;"
    style_rel = "rhombus;whiteSpace=wrap;html=1;fontStyle=1;strokeWidth=1.5;fillColor=#ffffff;strokeColor=#000000;fontSize=12;"
    style_edge = "endArrow=none;html=1;rounded=0;strokeWidth=1.5;strokeColor=#000000;"
    style_card = "text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=#ffffff;fontStyle=1;fontSize=12;"
    
    # Title
    c_title = ET.SubElement(root, "mxCell", {
        "id": "title",
        "value": '<b>Entity Relationship Diagram (ERD) - Notasi Peter Chen</b><br><font color="#555555">Pemodelan Konseptual Basis Data Relasional Sistem Informasi ARTHA (Entitas, Relasi, dan Kardinalitas)</font>',
        "style": style_title,
        "vertex": "1",
        "parent": "1"
    })
    geo = ET.SubElement(c_title, "mxGeometry", {"x": "50", "y": "25", "width": "650", "height": "40", "as": "geometry"})
    
    # Legend
    c_legend = ET.SubElement(root, "mxCell", {
        "id": "legend",
        "value": "<b>Standar Notasi Peter Chen (1976):</b>&nbsp;&nbsp; [ Persegi Panjang ] = Entitas &nbsp;|&nbsp; &lt; Belah Ketupat &gt; = Relasi &nbsp;|&nbsp; 1 / N = Rasio Kardinalitas",
        "style": "text;html=1;strokeColor=#000000;fillColor=#FAFAFA;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=4;fontSize=11;strokeWidth=1;",
        "vertex": "1",
        "parent": "1"
    })
    geo = ET.SubElement(c_legend, "mxGeometry", {"x": "1000", "y": "25", "width": "770", "height": "40", "as": "geometry"})

    # 10 ENTITIES
    # (id, name, cx, cy, w, h)
    entities = [
        ('ent_branches',        '<b>branches</b>',              620,  180, 140, 45),
        ('ent_study_groups',    '<b>study_groups</b>',          1060, 180, 140, 45),
        ('ent_course_packages', '<b>course_packages</b>',       1520, 180, 150, 45),
        ('ent_users',           '<b>users</b>',                 240,  420, 140, 45),
        ('ent_students',        '<b>students</b>',              620,  420, 140, 45),
        ('ent_enrollments',     '<b>enrollments</b>',           1060, 420, 140, 45),
        ('ent_daily_rec',       '<b>daily_reconciliations</b>', 240,  660, 170, 45),
        ('ent_tuition_bills',   '<b>tuition_bills</b>',         1060, 660, 140, 45),
        ('ent_payments',        '<b>payments</b>',              1520, 660, 140, 45),
        ('ent_payment_proofs',  '<b>payment_proofs</b>',        1520, 900, 150, 45),
    ]
    
    for eid, name, cx, cy, w, h in entities:
        c = ET.SubElement(root, "mxCell", {
            "id": eid,
            "value": name,
            "style": style_ent,
            "vertex": "1",
            "parent": "1"
        })
        ET.SubElement(c, "mxGeometry", {
            "x": str(cx - w/2),
            "y": str(cy - h/2),
            "width": str(w),
            "height": str(h),
            "as": "geometry"
        })

    # 14 RELATIONSHIPS
    relationships = [
        ('rel_mengelola',    'Mengelola',    840,  180, 110, 50),
        ('rel_memiliki',     'Memiliki',     430,  300, 110, 50),
        ('rel_menaungi',     'Menaungi',     620,  300, 110, 50),
        ('rel_ditempati',    'Ditempati',    1060, 300, 110, 50),
        ('rel_ditawarkan',   'Ditawarkan',   1290, 300, 110, 50),
        ('rel_mengambil',    'Mengambil',    840,  420, 110, 50),
        ('rel_melakukan',    'Melakukan',    240,  540, 110, 50),
        ('rel_menerbitkan',  'Menerbitkan',  1060, 540, 115, 50),
        ('rel_melayani',     'Melayani',     1360, 540, 110, 50),
        ('rel_diselesaikan', 'Diselesaikan', 1290, 660, 115, 50),
        ('rel_melampirkan',  'Melampirkan',  1520, 780, 115, 50),
        ('rel_memvalidasi',  'Memvalidasi',  1220, 900, 110, 50),
        ('rel_mengadakan',   'Mengadakan',   80,   420, 110, 50),
        ('rel_menerima',     'Menerima',     1720, 420, 110, 50),
    ]

    for rid, name, cx, cy, w, h in relationships:
        c = ET.SubElement(root, "mxCell", {
            "id": rid,
            "value": name,
            "style": style_rel,
            "vertex": "1",
            "parent": "1"
        })
        ET.SubElement(c, "mxGeometry", {
            "x": str(cx - w/2),
            "y": str(cy - h/2),
            "width": str(w),
            "height": str(h),
            "as": "geometry"
        })

    # Helper to add edge with optional waypoints and cardinalities
    def add_rel_edges(edge1_id, edge2_id, ent_src, rel, ent_tgt, card1, card2, pts1=None, pts2=None, pos1=-0.4, pos2=0.4, orthogonal=False):
        st1 = "edgeStyle=orthogonalEdgeStyle;" + style_edge if orthogonal else style_edge
        st2 = "edgeStyle=orthogonalEdgeStyle;" + style_edge if orthogonal else style_edge
        # Edge 1: ent_src -> rel
        e1 = ET.SubElement(root, "mxCell", {
            "id": edge1_id,
            "style": st1,
            "edge": "1",
            "source": ent_src,
            "target": rel,
            "parent": "1"
        })
        geo1 = ET.SubElement(e1, "mxGeometry", {"relative": "1", "as": "geometry"})
        if pts1:
            arr = ET.SubElement(geo1, "Array", {"as": "points"})
            for px, py in pts1:
                ET.SubElement(arr, "mxPoint", {"x": str(px), "y": str(py)})
                
        # Card 1 label
        lbl1 = ET.SubElement(root, "mxCell", {
            "id": f"lbl_{edge1_id}",
            "value": card1,
            "style": style_card,
            "vertex": "1",
            "connectable": "0",
            "parent": edge1_id
        })
        ET.SubElement(lbl1, "mxGeometry", {"x": str(pos1), "y": "0", "relative": "1", "as": "geometry"})

        # Edge 2: rel -> ent_tgt
        e2 = ET.SubElement(root, "mxCell", {
            "id": edge2_id,
            "style": st2,
            "edge": "1",
            "source": rel,
            "target": ent_tgt,
            "parent": "1"
        })
        geo2 = ET.SubElement(e2, "mxGeometry", {"relative": "1", "as": "geometry"})
        if pts2:
            arr = ET.SubElement(geo2, "Array", {"as": "points"})
            for px, py in pts2:
                ET.SubElement(arr, "mxPoint", {"x": str(px), "y": str(py)})

        # Card 2 label
        lbl2 = ET.SubElement(root, "mxCell", {
            "id": f"lbl_{edge2_id}",
            "value": card2,
            "style": style_card,
            "vertex": "1",
            "connectable": "0",
            "parent": edge2_id
        })
        ET.SubElement(lbl2, "mxGeometry", {"x": str(pos2), "y": "0", "relative": "1", "as": "geometry"})

    # 1. Mengelola (branches -> study_groups) HORIZONTAL
    add_rel_edges("edge_br_mgl", "edge_mgl_sg", "ent_branches", "rel_mengelola", "ent_study_groups", "1", "N")

    # 2. Menaungi (branches -> students) VERTICAL
    add_rel_edges("edge_br_mng", "edge_mng_st", "ent_branches", "rel_menaungi", "ent_students", "1", "N")

    # 3. Ditempati (study_groups -> enrollments) VERTICAL
    add_rel_edges("edge_sg_dtp", "edge_dtp_en", "ent_study_groups", "rel_ditempati", "ent_enrollments", "1", "N")

    # 4. Mengambil (students -> enrollments) HORIZONTAL
    add_rel_edges("edge_st_mgb", "edge_mgb_en", "ent_students", "rel_mengambil", "ent_enrollments", "1", "N")

    # 5. Menerbitkan (enrollments -> tuition_bills) VERTICAL
    add_rel_edges("edge_en_mnb", "edge_mnb_tb", "ent_enrollments", "rel_menerbitkan", "ent_tuition_bills", "1", "N")

    # 6. Diselesaikan (tuition_bills -> payments) HORIZONTAL
    add_rel_edges("edge_tb_dsl", "edge_dsl_pay", "ent_tuition_bills", "rel_diselesaikan", "ent_payments", "1", "N")

    # 7. Melampirkan (payments -> payment_proofs) VERTICAL
    add_rel_edges("edge_pay_mlp", "edge_mlp_pp", "ent_payments", "rel_melampirkan", "ent_payment_proofs", "1", "1")

    # 8. Melakukan (users -> daily_reconciliations) VERTICAL
    add_rel_edges("edge_usr_mlk", "edge_mlk_dr", "ent_users", "rel_melakukan", "ent_daily_rec", "1", "N")

    # 9. Memiliki (branches -> users) DIAGONAL SYMMETRIC
    add_rel_edges("edge_br_mem", "edge_mem_usr", "ent_branches", "rel_memiliki", "ent_users", "1", "N")

    # 10. Ditawarkan (course_packages -> enrollments) DIAGONAL SYMMETRIC
    add_rel_edges("edge_cp_dtw", "edge_dtw_en", "ent_course_packages", "rel_ditawarkan", "ent_enrollments", "1", "N")

    # 11. Mengadakan (branches -> daily_rec) PERIMETER LEFT
    add_rel_edges("edge_br_mgd", "edge_mgd_dr", "ent_branches", "rel_mengadakan", "ent_daily_rec", "1", "N",
                  pts1=[(620, 95), (80, 95)],
                  pts2=[(80, 660)],
                  pos1=-0.8, pos2=0.7,
                  orthogonal=True)

    # 12. Menerima (branches -> payments) PERIMETER RIGHT
    add_rel_edges("edge_br_mnr", "edge_mnr_pay", "ent_branches", "rel_menerima", "ent_payments", "1", "N",
                  pts1=[(620, 95), (1720, 95)],
                  pts2=[(1720, 660)],
                  pos1=-0.8, pos2=0.7,
                  orthogonal=True)

    # 13. Melayani (users -> payments) ORTHOGONAL
    add_rel_edges("edge_usr_mly", "edge_mly_pay", "ent_users", "rel_melayani", "ent_payments", "1", "N",
                  pts1=[(360, 435), (360, 540)],
                  pts2=[(1440, 540), (1440, 638)],
                  pos1=-0.7, pos2=0.7,
                  orthogonal=True)

    # 14. Memvalidasi (users -> payment_proofs) BOTTOM ORTHOGONAL
    add_rel_edges("edge_usr_mvl", "edge_mvl_pp", "ent_users", "rel_memvalidasi", "ent_payment_proofs", "1", "N",
                  pts1=[(240, 900)],
                  pts2=[],
                  pos1=-0.6, pos2=0.6,
                  orthogonal=True)

    # Write files
    tree = ET.ElementTree(mxfile)
    dst_aset = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.drawio"
    dst_drawio = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.drawio"
    
    tree.write(dst_aset, encoding="utf-8", xml_declaration=True)
    tree.write(dst_drawio, encoding="utf-8", xml_declaration=True)
    print(f"Saved draw.io to:\n - {dst_aset}\n - {dst_drawio}")

    # Also update DIAGRAM SKRIPSI.drawio
    master_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\DIAGRAM SKRIPSI.drawio"
    if os.path.exists(master_path):
        m_tree = ET.parse(master_path)
        m_root = m_tree.getroot()
        # Find if diag_chen_konseptual exists, replace or append
        existing = m_root.find(".//diagram[@id='diag_chen_konseptual']")
        if existing is not None:
            m_root.remove(existing)
        m_root.append(diagram)
        m_tree.write(master_path, encoding="utf-8", xml_declaration=True)
        print(f"Updated page 'diag_chen_konseptual' in master {master_path}")

if __name__ == "__main__":
    generate_drawio()
