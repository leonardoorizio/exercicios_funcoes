'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos
'''

def soma():

    valores = []

    for i in range(3):
        i += 1
        valores.append(int(input(f'Entre com o {i}º número:')))

    resultado = sum(valores)
    print(f'Soma dos valores {valores}: {resultado}')

soma()