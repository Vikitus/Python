"""18.	Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

tamArquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a velocidade de Download em Mbps: "))

tempo = tamArquivo/velocidade
tempo = tempo/60

print("O tempo estimado de download do arquivo é %0.2f minutos" %tempo)
