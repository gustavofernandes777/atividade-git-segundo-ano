missoes = []
 
while True:
    print("\n----MENU----")
    print("1. Adicionar missão")
    print("2. Remover missão")
    print("3. Concluir missão")
    print("4. Listar missões")
    print("5. Mostrar missões por dificuldade")
    print("6. Sair")

    op = input("escolha: ")

    if op== "1":
        nome = input("Nome da missão: ")
        dificuldade = input("Dificuldade (Fácil, Média, Díficil): ")
        
        status = "Pendente"
        missoes.append([nome, dificuldade, status])
            
    elif op == "2":
        nome = input("Nome da missão para remover: ")
        for m in missoes:
            if m [0] == nome:
                missoes. remove(m)
                print("Removida!")
                break
                
    elif op == "3":
        nome = input("Nome da missão para concluir: ")        
        for m in missoes:
            if m [0] == nome:
                m[2] = "Concluída"
                print("Missão concluída!")
                break
                
    elif op == "4":
        for m in missoes:
            print (m)
            
    elif op == "5":
        dificuldade = input("Qual dificuldade quer ver?: ")
        for m in missoes:
            if m[1] == dificuldade:
                print(m)
                
    elif op == "6":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")