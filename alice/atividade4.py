while True:
    print("\nBem-vindo!")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")

    inventario = []

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        inventario.append([nome, quantidade])

    elif opcao == "2":
        nome = input("Nome do item para remover: ")
        achou = False

        for item in inventario:
            if item[0] == nome:
                inventario.remove(item)
                print("Item removido!")
                achou = True
                break

        if achou == False:
            print("Item não encontrado!")

    elif opcao == "3":
        print("\nInventário:")
        for item in inventario:
            print(item[0], "-", item[1])

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")