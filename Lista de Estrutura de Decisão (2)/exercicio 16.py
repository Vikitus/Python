"""16.	Fa�a um programa que calcule as ra�zes de uma equa��o do segundo grau, na forma ax2 + bx + c. O programa dever� pedir os valores de a, b e c e fazer as consist�ncias, informando ao usu�rio nas seguintes situa��es:
a.	Se o usu�rio informar o valor de A igual a zero, a equa��o n�o � do segundo grau e o programa n�o deve fazer pedir os demais valores, sendo encerrado;
b.	Se o delta calculado for negativo, a equa��o n�o possui raizes reais. Informe ao usu�rio e encerre o programa;
c.	Se o delta calculado for igual a zero a equa��o possui apenas uma raiz real; informe-a ao usu�rio;
d.	Se o delta for positivo, a equa��o possui duas raiz reais; informe-as ao usu�rio;
"""

a = float(input("Digite o valor de a: "))
if a == 0:
    print("N�o � uma equa��o do segundo grau")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = (b**2) - (4 * a * c)
    
    if delta < 0:
        print("A equa��o n�o possui raizes reais")
    else:
        if delta == 0:
            raiz = -b / (2 * a)
            print("A equa��o possui apenas a rais Real %i" %raiz)
        else:
            raiz1 = ((-b) + (delta ** 0.5)) / (2 * a)
            raiz2 = ((-b) - (delta ** 0.5)) / (2 * a)
            print("")
            print("A equa��o possui duas rais Reais")
            print("Raiz 1: %i" %raiz1)
            print("Raiz 2: %i" %raiz2)
            
            
            
            