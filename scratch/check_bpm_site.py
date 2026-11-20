import urllib.request
import re

url = 'http://fundamentals-of-bpm.org/'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Status:", resp.status, "HTML len:", len(html))
        # Find links
        links = re.findall(r'href=[\"\']([^\"\']+)[\"\']', html)
        for l in links:
            if 'pdf' in l.lower() or 'chapter' in l.lower() or 'slide' in l.lower() or 'material' in l.lower():
                print("Link:", l)
except Exception as e:
    print("Error:", e)

