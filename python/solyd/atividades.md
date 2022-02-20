## AULA 02 - Atividade

``` python
nome = input("Qual o seu nome?\n")
cpf = input("Qual o seu CPF?\n")
endereco = input("Qual o seu endereço?\n")
idade = input("Qual a sua idade?\n")
altura = input("Qual a sua altura?\n")
telefone = input("Qual o seu telefone?\n")

print("\nSEU RELATÓRIO\nNome:",nome+"\nCPF:",cpf+"\nEndereço:,",endereco+"\nIdade:",idade,"anos"+"\nAltura:",altura,"metros"+"\nTelefone:",telefone)
```


## AULA 03 - Atividade

``` python
idade = int(input("Qual a sua idade?\n"))
peso = float(input("Qual o seu peso?\n"))
altura = float(input("Qual a sua altura?\n"))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print("\nVocê está apto para entrar no Exército!")
else:
    print("\nVocê não pode entrar no Exército.")
```


## AULA 05 - Atividade

``` python
pessoas = int(input("Quantas pessoas convidadas?\n"))
convites = []
while pessoas >= 1:
    nome = input("Convite #"+str(pessoas)+" para: ")
    convites.append(nome)
    pessoas -= 1
print("Lista de convidados:")
for nome in convites:
    print(nome)
```


## AULA 07 - Atividade

```python
def maior(colecao):
    valor = None
    for i in colecao:
        if (valor is None) or (i > valor):
            valor = i
    return valor
def menor(colecao):
    valor = float("inf")
    for i in colecao:
        if (i < valor):
            valor = i
    return valor
print(maior({1,-2,3,4,5}))
print(menor({1,-2,3,4,5}))
```


## AULA 09 - Atividade

Em arquivo cliente.py:
``` python
class Cliente():
    def __init__(self, cpf, nome, idade):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return ("\nCliente 01\nNome: "+self.nome+"\nCPF: "+self.cpf+"\nIdade: "+str(self.idade))
```

Em arquivo conta.py:
```python
class Conta():
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = -limite
    def __str__(self):
        return ("\nConta 01\nCPF: "+str(self.cliente.cpf)+"\nNome: "+str(self.cliente.nome)+"\nSaldo: R$"+str(self.saldo))
    def depositar(self, valor):
        if (valor > 0):
            self.saldo += valor
            print("\nValor depositado! Saldo atual: R$"+str(self.saldo))
        else:
            print("Erro: valor de depósito inválido!")
    def sacar(self, valor):
        if (valor < 0) or (self.saldo - valor < self.limite):
            print("Erro: valor de saque inválido ou insuficiente!")
        else:
            self.saldo -= valor
            print("\nValor sacado! Saldo atual: R$"+str(self.saldo))
```

Em arquivo main.py:
``` python
from cliente import Cliente
from conta import Conta

cliente_01 = Cliente("111.111.111-11", "Eduarda", 18)
print(cliente_01)
conta_01 = Conta(cliente_01, 100, 1000)
print(conta_01)
conta_01.sacar(1000)
conta_01.depositar(10)
```


## AULA 13 - Atividade

```

```
