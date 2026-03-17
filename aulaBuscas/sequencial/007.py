import random

def buscar_primeiro_maior_que_50(lista):
    for indice, numero in enumerate(lista):
        if numero > 50:
            return indice, numero

    return -1, -1


lista = [random.randint(1, 100) for _ in range(100)]
print("Lista:", lista)

indice, valor = buscar_primeiro_maior_que_50(lista)

if indice != -1:
    print(f"O primeiro número maior que 50 é {valor} e está no índice {indice}.")
else:
    print("Nenhum número maior que 50 foi encontrado.")