a = input("Digite a nota 1: ")
b = input("Digite a nota 2: ")
media = (float(a)+float(b))/2
if media==10:
    print("Aprovado com Distinção")
elif media>=7:
    print("Aprovado")
else:
    print("Reprovado")    