matriz = []
res = 0

while res != 4:
    print("O que você quer realizar:")
    print("1- Cadastrar produto")
    print("2- Relatório")
    print("3- Relatório do produto específico")
    print("4- Sair")

    res = int(input())

    if res == 1:

        nome = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade desse produto: "))
        preco = float(input("Digite o valor (R$) do produto: "))

        if qtd > 50:
            status = "Estoque Alto"
        elif qtd >= 20 and qtd <= 50:
            status = "Estoque Médio"
        else:
            status = "Estoque Baixo"
        produto = [nome, qtd, preco, status]
        matriz.append(produto)

    elif res == 2:

        total = 0
        valor = 0

        print("\nRELATÓRIO GERAL\n")

        for i in matriz:
            total += i[1]
            valor += i[1] * i[2]

        print("Quantidade total de itens:", total)
        print("Valor total do estoque: R$", valor)

    elif res == 3:

        r = input("Qual item em específico você quer verificar? ")

        for i in matriz:

            if r == i[0]:

                print("\nProduto encontrado:\n")
                print("Nome:", i[0])
                print("Quantidade:", i[1])
                print("Preço:", i[2])
                print("Situação:", i[3])