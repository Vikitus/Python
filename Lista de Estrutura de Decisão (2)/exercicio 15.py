"""15.	Fa�a um Programa que pe�a os 3 lados de um tri�ngulo. O programa dever� informar se os valores podem ser um tri�ngulo. Indique, caso os lados formem um tri�ngulo, se o mesmo �: equil�tero, is�sceles ou escaleno.
o	Dicas:
o	Tr�s lados formam um tri�ngulo quando a soma de quaisquer dois lados for maior que o terceiro;
o	Tri�ngulo Equil�tero: tr�s lados iguais;
o	Tri�ngulo Is�sceles: quaisquer dois lados iguais;
o	Tri�ngulo Escaleno: tr�s lados diferentes;
"""

ladoA = int(input("Digite o tamanho do lado A: "))
ladoB = int(input("Digite o tamanho do lado B: "))    
ladoC = int(input("Digite o tamanho do lado C: "))
            
if ladoA < (ladoB + ladoC) and ladoB< (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    if ladoA == ladoB == ladoC:
        print("� um Tri�ngulo Equil�tero")
    if ladoA == ladoB != ladoC or ladoB == ladoC != ladoA:
        print("� um Tri�ngulo Is�sceles")
    if ladoA != ladoB !=ladoC:
        print("� um Tri�ngulo Escaleno")
else:
    print("Valores informados n�o formam um Tri�ngulo")
    
            