num = int(input("Insira um número: "))

pares = 0
impares = 0
soma = 0
for cont in range (num):
    if (cont % 2 ) == 0:

        pares  +=1

        soma = soma + cont 
    else:
        impares  += 1
        print(f"Quantidade de números impares: ",impares)
        print(f"Quantidade de números pares:",pares)
        print(f"Soma de todos os números pares é: ", soma)

