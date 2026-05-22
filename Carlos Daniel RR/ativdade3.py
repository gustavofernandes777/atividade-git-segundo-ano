
N = int(input("Digite um número inteiro positivo: "))
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0

for numero in range(1, N + 1):

   
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
    
        quantidade_impares += 1

print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números pares:", soma_pares)