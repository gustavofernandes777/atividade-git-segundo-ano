missoes = []

while True:
    opcao = input("\n1-Adicionar\n2-Remover\n3-Concluir\n4-Listar\n5-Por dificuldade\n6-Sair\nEscolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        d = input("Dificuldade (Fácil/Média/Difícil): ")
        if d not in ["Fácil","Média","Difícil"]:
            print("Erro!")
        else:
            missoes.append([nome,d,"Pendente"])

    elif opcao == "2":
        nome = input("Nome: ")
        ok = False
        for m in missoes:
            if m[0] == nome:
                missoes.remove(m)
                ok = True
                break
        print("Removida!" if ok else "Erro!")

    elif opcao == "3":
        nome = input("Nome: ")
        ok = False
        for i in range(len(missoes)):
            if missoes[i][0] == nome:
                missoes[i][2] = "Concluída"
                ok = True
                break
        print("Concluída!" if ok else "Erro!")

    elif opcao == "4":
        for m in missoes:
            print(m)

    elif opcao == "5":
        d = input("Dificuldade: ")
        for m in missoes:
            if m[1] == d:
                print(m)

    elif opcao == "6":
        break

    else:
        print("Inválido!")