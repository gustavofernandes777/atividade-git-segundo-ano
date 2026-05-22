qdtnotas = int(input ("Quantas notas você quer cadastrar?"))
alunos = int(input("Quantos alunos você quer cadastrar?"))
for item in range(alunos):
    nome_aluno = input("Digite o nome do aluno:")
    soma=0
    for i in range(qdtnotas):
        nota = float(input("Digite a nota:"))
        soma += nota
    media = soma / qdtnotas
    if media >= 6:
        print("Aprovado")
        print("A média do aluno é: ", media) 

    elif media <= 4:
        print("Reprovado")
        print("A média do aluno é: ", media) 

    else:
        print("Recuperação")
        print("A média do aluno é: ", media) 