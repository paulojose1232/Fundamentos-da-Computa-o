print("Este algoritmo somará a quantidade de moedas e dará o total em reais")
n1 = int(input('Insira a quantidade de moedas de 1 real: '))
n2 = int(input('Insira a quantidade de moedas de 50 centavos: '))
n3 = int(input('Insira a quantidade de moedas de 25 centavos: '))
n4 = int(input('Insira a quantidade de moedas de 1 centavo '))
n5 = int(input('Insira a quantidade de moedas de 5 centavos: '))
n6 = int(input('Insira a quantidade de moedas de 10 centavos '))
somatotal = n1 * 1 + n2 * 0.5 + n6 * 0.1 + n3 * 0.25 + n4 * 0.01 + n5 * 0.05
print("O valor total é de:", somatotal, "reais")
