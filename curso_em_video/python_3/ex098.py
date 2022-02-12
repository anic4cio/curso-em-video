"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep
def contagem_padrao():
    a = 1
    b = 11
    c = 1
    for x in range(a, b, c):
        print(x, end=' ')
        sleep(.3)
    print('FIM!')


def contagem_regressiva():
    a = 10
    b = 0
    c = -2
    for y in range(a, b, c):
        print(y, end=' ')
        sleep(.3)
    print('Terminou!')


def contagem_personalizada():
    a = int(input('Número para iniciar a contagem: '))
    b = int(input('Número final da contagem: '))
    c = int(input('Passo da contagem: '))
    if b < 0:
        c = c - (c * 2)
    for z in range(a, b, c):
        print(z, end=' ')
        sleep(.3)


contagem_padrao()
contagem_regressiva()
contagem_personalizada()
