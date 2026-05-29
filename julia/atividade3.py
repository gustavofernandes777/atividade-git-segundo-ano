num = int(input("insira um numero inteiro possitivo: "))
pares = 0 
impares = 0
somas = 0

for i in range(1, 1 + num):
    if i % 2 == 0:
        pares += 1 
        somas += i 
else:
    impares += 1

print ("pares: ", pares)
print ("impares: ", impares)
print ("soam dos pares:", somas)