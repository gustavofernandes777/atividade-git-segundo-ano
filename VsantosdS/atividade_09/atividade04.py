inventario = []

while True:
    print("\nMenu:")
    print("1 - adicionar item")
    print("2 - Remover item")
    print("3 - mostrar inventário")
    print("4 - sair")

    digitado = int(input("escolha uma opção: "))
    
    if digitado == 1:
        nome = input("digite o nome do item: ")
        quantidade = int(input("digite a quantidade de intens: "))
        inventario.append((nome, quantidade))
    
    elif digitado == 2:
        nome = input("digite o nome do item que deseja remover: ")
        for item in inventario:
            if item[0] == nome:
                inventario.remove(item)
                print(f"{nome} removido do inventário.")
                break
        else:
            print(f"{nome} não encontrado no inventário.")
    
    elif digitado == 3:
        print("\nInventário:")
        for item in inventario:
            print(f"Item: {item[0]}, Quantidade: {item[1]}")
    
    elif digitado == 4:
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")