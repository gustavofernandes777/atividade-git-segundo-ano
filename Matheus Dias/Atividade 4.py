inventario = []

while True:
    print("\n1 - Adicionar |2 - Remover | 3 - Mostrar | 4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Item: ")
        qtd = input("Qtd: ")
        inventario = inventario + [(nome, qtd)]
        print("Adicionado!")

    elif opcao == "2":
        nome_rem = input("Nome para remover: ")
        inventario = [item for item in inventario if item [0] != nome_rem]
        print("Removido!")

    elif opcao == "3":
        print(inventario)

    elif opcao == "4":
        break