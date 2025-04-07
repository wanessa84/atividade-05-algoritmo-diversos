#--------------------------
#1) Crie um algoritmo que solicite ao usuário a sua idade e exiba se ele é maior que de idade ou menor de idade.
#------------------------

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#----------------------------------
# 2) Crie um algoritmo que leia a temperatura em Celsius e informe se está calor (acima de 30o) frio (abaixo de 10o) ou agradável (entre 10o e 30o). 
#---------------------------------

temperatura = float(input("Digite a temperatura: "))

if temperatura > 30:
    print("Está calor.")
elif temperatura < 10:
    print("Está frio.")
else:
    print("O clima está agradável.")

#-------------------------
# 3) Escreva um algoritmo que leia o nome de um aluno e a sua nota, caso seja 7 ou superior exibir aprovado, caso contrário reprovado. 
# ------------------------

nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print(f"{nome} está aprovado.")
else:
    print(f"{nome} está reprovado.")

#--------------------------
#4) Crie um algoritmo que leia 10 números inteiros fornecidos pelo usuário, calcule a soma dos números informados, exiba o resultado na tela.
#-----------------------------

soma = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    soma += numero

print(f"A soma dos números informados é: {soma}")

#-----------------------
#5) Crie um algoritmo que leia a idade do usuário, e informe se é uma pessoa jovem (18 e 25 anos), adulto (26 e 60 anos) ou idosa (acima de 60 anos).
#-------------------------

idade = int(input("Digite sua idade: "))

if 18 <= idade <= 25:
    print("Você é uma pessoa jovem.")
elif 26 <= idade <= 60:
    print("Você é um adulto.")
elif idade > 60:
    print("Você é uma pessoa idosa.")
else:
    print("Você é menor de 18 anos.")

#--------------------------
# 6) Crie uma função chamada imprimir_nome que receba o nome como parâmetro e exiba o nome na tela. Solicite o usuário o nome, e chame a função.    
#---------------------------
def imprimir_nome(nome):
    print(f'O nome fornecido é: {nome}')

nome_usuario = input('Digite seu nome: ')

imprimir_nome(nome_usuario)

#----------------------------
#7) Escreva um algoritmo que leia um número inteiro positivo e exiba a tabuada desse número (1 a 10).
#----------------------------
numero = int(input("Digite um número inteiro positivo: "))

if numero > 0:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Por favor, digite um número positivo.")

#---------------------------
# 8) Crie um algoritmo que leia o preço de um produto e calcule o valor com 10% de desconto, exiba o preço com desconto.    
#----------------------------
preco = float(input("Digite o preço do produto: "))

desconto = preco * 0.10
preco_com_desconto = preco - desconto

print(f"O preço com 10% de desconto é: R${preco_com_desconto:.2f}")

#-------------------------
#9) Crie um algoritmo que leia o valor de um produto e informe se ele está dentro de uma faixa de preço (menor que R$: 50.00, entre R$:50.00 e R$:100.00 ou maior que R$:100.00)
#-------------------------







#--------------------------
#10) Escreva uma função chamada calcular_area_quadrado que receba o valor de um lado de um quadrado e retorne a área. Solicite ao usuário o valor do lado e exiba o resultado. Fórmula: área = lado2
#-------------------------
def calcular_area_quadrado(lado):
    
    return lado ** 2

lado_quadrado = float(input("Digite o valor do lado do quadrado: "))
area = calcular_area_quadrado(lado_quadrado)
print(f"A área do quadrado é: {area}")

#-------------------------------
#11) Crie uma função lambda que receba dois números e retorne a diferença entre o maior e o menor número. Solicite ao usuário os dois números e exiba o resultado.
#-------------------------------



#------------------------------
#12) Crie um algoritmo que leia a altura de uma pessoa e informe se ela pode ou não participar de uma montanha-russa, considerando que a altura mínima necessária é 1,40m.
#-----------------------------




#-------------------------------
#13) Crie uma função chamada converter_fahrenheit_para_celsius que
#receba uma temperatura Fahrenheit e converta para celsius. Solicite o
#usuário a temperatura em Fahrenheit e exiba o resultado da conversão.
#Fórmula: C = (5/9) * (Fahrenheit - 32).
#------------------------------------

