import random
import time

def selection_sort(lista):
    lista=lista.copy()
    for i in range(len(lista)):
        menor=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[menor]:
                menor=j
        lista[i],lista[menor]=lista[menor],lista[i]
    return lista

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=selection_sort(lista_teste)
fim=time.time()

print("Selection Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])