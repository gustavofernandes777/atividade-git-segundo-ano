missoes = []
opcoes = ["Fácil", "Média", "Difícil"]

while True:
    print("\n1.adicionar Missão 2.remover 3.Concluir 4.Listar 5.Mostrar missão por dificuldade 6.Sair")
    op = input("Opção: ")

    if op == '1':
        n, d = input("Nome: "), input("Dificuldade: ").capitalize()
        if d in opcoes: missoes.append({"nome": n, "dificuldade": d, "status": "Pendente"})
        else: print("Erro: Dificuldade inválida.")
    
    elif op == '2':
        n = input("Nome: ")
        antes = len(missoes)
        missoes = [m for m in missoes if m['nome'] != n]
        if len(missoes) == antes: print("Erro: Missão não encontrada.")
        
    elif op == '3':
        n = input("Nome: ")
        found = False
        for m in missoes:
            if m['nome'] == n: m['status'] = "Concluída"; found = True
        if not found: print("Erro: Missão não encontrada.")
            
    elif op == '4':
        for m in missoes: print(m)
        
    elif op == '5':
        d = input("Dificuldade: ").capitalize()
        for m in [m for m in missoes if m['dificuldade'] == d]: print(m)
        
    elif op == '6': break