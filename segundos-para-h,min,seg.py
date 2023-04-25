print("Este programa transforma tempo em segundos para horas,minutos e segundos")
t = int(input("Insira o tempo em segundos:"))
h = t // 3600
m = (t % 3600) // 60
s = ((t % 3600) % 60)
print(h, "hora(s)", m, "minuto(s)", s, "segundo(s)")
