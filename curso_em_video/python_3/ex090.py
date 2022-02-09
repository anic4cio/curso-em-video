"""
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também
a situação num dicionário. No final, mostre o conteúdo da estrutura na tela.
"""

dados = {'Nome': str(input('Nome do aluno: ')), 'Media': float(input('Média do aluno: '))}
if dados['Media'] < 5:
    dados['Situação'] = 'Reprovado'
elif dados['Media'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Aprovado'
print('~+' * 15)
for keys, values in dados.items():
    print(f'{keys} é {values}.')
