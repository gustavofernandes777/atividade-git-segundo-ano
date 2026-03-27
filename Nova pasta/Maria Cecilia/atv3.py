nume=int(input("Digite um número inteiro:"))

par=0
impar=0
somapar=0

for i in range(1, nume+1):
    if i %2==0:
        par+=1
        somapar+=i
    else:
        impar+=1

print("Quantidade de números pares:", par) 
print("Quantidade de números impar:",impar)
print("Soma dos números pares:",somapar)