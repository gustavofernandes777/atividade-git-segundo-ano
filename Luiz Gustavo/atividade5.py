lista = []
a = 0
while a != 5:
    print("1 - Adicionar missão")
    print("2- Remover missão")
    print("3- Concluir missão")
    print("4- Listar missão")
    print("5- Mostrar missão por dificuldade")
    print("6- Sair")
    a = int(input())
    match a:

        case 1: 
            print("Adicione o nome da missão: ")
            name = input()
            print("Qual a dificuldade? ")
            dfc = int(input())
            if dfc != ("fácil") and ("médio") and ("díficl"):
                print("Erro, tente novamente.")
            else:
                status = "Em andamento"
                carac = [name, dfc, status]
                lista.append(carac)
        case 2:
            remove = input("Missão você quer remover? ")
            for i in carac:
                if i[0] == remove:
                    lista.remove(i)
                elif i[0] != remove:
                  print("Erro, tente novamente.")
        case 3:
            
                
        case 4:
            print(lista)
        case:
            mod = input("Qual item você quer modificar? ")
            qtd2 = int(input("Igite a nova quantidade desse item: "))

            for i in lista:
                if i[0] == mod:
                    lista.remove(i)
                    lista.append((mod, qtd2))
        case 6:
            print("Programa finalizado...")
            break