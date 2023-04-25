#Fazer um programa para ler as notas de uma turma de 40 alunos, imprimir a qtd de alunos acima da media da turma
soma = 0
cont = 0
notas = [0.0]*5
for i in range(0,5):
    nota = float(input("Insira nota: "))
    notas[i] = nota
    soma = soma+notas[i]
media = soma/5
print ("Média é", media)
for j in range(0,5):
    if notas[j] > media:
        cont = cont + 1
print("Quantidade de notas acima da média da turma:",cont)