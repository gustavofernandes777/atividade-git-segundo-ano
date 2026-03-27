N = int(input("Digite número inteiro positivo N: "))

par =  0
impar = 0
soma = 0
for i in range(1, N + 1):
    if(i%2 == 0):
     par = par + 1
     soma += i
    
    else:
       impar = impar + 1
print(f"Quantos números pares existem", par)
print(f"Quantos números ímpares existem", impar)
print(f"Soma de todos os numero pares é: ", soma)  
   



