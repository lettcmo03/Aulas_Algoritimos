n_str = input("Digite um número inteiro: ").strip()

sinal = ""
if n_str.startswith("-"):
    sinal = "-"
    n_str = n_str[1:]

invertido = n_str[::-1]
print(f"Invertido: {sinal}{invertido}")