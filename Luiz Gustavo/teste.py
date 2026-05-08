matriz = [
    [10, "oi"],
    [100, "Olá"],
    [1000, "teste"],
    [10000, ":)"],
    [100000, ":("]
]

t = int(input())

for i in matriz:    
    if t == i[0]:
        print(i[1])