inv = [( )]
while True:
    menu = input (" 1 - Adicionar item\n 2-Remover item\n 3 - Mostrar inventário\n 4 - Alterar quantidade\n 5 - Sair\n")
    if menu == "1":
        nome = input ("nome: ")
        qtd = int (input("qtd: "))
        inv.append([nome,qtd])
    elif menu == "2":
        nome = input ("nome")
        for item in inv:
            if item [0]== nome:
                inv.remove (item)
    elif menu == "3":
        for item in inv:
            print (item)
    elif menu == "4":
      for item in inv:
                for item [1] in inv:
                    inv = (input("Qual quantidade deseja alterar"))
    else:
        break