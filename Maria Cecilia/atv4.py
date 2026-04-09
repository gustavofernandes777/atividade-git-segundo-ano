inventario=[]
opcao=0

while opcao != 4:
    print("\n1-adicionar item")
    print("2-remover item")
    print("3-mostrar inventário")
    print("4-sair")

    opcao=int(input("Escolha uma opcao:"))

    if opcao == 1:
        nome=input("Nome: ")
        quantidade=int(input("quantidade: "))
        inventario.append((nome,quantidade))
        print("Item adicionado!")
    elif opcao == 2:
        nome = input("Nome para remover: ")
        i=0

        while i<len(inventario):
            if inventario[i][0] == nome:
                inventario.pop(i)
            else:
                i += 1

        print("Remoção concluída!")
    
    elif opcao == 3:
        if len(inventario) == 0:
            print("Inventario vazio")
        else:
            for item in inventario:
                print(item[0], "-", item[1])

    elif opcao == 4:
        print("Saindo...")

    else:
        print("Opção inválida!")