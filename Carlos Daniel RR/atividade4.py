while True:
    
    print("\n=== INVENTÁRIO DO JOGO ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Editar quantidade de um item")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

 
    if opcao == "1":
        nome = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade: "))

        inventario.append([nome, quantidade])
        print(f"Item '{nome}' adicionado com sucesso!")


    elif opcao == "2":
        nome = input("Digite o nome do item para remover: ")

        encontrado = False

        for item in inventario:
            if item[0].lower() == nome.lower():
                inventario.remove(item)
                encontrado = True
                print(f"Item '{nome}' removido com sucesso!")
                break

        if not encontrado:
            print("Item não encontrado.")

   
    elif opcao == "3":
        print("\n=== INVENTÁRIO ===")

        if len(inventario) == 0:
            print("O inventário está vazio.")
        else:
            for item in inventario:
                print(f"Item: {item[0]} | Quantidade: {item[1]}")

    
    elif opcao == "4":
        nome = input("Digite o nome do item: ")

        encontrado = False

        for item in inventario:
            if item[0].lower() == nome.lower():
                nova_quantidade = int(input("Digite a nova quantidade: "))
                item[1] = nova_quantidade
                encontrado = True
                print("Quantidade atualizada com sucesso!")
                break

        if not encontrado:
            print("Item não encontrado.")

    
    elif opcao == "5":
        print("Saindo do programa...")
        break

   
    else:
        print("Opção inválida. Tente novamente.")
        #pedi a ajuda do meu amigo para fazer o código, ele apenas me ajudou a organizar o código, mas a lógica e a estrutura do código foi feita por mim.