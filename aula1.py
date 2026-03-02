def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def testeAB():
    while True:
        a = float(input("Insira o primeiro valor: "))
        b = float(input("Insira o segundo valor: "))

        if a > b:
            print("certo")
            return a, b
        else:
            print("deu erro (o primeiro valor precisa ser maior que o segundo)")

a, b = testeAB()

resultado1 = soma(a, b)
resultado2 = subtracao(a, b)
resultado3 = multiplicacao(a, b)
resultado4 = divisao(a, b)

print(
    f"a={a}, b={b} -> "
    f"soma={resultado1:.3f}, "
    f"sub={resultado2:.3f}, "
    f"mult={resultado3:.3f}, "
    f"div={resultado4:.3f}"
)