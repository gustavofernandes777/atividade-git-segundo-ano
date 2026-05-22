matriz = [
    ["Classificação", "p", "j", "v", "e", "d", "ULT. JOGOS"],
    ["Palmeiras", 29, 12, 9, 2, 1, ["v", "v", "v", "e", "v"]],
    ["Flamengo", 23, 11, 7, 2, 2, ["e", "d", "v", "v", "v"]],
    ["Fluminense", 23, 12, 7, 2, 4, ["v", "v", "e", "v"]],
    ["São Paulo", 20, 12, 7, 2, 3, ["d", "e", "v", "d", "d"]],
    ["Bahia", 20, 11, 6, 2, 3, ["d", "v", "d", "v", "d"]],
    ["Athletico-PR", 19, 12, 6, 1, 5, ["v", "d", "d", "v", "d"]],
    ["Coritiba", 19, 12, 5, 4, 3, ["d", "e", "e", "e", "v"]],
    ["Bragantino", 17, 12, 5, 2, 5, ["d", "v", "v", "d", "v"]],
    ["Botafogo", 16, 11, 5, 1, 5, ["d", "v", "v", "e", "v"]],
    ["Vasco da Gama", 16, 12, 4, 4, 4, ["v", "e", "d", "e", "v"]],
    ["EC Vitória", 15, 11, 4, 3, 4, ["v", "d", "e", "v", "e"]],
    ["Atlético MG", 14, 12, 4, 2, 6, ["d", "v", "v", "d", "d"]],
    ["Grêmio", 13, 12, 3, 4, 5, ["d", "d", "e", "e", "d"]],
    ["Internacional", 13, 12, 3, 4, 5, ["v", "e", "v", "e", "d"]],
    ["Santos", 13, 12, 3, 4, 5, ["e", "v", "d", "v", "d"]],
    ["Cruzeiro", 13, 12, 3, 4, 5, ["e", "v", "d", "v", "v"]],
    ["Corinthias", 12, 12, 2, 6, 4, ["e", "d", "d", "e", "e"]],
    ["Mirasol", 9, 11, 2, 3, 6, ["d", "d", "d", "d", "v"]],
    ["Remo", 8, 12, 1, 5, 6, ["v", "d", "e", "e", "d"]],
    ["Chapecoense", 8, 11, 1, 5, 5, ["d", "d", "e", "d", "d"]],
    
]

matriz.append(["Barcelona", 85, 33, 28, 1, 4, ["v", "v", "v", "v", "v"]]),

for time in matriz:
    if time[0] == "Corinthias":
       time[1] = 150

    elif time[0] =="Palmeiras" or time[0] == "São Paulo" or time[0] == "Santos" or time[0] == "Flamengo":
        time[1] = time[1] - 10

matriz_ordenada = sorted(matriz[1:], key=lambda row: row[1], reverse=True)

print(matriz[0])
for posicao, time in enumerate(matriz_ordenada):
    print(f"{posicao+1}º {time}")

