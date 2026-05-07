qntnotas = int(input("quantidade de notas: "))
alunos = int (input("quantidade de alunos: "))
for item in range (alunos):
    nome =  input("insira nome do aluno: ")
    soma = 0
for item in range (qntnotas):
     notas = float(input("insira nota: "))
     soma += notas 
media = soma / qntnotas 
if media >= 6:
     print("Aprovado")
     print("A media do aluno é: ", media)
elif media <= 4:
     print("reprovado")
     print("A mdeia do aluno é: ", media)
else:
     print("recuperação")
     print("A media do aluno é: ", media)
     