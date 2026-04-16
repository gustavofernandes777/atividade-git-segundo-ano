lista = []
while True:
    print(" 1 - Adicionar item\n 2 - Remover item\n 3 - Mostrar item\n 4 - Alterar quantidade\n 5 - Sair\n ")
    opcao = input()


    if opcao == "1":
        nome = (input("Digite o nome do item: "))
        qtde = (input("Digite a quantidade: "))
        lista.append ([nome, qtde])
   
    elif opcao == "2":
        nome = (input("Qual item deseja remover? "))
        for item in lista:
            if item [0] == nome:
                lista.remove(item)
                break


    elif opcao == "3":
        if len(lista) == 0:
            print ("Lista vazia")
        else:
            for item in lista:
                print("Item:", item[0], "Quantidade:", item [1])


    elif opcao == "4":
        nome = (input("Qual item deseja alterar? "))
        for item in lista:
            if item [0] == nome:
                novaqtde = int(input("Digite a nova quantidade: "))
                lista.remove(item)
                lista.append((nome, novaqtde))
                print("Item atualizado: ", item [0], item [1])
                break
            else:
                print("Item não encontrado")
    else:
        print("Você saiu")
        break



