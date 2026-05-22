matriz= [
    
    ["Classificação", ["P", "J", "V", "E", "D"], ["ÚLT. JOGOS"]],
   
    ["1º Palmeiras", [29, 12, 9, 2, 1], ["v", "v", "e", "v", "e"]],
    ["2º Flamengo", [23, 11, 7, 2, 2], ["d", "v", "v", "e", "v"]],
    ["3º Fluminense", [23, 12, 7, 2, 3], ["e", "v", "v", "e", "d"]],
    ["4º São Paulo", [20, 13, 6, 2, 4], ["d", "e", "v", "v", "e"]],
    ["5º Bahia", [20, 11, 6, 2, 3], ["e", "v", "v", "e", "v"]],
    ["6º Athletico-PR", [19, 12, 6, 1, 5], ["e", "v", "v", "e", "d"]],
    ["7º Coritiba", [19, 12, 5, 4, 3], ["v", "e", "d", "e", "v"]],
    ["8º Bragantino", [17, 12, 5, 2, 5], ["v", "e", "e", "v", "d"]],
    ["9º Botafogo", [16, 11, 5, 1, 5], ["v", "e", "d", "v", "e"]],
    ["10º Vasco", [16, 12, 4, 4, 4], ["d", "v", "e", "d", "v"]],
    ["11º Vitória", [15, 11, 4, 3, 4], ["v", "e", "d", "v", "e"]],
    ["12º Internacional", [14, 10, 4, 2, 4], ["v", "d", "v", "e", "d"]],
    ["13º Atlético-MG", [14, 11, 3, 5, 3], ["e", "e", "v", "d", "e"]],
    ["14º Fortaleza", [13, 11, 3, 4, 4], ["d", "e", "v", "e", "v"]],
    ["15º Cruzeiro", [12, 11, 3, 3, 5], ["e", "d", "d", "v", "v"]],
    ["16º Grêmio", [11, 11, 3, 2, 6], ["d", "v", "e", "d", "d"]],
    ["17º Cuiabá", [10, 11, 2, 4, 5], ["e", "e", "v", "d", "d"]],
    ["18º Criciúma", [9, 10, 2, 3, 5], ["d", "e", "d", "v", "e"]],
    ["19º Juventude", [8, 11, 1, 5, 5], ["e", "d", "e", "e", "d"]],
    ["20º Atlético-GO", [5, 11, 1, 2, 8], ["d", "d", "e", "d", "v"]]
]


for clube in tabela:

    nome = clube[0]

    # Corinthians ganha novos pontos
    if nome == "Corinthians":
        clube[1] = 150

    # Alguns times perdem pontos
    elif nome == "Palmeiras":
        clube[1] -= 10

    elif nome == "Santos":
        clube[1] -= 10

    elif nome == "São Paulo":
        clube[1] -= 10

    elif nome == "Flamengo":
        clube[1] -= 10

# Nova lista sem o cabeçalho
classificacao = []

for i in range(1, len(tabela)):
    classificacao.append(tabela[i])

# Ordena pelos pontos
classificacao = sorted(
    classificacao,
    key=lambda item: item[1],
    reverse=True
)

# Mostra cabeçalho
print(tabela[0])

# Exibe classificação
contador = 1

for clube in classificacao:

    # Define situação
    if contador == 1:
        status = "Campeão"

    elif contador <= 6:
        status = "Libertadores"

    elif contador <= 15:
        status = "Sul-Americana"

    else:
        status = "Rebaixado"

    # Mostra resultado
    print(f"{contador}º Lugar -> {clube} -> {status}")

    contador += 1