"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto 
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
Ex:
escreva('Olá, Mundo!') 
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
"""


def escreva(txt):
    tamanho = len(txt)
    print('~' * tamanho)
    print(f'{txt}')
    print('~' * tamanho)


while True:
    escreva(input('Digite sua frase para dar um print especial: '))
