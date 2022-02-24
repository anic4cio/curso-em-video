"""
Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

import moedav3
valor = int(input('Digite um valor: R$ '))
print(f'Dobro de R${valor}: {moedav3.dobro(valor,)}')
print(f'Triplo de R${valor}: {moedav3.triplo(valor,)}')
print(f'R${valor},00 mais 10%: {moedav3.porcentagem_mais(valor, 10,)}')
print(f'R${valor},00 menos 10%: {moedav3.porcentagem_menos(valor, 10,)}')
