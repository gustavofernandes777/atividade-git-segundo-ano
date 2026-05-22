while True:
    print("\n1- Adicionar")
    print("2-Remover")
    print("3-Concluir")
    print("4-Listar")
    print("5-Filtra")
    print("6-Sair")
    
    
    op = input("Escolha: ")
    
    if op ==  "1":
        nome = input("Nome: ")
        dif = input("Dificuldade: ")
        
        if dif == "Fácil" or dif == "Média" or dif == "Díficil":
            missoes.append([ nome, dif, "pendente"])
        else:
            print("Dificuldade inválida")
            
    elif op == "2":
        nome = input ("Nome: ")
        for m in missoes:
            if m [0] == nome:
                missoes.remove(m)
                
    elif op == "3":
        nome = input ("Nome: ")        
        for m in missoes:
            if m [0] == nome:
                m[2] = "Concluída"
                
    elif op == "4":
        for m in missoes:
            print (m)
            
    elif op == "5":
        dif = input("Dificuldade: ")
        for m in missoes:
            if m[1] == dif:
                print(m)
                
    elif op == "6":
        break