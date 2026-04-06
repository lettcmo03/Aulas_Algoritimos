def contar_elemento(lista, alvo):
    if len(lista) == 0:
        return 0

    if lista[0] == alvo:
        return 1 + contar_elemento(lista[1:], alvo)

    return contar_elemento(lista[1:], alvo)


print(contar_elemento([1, 2, 3, 2, 2, 4], 2))  
print(contar_elemento([5, 5, 5], 1))          