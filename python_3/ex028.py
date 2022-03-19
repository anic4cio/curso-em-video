"""
Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

import random
num = int(input('Tente adivinhar o número que vou pensar de 0 a 5: '))
escolha = random.choice([0, 1, 2, 3, 4, 5])
if num == escolha:
    print('PARABÉNS! VOCÊ ADIVINHOU! NÚMERO {}'.format(escolha))
elif num > 5:
    print('O número é de 0 a 5 meu brother.')
else:
    print('ERROU! Escolhi o número {}'.format(escolha))


