idade = int(input("Informe a sua Idade: "))

if idade >= 18:
    print("Autorizado para entrar no evento!")
else:
    auto = input("Você possui autorização dos pais? (sim/não)")

    if idade >= 16 and auto == "sim":
        print("Entrada permitida no evento!")
    elif idade < 16 and auto == "sim":
        print("Entrada permitida!")
    else:
        print("Entrada negada no evento")