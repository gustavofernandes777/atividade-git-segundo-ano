print("---Menu de jogo---")
invent=[]
a = 0
while a != 4:
    print("1- Adicionar item")
    print("2- Remover item")
    print("3- Mostrar item")
    print("4- Sair")
    a = int(input())
    if(a>4) or (a<1):
        print("Número invalido! Tente novamente!")
    elif (a == 1):
        nome =(input("Digite o nome do item:"))
        quant = int(input("Digite a quantidade do item:"))
        item = (nome, quant)
        invent.append (item)
    elif(a == 2):
        delete = (input("Digite o item que queira remover:"))
        for i in invent:
            if i[0] == delete:
                invent.remove (i)
    elif(a == 3):
        print(invent)
        