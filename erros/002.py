# Crie um programa que peça ao usuário o nome de uma cor e mostre seu valor em RGB de acordo com um dicionário pré-definido. O programa deve tratar exceções caso o nome da cor não exista no dicionário.

cores = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255)}

try:
    color = input('Tell me a color to see its corresponding RGB Value: ').lower()
    print(cores[color])
except KeyError:
        print('ERROR!!! Color Not Found')