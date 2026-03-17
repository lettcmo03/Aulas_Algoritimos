def fatorial_rec(n: int) -> int:
    if n < 0:
        raise ValueError("Fatorial não é definido para negativos.")
    if n in (0, 1):
        return 1
    return n * fatorial_rec(n - 1)


def ex34():
    n = int(input("Digite um inteiro >= 0: "))
    print(f"{n}! = {fatorial_rec(n)}")

ex34()