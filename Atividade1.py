idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Entrada permitida no evento.")

elif idade >= 16:
    aut = (input("Você possui a autorização dos responsáveis?"))

    if aut == "sim":
        print("Entrada permitida apenas com a autorização dos responsáveis.")

    else:
        print("Entrada não permitida no evento.")

elif idade < 16:
    print("Entrada não permitida no evento.")