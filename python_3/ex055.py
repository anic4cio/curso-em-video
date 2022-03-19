"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos
"""

leves = 999
pesados = 0
for pesos in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if peso < leves:
        leves = peso
    if peso > pesados:
        pesados = peso
print('O maior peso de {} e o menor foi de {}'.format(pesados, leves))

#Método não gambiarrento

leves = 0
pesados = 0
for pesos in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if pesos == 1:
        leves = peso
        pesados = peso
    if peso < leves:
        leves = peso
    if peso > pesados:
        pesados = peso
print('O maior peso de {} e o menor foi de {}'.format(pesados, leves))