"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times_a = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
           'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
           'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(50*'~=')
print(f'Os 5 primeiros são: {times_a[:5]}')
print(50*'~=')
print(f'Os 4 últimos são: {times_a[-4:]}')
print(50*'~=')
print(f'Times em ordem alfabética: {sorted(times_a)}')
print(50*'~=')
print('O Chapecoense está na {}ª posição'.format(times_a.index('Chapecoense')+1))
