import random
lista = []
for i in range(100):
    lista.append(random.randint(1,200))
print(lista)

def buscaSequencial(lista, chave):
    indice = 0
    for num in lista:
        if num == chave:
            return indice
        indice += 1
    return -1

chave = 45
busca = buscaSequencial(lista, chave)

if busca != -1:
    print(f'O número {chave} está na posição {busca} da lista')
else:
    print('O número NÃO foi encontrado')