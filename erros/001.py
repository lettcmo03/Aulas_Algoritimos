# Escreva um programa que peça ao usuário dois números e faça a divisão do primeiro pelo segundo. Se o usuário inserir um valor inválido ou tentar dividir por zero, o programa deve exibir uma mensagem de erro apropriada.

try:
    x = int(input('Give me a number: '))
    y = int(input('Give me another number: '))
    
    res = x/y
except ZeroDivisionError:
    print('Can not divide by 0')
except:
    print('Could not complete the division')
else:
    print(res)
finally:
    print('THE END!!!')