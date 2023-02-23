import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')
req = requests.get('https://www.reddit.com/r/destiny2/')
soup = BeautifulSoup(req.text, 'html.parser')

links = soup.find_all('a')

for link in links:
    print(link.get('href'))
    