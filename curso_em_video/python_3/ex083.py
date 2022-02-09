"""
Exercício Python 083: Crie um programa onde o usuário
digite uma expressão qualquer que use parênteses. Seu
aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
"""

conta = str(input('Digite uma expressão matemática: '))
parenteses = []
for p in conta:
    if p == '(':
        parenteses.append(p)
    elif p == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(p)
if len(parenteses) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')

