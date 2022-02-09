"""
Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice
s1 = input('First student: ')
s2 = input('Second student: ')
s3 = input('Third student: ')
s4 = input('Forth student: ')
shutter = [s1, s2, s3, s4]
sorter = choice(shutter)
print('The target student is {}'.format(sorter))

bike = str(input('What is your next motorbike? '))
m1 = str(input('Another one: '))
m2 = str(input('Last bike that you want: '))
bs = [bike, m1, m2]
sort = choice(bs)
print('Your probably next moto is {}'.format(sort))
