limite = int(input("Digite o valor de n: "))
cont = 1
n = 1
m = 1
soma = 0
while cont <= limite:
    soma = soma + (n/m)
    print(n,"/",m)
    n = n+1
    m = m+2
    cont = cont + 1
    
print("A soma � %0.2f" %soma)