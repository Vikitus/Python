"""
12.	Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte f�rmula: (72.7*altura) - 58
"""

altura = float(input("Digite sua altura: "))

peso = (72.7 * altura) - 58

print("Seu peso ideal � %0.3f kg" %peso)