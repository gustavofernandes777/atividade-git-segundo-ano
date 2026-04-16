print("---Menu de jogo---")
lista =[]
a = 0

while a != 6:
    print()
    print("1- Adicionar missão")
    print("2- Remover missão")
    print("3- Concluir missão")
    print("4- Listar missões")
    print("5- Mostrar missões por dificuldade")
    print("6- Sair")
    a = int(input())

    if(a>6) or (a<1):
        print("Número invalido! Tente novamente!")
 
    elif (a == 1):
        nome =(input("Digite o nome da missão:"))

        c = 1
        while (c == 1):
            print("Escolha a dificuldade da missão:")
            print()
            print("1- Fácil")
            print("2- Média")
            print("3- Difícil")
            b = int(input())

            if(b<1) or (b>3):
                print("Dificuldade não encontrada. Tente novamente.")
                c = 1
            elif(b == 1):
                    c = 0
                    dificuld = "Fácil"
            elif(b == 2):
                c = 0
                dificuld = "Média"
            elif(b == 3):
                c = 0
                dificuld = "Difícil"
            
        status = "Pendente"
        missao = (nome, dificuld, status)
        lista.append (missao)

    elif(a == 2):
        delete = (input("Digite a missão que queira remover: "))
        encontrado = False
        for i in lista:
            if i[0] == delete:
                lista.remove (i)
                encontrado = True
                break
        if not encontrado:
            print("Item não encontrado!")

    elif(a == 3):
        concluida = (input("Digite a missão que você queira concluir: "))
        encontrado = False
        for i in lista:
            if i[0] == concluida:
                novadificuld = i[1]
                lista.remove(i) 
                novostatus = "Concluida"
                novamissao = (concluida, novadificuld, novostatus)   
                encontrado = True
                lista.append(novamissao)
                break
        if not encontrado:
            print("Missão não encontrado!")
    elif(a == 4):
        print("---Lista de missões---")
        for i in lista:
            print("Missão:", i[0], "-", i[1], ":", i[2])

    elif (a == 5):
         c = 1
         while (c == 1):
            print("Escolha a dificuldade que deseja visualizar:")
            print()
            print("1- Fácil")
            print("2- Média")
            print("3- Difícil")
            b = int(input())

            if(b<1) or (b>3):
                print("Dificuldade não encontrada. Tente novamente.")
                c = 1
            elif(b == 1):
                    c = 0
                    for i in lista:
                        if i[1] == "Fácil":
                            print("Missão:", i[0], "-", i[1], ":", i[2])
            elif(b == 2):
                c = 0
                for i in lista:
                    if i[1] == "Média":
                        print("Missão:", i[0], "-", i[1], ":", i[2])
            elif(b == 3):
                c = 0
                for i in lista:
                    if i[1] == "Difícil":
                        print("Missão:", i[0], "-", i[1], ":", i[2])