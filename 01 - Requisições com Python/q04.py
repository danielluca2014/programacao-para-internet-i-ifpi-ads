import requests
import requests_cache

requests_cache.install_cache('cache')
r = requests.get('https://cdn.mos.cms.futurecdn.net/Y4GuDCyS2HcACXMLTSyCgS-970-80.jpg.webp')

with open('cayde6.jpeg', 'wb') as file:
    file.write(r.content)
    