print("Para pedir File Duplo digite 1")
print("Para pedir Alcatra digite 2")
print("Para pedir Picanha digite 3")

tipo_carne = int(input("Digite o tipo de carne: "))
quant_carne = float(input("Digite a quantidade de carne: "))

if (tipo_carne == 1):
    if (quant_carne <= 5):
        preco_total = quant_carne * 4.90
        tipo_carne = "File Duplo"
    else:
        preco_total = quant_carne * 5.80
        tipo_carne = "File Duplo"
elif (tipo_carne == 2):
    if (quant_carne <= 5):
        preco_total = quant_carne * 5.90
        tipo_carne = "Alcatra"
    else:
        preco_total = quant_carne * 6.80
        tipo_carne = "Alcatra"
        
elif (tipo_carne == 3):
    if (quant_carne <= 5):
        preco_total = quant_carne * 6.90
        tipo_carne = "Picanha"
        
    else:
        preco_total = quant_carne * 7.80
        tipo_carne = "Picanha"
        
else:
    print("Tipo invalido")

print("Digite 1 para cartão tabajara")
print("Digite 2 para dinheiro")
print("Digite 3 para outros cartões")

forma = int(input("Digite a forma de pagamento: "))

if (forma == 1):
    desconto = 0.05 * preco_total
    total_pagar = preco_total - desconto
    forma = "Cartão Tabajara"
elif (forma == 2):
    desconto = 0
    total_pagar = preco_total - desconto
    forma = "Dinheiro"
elif (forma == 3):
    desconto = 0
    total_pagar = preco_total - desconto
    forma = "Cartão de credito"
else:
    print("Forma invalida de pagamento")
    
print("Tipode de carne: ",tipo_carne)
print("Quantidade de carne: ",quant_carne,"Kg")
print("Preço Total: R$%0.2f" %preco_total)
print("Tipo de pagamento: ",forma)
print("Valor do desconto: R$%0.2f" %desconto)
print("Valor a pagar: R$%0.2f" %total_pagar)

