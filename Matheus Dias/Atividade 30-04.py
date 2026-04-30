tabela_brasileirao = [
    ["Classificação", ["P", "J", "V", "E", "D"], ["ÚLT. JOGOS"]],
    ["Palmeiras", [29, 12, 9, 2, 1], ["v", "v", "v", "e", "v"]],
    ["Flamengo", [23, 11, 7, 2, 2], ["e", "d", "v", "v", "v"]],
    ["Fluminense", [23, 12, 7, 2, 3], ["v", "v", "e", "d", "v"]],
    ["São Paulo", [20, 12, 6, 2, 4], ["d", "e", "v", "d", "d"]],
    ["Bahia", [20, 11, 6, 2, 3], ["d", "v", "d", "v", "d"]],
    ["Athletico-PR", [19, 12, 6, 1, 5], ["v", "d", "v", "e", "d"]],
    ["Coritiba", [19, 12, 5, 4, 3], ["d", "e", "e", "e", "v"]],
    ["Bragantino", [17, 12, 5, 2, 5], ["d", "v", "d", "e", "v"]],
    ["Botafogo", [16, 11, 5, 1, 5], ["d", "v", "v", "e", "v"]],
    ["Vasco da Gama", [16, 12, 4, 4, 4], ["v", "e", "d", "e", "v"]],
    ["EC Vitória", [15, 11, 4, 3, 4], ["v", "d", "e", "v", "e"]],
    ["Atlético-MG", [14, 12, 4, 2, 6], ["d", "v", "v", "d", "d"]],
    ["Grêmio", [13, 12, 3, 4, 5], ["d", "v", "e", "e", "d"]],
    ["Internacional", [13, 12, 3, 4, 5], ["v", "e", "v", "e", "d"]],
    ["Santos", [13, 12, 3, 4, 5], ["e", "v", "d", "v", "d"]],
    ["Cruzeiro", [13, 12, 3, 4, 5], ["e", "v", "d", "v", "v"]],
    ["Corinthians", [12, 12, 2, 6, 4], ["e", "v", "d", "v", "d"]]
]

for time in tabela_brasileirao[1:]:
    nome = time[0]
    pontos = time[1][0]
    
    if nome == "Corinthians":
        time[1][0] += 150
    elif nome in ["Palmeiras", "Santos", "São Paulo", "Flamengo"]:
        time[1][0] -= 15
        if time[1][0] < 0: time[1][0] = 0

time_novo = ["Fortaleza", [10, 5, 3, 1, 1], ["v", "v", "v", "v", "d"]]
tabela_brasileirao.append(time_novo)

dados_ordenados = sorted(tabela_brasileirao[1:], key=lambda x: x[1][0], reverse=True)

print(f"{'Pos':<4} | {'Time':<15} | {'P':<4} | {'J':<2} | {'V':<2} | {'E':<2} | {'D':<2} | {'Últ. Jogos'}")
print("-" * 60)

for i, time in enumerate(dados_ordenados):
    nome = time[0]
    p, j, v, e, d = time[1]
    ultimos = " ".join(time[2])
    print(f"{i+1:<4} | {nome:<15} | {p:<4} | {j:<2} | {v:<2} | {e:<2} | {d:<2} | {ultimos}")