idade = int(input("Digite sua idade: "))
auto = input("Possui autorização dos responsáveis? (sim/nao): ").lower()

if idade >= 18:
    print("Entrada permitida no evento.")

elif idade >= 16 and auto == "sim":
    print("Entrada permitida no evento.")

elif idade < 16 and auto == "sim":
    print("Entrada permitida apenas com responsável.")

else:
    print("Entrada não permitida no evento.")