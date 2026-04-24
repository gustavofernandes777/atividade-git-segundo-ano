alunos = int(input("Digite a Quantidade de Alunos: "))
notas = int(input("Digite a Quantidade de Notas: "))

for aluno in range(alunos):
    soma = 0
    nome = input("Digite o Nome do Aluno: ")

    for nota in range(notas):
        nota = float(input("Digite as Notas do Aluno: "))
        soma = soma + nota
    

    med = soma / notas

    print("Media:", med)

    if med < 4:
        print("Reprovado")
    elif med >= 6:
        print("Aprovado")
    else:
        print("Recuperacao")
