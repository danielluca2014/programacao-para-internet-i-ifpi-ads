import requests
import requests_cache
from bs4 import BeautifulSoup
import pandas as pd

requests_cache.install_cache('cache')
r = requests.get('https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/')

soup = BeautifulSoup(r.content, 'html.parser')
table = soup.find('table')
table_str = str(table)

df = pd.read_html(table_str)[0]
print(df)
