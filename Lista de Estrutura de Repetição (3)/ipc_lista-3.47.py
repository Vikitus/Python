#
#ipc_lista_3_39-51(Questões 49 e 51 são iguais)
#Thiago Santos Borges//Matricula->1615310023
#Lorene da Silva Marques//Matricula->1615310013
#Matheus Palheta Barbosa//Matricula->1615310019
#Luiz Alexandre Olivera de Souza//Matricula->1615310057
#Nadine da Cunha Brito//Matricula->1615310040
#
i = 1
acmmedia = medianota = maior = menor = 0
cond = True
nome = input("Atleta: ")
while i < 8:
    nota = float(input("Nota: "))
    if i == 1:
        maior = menor = nota
    elif nota > maior:
        maior = nota
    elif nota < menor:
        menor = nota
    acmmedia = (acmmedia + nota)
    i = i +1

acmmedia = acmmedia - maior - menor
i = i - 3
medianota = acmmedia / i
print("Resultado final:\n")
print("Atleta: ",nome)
print("Melhor nota: %.1f" %maior)
print("Pior nota: %.1f" %menor)
print("Média: %.2f" %medianota)
cond = False
