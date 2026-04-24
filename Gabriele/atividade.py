idade = int(input("Digite sua idade: "))
autorização = input("Possui autorização dos pais (Sim/Não): ")

if idade >= 18:
    print("Entrada permitida no evento.")
elif idade == 16 and autorizacao == "não":
    print("Entrada não permitida no evento.")
elif idade == 16 and autorizacao == "sim":
    print("Entrada permitida apenas com responsável.")
else:("Entrada não permitida no evento.")
