"""
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = str(input('Digite seu nome completo: ')).title().strip().split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

#As vezes pode parecer inalcançavel e tem dias que não progredimos muito bem
#Mas não posso desanimar
#Tenho até os meus 30 anos, hoje tenho 23 e estamos no começo de 2022