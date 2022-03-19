"""
Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
print('\033[1;31mCONTAGEM REGRESSIVA PARA QUEIMA DE FOGOS!\033[m')
for contagem in range(10, 0, -1):
    print(contagem)
    sleep(0.7)
print('\033[1;33mFOGO!')
