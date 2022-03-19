"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = ''
while opcao != 5:
    print(5*'~-', 'MENU', 5*'~-')
    print('[1] - Somar valores')
    print('[2] - Multiplicar')
    print('[3] - Maior número')
    print('[4] - Inserir novos números')
    print('[5] - Sair')
    opcao = int(input('Digite a sua opção: '))
    if opcao == 1:
        print('A soma dos dois valores é: {}'.format(valor1 + valor2))
    if opcao == 2:
        print('{} x {} = {}'.format(valor1, valor2, valor1 * valor2))
    if opcao == 3:
        if valor1 > valor2:
            print('{} é maior que {}'.format(valor1, valor2))
        elif valor2 > valor1:
            print('{} é maior que {}'.format(valor2, valor1))
        else:
            print('Os valores são iguais.')
    if opcao == 4:
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
print('Programa encerrado.')
