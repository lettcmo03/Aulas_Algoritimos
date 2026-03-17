try:
    a = float(input("Numerador: "))
    b = float(input("Denominador: "))
    resultado = a / b
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: você digitou um valor inválido.")
else:
    print(f"Resultado: {resultado}")
finally:
        print("Fim do programa.")