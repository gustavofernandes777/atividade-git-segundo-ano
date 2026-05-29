lunos = int (input("quantos alunos desejam cadastrar"))
notas = int(input("quantas notas cada aluno terá"))
for i in range(alunos):
     nome = input("nome do aluno: ")
     soma = 0
     for j in range (notas):
          nota = float(input("digite a nota:"))
          soma += nota
          media = soma/notas
     if media >= 6:
          print("aprovado")
     elif media < 4:
          print("reprovado")
     else:
          print("recuperacao")
     