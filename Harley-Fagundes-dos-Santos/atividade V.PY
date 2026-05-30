missoes = []

while True:
    print("\n------ MENU ------")
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar missões por dificuldade")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    match opcao:

        case 1:
            nome = input("Digite o nome da missão: ")
            dificuldade = input("Digite a dificuldade (Fácil, Média ou Difícil): ")

            if dificuldade == "Fácil" or dificuldade == "Média" or dificuldade == "Difícil":
                missao = [nome, dificuldade, "Pendente"]
                missoes.append(missao)
                print("Missão adicionada!")
            else:
                print("Dificuldade inválida!")

        case 2:
            nome = input("Digite o nome da missão que deseja remover: ")

            encontrada = False

            for missao in missoes:
                if missao[0] == nome:
                    missoes.remove(missao)
                    encontrada = True
                    print("Missão removida!")
                    break

            if encontrada == False:
                print("Missão não encontrada!")

        case 3:
            nome = input("Digite o nome da missão concluída: ")

            encontrada = False

            for missao in missoes:
                if missao[0] == nome:
                    nova_missao = [missao[0], missao[1], "Concluída"]

                    missoes.remove(missao)
                    missoes.append(nova_missao)

                    encontrada = True
                    print("Missão concluída!")
                    break

            if encontrada == False:
                print("Missão não encontrada!")

        case 4:
            if missoes == []:
                print("Nenhuma missão cadastrada.")
            else:
                for missao in missoes:
                    print(missao)

        case 5:
            dificuldade = input("Digite a dificuldade que deseja ver: ")

            if dificuldade == "Fácil" or dificuldade == "Média" or dificuldade == "Difícil":

                for missao in missoes:
                    if missao[1] == dificuldade:
                        print(missao)

            else:
                print("Dificuldade inválida!")

        case 6:
            print("Programa encerrado.")
            break

        case _:
            print("Opção inválida!")