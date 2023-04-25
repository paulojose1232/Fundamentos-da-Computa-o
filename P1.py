def saque(notas):
    notas_dadas = {}

    try:
        valor = int(input("Entre com o valor desejado: "))
    except:
        print("Valor inválido. Utilize um número e tente de novo")
        return False, notas_dadas

    if valor > soma_notas(notas):
        print("Valor acima do saldo atual da máquina.")
        return False, notas_dadas

    for nota, quantidade in notas.items():
        valor_nota = int(nota)

        qtd_notas_necessarias = int(valor / valor_nota)

        if qtd_notas_necessarias > quantidade:
            qtd_nota_dada = quantidade
        else:
            qtd_nota_dada = qtd_notas_necessarias

        valor -= qtd_nota_dada * valor_nota
        notas_dadas[nota] = qtd_nota_dada

    if valor > 0:
        print(
            "A combinação de notas existente não consegue disponibilizar o valor requisitado."
        )
        return False, notas_dadas

    print("Você receberá:")
    for nota, quantidade in notas_dadas.items():
        if quantidade > 0:
            print(str(quantidade), "nota(s() de", nota)

    return True, notas_dadas


def deposito(notas):
    for nota in notas.keys():
        try:
            notas[nota] += int(input(f"Quantidade de notas de {nota}: "))
        except:
            print("Valor inválido. Utilize um número e tente de novo")
            return False, notas
    return True, notas


def mostra_historico(historico):
    if len(historico) == 0:
        print("Nenhuma operação foi realizada ainda.")
    for operacao in historico:
        operador = "+" if operacao[0] == "Deposito" else "-"
        print(operador + str(operacao[1]))
    return


def mostra_saldo(notas):
    for nota, quantidade in notas.items():
        print(str(nota) + ": " + str(quantidade))

    print("Total:", str(soma_notas(notas)), "reais.")
    return


def soma_notas(notas):
    return (
        100 * notas["100"]
        + 50 * notas["50"]
        + 20 * notas["20"]
        + 10 * notas["10"]
        + 5 * notas["5"]
        + 2 * notas["2"]
        + notas["1"]
    )


def menu():
    print("\nEscolha a operação")
    print("1 - Saque")
    print("2 - Deposito")
    print("3 - Historico")
    print("4 - Saldo")
    print("5 - Sair")
    operacao = input("Operação: ")
    if operacao not in "12345":
        print("Operação inválida.")
        return "0"
    return operacao


def main():
    historico = []
    notas = {"100": 100, "50": 100, "20": 100, "10": 100, "5": 100, "2": 100, "1": 100}

    operacao = menu()
    while operacao in "01234":
        if operacao == "1":
            realizavel, notas_necessarias = saque(notas)
            if realizavel:
                historico.append(["Saque", soma_notas(notas_necessarias)])
                for nota, quantidade in notas_necessarias.items():
                    notas[nota] -= quantidade

        elif operacao == "2":
            realizavel, notas = deposito(notas)
            if realizavel:
                historico.append(["Deposito", soma_notas(notas)])

        elif operacao == "3":
            mostra_historico(historico)

        elif operacao == "4":
            mostra_saldo(notas)

        operacao = menu()


main()
