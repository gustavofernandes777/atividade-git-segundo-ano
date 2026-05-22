matriz = [
    ["Palmeiras", 29, 12, 9, 2, 1, ["V", "V", "V", "E", "V"]],
    ["Flamengo", 23, 11, 7, 2, 2, ["E", "D", "V", "V", "V"]],
    ["Fluminense", 23, 12, 7, 2, 3, ["V", "V", "E", "D", "V"]],
    ["São Paulo", 20, 12, 6, 2, 4, ["V", "D", "V", "V", "E"]],
    ["Bahia", 20, 11, 6, 2, 3, ["V", "V", "D", "E", "V"]],
    ["Athletico-PR", 19, 12, 6, 1, 5, ["D", "V", "V", "D", "V"]],
    ["Coritiba", 19, 12, 5, 4, 3, ["E", "E", "V", "V", "D"]],
    ["RB Bragantino", 17, 12, 5, 2, 5, ["D", "V", "D", "V", "E"]],
    ["Botafogo", 16, 11, 5, 1, 5, ["V", "D", "V", "D", "D"]],
    ["Vasco", 16, 12, 4, 4, 4, ["E", "V", "D", "E", "V"]],
    ["Vitória", 15, 11, 4, 3, 4, ["D", "V", "E", "V", "D"]],
    ["Atlético-MG", 14, 12, 4, 2, 6, ["V", "D", "D", "V", "D"]],
    ["Grêmio", 13, 12, 3, 4, 5, ["E", "E", "V", "D", "E"]],
    ["Internacional", 13, 12, 3, 4, 5, ["D", "V", "D", "E", "V"]],
    ["Santos", 13, 12, 3, 4, 5, ["V", "D", "E", "D", "V"]],
    ["Cruzeiro", 13, 12, 3, 4, 5, ["D", "E", "V", "D", "D"]],
    ["Corinthians", 12, 12, 2, 6, 4, ["E", "D", "D", "E", "E"]],
    ["Mirassol", 9, 11, 2, 3, 6, ["D", "D", "V", "D", "E"]],
    ["Remo", 8, 12, 1, 5, 6, ["E", "E", "D", "D", "E"]],
    ["Chapecoense", 8, 11, 1, 5, 5, ["D", "E", "D", "E", "D"]]
]

matriz.append(["Barcelona", 70, 30, 22, 5, 8, ["V", "V", "V", "V", "E"]])
matriz.remove(matriz[2])

for time in matriz:
    if time[0] == "Corinthians":
        time[1] = 150
    elif time[0] == "Palmeiras":
        time[1] = 19
    elif time[0] == "Flamengo":
        time[1] = 13
    elif time[0] == "São Paulo":
        time[1] = 10
    elif time[0] == "Santos":
        time[1] = 3

matriz_ordenada = sorted(matriz, key=lambda row: row[1], reverse=True)

print(matriz_ordenada[0])

for posicao, time in enumerate(matriz_ordenada):
    print(f"{posicao+1}º {time}")