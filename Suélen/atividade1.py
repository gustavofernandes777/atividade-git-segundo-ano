idade = int (input("Digite sua idade: "))
autorizacao = input ("Tem autorização dos responsáveis? (sim/não): ")
if idade >=16:
    print("Entrada permitida no evento")
elif autorizacao == "sim":
    print("Entrada permitida apenas com responsável")
else:
    print("Entada não permitida no evento")




