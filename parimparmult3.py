n = int(input("Insira um número:"))
if n % 2 == 0 and n % 3 == 0:
    print("Par e Multiplo de 3")
elif n % 2 == 0:
    print("Par")
elif n % 2 != 0 and n % 3 == 0:
    print("Impar e Multiplo de 3")
elif n % 2 != 0:
    print("Impar")
