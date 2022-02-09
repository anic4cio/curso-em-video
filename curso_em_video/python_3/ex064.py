"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
"""

numero = 0
total = 0
ciclo = -1
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    total += numero
    ciclo += 1
total = total - 999
print('Você digitou {} números e a soma entre eles foi {}'.format(ciclo, total))
