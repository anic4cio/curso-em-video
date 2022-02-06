from random import randint
tupla_random = (randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99), randint(0, 99))
print(tupla_random)
print('O maior valor na tupla foi {}.'.format(max(tupla_random)))
print('O menor valor na tupla foi {}.'.format(min(tupla_random)))
