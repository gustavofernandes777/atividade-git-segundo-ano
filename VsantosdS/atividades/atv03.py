n = int(input("digite um número inteiro positivo: "))

qtd_pares = 0
qtd_impares = 0
soma_pares = 0

for i in range(1, n + 1):
    if i % 2 == 0:

        qtd_pares += 1
        soma_pares +=i
    else:

        qtd_impares += 1

print("-" * 30)
print(f"resultado de 1 até {n}: ")
print(f"quantidade de números pares: {qtd_pares}")
print(f"quantidade de números impares: {qtd_impares}")
print(f"soma de todos os números pares: {soma_pares}")
print("-" * 30)