inven = []

while True:
    print("1- adicionar item")
    print("2- remover item")
    print("3- mostrar inventario")
    print("4- sair")
    
    op = input("escolha: ")
    
    if op == "1":
        nome = input("nome: ")
        qntd = int(input("quantidade: "))
        inven.append((nome, qntd))
    
    elif op == "2":
        nome = input("nome para remover: ")
        for item in inven:
            if item[0] == nome:
                inven.remove(item)
                print("Item removido!")
                break
        else:
            print("Item não encontrado.")
    
    elif op == "3":
        if not inven:
            print("Inventário vazio.")
        else:
            for item in inven:
                print(f"Nome: {item[0]} | Quantidade: {item[1]}")
    
    elif op == "4":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")