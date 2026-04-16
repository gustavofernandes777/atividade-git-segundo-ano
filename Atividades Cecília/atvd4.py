inv= []

while True:
    print("/n 1- Adicionar item")
    print("2-Remover item")
    print("3-Mostrar inventário")
    print("4- Alterar nome do item")
    print("5-Sair")
    
    opcão= input("Escolha: ")

    if opcão=="1":
        nome=input("Nome: ")
        quantidade= int(input("Quantidade: "))
        inv.append((nome, quantidade))

    elif opcão=="2":
        nome=input("nome para remover: ")
        for item in inv:
            if item [0]==nome:
                inv.remove(item)

    elif opcão=="3":
        for item in inv:
            print(item)
    
    elif opcão=="4":
        nome=input("Nome para alterar: ")
        for item in inv:
            quantidade= int(input("Quantidade do intem: "))
            if item [0]==nome:
                inv[0]=(item,quantidade)                                                            

    elif opcão=="5":
        break