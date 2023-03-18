import re
import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('cache')

def main(): 
    print('Seja bem vindo ao Buscador de links!\n')
    opcao = 1
    
    while(opcao != 0):
        url = 'https://www.reddit.com/'

        print(f'\nSite de busca atual: {url}')

        keyword = input('Palavra chave: ')
        depth = int(input('Profundidade: '))

        print('\nBuscando resultados...\n')
    
        resultados = search(keyword, url, depth)

        if resultados:
            for resultado in resultados:
                print(f'URL: {resultado[0]}')
                print(f'{resultado[1]}\n')
                print(f'Ocorrências: {resultado[2]}')
                print(f'Pontuação: {resultado[3]}\n')

        else: 
            print('Não há correnspondências dessa palavra-chave...\n')

        opcao = int(input('Você deseja realizar uma nova busca? '))

resultados = [] # Lista para armazenar os resultados das buscas
quantidade_referencias = {} # Dicionário para armazenar a quantidade de referências por URL

def search(keyword, url, depth):
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')

    resultados_keyword = buscar_keyword(soup, keyword) # Busca a palavra-chave na página

    quantidade_ocorrencias = len(resultados_keyword) # Calcula a quantidade de ocorrências da palavra-chave
    
    # Calcula a pontuação da página com base na quantidade de referências e a quantidade de ocorrências da palavra-chave
    pontuacao = calcular_pontuacao(url, quantidade_referencias, quantidade_ocorrencias) 

    # Se existirem resultados, os adiciona a uma lista
    if resultados_keyword:
        resultados.append((url, resultados_keyword, quantidade_ocorrencias, pontuacao))

    # Busque por todas as tags "a" que tenham um atributo "href" começando com http ou https
    links = soup.find_all('a', attrs={'href': re.compile("^https?://")})

    for link in links:
        nova_url = link.get('href')
        if nova_url:
            if nova_url in quantidade_referencias:
                quantidade_referencias[nova_url] += 1 # Incrementa a quantidade de referências para a URL se ela já existir no dicionário
            else:
                quantidade_referencias[nova_url] = 1 # Adiciona a URL ao dicionário com valor inicial 1
    
    # Faz uma busca recursiva em outras páginas
    if depth > 0:
        for link in links:
            nova_url = link.get('href')
            if nova_url:
                search(keyword, nova_url, depth - 1)
                
    return sorted(resultados, key=lambda x: x[3], reverse=True) # Ordena em ordem decrescente de acordo com a pontuação

# Retorna uma lista com os trechos em que a palavra-chave ocorre
def buscar_keyword(soup, palavra_chave):
    resultados = [] 

    for texto in soup.find_all(string=True):
        if palavra_chave in texto:
            posicao = texto.find(palavra_chave)
            inicio_trecho = max(posicao - 20, 0)
            fim_trecho = min(posicao + 20, len(texto))
            trecho_completo = texto[inicio_trecho:fim_trecho]
            
            resultados.append(trecho_completo)

    return resultados

def calcular_pontuacao(url, quantidade_referencias, quantidade_ocorrencias):
    pontuacao = 0

    if url in quantidade_referencias:
        pontuacao += quantidade_referencias[url] * 5

    if quantidade_ocorrencias > 0:
        pontuacao += quantidade_ocorrencias * 10
    
    return pontuacao

if __name__ == '__main__':
    main()
