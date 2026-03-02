n = int(input("Digite N (>= 1): "))

if n < 1:
    print("N deve ser >= 1") 

soma = sum(range(1, n + 1))

print(f"Soma de 1 até {n}: {soma}")