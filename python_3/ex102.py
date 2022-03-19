"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

from re import X


def fatorial(numero, show=False):
    fat = 1
    for x in range(numero, 0, -1):
        fat = fat * x
        if show:
            if x > 1:
                print(f'{x} x ', end='')
            if x == 1:
                print('1 = ', end='')
    return fat

print(fatorial(5, show=True))
            