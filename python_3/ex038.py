"""
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
Mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais
"""

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
if numero1 > numero2:
    print('O número {} é maior que o número {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é maior que o número {}'.format(numero2, numero1))
else:
    print('Os números são idênticos!')
