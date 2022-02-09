"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados num dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Resultados das jogadas dos dados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
print('~+' * 15, '\n~+ RANKING DOS JOGADORES +~')
cont = 1
for spot in range(0, 7):
    for jogador, pontos in jogadores.items():
        if pontos == (6 - spot):
            sleep(0.5)
            print(f'{cont}° lugar: {jogador} com {pontos}')
            cont += 1
