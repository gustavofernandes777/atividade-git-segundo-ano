escolha = 0
lista = []
while escolha != 6:
    print("1 - Adicionar missão\n"
    "2 - Remover missão\n"
    "3 - Concluir missão\n"
    "4 - Lista de missões\n"
    "5 - Mostrar missões por dificuldade\n"
    "6 - Sair")
    escolha = int(input("Escolha uma opção: "))
    match escolha:
        case 1:
            addm = str(input("Insira o nome da missão: "))
            adddificult = int(input(" 1- Fácil\n 2- Média\n 3- Difícil\nEscolha dificuldade: "))
            if adddificult == 1:
                adddificult = "Fácil"
            elif adddificult == 2:
                adddificult = "Média"
            elif adddificult == 3:
                adddificult = "Difícil"
            else:
                print("Erro (nivel de dificuldade inexistente)")
            status = "Pendente"
            tulpamiss = [addm, adddificult, status]
            lista.append(tulpamiss)
        case 2:
            removmiss = str(input("Insira o nome da missão que deseja remover: "))
            for missão in lista:
                if missão[0] == removmiss:
                    lista.remove(missão)
                else:
                    print("Missão não encontrada!")
        case 3:
            concluirmiss = str(input("Insira o nome da missão que deseja concluir: "))
            for missão in lista:
                if missão[0] == concluirmiss:
                    missão[2] = "Concluida"
                else:
                    print("Missão inexistente!")
        case 4:
            print(lista)
        case 5:
            mostrarmiss = int(input(" 1- Fácil\n 2- Média\n 3- Difícil\nInsira o nivel de missão que deseja visualizar: "))
            if mostrarmiss == 1:
                mostrarmiss = "Fácil"
            elif mostrarmiss == 2:
                mostrarmiss = "Média"
            elif mostrarmiss == 3:
                mostrarmiss = "Difícil"
            else:
                print("Erro (nivel de dificuldade inexistente)")
            for missão in lista:
                if missão[1] == mostrarmiss:
                    print(missão)