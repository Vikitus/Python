"""7.	Fa�a um programa que leia 5 n�meros e informe o maior n�mero."""

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