missoes = []

while True:

    
    print("\n===== MENU =====")
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar missões por dificuldade")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

   
    if opcao == "1":

        nome = input("Nome da missão: ")
        dificuldade = input("Dificuldade (Fácil, Média ou Difícil): ")

    
        if dificuldade == "Fácil" or dificuldade == "Média" or dificuldade == "Difícil":

            
            missao = [nome, dificuldade, "Pendente"]

           
           
            missoes.append(missao)

            print("Missão adicionada!")

        else:
            print("Dificuldade inválida!")

   
   
    elif opcao == "2":

        nome = input("Digite o nome da missão: ")

        encontrou = False

        for missao in missoes:

            if missao[0] == nome:

                missoes.remove(missao)

                encontrou = True

                print("Missão removida!")

        if encontrou == False:
            print("Missão não encontrada!")

    
    elif opcao == "3":

        nome = input("Digite o nome da missão: ")

        encontrou = False

        for i in range(len(missoes)):

            if missoes[i][0] == nome:

                
                nova_missao = [
                    missoes[i][0],
                    missoes[i][1],
                    "Concluída"
                ]

                missoes[i] = nova_missao

                encontrou = True

                print("Missão concluída!")

        if encontrou == False:
            print("Missão não encontrada!")

    
    elif opcao == "4":

        if len(missoes) == 0:

            print("Nenhuma missão cadastrada.")

        else:

            print("\n===== MISSÕES =====")

            for missao in missoes:

                print("Nome:", missao[0])
                print("Dificuldade:", missao[1])
                print("Status:", missao[2])
                print("------------------")

    elif opcao == "5":

        dificuldade = input("Digite a dificuldade: ")

        encontrou = False

        for missao in missoes:

            if missao[1] == dificuldade:

                print("Nome:", missao[0])
                print("Status:", missao[2])
                print("------------------")

                encontrou = True

        if encontrou == False:
            print("Nenhuma missão encontrada!")

 
    elif opcao == "6":

        print("Programa encerrado.")
        break

    
    else:

        print("Opção inválida!")
        #pedi ajuda pro colega tmbem para organizar o código, mas a lógica e a estrutura do código foi feita por mim.