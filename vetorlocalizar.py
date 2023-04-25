vet = []
n = int(input("n: "))
while n >= 0:
    vet.append(n)
    n=int(input("n: "))
print(vet)

n = int(input("n: "))
achou = False
for i in range(0,len(vet)):
    if n == vet[i]:
        print(i)
        achou = True
if not achou:
    print("Não encontrado",n)