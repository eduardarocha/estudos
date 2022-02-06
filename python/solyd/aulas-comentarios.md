## AULA 01 - Introdução ao Python e Configurando o Ambiente

Instalação do [Python](https://www.python.org/downloads).


## AULA 02 - Variáveis, tipos, entrada, saída e operadores matemáticos

_**variável**_ : valor sendo função, str, int, float, bool.

### Funções básicas
`print(v)` : Imprime o valor de variáveis, funções.
* `\n` : Quebra de linha.
* `\t` : Tab; espaço em branco.
* `,` : Transforma em string e junta valores colocando um espaço entre eles.
* `+` : Soma valores de tipos iguais.

`type(v)` : Imprime o tipo do valor de uma variável.

`str(v)` : Converte valores de variáveis para tipo string.

`int(v)` : Converte valores de variáveis para tipo int.

`float(v)` : Converte valores de variáveis para tipo float.

`input(v)` : Exmprime uma entrada de valor.

### Operadores matemáticos
* `+` : Soma.
* `-` : Subtração.
* `*` : Multiplicação.
* `/` : Divisão.
* `**` : Potência.
* `**(1/2)` : Raiz quadrada.
* `v += n` : `n` somado ao valor anterior.


## AULA 03 - Operadores lógicos e estruturas de decisões (IF e ELSE)

`if:` : Condicional se.

`elif:` : Condicional se-não-se.

`else:` : Condicional se-não.

### Operadores lógicos
* `=` : Atribuir valor.
* `==` : Comparativo de igualdade.
* `!=` : Comparativo de diferença.
* `>` : Comparativo de maioridade.
* `>=` : Comparativo de maior-igual.
* `<` : Comparativo de menoridade.
* `<=` : Comparativo de menor-igual.
* `and` : Comparativo de verdadeiro-verdadeiro = True.
* `or` : Comparativo de verdadeiro-verdadeiro/verdadeiro-falso = True.
* `in` : Pertence.
* `not` : Negação.


## AULA 04 - Strings e listas

_**string**_ : Lista de caracteres.

`v = [i0, i2, i2]` : Lista de posições.

`v[i]` : Posição +/- `[i]` de um caractere dentro de uma variável, imprimindo seu valor.
* `v[i:in]` : Posição `[i]` até posição `[in]`.
* `v[i:in:p]` : Posição `[i]` até posição `[in]` pulando n caracteres +/- `[p]`.

`v.append(i)` : Adicionar elemento `[in]` à lista.

`v.remove(i)` : Remover elemento `[i]` à lista.

`v.clear()` : Limpar a lista.

`v.insert(i, in)` : Posição `[i]` insere elemento `[in]` à lista.

`v.count(i)` : Contar repetição de `[i]`.

`len(v)` : Conta o número de caracteres em um tipo string.

`v.pop()` : Remove o último da lista.

### Outras funções
`v.lower()` : Transforma um valor string em caracteres minúsculos.

`v.upper()` : Transforma um valor string em caracteres maiúsculos.

`v.split("i")` : Transforma um valor string em lista quando um determinado caractere `[i]`.


## AULA 05 - Estruturas de laço (WHILE e FOR)

`for i in v:` : Percorre todas posições em determinado valor.

`while:` : Condicional enquanto.
* `break` : Finaliza um processo de repetição.

### Outras funções
`range(n)` : Cria `[n]` quantidade de caracteres em ordem numérica.
* `range(i, in, n)` : Cria uma contagem em ordem numérica apartir do `[i]` até `[in]` pulando n.

`len(v)` : Retorna a quantidade de itens `[i]`.


## AULA 06 - Tuplas, dicionários e conjuntos

`lista = [i0,i1,i2]` : _**list**_ : Itens ordenados e posicionamente mutáveis.
* `lista[0]` : Exibe valor de item em sua posição.

`tupla = (i0,i1,i2)` : _**tuple**_ : Itens ordenados, limitatos e não-mutáveis.
* `lista[0]` : Exibe valor de item em sua posição.

`dicionario = {"c1":v1,"c2":v2}` : _**dict**_ : Chave + valor; chaves não ordenadas e repetidas.
* `dicionario[c1]` : Exibe valor de chave em seu nome.
* `dicionario.values()` : Lista todos os valores.
* `dicionario.keys()` : Lista todas as chaves.

`conjunto = set{va,vb,vc}` : _**set**_ : Não há ordem e repetição de valores em itens (repetição de mesmos itens).
* `conjunto.add(v)` : Adiciona um valor como item ao conjunto.
* `conjunto.remove(v)` : Remove um item com este valor.


## AULA 07 - Funções e Métodos

`def funcao(p):` : Define uma função a partir de argumento (parâmetro).
* `return` : Retorno de uma condição.

`__init__` : Inicia um objeto e pede suas predefinições/estado.

`__str__ `: Print padrão de um objeto construido a partir da classe.


## AULA 08 - Argumentos de linha de comando

`import sys` : Importação de bibliotecas, neste caso, a biblioteca "sys".

>No Terminal, deve-se caminhar até a pasta com o arquivo .py:
>
>`python3 [nome do arquivo] [argumento_1]` : Um argumento está sendo declarado `[nome do arquivo]`; outros argumentos podem ser declarados por espaço `[argumento_1] [argumento_2] ...`

**Em arquivo [nome do arquivo].py:**
``` python
import sys
argumentos = sys.argv
def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
if argumentos[1] == "soma":
    valor = soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    valor = sub(float(argumentos[2]), float(argumentos[3]))
print(valor)
```


##  AULA 09 - Orientação a objeto

`class [nome]:` : _**classe**_ : Descreve o objeto a partir de características, funções e métodos.
* `def __inti__(self)`: : Método construtor de objeto.
    * `self.[característica] = [valor de característica atual]` : Objeto e sua característica ganham um valor temporário, circunstancial.

**Em arquivo veiculo.py:**
``` python
class Veiculo():
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    def abastecer(self, litros):
        self.tanque += litros
```

`from [nome do arquivo] import [nome da classe]` : Importar classe de um outro arquivo.

`class [nome]([herança]):` : Definir uma classe `[nome]` e sua classe de `[herança]`.

**Em arquivo carro.py:**
``` python
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("\nErro: tanque com capacidade inferior!")
        else:
            self.tanque += litros
```

**Em arquivo main.py:**
``` python
from veiculo import Veiculo
from carro import Carro

veiculo_01 = Veiculo("rosa", 6, "Ford", 10)
print("\nVeiculo 01\nCor:",veiculo_01.cor+"\nRodas:",str(veiculo_01.rodas)+"\nMarca:",veiculo_01.marca+"\nTanque:",str(veiculo_01.tanque))
veiculo_01.abastecer(10)
print("\nVeiculo 01\nTanque:",str(veiculo_01.tanque))

veiculo_02 = Carro("azul", "BMW", 30)
print("\nVeiculo 02\nCor:",veiculo_02.cor+"\nRodas:",str(veiculo_02.rodas)+"\nMarca:",veiculo_02.marca+"\nTanque:",str(veiculo_02.tanque))
veiculo_02.abastecer(100)
print("\nVeiculo 02\nTanque:",str(veiculo_02.tanque))
```


## AULA 10 - Entrada e saída de arquivos

`[variável] = open([caminho do arquivo], [modo de abertura])` : Criação de arquivos.
* `[modo de abertura]` : "r" read, "w" write, "r+" read-write, "a" append, "b" bits (binary)/"rb" read-binary.

`[nome da variável].read()` : Leitura do arquivo.

`[nome da variável].write()` : Escrita do arquivo.


## AULA 11 - Tratamentos de erros e exceções (TRY e EXCEPT)

`try:` : Tentativa.

`except [especificação de erro]:` : Exceção à tentativa (erro, especificado ou não).
* `except [especificação de erro] as [variável]:` : Exceção à tentativa, adicionado seu valor à uma variável.

`import time` : Importação de bibliotecas, neste caso, a biblioteca "time".
* `time.sleep([tempo em segundos])` : Pausa o xprograma por [tempo em segundos].


## AULA 12 - Bibliotecas, PIP e Requisições Web

> No terminal, algumas bibliotecas:
>
> `pip install requests` ou `-m pip install requests` : Iniciando o pip (gerenciador de pacotes externos) e instalando a biblioteca `requests`.
>
> `pip install bs4` ou `-m pip install bs4` : Iniciando o pip (gerenciador de pacotes externos) e instalando a biblioteca `bs4` (Beautiful Soup 4).

`import requests` ou [`from pip._vendor import requests`](https://stackoverflow.com/questions/48775755/importing-requests-into-python-using-visual-studio-code) : Requisições web.

`requisicao = requests.get("[endereço]")` : Requisição para receber/pegar informações.
* `requisicao.status_code` : Estado do endereço em códigos numéricos.
* `requisicao.text` : Conteúdo do endereço; código-fonte.

`requests.post("[endereço]")` : Requisição para enviar informações.

### `headers` : Cabeçalhos
`cabecalho = {[especificação]: [conteúdo]}` `headers = cabecalho` : Alterando ou criando especificações (`[especificação]: [conteúdo]`) de cabeçalho (`headers`).

Pode-se criar outras especificações de cabeçalhos.

De cabeçalho-padrão http, tem-se:
* `User-agent` : Especificações do navegador, sistema operacional, etc.
* `Referer` : De onde/quem vem o acesso para determinado endereço.

### `cookies` : Informações temporárias
`temporario = {[especificação]: [conteúdo]}` `cookies = temporario` : Alterando ou criando especificações (`[especificação]: [conteúdo]`) de cookies (`cookies`).

Pode-se criar outras especificações de cookies.

### `data` : Enviar dados
`dados = {[especificação]: [conteúdo]}` `dados = data` : Alterando ou criando especificações (`[especificação]: [conteúdo]`) de dados (`data`).

Pode-se criar outras especificações de dados.

**Em arquivo main.py:**
``` python
from pip._vendor import requests

cabecalho = {"User-agent": "Windows 10", "Referer": "https://www.google.com"}
temporario = {"Ultima-visita": "29-01-2022"}
dados = {"User": "Eduarda", "Password": "eduarda123"}
texto = None

try:
    requisicao = requests.get("https://www.g1.com.br", headers = cabecalho, cookies = temporario, data = dados)
    texto = requisicao.text
except Exception as e:
    print("Erro de requisição:", e)
print(texto)
```


## AULA 13 - API, JSON e consultando listas de filmes

_**API**_ : Interface de comunicação com outros programas.

Databases abertas com informações de diversos filmes ([API movies](https://apipheny.io/free-api/)):
* API utilizada na aula : [OMDb API](https://www.omdbapi.com).
* API utilizada na prática : [Public APIS](https://api.publicapis.org/entries).

`import json` : Biblioteca json; no python, permite-se que transforme json para objeto (neste caso, dicionário).

11:00

**Em arquivo main.py:**
``` python

```