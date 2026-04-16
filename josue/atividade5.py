missoes = []

while True:
    op = input("1-add 2-rem 3-conc 4-list 5-filtrar 0-sair: ")

    if op == "1":
        n = input("Nome: ")
        d = input("Dif: ")
        if d in ["facil","Média","Difícil"]:
            missoes.append([n,d,"P"])
        else:
            print("Erro")

    elif op == "2":
        n = input("Nome: ")
        for m in missoes:
            if m[0] == n:
                missoes.remove(m)

    elif op == "3":
        n = input("Nome: ")
        for m in missoes:
            if m[0] == n:
                m[2] = "C"

    elif op == "4":
        print(missoes)

    elif op == "5":
        d = input("Dif: ")
        for m in missoes:
            if m[1] == d:
                print(m)

    elif op == "0":
        break