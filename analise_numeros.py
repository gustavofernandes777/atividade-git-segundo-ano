def analisar_numeros():
    """
    Pede ao usuário um número inteiro positivo N, analisa os números de 1 a N,
    e exibe a contagem de números pares e ímpares, e a soma dos números pares.
    """
    while True:
        try:
            n_str = input("Digite um número inteiro positivo (N): ")
            n = int(n_str)
            if n <= 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    count_pares = 0
    count_impares = 0
    soma_pares = 0

    for numero in range(1, n + 1):
        if numero % 2 == 0:  # É par
            count_pares += 1
            soma_pares += numero
        else:  # É ímpar
            count_impares += 1

    print(f"\nAnálise dos números de 1 até {n}:")
    print(f"Quantidade de números pares: {count_pares}")
    print(f"Quantidade de números ímpares: {count_impares}")
    print(f"Soma dos números pares: {soma_pares}")

analisar_numeros()
