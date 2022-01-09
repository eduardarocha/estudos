# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 01 - Introdução ao Python e Configurando o Ambiente:
'''
Instalação do Python: https://www.python.org/downloads
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 02 - Variáveis, tipos, entrada, saída e operadores matemáticos:
'''
v = "valor" : variável = valor sendo função, str, int, float, bool
print(v) : Imprime o valor de variáveis, funções.
    \n : Quebra de linha.
    \t : Tab; espaço em branco.
    , : Transforma em string e junta valores colocando um espaço entre eles.
    + : Soma valores de tipos iguais.
type(v) : Imprime o tipo do valor de uma variável.
str(v) : Converte valores de variáveis para tipo string.
int(v) : Converte valores de variáveis para tipo int.
float(v) : Converte valores de variáveis para tipo float.
input(v) : Exmprime uma entrada de valor

+ : Soma.
- : Subtração.
* : Multiplicação.
/ : Divisão.
** : Potência.
**(1/2) : Raiz quadrada.
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 03 - Operadores lógicos e estruturas de decisões (IF e ELSE) :
'''
if: : Condicional se.
elif: : Condicional se-não-se.
else: : Condicional se-não.
= : Atribuir valor.
== : Comparativo de igualdade.
!= : Comparativo de diferença.
> : Comparativo de maioridade.
>= : Comparativo de maior-igual.
< : Comparativo de menoridade.
<= : Comparativo de menor-igual.
and : Comparativo de verdadeiro-verdadeiro = True.
or : Comparativo de verdadeiro-verdadeiro/verdadeiro-falso = True.
in : Pertence.
not : Negação.
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 04 - Strings e listas:
'''
v.lower() : Transforma um valor string em caracteres minúsculos.
v.upper() : Transforma um valor string em caracteres maiúsculos.
v.split("i") : Transforma um valor string em lista quando um determinado caractere [i].

string : Lista de caracteres.
v = [i0, i2, i2] : Lista de posições.
v[i] : Posição +/- [i] de um caractere dentro de uma variável, imprimindo seu valor.
    v[i:in] : Posição [i] até posição [in].
    v[i:in:p] : Posição [i] até posição [in] pulando n caracteres +/- [p].
v.append(i) : Adicionar elemento [in] à lista.
v.remove(i) : Remover elemento [i] à lista.
v.clear() : Limpar a lista.
v.insert(i, in) : Posição [i] insere elemento [in] à lista.
v.count(i) : Contar repetição de [i].
len(v) : Conta o número de caracteres em um tipo string.
v.pop() : Remove o último da lista.
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 05 - Estruturas de laço (WHILE e FOR):
'''
for i in v: : Percorre todas posições em determinado valor.
range(n) : Cria [n] quantidade de caracteres em ordem numérica.
    range(i, in, n) : Cria uma contagem em ordem numérica apartir do [i] até [in] pulando n.
len(v) : Retorna a quantidade de itens [i].

while: : Condicional enquanto.

v += n : n somado ao valor anterior.
break : Finaliza um processo de repetição.
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 06 - Tuplas, dicionários e conjuntos:
'''
lista = [i0,i1,i2] : (list) Itens ordenados e posicionamente mutáveis.
    lista[0] : Exibe valor de item em sua posição.
tupla = (i0,i1,i2) : (tuple) Itens ordenados, limitatos e não-mutáveis.
    lista[0] : Exibe valor de item em sua posição.
dicionario = {"c1":v1,"c2":v2} : (dict) Chave + valor; chaves não ordenadas e repetidas.
    dicionario[c1] : Exibe valor de chave em seu nome.
    dicionario.values() : Lista todos os valores.
    dicionario.keys() : Lista todas as chaves.
conjunto = set{va,vb,vc} : (set) Não há ordem e repetição de valores em itens (repetição de mesmos itens).
    conjunto.add(v) : Adiciona um valor como item ao conjunto.
    conjunto.remove(v) : Remove um item com este valor.

'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 7 - Funções e Métodos:
'''
def funcao(p): : Define uma função a partir de argumento (parâmetro).
    return : Retorno de uma condição.
__init__ : Inicia um objeto e pede suas predefinições/estado.
__str__ : Print padrão de um objeto construido a partir da classe.
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 8 - Argumentos de linha de comando:
'''
import sys : Importação de bibliotecas, neste caso, a biblioteca "sys".
>> C:\Users\eduar\.. : No terminal, deve-se caminhar até a pasta com o arquivo .py.
>> python3 [nome do arquivo] [argumento_1] : Um argumento está sendo declarado [nome do arquivo]; outros argumentos podem ser declarados por espaço [argumento_1].
'''
# Cria um novo arquivo .py e cole este exemplo:
'''
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
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  Aula 9 - Orientação a objeto:
'''
class [nome]: : (classe) Descreve o objeto a partir de características, funções e métodos.
    def __inti__(self): : Método construtor de objeto.
        self.[característica] = [valor de característica atual] : Objeto e sua característica ganham um valor temporário, circunstancial.
'''
# Em arquivo veiculo.py:
'''
class Veiculo():
    def __init__(self, cor, rodas, marca, tanque):
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
        
    def abastecer(self, litros):
        self.tanque += litros
'''
'''
from [nome do arquivo] import [nome da classe]
class [nome]([herança]):
'''
# Em arquivo carro.py:
'''
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("\nErro: tanque com capacidade inferior!")
        else:
            self.tanque += litros
'''
'''
from [nome do arquivo] import [nome da classe] : Importa a classe de outro arquivo.
'''
# Em arquivo main.py:
'''
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
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Aula 10 - Entrada e saída de arquivos:
'''

'''