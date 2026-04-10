escolha = 10
lista = []

while escolha != 4:

    print("----- MENU -----")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")

    escolha = int(input("Escolha uma opção:"))

    if escolha > 4 or escolha < 1:
        print("Opcão inválida, escolha novamente.")

    elif escolha == 1:
        adicionar = input("Digite o nome do item:")
        quantidade = int(input("Digite a quantidade de itens:"))

        item = (adicionar, quantidade)

        lista.append(item)

    elif escolha == 2:
        remover = input("Digite o nome do item que deseja remover:")

        for item_a_remover in lista:
            item_a_remover
            if item_a_remover[0] == remover:
                lista.remove(item_a_remover)

    elif escolha == 3:
        print(lista)

