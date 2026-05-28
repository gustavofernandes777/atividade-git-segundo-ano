idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Entrada permitida no evento.")

else:
    autorizacao = input("Possui autorização dos responsáveis? (sim/nao): ")

    if idade >= 16 and autorizacao == "sim":
        print("Entrada permitida no evento.")

    elif idade < 16 and autorizacao == "sim":
        print("Entrada permitida apenas com responsável.")

    else:
        print("Entrada não permitida no evento.")
