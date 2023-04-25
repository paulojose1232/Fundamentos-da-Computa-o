n = int(input("Insira sua idade:"))
if n <= 0:
    print("Erro")
elif n <= 3:
    print("Bebê")
elif n <= 11:
    print("Criança")
elif n <= 17:
    print("Adolescente")
elif n <= 30:
    print("Jovem")
elif n <= 64:
    print("Adulto")
else:
    print("Idoso")
