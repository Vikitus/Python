"""
11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
  a.o produto do dobro do primeiro com metade do segundo .
  b.a soma do triplo do primeiro com o terceiro.
  c.o terceiro elevado ao cubo.
"""

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))
num3 = float(input("Digite um numero real:"))

letraA = (num1*2)*(num2/2)
letraB = (num1*3)+num3
letraC = num3**3

print(letraA ,letraB ,letraC)
