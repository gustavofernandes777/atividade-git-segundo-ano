print("---Menu de jogo---")
invent=[]
a = 0

while a != 5:
    print()
    print("1- Adicionar item")
    print("2- Remover item")
    print("3- Mostrar inventário")
    print("4- Alterar quantidade de item")
    print("5- Sair")
    a = int(input())

    if(a>5) or (a<1):
        print("Número invalido! Tente novamente!")

    elif (a == 1):
        nome =(input("Digite o nome do item:"))
        quant = int(input("Digite a quantidade do item: "))
        item = (nome, quant)
        invent.append (item)

    elif(a == 2):
        delete = (input("Digite o item que queira remover: "))
        encontrado = False
        for i in invent:
            if i[0] == delete:
                invent.remove (i)
                encontrado = True
                break
        if not encontrado:
            print("Item não encontrado!")

    elif(a == 3):
        print("---Inventário---")
        for i in invent:
            print("Item:", i[0], "-", i[1])

    elif (a == 4):
        alter = (input("Digite o item que queira substituir a quantidade: "))
        localizado = False
        for i in invent:
            if i[0] == alter:
                novaquant = int(input("Digite a nova quantidade: ")) 
                invent.remove (i)
                novoitem = (alter, novaquant)
                invent.append (novoitem)
                localizado = True
                break
        if not localizado:
            print("Item não encontrado!")