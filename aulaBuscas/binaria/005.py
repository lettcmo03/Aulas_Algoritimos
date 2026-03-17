def busca_binaria_nome(lista_nomes, alvo):
    inicio = 0
    fim = len(lista_nomes) - 1
    alvo = alvo.lower()

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_meio = lista_nomes[meio].lower()

        if nome_meio == alvo:
            return meio
        elif nome_meio < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


nomes = ["Amanda", "Beatriz", "Carlos", "Marina", "Pedro"]
print(busca_binaria_nome(nomes, "marina"))