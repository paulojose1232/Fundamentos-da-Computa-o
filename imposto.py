print("Este algoritmo calculará sua dívida ISS")
n = int(input("Insira seu saldo:"))
if n < 100:
    print("Isento")
elif n < 1000:
    print("ISS devido:", n * 0.01)
elif n < 10000:
    print("ISS devido:", n * 0.02)
elif n < 100000:
    print("ISS devido:", n * 0.03)
else:
    print("ISS devido:", n * 0.05)
