alunos = int(input("Quantos alunos: ")) 
qtd_notas = int(input("Quantas notas: "))  

for i in range(alunos):
    nome = input("\nnome do aluno")
    soma = 0

    for j in range(qtd_notas):
        soma += float(input(f"notas {j+1}:"))

    media = soma / qtd_notas  
   

    if media >= 6:         
        status = "Aprovado"     
    elif media < 4:         
        status = "Reprovado"  
    else:         
        status = "Recuperação"     
        
    print(f"Aluno: {nome}, Média: {media:.2f}, Status: {status}")