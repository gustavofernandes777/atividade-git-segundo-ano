numero = int(input("Informe um número positivo: "))
pares = 0
impares = 0
somapar = 0

for numero in range(numero):
    numero += 1
    print(numero)

    if (numero % 2) == 0:
        print ("Número par")
        pares += 1
        somapar += numero
    else:
        impares += 1
        print("Número impar")

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"A soma dos números pares é: {somapar}")

       
    





