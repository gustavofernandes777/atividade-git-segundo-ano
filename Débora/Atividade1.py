alunos = int(input("digite um numero de alunos: "))
notas = int(input("digite um numero de notas: "))

for i in range(alunos):
    nome = input("nome do aluno: ")
    soma = 0
    for i in range (notas):
        nota = float(input("digite a nota:"))
        soma += nota
        media = soma/notas
        if media >= 10:
            print("aprovado")
        elif media < 6:
            print("reprovado")
        else:
            print("recuperação")