escolha = 10
lista = [] 

while escolha != 6:

    print("-----  MENU  -----")
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar missões por dificuldade")
    print("6 - Sair")

    escolha = int(input("Escolha uma opção"))

    match escolha:
        case 1:

            nome = input("Insira o nome da missão:")
            dificuldade = input("Insira a dificuldade da missão |facil / media / dificil|")
            status = input("Insira o status da missão (pendente / concluida)")

            missao = [nome, dificuldade, status]

            lista.append(missao)

        case 2:
            
            remover = input("Digite o nome da missão que deseja remover: ")

            for item_a_remover in lista:
                if item_a_remover[0] == remover:
                    lista.remove(item_a_remover)

        case 3:

            nome_concluir = input("Digite o nome da missão que deseja concluir: ")

            for missao in lista:
                if missao[0] == nome_concluir:
                    missao[2] = "concluida"


        case 4:

            print(lista)

        case 5:

            dificuldade_busca = input("Digite a dificuldade (facil / media / dificil): ")

            for m in lista:
                if m[1] == dificuldade_busca:
                    print(m)