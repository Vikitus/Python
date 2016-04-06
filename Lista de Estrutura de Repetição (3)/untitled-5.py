limite = int(input("Digite o valor de n: "))
cont = 1
n = 1
m = 1
soma = 0
while cont <= limite:
    soma = soma + (n/m)
    print(n,"/",m)
    m = m+1
    cont = cont + 1
    
print("A soma é %0.2f" %soma)