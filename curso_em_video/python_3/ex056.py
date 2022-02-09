"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais
velho e quantas mulheres têm menos de 20 anos.
"""

media_idade = 0
idade_velho = 0
mulher_20 = 0
for x in range(0, 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    media_idade = idade + media_idade
    if sexo == 'M' and idade > idade_velho:
        nome_velho = nome
        idade_velho = idade
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
media_idade = media_idade / 4
print('A média de idade do grupo foi {} anos'.format(media_idade))
print('O nome do homem mais velho é {}, de {} anos.'.format(nome_velho, idade_velho))
print('{} mulheres tem menos de 20 anos'.format(mulher_20))
