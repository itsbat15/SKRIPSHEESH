import urllib.request

url = 'https://repository.ipb.ac.id/bitstream/handle/123456789/123653/Draft%20Tesis%20Addini%20Yusmar%20G6501202048%20Fullteks.pdf'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        print("Status:", resp.status, "Length:", resp.headers.get('Content-Length'), "Content-Type:", resp.headers.get('Content-Type'))
        data = resp.read()
        print("Read bytes:", len(data))
        with open('scratch/yusmar_ipb_fullteks.pdf', 'wb') as f:
            f.write(data)
        print("Saved successfully!")
except Exception as e:
    print("Error:", e)

