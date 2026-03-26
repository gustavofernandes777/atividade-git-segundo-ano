qnotas = int(input("digite a quantidade de alunos que serão cadastrados"))
alunos = int(input("digite a quantidade de notas"))
for aluno in range(alunos):
    soma=0.0
    nome = [ str(input("digite o nome do aluno(a)"))]
    print(nome)

    for nota in range(qnotas):
        nota= float(input("insira a nota do aluno"))
        if nota >10:
            break
        print(nota)
        soma = soma + nota
    media = soma/qnotas
    if media > 10:
        break
    print(f"o aluno(a) {nome}, tem como média {media}")

    if nota >=6:
        print("aprovado(a)!!")
    else:
        print("reprovado(a)...")