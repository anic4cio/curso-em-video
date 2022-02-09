"""
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

dist = float(input('Quantos quilômetros foram percorridos na sua viagem? '))
if dist <= 200:
    dist = dist * 0.50
    print('O valor total da sua viagem foi de R${:.2f}'.format(dist))
else:
    dist = dist * 0.45
    print('O valor total da sua viagem com valor promocional foi R${:.2f}'.format(dist))

