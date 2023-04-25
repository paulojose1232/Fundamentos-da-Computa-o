matriz = []
for i in range(0,3):
    matriz.append(0)
    matriz[i] = []
    for j in range(0,3):
        matriz[i].append(int(input("n:")))

print(matriz)

somaDiagonal = 0
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            somaDiagonal += matriz[i][j]

print(somaDiagonal)