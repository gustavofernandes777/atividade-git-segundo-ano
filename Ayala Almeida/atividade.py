inventario = []
opcao = 0
while opcao != 4 :
    print ("\n1 - Adicionar item")
    print ("2 - Remover item")
    print("3 - Mostrar inventário")
    print(" 4 - Sair")

    opcao = int (input("Digite a opcao:"))
     
    if opcao == 1 :  
        nome = input("Nome do item:")
        quantidade = int(input("Quantidade: "))
        item = (nome,quantidade)
        inventario.append(item)
        print("item adicionado!")

    elif opcao == 2:
        nome = input("Nome do item para remover: ")
        for i in inventario:
            if i[0] == nome:
                inventario.remove(i)
                print("Item removido!")
                break


    elif opcao == 3:
        print("\nInventário:")
        for item in inventario:
            print(item[0], item [1])
        

    else :
        print("Opção inválida")

