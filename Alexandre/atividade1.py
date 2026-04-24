qt_alunos = int(input("digite a quantidade de alunos: "))
qt_nota = int (input("digite a qauntidade de notas: "))
for i in range(qt_alunos):
    print(f"Aluno {i+1}: ")
soma = 0
for j in range(qt_nota):
    nota = float(input(f"Digite a nota {j+1}: "))
    soma += nota
media = soma / qt_nota
print(f"A média do aluno {i+1} é: {media:.2f}")
if media >= 7:
    print("Aprovado")
else:
    if media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

