notas = 0

qtd = int(input("Deseja cadastrar quantas notas:"))

div = qtd

for nota in range (qtd):
    nota = int(input("Insira nota:"))

    while qtd > 0:

        if nota > 10 or nota < 0:
            notaa = int(input("Nota inválida digite novamente:"))

            notas += notaa

        else:

            notas += nota
            qtd = qtd - 1

        break

media = nota / div

if media >= 7:
    print("Aprovado")

elif media >= 5 and media <= 6.9:
    
    print("Recuperação")

else:

    print("Reprovado")

print(media)