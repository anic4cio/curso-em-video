# import random
# s1 = input('First student: ')
# s2 = input('Second student: ')
# s3 = input('Third student: ')
# s4 = input('Forth student: ')
# sort = [s1, s2, s3, s4]
# random.shuffle(sort)
# print(sort)

from random import shuffle
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Third name: '))
n4 = str(input('Forth nane: '))
sort = [n1, n2, n3, n4]
shuffle(sort)
print(sort)
