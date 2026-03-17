def busca_ultima_ocorrencia(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista_ordenada[meio] == alvo:
            resultado = meio
            inicio = meio + 1  # continua buscando mais à direita
        elif lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return resultado


lista = [1, 2, 2, 2, 3, 4]
print(busca_ultima_ocorrencia(lista, 2))