import requests
import requests_cache

requests_cache.install_cache('cache')
cep = input('Digite o CEP: ')

r = requests.get(f'https://cdn.apicep.com/file/apicep/{cep}.json')

endereco = r.json()
print(f'Endereço: {endereco["address"]}, {endereco["district"]}, {endereco["city"]}/{endereco["state"]}')
