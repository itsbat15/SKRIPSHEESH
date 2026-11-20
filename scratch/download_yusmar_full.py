import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

opener = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=ctx),
    urllib.request.HTTPCookieProcessor()
)
opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'),
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'),
    ('Accept-Language', 'en-US,en;q=0.9,id;q=0.8')
]

url = 'https://jtiik.ub.ac.id/index.php/jtiik/en/article/view/7237'
try:
    resp = opener.open(url, timeout=15)
    html = resp.read().decode('utf-8', errors='ignore')
    print('Status:', resp.status, 'HTML length:', len(html))
    with open('scratch/jtiik_page.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    # find links
    links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', html)
    print("Total links found:", len(links))
    pdf_links = [l for l in links if 'pdf' in l.lower() or 'download' in l.lower() or '7237' in l]
    for l in pdf_links:
        print('Matching link:', l)
except Exception as e:
    print('Error:', e)

