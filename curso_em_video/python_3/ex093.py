"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será guardado num dicionário, incluindo
o total de gols feitos durante o campeonato.
"""

carreira = {}
gols = []
cont = 1
total = 0
carreira['jogador'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas {carreira["jogador"]} jogou? '))
for x in range(1, partidas+1):
    gol = int(input(f'  Quantos gols na partida {x}? '))
    total += gol
    carreira['partida'+str(x)] = gol
    gols.append(gol)
carreira['gols'] = gols
print('~-' * 20)
print(f'O jogador {carreira["jogador"]} jogou {partidas} partidas.')
print(f'Sua sequência de gols foi {gols}')
print('~-' * 20)
for k, v in carreira.items():
    cont += 1
    if cont > 2:
        print(f'Em {k}, {carreira["jogador"]} fez {v} gols.')
print(f'Total de gols: {total}')
print('~-' * 20)
print(carreira)

