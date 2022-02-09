""""
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (desconsiderando os espaços).

– Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é {}.'.format(nome.upper()))
print('Em letras minúsculas fica {}.'.format(nome.lower()))
print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
