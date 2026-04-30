menu = []

while True:
    print("|=-=Menu de Missões=-=|")

    print()

    print("1-Adicionar Missão")
    print("2-Remover Missão")
    print("3-Concluir Missão")
    print("4-Listar Missões")
    print("5-Mostrar Missões por Dificuldade")
    print("6-Sair")

    print()

    opcao = int(input("Escolha uma opção do menu de missões: "))

    match opcao:
        case 1:
            nome_missao = input("Informe o nome da missão: ")
            dificul = input("Dificuldade (Fácil/Médio/Difícil): ")

            missao = [nome_missao, dificul, "Pendente"]
            menu.append(missao)
            print("Missão adicionada com sucesso!")

        case 2:
            nome_remover = input("Qual o nome da missão que deseja remover? ")
            for m in menu:
                if m[0] == nome_remover:
                    menu.remove(m)
                    print("missão removida!")
                    break
        case 3:
            nome_concluir = input("Informe o nome da missão concluída: ")
            for m in menu:
                if m[0] == nome_concluir:
                    m[2] = "Concluída"
                    print("Status atualizado!")
                    break

        case 4:
            print("-----LISTA DE MISSÕES-----")

            print()

            for m in menu:
                print(f"Nome: {m[0]} | Dif: {m[1]} | Status: {m[2]}")

        
        case 5:
            dif_busca = input("Missões por dificuldade: ")
            for m in menu:
                if m[1] == dif_busca:
                    print(f"Nome: {m[0]} | Status: {m[2]}")

        case 6:
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida!")    