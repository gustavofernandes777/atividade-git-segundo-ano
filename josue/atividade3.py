n = int(input("digite um numero inteiro positivo"))

pares = 0
impares = 0
somapares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        pares += 1
        somapares += i
    else:
        impares += 1
    
    print(f"\nresultado para N = {n}:")
    print(f"Quantidades de pares {pares}:")
    print(f"Quantidades de numeros impares: {impares}")
    print(f"soma dos numeros pares:{somapares}")
