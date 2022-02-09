"""
Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

#Jeito bruto
l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
hipo = (l1 ** 2 + l2 ** 2) ** 0.5
print('{:.2f}'.format(hipo))

#Jeito inteligente
from math import hypot
l1 = float(input('Digite um número: '))
l2 = float(input('Digite outro: '))
hipo = hypot(l1, l2)
print('{:.2f}'.format(hipo))
