num_alunos = int(input("quantos alunos serão registrados"))
notas = int(input("quantas notas por alunos"))
for i in range  (num_alunos):
    nome = input("nome do aluno ")
    soma = 0 
    for j in range (notas):
        nota = float (input("digite a nota"))
        soma += nota
    media = soma/notas 
    if media >= 7: 
        print(f"O aluno {nome} foi aprovado com média {media:.2f}")
    elif media < 5:
        print(f"O aluno {nome} foi reprovado com média {media:.2f}")
    else:
        print (f"O aluno {nome} está em recuperação com média {media:.2f}")