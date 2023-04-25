#Questão numero 1 30/11/2021
def ml2(m5):
    ml = 0
    for x in range(0,len(m5)):
        for y in range(0,len(m5[0])):
            if m5[x][y] > ml:
                ml=m5[x][y]
    return ml
def createm(m5):
    for x in range(0,x1):
        m5.append(0)
        m5[x] = []
        for y in range(0,x2):
            m5[x].append(int(input("Coloque os lados do quadrilatero : ")))
    return m5
def p2(m5):
    for x in range(0, len(m5)):
        p3 = 0
        for y in range(0, len(m5[0])):
            p3+=m5[x][y]
        v1.append(p3)
    return v1
x1 = 5
x2 = 4
vml = []
v1 = []
m5 = []
createm(m5)
p2(m5)
print("A matriz (m5) colocada é : ")
for x in range(0, x1):
    for y in range(0, x2):
        print(m5[x][y], end=' ')
    print()
print("O vetor com os perimetros (2p) é : ", v1)
print("O maior lado (l) do quadrilátero é : ", ml2(m5))