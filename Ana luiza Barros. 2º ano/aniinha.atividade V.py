lista = []

while True:

    print('=================')
    print('     MENU')
    print('=================')

    print()
    print("1 - Adcionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar por dificuldade")
    print("6 - Sair")
    print()

    numero = int(input("Olá querido jogador, Insira um número de 1 a 6: "))
    print()

    if numero == 6:
        print("Saindo...")
        break

    elif numero == 1:

        nome_m = input("Adcione o nome da missão que desejas: ")
        dificuldade = input("Adcione a dificuldade que desejas (Fácil, Média ou Difícil): ")

        if dificuldade != "Fácil" and dificuldade != "Média" and dificuldade != "Difícil":

            print("Dificuldade inexistente: ERRO")

        else:

            status = "Pendente"
            missao = (nome_m, dificuldade, status)
            lista.append(missao)
            print("Missão adicionada!")

    elif numero == 2:
        missao_remove = input("Remova a missão que desejas: ")

        for m_remove in lista:
            if m_remove[0] == missao_remove:
                lista.remove(m_remove)
                print(f"{missao_remove} removido!")
                break

        else:
            print("Missão inexistente: ERRO")

    elif numero == 3:

        novo_status = input("Insira o nome da missão que desejas concluir: ")

        for concluida in lista:
            if concluida[0] == novo_status:
                nova_missao = (
                    concluida[0],
                    concluida[1],
                    "Concluída"
                )

                lista.remove(concluida)
                lista.append(nova_missao)
                print(f"{novo_status} alterado!")
                break

        else:
            print("Missão inexistente: ERRO")

    elif numero == 4:

        for missao in lista:
            print(missao)

    elif numero == 5:

        m_d = input("Insira uma dificuldade (Fácil, Média ou Difícil): ")

        for m_dificuldade in lista:
            if m_dificuldade[1] == m_d:
                print(m_dificuldade)

    else:
        print("Opção inválida!")




         
         
    
    
