v = []
for i in range (0,5):
    v.append(int(input("nota: ")))
print("Vetor: ",v)

for i in range (0,4):
    for j in range(i+1,5):
        if v[i] > v[j]:
            aux = v[i]
            v[i] = v[j]
            v[j] = aux
print("Vetor ordenado",v)
elem = int(input("Elemento do vetor: "))
pos = 0
inicio = 0
fim = len(v)-1
achou = False
while inicio <= fim and not achou:
    meio=(inicio+fim)//2
    if elem== v[meio]:
        pos=meio
        achou=True
    elif elem< v[meio]:
        fim = meio-1
    else:
        inicio=meio+1
if achou:
    print("Posição encontrada:",pos)
else:
    print("Não encontrado")