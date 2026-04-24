print("---------- BEM VIMDO AO JOGO TEINEKES ----------\n")

nome = input("Digite seu nome: ")

print("Olá,", nome)
fila = []

while True:
    print("\n1 - Adicionar paciente")
    print("2 - Mostrar fila")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        fila.append(nome)

    elif op == "2":
        print("Fila:", fila)

    elif op == "0":
        break