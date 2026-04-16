
idade = int(input("Digite sua idade: "))
autorizacao = input("Possui autorização dos responsáveis? (sim/nao): ").strip().lower()

if idade >= 18:
    print("Entrada permitida no evento.")
    
elif idade >= 16:
    if autorizacao == "sim":
        print("Entrada permitida no evento.")
    else:
        print("Entrada não permitida no evento.")
        
else:
    if autorizacao == "sim":
        print("Entrada permitida apenas com responsável.")
    else:
        print("Entrada não permitida no evento.")