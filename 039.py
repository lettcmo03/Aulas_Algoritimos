while True:
    print("\n=== MENU ===")
    print("1 - Dizer Olá")
    print("2 - Somar dois números")
    print("0 - Sair")

    opcao = input("Escolha: ").strip()

    match opcao:
        case "1":
            print("Olá! 😊")

        case "2":
            try:
                a = float(input("A: "))
                b = float(input("B: "))
                print(f"Soma: {a + b}")
            except ValueError:
                print("Digite apenas números válidos.")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida.")