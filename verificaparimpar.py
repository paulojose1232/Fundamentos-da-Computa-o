num = int(input('Escreva um numero: '))
qtdPares = 0
qtdImpares = 0
mediaPares = 0
mediaImpares = 0
somaImpares = 0
somaPares = 0
while num != 0:
    if num%2 == 0:
        qtdPares += 1
        somaPares += num
    else:
        qtdImpares += 1
        somaImpares += num
    num = int(input('Escreva outro número: '))
mediaPares = somaPares/qtdPares
mediaImpares = somaImpares/qtdImpares
print('Quantidade de números pares: ', qtdPares)
print('Média dos numeros pares: ', mediaPares)
print('Quantidade de numeros ímpares: ', qtdImpares)
print('Média dos números ímpares: ', mediaImpares)