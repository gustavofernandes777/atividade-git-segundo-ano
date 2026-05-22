inventario = []

while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")

    digitado = input("Escolha uma opção: ")

    if digitado == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        inventario.append([nome, quantidade])

    elif digitado == "2":
        nome = input("Nome do item para remover: ")

        for item in inventario:
            if item[0] == nome:
                inventario.remove(item)
                print("Item removido!")
                break
        else:
            print("Item não encontrado!")

    elif digitado == "3":
        print("\nInventário:")

        if len(inventario) == 0:
            print("Inventário vazio!")
        else:
            for item in inventario:
                print(f"{item[0]} - {item[1]}")

    elif digitado == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")