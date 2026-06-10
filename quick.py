import random
import time

def quick_sort(lista):
    lista=lista.copy()
    if len(lista)<=1:
        return lista
    pivo=lista[len(lista)//2]
    menores=[x for x in lista if x<pivo]
    iguais=[x for x in lista if x==pivo]
    maiores=[x for x in lista if x>pivo]
    return quick_sort(menores)+iguais+quick_sort(maiores)

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=quick_sort(lista_teste)
fim=time.time()

print("Quick Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])