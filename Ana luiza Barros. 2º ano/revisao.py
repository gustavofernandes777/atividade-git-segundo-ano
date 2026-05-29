inventario = []

while True:

    print('========================')
    print('   SUPERMERCADO FELIZ   ')
    print('=========================')

    print()

    print("1 - Cadastrar produto")
    print("2 - Situação do estoque")
    print("3 - Exibir relatório")
    print("4 - Sair")

    print()

    numero=(int(input("Olá, insira número de 1 a 4:  ")))
    print()

    match numero:
        case 1:
    
            nome=input("Insira nome do produto: ")
            preco = float(input("Insira o preço do produto: "))
            quantidade=int(input("Insira a quantidade do produto: "))


            produto=[nome, preco, quantidade]
            inventario.append(produto)

            print(f"{produto} adcionado!")

        case 2: 
                 
             nome=(input("Insira o nome do produto que desejas verificar: "))

             for produto in inventario:

                if produto[0] == nome:

                     if produto[2] > 50:
                      print("Estoque alto")

                     elif produto[2] >=20 and produto[2] <=50:
                      print("Estoque médio")

                     elif produto[2] <20:
                      print("Estoque baixo")

        case 3:
            for produto in inventario:
                print(produto)
        
        case 4:
          break
   


