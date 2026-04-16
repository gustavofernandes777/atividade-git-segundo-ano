inventorio = []

while True:
    print("\nBem-vindo!")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")

    digitado = input("escolha uma opção: ")

    if digitado == "1":
        nome = input("Nome do item: ")
        quantidade = int(input("Quantidade: "))
        inventario.append([nome, quantidade])

    elif digitado == "2":
        nome = input("nome do item para remover: ")
        for item in invatario:
            if item[0] == nome:
                inventario.remove(item)
                print("item removido!")
                break
        else:
         print("item não encontrado!")

    elif digitado == "3":
        print("\ninventario:")
        for item in inventario:
            print(f"{item[0]} - {item[1]}")

    elif digitado == "4":
        print("saindo...")
        break
    else:
        print("opção invalida!")