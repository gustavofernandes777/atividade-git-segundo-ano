qntnotas= int(input("Quantidade de notas: "))
alunos= int (input("Quantidade de alunos cadastrado: "))
for item in range (alunos):
    nome= input("Insira nome do aluno: ")
    soma=0
    for item in range (qntnotas):
     notas = float(input("Insira nota: "))
     soma+=notas
media= soma/qntnotas
if media>=6:
    print ("aprovado")
    print("a média do aluno é: ", media)
elif media <=4:
    print ("reprovado")
    print ("a media do aluno é: ", media)
else:
    print ("recuperação")
    print (" a media do aluno é: ", media)
