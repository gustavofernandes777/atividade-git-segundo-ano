
estoque = []

quantidade_produtos = int(input("Quantos produtos deseja cadastrar? "))

for i in range(quantidade_produtos):
    print(f"\nCadastro do produto {i+1}")

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))

    if quantidade > 50:
        situacao = "Estoque Alto"
    elif 20 <= quantidade <= 50:
        situacao = "Estoque Médio"
    else:
        situacao = "Estoque Baixo"

    produto = [nome, preco, quantidade, situacao]
    
    estoque.append(produto)

print("\nRELATÓRIO")

for produto in estoque:
    print(f"\nProduto: {produto[0]}")
    print(f"Preço: R$ {produto[1]:.2f}")
    print(f"Quantidade: {produto[2]}")
    print(f"Situação: {produto[3]}")