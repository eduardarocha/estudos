# Aula 02 - Atividade:
'''
nome = input("Qual o seu nome?\n")
cpf = input("Qual o seu CPF?\n")
endereco = input("Qual o seu endereço?\n")
idade = input("Qual a sua idade?\n")
altura = input("Qual a sua altura?\n")
telefone = input("Qual o seu telefone?\n")

print("\nSEU RELATÓRIO\nNome:",nome+"\nCPF:",cpf+"\nEndereço:,",endereco+"\nIdade:",idade,"anos"+"\nAltura:",altura,"metros"+"\nTelefone:",telefone)
'''

# Aula 03 - Atividade:
'''
idade = int(input("Qual a sua idade?\n"))
peso = float(input("Qual o seu peso?\n"))
altura = float(input("Qual a sua altura?\n"))

if (idade >= 18) and (peso >= 60) and (altura >= 1.70):
    print("\nVocê está apto para entrar no Exército!")
else:
    print("\nVocê não pode entrar no Exército.")
'''

# Aula 05 - Atividade:
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

