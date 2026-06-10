import random
import time

def bubble_sort(lista):
    lista=lista.copy()
    for i in range(len(lista)):
        trocou=False
        for j in range(0,len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]=lista[j+1],lista[j]
                trocou=True
        if not trocou:
            break
    return lista

lista_teste=[random.randint(0,10000) for _ in range(10000)]

inicio=time.time()
lista_ordenada=bubble_sort(lista_teste)
fim=time.time()

print("Bubble Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])