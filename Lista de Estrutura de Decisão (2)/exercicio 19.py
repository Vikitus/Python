"""19.	Fa�a um Programa que leia um n�mero inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
o	Observando os termos no plural a coloca��o do "e", da v�rgula entre outros. Exemplo:
o	326 = 3 centenas, 2 dezenas e 6 unidades
o	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

num = int(input("Digite um numero menor que 1000: "))

centena = int(num / 100)
resto = num % 100

dezena = int(resto / 10)
resto = resto % 10

print(num)
print(centena)
print(dezena)
print(resto)