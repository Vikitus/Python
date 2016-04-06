"""18.	Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = input("digite uma data com o seguinte formato dd/mm/aaaa: ")
dia = int(data[0:2]) 
mes = int(data[3:5]) 
ano = int(data[6:10])

if (ano % 4 == 0 and ano % 100 !=0) or ano % 400 == 0:
    bissexto = "sim"
else:
    bissexto = "nao"

if ano > 0:
    anoTrue = True
    
if mes > 0 and mes <= 12:
    mesTrue = True

if mes == 2 and bissexto == "sim":
    if dia > 0 and dia <= 29:
        diaTrue = True
    else:
        diaTrue = False
elif mes == 2 and bissexto == "nao":
    if dia > 0 and dia <= 28:
        diaTrue = True
    else:
        diaTrue = False
else:
    if dia > 0 and dia <= 31:
        diaTrue = True

if diaTrue == mesTrue == anoTrue == True:
    print("Data valida")
else:
    print("Data Invalida")