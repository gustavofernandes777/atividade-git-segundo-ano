lista = []
matriz = [lista]
res = 0

while res != 4:
    print("O que você quer realizar: ")
    print("1- Cadastrar produto")
    print("2- Relatório")
    res = int(input())

    if res == 1:
        nome = input("Digite o nome do produto: ")
        qtd = int(input("Digite a quantidade desse produto: "))
        preco = float(input("Digite o valor (R$) do produto: "))
        lista.append(nome)
        lista.append(qtd)
        lista.append(preco)
        if qtd > 50:
            status = "Estoque Alto"
            lista.append(status)
        elif qtd >= 20 and qtd <= 50:
            status = "Estoque Médio"
            lista.append(status)
        elif qtd < 20:
            status = "Estoque Baixo"
            lista.append(status)
        for i in lista:
            print(i)
    if res == 2:
        print("Relatório total")
        print()