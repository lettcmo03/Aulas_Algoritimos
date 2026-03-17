entrada = input("Digite números separados por espaço: ").strip()
numeros = [float(x) for x in entrada.split()]

numeros_ordenados = sorted(numeros)

print("Ordenada:", numeros_ordenados)