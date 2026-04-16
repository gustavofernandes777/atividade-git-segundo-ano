inventario = [] 
while True: 
    print("\n1 - Adicionar | 2 - Remover | 3 - Mostrar | 4 - Alterar Quantidade | 5 - Sair") 
    opcao = input("Escolha: ") 
    
    if opcao == '1': 
        nome = input("Item: ") 
        qtd = input("Qtd: ") 
        inventario += [(nome, qtd)] 
        print("Adicionado!") 
        
    elif opcao == '2': 
        nome_rem = input("Nome para remover: ") 
        inventario = [item for item in inventario if item[0] != nome_rem] 
        print("Removido!") 
        
    elif opcao == '3': 
        print("\n--- Inventário ---") 
        for item in inventario: 
            print(f"Item: {item[0]} | Qtd: {item[1]}") 
        print("------------------") 
        
    elif opcao == '4': 
        nome_alt = input("Nome do item para alterar: ") 
        nova_qtd = input("Nova quantidade: ") 
        
        novo_inventario = [] 
        for item in inventario: 
            if item[0] == nome_alt: 
                novo_inventario += [(item[0], nova_qtd)] 
            else: 
                novo_inventario += [item] 
        inventario = novo_inventario 
        print("Quantidade alterada!") 
        
    elif opcao == '5': 
        print("Saindo...") 
        break 
        
    else: 
        print("Opção inválida, tente novamente.")