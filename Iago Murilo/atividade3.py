# - Peça ao usuário um número inteiro positivo N.

num = int(input("Insira um numero inteiro: "))
par = 0
impar = 0
soma = 0

#- Utilize um laço for para analisar todos os números de 1 até N.
#- Para cada número, use condicionais para verificar se ele é:
#    - Par
#    - Ímpar

for i in range(1, num+1):
    if i % 2 == 0:
        par = par + 1
        soma = soma + i
    elif i%2!=0 :
        impar = impar + 1

#- Ao final, o programa deve mostrar:
#    - Quantos números pares existem
#    - Quantos números ímpares existem
#    - A soma apenas dos números pares

print (f"Numeros pares existentes: {par}")
print (f"Numeros impares existentes: {impar}")
print (f"Soma dos pares: {soma}")