# Crie um programa que simule uma transferência bancária. Peça ao usuário o saldo da conta e o valor da transferência. Caso o saldo seja insuficiente, levante uma exceção do tipo ValueError com amensagem "Saldo insuficiente". Trate a exceção adequadamente e informe o usuário.


def realizar_transferencia(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")

    return saldo - valor


def main():
    try:
        saldo = float(input("Digite o saldo da conta: "))
        valor = float(input("Digite o valor da transferência: "))

        novo_saldo = realizar_transferencia(saldo, valor)

        print(f"Transferência realizada com sucesso!")
        print(f"Saldo atual: R$ {novo_saldo:.2f}")

    except ValueError as erro:
        print(f"Erro: {erro}")

    except Exception:
        print("Ocorreu um erro inesperado.")


main()