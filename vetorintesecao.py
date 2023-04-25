vet1 = [0]*5
vet2 = [0]*5
for i in range(0,5):
    vet1[i] = int(input("Insira um número: "))
for i in range(0,5):
    vet2[i] = int(input("Insira um número: "))
print ("Vetor 1: ",vet1)
print ("Vetor 2: ",vet2)
for i in range(0,5):
    for j in range(0,5):
        if vet1[i]== vet2[j]:
            print ("Números com interseção", vet1[i])