"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

lista = []
continuar = 'S'
while continuar == 'S':
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Este número já está na lista.')
    else:
        lista.append(numero)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
print(f'Os números da lista foram: {sorted(lista)}')
