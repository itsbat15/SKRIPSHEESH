import xml.etree.ElementTree as ET

tree = ET.parse(r'DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.drawio')
root = tree.getroot()

nodes = {}
for c in root.findall('.//mxCell'):
    if c.get('vertex') == '1':
        cid = c.get('id')
        geo = c.find('mxGeometry')
        if geo is not None:
            nodes[cid] = {
                'val': c.get('value', ''),
                'x': float(geo.get('x', 0)),
                'y': float(geo.get('y', 0)),
                'w': float(geo.get('width', 0)),
                'h': float(geo.get('height', 0)),
                'cx': float(geo.get('x', 0)) + float(geo.get('width', 0))/2,
                'cy': float(geo.get('y', 0)) + float(geo.get('height', 0))/2,
            }

for c in root.findall('.//mxCell'):
    if c.get('edge') == '1':
        cid = c.get('id')
        src = c.get('source')
        tgt = c.get('target')
        src_n = nodes.get(src, {})
        tgt_n = nodes.get(tgt, {})
        if src_n and tgt_n:
            dx = abs(src_n['cx'] - tgt_n['cx'])
            dy = abs(src_n['cy'] - tgt_n['cy'])
            style = c.get('style', '')
            print(f"{cid:15} | {src:18} ({src_n['cx']:6.1f}, {src_n['cy']:6.1f}) -> {tgt:18} ({tgt_n['cx']:6.1f}, {tgt_n['cy']:6.1f}) | dx={dx:6.1f}, dy={dy:6.1f}")

