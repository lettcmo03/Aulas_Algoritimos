entrada = input("Digite números separados por espaço: ").strip()
numeros = [float(x) for x in entrada.split()]

print(f"Soma: {sum(numeros)}")