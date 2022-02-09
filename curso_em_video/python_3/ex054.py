"""
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
maiores = 0
menores = 0
for nascimetos in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano = date.today().year
    idade = ano - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Ao todos, foram {} maiores e {} menores.'.format(maiores, menores))
