print("Este programa transforma dia(s) em ano(s),mes(es) e dia(s)")
d = int(input("Insira dia(s):"))
a = d // 360
m = (d % 360) // 30
d1 = (d % 360) % 30
print(a, "ano(s)", m, "mes(es)", d1, "dia(s)")
