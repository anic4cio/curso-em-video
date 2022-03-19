"""
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""

print('Soma de todos os números ímpares múltiplos de 3 até 500')
soma = 0
contador = 0
for numeros in range(1, 500, 2):
    if numeros % 3 == 0:
        soma += numeros
        contador += 1
print(soma)
print(contador)
