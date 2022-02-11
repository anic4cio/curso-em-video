"""
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

#ESSE EXERCÍCIO FOI KABULOSO, MAS FOI DAORA

lista = []
gols = []
jogadores = {}
while True:
    gols.clear()
    jogadores.clear()
    total = 0
    jogadores['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for bmw in range(1, partidas+1):
        gol = int(input(f'Quantos gols foram feitos na partida {bmw}? '))
        gols.append(gol)
        total += gol
    jogadores['gols'] = gols.copy()
    jogadores['total'] = total
    lista.append(jogadores.copy())    
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input('Erro. Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('~-' * 21)
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<15}{"Total":<5}')
print('~-' * 21)
contador = 1
for gs in lista:
    print(f'{contador:<5}{gs["nome"]:<15}{str(gs["gols"]):<15}{gs["total"]}')
    contador += 1
print('~-' * 21)
while True:
    mostrar = int(input('Digite o código do jogador para ver suas informações (Digite 999 para sair): '))
    if mostrar == 999:
        break    
    print('~-' * 21)
    print(f'Mostrando levantamento do jogador {lista[mostrar-1]["nome"]}')
    for x, t in enumerate (lista[mostrar-1]["gols"]):
        print(f'No jogo {x+1}, fez {t} gols')
print('~-' * 21)
print("ENCERRANDO...")

