import urllib.request
import re

url = 'https://repository.ipb.ac.id/handle/123456789/123653'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        print("Status:", resp.status, "HTML len:", len(html))
        # find bitstream pdf links
        bitstreams = re.findall(r'href=[\"\'](/bitstream/[^\"\']+)[\"\']', html)
        for b in set(bitstreams):
            print("Bitstream:", b)
except Exception as e:
    print("Error:", e)

