lista = []

while True:

    print('=================')
    print('   INVENTÁRIO   ')
    print('=================')

    print()

    print("1 - Adcionar item")
    print("2 - Remover item")
    print("3 - Mostrar iventário")
    print("4 - Alterar a quantidade de itens")
    print("5 - Sair")

    print()

    numero=(int(input("Olá querido jogador, Insira um número de 1 a 4: "))) 
    print()

    if numero == 5:   
        break

    elif numero == 1:
        nome=(input("Adcione o nome do item que desejas: "))
        quantidade=(int(input("Adcione a quantidade do item que desejas: ")))

        item = (nome, quantidade)
        lista.append(item)
        print()
        print(f"{nome} adcionado!")
        print(f"{quantidade} adcionado!")

        print()

    elif numero == 2:
        nome_remove =(input("Remova o nome do item que desejas: "))

        for item_remove in lista:
            if item_remove [0] == nome_remove:
                lista.remove(item_remove)
                print(f"{nome_remove} removido!")
            else:
                print("Inválido")

    elif numero == 3:
        
        print(lista)
    
    elif numero == 4:
         nova_quan =(input("Insira o nome do item que desejas alterar a quantidade: "))
         
         for quan_remove in lista:
             if quan_remove [0] == nova_quan:
                 alterar_quan =int(input("Altere a quantidade de itens que desejas: "))
                 lista.remove(quan_remove)
                 lista.append((nova_quan, alterar_quan))
                 print(f"{alterar_quan} alterado!")
             else:
                print("Não encontrado, buscando o próximo.")

    else:
        print("FIM DA JOGADA!")
   


       


    

