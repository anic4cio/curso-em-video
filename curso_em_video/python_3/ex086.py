"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[], [], []]
for x in range(0, 3):
    for t in range(0, 3):
        numero = int(input(f'Digite um número: [{x}:{t}] '))
        matriz[x].append(numero)
for x in range(0, 3):
    for t in range(0, 3):
        print(f'[{matriz[x][t]:^3}]', end=' ')
    print()
