
n = int(input("Quantas notas deseja cadastrar? "))
notas = []

for i in range(n):
    nota = -1
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a {i+1}ª nota (0 a 10): "))
        if nota < 0 or nota > 10:
            print("Nota inválida! Tente novamente.")
    notas.append(nota) 

media = sum(notas) / n

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f} - Situação: {situacao}")