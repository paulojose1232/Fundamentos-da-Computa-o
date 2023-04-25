#Questão 2 07/12/2021 Paulo José
#Para mudar a quantidade de posições do vetor, basta mudar o "5" na linha "Vetposicoes"
def A_vetor(V1,V2,V3):
    N4Vetor=[0]*(3*len(V1))
    for s in range(0,len(V1)):
        N4Vetor[3*s] = V1[s]
        N4Vetor[3*s+1] = V2[s]
        N4Vetor[3*s+2] = V3[s]
    return N4Vetor
def P_vetor(V0):
    for h in range(0,len(V0)):
        print(V0[h],end=" ")
    print()
def I_vetor(V1,V2,V3):
    N4Vetor = [0]*(3*len(V1))
    for x in range(0,len(V1)):
        N4Vetor[x]=V1[len(V1)-x-1]
        N4Vetor[x+len(V1)]=V2[len(V2)-x-1]
        N4Vetor[x+len(V1)+len(V2)]=V3[len(V3)-x-1]
    return N4Vetor
def C_vetor(k):
    V0=[0]*int(k)
    for b in range(0,int(k)):
        print("Escolha o elemento", b, "do Vetor:")
        V0[b]=input()
    return V0
Vetposicoes = 5
N1Vetor=C_vetor(Vetposicoes)
N2Vetor=C_vetor(Vetposicoes)
N3Vetor=C_vetor(Vetposicoes)
P_vetor(A_vetor(N1Vetor,N2Vetor,N3Vetor))
print("|-----------------------------------|")
P_vetor(I_vetor(N1Vetor,N2Vetor,N3Vetor))