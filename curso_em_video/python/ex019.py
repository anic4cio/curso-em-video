# import random
# a1 = input('Primeiro aluno: ')
# a2 = input('Segundo aluno: ')
# a3 = input('Terceiro aluno: ')
# a4 = input('Quarto aluno: ')
# sort = [a1, a2, a3, a4]
# ran = random.choice(sort)
# print('O aluno escolhido foi {}'.format(ran))
import random
from random import choice
# s1 = input('First student: ')
# s2 = input('Second student: ')
# s3 = input('Third student: ')
# s4 = input('Forth student: ')
# shutter = [s1, s2, s3, s4]
# sorter = random.choice(shutter)
# print('The target student is {}'.format(sorter))

bike = str(input('What is your next motorbike? '))
m1 = str(input('Another one: '))
m2 = str(input('Last bike that you want: '))
bs = [bike, m1, m2]
sort = random.choice(bs)
print('Your probably next moto is {}'.format(sort))
