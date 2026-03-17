def busca_matriz(matriz, alvo):
    for linha, valores_linha in enumerate(matriz):
        for coluna, valor in enumerate(valores_linha):
            if valor == alvo:
                return linha, coluna

    return -1, -1


matriz = [
    [5, 8, 2],
    [9, 1, 7],
    [4, 6, 3]
]

numero = 7
linha, coluna = busca_matriz(matriz, numero)

if linha != -1:
    print(f"O número {numero} foi encontrado na posição ({linha}, {coluna}).")
else:
    print("Número não encontrado.")