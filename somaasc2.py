s = input("Insira sua cadeia:")
soma = 0
for i in range(0,len(s)):
    soma = soma + ord(s[i])
print("A soma é:",soma)