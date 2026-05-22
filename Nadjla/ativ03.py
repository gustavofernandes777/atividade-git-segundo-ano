n = int(input("digite um numero inteiro positivo N :"))

qtd_pares = 0
qtd_impares = 0
soma_pares = 0


for i in range(1, n + 1):
    if i % 2 == 0:
      
        qtd_pares += 1
        soma_pares += i
    else:
       
        qtd_impares += 1


print("-" * 30)
print(f"Resultados de 1 até {n}:")
print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
print(f"Soma de todos os números pares: {soma_pares}")
print("-" * 30)