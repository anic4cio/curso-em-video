"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""

from datetime import date
ano_nascimento = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
idade = ano - ano_nascimento
if idade == 18:
    print('Você está na maioridade e deve se alistar no serviço militar.')
elif idade < 18:
    print('Você ainda não tem idade suficiente para de alistar, faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Se você não se alistou há {} anos atrás, já passou da hora de se alistar.'.format(idade - 18))
