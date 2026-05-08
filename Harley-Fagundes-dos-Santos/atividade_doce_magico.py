itens = {}
tvendas = {}
contas = {}
tganho = 0
tcontas = 0
senha_mestre = 147

'''while True:
    print("\nEmpresa-doce mágico\n")
    print("1-Repositor")
    print("2-Funcionário")
    print("3-Contador")
    print("4-Chefe")
    print("0-Sair do sistema")
    pessoa = int(input("Quem deseja acessar o sistema? "))
    if pessoa == 1:
        senha_rep = input("crie uma senha: ")
    elif pessoa == 2:
        senha_func = input("crie uma senha: ")
    elif pessoa == 3:
        senha_cont = input("crie uma senha: ")
    elif pessoa == 4:
        senha_chefe = input("crie uma senha: ")
    else:
        print ("opção inválida")
        exit()
'''


while True:
    print("\nEmpresa-doce mágico\n")
    print("1-Repositor")
    print("2-Funcionário")
    print("3-Contador")
    print("4-Chefe")
    print("5-Cadastro de funcionario")
    print("0-Sair do sistema")

    pessoa = int(input("Quem deseja acessar o sistema? "))

    if pessoa == 0:
        print("Encerrando sistema...")
        break

    if 0 < pessoa <= 5:
        senha = int(input("Digite a senha: "))
    else:
        print("Opção inválida")
        continue

    if senha == 1234 and pessoa == 1:
        while True:
            print("\n--- MENU REPOSITOR ---")
            print("1 - Adicionar novo item")
            print("2 - Alterar quantidade")
            print("0 - Voltar")

            op_rep = int(input())

            if op_rep == 1:
                nomep = input("Produto: ")
                quantp = int(input("Quantidade: "))
                valorp = float(input("Preço: "))
                itens[nomep] = {"quantidade": quantp, "valor": valorp}

            elif op_rep == 2:
                nomep = input("Qual item deseja alterar? ")
                if nomep in itens:
                    novaquant = int(input("Nova quantidade: "))
                    itens[nomep]["quantidade"] = novaquant
                else:
                    print("Item não encontrado")

            else:
                break

            print("\nEstoque:")
            for nomep, dados in itens.items():
                print(nomep, "-", dados["quantidade"], "unidades à R$", dados["valor"])

    elif senha == 1233 and pessoa == 2:
        while True:
            print("\n--- MENU FUNCIONÁRIO ---")
            print("1 - Registrar venda")
            print("0 - Voltar")

            op_func = int(input("Escolha: "))

            if op_func == 1:
                nomep = input("Produto vendido: ")

                if nomep in itens:
                    quantr = int(input("Quantidade vendida: "))

                    if itens[nomep]["quantidade"] >= quantr:
                        itens[nomep]["quantidade"] -= quantr

                        preco = itens[nomep]["valor"]
                        venda = preco * quantr
                        tganho += venda

                        if nomep not in tvendas:
                            tvendas[nomep] = {"vendidos": 0, "total": 0}

                        tvendas[nomep]["vendidos"] += quantr
                        tvendas[nomep]["total"] += venda

                        print(f"Venda realizada! Valor: R${venda}")
                    else:
                        print("Estoque insuficiente!")
                else:
                    print("Produto não existe")

            else:
                break

            print("\nEstoque atual:")
            for nomep, dados in itens.items():
                print(nomep, "-", dados["quantidade"], "unidades à R$", dados["valor"])

    elif senha == 2000 and pessoa == 3:
        while True:
            print("\n--- MENU DO CONTADOR ---")
            print("1 - Ver vendas")
            print("2 - Adicionar contas")
            print("3 - Ver contas")
            print("4 - Ver lucro")
            print("0 - Sair")

            op_contador = int(input("Escolha: "))

            if op_contador == 1:
                print("\nRelatório de vendas:")
                for nomep, dados in tvendas.items():
                    print(nomep, "- vendidos:", dados["vendidos"], "| total: R$", dados["total"])

            elif op_contador == 2:
                tipoconta = input("Tipo da conta: ")
                valorconta = float(input("Valor: "))
                contas[tipoconta] = valorconta
                tcontas += valorconta

            elif op_contador == 3:
                print("\nContas:")
                for tipo, valor in contas.items():
                    print(tipo, "- R$", valor)
                print("Total de contas: R$", tcontas)

            elif op_contador == 4:
                lucro = tganho - tcontas
                print(f"Lucro atual: R${lucro}")

            else:
                break

    elif senha == 9999 and pessoa == 4:
        while True:
            print("\n--- MENU DO CHEFE ---")
            print("1 - Ver estoque completo")
            print("2 - Ver relatório de vendas")
            print("3 - Ver contas")
            print("4 - Ver lucro geral")
            print("0 - Sair")

            op_chefe = int(input("Escolha: "))

            if op_chefe == 1:
                print("\nEstoque completo:")
                for nomep, dados in itens.items():
                    print(nomep, "-", dados["quantidade"], "unidades à R$", dados["valor"])

            elif op_chefe == 2:
                print("\nRelatório de vendas:")
                for nomep, dados in tvendas.items():
                    print(nomep, "- vendidos:", dados["vendidos"], "| total: R$", dados["total"])

            elif op_chefe == 3:
                print("\nContas:")
                for tipo, valor in contas.items():
                    print(tipo, "- R$", valor)
                print("Total de contas: R$", tcontas)

            elif op_chefe == 4:
                lucro = tganho - tcontas
                print(f"\nLucro total da empresa: R${lucro}")

            else:
                break
    elif pessoa == 5:
        if senha == senha_mestre:
            print("\nEmpresa-doce mágico\n")
            print("1-Repositor")
            print("2-Funcionário")
            print("3-Contador")
            print("4-Chefe")
            print("0-Sair do sistema")
            pessoa = int(input("Quem deseja acessar o sistema? "))
            if pessoa == 1:
                senha_rep = input("crie uma senha: ")
            elif pessoa == 2:
                senha_func = input("crie uma senha: ")
            elif pessoa == 3:
                senha_cont = input("crie uma senha: ")
            elif pessoa == 4:
                senha_chefe = input("crie uma senha: ")
            else:
                print ("opção inválida")
                exit()
        else:
            print("Acesso negado")

    else:
        print("Acesso negado")