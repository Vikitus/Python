"""16.	Fa�a um programa para uma loja de tintas. O programa dever� pedir o tamanho em metros quadrados da �rea a ser pintada. Considere que a cobertura da tinta � de 1 litro para cada 3 metros quadrados e que a tinta � vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usu�rio a quantidades de latas de tinta a serem compradas e o pre�o total."""

metros= int(input("Digite o tamanho em M� a pintar: "))

numLitros = metros / 3
numLatas = numLitros / 18
valor = numLatas* 80

print("O numero de latas a comprar � %i" %numLatas)
print("Pre�o Total: R$%0.2f" %valor)