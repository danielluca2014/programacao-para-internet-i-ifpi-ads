import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')
req = requests.get('https://www.w3schools.com/python/module_requests.asp')
soup = BeautifulSoup(req.text, 'html.parser')

input_tag = input('Tag: ')
tags = soup.find_all(input_tag)

for tag in tags:
    print(tag.text)
