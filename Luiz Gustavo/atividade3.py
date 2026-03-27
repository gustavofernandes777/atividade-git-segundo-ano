N = int(input("Insira um número: "))

somapar = 0
par = 0
impar = 0

for n in range(1, N+1):
    if n%2 == 0:
        par = par+1
        somapar+= n
    else:
        impar = impar+1
print(f"Quantidade de números impar: ", impar)
print(f"Quantidade de números pares: ", par)
print(f"Soma de todos os números pares é: ", somapar)