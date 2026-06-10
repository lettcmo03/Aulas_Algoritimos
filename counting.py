import random
import time

def counting_sort(lista):
    if len(lista)==0:
        return []
    maior=max(lista)
    contagem=[0]*(maior+1)
    for numero in lista:
        contagem[numero]+=1
    ordenada=[]
    for numero,quantidade in enumerate(contagem):
        ordenada.extend([numero]*quantidade)
    return ordenada

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=counting_sort(lista_teste)
fim=time.time()

print("Counting Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])