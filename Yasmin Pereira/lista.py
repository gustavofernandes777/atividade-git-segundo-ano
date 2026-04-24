lista = []

while True:
    print("\nMENU")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Alterar a quantidade de itens")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome do item: ")
        qtd = int(input("Digite a quantidade: "))
        item = (nome, qtd)
        lista.append(item)
        print(f"Item {nome} adicionado com quantidade {qtd}")

    elif opcao == 2:
        nome = input("Digite o nome do item que deseja remover: ")
        for item in lista:
            if nome == item [0]:
                lista.remove(item)
                print(f"Item {nome} removido com sucesso!")
                break
 
    elif opcao == 3:
        print(lista)

    elif opcao == 4:
        nome = input("Digite o nome do item que deseja alterar: ")

        for item in lista:
            if item[0] == nome:
                lista.remove(item)
                nova_qtd = int(input("Digite a nova quantidade: "))
                item = (nome, nova_qtd)
                lista.append(item)
                print(f"Quantidade do item {nome} atualizada para  {nova_qtd}")
                break
        else:
            print("Item não encontrado!")

    elif opcao == 5:
        print("Saindo do programa...")
        break       