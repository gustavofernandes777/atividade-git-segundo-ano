cadastro = []

while True:
    print("=================")
    print("MENU DA MINI LOJA")
    print("=================")
    print("1-Cadastrar Produto")
    print("2-Situação do Estoque")
    print("3-Exibir Relatório")
    print("4-Sair")

    print()

    opcao = int(input("Escolha uma opcão do menu: "))

    print()

    match opcao:
        case 1:
            Nome_pro = input("Informe o Nome do Produto: ")
            Preço_pro = input(f"Informe o Preço do Produto: ")
            Quant_pro = int(input("Informe a Quantidade de Produtos: "))

            produtos = [Nome_pro, Preço_pro, Quant_pro]
            cadastro.append(produtos)
            print("Produtos cadastrado!!!!")

        case 2:
            

        
        case 4:
            print("Encerrando o programa....")
            break





