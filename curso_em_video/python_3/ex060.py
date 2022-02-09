"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""

#Esse foi difícil, mas eu consegui
numero = int(input('Digite o número: '))
fatorial = 1
for numero in range(numero, 0, -1):
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' = ', end='')
    fatorial *= numero
print(fatorial)


