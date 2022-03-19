"""
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Ângulo: {:.2g} \nSeno: {:.2g} \nCosseno: {:.2g} \nTangente: {:.2g} \n'.format(ang, sen, cos, tan))
