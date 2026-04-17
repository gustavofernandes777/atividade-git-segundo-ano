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

        missao = (nome_m, dificuldade)
        lista.append(missao)
        print()

        if dificuldade != 1 and dificuldade != 2 and dificuldade != 3:

                 print("Dificuldade inexistente: ERRO")
    
    
