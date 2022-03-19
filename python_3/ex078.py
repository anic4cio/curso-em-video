"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

valores = []
for posicao in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {posicao}: ')))
print(f'O maior número digitado foi {max(valores)} nas posições: ', end='')
for v, n in enumerate(valores):
    if max(valores) == n:
        print(v, end='. ')
print()
print(f'O menor número digitado foi {min(valores)} nas posições: ', end='')
for v, n in enumerate(valores):
    if min(valores) == n:
        print(v, end='. ')
