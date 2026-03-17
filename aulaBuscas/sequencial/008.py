import time

def busca_sequencial(lista, chave):
    for indice, numero in enumerate(lista):
        if numero == chave:
            return indice
    return -1


def busca_binaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


lista = list(range(1, 100001))
chave = 99999

inicio_seq = time.perf_counter()
resultado_seq = busca_sequencial(lista, chave)
fim_seq = time.perf_counter()

inicio_bin = time.perf_counter()
resultado_bin = busca_binaria(lista, chave)
fim_bin = time.perf_counter()

tempo_seq = fim_seq - inicio_seq
tempo_bin = fim_bin - inicio_bin

print(f"Busca sequencial: índice {resultado_seq} | tempo: {tempo_seq:.10f} segundos")
print(f"Busca binária: índice {resultado_bin} | tempo: {tempo_bin:.10f} segundos")