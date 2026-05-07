idade = int(input("Digite sua idade: "))
autorizacao = input ("Tem autorização dos responsaveis?: (sim/não)")
if idade >= 16:
     print ("Entrada permitida no evento ")

if autorizacao == "sim":
     print("Entrada permitida apenas com responsavel")
else:
     print("Entrada não permitida no evento")