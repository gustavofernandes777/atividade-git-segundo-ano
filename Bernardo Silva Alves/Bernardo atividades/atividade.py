alunos = int(input("Digite o numero de alunos: "))
notas = int(input("Digite a quantidade de notas: "))


for aluno in range(alunos):
    soma = 0
    nome = input("Digite o nome do aluno: ")


    for i in range(notas):
        nota = float(input("Digite a nota: "))
        soma += nota


    media = soma / notas


    print(f"Nome: {nome}               Média: {media}")


    if media >= 6:
        print("Aprovado")
    elif media < 4:
        print("Reprovado")
    else:
        print("Recuperação")