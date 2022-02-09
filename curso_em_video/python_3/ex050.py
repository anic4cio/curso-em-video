"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

soma = 0
for seis in range(0, 6):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        soma += numeros

print('A soma de todos os pares foi {}'.format(soma))
