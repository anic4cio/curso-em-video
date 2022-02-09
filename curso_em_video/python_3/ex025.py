"""
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = str(input('Insira seu nome completo: ')).strip().title().split()
print('Silva' in nome)
