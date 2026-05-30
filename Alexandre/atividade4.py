inventario = []

while True:
    print("1 - Adicionar Item\n2 - Remover Item\n3 - Mostrar Inventário\n4- Editar quantidade de Item\n5 - Sair")
    n = int(input("\nDigite o valor: "))
    if n == 5:
        print(f"\nVocê saiu do codigo.")
        break
    elif n == 1:
        nome = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade do item: "))
        inventario.append(nome)
        inventario.append(quantidade)
    elif n == 2:
        nome = input("Digite exatamente igualzinho o nome do produto que voce quer retirar: ")
        localizacao = inventario.index(nome)
        del inventario[localizacao]
        del inventario[localizacao]
    elif n == 3:
        print("\n", inventario)
        print("\n")
    elif n == 4:
        nome = input("Digite exatamente o mesmo nome do item que voce quer mudar a quantidade: ")
        localizacao = inventario.index(nome)
        inventario[localizacao+1] = int(input("Digite a quantidade nova: "))
    else:
        print("Numero invalido.")

