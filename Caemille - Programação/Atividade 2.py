idade = int(input("Digite sua idade:"))
aut = (input("Você possui a autorização dos responsáveis?(sim/não)"))

if idade >= 18:
    print("Entrada permitida no evento.")

elif idade >= 16 and aut == 'sim':
     print("Entrada permitida apenas com a autorização dos responsáveis.")

else:
    print("Entrada não permitida no evento.")