import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')
q = input('Digite o termo a ser buscado: ')

r = requests.get(f'http://www.google.com/search?q={q}')
print(f'URL: {r.url}')

soup = BeautifulSoup(r.text, 'html.parser')
headers = soup.find_all('h3')

for header in headers:
    texto = header.get_text()
    print(" - ", texto)
