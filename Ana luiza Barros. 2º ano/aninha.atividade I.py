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
        nota = float(input("Insira nota: "))
        while nota < 0 or nota > 10:
            nota = float(input("Insira nota válida: "))
        soma += nota
        print(soma)

    media = soma/notas

    if media >= 7:
        print("Parabéns meu querido aluno, estás aprovado!")
    elif media >=5 and media <=6.9:
        print("Recuperação!")
    else:
        print("Sinto muito, reprovastes. Irás melhor da próxima!")
