n = int (input("Digite um numero inteiro positivo "))
pares = 0 
impares = 0
soma_pares = 0

for i in range (1, n+1):
    if i % 2 == 0:
        pares += 1
        soma_pares += i 
    else:
        impares +=1
        
print ("Quantidade de pares:", pares)
print("Quantidade de impares:", impares)
print("Soma dos pares:", soma_pares)
    