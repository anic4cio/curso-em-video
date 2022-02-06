from random import choice
from time import sleep
print('Vamos jogar Jokenpô! ')
print('Pedra, papel ou tesoura')
while True:
    acao = ['-Pedra', '-Papel', '-Tesoura']
    acao_jogador = str(input('Digite sua ação: ')).title()
    print('JO...')
    sleep(0.5)
    print('KEN...')
    sleep(0.5)
    print('PÔ...')
    sleep(0.5)
    acao = choice(acao)
    print(acao)
    if acao_jogador == 'Pedra' and acao == '-Pedra':
        print('\033[34mEmpate, vamos jogar novamente?\033[m')
    if acao_jogador == 'Tesoura' and acao == '-Tesoura':
        print('\033[34mEmpate, vamos jogar novamente?\033[m')
    if acao_jogador == 'Papel' and acao == '-Papel':
        print('\033[34mEmpate, vamos jogar novamente?\033[m')
    if acao_jogador == 'Pedra' and acao == '-Tesoura':
        print('\033[32mPerdi :( Vamos jogar novamente?\033[m')
    if acao_jogador == 'Papel' and acao == '-Pedra':
        print('\033[32mPerdi :( Vamos jogar novamente?\033[m')
    if acao_jogador == 'Tesoura' and acao == '-Papel':
        print('\033[32mPerdi :( Vamos jogar novamente?\033[m')
    if acao_jogador == 'Tesoura' and acao == '-Pedra':
        print('\033[31mGanhei! Vamos jogar novamente?\033[m')
    if acao_jogador == 'Pedra' and acao == '-Papel':
        print('\033[31mGanhei! Vamos jogar novamente?\033[m')
    if acao_jogador == 'Papel' and acao == '-Tesoura':
        print('\033[31mGanhei! Vamos jogar novamente?\033[m')
    if acao_jogador != 'Pedra' and acao_jogador != 'Tesoura' and acao_jogador != 'Papel':
        print('Ação inválida. Jogue novamente!')