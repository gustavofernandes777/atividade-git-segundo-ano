def sistema_notas():
    try:
        qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))
        qtd_notas = int(input("Quantas notas cada aluno terá? "))

        if qtd_alunos <= 0 or qtd_notas <= 0:
            print("Quantidade de alunos e notas deve ser maior que zero.")
            return

        alunos = []

        for i in range(qtd_alunos):
            nome = input(f"\nDigite o nome do aluno {i+1}: ").strip()
            notas = []

            for j in range(qtd_notas):
                while True:
                    try:
                        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("A nota deve estar entre 0 e 10.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")

            media = sum(notas) / qtd_notas
            situacao = "Aprovado" if media >= 6 else "Reprovado"

            alunos.append({
                "nome": nome,
                "notas": notas,
                "media": media,
                "situacao": situacao
            })

        print("\n--- RELATÓRIO FINAL ---")
        for aluno in alunos:
            print(f"{aluno['nome']}: Notas {aluno['notas']} | Média {aluno['media']:.2f} | {aluno['situacao']}")

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros para quantidades.")

sistema_notas()