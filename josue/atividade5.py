missoes = []
opcao = 0

while opcao != "5":
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == 1:
        nome = input("Nome: ")
        dificuldade = input("Dificuldade (Fácil, Média ou Difícil): ")

        if dificuldade != "Fácil" and dificuldade != "Média" and dificuldade != "Difícil":
            print("Erro: dificuldade inválida!")
        else:
            missoes.append([nome, dificuldade])
            print("Missão adicionada!")

    elif opcao == 2:
        nome = input("Nome da missão: ")

        for m in missoes:
            if m[0] == nome:
                missoes.remove(m)
                print("Missão removida!")
                break
        else:
            print("Erro: missão não encontrada!")

    elif opcao == "3":
        nome = input("Nome da missão: ")

        for m in missoes:
            if m[0] == nome:
                m[2] = "Concluída"
                print("Missão concluída!")
                break
        else:
            print("Erro: missão não encontrada!")

    elif opcao == 4:
        for m in missoes:
            print("Nome:", m[0], "| Dificuldade:", m[1], "| Status:", m[2])

    elif opcao == 5:
        print("Saindo...")

    else:
        print("Opção inválida!")