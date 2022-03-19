"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
"""

def jogador(nome, gols=0):
    if nome.strip() == '' or nome in ' ':
        nome = '"desconhecido"'
    if gols not in '0123456789' or gols.strip() == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gols.')

a = str(input('Digite o nome do jogador:'))
b = str(input('Digite o número de gols: '))
jogador(a, b)

