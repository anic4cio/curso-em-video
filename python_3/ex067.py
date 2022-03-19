"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

tabuada = int(input('Quer ver a tabuada de que número: '))
while True:
    for i in range(1, 11):
        print(f'{tabuada} x {i:2} = {i * tabuada}')
    print(10*'~-')
    tabuada = int(input('Quer ver mais alguma tabuada? \nDigite o número para ver a tabuada  \nOu número negativo para sair: '))
    if tabuada < 0:
        print('\nPrograma encerrado.')
        break
