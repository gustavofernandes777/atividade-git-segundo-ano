print("---Evento escolar---")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print(f"Entrada permitida! Aproveite o evento {nome}!")
elif idade >= 16:
    a = 1
    while (a == 1):
        opcao = input("Você possui autorização de seus pais? (s/n)")
        if opcao == 's' or opcao == 'S':
            print(f"Entrada permitida! Aproveite o evento {nome}!")
            a = 2
        elif opcao == 'n' or opcao == 'N':
            print("Entrada negada! Com a sua idade, você precisa de autorização dos seus pais para entrar no evento!")
            a = 2
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não!")
            a = 1
elif idade > 0 and idade < 16:
    b = 1
    while (b == 1):
        escolha = input("Você está acompanhado com um responsável? (s/n)")
        if escolha == 's' or escolha == 'S':
            print(f"Entrada permitida! Aproveite o evento {nome}!")
            b = 2
        elif escolha == 'n' or escolha == 'N':
            print("Entrada negada! Com a sua idade, você precisa estar acompanhado com um responsável para entrar no evento!")
            b = 2
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não!")
            b = 1
