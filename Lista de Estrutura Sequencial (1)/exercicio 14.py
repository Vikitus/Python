"""14.	Jo�o Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento di�rio de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de S�o Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. Jo�o precisa que voc� fa�a um programa que leia a vari�vel peso (peso de peixes) e verifique se h� excesso. Se houver, gravar na vari�vel excesso e na vari�vel multa o valor da multa que Jo�o dever� pagar. Caso contr�rio mostrar tais vari�veis com o conte�do ZERO."""

peso = float(input("Digite o peso do peixe: "))

if peso > 50: 
    excesso = peso - 50
    multa = excesso * 4
    print("Voc� excedeu o peso em %0.3f kg" %excesso)
    print("Devera pagar uma multa de R$%0.2f" %multa)
else:
    excesso = 0
    multa = 0    
    print("Voc� excedeu o peso em %0.3f kg" %excesso)
    print("Devera pagar uma multa de R$%0.2f" %multa)    