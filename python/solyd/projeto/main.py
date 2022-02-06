from pip._vendor import requests
import json

req = None
try:
    req = requests.get("https://api.publicapis.org/entries")
except:
    print("Erro na conexão!")
    exit()
    
print(req.text)