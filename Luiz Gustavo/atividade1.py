alunos = int(input("Insira a quantidade de alunos: "))
notas = int(input("Insira a quantidade de notas: "))

for i in range(alunos):
    soma = 0
    
    nome = input("Digite o nome do aluno: ")

    for j in range(notas):

        while True:
            nota = float(input("Insira a nota do aluno: "))

            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida! Digite novamente.")

        soma += nota

    media = soma / notas

    print(f"Média de {nome}: {media:.2f}")

    if media >= 6:
        print("Aluno aprovado.")
    elif media >= 4:
        print("Recuperação.")
    else:
        print("Reprovado.")