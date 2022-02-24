"""
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.
"""

import moedav2
valor = int(input('Digite um valor: R$ '))
print(f'Dobro de R${valor}: {moedav2.dobro(valor)}')
print(f'Triplo de R${valor}: {moedav2.triplo(valor)}')
print(f'R${valor},00 menos 10%: {moedav2.porcentagem_menos(valor, 10)}')
print(f'R${valor},00 mais 10%: {moedav2.porcentagem_mais(valor, 10)}')
