alunos = int(input("Quantos alunos serão cadastrados: "))
notas = int(input("Quantas notas serão cadastradas: "))

for i in range(alunos):
    nome = input(f"\NNome do aluno {i+1}: ")
    notas = [float(input(f"Nota{j+1}: ")) for range(notas)]
    if media >= 6: sit = "Aprovado"
    elif media < 4: sit = "Reprovado"
    else: sit = "Recuperação"