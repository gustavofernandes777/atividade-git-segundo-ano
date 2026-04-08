num = int(input("Digite um número inteiro positivo: "))
pares = 0
impares = 0
somas = 0

for i in range(1, 1 + num):
    if i % 2 == 0:
        pares += 1
        somas += i
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
print("Soma dos pares:", somas)