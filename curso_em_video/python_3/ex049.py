"""
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

tabuada = int(input('Digite o número da tabuada desejado: '))
for multi in range(1, 11):
    print('{} X {:2} = {}'.format(tabuada, multi, (multi * tabuada)))
