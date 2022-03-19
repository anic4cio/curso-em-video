"""
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

num = int(input('Digite um número de 0 a 9999: '))
uni = num % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print('Unidades: {}'.format(uni))
print('Dezenas: {}'.format(dez))
print('Centenas: {}'.format(cent))
print('Milhares: {}'.format(mil))
