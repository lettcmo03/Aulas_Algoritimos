entrada = input("Digite números separados por espaço: ").strip()
numeros = [int(x) for x in entrada.split()]
pares = [n for n in numeros if n % 2 == 0]

print("Pares:", pares)