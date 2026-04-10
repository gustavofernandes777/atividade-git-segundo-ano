lista = []

while True:
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")

    decisão = int (input("Escolha uma opção:"))

    if decisão == 1:
        item = (input("Digite o item para adicionar:"))
        lista.append(item)
        print(f"{item} Adicionado!")

    elif decisão == 2:
        item = (input("Escolha um item para remover:"))
        if item in lista:
            lista.remove(item)
            print(f"{item} Removido!")
        
        else:
            print("Item não encontrado!")
