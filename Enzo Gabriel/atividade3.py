num = int(input("Digite um número: "))

par = 0
impares = 0
soma = 0

for numero in range(1, num + 1):
    if numero % 2 == 0:
        par = par + 1
        soma = soma + numero
    else:
        impares = impares + 1

print("Quantidade de pares:", par)
print("Quantidade de ímpares:", impares)
print("Soma dos pares:", soma)


       