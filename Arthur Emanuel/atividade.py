alter = 0


lista = []


while alter != 4:
    print("1 - Adicionar item\n"
        "2 - Remover item\n"
        "3 - Remover quantidade de itens\n"
        "4 -  Mostrar inventário\n"
        "5 - Sair\n")
   
    alter = int(input("Escolha um número: "))


    if alter == 1:
        print("Você deseja adicionar item")
        additem = str(input("Insira item: "))
        qtd = int(input("Insira quantidade de itens: "))
        tuplaitem = (additem, qtd)
        lista.append(tuplaitem)


    if alter == 2:
        print("Você escolheu remover item")
        removitem = str(input("Insira o item para remover: "))
        for item in lista:
            if item[0] == removitem:
                lista.remove(item)

    if alter == 3:
        print("Você escolheu remover quantidade de itens")
        removeitem = str(input("Insira o item para remover quantidade: "))
        for item in lista:
            if item[0] == removeitem:
                qtd = int(input("Insira a quantidade a ser removida: "))
                if qtd >= item[1]:
                    lista.remove(item)
                else:
                    lista[lista.index(item)] = (item[0], item[1] - qtd)
    if alter == 4:
        print("Você escolheu mostrar inventário")
        print(lista)