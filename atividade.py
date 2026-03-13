idade = int(input("Digite sua idade:"))
per = input("Possui autorização dos responsáveis? (sim/nao):")

if idade < 16 and per == "sim":
    print("Entrada permitida apenas com responsável.")    

elif idade >= 16 and idade < 18 and per == "sim":
    print("Entrada permitida no evento.")

elif idade >= 18:
    print("Entrada permitida no evento.")

else:
    print("Entrada não permitida no evento.")