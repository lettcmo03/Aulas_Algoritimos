def maior_lista(lista):
    if len(lista) == 1:
        return lista[0]

    maior_do_resto = maior_lista(lista[1:])

    if lista[0] > maior_do_resto:
        return lista[0]

    return maior_do_resto


print(maior_lista([4, 7, 2, 9, 1]))  
print(maior_lista([3]))              