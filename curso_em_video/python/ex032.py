# ano = str(input('Digite um ano e verifique se é bissexto: '))
# if ano[2:] == 00 and ano % 400 == 0:
#     print('Sim, o ano de {} é Bissexto!'.format(ano))
# if ano % 4 == 0:
#     print('{} é um ano bissexto!'.format(ano))
# else:
#     print('O ano {} não é bissexto.')

#O problema aqui é que eu não consigo usar str, float ou int com numeros usando a função de analisar texto [:]

#Era só fazer 100 resto da divisão igual a zero (100 % == 0)

from datetime import date
ano = int(input('Digite um ano e verifique se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim, o ano de {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
