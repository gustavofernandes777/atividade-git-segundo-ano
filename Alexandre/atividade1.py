idade = int(input("qual sua idade: "))
autorizacao = input("tem autorização? sim ou não: ")
permissao = "NAO"

if idade >= 16:
    permissao = "SIM"
elif autorizacao == "sim":
    permissao = "SIM"

if permissao == "SIM":
    if idade < 16:
        print("Entrada permitida na festa, com autorização")
    else:
        print("Entrada permitida na festa.")
else:
    print("Entrada negada!")