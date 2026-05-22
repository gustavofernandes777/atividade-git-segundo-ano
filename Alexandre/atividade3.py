n = int(input("Digite um numero inteiro: "))
impares = 0
pares = 0
soma_pares = 0

for a in range(1, n+1):
    if a%2 == 0:
        pares += 1
        soma_pares += a
    elif a%2 != 0:
        impares += 1

print(f"Existem {pares} número(s) pare(s)")
print(f"Existem {impares} número(s) impar(es)")
print(f"A soma dos pare(s) é: {soma_pares}")