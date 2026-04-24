lista = []

while True:
    print("========= MENU DO JOGUINHO DA CAH =========")
    print("\n1 - Adicionar missão")
    print("2 - Remover missão")
    print("3 - Concluir missão")
    print("4 - Listar missões")
    print("5 - Listar missões por dificuldade")
    print("6 - Sair")

    decisao = int (input("Digite sua opção:"))

    if decisao == 1:
        nome_missao = (input("Digite o nome da missão que deseja adicionar:"))
        dificuldade = (input(f"Qual a dificuldade da missão {nome_missao}?"))
   
    lista.append (nome_missao)

    missao = (nome_missao, dificuldade, "pendente")
        
    if dificuldade != 'fácil' and dificuldade != 'média' and dificuldade !='difícil':
       print("Erro em adicionar missão!")
       break

    elif decisao == 2:
     nome_missao = (input("Digite o nome da missão que deseja remover:"))
    
     if lista [0] == nome_missao:
         lista.remove(nome_missao)
         print(f"A missão {nome_missao} foi removida com sucesso!")

     elif lista != nome_missao:
         print("Não existe essa missão cadastrada!")
         break
     
    elif decisao == 3:
        "pendente" == "concluída"
        print("Missão Concluída!")

    elif decisao == 4:
        print("Missões: ")
        for missao in lista:
            print(missao)

    elif decisao == 5:
     dificuldade = (input(f"Qual a dificuldade que deseja listar?"))
     print(lista, dificuldade)
   
    elif decisao == 6:
        print("Saindo do menu!")