def busca_mais_proximo(lista_ordenada, alvo):
    if not lista_ordenada:
        return -1

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

    # depois do loop, inicio e fim ficaram nas posições vizinhas mais próximas
    if inicio >= len(lista_ordenada):
        return fim
    if fim < 0:
        return inicio

    if abs(lista_ordenada[inicio] - alvo) < abs(lista_ordenada[fim] - alvo):
        return inicio
    else:
        return fim


lista = [10, 20, 30, 40, 50]
indice = busca_mais_proximo(lista, 33)
print(indice, lista[indice])