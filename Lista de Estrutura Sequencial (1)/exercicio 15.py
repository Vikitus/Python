"""15.	Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
 .	salário bruto.
a.	quanto pagou ao INSS.
b.	quanto pagou ao sindicato.
c.	o salário líquido.
d.	calcule os descontos e o salário líquido, conforme a tabela abaixo:
e.	+ Salário Bruto : R$
f.	- IR (11%) : R$
g.	- INSS (8%) : R$
h.	- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

valorHora = float(input("Digite quanto você ganha por hora: "))
Hora = float(input("Digite quantas horas voce trabalhou nesse mes: "))

salarioBruto = valorHora * Hora
IR = (11*salarioBruto)/100
INSS = (8*salarioBruto)/100
sindicato = (5*salarioBruto)/100
descontos = INSS + IR + sindicato
salarioLiquido = salarioBruto - descontos

print("Salario Bruto: R$%0.2f" %salarioBruto)
print("Voce pagou R$%0.2f ao INSS" %INSS)
print("Voce pagou R$%0.2f ao Sindicato" %sindicato)
print("Salario Liquido: R$%0.2f" %salarioLiquido)



