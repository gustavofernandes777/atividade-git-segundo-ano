lista = []


while True:
    print("\n1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missão")
    print("5 - Mostrar missão por dificuldade")
    print("6 - Sair")
   
    a = int(input("Escolha uma opção: "))


    match a:


        case 1:
            name = input("Nome da missão: ")
            dfc = input("Dificuldade (Fácil, Média ou Difícil): ")


            if dfc not in ["Fácil", "Média", "Difícil", "fácil", "média", "difícil"]:
                print("Erro, dificuldade inválida.")
            else:
                lista.append([name, dfc, "Pendente"])
                print("Missão adicionada!")


        case 2:
            remove = input("Qual missão você quer remover? ")


            for i in lista:
                if i[0] == remove:
                    lista.remove(i)
                    print("Missão removida!")
                    break
            else:
                print("Missão não encontrada.")


        case 3:
            concluir = input("Qual missão deseja concluir? ")


            for i in lista:
                if i[0] == concluir:
                    i[2] = "Concluída"
                    print("Missão concluída!")
                    break
            else:
                print("Missão não encontrada.")


        case 4:
            if not lista:
                print("Nenhuma missão cadastrada.")
            else:
                for i in lista:
                    print(f"Nome: {i[0]} | Dificuldade: {i[1]} | Status: {i[2]}")


        case 5:
            busca = input("Digite a dificuldade (Fácil, Média ou Difícil): ")


            if busca not in ["Fácil", "Média", "Difícil", "fácil", "média", "difícil"]:
                print("Dificuldade inválida.")
            else:
                achou = False
                for i in lista:
                    if i[1] == busca:
                        print(f"Nome: {i[0]} | Status: {i[2]}")
                        achou = True
                if not achou:
                    print("Nenhuma missão encontrada nessa dificuldade.")


        case 6:
            print("Programa finalizado...")
            break

