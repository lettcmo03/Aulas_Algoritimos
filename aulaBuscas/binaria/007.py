def contar_menores_que_x(lista_ordenada, alvo):
    inicio = 0
    fim = len(lista_ordenada)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio

    return inicio


lista = [1, 2, 2, 3, 5, 7, 9]
print(contar_menores_que_x(lista, 5))