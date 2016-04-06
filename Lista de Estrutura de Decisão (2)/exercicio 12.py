"""12.	Fa�a um programa para o c�lculo de uma folha de pagamento, sabendo que os descontos s�o do Imposto de Renda, que depende do sal�rio bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Sal�rio Bruto, mas n�o � descontado (� a empresa que deposita). O Sal�rio L�quido corresponde ao Sal�rio Bruto menos os descontos. O programa dever� pedir ao usu�rio o valor da sua hora e a quantidade de horas trabalhadas no m�s.
o	Desconto do IR:
o	Sal�rio Bruto at� 900 (inclusive) - isento
o	Sal�rio Bruto at� 1500 (inclusive) - desconto de 5%
o	Sal�rio Bruto at� 2500 (inclusive) - desconto de 10%
o	Sal�rio Bruto acima de 2500 - desconto de 20% Imprima na tela as informa��es, dispostas conforme o exemplo abaixo. No exemplo o valor da hora � 5 e a quantidade de hora � 220.
o	        Sal�rio Bruto: (5 * 220)        : R$ 1100,00
o	        (-) IR (5%)                     : R$   55,00  
o	        (-) INSS ( 10%)                 : R$  110,00
o	        FGTS (11%)                      : R$  121,00
o	        Total de descontos              : R$  165,00
                Sal�rio Liquido                 : R$  935,00"""

valor = int(input("Digite o valor por hora trabalhada R$ "))
hora = int(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = valor*hora

if salarioBruto <= 900:
    IR = 0
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
    
    print("Sal�rio Bruto: R$%0.2f" %salarioBruto)
    print("IR: Isento")
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Sal�rio Liquido: R$%0.2f" %salarioLiqui)

elif salarioBruto > 900 and salarioBruto <= 1500:
    IR = salarioBruto * (5 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Sal�rio Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Sal�rio Liquido: R$%0.2f" %salarioLiqui)    
    
elif salarioBruto > 1500 and salarioBruto <= 2500:
    IR = salarioBruto * (10 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Sal�rio Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Sal�rio Liquido: R$%0.2f" %salarioLiqui)    

else:
    IR = salarioBruto * (20 / 100)
    INSS = salarioBruto * 0.1
    FGTS = salarioBruto * 0.11
    descontos = IR + INSS
    salarioLiqui = salarioBruto - descontos
        
    print("Sal�rio Bruto: R$%0.2f" %salarioBruto)
    print("IR: R$%0.2f" %IR)
    print("INSS: R$%0.2f" %INSS)
    print("FGTS: R$%0.2f" %FGTS)
    print("Total de descontos: R$%0.2f" %descontos)
    print("Sal�rio Liquido: R$%0.2f" %salarioLiqui)