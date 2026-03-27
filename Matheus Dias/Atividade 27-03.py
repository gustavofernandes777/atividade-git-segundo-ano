while True:
    try:
        n = int(input("Digite um número inteiro positivo (N): "))
        if n > 0:
            break
        else:
            print("Por favor, digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

total_pares = 0
total_impares = 0
soma_pares = 0

print(f"\nAnalisando números de 1 até {n}:")
for i in range(1, n + 1):
    
    if i % 2 == 0:
        total_pares += 1
        soma_pares += i
    else:
        total_impares += 1

print("-" * 30)
print(f"Resultados finais:")
print(f"Quantidade de números pares: {total_pares}")
print(f"Quantidade de números ímpares: {total_impares}")
print(f"Soma dos números pares: {soma_pares}")
print("-" * 30)
