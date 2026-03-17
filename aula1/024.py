entrada = input("Digite números separados por espaço: ").strip()

numeros = [float(x) for x in entrada.split()]

if not numeros:
        print("Lista vazia.")

print(f"Menor: {min(numeros)}")
print(f"Maior: {max(numeros)}")