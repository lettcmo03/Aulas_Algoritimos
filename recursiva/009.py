def soma_lista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + soma_lista(lista[1:])


print(soma_lista([1, 2, 3, 4]))  
print(soma_lista([]))           