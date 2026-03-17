def busca_binaria(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_ordenada[meio] == alvo:
            return meio
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


lista = [1, 3, 5, 7, 9, 11]
print(busca_binaria(lista, 7))