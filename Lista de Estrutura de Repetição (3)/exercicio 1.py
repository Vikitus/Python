"""1.	Fa�a um programa que pe�a uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inv�lido e continue pedindo at� que o usu�rio informe um valor v�lido."""
nota = int(input("Digite uma nota entre 0 e 10: "))
while 0 <= nota <= 10:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    
print("Nota Invalida")