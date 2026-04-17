item = ("arco", 2)
lista = []
lista.append(item)
a = 0

while a != 5:
    print("1 - Adicionar item")
    print("2- Remover item")
    print("3- Mostrar inventário")
    print("4- Modificar item")
    print("5- Sair")
    a = int(input())

    if a == 1:
        print("Adicione o nome do item: ")
        name = input()
        print("Quantas unidades desse item? ")
        qtd = int(input())
        tupla1 = (name, qtd)
        lista.append(tupla1)

    elif a == 2:
        remove = input("Qual item você quer remover? ")
        for i in lista:
            if i[0] == remove:
                lista.remove(i)
                print(f"O item {remove} foi removido.")
                break  
    elif a == 3:
        print("Inventário atual:")
        print(lista)

    elif a == 4:
        mod = input("Qual item você quer modificar? ")
        qtd2 = int(input("Digite a nova quantidade desse item: "))

        for i in lista:
            if i[0] == mod:
                lista.remove(i)
                lista.append((mod, qtd2))
                print(f"O item {mod} foi modificado para a quantidade {qtd2}.")
                break  
    elif a == 5:
        print("Programa finalizado...")
        break 