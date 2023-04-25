#Questão numero 1 30/11/2021
def criam():
    m = []
    for x in range(0,5):
        m.append(0)
        m[x] = []
        for y in range(0,4):
            m[x].append(int(input("Coloque um número: ")))
    return m
def mL(m):
    mL = 0
    for x in range(0, len(m)):
        for y in range(0, len(m[0])):
            if m[x][y] > mL:
                mL = m[x][y]
    return mL
def cP(m):
    vP = []
    for x in range(0, len(m)):
        p = 0
        for y in range(0, len(m[0])):
            p += m[x][y]
        vP.append(p)
    return vP
m=criam()
for el in m:
    print(f'{el} \n')
print(m)
print(mL(m))