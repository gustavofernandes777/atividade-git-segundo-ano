lista = []

while True:

    print('=================')
    print('     MENU   ')
    print('=================')

    print()

    print("1 - Adcionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar por dificuldade")
    print("6 - Sair")

    print()

    numero=(int(input("Olá querido jogador, Insira um número de 1 a 6: "))) 
    print()

    if numero == 6:   
        break

    elif numero == 1:
        nome_m=(input("Adcione o nome da missão que desejas: "))
        dificuldade=(int(input("Adcione a dificuldade que desejas ( 1, 2 ou 3 ): ")))
        status =(input("Insira status ( pendente ou concluída ): "))

        missao = (nome_m, dificuldade, status)
        lista.append(missao)
        print()

        if dificuldade != 1 and dificuldade != 2 and dificuldade != 3:

                 print("Dificuldade inexistente: ERRO")

    elif numero == 2:
         missao_remove =(input("Remova a missão que desejas: "))

         for m_remove in lista:
            if m_remove [0] == missao_remove:
                lista.remove(m_remove)
                print(f"{missao_remove} removido!")
            else:
                print("Missão inexistente: ERRO")

    elif numero ==3:
         novo_status=(input("Insira o nome da missão que desejas concluir: "))

         for concluida in lista:
             if concluida [0] == novo_status:
                concluida [2] == "Missão concluída"
                print(f"{novo_status} alterado!")

    elif numero ==4:
         print(lista)

    elif numero ==5:
         m_d = (input("Insira uma dificuldade ( 1, 2 ou 3): "))
         
         for m_dificuldade in lista:
              m_dificuldade [1] == m_d
              print(f"{nome_m}!")





         
         
    
    
