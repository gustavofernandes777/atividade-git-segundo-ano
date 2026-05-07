matriz = [
["Classificação" "P", "J", "V", "E", "D", "ULT. JOGOS"],
["Palmeiras", 29,12,9,2,1,["V", "V", "V", "E", "V"]],
["Flamengo", 23,11,7,2,2,["E", "D", "V", "V", "V"]],
["Fluminense", 23,12,7,2,3,["V", "V", "E", "D", "V"]],
["Sao Paulo", 20,12,6,2,4,["D", "E", "V", "D", "D"]],
["Bhaia", 20,11,6,2,3,["D", "V", "D", "V", "D"]],
["Atletico-PR", 19,12,6,1,5,["V", "D", "D", "V", "D"]],
["Coritiba", 19,12,5,4,3,["D", "E", "E", "E", "V"]],
["Bragantino", 17,12,5,2,5,["D", "V", "V", "D", "V"]],
["Botafogo", 16,11,5,1,5,["V", "V", "V", "E", "V"]],
["Vasco", 16,12,4,4,4,["V", "E", "D", "E", "V"]],
["Vitoria", 15,11,4,3,4,["V", "D", "E", "V", "E"]],
["Atletico-MG", 14,12,4,2,6,["D", "V", "V", "D", "D"]],
["Gremio", 13,12,3,4,5,["D", "D", "E", "E", "D"]],
["Internacional", 13,12,3,4,5,["V", "E", "V", "E", "D"]],
["Santos", 13,12,3,4,5,["E", "V", "D", "V", "D"]],
["Cruzeiro", 13,12,3,4,5,["E", "V", "D", "V", "V"]],
["Corinthians", 12,12,2,6,4,["E", "D", "D", "E", "E"]],
["Mirasol", 9,11,2,3,6,["D", "D", "D", "D", "V"]],
["Remo", 8,12,1,5,6,["V", "D", "E", "E", "D"]],
["Chapecoense", 8,11,1,5,5,["D", "D", "E", "D", "D"]],

]

matriz.append(["Real Madrid", 78, 11, 1, 1, 1,["V", "V", "V","V","V"]])


matriz[16][1] = 150

for time in matriz:
    if time[0] == "Corinthians":
        time [1] = 150 
matriz.append(["Barcelona", 78, 11, 1, 1, 1,["V", "V", "V","V","V"]])

for time in matriz:
    if time[0] == "Plameiras":
        time[1] -= 10
        
for time in matriz:
    if time[0] == "Sao Paulo":
        time[1] -= 10
        
for time in matriz:
    if time [0] == "Flamengo":
        time[1] -= 10
        
for time in matriz:
    if time [0] == "Santos":
        time[1] -= 10
        
matriz_ordenada = sorted(matriz[1:], key=lambda x: x[1], reverse=True)

print(matriz [0])
for posicao, time in enumerate (matriz_ordenada):
                 
 if posicao == 0:
   time.append("CAMPEÃO")
 elif posicao >= 1 and posicao <= 5:
    time.append("LIBERTADORES")
    
if posicao >= 6 and posicao <= 17:
    time.append("SULAMERICANA")
elif posicao >= 17:
    time.append("REBAIXADO")
    
print(f"{posicao + 1} {time}")

print(f"{posicao + 1}º {time}")