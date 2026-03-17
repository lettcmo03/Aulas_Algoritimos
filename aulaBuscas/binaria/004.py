def busca_insercao(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


lista = [1, 3, 5, 7]
print(busca_insercao(lista, 4))
print(busca_insercao(lista, 7))
print(busca_insercao(lista, 8))