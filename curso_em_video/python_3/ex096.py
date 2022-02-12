"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as 
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
"""

def area(a, b):
    area = a * b
    print(f'O total da área com {a}m x {b}m é de {area:.2f}mts²')
    
l1 = float(input('Digite a primeira metragem: '))
l2 = float(input('Digite a segunda metragem: '))
area(l1, l2)
