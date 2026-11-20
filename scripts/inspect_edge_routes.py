import xml.etree.ElementTree as ET

tree = ET.parse(r'DRAFT PROPOSAL MD\BAB 3\ASET BAB 3\Gambar_3_9_ERD_Konseptual_ARTHA.drawio')
root = tree.getroot()

for c in root.findall('.//mxCell'):
    if c.get('edge') == '1':
        cid = c.get('id')
        style = c.get('style', '')
        geo = c.find('mxGeometry')
        pts = []
        if geo is not None:
            arr = geo.find('Array')
            if arr is not None:
                for pt in arr.findall('mxPoint'):
                    pts.append((pt.get('x'), pt.get('y')))
        print(f"{cid:15} | src={c.get('source'):18} | tgt={c.get('target'):18} | pts={pts}")

