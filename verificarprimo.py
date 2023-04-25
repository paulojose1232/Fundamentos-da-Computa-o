n = int(input("Insira a quantidade de números a ser avaliado:"))
cont = 0
for i in range(1,n+1):
    num = int(input("Insira o número para ser avaliado:"))
    primo = True
    for i in range(2,num//2+1):
        if num % i ==0:
            primo = False
            print(num,"não é primo")
    if primo == True:
        cont = cont +1
        print(num,"é primo")
print(cont,"Total de números primos")