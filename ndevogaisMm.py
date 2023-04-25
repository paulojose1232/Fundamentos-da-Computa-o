cadeia = input("Insira sua cadeia:")
cont = 0
for i in range(0,len(cadeia)):
    if cadeia[i].lower()== "a" or cadeia[i].lower()=="e" or cadeia[i].lower()=="i" or cadeia[i].lower()=="o" or cadeia[i].lower()=="u":
        cont = cont+1
print(cont)