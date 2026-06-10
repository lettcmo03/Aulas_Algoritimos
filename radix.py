import random
import time

def radix_sort(lista):
    lista=lista.copy()
    if len(lista)==0:
        return lista
    maior=max(lista)
    expoente=1
    while maior//expoente>0:
        lista=counting_sort_por_digito(lista,expoente)
        expoente*=10
    return lista
def counting_sort_por_digito(lista,expoente):
    n=len(lista)
    saida=[0]*n
    contagem=[0]*10
    for numero in lista:
        indice=(numero//expoente)%10
        contagem[indice]+=1
    for i in range(1,10):
        contagem[i]+=contagem[i-1]
    for i in range(n-1,-1,-1):
        indice=(lista[i]//expoente)%10
        saida[contagem[indice]-1]=lista[i]
        contagem[indice]-=1
    return saida

lista_teste=[random.randint(0,100000) for _ in range(100000)]

inicio=time.time()
lista_ordenada=radix_sort(lista_teste)
fim=time.time()

print("Radix Sort")
print(f"Tempo: {fim-inicio:.4f} segundos")
print(lista_ordenada[:20])