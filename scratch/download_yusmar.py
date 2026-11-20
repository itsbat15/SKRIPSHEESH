import urllib.request
import ssl
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

# 1. Yusmar et al. (2023)
urls = [
    'https://jtiik.ub.ac.id/index.php/jtiik/article/download/7237/pdf',
    'https://jtiik.ub.ac.id/index.php/jtiik/article/view/7237',
    'https://doi.org/10.25126/jtiik.2023107237'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content_type = resp.headers.get('Content-Type')
            content_len = resp.headers.get('Content-Length')
            final_url = resp.geturl()
            print(f"URL: {url} -> Status: {resp.status}, Content-Type: {content_type}, Length: {content_len}, Final: {final_url}")
            if 'pdf' in str(content_type).lower():
                data = resp.read()
                out_path = 'JURNAL/36_REFERENSI_PDF/Yusmar_dkk_2023_JTIIK_SINTA2_BPMN_Agrowing.pdf'
                with open(out_path, 'wb') as f:
                    f.write(data)
                print(f"SAVED PDF TO {out_path} ({len(data)} bytes)")
                break
    except Exception as e:
        print(f"Error for {url}: {e}")

