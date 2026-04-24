inventario = []
opcao = 0

while opcao != 5:
    print("1- Adicionar item ")
    print("2- Remover item ")
    print("3- Mostrar itens ")
    print("4- Alterar quantidade do item")
    print("5- Sair")

    opcao = int(input("Escolha uma opção: "))

    if (opcao > 5) or (opcao < 1):
        print("Número inválido! Tente novamente!")

    elif opcao == 1:
        nome = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade do item: "))
        item = (nome, quantidade)
        inventario.append(item)

    elif opcao == 2:
        remover = input("Digite o item que deseja remover: ")
        for i in inventario:
            if i[0] == remover:
                inventario.remove(i)
                print("Item removido!")
                break

    elif opcao == 3:
        print("Inventário:", inventario)

    elif opcao == 4:
        alterar = input("Digite o nome do item que deseja alterar: ")
        
        for i in inventario:
            if i[0] == alterar:
                nova_quant = int(input("Digite a nova quantidade: "))
                inventario.remove(i)
                inventario.append((alterar, nova_quant))
                print("Quantidade atualizada!")
                break
            else:
                print("Esse item não foi cardartado: ")
