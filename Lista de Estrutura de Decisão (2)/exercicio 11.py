"""11.	As Organiza��es Tabajara resolveram dar um aumento de sal�rio aos seus colaboradores e lhe contraram para desenvolver o programa que calcular� os reajustes.
o	Fa�a um programa que recebe o sal�rio de um colaborador e o reajuste segundo o seguinte crit�rio, baseado no sal�rio atual:
o	sal�rios at� R$ 280,00 (incluindo) : aumento de 20%
o	sal�rios entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	sal�rios entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	sal�rios de R$ 1500,00 em diante : aumento de 5% Ap�s o aumento ser realizado, informe na tela:
o	o sal�rio antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo sal�rio, ap�s o aumento.
"""

salario = float(input("Digite o valor do seu salario R$ "))

if salario <= 280:
    percentual = 20 / 100
    reajuste = salario * percentual
    novoSalario = salario + reajuste
    percentual = percentual*100
    
    print("")
    print("Salario inicial R$%0.2f" %salario)
    print("Percentual do aumento %i" %percentual)
    print("Valor do aumento R$%0.2f" %reajuste)
    print("Novo salario R$%0.2f" %novoSalario)
elif salario > 280 and salario <= 700:
    percentual = 15 / 100
    reajuste = salario * percentual
    novoSalario = salario + reajuste
    percentual = percentual*100
    
    print("")   
    print("Salario inicial R$%0.2f" %salario)
    print("Percentual do aumento %i/%" %percentual)
    print("Valor do aumento R$%0.2f" %reajuste)
    print("Novo salario R$%0.2f" %novoSalario)
elif salario > 700 and salario <= 1500:
    percentual = 10 / 100
    reajuste = salario * percentual
    novoSalario = salario + reajuste
    percentual = percentual*100
       
    print("")    
    print("Salario inicial R$%0.2f" %salario)
    print("Percentual do aumento %i" %percentual)
    print("Valor do aumento R$%0.2f" %reajuste)
    print("Novo salario R$%0.2f" %novoSalario)
else:
    percentual = 5 / 100
    reajuste = salario * percentual
    novoSalario = salario + reajuste
    percentual = percentual*100
    
    print("")      
    print("Salario inicial R$%0.2f" %salario)
    print("Percentual do aumento %i" %percentual)
    print("Valor do aumento R$%0.2f" %reajuste)
    print("Novo salario R$%0.2f" %novoSalario)