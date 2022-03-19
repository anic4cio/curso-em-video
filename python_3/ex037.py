"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
"""

numero = int(input('Digitr um número inteiro: '))
print("""Escolha umas das bases para conversão:
[1] - Converter para Binário
[2] - Converter para Octal
[3] - Coverter para Hexadecimal""")
escolha = int(input('Digite o número da opção desejada: '))
if escolha == 1:
    print('O número {} em Binário equivale a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} em Octal equivale a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} em Hexadecimal equivale a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')
