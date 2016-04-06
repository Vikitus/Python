"""12.	Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o	Desconto do IR:
o	Salário Bruto até 900 (inclusive) - isento
o	Salário Bruto até 1500 (inclusive) - desconto de 5%
o	Salário Bruto até 2500 (inclusive) - desconto de 10%
o	Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
o	        Salário Bruto: (5 * 220)        : R$ 1100,00
o	        (-) IR (5%)                     : R$   55,00  
o	        (-) INSS ( 10%)                 : R$  110,00
o	        FGTS (11%)                      : R$  121,00
o	        Total de descontos              : R$  165,00
                Salário Liquido                 : R$  935,00"""

valor = int(input("Digite o valor por hora trabalhada R$ "))
hora = int(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valor*hora

if salarioBruto <= 900:
    IR = 0
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
    
    print("Salário Bruto: R$%0.2f" %salarioBruto)
    print("IR: Isento")
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Salário Liquido: R$%0.2f" %salarioLiqui)

elif salarioBruto > 900 and salarioBruto <= 1500:
    IR = salarioBruto * (5 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Salário Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Salário Liquido: R$%0.2f" %salarioLiqui)    
    
elif salarioBruto > 1500 and salarioBruto <= 2500:
    IR = salarioBruto * (10 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Salário Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Salário Liquido: R$%0.2f" %salarioLiqui)    

else:
    IR = salarioBruto * (20 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Salário Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Salário Liquido: R$%0.2f" %salarioLiqui)