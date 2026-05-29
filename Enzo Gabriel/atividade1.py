alunos = int(input("Digite a Quantidade de Alunos: "))
notas = int(input("Digite a Quantidade de Notas: "))

for aluno in range(alunos):
    soma = 0
    nome = input("Digite o Nome do Aluno: ")

    for nota in range(notas):

        nota = float(input("Digite as Notas do Aluno: "))

        while nota < 0 or nota > 10:
            print("Nota inválida! Digite uma nota entre 0 e 10.")
            nota = float(input("Digite a Nota Novamente: "))

        soma = soma + nota

    med = soma / notas

    print("Media:", med)

    if med < 4:
        print("Reprovado")
    elif med >= 6:
        print("Aprovado")
    else:
        print("Recuperacao")