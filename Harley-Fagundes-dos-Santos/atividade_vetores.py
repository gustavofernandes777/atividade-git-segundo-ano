inventario = []
while True:
    print("-" * 10 + "MENU" + "-"*10)
    print("1-adicionar item")
    print("2-excluir item")
    print("3-mostrar inventário")
    print("4-alterar item")
    print("5-sair")
    menu = int(input("digite a função que você deseja fazer:"))
    
    if menu == 1:
        nome = input("digite o nome do item que deseja adicionar.\n")
        quant = int(input("digite a quantidade do item que deseja adicionar.\n"))
        itens = [nome, quant]
        inventario.append(itens)
    elif menu == 2:
        item_rem = input("digite o nome do item que deseja remover\n")
        quant_rem = int(input("digite a quantidade do item que desja remover\n"))
        itens_rem = [item_rem, quant_rem]
        inventario.remove(itens_rem)
    elif menu == 3:
        for i in inventario:
            print(i)
    elif menu == 4:
        nome_alter = input("digite o nome do produto que deseja alterar: ")
        for nome in inventario:
            if nome[0] == nome_alter:
                nova_quant = input("digite a nova quantidade: ")
                nome[1] = nova_quant
                break
            else:
                print("item não encontrado...")
    elif menu == 5:
        print("desligando")
        break
    else:
        print("esta opção não existe.")
        continue