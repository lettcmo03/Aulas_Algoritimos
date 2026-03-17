def busca_binaria_linha(linha, alvo):
    inicio = 0
    fim = len(linha) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if linha[meio] == alvo:
            return meio
        elif linha[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


def busca_matriz_ordenada(matriz, alvo):
    for i, linha in enumerate(matriz):
        if linha[0] <= alvo <= linha[-1]:
            coluna = busca_binaria_linha(linha, alvo)
            if coluna != -1:
                return i, coluna

    return -1, -1


matriz = [
    [1, 4, 7, 11],
    [12, 15, 18, 20],
    [21, 24, 27, 30],
    [31, 35, 40, 45]
]

print(busca_matriz_ordenada(matriz, 27))