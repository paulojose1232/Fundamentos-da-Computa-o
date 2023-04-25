#Questão numero 2 30/11/2021
def naorepeticao(v2):
    nv=[0]*20
    x=0
    for h in range(0,20):
        found=False
        for k in range(0,x):
            if v2[h]==0:
                found=True
        if not found:
            nv[x]=v2[h]
            x+=1
    return nv
def cv(v1):
    for h in range(0,20):
        v1[h]=int(input('Coloque os números do vetor : '))
    return v1
v3=[0]*20
cv(v3)
print('O vetor de maneira ordenada é : ', naorepeticao(v3))