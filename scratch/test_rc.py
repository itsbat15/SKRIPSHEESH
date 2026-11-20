import fitz

doc = fitz.open(r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\JURNAL\36_REFERENSI_PDF\03_Fajriansyah_dkk_2026_JRIS_SINTA3.pdf')
page = doc[0]
for annot in page.annots():
    stroke = annot.colors.get('stroke')
    if stroke and abs(stroke[0] - 0.1) < 0.05:
        xref = annot.xref
        doc.xref_set_key(xref, 'DS', '(font: Helvetica,sans-serif 10.0pt; text-align:left; color:#000000)')
        doc.xref_set_key(xref, 'DA', '(/Helv 10 Tf 0 g)')
        content_html = annot.info['content'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>')
        rc_text = f'<?xml version="1.0"?><body xmlns="http://www.w3.org/1999/xhtml" xmlns:xfa="http://www.xfa.org/schema/xfa-data/1.0/" xfa:APIVersion="Acrobat:8.0.0" xfa:spec="2.0.2" style="font-size:10.0pt;text-align:left;color:#000000;font-weight:normal;font-style:normal;font-family:Helvetica,sans-serif"><p dir="ltr">{content_html}</p></body>'
        # in PDF, strings in parentheses need escaping of ( and )
        rc_escaped = rc_text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        doc.xref_set_key(xref, 'RC', f'({rc_escaped})')
        print('Successfully set DS, DA, RC on xref', xref)
        print('New XREF:', doc.xref_object(xref)[:400])
        break

