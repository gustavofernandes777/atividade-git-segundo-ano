print("////// Menu de Missões //////\n")

missoes = []
a = 0

while a != 6:
    print("/ 1- Adicionar missão /")
    print("/ 2- Remover missão /")
    print("/ 3- Concluir missão /")
    print("/ 4- Mostrar missões /")
    print("/ 5- Mostrar por dificuldade /")
    print("/ 6- Sair /")

    a = int(input("Escolha uma opção: "))

    if (a > 6) or (a < 1):
        print("Número inválido! Tente novamente!")

    elif a == 1:
        nome = input("Digite o nome da missão: ")
        dificuldade = input("Digite a dificuldade (Fácil/Média/Difícil): ")

        if dificuldade != "Fácil" and dificuldade != "Média" and dificuldade != "Difícil":
            print("Dificuldade inválida!")
        else:
            missao = [nome, dificuldade, "Pendente"]
            missoes.append(missao)
            print("Missão adicionada!")

    elif a == 2:
        remover = input("Digite o nome da missão que deseja remover: ")

        for m in missoes:
            if m[0] == remover:
                missoes.remove(m)
                print("Missão removida!")
                break

    elif a == 3:
        concluir = input("Digite o nome da missão para concluir: ")

        for m in missoes:
            if m[0] == concluir:
                missoes.remove(m)
                missoes.append([concluir, m[1], "Concluída"])
                print("Missão concluída!")
                break

    elif a == 4:
        print("Missões:", missoes)

    elif a == 5:
        dif = input("Digite a dificuldade: ")

        for m in missoes:
            if m[1] == dif:
                print(m)