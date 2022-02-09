"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print(f' ~='*10, '\n', '       LOJAS KORTEZAN', '\n', '~= '*10)
nome_barato = ''
maisdemil = total = produtos = maisbarato = 0
while True:
    continuar = ' '
    nome_produto = str(input('Produto: '))
    preco = int(input('Preço: R$'))
    if produtos == 0 or preco < maisbarato:
        maisbarato = preco
        nome_barato = nome_produto
    if preco > 1000:
        maisdemil += 1
    produtos += 1
    total += preco
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Total de produtos: {produtos} \nTotal a pagar: R${total:.2f}')
print(f'Total de produtos acima de R$1000: {maisdemil}')
print(f'O produto mais barato foi {nome_barato}, custando {maisbarato}')
