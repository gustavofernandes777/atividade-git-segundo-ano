alunos = int(input("Insira a quantidade de alunos: "))
notas = int(input("Insira a quantidade de notas: "))

for i in range(alunos):
    soma = 0
    nome = input("\nDigite o nome do aluno: ")

    for j in range(notas):
        nota = -1 
        for tentativa in range(100):
            nota = float(input(f"Insira a nota {j+1} do aluno {nome}: "))
            if 0 <= nota <= 10:
                break
            elif nota < 0 or nota > 10:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        soma += nota

    media = soma / notas
    print(f"Média do aluno {nome}: {media:.2f}")

    if media >= 6:
        print("Aluno aprovado.\n")
    elif media >= 4:
        print("Recuperação.\n")
    elif media < 4:
        print("Reprovado.\n")