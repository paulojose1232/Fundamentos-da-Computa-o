matriz = []
somaPares = 0
for i in range(0, 3):
    matriz.append(0)
    matriz[i] = []
    for j in range(0,3):
        n = int(input("Coloque um numero: "))
        if n%2==0:
            somaPares += n
        matriz[i].append(n)
print(matriz)
print(somaPares)
