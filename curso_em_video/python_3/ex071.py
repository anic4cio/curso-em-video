"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('Saque seu dinheiro e esconda-o no colchão: ')
valor = int(input('Quanto deseja sacar? R$'))
cedula50 = valor // 50
cedula20 = (valor - (cedula50 * 50)) // 20
cedula10 = (valor - (cedula50 * 50 + cedula20 * 20)) // 10
cedula1 = (valor - (cedula50 * 50 + cedula20 * 20 + cedula10 * 10))
print(f'Para sacar R${valor} você receberá: ')
if cedula50 != 0:
    print(f'{cedula50} cédulas de R$50')
if cedula20 != 0:
    print(f'{cedula20} cédulas de R$20')
if cedula10 != 0:
    print(f'{cedula10} cédulas de R$10')
if cedula1 != 0:
    print(f'{cedula1} cédulas de R$1')
