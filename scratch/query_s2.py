import urllib.request
import json

url = 'https://api.semanticscholar.org/graph/v1/paper/10.25126/jtiik.2023107237?fields=title,authors,year,abstract,openAccessPdf,externalIds'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(json.dumps(data, indent=2))
except Exception as e:
    print("Error:", e)

