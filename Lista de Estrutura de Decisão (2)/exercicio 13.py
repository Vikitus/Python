"""13.	Fa�a um Programa que leia um n�mero e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inv�lido."""

numero = int(input("Digite um numero: "))

if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Ter�a")
elif numero == 4:
    print("Quarta")    
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta") 
elif numero == 7:
    print("Sabado")
else:
    print("Valor inv�lido")
    