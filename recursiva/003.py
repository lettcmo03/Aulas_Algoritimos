palavra = 'perfeita'

lista = palavra.split()

def inverter(lista):
    if len(lista) <= 1:
        return lista
    return lista[-1] + inverter(lista[1:-1]) + lista[0]

print(inverter(palavra))