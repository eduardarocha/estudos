# https://www.pythonprogressivo.net/2018/06/Lista-Exercicios-Lacos-Looping-Python.html

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 01
'''
nota = float(input("Registre a nota: "))
while (nota < 0) or (nota > 10):
    nota = float(input("Valor inválido! Tente novamente: "))
print("Nota",str(nota),"registrada.")
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 02
'''
user = input("User: ")
senha = input("Senha: ")
while senha == user:
    print("Nome de usuário e senha iguais. Tente novamente:")
    senha = input("Senha: ")
print("Acesso confirmado.")
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 03
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 04 e 05
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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 06
'''
#import sys
numeros = range(1,21)
for i in numeros:
    #sys.stdout.write(str(i)+" ")
    print(str(i), end=" ")
'''
'''
import sys
numeros = range(1,21)
for i in numeros:
    sys.stdout.write(str(i)+" ")
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 07
'''
ordem = 0
lista = []
maior_numero = None
while ordem < 5:
    ordem += 1
    lista.append(int(input("Escreva o "+str(ordem)+"º número: ")))
for numero in lista:
    if (maior_numero is None) or (numero > maior_numero):
        maior_numero = numero
print("Maior número:",str(maior_numero))
'''
'''
ordem = 0
lista = []
while ordem < 5:
    ordem += 1
    lista.append(int(input("Escreva o "+str(ordem)+"º número: ")))
maior_numero = max(lista)
print("Maior número:",str(maior_numero))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 08
'''
ordem = 0
lista = []
while ordem < 5:
    ordem += 1
    lista.append(int(input("Escreva o "+str(ordem)+"º número: ")))
soma = 0
media = 0
for numero in lista:
    soma += numero
    media = soma/ordem
print("Soma: "+str(soma)+"\nMédia: "+str(media))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 09
'''
numeros = range(0,51,2)
for i in numeros:
    print(str(i), end=" ")
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 10 e 11
'''
numero_1 = int(input("1º número: "))
numero_2 = int(input("2º número: ")) + 1
soma = 0
for i in range(numero_1,numero_2):
    print(i, end=" ")
    soma += i
print("\nSoma:",str(soma))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 12
'''
tabuada = int(input("Tabuada de: "))
resultado = 0
for i in range(1,11):
    resultado = tabuada * i
    print(tabuada,"x",i,"=",resultado)
'''
'''
tabuada = float(input("Tabuada de: "))
while tabuada > 10:
    tabuada = float(input("Digite qualquer número inteiro entre 1 a 10. Tente novamente:\nTabuada de: "))
resultado = 0
for i in range(1,11):
    resultado = tabuada * i
    print("%d x %d = %d" % (tabuada,i,resultado))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 13
'''
base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = 1
for i in range(expoente):
    resultado *= base
print("%d^%d = %d" % (base,expoente,resultado))
'''
'''
base = int(input("Base: "))
expoente = int(input("Expoente: "))
resultado = base**expoente
resultado = print("%d^%d = %d" % (base,expoente,resultado))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 14
'''
ordem = range(1,11)
pares = []
impares = []
for i in ordem:
    numero = int(input(str(i)+"º número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Pares:",str(pares))
print("Impares:",str(impares))
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 15
'''
fazer duas tabelas, depois somar. Será?
'''
