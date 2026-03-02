soma = 0
while True:
    n = float(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    soma += n
print(f"Soma total: {soma}")