"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
ciclo = 1
while ciclo <= 10:
    print('{} > '.format(termo), end='')
    print(termo, end='')
    print(' > ' if ciclo < 10 else ' > Fim', end='')
    termo += razao
    ciclo += 1
print('Fim')