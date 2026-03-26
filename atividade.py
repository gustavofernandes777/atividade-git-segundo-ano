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