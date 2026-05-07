matriz = [
["Classificação", "P", "J","V","E","D","ÚLT. JOGOS"],
[ "Palmeiras", 29,12,9,2,1,["V","V","V","E","V"]],
[ "Flamengo", 23,11,7,2,2,["V","V"," V","E","V"]],
["FLuminense", 23,12,7,2,3,["V","V","V","E","V"]],
["SAO PAULO", 20,12,6,2,4,["V","V","V","E","V"]],
["BAHIA", 20,11,6,2,3,["V","V","V","E","V"]],
["ATLETICO-PR", 19,12,6,1,5,["V","V","V","E","V"]],
["CORITIBA", 19,12,5,4,3,["V","V","V","E","V"]],
["BRAGANTINO", 17,12,5,2,5,["V","V","V","E","V"]],
["BOTAFOGO", 16,11,5,1,5,["V","V","V","E","V"]],
["VASCO", 16,12,4,4,4,["V","V","V","E","V"]],
["VITORIA", 15,11,4,3,4,["V","V","V","E","V"]],
["ATLETICO-MG", 14,12,4,2,6,["V","V","V","E","V"]],
["GREMIO", 13,12,3,4,5,["V","V","V","E","V"]],
["INTERNACIONAL", 13,12,3,4,5,["V","V","V","E","V"]],
["SANTOS", 13,12,3,4,5,["V","V","V","E","V"]],
["CRUZEIRO", 13,12,3,4,5,["V","V","V","E","V"]],
["CORINTHIANS", 12,12,2,6,4,["V","V","V","E","V"]],
["MIRASOL", 9,11,2,3,6,["V","V","V","E","V"]],
["REMO", 8,12,1,5,6,["V","V","V","E","V"]],
["CHAPECOENSE", 8,11,1,5,5,["V","V","V","E","V"]]
]
matriz.append(["Real Madrid", 78, 11, 1, 1,1,["V","V","V","V","V"]])

matriz[16][1] = 150

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
