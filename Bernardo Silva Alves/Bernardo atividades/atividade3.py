num = int(input("Insira um número:"))

par = 0

impar = 0

soma = 0

for numeros in range(num):
    numeros += 1

    if numeros % 2 == 0:
        par += 1
        soma += numeros

    else:
        impar += 1

print("Quantidade de Números pares:", par)
print("Quantidade de Números ímpares:", impar)
print("Soma dos números pares:", soma)