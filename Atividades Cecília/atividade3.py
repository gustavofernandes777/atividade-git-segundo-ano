numero=int(input("Digite um número inteiro: "))

pares=0
impar=0
soma_pares=0

for i in range (1,numero+1):
    if i%2==0:
        pares +=1
        soma_pares+=i
    else:
        impar+=1

print("Quantidade de números pares: ", pares)
print("Quantidade de números ímpares: ", impar)
print("Soma dos números pares: ", soma_pares)

