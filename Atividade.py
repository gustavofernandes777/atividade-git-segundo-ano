<<<<<<< HEAD
idade=int(input("Digite idade do aluno: "))
autorizacao= input("Possui autorização dos responsáveis? (sim ou não): ")
if idade>=18:
    print("Entrada autorizada")
elif idade>=16 and autorizacao== "sim":
    print("Entrada permitida")
elif idade < 16 and autorizacao=="sim":
    print("Entrada permitida apenas com responsável")
else:
    print("Entrada não permitida no evento")
=======
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
>>>>>>> 1516062ed64f9742f9009b4186a2d2575743cfd3
