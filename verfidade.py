print("Este algoritmo lhe classifica quanto sua idade")
n = int(input("Insira sua idade:"))
if n <= 0:
    print("Erro")
else:
    if 1 <= n <= 3:
        print("Bebê")
    else:
        if 4 <= n <= 11:
            print("Criança")
        else:
            if 12 <= n <= 17:
                print("Adolescente")
            else:
                if 18 <= n <= 30:
                    print("Jovem")
                else:
                    if 31 <= n <= 64:
                        print("Adulto")
                    else:
                        print("Idoso")
