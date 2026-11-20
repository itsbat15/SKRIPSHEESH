
import urllib.request
from bs4 import BeautifulSoup

def get_images(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            for img in soup.find_all('img'):
                src = img.get('src')
                if src and ('diagram' in src or 'tier' in src or 'architecture' in src or 'c4' in src):
                    print(url, '-->', src)
    except Exception as e:
        print(url, '--> Error:', e)

get_images('https://c4model.com/')
get_images('https://en.wikipedia.org/wiki/Multitier_architecture')
get_images('https://www.digitalocean.com/community/conceptual-articles/5-common-server-setups-for-your-web-application')
