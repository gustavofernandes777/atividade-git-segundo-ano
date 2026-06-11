alunos = int(input("Quantos alunos deseja cadastrar? "))
notas = int(input("Quantas notas deseja cadastrar para cada aluno? "))

for i in range(alunos):

    soma = 0

    nome = input("\nDigite o nome do aluno: ")

    for j in range(notas):
        nota = float(input(f"Digite a {j+1}ª nota: "))
        soma += nota

    media = soma / notas

    print(f"\nAluno: {nome}")
    print(f"Média = {media:.1f}")

    if media >= 6:
        print("Aluno aprovado!")

    elif media < 4:
        print("Aluno reprovado!")

    else:
        print("Aluno em recuperação!")
