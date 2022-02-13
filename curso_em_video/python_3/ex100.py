"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e 
a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint
def random_list(list):
    for x in range(0, 5):
        list.append(randint(0, 9))


def soma_pares(soma):
    for y in list:
        if y % 2 == 0:
            soma.append(y)


list = []
soma = []
random_list(list)
soma_pares(soma)
print('Os valores sorteados foram', end=': ')
print(*list, sep=", ", end='. \n')
print('Os valores pares dos números acima são: ', end='')
print(*soma, sep=', ', end='. \n')
print(f'A soma dos pares é {sum(soma)}')

