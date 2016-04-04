"""16.	Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total."""

metros= int(input("Digite o tamanho em M² a pintar: "))

numLitros = metros / 3
numLatas = numLitros / 18
valor = numLatas* 80

print("O numero de latas a comprar é %i" %numLatas)
print("Preço Total: R$%0.2f" %valor)