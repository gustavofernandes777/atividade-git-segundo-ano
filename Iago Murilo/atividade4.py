escolha = 0

lista  = []

while escolha != 4:
   
    print("1 - Adicionar item\n"
          "2 - Remover item\n"
          "3 - Mostrar inventario\n"
          "4 - Sair")
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        print("Você escolheu adicionar item")
        additem = str(input("Insira o item: "))
        quant = int(input("Insira quantidade de item: "))
        tuplaitem = (additem, quant)
        lista.append(tuplaitem)

    if escolha == 2:
        print("Você escolheu remover item")
        removitem = str(input("Insira o item para remover: "))
        for item in lista:
            if item[0] == removitem:
                lista.remove(item)

    if escolha == 3:
        print("Você escolheu mostrar inventario")
        print(lista)
    
