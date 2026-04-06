# Escreva uma função que verifica se uma senha possui no mínimo 8 caracteres e pelo menos um número. Se a senha não atender aos requisitos, levante uma exceção com uma mensagem personalizada. Trate a exceção e mostre a mensagem ao usuário.

def validKey(passkey):
    if len(passkey) < 8:
        raise ValueError('Too Short! Try again')
    else:
        print('Passkey created Succesfully')

try:
    passkey = input('Type your passkey: ')
    validKey(passkey)
except:
    print('Invalid Passkey')
finally:
    print('Program is finished')