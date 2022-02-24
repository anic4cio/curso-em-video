"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas 
aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse 
módulo e use algumas dessas funções.
"""

import moeda 
valor = int(input('Digite um número e veja: '))
print(f'Dobro de {valor}: {moeda.dobro(valor)}')
print(f'Triplo de {valor}: {moeda.triplo(valor)}')
print(f'{valor} mais 10%: {moeda.porcentagem_mais(valor, 10)}')
print(f'{valor} menos 10%: {moeda.porcentagem_menos(valor, 10)}')
