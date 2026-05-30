alunos = int(input("Quantas alunos deseja cadastrar? "))
notas = int(input("Quantas notas para cada aluno deseja cadatrar? "))

for i in range(alunos):
    soma = 0
    nome = input("Insira o nome do aluno: ")
    for nota in range(notas):
        nota = float(input("Digite a nota: "))

        while nota < 0 or nota > 10:
             nota = float(input("Digite a nota: "))

        soma+=nota
    media = soma/notas


    if media>=6:
        print(f"Média = {media} Aluno aprovado!")
    elif media<4:
        print(f"Média = {media} Reprovado")
    else:
        print(f"Média = {media}Recuperação")
