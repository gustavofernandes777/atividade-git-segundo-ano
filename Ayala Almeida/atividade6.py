matriz =[
  ["Classifição", "P","J", "V", "E", "D", "ULT.JOGOS"],
  ["Palmeiras", 29 , 12,  9, 2, 1, ["V", "V", "V","E","V"]],
  ["Flamengo", 23 , 11, 7, 2, 2, ["E", "D", "V","V","V"]],
  ["Fluminense", 23 , 12,  7, 2, 4, ["V", "V", "V","V"]],
  ["São Paulo", 20 , 12,  6, 2, 3, ["D", "E", "V","D","D"]],
  ["Bahia", 20 , 11, 6 , 2, 3, ["D", "V", "D","V","D"]],
  ["Athlético-PR", 19 , 12,  6, 1, 5, ["V", "D", "D","V","D"]],
  ["Coritiba", 19 , 12,  5, 4, 3, ["D", "E", "E","E","V"]],
  ["Bragantino", 17 , 12,  5, 2, 5, ["D", "V", "V","D","V"]],
  ["Botafogo", 16 , 11,  5, 1, 5, ["D", "V", "V","E","V"]],
  ["Vasco da Gama", 16 , 12, 4, 4, 4, ["V", "E", "D","E","V"]],
  ["EC Vitória", 15 , 11, 4, 3, 4, ["V", "D", "E","V","E"]],
  ["Atlético MG", 14, 12, 4, 2, 6, ["D", "V", "V","D","D"]],
  ["Grêmio", 13 , 12, 3, 4, 5, ["D", "D", "E","E","D"]],
  ["Internacional", 13 , 12, 3, 4, 5, ["V", "E", "V","E","D"]],
  ["Santos", 13 , 12, 3, 4, 5, ["E", "V", "D","V","D"]],
  ["Cruzeiro", 13 , 12, 3, 4, 5, ["E", "V", "D","V","V"]],
  ["Corinthias", 12 , 12, 2, 6, 4, ["E", "V", "V","V","V"]],
  ["Mirasol", 9, 11, 2, 3, 6, ["D", "D", "D","D","V"]],
  ["Remo", 8 , 12, 1, 5, 6, ["V", "D", "E","E","D"]],
  ["Chapecoense", 8 , 11, 1, 5, 5, ["D", "D", "E","D","D"]]
]
 
matriz.append(["Barcelona", 85, 33, 28, 1, 4,["V", "V", "V","V", "V"]])

for time in matriz:
    if time  [0] == "Corinthias":
        time [1] = 150
 
    elif time[0] == "Palmeiras" or time[0] == "São Paulo" or time[0] == "Santos" or time[0] == "Flamengo":
        time[1] = time[1] - 10

matriz_ordenada = sorted(matriz[1:], key=lambda row: row[1], reverse=True)
print(matriz[0])
for posicao, time in enumerate(matriz_ordenada):
    print(f"{posicao+1}º {time}")

    if posicao == 0:
       status = "Campeão"

    elif posicao >= 1 and posicao <= 5:
        status  =  "Libertadores"

    elif posicao >= 6 and posicao <= 14:
        status = "Sulamericana"

    else:
        status = "Rebaixado"

    time.append(status)

print(matriz[10])

for posicao, time in enumerate(matriz_ordenada):
    print(f"{posicao + 1}° Lugar - {time} ")