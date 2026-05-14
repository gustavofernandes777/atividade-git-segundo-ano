matriz_produtos = []

while True:
    nome = input("Digite o nome do produto (ou 'SAIR' para encerrar): ")
    if nome == "SAIR":
        break
    if nome == "sair":
        break
        
    preco = float(input("Digite o preço: R$ "))
    quantidade = int(input("Digite a quantidade: "))
    
    produto = [nome, preco, quantidade]
    matriz_produtos = matriz_produtos + [produto]

print("\nRELATÓRIO FINAL DO ESTOQUE")
print("Produto              | Preço      | Qtd        | Situação")
print("-" * 65)

for prod in matriz_produtos:
    nome_prod = prod[0]
    preco_prod = prod[1]
    qtd_prod = prod[2]
    
    if qtd_prod > 50:
        situacao = "Estoque Alto"
    elif qtd_prod >= 20:
        situacao = "Estoque Médio"
    else:
        situacao = "Estoque Baixo"
        
    print(f"{nome_prod:<20} | R$ {preco_prod:<8.2f} | {qtd_prod:<10} | {situacao}")