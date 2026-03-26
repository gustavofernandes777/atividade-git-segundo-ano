alunos = int(input("insira a quantidade de alunos: "))
notas = int(input("insira a quantidade de notas: "))

for i in range(alunos):
    soma = 0
    print("Digite o nome do aluno: ")
    nome = input()
    for nota in range(notas):
        print("insira a nota do aluno: ")
        nota = float(input())
        soma += nota
    media = soma/notas
    if media >= 6:
        print("aluno aprovado.")
    elif media < 6 and media >= 4:
        print("Recuperação.")
    elif media < 4:
        print ("Reprovado.")