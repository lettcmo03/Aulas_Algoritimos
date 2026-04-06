import random

num = random.randrange(100, 500)

sum = list(map(int, str(num)))

print(sum)

def somaRecursiva(sum):
    if len(sum) == 0:
        return 0
    return sum[0] + somaRecursiva(sum[1:])

res = somaRecursiva(sum)

print(res)