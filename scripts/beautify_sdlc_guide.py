import re
import os

file_path = r'c:\Users\ARIEL\OneDrive - MSFT\Documents\ARTHA\KOMPARASI_DAN_JUSTIFIKASI_METODE_SDLC.md'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Format the 12 Image Blocks
def format_image_block(match):
    full = match.group(0)
    m_img = re.search(r'!\[(.*?)\]\((.*?)\)', full)
    alt = m_img.group(1) if m_img else ''
    src = m_img.group(2) if m_img else ''
    
    # Extract figure number, title, source citation, and pdf link
    # Pattern: _Gambar 2.1 Alur ... (Sumber: Royce...; Dokumen PDF: [Royce...](...))_
    m_cap = re.search(r'[_\*]Gambar\s+([0-9\.]+[a-z]?)\s+(.*?)\s*\(Sumber:\s*(.*?);\s*Dokumen PDF:\s*\[(.*?)\]\((.*?)\)\)[_\*]', full)
    if m_cap:
        fig_num = m_cap.group(1)
        fig_title = m_cap.group(2).strip()
        source_cite = m_cap.group(3).strip()
        pdf_label = m_cap.group(4).strip()
        raw_url = m_cap.group(5).strip()
        pdf_url = raw_url.replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './')
        pdf_url = pdf_url.replace('<', '').replace('>', '')
        
        # Clean page label for button, e.g. "hlm. 2"
        page_info = pdf_label.split(',')[-1].strip() if ',' in pdf_label else pdf_label
        
        html_card = (
            f'<p align="center">\n'
            f'  <img src="{src}" alt="{alt}" width="560" style="max-width: 92%; height: auto; border: 1px solid #d0d7de; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); background-color: #ffffff; padding: 6px;" />\n'
            f'  <br>\n'
            f'  <em><b>Gambar {fig_num}</b> {fig_title} (Sumber: {source_cite})</em>\n'
            f'  <br>\n'
            f'  <a href="{pdf_url}">📄 Buka Naskah PDF Sumber ({page_info})</a>\n'
            f'</p>'
        )
        return html_card
    else:
        print('FAILED MATCH ON:', full[:80])
        return full

pattern_img = r'!\[.*?\]\(\./gambar_metode/[^\)]+\)\s*\n[_\*]Gambar[^\n]+\)[_\*]'
text, count_img = re.subn(pattern_img, format_image_block, text)
print(f'Successfully formatted {count_img} image cards.')

# 2. Format Section 1 (Landasan Pustaka) Links
# Look for lines with: Berkas PDF: [...] (...). Berkas Ekstraksi: [...] (...)
def format_sec1_links(match):
    prefix = match.group(1)
    pdf_url = match.group(2).replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './').replace('<', '').replace('>', '')
    txt_url = match.group(3).replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './').replace('<', '').replace('>', '')
    return (
        f'{prefix}<br>\n'
        f'     ↳ <a href="{pdf_url}">📄 Buka Berkas PDF</a> &nbsp;|&nbsp; <a href="{txt_url}">📝 Buka Teks Ekstraksi</a>'
    )

pattern_sec1 = r'(\s*-\s+.*?)\.\s*Berkas PDF:\s*\[.*?\]\((.*?)\)\.\s*Berkas Ekstraksi:\s*\[.*?\]\((.*?)\)\.'
text, count_sec1 = re.subn(pattern_sec1, format_sec1_links, text)
print(f'Formatted {count_sec1} items in Section 1.')

# 3. Format Section 6 (Daftar Pustaka) Links
# Pattern: - Author... Berkas PDF: [Label](URL). Berkas Ekstraksi: [Label](URL).
def format_sec6_links(match):
    prefix = match.group(1)
    pdf_url = match.group(2).replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './').replace('<', '').replace('>', '')
    txt_url = match.group(3).replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './').replace('<', '').replace('>', '')
    return (
        f'{prefix}<br>\n'
        f'  ↳ <a href="{pdf_url}">📄 Berkas PDF</a> &nbsp;|&nbsp; <a href="{txt_url}">📝 Teks Ekstraksi</a>'
    )

pattern_sec6 = r'(\s*-\s+.*?)\.\s*Berkas PDF:\s*\[.*?\]\((.*?)\)\.\s*Berkas Ekstraksi:\s*\[.*?\]\((.*?)\)\.'
text, count_sec6 = re.subn(pattern_sec6, format_sec6_links, text)
print(f'Formatted {count_sec6} items in Section 6.')

# 4. Check for any leftover file:/// in the text and replace them with ./
leftover_file_urls = re.findall(r'file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/([^\)\s>\"\'<]+)', text)
print(f'Remaining file:/// URLs to replace: {len(leftover_file_urls)}')
text = text.replace('file:///c:/Users/ARIEL/OneDrive%20-%20MSFT/Documents/ARTHA/', './')

# 5. Write back to file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated KOMPARASI_DAN_JUSTIFIKASI_METODE_SDLC.md successfully!')
