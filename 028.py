entrada = input("Digite números separados por espaço: ").strip()
numeros = [int(x) for x in entrada.split()]

alvo = int(input("Qual número deseja contar? "))

print(f"{alvo} aparece {numeros.count(alvo)} vez(es).")