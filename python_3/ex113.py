"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaint(inteiro):
    while True:
        try:
            inteiro = int(input('Digite um número inteiro: '))
            print(f'\033[92mO valor {inteiro} foi aceito!\033[m')

            break
        except ValueError:
            print('\033[31mErro. Você inseriu um dado inválido.\033[m')
    return inteiro

def leiafloat(real):
    while True:
        try:
            real = input('Digite um número: ').replace(',', '.')
            real = float(real)
            print(f'\033[92mO valor {real} foi aceito.\033[m')
            break
        except ValueError:
            print('\033[31mErro. Digite um número usando caracteres numéricos.\033[m')
    return real

leiafloat('Digite um número: ')
