import requests
import requests_cache
import re
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')
r = requests.get('https://pt.wikipedia.org/wiki/Terraria')
soup = BeautifulSoup(r.text, 'html.parser')
texto = soup.get_text()

termo = input('Digite o termo procurado: ')

resultados = re.findall(f'.{{0,20}}{termo}.{{0,20}}', texto)

for resultado in resultados:
    print(resultado)
