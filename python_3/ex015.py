"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('Calcule o valor do aluguel do veículo.')
dia = int(input('Quantos dias ficou com o veículo? '))
km = float(input('Quantos quilômetros foram percorridos? '))
tot = (dia * 60) + (km * 0.15)
print('O total do aluguel do veículo foi de R${:.2f}'.format(tot))

