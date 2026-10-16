import os
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urlparse

PAGES = [
    {"name": "Beranda (Home)", "url": "https://bimbelartha.id/"},
    {"name": "Tentang Kami", "url": "https://bimbelartha.id/tentang-kami/"},
    {"name": "Layanan", "url": "https://bimbelartha.id/layanan/"},
    {"name": "Team Pengajar", "url": "https://bimbelartha.id/team-pengajar/"},
    {"name": "Galeri", "url": "https://bimbelartha.id/galeri/"},
    {"name": "Galeri - TK", "url": "https://bimbelartha.id/tk/"},
    {"name": "Galeri - SD", "url": "https://bimbelartha.id/sd/"},
    {"name": "Galeri - SMP", "url": "https://bimbelartha.id/smp/"},
    {"name": "Galeri - SMA", "url": "https://bimbelartha.id/sma/"},
    {"name": "Galeri - Bahasa Inggris", "url": "https://bimbelartha.id/bahasa-inggris/"},
    {"name": "Pendaftaran", "url": "https://bimbelartha.id/pendaftaran/"},
    {"name": "Artikel", "url": "https://bimbelartha.id/artikel/"},
    {"name": "Kontak Kami", "url": "https://bimbelartha.id/kontak-kami/"}
]

OUTPUT_DIR = os.getcwd()
IMAGE_DIR = os.path.join(OUTPUT_DIR, "downloaded_assets", "images")
os.makedirs(IMAGE_DIR, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_html(url):
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def download_image(img_url):
    if not img_url or img_url.startswith("data:"):
        return None
    
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    
    parsed = urlparse(img_url)
    filename = os.path.basename(parsed.path)
    if not filename or '.' not in filename:
        return None
    
    filename = re.sub(r'[^\w\-_\.]', '_', filename)
    local_path = os.path.join(IMAGE_DIR, filename)
    
    rel_path = f"downloaded_assets/images/{filename}"
    if os.path.exists(local_path):
        return rel_path
    
    req = urllib.request.Request(img_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out_file:
            out_file.write(resp.read())
        print(f"Downloaded image: {filename}")
        return rel_path
    except Exception as e:
        print(f"Failed image {img_url}: {e}")
        return img_url

def clean_text(text):
    if not text:
        return ""
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " ".join(lines)

def extract_page_data(page):
    url = page["url"]
    print(f"Processing: {page['name']}")
    html = fetch_html(url)
    if not html:
        return None

    soup = BeautifulSoup(html, 'html.parser')
    
    images = []
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        alt = img.get('alt', '')
        if src and not 'emoji' in src:
            local_img = download_image(src)
            if local_img:
                images.append({"original_url": src, "local_path": local_img, "alt": alt})

    headings = []
    for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        htext = clean_text(h.get_text())
        if htext and len(htext) > 1 and not htext.startswith('{'):
            headings.append({"tag": h.name, "text": htext})
            
    paragraphs = []
    for p in soup.find_all(['p', 'div', 'li']):
        # avoid code/script divs
        if p.find(['script', 'style', 'svg']):
            continue
        ptext = clean_text(p.get_text())
        if ptext and len(ptext) > 10 and not ptext.startswith('/*') and not 'function(' in ptext and not 'window.' in ptext and not 'var ' in ptext:
            if ptext not in paragraphs:
                paragraphs.append(ptext)
            
    return {
        "title": page["name"],
        "url": url,
        "headings": headings,
        "paragraphs": paragraphs,
        "images": images
    }

def main():
    extracted_site = {
        "site_name": "Bimbel Artha Balikpapan",
        "tagline": "Bimbingan Belajar Artha - Balikpapan",
        "menu_structure": {
            "Main Navigation": [
                {"title": "Beranda", "url": "https://bimbelartha.id/"},
                {"title": "Tentang Kami", "url": "https://bimbelartha.id/tentang-kami/"},
                {"title": "Layanan", "url": "https://bimbelartha.id/layanan/"},
                {"title": "Team Pengajar", "url": "https://bimbelartha.id/team-pengajar/"},
                {
                    "title": "Galeri",
                    "url": "https://bimbelartha.id/galeri/",
                    "submenu": [
                        {"title": "TK", "url": "https://bimbelartha.id/tk/"},
                        {"title": "SD", "url": "https://bimbelartha.id/sd/"},
                        {"title": "SMP", "url": "https://bimbelartha.id/smp/"},
                        {"title": "SMA", "url": "https://bimbelartha.id/sma/"},
                        {"title": "Bahasa Inggris", "url": "https://bimbelartha.id/bahasa-inggris/"}
                    ]
                },
                {"title": "Pendaftaran", "url": "https://bimbelartha.id/pendaftaran/"},
                {"title": "Artikel", "url": "https://bimbelartha.id/artikel/"},
                {"title": "Kontak Kami", "url": "https://bimbelartha.id/kontak-kami/"}
            ]
        },
        "pages": []
    }

    for page in PAGES:
        data = extract_page_data(page)
        if data:
            extracted_site["pages"].append(data)

    json_path = os.path.join(OUTPUT_DIR, "website_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(extracted_site, f, ensure_ascii=False, indent=2)

    md_path = os.path.join(OUTPUT_DIR, "WEBSITE_CONTENT.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Dokumentasi Struktur & Konten Website Bimbel Artha Balikpapan\n\n")
        f.write("> **Sumber**: [https://bimbelartha.id/](https://bimbelartha.id/)\n")
        f.write("> **Status Ekstraksi**: Berhasil (Menu, Teks, Submenu, Gambar)\n\n")
        
        f.write("## 1. Struktur Navigasi Menu & Submenu (Sitemap)\n\n")
        for item in extracted_site["menu_structure"]["Main Navigation"]:
            if "submenu" in item:
                f.write(f"- 📁 **{item['title']}** (`{item['url']}`)\n")
                for sub in item["submenu"]:
                    f.write(f"  - 📄 {sub['title']} (`{sub['url']}`)\n")
            else:
                f.write(f"- 📄 **{item['title']}** (`{item['url']}`)\n")
        f.write("\n---\n\n")

        f.write("## 2. Rincian Konten Halaman\n\n")
        for p in extracted_site["pages"]:
            f.write(f"### 🌐 Halaman: {p['title']}\n")
            f.write(f"**URL**: [{p['url']}]({p['url']})\n\n")
            
            f.write("#### 📌 Heading & Sub-heading:\n")
            for h in p["headings"]:
                f.write(f"- `<{h['tag']}>` {h['text']}\n")
            f.write("\n")
            
            f.write("#### 📝 Poin Teks Utama:\n")
            filtered_p = [txt for txt in p["paragraphs"] if len(txt) > 15 and not txt.startswith("©") and not txt.startswith("Menu")]
            for text in filtered_p[:25]:
                f.write(f"- {text}\n")
            f.write("\n")
                
            f.write("#### 🖼️ Gambar / Aset Media:\n")
            seen_imgs = set()
            for img in p["images"]:
                if img['local_path'] not in seen_imgs:
                    seen_imgs.add(img['local_path'])
                    alt_text = img['alt']
                    loc_path = img['local_path']
                    orig_url = img['original_url']
                    f.write(f"- `{loc_path}` ({orig_url}) | Alt: {alt_text}\n")
            f.write("\n---\n\n")

    print("Extraction complete!")

if __name__ == "__main__":
    main()
