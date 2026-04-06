# Escreva um programa que solicite um número ao usuário. Se o número for maior que 10, exiba uma mensagem dizendo que o número é válido. Utilize o bloco else para imprimir que o programa foi executado com sucesso, e o bloco finally para imprimir "Programa encerrado".
def validNum(num):
    return num > 10
try:
    num = int(input("Give me a number: "))
    if validNum(num):
        print('Is a Valid Number!')
    else:
        print("NOT a Valid Number!")
except Exception as e:
    print(f'May have an error of {e}')
finally:
    print('Program is finished')