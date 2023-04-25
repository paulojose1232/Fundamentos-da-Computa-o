#Ler duas strings e imprimir a interseçao
cadeia1 = input("Insira a primeira cadeia: ")
cadeia2 = input("Insira a segunda cadeia: ")
for i in range(0,len(cadeia1)):
    for x in range(0, len(cadeia2)):
        if cadeia1[i] == cadeia2[x]:
            print(cadeia2[x])
