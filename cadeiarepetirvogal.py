#Ler uma cadeia e criar uma nova cadeia repetindo a vogal
cadeia = input("Insira uma cadeia: ")
aux = ""
for i in range(0,len(cadeia)):
    if cadeia[i] == "A" or cadeia[i] == "E" or cadeia[i] == "I" or cadeia[i] == "O" or cadeia[i] == "U" or cadeia[i] == "a" or cadeia[i] == "e" or cadeia[i] == "i" or cadeia[i] == "o" or cadeia[i] == "u":
       aux = aux + cadeia[i]+cadeia[i]
    else:
        aux=aux+cadeia[i]
print ("Nova cadeia:", aux)