cadeia = input("Insira a cadeia:")
cont = 0
cont1 = 0
cont2 = 0
for i in range(0,len(cadeia)):
    if cadeia[i].isalpha():
        cont = cont + 1
    elif cadeia[i].isdigit():
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print("letras:",cont,"digitos:",cont1,"outros:",cont2)