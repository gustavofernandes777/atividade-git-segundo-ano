lista = []
tentativa = 0

while tentativa != 4:
    print()
    print("-" * 12 + "MENU" + "-" * 15 )
    print("1 - Adicionar Item")
    print("2 - Excluir")
    print("3 - Mostrar Inventário")
    print("4 - Sair")
    escolha = int(input("Escolha uma das opções (1 A 4) para execução: "))

    if escolha > 4 or escolha < 1:
        print("Tente Novamente!")

    elif escolha == 1:
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade de Itens: "))
        item_total = (item, quantidade)
        lista.append(item_total)

    elif escolha == 2:
        remover = input("Digite o nome do item: ")
        for item_remove in lista:
            if item_remove[0] == remover:
                lista.remove(item_remove)

    elif escolha == 3:
        print(lista)

    elif escolha == 4:
        print("SAINDO...")
        exit()

