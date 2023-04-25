cont = 0
soma = 0
nome = input("Insira um nome:")
while nome != "fim":
    sexo = input("Insira o gênero:")
    n1 = float(input("Insira nota 1:"))
    n2 = float(input("Insira nota 2:"))
    media = (n1+n2)/2
    if sexo == "F":
        print("Média feminina é igual a",media)
    else:
        cont += 1
        soma = soma + media
    nome = input("Insira um nome:")
if cont > 0:
    print("Média masculina é igual a",soma/cont)
else:
    print("Não tem homem")