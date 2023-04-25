n1 = float(input("Insira nota 1: "))
n2 = float(input("Insira nota 2: "))
if (n1+n2)//2>=int(7):
    print("Aprovado")
else:
    if (n1+n2)//2>=4:
        print("Prova final")
    else:
        print("Reprovado")
