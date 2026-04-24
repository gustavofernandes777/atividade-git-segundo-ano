print("---Menu de Missões---")
missoes = []
a = 0

while a != 5:
    print()
    print("1- Adicionar missão")
    print("2- Remover missão")
    print("3- Concluir missão")
    print("4- Listar missões")
    print("5- Mostrar por dificuldade")
    print("6- Sair")
    a = int(input())

    if(a > 6) or (a < 1):
        print("Número invalido! Tente novamente!")

    elif (a == 1):
        nome = input("Digite o nome da missão: ")
        dificuldade = input("Digite a dificuldade (fácil, Media, Difícil): ")

        if dificuldade != "fácil" and dificuldade != "Media" and dificuldade != "Difícil":
            print("Dificuldade inválida!")
        else:
            status = "pendente"
            missao = (nome, dificuldade, status)
            missoes.append(missao)

    elif(a == 2):
        deletar = input("Digite o nome da missão que queira remover: ")
        encontrado = False

        for i in missoes:
            if i[0] == deletar:
                missoes.remove(i)
                encontrado = True
                break

        if not encontrado:
            print("Missão não encontrada!")

    elif(a == 3):
        concluir = input("Digite o nome da missão que queira concluir: ")
        novo_vetor = []
        encontrado = False

        for i in missoes:
            if i[0] == concluir:
                nova_missao = (i[0], i[1], "concluída")
                novo_vetor.append(nova_missao)
                encontrado = True
            else:
                novo_vetor.append(i)

        missoes = novo_vetor

        if not encontrado:
            print("Missão não encontrada!")

    elif(a == 4):
        print("---Lista de Missões---")
        for i in missoes:
            print("Missão:", i[0], "| Dificuldade:", i[1], "| Status:", i[2])

    elif(a == 5):
        dif = input("Digite a dificuldade que deseja ver (fácil, Media, Difícil): ")

        if dif != "fácil" and dif != "Media" and dif != "Difícil":
            print("Dificuldade inválida!")
        else:
            print("---Missões dessa dificuldade---")
            for i in missoes:
                if i[1] == dif:
                    print("Missão:", i[0], "| Status:", i[2])

    elif(a == 6):
        print("Saindo do sistema...")