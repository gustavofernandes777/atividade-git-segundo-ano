missoes = []


def dificuldade_valida(dificuldade):
    return dificuldade in ["Fácil", "Média", "Difícil"]

def adicionar_missao():
    nome = input("Digite o nome da missão: ")
    dificuldade = input("Digite a dificuldade (Fácil, Média, Difícil): ")

    if dificuldade_valida(dificuldade):
        missao = [nome, dificuldade, "Pendente"]
        missoes.append(missao)
        print("Missão adicionada com sucesso!")
    else:
        print("Erro: dificuldade inválida!")

def remover_missao():
    nome = input("Digite o nome da missão para remover: ")
    
    for missao in missoes:
        if missao[0] == nome:
            missoes.remove(missao)
            print("Missão removida com sucesso!")
            return
    
    print("Erro: missão não encontrada!")

def concluir_missao():
    nome = input("Digite o nome da missão para concluir: ")

    for i in range(len(missoes)):
        if missoes[i][0] == nome:
            nova_missao = [missoes[i][0], missoes[i][1], "Concluída"]
            missoes[i] = nova_missao
            print("Missão concluída com sucesso!")
            return

    print("Erro: missão não encontrada!")


def listar_missoes():
    if len(missoes) == 0:
        print("Nenhuma missão cadastrada.")
    else:
        print("\n--- Lista de Missões ---")
        for missao in missoes:
            print("Nome:", missao[0], "| Dificuldade:", missao[1], "| Status:", missao[2])


def mostrar_por_dificuldade():
    dificuldade = input("Digite a dificuldade (Fácil, Média, Difícil): ")

    if not dificuldade_valida(dificuldade):
        print("Erro: dificuldade inválida!")
        return

    print(f"\n--- Missões {dificuldade} ---")
    encontrou = False

    for missao in missoes:
        if missao[1] == dificuldade:
            print("Nome:", missao[0], "| Status:", missao[2])
            encontrou = True

    if not encontrou:
        print("Nenhuma missão encontrada.")


while True:
    print("\n===== MENU =====")
    print("1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Mostrar missões por dificuldade")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_missao()
    elif opcao == "2":
        remover_missao()
    elif opcao == "3":
        concluir_missao()
    elif opcao == "4":
        listar_missoes()
    elif opcao == "5":
        mostrar_por_dificuldade()
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")