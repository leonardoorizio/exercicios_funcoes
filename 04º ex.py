'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero
ou negativo.
'''

def positivo_negativo():

    cliente = int(input('Entre com um número:'))

    if cliente <= 0:
        print('N')
    else:
        print('P')

positivo_negativo()
