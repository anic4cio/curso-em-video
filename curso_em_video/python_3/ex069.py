"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos
"""

pessoas = mais_18 = homens = mulher_20 = 0
while True:
    continuar = ' '
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        print('Programa encerrado!')
        break
print(f'Pessoas maiores de idade: {mais_18}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres abaixo dos 20: {mulher_20}')
