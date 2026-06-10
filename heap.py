import random
import time
import heapq

def heap_sort(lista):
    lista=lista.copy()
    heapq.heapify(lista)
    ordenada=[]
    while lista:
        ordenada.append(heapq.heappop(lista))
    return ordenada

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=heap_sort(lista_teste)
fim=time.time()

print("Heap Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])