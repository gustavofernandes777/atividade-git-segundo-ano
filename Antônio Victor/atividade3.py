print("---Análise de Números---")
print()
num = int(input("Digite um número: "))
par = 0
impar = 0
somap = 0
somai = 0
for i in range(1, num+1):
    if(i%2 == 0):
        par = par + 1
        somap = i + somap
    else:
        impar = impar + 1
        somai = i + somai

print(f"A contagem do seu número resultou em {par} números pares e em {impar} números ímpares.")
print(f"A soma dos números pares resultou em {somap}.")
print(f"A soma dos números ímpares resultou em {somai}.")

    