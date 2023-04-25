cont = 0
contb=0
conta=0
cadeia = input("insira uma cadeia:")
for i in range(0,len(cadeia)):
    if cadeia[i].isalpha():
        contb=contb+1
    elif cadeia[i].isdigit():
        conta=conta+1
    else:
        cont = cont + 1
print(cont)