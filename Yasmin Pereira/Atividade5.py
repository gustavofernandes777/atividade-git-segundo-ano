Lista = []
concluido = []

while True:
    print("\nMenu:")
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar missões por dificuldade")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        nome = input("Digite o nome da missão: ")

        dificuldade = ""
        while dificuldade != "Fácil" and dificuldade != "Médio" and dificuldade != "Difícil":
            dificuldade = input("Digite o nível de dificuldade: ")

        missao = [nome, dificuldade, "pendente"]
        Lista.append(missao)

    if opcao == 2:
        nome = input("Digite o nome da missão que deseja remover: ") 
        for missao in Lista:
             if nome == missao[0]:
                Lista.remove(missao)
                print(f"Missão {nome} removida com sucesso!")
                break
             
    if opcao == 3:
        nome = input("Digite o nome da missão que deseja concluir: ")
        for missao in Lista:
            if missao[0] == nome:
                 missao[2] = "concluido"
                 concluido.append(missao)
                 print(f"Missão {nome} concluída com sucesso!")
                 break
            else:
                print("Esta missão já foi concluída ou não existe...")

    if opcao == 4:
        print("Missões: ")
        for missao in Lista:
            print(missao)

    if opcao == 5:
        dificuldade = input("Digite a dificuldade:")
        for missao in Lista:
            if missao[1] == dificuldade:
                print(missao)

    if opcao == 6:
        print("Saindo...")
        break