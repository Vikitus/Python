"""17.	Fa�a um Programa que pe�a um n�mero correspondente a um determinado ano e em seguida informe se este ano � ou n�o bissexto."""

ano = int(input("Digite um ano: "))

if ano % 400 ==0:
    print("Ano Bissexto")
elif ano % 4 == 0:
    if ano % 100 != 0:
        print("Ano Bissexto")
    else:
        print("N�o � ano Bissexto")
else:
    print("N�o � ano Bissexto")
    