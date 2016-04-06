"""15.	Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
o	Dicas:
o	Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
o	Triângulo Equilátero: três lados iguais;
o	Triângulo Isósceles: quaisquer dois lados iguais;
o	Triângulo Escaleno: três lados diferentes;
"""

ladoA = int(input("Digite o tamanho do lado A: "))
ladoB = int(input("Digite o tamanho do lado B: "))    
ladoC = int(input("Digite o tamanho do lado C: "))
            
if ladoA < (ladoB + ladoC) and ladoB< (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        print("É um Triângulo Equilátero")
    if ladoA == ladoB != ladoC or ladoB == ladoC != ladoA:
        print("É um Triângulo Isósceles")
    if ladoA != ladoB !=ladoC:
        print("É um Triângulo Escaleno")
else:
    print("Valores informados não formam um Triângulo")
    
            