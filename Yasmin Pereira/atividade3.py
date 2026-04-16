num = int(input("Insira um número inteiro positivo: "))

pares = 0
impar = 0
soma = 0

for i in range(num):
    i = i + 1
    print(i)
    if (i % 2 ) == 0:       
        pares += 1
        soma += i
    else:
        impar+=1

print(f"Existem {pares} números pares")
print(f"Existem {impar} números ímpares")    
print(f"A soma dos números pares é: {soma}")