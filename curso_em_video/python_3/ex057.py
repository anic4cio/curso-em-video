"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’
ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[1mDigite seu sexo: [M/F] \033[m')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('\033[31mDado inválido. Digite novamente.\033[m')
print('\033[32mSexo registrado com sucesso!\033[m')

