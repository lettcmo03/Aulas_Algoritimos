import random
lista = []
for i in range(45):
    lista.append(random.randint(1,40))
print(lista)

def buscaSequencial(lista, chave):
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
            return indice
    return -1

chave = 13
busca = buscaSequencial(lista, chave)

if busca != -1:
    for indice in range(busca, len(lista)):
        if lista[indice] == chave:
            print(f'O número {chave} está na posição {indice} da lista')
    # print(f'O número {chave} está na posição {busca} da lista')
else:
    print('O número NÃO foi encontrado')