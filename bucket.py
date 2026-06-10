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

def bucket_sort(lista):
    if len(lista)==0:
        return []
    lista=lista.copy()
    maior=max(lista)
    menor=min(lista)
    if maior==menor:
        return lista
    quantidade_buckets=len(lista)
    buckets=[[] for _ in range(quantidade_buckets)]
    for numero in lista:
        indice=int((numero-menor)/(maior-menor+1)*quantidade_buckets)
        buckets[indice].append(numero)
    ordenada=[]
    for bucket in buckets:
        ordenada.extend(insertion_sort(bucket))
    return ordenada

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=bucket_sort(lista_teste)
fim=time.time()

print("Bucket Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])