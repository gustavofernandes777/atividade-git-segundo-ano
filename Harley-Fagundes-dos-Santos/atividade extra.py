grupoA = []
grupoB = []

print("CADASTRO DO GRUPO A")

for i in range(4):
    selecao = input("Digite a seleção que deseja colocar neste grupo: ")
    grupoA.append(selecao)

print("\nGrupo A:", grupoA)

print("\nCADASTRO DO GRUPO B")

for i in range(4):
    selecao = input("Digite a seleção que deseja colocar neste grupo: ")
    grupoB.append(selecao)

print("\nGrupo B:", grupoB)

tabelaA = []
tabelaB = []

for selecao in grupoA:
    tabelaA.append([selecao, 0, 0, 0, 0, 0, 0, 0, 0])

for selecao in grupoB:
    tabelaB.append([selecao, 0, 0, 0, 0, 0, 0, 0, 0])


def atualizar(selecao1, gols1, selecao2, gols2):

    selecao1[2] += 1
    selecao2[2] += 1

    selecao1[6] += gols1
    selecao1[7] += gols2

    selecao2[6] += gols2
    selecao2[7] += gols1

    if gols1 > gols2:

        selecao1[1] += 3
        selecao1[3] += 1
        selecao2[5] += 1

    elif gols2 > gols1:

        selecao2[1] += 3
        selecao2[3] += 1
        selecao1[5] += 1

    else:

        selecao1[1] += 1
        selecao2[1] += 1

        selecao1[4] += 1
        selecao2[4] += 1

    selecao1[8] = selecao1[6] - selecao1[7]
    selecao2[8] = selecao2[6] - selecao2[7]


def faseDeGrupos(tabela, grupo):

    print(f"\nFASE DE GRUPOS - {grupo}")

    for i in range(len(tabela)):

        for j in range(i + 1, len(tabela)):

            print(f"\n{tabela[i][0]} x {tabela[j][0]}")

            gols1 = int(input(f"Gols de {tabela[i][0]}: "))
            gols2 = int(input(f"Gols de {tabela[j][0]}: "))

            atualizar(
                tabela[i],
                gols1,
                tabela[j],
                gols2
            )


faseDeGrupos(tabelaA, "GRUPO A")
faseDeGrupos(tabelaB, "GRUPO B")

tabelaA.sort(
    key=lambda x: (x[1], x[8], x[6]),
    reverse=True
)

tabelaB.sort(
    key=lambda x: (x[1], x[8], x[6]),
    reverse=True
)

print("\n========================")
print("CLASSIFICAÇÃO GRUPO A")
print("========================")

for i in range(len(tabelaA)):

    print(
        f"{i+1}º {tabelaA[i][0]} | "
        f"PTS:{tabelaA[i][1]} | "
        f"J:{tabelaA[i][2]} | "
        f"V:{tabelaA[i][3]} | "
        f"E:{tabelaA[i][4]} | "
        f"D:{tabelaA[i][5]} | "
        f"GP:{tabelaA[i][6]} | "
        f"GC:{tabelaA[i][7]} | "
        f"SG:{tabelaA[i][8]}"
    )

print("\n========================")
print("CLASSIFICAÇÃO GRUPO B")
print("========================")

for i in range(len(tabelaB)):

    print(
        f"{i+1}º {tabelaB[i][0]} | "
        f"PTS:{tabelaB[i][1]} | "
        f"J:{tabelaB[i][2]} | "
        f"V:{tabelaB[i][3]} | "
        f"E:{tabelaB[i][4]} | "
        f"D:{tabelaB[i][5]} | "
        f"GP:{tabelaB[i][6]} | "
        f"GC:{tabelaB[i][7]} | "
        f"SG:{tabelaB[i][8]}"
    )

primeiroA = tabelaA[0]
segundoA = tabelaA[1]

primeiroB = tabelaB[0]
segundoB = tabelaB[1]

print("\nCLASSIFICADOS")

print("Grupo A:")
print("1º", primeiroA[0])
print("2º", segundoA[0])

print("\nGrupo B:")
print("1º", primeiroB[0])
print("2º", segundoB[0])


def mataMata(time1, time2):

    print(f"\n{time1} x {time2}")

    gols1 = int(input(f"Gols de {time1}: "))
    gols2 = int(input(f"Gols de {time2}: "))

    if gols1 > gols2:

        vencedor = time1

    elif gols2 > gols1:

        vencedor = time2

    else:

        print("Empate!")

        while True:

            vencedor = input(
                f"Quem venceu nos pênaltis ({time1} ou {time2})? "
            )

            if vencedor == time1 or vencedor == time2:
                break

            print("Digite uma seleção válida.")

    return vencedor, gols1, gols2


print("\n========================")
print("SEMIFINAIS")
print("========================")

print(f"{primeiroA[0]} x {segundoB[0]}")
print(f"{primeiroB[0]} x {segundoA[0]}")

finalista1, semi1g1, semi1g2 = mataMata(
    primeiroA[0],
    segundoB[0]
)

finalista2, semi2g1, semi2g2 = mataMata(
    primeiroB[0],
    segundoA[0]
)

if finalista1 == primeiroA[0]:
    eliminadoSemi1 = segundoB[0]
else:
    eliminadoSemi1 = primeiroA[0]

if finalista2 == primeiroB[0]:
    eliminadoSemi2 = segundoA[0]
else:
    eliminadoSemi2 = primeiroB[0]

print("\nFINALISTAS")
print(finalista1)
print(finalista2)

print("\nDISPUTA DE TERCEIRO LUGAR")

terceiroLugar, terceiroG1, terceiroG2 = mataMata(
    eliminadoSemi1,
    eliminadoSemi2
)

print("\n========================")
print("FINAL")
print("========================")

campeao, finalg1, finalg2 = mataMata(
    finalista1,
    finalista2
)

if campeao == finalista1:
    viceCampeao = finalista2
else:
    viceCampeao = finalista1

print("\n========================")
print("RESULTADOS DAS SEMIFINAIS")
print("========================")

print(
    f"{primeiroA[0]} {semi1g1} x {semi1g2} {segundoB[0]}"
)

print(
    f"{primeiroB[0]} {semi2g1} x {semi2g2} {segundoA[0]}"
)

print("\nRESULTADO DA DISPUTA DE 3º LUGAR")

print(
    f"{eliminadoSemi1} {terceiroG1} x {terceiroG2} {eliminadoSemi2}"
)

print("\n========================")
print("RESULTADO DA FINAL")
print("========================")

print(
    f"{finalista1} {finalg1} x {finalg2} {finalista2}"
)

print("\n========================")
print("CLASSIFICAÇÃO FINAL")
print("========================")

print(" 1º Lugar:", campeao)
print(" 2º Lugar:", viceCampeao)
print(" 3º Lugar:", terceiroLugar)