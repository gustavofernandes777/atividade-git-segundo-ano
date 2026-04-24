alunos=int(input("Quantos alunos deseja cadastrar?:"))
notas=int(input("Quantas notas cada aluno terá?:"))

for i in range(alunos):
    print(f"\nAluno{i+1}")
    nome= input("Nome do aluno: ")

    soma=0
    for j in range(notas):
        nota=float(input(f"Digite a nota {j+1}: "))
        soma+=nota

    media=soma/notas
    print(f"Média de {nome}: {media:.2f}")

    if media >= 6:
        print("Aprovado")
    elif media < 4:
        print("Reprovado")
    else:
        print("Recuperação")