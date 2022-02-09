"""
Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velo = float(input('Qual velocidade você passou pelo radar: '))
if velo > 80:
    print('Você foi multado em R${:.2f} por dirigir acima da velocidade!'.format((velo - 80)*7))
else:
    print('Diriga com conciência, boa viagem!')

