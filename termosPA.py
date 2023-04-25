n = int(input('Quantidade de termos de uma PA: '))
razao = int(input('Razão: '))
termo1 = int(input('Primeiro termo: '))
print(termo1)
termoAtual = termo1
for i in range(1,n):
    termoAtual = termoAtual + razao
    print(termoAtual)