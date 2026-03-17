import random

lista = []
for i in range(45):
    lista.append(random.randint(1, 40))
print(lista)

def menor_indice(lista):
    menor = lista[0]
    indice_menor = 0

    for i, num in enumerate(lista):
        if num < menor:
            menor = num
            indice_menor = i

    return menor, indice_menor

menor, indice = menor_indice(lista)

if menor is not None:
    print(f"O menor número da lista é {menor} e está na posição {indice}")
else:
    print("Lista vazia.")