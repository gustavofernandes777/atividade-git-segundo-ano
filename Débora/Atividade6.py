tabela_brasileirao= [
["classificação", ["p","j", "v","e", "d"], ["ÚLT.Jogod"]],
["flamengo",23, 11, 7, 2, 2,20, 10, 10, 69,["e", "d", "v", "v", "v"]],
["palmeiras", 29, 12, 9, 2, 1, 22, 10, 12, 80,["v", "v", "v", "e", "v"]],
["fluminense", 23, 12, 7, 2, 3, 21, 15, 6, 63,["v", "v", "e", "d", "v"]],
["sao paulo", 20, 12, 6, 2, 4, 16, 11, 5, 55,["d", "e", "v", "d", "d"]],
["bahia", 20, 11, 6, 2, 3, 15, 12, 3, 60, ["d", "v", "d", "v", "d"]],
["athletico-PR", 19, 12, 6, 1, 5, 17, 14, 3, 52,["v", "d", "d", "v","d"]],
["coritiba",19, 12, 5, 4, 3, 15, 12,3, 52,["d", "e", "e", "e","v"]],
["braganito", 17, 12,5, 2, 5, 15, 14, 1, 47,["d", "v", "v","d", "v"]],
["botafogo", 16,11, 5, 1, 5, 22, 22, 0, 48,["v", "v", "v", "e", "v"]],
["vasco", 16, 12, 4, 4, 4, 18, 18, 0, 44,["v","e","d","e","v"]],
["vitoria",15, 11, 4, 3, 4, 11, 14, -3, 45,["v", "d", "e", "v", "e"]],
["cruzeiro", 13, 12, 3, 4, 5, 16, 21, -5,["e", "v", "d", "v", "v"]],
["santso", 13, 12, 3, 4, 5, 16, 19, -3, ["e",""]],
["Grêmio", 13, 12, 9, 2, 1, ["d", "d", "e", "e", "d"]],
["Internacional", 13, 12, 3, 4, 5, ["v", "e", "v", "e", "d"]],
["Santos", 13, 12, 3, 4, 5, ["e", "v", "d", "v", "d"]],
["Cruzeiro", 13, 12, 3, 4, 5, ["e", "v", "d", "v", "v"]],
["Corinthians", 12, 12, 2, 6, 4, ["e", "d", "d", "e", "e"]],
["Mirassol", 9, 11, 2, 3, 6, ["d", "d", "d", "d", "v"]],
["Remo", 8, 12, 1, 5, 6, ["v", "d", "e", "e", "d"]],
tabela_brasileirao = [
    ["Classificação", "P", "J", "V", "E", "D", "GM", "GS", "SG", "Aproveitamento", "Últimos Jogos"],

    ["Flamengo", 23, 11, 7, 2, 2, 20, 10, 10, 69, ["E", "D", "V", "V", "V"]],
    ["Palmeiras", 29, 12, 9, 2, 1, 22, 10, 12, 80, ["V", "V", "V", "E", "V"]],
    ["Fluminense", 23, 12, 7, 2, 3, 21, 15, 6, 63, ["V", "V", "E", "D", "V"]],
    ["São Paulo", 20, 12, 6, 2, 4, 16, 11, 5, 55, ["D", "E", "V", "D", "D"]],
    ["Bahia", 20, 11, 6, 2, 3, 15, 12, 3, 60, ["D", "V", "D", "V", "D"]],
    ["Athletico-PR", 19, 12, 6, 1, 5, 17, 14, 3, 52, ["V", "D", "D", "V", "D"]],
    ["Coritiba", 19, 12, 5, 4, 3, 15, 12, 3, 52, ["D", "E", "E", "E", "V"]],
    ["Bragantino", 17, 12, 5, 2, 5, 15, 14, 1, 47, ["D", "V", "V", "D", "V"]],
    ["Botafogo", 16, 11, 5, 1, 5, 22, 22, 0, 48, ["V", "V", "V", "E", "V"]],
    ["Vasco", 16, 12, 4, 4, 4, 18, 18, 0, 44, ["V", "E", "D", "E", "V"]],
    ["Vitória", 15, 11, 4, 3, 4, 11, 14, -3, 45, ["V", "D", "E", "V", "E"]],
    ["Cruzeiro", 13, 12, 3, 4, 5, 16, 21, -5, 36, ["E", "V", "D", "V", "V"]],
    ["Santos", 13, 12, 3, 4, 5, 16, 19, -3, 36, ["E", "V", "D", "V", "D"]],
    ["Grêmio", 13, 12, 3, 4, 5, 12, 16, -4, 36, ["D", "D", "E", "E", "D"]],
    ["Internacional", 13, 12, 3, 4, 5, 14, 17, -3, 36, ["V", "E", "V", "E", "D"]],
    ["Corinthians", 12, 12, 2, 6, 4, 10, 14, -4, 33, ["E", "D", "D", "E", "E"]],
    ["Mirassol", 9, 11, 2, 3, 6, 9, 18, -9, 27, ["D", "D", "D", "D", "V"]],
    ["Remo", 8, 12, 1, 5, 6, 8, 20, -12, 22, ["V", "D", "E", "E", "D"]],
]

print("========== TABELA ORIGINAL ==========\n")


print("\n========== ATUALIZAÇÃO DOS TIMES ==========\n")

for time in tabela_brasileirao[1:]:

    if time[0] == "Corinthians":
        time[1] += 15
        print(f"{time[0]} recebeu bônus de 15 pontos!")

    elif time[0] in ["Palmeiras", "São Paulo", "Santos", "Flamengo"]:
        time[1] -= 3
        print(f"{time[0]} perdeu 3 pontos!")

tabela_ordenada = sorted(
    tabela_brasileirao[1:],
    key=lambda row: row[1],
    reverse=True
)

print("\n========== CLASSIFICAÇÃO FINAL ==========\n")

print(tabela_brasileirao[0])

for posicao, time in enumerate(tabela_ordenada, start=1):
    print(
        f"{posicao}º Lugar -> "
        f"{time[0]} | "
        f"{time[1]} pts | "
        f"Vitórias: {time[3]} | "
        f"Saldo: {time[8]} | "
        f"Últimos jogos: {time[10]}"
    )

print("\n========== PESQUISA DE TIME ==========\n")

for time in tabela_brasileirao[1:]:

for linha in tabela_brasileirao:
    print(linha)
    if "Flamengo" in time[0]:
        print("Time encontrado!")
        print(f"Nome: {time[0]}")
        print(f"Pontos: {time[1]}")
        print(f"Jogos: {time[2]}")
        print(f"Vitórias: {time[3]}")
        print(f"Empates: {time[4]}")
        print(f"Derrotas: {time[5]}")
        print(f"Saldo de gols: {time[8]}")
        print(f"Aproveitamento: {time[9]}%")
        print(f"Últimos jogos: {time[10]}")