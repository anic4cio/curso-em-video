"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""

fibo1 = 0
fibo2 = 1
ciclo = 0
termos = int(input('Digite quantos termos deseja mostrar: '))
while ciclo < termos:
    print(fibo1, end=' > ')
    fibo3 = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo3
    ciclo += 1
print('Fim')
