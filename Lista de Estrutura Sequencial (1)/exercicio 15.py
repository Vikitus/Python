"""15.	Fa�a um Programa que pergunte quanto voc� ganha por hora e o n�mero de horas trabalhadas no m�s. 
Calcule e mostre o total do seu sal�rio no referido m�s, sabendo-se que s�o descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, fa�a um programa que nos d�:
 .	sal�rio bruto.
a.	quanto pagou ao INSS.
b.	quanto pagou ao sindicato.
c.	o sal�rio l�quido.
d.	calcule os descontos e o sal�rio l�quido, conforme a tabela abaixo:
e.	+ Sal�rio Bruto : R$
f.	- IR (11%) : R$
g.	- INSS (8%) : R$
h.	- Sindicato ( 5%) : R$
= Sal�rio Liquido : R$
Obs.: Sal�rio Bruto - Descontos = Sal�rio L�quido."""

valorHora = float(input("Digite quanto voc� ganha por hora: "))
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



