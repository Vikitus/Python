"""
13.	Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
 .	Para homens: (72.7*h) - 58
a.	Para mulheres: (62.1*h) - 44.7 (h = altura)
b.	Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

altura = float(input("Digite sua altura: "))
print("M = Masculino  F=Feminino")
sexo = input("Digite seu Sexo: ")

if sexo =="M" or sexo=="m":
    peso = (72.7 * altura) - 58
elif sexo =="F" or sexo=="f":
    peso = (62.1 * altura) - 44.7
else:
    print("Sexo invalido")

print("Seu peso ideal é %0.3f kg" %peso)