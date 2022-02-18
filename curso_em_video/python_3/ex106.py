"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
Importante: use cores.
"""

cores = ('\033[m', '\033[30;41m', '\033[30;42m', '\033[30;43m', '\033[30;44m', '\033[30;45m', '\033[7;30m')

def titulo(texto, cor=0):
    tamanho = len(texto)
    print(cores[cor], end='')
    print('~' * tamanho)
    print(texto)
    print('~' * tamanho)
    print(cores[0], end='')


def pyhelp(item):
    titulo(f'Manual do comando.\'{item}\'', 4)
    print(cores[6], end='')
    help(item)
    print(cores[0], end='')

 
#Main
funcao = str(input('Digite a função que deseja ver a ajuda: '))
pyhelp(funcao)