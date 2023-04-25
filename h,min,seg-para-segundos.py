print("Este programa transforma hora(s),minuto(s) e segundo(s) em segundo(s)")
h = int(input("Insira hora(s): "))
m = int(input("Insira minuto(s): "))
s = int(input("Insira segundo(s): "))
t = h * 3600 + m * 60 + s
print(t, "segundos")
