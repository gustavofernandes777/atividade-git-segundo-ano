missoes = []
while True:
    print(" 1-Adicionar missão\n 2-Remover missão\n 3-Concluir missão\n 4-Listar missões\n 5-Mostrar missões por dificuldade\n 6-Sair")
    op = input("Opção: ")
    match op:
        case "1":
            nome = input("Informe o nome da missão: ")
            dif = input("Dificuldade (Fácil, Média, Difícil): ")
            if dif not in ["Fácil", "Média", "Difícil"]:
                print("Erro!")
            else:
                missoes.append([nome, dif, "Pendente"])
        case "2":
            nome = input("Informe o nome da missão: ")
            achou = False
            for m in missoes:
                if m[0] == nome:
                    missoes.remove(m)
                    achou = True
            if not achou:
                print("Não encontrada")
        case "3":
            nome = input("Informe o nome da missão: ")
            for i in range(len(missoes)):
                if missoes[i][0] == nome:
                    missoes[i] = [missoes[i][0], missoes[i][1], "Concluída"]
        case "4":
            for m in missoes:
                print(m)
        case "5":
            dif = input("Informe a dificuldade: ")
            for m in missoes:
                if m[1] == dif:
                    print(m)
        case "6":
            print("Você saiu")
            break
        case _:
            print("Inválido")