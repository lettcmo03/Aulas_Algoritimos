qtd = 10
fib = []

a, b = 0, 1
for _ in range(qtd):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci (10 primeiros):", fib)