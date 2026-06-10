import random
import time

def insertion_sort(lista):
    lista=lista.copy()
    for i in range(1,len(lista)):
        chave=lista[i]
        j=i-1
        while j>=0 and lista[j]>chave:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=chave
    return lista

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=insertion_sort(lista_teste)
fim=time.time()

print("Insertion Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])