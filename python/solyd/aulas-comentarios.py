# Aula 1 - Introdução ao Python e Configurando o Ambiente:
'''
Instalação do Python: https://www.python.org/downloads
'''

# Aula 2 - Variáveis, tipos, entrada, saída e operadores matemáticos:
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
# Atividade:
'''
nome = input("Qual o seu nome?\n")
cpf = input("Qual o seu CPF?\n")
endereco = input("Qual o seu endereço?\n")
idade = input("Qual a sua idade?\n")
altura = input("Qual a sua altura?\n")
telefone = input("Qual o seu telefone?\n")

print("\nSEU RELATÓRIO\nNome:",nome+"\nCPF:",cpf+"\nEndereço:,",endereco+"\nIdade:",idade,"anos"+"\nAltura:",altura,"metros"+"\nTelefone:",telefone)
'''

# Aula 3 - Operadores lógicos e estruturas de decisões (IF e ELSE) :
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
not : Negação.
'''
# Atividade:
'''
idade = int(input("Qual a sua idade?\n"))
peso = float(input("Qual o seu peso?\n"))
altura = float(input("Qual a sua altura?\n"))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print("\nVocê está apto para entrar no Exército!")
else:
    print("\nVocê não pode entrar no Exército.")
'''

# Aula 4 - Strings e listas:
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

# Aula 5 - Estruturas de laço (WHILE e FOR):
'''
for i in v: : Percorre todas posições em determinado valor.
range(n) : Cria [n] quantidade de caracteres em ordem numérica.
    range(i, in, n) : Cria uma contagem em ordem numérica apartir do [i] até [in] pulando n.
len(v) : Retorna a quantidade de itens [i].

while: : Condicional enquanto.

v += n : n somado ao valor anterior.
break : Finaliza um processo de repetição.
'''
# Atividade:
'''
pessoas = int(input("Quantas pessoas convidadas?\n"))
convites = []
while pessoas >= 1:
    nome = input("Convite #"+str(pessoas)+" para: ")
    convites.append(nome)
    pessoas -= 1
print("Lista de convidados:")
for nome in convites:
    print(nome)
'''
# https://www.pythonprogressivo.net/2018/06/Como-Validar-Dados-em-Python-Exemplos-Codigo-Comentado.html
'''
nota = float(input("Registre a nota: "))
while (nota < 0) or (nota > 10):
    nota = float(input("Valor inválido! Tente novamente: "))
print("Nota",str(nota),"registrada.")
'''
'''
user = input("User: ")
senha = input("Senha: ")
while senha == user:
    print("Nome de usuário e senha iguais. Tente novamente:")
    senha = input("Senha: ")
print("Acesso confirmado.")
'''
'''
nome = input("\nNome: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo: ")
estado_civil = input("Estado Civil: ")
while len(nome) <= 3:
    nome = input("\nNome inválido. Tente novamente:\nNome: ")
while (idade <= 0) or (idade >= 150):
    idade = int(input("\nIdade impossível. Tente novamente:\nIdade: "))
while salario < 0:
    salario = float(input("\nValor inválido. Tente novamente:\nSalário: "))
while sexo != ("f" or "m"):
    sexo = input("\nSexo inválido. Tente novamente:\nSexo: ")
while estado_civil != ("s" or "c" or "v" or "d"):
    estado_civil = input("\nEstado Civil inválido. Tente novamente:\nEstado Civil: ")
print("\nInformações registradas."+nome+"\n"+str(idade)+"\n"+str(salario)+"\n"+sexo+"\n"+estado_civil)
'''
'''
a = int(input("População A: "))
b = int(input("População B: "))
taxa_a = float(input("Taxa da polulação A: "))
taxa_b = float(input("Taxa da população B: "))
ano = 0
while a < b:
    ano += 1
    crescimento_a = (a * (taxa_a/100))      # a *= 1 + (taxa_a/100)
    a += crescimento_a
    crescimento_b = (b * (taxa_b/100))      # B *= 1 + (taxa_b/100)
    b += crescimento_b
    print("\nAno:",str(ano))
    print("Cidade A:",str(a))
    print("Cidade B:",str(b))
'''

# Aula 6 - Tuplas, dicionários e conjuntos:
'''
 
'''
