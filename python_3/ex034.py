"""
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite seu salário atual: '))
if salario <= 1250:
    reajuste_salarial = salario * 0.15
    print('Seu salário atual agora é R${}'.format(salario + reajuste_salarial))
else:
    reajuste_salarial = salario * 0.10
    print('Seu salário atual agora é de {} reais'.format(salario + reajuste_salarial))

