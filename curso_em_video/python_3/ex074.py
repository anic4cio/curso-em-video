"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint
tupla_random = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print(tupla_random)
print('O maior valor na tupla foi {}.'.format(max(tupla_random)))
print('O menor valor na tupla foi {}.'.format(min(tupla_random)))
