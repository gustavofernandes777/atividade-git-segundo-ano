num_alunos = int(input("Digite o número de alunos: "))
num_notas = int(input("Digite o número de notas por aluno: "))

for i in range(num_alunos):
    nome_aluno = input(f"Digite o nome do aluno {i+1}: ")
    
    soma_notas = 0.0
    
    for j in range(num_notas):
        nota = float(input(f"Digite a nota {j+1} para {nome_aluno}: "))
        soma_notas += nota
    
    media = soma_notas / num_notas
    
    if media >= 6:
        status = "Aprovado"
    elif media < 4:
        status = "Reprovado"
    else:
        status = "Recuperação"
        
    print(f"Aluno: {nome_aluno}, Média: {media:.2f}, Status: {status}")