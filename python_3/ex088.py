"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import sample
from time import sleep
print('Gerador de números para MEGA SENA!')
jogos = int(input('Quantos jogos deseja gerar? '))
for x in range(1, jogos+1):
    print(f'Jogo {x}: {sorted(sample(range(0, 61), 6))}')
    sleep(0.7)
print('Boa Sorte!')
