num = int(input("Insira um número: "))

pares = 0
impares = 0
soma = 0

for cont in range (num):
    cont += 1
    print (cont)
    
    if (cont % 2) == 0:
        pares += 1
        soma = soma + cont
    
    else:
        impares +=1
 
print(f"Existem {pares} números pares.")
print(f"Existem {impares} números impares.")

print("A soma dos números pares é:", soma)