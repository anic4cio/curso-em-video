"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média
de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

lista = []
aluno = []
continuar = ''
while continuar != 'N':
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    lista.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print(f'N° NOME          MÉDIA   ')
for x in range(0, len(lista)):
    print(f'{x:<3}{lista[x][0]:<14}{(lista[x][1] + lista[x][2]) / 2:2.1f}')
while True:
    notas = int(input('Mostrar notas de qual aluno: (999 para sair) '))
    if notas == 999:
        break
    print(f'As notas de {lista[notas][0]} são {lista[notas][1:]}')