def mostrar_menu():
    print("\n--- Bem-vindo ao seu banco virtual ---")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Transferência")
    print("4 - Extrato")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")
    return escolha


def deposito(saldo, extrato):
    try:
        valor = float(input("Quanto você quer depositar? R$ "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
        else:
            print("Não é possível depositar valores negativos ou zero.")

    except ValueError:
        print("Digite um valor válido!")

    return saldo, extrato


def saque(saldo, extrato):
    try:
        valor = float(input("Quanto você quer sacar? R$ "))

        if valor > 0:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Saque: -R$ {valor:.2f}")
                print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente para este saque.")
        else:
            print("Não é possível sacar valores negativos ou zero.")

    except ValueError:
        print("Digite um valor válido!")

    return saldo, extrato


def transferencia(saldo, extrato):
    conta = input("Digite o número da conta para transferência: ")

    try:
        valor = float(input("Quanto você quer transferir? R$ "))

        if valor > 0:
            if valor <= saldo:
                saldo -= valor
                extrato.append(f"Transferência para conta {conta}: -R$ {valor:.2f}")
                print(f"Transferência realizada com sucesso! Novo saldo: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente para esta transferência.")
        else:
            print("Não é possível transferir valores negativos ou zero.")

    except ValueError:
        print("Digite um valor válido!")

    return saldo, extrato


def mostrar_extrato(saldo, extrato):
    print("\n--- Extrato da sua conta ---")

    if extrato:
        for registro in extrato:
            print(registro)
    else:
        print("Nenhuma movimentação ainda.")

    print(f"Saldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0.0
    extrato = []

    while True:
        escolha = mostrar_menu()

        if escolha == "1":
            saldo, extrato = deposito(saldo, extrato)

        elif escolha == "2":
            saldo, extrato = saque(saldo, extrato)

        elif escolha == "3":
            saldo, extrato = transferencia(saldo, extrato)

        elif escolha == "4":
            mostrar_extrato(saldo, extrato)

        elif escolha == "5":
            print("Obrigado por usar nosso banco. Até mais!")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()