print("////// Menu de jogo //////\n")

invent = []
a = 0

while a != 5:
    print("/ 1- Adicionar item /")
    print("/ 2- Remover item /")
    print("/ 3- Mostrar itens /")
    print("/ 4- Alterar quantidade do item /")
    print("/ 5- Sair /")

    a = int(input("Escolha uma opção: "))

    if (a > 5) or (a < 1):
        print("Número inválido! Tente novamente!")

    elif a == 1:
        nome = input("Digite o nome do item: ")
        quant = int(input("Digite a quantidade do item: "))
        item = (nome, quant)
        invent.append(item)

    elif a == 2:
        remover = input("Digite o item que deseja remover: ")
        for i in invent:
            if i[0] == remover:
                invent.remove(i)
                print("Item removido!")
                break

    elif a == 3:
        print("Inventário:", invent)

    elif a == 4:
        alterar = input("Digite o nome do item que deseja alterar: ")
        
        for i in invent:
            if i[0] == alterar:
                nova_quant = int(input("Digite a nova quantidade: "))
                invent.remove(i)
                invent.append((alterar, nova_quant))
                print("Quantidade atualizada!")
                break
            else:
                print("Esse item não foi cardartado: ")
