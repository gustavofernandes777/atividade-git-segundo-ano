numeros=int(input('Por favor, insira um número positivo: '))
pares = 0
impares = 0

somap = 0 
somai = 0

for numero in range( numeros+1 ):

    if numero % 2 == 0:
      pares +=1
      somap = numero + somap

    else:
        impares +=1
        somai = numero + somai

print(f"A quantidade de números impares é: {impares}" )
print(f"A quantidade de números pares é: {pares}" )
print()

print(f"A soma dos números impares é: {somai}" )
print(f"A soma dos números pares é: {somap}" )


