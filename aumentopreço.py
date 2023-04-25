n = int(input("Insira o valor do produto:"))
if n <= 50:
    print("Barato", ",", "Novo valor:", n * 1.05)
elif n <= 80:
    print("Barato", ",", "Novo valor:", n * 1.1)
elif n <= 100:
    print("Normal", ",", "Novo valor:", n * 1.1)
elif n <= 120:
    print("Normal", ",", "Novo valor:", n * 1.15)
elif n <= 200:
    print("Caro", ",", "Novo valor:", n * 1.15)
else:
    print("Muito caro", ",", "Novo valor:", n * 1.15)
