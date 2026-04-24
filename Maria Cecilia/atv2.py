print("---Sistema de Notas---")
alunos =int(input("Digite a quantidade de alunos: "))
notas =int(input("Digite a quantidade de notas para cada aluno: "))
for i in range(alunos):
        soma = 0
        nome = (input(f"Digite o nome do aluno {i+1}: "))
        for f in range(notas):
                note = float(input(f"Digite a nota {f+1}: "))
                soma = soma + note
        media = soma/notas
        print(f"A média do aluno {nome} é: {media:.2f}")
        if media >= 7:
                print("Aluno aprovado!")
        elif media >= 5 and media < 7:
                print("Aluno em recuperação!")
        else:
                print("Aluno reprovado!")
                
            
        
