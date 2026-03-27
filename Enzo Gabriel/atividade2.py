idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pergunta de Seguranca")
    num = int(input("Quanto e 8 + 6? "))
    
    if num == 14:
        print("Correto!")
        print("Permissao Concedida")
    else:
        print("Permissao Recusada! Volte com seus pais.")

else:
    aut = input("Voce possui permissao de seu responsavel? (sim ou nao) ").strip().lower()

    if 16 <= idade <= 17 and aut == "sim":
        print("Entrada permitida no evento.")

    elif 16 <= idade <= 17 and aut == "nao":
        print("Entrada nao permitida no evento.")

    elif idade < 16 and aut == "sim":
        print("Entrada permitida apenas com responsavel.")
    
    elif idade < 16 and aut == "nao":
        print("Entrada nao permitida no evento.")
    
    else:
        print("Tente novamente!")