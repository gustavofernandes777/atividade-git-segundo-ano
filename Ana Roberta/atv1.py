inventario = []
opcao = 0
while opcao != "4":
    print ("\n1 - adicionar")
    print("2 - remover")
    print("3 - mostrar ")
    print("4 - sair")

    opcao = input  ("escolha: ")

    if opcao == "1":
        nome = input("nome do item :")
        quantidade = int(input ("quantidade:"))
        inventario.append((nome, quantidade))
        print("adicionado")

    elif opcao == "2":
        nome = input("nome para remover")

        for item in inventario :
            if item [0] == nome:
                inventario.remove(item)
                print("Removido")

    elif opcao == "3" :
        print("inventario")
        for item in inventario:
            print(item)
