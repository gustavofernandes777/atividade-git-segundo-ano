missoes = []

while True:
    print("\n1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar todas")
    print("5 - Listar por dificuldade")
    print("6 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome da missão: ")
        dificuldade = input("Dificuldade (facil, medio, dificil): ").lower()

        if dificuldade not in ["facil", "medio", "dificil"]:
            print("Dificuldade inválida!")
        else:
            missoes.append((nome, dificuldade, "pendente"))

    elif opcao == "2":
        nome = input("Nome da missão para remover: ")

        for m in missoes:
            if m[0] == nome:
                missoes.remove(m)
                print("Missão removida!")
                break
        else:
            print("Missão não encontrada.")

    elif opcao == "3":
        nome = input("Nome da missão para concluir: ")
        nova_lista = []

        for m in missoes:
            if m[0] == nome:
                nova_lista.append((m[0], m[1], "concluida"))
                print("Missão concluída!")
            else:
                nova_lista.append(m)

        missoes = nova_lista

    elif opcao == "4":
        if len(missoes) == 0:
            print("Nenhuma missão.")
        else:
            for m in missoes:
                print(f"Nome: {m[0]} | Dificuldade: {m[1]} | Status: {m[2]}")

    elif opcao == "5":
        dif = input("Qual dificuldade deseja ver? ").lower()

        for m in missoes:
            if m[1] == dif:
                print(f"Nome: {m[0]} | Status: {m[2]}")

    elif opcao == "6":
        break

    else:
        print("Opção inválida!")