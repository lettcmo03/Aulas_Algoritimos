def remover_duplicados_mantendo_ordem(valores):
    vistos = set()
    resultado = []
    for v in valores:
        if v not in vistos:
            vistos.add(v)
            resultado.append(v)
    return resultado


def ex():
    entrada = input("Digite itens separados por espaço: ").split()
    sem_duplicados = remover_duplicados_mantendo_ordem(entrada)
    print("Sem duplicados:", sem_duplicados)

ex()