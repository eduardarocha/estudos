from pip._vendor import requests
import json

def inicio(titulo):
    #lista = []
    for i in range(1, 101):
        try:
            requisicao = requests.get('https://www.omdbapi.com/?apikey=4ece8198&s=' + titulo + '&type=movie%page=' + str(i))
            detalhes = json.loads(requisicao.text)
            #lista.append(detalhes)
        except:
            print('Falha na conexão.')
