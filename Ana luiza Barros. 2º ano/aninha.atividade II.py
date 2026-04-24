aluno = int(input("Quantos alunos desejas insirir? "))
print(aluno)
print()

notas = int(input("Quantas notas desejas insirir para cada aluno? "))
print(notas)
print()

for nome in range(aluno):
    soma = 0
    nome = (input("Insira o nome do aluno: "))
    print(nome)

    for nota in range(notas):
        nota = int(input("Insira nota: "))
        soma += nota
        print(soma)

    media = soma/notas

    if media >= 6:
        print("Parabéns meu querido aluno, estás aprovado!")
    else:
        print("Sinto muito, reprovastes. Irás melhor da próxima!")