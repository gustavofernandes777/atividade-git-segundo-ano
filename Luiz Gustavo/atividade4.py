item = ("arco", 2)

lista = []
a = 0
while a != 4:
    print("1 - Adicionar item")
    print("2- Remover item")
    print("3- Mostrar inventário")
    print("4- Sair")
    a = int(input())

    if a == 1:
        print("Adicione o nome do item: ")
        name = input()
        print("Quantas unidades desse item? ")
        qtd = int(input())
        tupla1 = (name, qtd)

        lista.append(tupla1)
    elif a == 2:
        print("Qual item você quer remover? ")
        remove = input()
        for i in lista:
            if i[0] == remove:
                lista.remove(i)
    elif a == 3:
        print(lista)