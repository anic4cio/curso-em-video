"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

from time import sleep
def contagem(inicio, fim, passo):
    if passo <= -1:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
    for x in range(inicio, fim, passo):
        print(x, end=' ', flush=True)
        sleep(.3)
    print('Fim!')
    sleep(.3)


contagem(0, 10, 1)
contagem(20, 0, 2)
print('Sua vez de contar!')
inicio = int(input('Número para iniciar a contagem: '))
fim = int(input('Número final da contagem: '))
passo = int(input('Passo da contagem: '))
contagem(inicio, fim, passo)
