str(print(f'\033[1;97;40m{"CORES DISPONÍVEIS":^40}\033[m'))
str(print(f'\033[1;30;107m{"Preto & Branco - [1]":^40}\033[m'))
str(print(f'\033[1;31;40m{"Vermelho - [2]":^40}\033[m'))
str(print(f'\033[1;33;40m{"Amarelo - [3]":^40}\033[m'))
str(print(f'\033[1;34;40m{"Azul - [4]":^40}\033[m'))
str(print(f'\033[1;35;40m{"Magenta - [5]":^40}\033[m'))
escolha_cor = input(f'\033[1;97;40m{"Escolha a cor desejada: ":^40}')
frase = str(input(f'{"Digite uma frase para colorir: ":^40}'))
cor = {'limpa': '\033[m', 'preto&branco': '\033[1;30;107m', 'vermelho': '\033[1;31;40m', 'amarelo': '\033[1;33;40m', 'azul': '\033[1;34;40m', 'magenta': '\033[1;35;40m'}
if escolha_cor == '1':
    print('{}{}{}'.format(cor['preto&branco'], frase, cor['limpa']))
if escolha_cor == '2':
    print('{}{}{}'.format(cor['vermelho'], frase, cor['limpa']))
if escolha_cor == '3':
    print('{}{}{}'.format(cor['amarelo'], frase, cor['limpa']))
if escolha_cor == '4':
    print('{}{}{}'.format(cor['azul'], frase, cor['limpa']))
if escolha_cor == '5':
    print('{}{}{}'.format(cor['magenta'], frase, cor['limpa']))


