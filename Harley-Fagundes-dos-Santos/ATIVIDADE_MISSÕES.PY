inventario = []
while True:
    print("-" * 10 + "MENU" + "-"*10)
    print("1-adicionar missão")
    print("2-excluir missão")
    print("3-concluir missões")
    print("4-listar missões")
    print("5-mostrar missões por dificuldade")
    print("6-sair")
    menu = int(input("digite a função que você deseja fazer:"))
    
    match menu:
        case 1:
            nome = input("digite o nome da missão que deseja adicionar.\n")
            dificuldade = int(input("digite a dificuldade da missão que deseja adicionar.\n"))
            if dificuldade = 1:
                
            itens = [nome, dificuldade]
            inventario.append(itens)
        case 2:
            item_rem = input("digite o nome do item que deseja remover\n")
            quant_rem = int(input("digite a quantidade do item que desja remover\n"))
            itens_rem = [item_rem, quant_rem]
            inventario.remove(itens_rem)
        case 3:
            for i in inventario:
                print(i)
        case 4:
            nome_alter = input("digite o nome do produto que deseja alterar: ")
            for nome in inventario:
                if nome[0] == nome_alter:
                    nova_quant = input("digite a nova quantidade: ")
                    nome[1] = nova_quant
                    break
                else:
                    print("item não encontrado...")
        case 5:
            print("desligando")
            break
        case 6:

        case _:
            print("esta opção não existe.")
            continue