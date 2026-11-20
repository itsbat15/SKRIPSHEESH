import fitz, os

pdf_dir = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF'

pdf_files = [
    '03_Fajriansyah_dkk_2026_JRIS_SINTA3.pdf',
    '15_Tiana_Gunanto_2026_JUKTISI_SINTA4.pdf',
    '05_Zakaria_dkk_2023_JuTISI_SINTA3.pdf',
    '10_Ahadi_dkk_2025_Djtechno_SINTA4.pdf',
    '04_Hendri_dkk_2025_JUSTIAN_SINTA3.pdf',
    '11_Sudirman_Tristianti_2021_MEANS_SINTA4.pdf',
    '12_Khafidhoh_dkk_2026_JTI_SINTA4.pdf',
    '01_Yuanita_dkk_2022_JUTIF_SINTA2.pdf',
    '13_Musofa_dkk_2025_JTIIK_SINTA2.pdf',
    '14_Apriyanti_dkk_2024_JATI_SINTA4.pdf'
]

def make_rc_string(content):
    # Escape XML
    c_xml = content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    lines = c_xml.split('\n')
    formatted_lines = []
    for idx, l in enumerate(lines):
        if idx == 0:
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:10pt;">{l}</span>')
        elif l.startswith('Kategori:'):
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:9.5pt;">{l}</span>')
        elif l.startswith('Kalimat Skripsi ARTHA:'):
            formatted_lines.append(f'<span style="color:#000000;font-weight:bold;font-size:9.5pt;">{l}</span>')
        else:
            formatted_lines.append(f'<span style="color:#000000;font-weight:normal;font-size:9.5pt;">{l}</span>')
    
    body_inner = '<br/>'.join(formatted_lines)
    rc = (
        '<?xml version="1.0"?>'
        '<body xmlns="http://www.w3.org/1999/xhtml" '
        'xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/" '
        'xfa:APIVersion="Acrobat:8.0.0" xfa:spec="2.0.2" '
        'style="font-size:9.5pt;text-align:left;color:#000000;font-weight:normal;font-style:normal;font-family:Helvetica,sans-serif">'
        f'<p dir="ltr">{body_inner}</p>'
        '</body>'
    )
    # Escape parentheses and backslashes for PDF string literal
    rc_pdf = rc.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    return rc_pdf

total_updated = 0

for fname in pdf_files:
    p = os.path.join(pdf_dir, fname)
    doc = fitz.open(p)
    doc_updated = 0
    
    for pno in range(len(doc)):
        page = doc[pno]
        for annot in page.annots():
            stroke = annot.colors.get('stroke')
            # identify green highlight
            if stroke and abs(stroke[0] - 0.1) < 0.05 and abs(stroke[1] - 0.75) < 0.05:
                xref = annot.xref
                content = annot.info.get('content', '')
                
                # 1. Set Default Style DS to pure solid black #000000
                doc.xref_set_key(xref, 'DS', '(font: Helvetica,sans-serif 9.5pt; text-align:left; color:#000000)')
                
                # 2. Set Default Appearance DA to 0 g (black)
                doc.xref_set_key(xref, 'DA', '(/Helv 10 Tf 0 g)')
                
                # 3. Set Rich Content RC with explicit color:#000000
                rc_str = make_rc_string(content)
                doc.xref_set_key(xref, 'RC', f'({rc_str})')
                
                # 4. Check if there is an associated Popup
                popup_xref_str = doc.xref_get_key(xref, 'Popup')
                if popup_xref_str and popup_xref_str[0] == 'xref':
                    try:
                        pxref = int(popup_xref_str[1].split()[0])
                        doc.xref_set_key(pxref, 'C', '[ 1 1 1 ]') # white background
                    except:
                        pass
                
                doc_updated += 1
                total_updated += 1
    
    temp_p = p + '.temp.pdf'
    doc.save(temp_p, deflate=True)
    doc.close()
    os.replace(temp_p, p)
    print(f'Updated {doc_updated} green highlights in {fname} with solid black hover styling')

print(f'\nTotal updated with black hover styling: {total_updated}/40')

