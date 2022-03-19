"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[], [], []]
pares = 0
for s in range(0, 3):
    for w in range(0, 3):
        numero = int(input(f'Digite um número para posição [{s}/{w}]: '))
        if numero % 2 == 0:
            pares += numero
        matriz[s].append(numero)
for s in range(0, 3):
    for w in range(0, 3):
        print(f'[{matriz[s][w]:^3}]', end=' ')
    print()
print(f'A soma dos números pares é {pares}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
