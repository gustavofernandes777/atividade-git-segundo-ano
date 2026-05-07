
estoque = []

quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_produtos):
    print(f"\nCadastro do produto {i+1}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    if quantidade > 50:
        situacao = "Estoque Alto"
    elif 20 <= quantidade <= 50:
        situacao = "Estoque Médio"
    else:
        situacao = "Estoque Baixo"

    # Lista com os dados do produto
    produto = [nome, preco, quantidade, situacao]

    # Adicionando produto na matriz
    estoque.append(produto)

# Relatório Final
print("\n===== RELATÓRIO FINAL =====")

for produto in estoque:
    print(f"""
Nome do produto: {produto[0]}
Preço: R$ {produto[1]:.2f}
Quantidade: {produto[2]}
Situação: {produto[3]}
""")