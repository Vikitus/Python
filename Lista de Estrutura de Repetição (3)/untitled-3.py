cont = 1
acertos = 0
print("Digite a resposta da questao %i" %cont)
q = input("R: ")
while cont != 11:
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
            cont = cont + 1
    elif (cont == 3):
        if (q == "c" or q == "C"):
            acertos = acertos + 1
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