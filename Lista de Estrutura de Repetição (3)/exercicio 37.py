
cod = 1
codAlto = 0
maisAlto = 0
codBaixo = 0
maisBaixo = 0
codGordo = 0
maisGordo = 0
codMagro = 0
maisMagro = 0
mediaAltura = 0
mediaPeso = 0
cont = 0

cod = int(input("Digite seu codigo: "))      
while cod != 0:
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    cont = cont + 1
    mediaAltura = mediaAltura + altura
    mediaPeso = mediaPeso + peso
    if(maisAlto < altura):
        maisAlto = altura
        codAlto = cod
    if(maisBaixo > altura):
        maisBaico = altura
        codBaixo = cod
    if(maisGordo < peso):
        maisGordo = peso
        codGordo = cod
    if(maisMagro > peso):
        maisMagro = peso
        codMagro = cod
    cod = int(input("Digite seu codigo: "))   
                
if cont > 1:
        mediaAltura = mediaAltura / cont
        mediaPeso = mediaPeso / cont

print("O mais alto � cod:", codAlto, "com", maisAlto)
print("O mais baixo � cod:", codBaixo, "com", maisBaixo)
print("O mais gordo � cod:", codGordo, "com", maisGordo)
print("O mais magro � cod:", codMagro, "com", maisMagro)
print("A media de peso � ", mediaAltura, "m")
print("A media de peso � ", mediaPeso, "kg")    
