"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores.
"""

opcao = str('')
total_numeros = media = soma = 0
while opcao != 'N':
    numero = int(input('Digite um número: '))
    if total_numeros == 0:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    total_numeros += 1
    soma += numero
    opcao = input('Deseja continuar? [S/N] ').upper()
media = soma / total_numeros
print('Você digitou {} números e a média foi {:.2f}'.format(total_numeros, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
