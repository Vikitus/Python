a = input("Digite o valor do produto 1: ")
b = input("Digite o valor do produto 2: ")
c = input("Digite o valor do produto 3: ")
    
if a<b and a<c:
    print("Voce deve comprar o produto 1")
elif b<c:
    print("Voce deve comprar o produto 2")
else:
    print("Voce deve comprar o produto 3")