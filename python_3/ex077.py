"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('Motard', 'Trilha', 'Liberdade', 'Realização', 'Perseverança', 'Satisfação', 'Conhecimento',
            'Programação', 'Tecnologia', 'Lifestyle')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')


