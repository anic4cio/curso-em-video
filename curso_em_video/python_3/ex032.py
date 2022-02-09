"""
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date
ano = int(input('Digite um ano e verifique se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Sim, o ano de {ano} é Bissexto!')
else:
    print(f'O ano {ano} não é bissexto.')
