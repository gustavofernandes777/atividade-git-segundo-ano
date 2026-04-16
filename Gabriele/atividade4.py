inventario = []
digitado = 0
while digitado != 4 :
  
    print("\n1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar inventário")
    print("4- Sair")

    digitado = int(input("Escolha uma opção: "))

    if digitado == 1:
        nome = input("Nome do item: ")
        qtd = int(input("Quantidade: "))
        item = (nome,qtd)
        inventario.append(item)
        print("item adicionado!")

    elif digitado == 2:
        nome = input("Nome do item para remover: ")
        for i in inventario:
            if i[0] == nome:
               inventario.remove(i)
               print ("Item removido")
               break 
        
    elif digitado == 3: 
        print("\nInventário: ")
        for item in inventario:
            print(item[0], item[1])
                  
    elif digitado == 4:
        print("Saindo...")
        break
        
    else:
        print("Opção inválida")
        
