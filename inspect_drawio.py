import xml.etree.ElementTree as ET

tree = ET.parse('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/ARTHA_Semua_Diagram_UML_Bab3.drawio')
root = tree.getroot()

for diag in root.findall('diagram'):
    name = diag.get('name')
    print(f"==================================================")
    print(f"PAGE: {name}")
    print(f"==================================================")
    model = diag.find('mxGraphModel')
    root_cell = model.find('root')
    cells = root_cell.findall('mxCell')
    print(f"Total elements: {len(cells)}")
    for c in cells:
        val = c.get('value', '')
        cid = c.get('id', '')
        edge = c.get('edge', '')
        src = c.get('source', '')
        tgt = c.get('target', '')
        style = c.get('style', '')
        geo = c.find('mxGeometry')
        pos_str = ""
        if geo is not None:
            pos_str = f"(x={geo.get('x')}, y={geo.get('y')}, w={geo.get('width')}, h={geo.get('height')})"
        
        if val:
            clean_val = val.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('<br>', ' ').replace('<b>', '').replace('</b>', '').replace('&laquo;', '<<').replace('&raquo;', '>>')
            print(f"  [{cid}] {pos_str} Text: '{clean_val.strip()}'")
        elif edge:
            print(f"  [EDGE {cid}] {src} --> {tgt}")

