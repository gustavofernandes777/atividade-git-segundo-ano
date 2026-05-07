quant_alunos = int(input("Quantos alunos deseja cadastrar? "))
quant_notas = int(input("Quantas notas cada aluno terá? "))

for i in range (quant_alunos):
    print(f"Aluno {i+1}")

    nome = input("Digite o nome do aluno: ")
    quant_alunos = int(input("Quantas notas esse aluno possui?"))

    soma = 0
    for i in range (quant_notas):
      nota = float(input(f"Digite a nota {i+1}:"))
      soma += nota

      media = soma / quant_notas

    if media >= 6:
        print("Aprovado!")
    elif media < 4:
        print("Reprovado!")
    else:
        print("Recuperação.")

