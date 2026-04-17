missoes = []

while True:
    print("\n1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome da missão: ")
        dificuldade = input("Dificuldade (facil, media, dificil): ")

        if dificuldade in ["facil", "media", "dificil"]:
            missoes.append([nome, dificuldade, "pendente"])
        else:
            print("Dificuldade inválida!")

    elif op == "2":
        nome = input("Nome da missão para remover: ")
        for m in missoes:
            if m[0] == nome:
                missoes.remove(m)
                break

    elif op == "3":
        nome = input("Nome da missão para concluir: ")
        for m in missoes:
            if m[0] == nome:
                m[2] = "concluida"

    elif op == "4":
        for m in missoes:
            print(m)

    elif op == "5":
        break


