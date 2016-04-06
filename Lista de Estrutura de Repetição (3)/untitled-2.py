print("Digite 1 para fazer a prova")
print("digite 0 para encerrar o programa")
num = int(input("numero:"))
cont = 1
acertos = 0
maior = 0
menor = 0 
media = 0
alunos = 0
while num != 0:
    print("Digite a resposta da questao %i" %cont)
    q = input("R: ")
    while cont != 10:
        if (cont == 1):
            if (q == "a" or q == "A"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 2):
            if (q == "b" or q == "B"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
        elif (cont == 3):
            if (q == "c" or q == "C"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 4):
            if (q == "d" or q == "D"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos 
                cont = cont + 1
        elif (cont == 5):
            if (q == "e" or q == "E"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos  
                cont = cont + 1
        elif (cont == 6):
            if (q == "e" or q == "E"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 7):
            if (q == "d" or q == "D"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 8):
            if (q == "c" or q == "C"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 9):
            if (q == "b" or q == "B"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        elif (cont == 10):
            if (q == "a" or q == "A"):
                acertos = acertos + 1
                cont = cont + 1
            else:
                acertos = acertos
                cont = cont + 1
        else:
            cont = cont + 1
        print("Digite a resposta da questao %i" %cont)
        q = input("R: ")
        
    cont = 1
    if (maior < acertos):
        maior = acertos
    if (menor > acertos):
        menor = acertos
    alunos = alunos + 1
    media = acertos
    print("Digite 1 para fazer a prova")
    print("digite 0 para encerrar o programa")
    num = int(input("numero:"))
media = media/alunos

print("maior:", maior)
print("menor:", menor)
print("total alunos:",alunos)
print("media:",media)