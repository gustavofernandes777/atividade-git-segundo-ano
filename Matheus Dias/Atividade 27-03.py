n = int(input("Digite um número inteiro positivo N: "))

pares = 0
impares = 0
soma_pares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        pares += 1
        soma_pares += i

    else:
        impares += 1

print("-" * 30)
print(f"Resultados para N = {n}:")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Soma apenas dos números pares: {soma_pares}")
print("-" * 30)