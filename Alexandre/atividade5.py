nome = []
dificuldade = []
status = []

while True:
    print("\n1 - Adicionar Missao\n2 - Remover Missao\n3 - Concluir Missao\n4 - Listar missoes\n5 - Mostrar missoes por dificuldade\n6 - Sair")
    opcao = int(input("Digite a opção escolhida: "))
    if opcao == 6:
        print("Voce saiu do codigo.")
        break
    elif opcao == 1:
        nome_missao = input("Digite o nome da missao: ")
        dificuldade_missao = input("Digite a dificuldade da missao[Dificil, Medio ou Facil]: ")
        nome.append(nome_missao)
        if dificuldade_missao.upper() == "DIFICIL" or dificuldade_missao.upper() == "MEDIO" or dificuldade_missao.upper() == "FACIL":
            dificuldade.append(dificuldade_missao.upper())
        else:
            print("Nivel de dificuldade indisponivel.")
        status.append("Pendente")

    elif opcao == 2:
        nome_missao = input("Digite exatamente o nome da missao, do mesmo jeito pfv: ")
        localizacao = nome.index(nome_missao)
        del nome[localizacao]
        del dificuldade[localizacao]
    
    elif opcao == 3:
        nome_missao = input("Digite o nome, exatamente o nome da missao: ")
        print("Status da Missão Atualizado!")
        localizacao = nome.index(nome_missao)
        if status[localizacao] == "Pendente":
            status[localizacao] = "Concluido"
        elif status[localizacao] == "Concluido":
            status[localizacao] = "Pendente"
    elif opcao == 4:
        for a, b, c in zip(nome, dificuldade, status):
            print(f"\nMissao: {a}, Dificuldade: {b}, Status: {c}\n")
    elif opcao == 5:
        dif = input("Digite a dificuldade da missao[Dificil, Medio ou Facil]: ").upper()
        lista_de_localizacao = []
        for y in range(len(dificuldade)):
            if dificuldade[y] == dif:
                print(f"Missoes {dif}: ")
                print(nome[y])
                print("\n")
    else:
        print("\nOpção Invalida.\n")