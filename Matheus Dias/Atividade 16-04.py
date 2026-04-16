missoes = [None] * 100  # Não soube como começar então o ChatGPT deu a ideia de começar criando um "vetor" com 100 espaços vazios
total_missoes = 0
continuar = True

while continuar:
    print("\n--- MENU DE MISSÕES ---")
    print("1. Adicionar missão")
    print("2. Remover missão")
    print("3. Concluir missão")
    print("4. Listar missões")
    print("5. Mostrar missões por dificuldade")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")

    # 1. ADICIONAR MISSÃO
    if opcao == "1":
        nome = input("Nome da missão: ")
        dif = input("Dificuldade (Fácil, Média, Difícil): ")

        if dif == "Fácil" or dif == "fácil" or dif == "Média" or dif == "média" or dif == "Difícil" or dif == "difícil":
            missoes[total_missoes] = (nome, dif, "Pendente")
            total_missoes += 1
            print("Missão adicionada!")
        else:
            print("Erro: Dificuldade inválida!")

    # 2. REMOVER MISSÃO
    elif opcao == "2":
        nome_busca = input("Nome da missão para remover: ")
        indice_remover = -1
        
        # Procura a missão pelo nome
        for i in range(total_missoes):
            if missoes[i][0] == nome_busca:
                indice_remover = i
                break
        
        if indice_remover != -1:
            for i in range(indice_remover, total_missoes - 1):
                missoes[i] = missoes[i+1]
            total_missoes -= 1
            print("Missão removida!")
        else:
            print("Erro: Missão não encontrada.")

    # 3. CONCLUIR MISSÃO
    elif opcao == "3":
        nome_busca = input("Nome da missão concluída: ")
        encontrou = False
        
        for i in range(total_missoes):
            if missoes[i][0] == nome_busca:
                nome_m, dif_m, status_m = missoes[i]
                missoes[i] = (nome_m, dif_m, "Concluída")
                encontrou = True
                print("Status atualizado para Concluída!")
                break
        
        if not encontrou:
            print("Erro: Missão não encontrada.")
            
    # 4. LISTAR MISSÕES
    elif opcao == "4":
        print("\n--- LISTA DE MISSÕES ---")
        for i in range(total_missoes):
            m = missoes[i]
            print(f"Missão: {m[0]} | Dificuldade: {m[1]} | Status: {m[2]}")

    # 5. MOSTRAR POR DIFICULDADE
    elif opcao == "5":
        busca_dif = input("Digite a dificuldade para filtrar: ")
        print(f"\n--- MISSÕES {busca_dif.upper()} ---")
        for i in range(total_missoes):
            if missoes[i][1] == busca_dif:
                print(f"- {missoes[i][0]} (Status: {missoes[i][2]})")

    # 6. SAIR
    elif opcao == "6":
        continuar = False
        print("Saindo...")

    else:
        print("Opção inválida!")