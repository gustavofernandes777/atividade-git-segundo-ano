inventario = []

while True:
    print("|---Menu de Inventário---|")

    print()

    print("1-Adicionar")
    print("2-Remover")
    print("3-Mostrar")
    print("4-Sair")
    print("5-Sair")

    print()

    opcao = int(input("Escolha um número do menu:"))

    if opcao == 1:
        nome = input("Item:")
        quant = int(input("Quantidades:"))
        item = (nome, quant)

        inventario.append(item)
        print("Item adicionado!")

    elif opcao == 2:
        remover = input("Que item você deseja remover:")

        for item in inventario:
            if item[0] == remover:
                inventario.remove(item)
                print("Item removido!")
                break

    elif opcao == 3:
        print("---LISTA DE ITENS---")
        
        print()

        for item in inventario:
            print("Nome:", item[0], "quant:", item[1])

    
    elif opcao == 4:
        mod = input("Qual item você quer modificar? ")
        qtd2 = int(input("Digite a nova quantidade desse item: "))

        for i in inventario:
            if i[0] == mod:
                inventario.remove(i)
                inventario.append((mod, qtd2))
                print(f"O item {mod} foi modificado para a quantidade {qtd2}.")
                break  
            
    elif opcao == 5:
        print("Programa finalizado...")
        break 

    elif opcao == 5:
        print("Saindo...")
        break