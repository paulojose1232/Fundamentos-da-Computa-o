b1 = float(input("Bola 1: "))
b2 = float(input("Bola 2: "))
b3 = float(input("Bola 3: "))
b4 = float(input("Bola 4: "))
b5 = float(input("Bola 5: "))
b6 = float(input("Bola 6: "))
b7 = float(input("Bola 7: "))
b8 = float(input("Bola 8: "))
if b1 == b2 == b3 == b4 == b5 == b6 == b7 == b8:
    print("Pesos iguais")
elif b1 != b2 and b1 == b3 and b1 == b4 and b1 == b5 and b1 == b6 and b1 == b7 and b1 == b8:
    print("Bola 2, peso:", b2)
elif b1 != b3 and b1 == b2 and b1 == b4 and b1 == b5 and b1 == b6 and b1 == b7 and b1 == b8:
    print("Bola 3, peso:", b3)
elif b1 != b4 and b1 == b3 and b1 == b2 and b1 == b5 and b1 == b6 and b1 == b7 and b1 == b8:
    print("Bola 4, peso:", b4)
elif b1 != b5 and b1 == b3 and b1 == b4 and b1 == b2 and b1 == b6 and b1 == b7 and b1 == b8:
    print("Bola 5, peso:", b5)
elif b1 != b6 and b1 == b3 and b1 == b4 and b1 == b2 and b1 == b5 and b1 == b7 and b1 == b8:
    print("Bola 6, peso:", b6)
elif b1 != b7 and b1 == b3 and b1 == b4 and b1 == b2 and b1 == b6 and b1 == b5 and b1 == b8:
    print("Bola 7, peso:", b7)
elif b1 != b8 and b1 == b3 and b1 == b4 and b1 == b2 and b1 == b6 and b1 == b7 and b1 == b5:
    print("Bola 8, peso:", b8)
elif b2 != b1 and b2 == b3 and b2 == b4 and b2 == b5 and b2 == b6 and b2 == b7 and b2 == b8:
    print("Bola 1, peso:", b1)
else:
    print("Mais de uma bola com pesos diferentes")
