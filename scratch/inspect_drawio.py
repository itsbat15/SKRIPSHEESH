import xml.etree.ElementTree as ET

def inspect(filepath):
    print("=" * 60)
    print("INSPECTING:", filepath)
    tree = ET.parse(filepath)
    for el in tree.getroot().findall('.//mxCell'):
        val = el.attrib.get('value', '')
        cid = el.attrib.get('id', '')
        edge = el.attrib.get('edge', '')
        src = el.attrib.get('source', '')
        tgt = el.attrib.get('target', '')
        if edge == '1':
            print(f"  [FLOW] {cid}: {src} -> {tgt} ({val})")
        elif val:
            # clean html tags for display
            clean_val = val.replace('<br>', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"')
            print(f"  [NODE] {cid}: {clean_val[:60]}")

inspect('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/Gambar_3_1_BPMN_As_Is_ARTHA.drawio')
inspect('DRAFT PROPOSAL MD/BAB 3/ASET BAB 3/Gambar_3_2_BPMN_To_Be_ARTHA.drawio')

