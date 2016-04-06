"""14.	Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
o	  Média de Aproveitamento  Conceito
o	  Entre 9.0 e 10.0        A
o	  Entre 7.5 e 9.0         B
o	  Entre 6.0 e 7.5         C
o	  Entre 4.0 e 6.0         D
o	  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

if media <= 4.0:
    conceito = "E"
    
    print("Nota 1 = %0.1f" %nota1)
    print("Nota 2 = %0.1f" %nota2)
    print("Media = %0.1f" %media)
    print("Conceito = %s" %conceito)
    print("REPROVADO")

elif media > 4.0 and media <= 6.0:
    conceito = "D"
    
    print("Nota 1 = %0.1f" %nota1)
    print("Nota 2 = %0.1f" %nota2)
    print("Media = %0.1f" %media)
    print("Conceito = %s" %conceito)
    print("REPROVADO")    

elif media > 6.0 and media <= 7.5:
    conceito = "c"
    
    print("Nota 1 = %0.1f" %nota1)
    print("Nota 2 = %0.1f" %nota2)
    print("Media = %0.1f" %media)
    print("Conceito = %s" %conceito)
    print("APROVADO") 
    
elif media > 7.5 and media <= 9.0:
    conceito = "b"
    
    print("Nota 1 = %0.1f" %nota1)
    print("Nota 2 = %0.1f" %nota2)
    print("Media = %0.1f" %media)
    print("Conceito = %s" %conceito)
    print("APROVADO") 
    
elif media > 9 and media <= 10:
    conceito = "a"
    
    print("Nota 1 = %0.1f" %nota1)
    print("Nota 2 = %0.1f" %nota2)
    print("Media = %0.1f" %media)
    print("Conceito = %s" %conceito)
    print("APROVADO") 
    
else:
    print("Valor invalido das notas")