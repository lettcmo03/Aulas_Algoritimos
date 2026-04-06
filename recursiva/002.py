import random

num = random.randrange(100, 500)

sum = list(map(int, str(num)))

print(sum)

def contarInteiros(sum):
    if len(sum) == 0:
        return 0
    return 1 + contarInteiros(sum[1:])

print(contarInteiros(sum))