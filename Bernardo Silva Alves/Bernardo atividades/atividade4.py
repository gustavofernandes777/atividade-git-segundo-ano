escolha = 10
lista = []

while escolha != 4:

    print("----- MENU -----")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4 - Sair")
    print("5 - Alterar quantidade")

    escolha = int(input("Escolha uma opção:"))

    if escolha > 5 or escolha < 1:
        print("Opcão inválida, escolha novamente.")

    elif escolha == 1:
        adicionar = input("Digite o nome do item:")
        quantidade = int(input("Digite a quantidade de itens:"))

        item = [adicionar, quantidade]

        lista.append(item)

    elif escolha == 2:
        remover = input("Digite o nome do item que deseja remover:")

        for item_a_remover in lista:
            item_a_remover
            if item_a_remover[0] == remover:
                lista.remove(item_a_remover)

    elif escolha == 3:
        print(lista)

    elif escolha == 5:
        alterar = input("Digite o nome do item que deseja alterar a quantidade:")
        alterar_quantidade = int(input("Digite a quantidade que deseja substituir:"))

        for item_a_remover2 in lista:
            item_a_remover2
            if item_a_remover2[0] == alterar:
                item_a_remover2[1] = alterar_quantidade
                print("Quantidade alterada")


