quantidadedenotas = int(input ("Quantas notas você quer cadastrar?"))
quantidadealunos = int(input("Quantos alunos você quer cadastrar?"))

for y in range(quantidadealunos):
    nome = input("Digite o nome do aluno:")
    soma = 0

    for i in range(quantidadedenotas):
        nota = float(input(f"Digite a nota {i+1}: "))
        soma += nota
    media = soma / quantidadedenotas
    if media >= 6:
        print("Aprovado!")
        print(f"A média do aluno é: {media}") 
    elif media <= 4:
        print("Reprovado!")
        print(f"A média do aluno é: {media}") 
    else:
        print("Recuperação!")
        print(f"A média do aluno é: {media}") 