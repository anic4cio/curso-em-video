"""
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante, 
a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)
"""

def readint(numero):
    while numero not in '0123456789' or numero == '':
        print(f'\033[1;31;40m{"Erro! Digite um número inteiro válido."}\033[m')
        numero = input('Digite um número válido: ')
        if numero.isnumeric():
            break
    print(f'\033[1;34;40m{"Número aceito!"}\033[m')

valor = input('Digite seu número: ')
readint(valor)
