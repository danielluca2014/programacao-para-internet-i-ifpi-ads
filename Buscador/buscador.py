import re
import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache("cache")

try:
    def search(keyword, url, depth):
        response = requests.get(url)
        html = BeautifulSoup(response.content, 'html.parser')
        text = html.get_text()

        results = None

        if keyword in text:
            results = re.findall(f'.{{0,20}}{keyword}.{{0,20}}', text)
        
        if depth > 0:
            links = html.find_all('a')
            for link in links:
                next_url = link.get('href')
                if next_url.startswith('https'):
                    search_result = search(keyword, next_url, depth - 1)
                    if search_result:
                        results = search_result

        return results

    results = search('audit', 'https://www.reddit.com/?feed=home', 1)

    for result in results:
        print(result)

except:
    print('Erro: Palavra chave não encontrada')
    