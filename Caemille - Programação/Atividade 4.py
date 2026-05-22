lista = []


while True:
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Alterar a quantidade de itens")
    print("5 - Sair")


    decisao = int (input("Escolha uma opção: "))


    if decisao == 1:
        nome = input("Digite o nome do item: ")
        quant = int (input("Digite a quantidade: "))

        item = (nome, quant)
        lista.append(item)
        print(f"{nome} adicionado {quant} vezes!")

    elif decisao == 2:
        nome = input("Digite o nome do item para remover: ")
        
        for item in lista:
            if nome == item [0]:
                lista.remove(item)
                print(f"{nome} removido!")
    
    elif decisao == 3:
        print(lista)

    elif decisao == 4:
        nome = input("Digite o nome do item que deseja alterar a quantidade:")
        
        for item in lista:
            if item[0] == nome:
                lista.remove (item)
                alteraçao = int (input (f"Digite a nova quantidade de {nome}:"))
                item = (nome, alteraçao)
                lista.append (item)
                print(f"A nova quantidade do {nome} é {alteraçao}")
                break
        
        else:
            print("Item não encontrado.")

    elif decisao == 5:
        print("Saida concluída!")
        break