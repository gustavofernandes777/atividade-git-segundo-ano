idade = int(input("Digite sua idade: "))
autorizacao = input("Possui autorização dos pais (sim/não): ")

if idade >= 18:
    print("Entrada permitida no evento.")
elif idade >= 16 and autorizacao == "sim":
    print("Entrada permitida no evento.")
elif idade < 16 and autorizacao == "sim":
    print("Entrada permitida apenas com responsável.")
else:
    print("Entrada não permitida no evento.")
