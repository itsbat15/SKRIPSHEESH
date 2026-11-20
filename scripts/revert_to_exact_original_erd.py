"""
revert_to_exact_original_erd.py
===============================
Takes Gambar_3_9_ERD_Chen_ARTHA_Lengkap_Atribut.drawio (the exact source of the user's image)
and removes ONLY:
- 63 attribute ellipse cells
- 63 attribute connector edges
Preserves:
- All 10 entities exactly as they are in the image
- All 14 relationships exactly as they are in the image
- All 28 relationship edges with exact waypoints, exit/entry points as in the image
- All 28 cardinality labels
- Title and legend
"""

import xml.etree.ElementTree as ET
import os

SRC_PATH = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA_Lengkap_Atribut.drawio"

TARGETS = [
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Chen_ARTHA.drawio",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.drawio",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Konseptual_ARTHA.drawio",
    r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\Gambar_3_9_ERD_Chen_ARTHA.drawio",
]

tree = ET.parse(SRC_PATH)
root = tree.getroot()

# 1. Identify attribute ellipses
att_ids = set()
for c in root.findall(".//mxCell"):
    style = c.get("style", "")
    if "ellipse" in style:
        att_ids.add(c.get("id"))

# 2. Identify edges connecting to attributes
att_edges = set()
for c in root.findall(".//mxCell"):
    if c.get("edge") == "1":
        src = c.get("source", "")
        tgt = c.get("target", "")
        if src in att_ids or tgt in att_ids:
            att_edges.add(c.get("id"))

print(f"Attribute ellipses to remove: {len(att_ids)}")
print(f"Attribute edges to remove: {len(att_edges)}")

# 3. Remove them from root model
model = root.find(".//root")
removed_count = 0
for c in list(model.findall("mxCell")):
    cid = c.get("id", "")
    if cid in att_ids or cid in att_edges:
        model.remove(c)
        removed_count += 1

print(f"Total elements removed: {removed_count}")

# 4. Count remaining elements
remaining_cells = model.findall("mxCell")
vertices = [c for c in remaining_cells if c.get("vertex") == "1"]
edges = [c for c in remaining_cells if c.get("edge") == "1"]
print(f"Remaining total cells: {len(remaining_cells)}")
print(f"Remaining vertices: {len(vertices)} (10 entities, 14 relations, 28 card labels, 1 title, 1 legend)")
print(f"Remaining edges: {len(edges)} (28 relationship edges)")

# Update Legend text to reflect no-attribute Peter Chen standard
for c in model.findall("mxCell"):
    cid = c.get("id", "")
    if cid == "legend":
        c.set("value", '<b>Standar Notasi Peter Chen (1976):</b>&nbsp;&nbsp; [ Persegi Panjang ] = Entitas &nbsp;|&nbsp; &lt; Belah Ketupat &gt; = Relasi &nbsp;|&nbsp; 1 / N = Rasio Kardinalitas')

# Save to all target files
for t in TARGETS:
    os.makedirs(os.path.dirname(t), exist_ok=True)
    tree.write(t, encoding="utf-8", xml_declaration=True)
    print(f"Successfully wrote exact original ERD without attributes to: {t}")

# Also update DIAGRAM SKRIPSI.drawio
master_path = r"c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\DRAFT PROPOSAL MD\DRAW IO\DIAGRAM SKRIPSI.drawio"
if os.path.exists(master_path):
    m_tree = ET.parse(master_path)
    m_root = m_tree.getroot()
    # Find if diag_chen_konseptual exists, replace or append
    existing = m_root.find(".//diagram[@id='diag_chen_konseptual']")
    if existing is not None:
        m_root.remove(existing)
    
    diag = root.find(".//diagram")
    if diag is not None:
        diag.set("id", "diag_chen_konseptual")
        diag.set("name", "Gambar 3.9 ERD Konseptual Notasi Chen (Entitas & Kardinalitas)")
        m_root.append(diag)
        m_tree.write(master_path, encoding="utf-8", xml_declaration=True)
        print(f"Updated page 'diag_chen_konseptual' in master {master_path}")

