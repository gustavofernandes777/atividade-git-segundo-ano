numero = int(input("informe um número inteiro"))
pares = 0
impares = 0
somapar = 0

for i in range (numero):
    i += 1
    print(i)
    if (i % 2) == 0:
        pares += 1
        somapar += i 
        print("seu número é par")
    else:
        impares += 1
        print("seu número é ímpar")
print(f"a quatidade de números pares é: {pares}")
print(F"a quantidade de número ímpares é: {impares}")
print(f"a soma dos pares é: {somapar}")