num_alunos = int(input("Quantos alunos serão registrados? "))
num_notas = int(input("Quantas notas por aluno? "))

for i in range(num_alunos):
    print(f"\n--- Registro do Aluno {i + 1} ---")
    nome = input("Nome do aluno: ")
    soma_notas = 0
    
    for j in range(num_notas):
        nota = float(input(f"Digite a {j + 1}ª nota de {nome}: "))
        soma_notas += nota
    
    media = soma_notas / num_notas
    
    if media >= 6:
        status = "Aprovado"
    elif media < 4:
        status = "Reprovado"
    else:
        status = "Recuperação"
    
    print(f"Resultado: O aluno {nome} ficou com média {media:.2f} e está: {status}")