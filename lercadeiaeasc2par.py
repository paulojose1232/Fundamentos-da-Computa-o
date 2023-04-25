cadeia=input("Insira uma cadeia:")
cadeianova = ""
for i in range(0,len(cadeia)):
    if ord(cadeia[i])%2==0:
        cadeianova= cadeianova+cadeia[i]
print(cadeianova)