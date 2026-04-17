inventario = []


while True:

        print("\nBem-vindo!")
        print("1 - adiciona item")
        print("2 - remover item")
        print("3 - mostrar inventario")
        print("4 - sair")

        digitado = input("escolha uma opcao:")
        
        if digitado == "1":
                nome = input("nome do item:")
                quantidade = int(input("quantidade:"))
                inventario.append([nome, quantidade])

        elif digitado == "2":
                nome = input("nome do item para remover: ")
                for item in inventario:
                        if item [0] == nome:
                                inventario.remove(item)
                                print("item removido!")
                                break
                        else:
                                print("item não encontrado!")

        elif digitado == "3":
                print("\ninventario:")
                for item in inventario:
                        print(f"{item[0]} - {item[1]}")

        elif digitado == "4":
                print("saindo...") 
                break      

        else:
                print("opção invalida!")     
                        
