from logging import exception
from pip._vendor import requests

try:
    requisicao = requests.get("https://www.g1.com.br")
except Exception as e:
    print("Erro de requisição:", e)
print(requisicao.text)