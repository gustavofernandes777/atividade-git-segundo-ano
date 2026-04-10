idade = int(input("Insira sua idade: "))
autorizacao = input("Possui autorização dos responsáveis? (sim/não): ")

entrada_permitida = False

if idade >= 18:
    entrada_permitida = True
elif idade >= 16:
    entrada_permitida = True
elif autorizacao == "sim":
    entrada_permitida = True

if entrada_permitida:
    if idade < 16:
        print("Entrada permitida no evento com a autorização do responsável")
    else:
        print("Entrada permitida no evento")
else:
    print("Entrada negada!")