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

        case 3:
            if not cadastro:
                print("Nenhum produto cadastrado para gerar relatório.")
            else:
                print("================================ Relatório de Produtos ================================")
                print(f"{'Produto':<20} | {'Preço Unitário':<15} | {'Quantidade':<12} | {'Total em Estoque':<15}")
                print("-" * 72)
                
                faturamento_total_estimado = 0
                for p in cadastro:
                    total_produto = p[1] * p[2]
                    faturamento_total_estimado += total_produto
                    print(f"{p[0]:<20} | R$ {p[1]:<12.2f} | {p[2]:<12} | R$ {total_produto:<12.2f}")
                
                print("-" * 72)
                print(f"Valor total investido no estoque do estabelecimento: R$ {faturamento_total_estimado:.2f}")
       
        case 4:
            print("Encerrando o programa....")
            break





