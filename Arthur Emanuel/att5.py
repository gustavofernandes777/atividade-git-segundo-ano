alter = 0

lista = []

while alter != 6: 
    print("1 - Adicionar missão\n"
        "2 - Remover missão\n"
        "3 - Concluir missão\n"
        "4 - Listar missões\n"
        "5 - Mostrar missões por dificuldade\n"
        "6 - Sair\n")
    
    alter = int(input("Escolha uma das opções: "))

    match alter:
        case 1: 
            print("Você deseja adicionar missão")
            addmissao = str(input("Digite qual missão deseja enfrentar: "))
            adddificult = int(input("Digite um número para mostrar a dificuldade que deseja a dificuldade da missão: \n 1 - Fácil \n 2 - Médio \n 3 - Difícil\n : "))
            if adddificult == 1:
                adddificult = "Fácil"

            elif adddificult == 2:
                adddificult = "Médio"

            elif adddificult == 3:
                adddificult = "Difícil"
            
            else:
                print("Ocorreeu um erro (o nível de dificuldade selecionado é inexistente)")

            status = "Pendente"

            tuplamissao = [addmissao, adddificult, status]
            lista.append(tuplamissao)

        case 2:
            print("Você escolheu remover missão")
            removmissao = str(input("Digite a missão que deseja remover: "))
            for missao in lista:
                if missao[0] == removmissao:
                    lista.remove(missao)
                else:
                    print("Missão não encontrada")

        case 3:
            print("Você escolheu concluir a missão")
            conclumissao = str(input("Digite qual missão deseja concluir: "))
            for missao in lista:
                if missao[0] == conclumissao:
                    missao[2] = "concluida"
                else:
                    print("Missão não encontrada.")    
                
        case 4:
            print("Você escolheu listar as missões")
            print(lista)
        
        case 5: 
            mostrarmissao = int(input(" 1 - Fácil\n 2 - Médio\n 3 - Difícil\n Você escolheu visualizar as missões por dificuldade: "))
            if mostrarmissao == 1:
                mostrarmissao = "Fácil"

            elif mostrarmissao == 2:
                mostrarmissao = "Médio"

            elif mostrarmissao == 3:
                mostrarmissao = "Difícil"

            else:
                print("Error(non-exist difficulty)")

            for missao in lista:
                if missao[1] == mostrarmissao:
                    print(missao)
        case 6:
            print("Finalizando programa...")
            break
