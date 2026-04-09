n = int(input("digite um número: "))

par = 0
impares = 0
soma = 0

for num in range(1, n + 1):
    if num % 2 == 0:
        par = par + 1
        soma = soma + num
    else:
        impares = impares + 1

print("Quantidade de pares:", par)
print("Quantidade de ímpares:", impares)
print("Soma dos pares:", soma)