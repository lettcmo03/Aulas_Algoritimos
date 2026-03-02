import math

def area_circulo(raio: float) -> float:
    if raio < 0:
        raise ValueError("Raio não pode ser negativo.")
    return math.pi * raio ** 2