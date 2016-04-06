"""7.	Faça um programa que leia 5 números e informe o maior número."""

numero = int(input("Digite um numero: "))
cont = 0
maior = numero
while cont < 4:
    numero = int(input("Digite um numero: "))
    if maior < numero:
        maior = numero
        cont = cont + 1
    else:
        cont = cont + 1

print("O maior numero digitado foi ",maior , "%")