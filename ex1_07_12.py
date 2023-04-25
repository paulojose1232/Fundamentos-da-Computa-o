#Questao 1 07/12/2021 Paulo José
def pedaco(M,m):
    for x in range(0, len(M) - len(m) + 1):
        p = 0
        for h in range(0, len(m)):
            if M[x + h]==m[h]:
                p+=1
        if p==len(m):
            return x
    return -1
y = input("Insira a cadeia F : ")
u = input("Insira a cadeia G : ")
if len(y)>len(u):
    if pedaco(y,u)>=0:
        print("G é um segmento de F")
    print("|--------------------------|")
    print("RETORNAR",pedaco(y,u))
else:
    if pedaco(u,y) >= 0:
        print("F é um segmento de G")
    print("|--------------------------|")
    print("RETONAR",pedaco(u, y))